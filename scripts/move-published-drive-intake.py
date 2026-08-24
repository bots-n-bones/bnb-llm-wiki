#!/usr/bin/env python3
"""Move canonically published Drive sources from Inbox to reviewed project folders."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

CANONICAL_ROOT_ID = "1VfCO8UnD0Qq4D6k-f-HTk7ELgy9j0XOg"
INBOX_FOLDER_ID = "10Xg3r5UUCygMiSWpog3z4Vima-b2a85N"
PROJECTS_FOLDER_ID = "1irV6M-FwMH-KHNAtDw5xHX5ioHgwTlgd"
DEFAULT_STAGING = Path("/opt/data/knowledge-intake")
DEFAULT_TOKEN = Path("/opt/data/google_token.json")
DEFAULT_DESTINATIONS = Path(__file__).resolve().parents[1] / "config" / "drive-project-destinations.json"
GOOGLE_TOKEN_URI = "https://oauth2.googleapis.com/token"
REQUIRED_DRIVE_SCOPE = "https://www.googleapis.com/auth/drive"


class PolicyError(ValueError):
    """A permanent scope/configuration failure that must not be retried blindly."""


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def atomic_json(path: Path, payload: dict) -> None:
    owner = path.stat() if path.exists() else path.parent.stat()
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    os.chmod(temporary, 0o600)
    if os.geteuid() == 0:
        os.chown(temporary, owner.st_uid, owner.st_gid)
    os.replace(temporary, path)


def load_destination_map(path: Path) -> dict[str, str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != "hermes-kb-drive-destinations/v1":
        raise PolicyError("destination map schema is invalid")
    if payload.get("canonical_root_id") != CANONICAL_ROOT_ID:
        raise PolicyError("destination map canonical root is invalid")
    if payload.get("inbox_folder_id") != INBOX_FOLDER_ID:
        raise PolicyError("destination map Inbox is invalid")
    if payload.get("projects_folder_id") != PROJECTS_FOLDER_ID:
        raise PolicyError("destination map projects root is invalid")
    projects = payload.get("projects")
    if not isinstance(projects, dict):
        raise PolicyError("destination project map is invalid")
    return {str(project): str(folder_id) for project, folder_id in projects.items() if folder_id}


def sanitize_error(error: Exception) -> str:
    text = re.sub(r"(?i)(access_token|refresh_token|client_secret|authorization)\s*[:=]\s*\S+", r"\1=[redacted]", str(error))
    return text.replace("\n", " ")[:500]


def validate_token_config(token: dict) -> None:
    if token.get("token_uri") != GOOGLE_TOKEN_URI:
        raise PolicyError("OAuth token endpoint is not the approved Google endpoint")
    if REQUIRED_DRIVE_SCOPE not in (token.get("scopes") or []):
        raise PolicyError("OAuth credential lacks required Drive write scope")
    for field in ("client_id", "client_secret", "refresh_token"):
        if not isinstance(token.get(field), str) or not token[field]:
            raise PolicyError(f"OAuth credential is missing {field}")


class DriveRestClient:
    def __init__(self, token_path: Path):
        token = json.loads(token_path.read_text(encoding="utf-8"))
        validate_token_config(token)
        request = urllib.request.Request(
            GOOGLE_TOKEN_URI,
            data=urllib.parse.urlencode({
                "client_id": token["client_id"],
                "client_secret": token["client_secret"],
                "refresh_token": token["refresh_token"],
                "grant_type": "refresh_token",
            }).encode(),
            headers={"Accept": "application/json", "User-Agent": "Hermes-KB-Drive-Mover"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            refreshed = json.loads(response.read().decode("utf-8"))
        self.access_token = refreshed["access_token"]

    def request(self, url: str, *, method: str = "GET", body: bytes | None = None) -> dict:
        request = urllib.request.Request(
            url,
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {self.access_token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "Hermes-KB-Drive-Mover",
            },
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))

    def get_file(self, file_id: str) -> dict:
        fields = urllib.parse.quote("id,name,mimeType,parents,trashed,webViewLink", safe=",")
        return self.request(f"https://www.googleapis.com/drive/v3/files/{urllib.parse.quote(file_id, safe="")}?fields={fields}&supportsAllDrives=true")

    def is_descendant(self, folder_id: str, ancestor_id: str) -> bool:
        pending = [folder_id]
        seen = set()
        while pending and len(seen) < 256:
            current = pending.pop()
            if current == ancestor_id:
                return True
            if current in seen:
                continue
            seen.add(current)
            metadata = self.get_file(current)
            pending.extend(metadata.get("parents") or [])
        return False

    def move_file(self, file_id: str, add_parent: str, remove_parents: list[str]) -> dict:
        query = urllib.parse.urlencode({
            "addParents": add_parent,
            "removeParents": ",".join(remove_parents),
            "supportsAllDrives": "true",
            "fields": "id,parents,webViewLink",
        })
        return self.request(
            f"https://www.googleapis.com/drive/v3/files/{urllib.parse.quote(file_id, safe="")}?{query}",
            method="PATCH",
            body=b"{}",
        )


def move_one(drive, item: dict, destinations: dict[str, str], *, now_value: str | None = None) -> dict:
    if item.get("status") != "published-canonical":
        raise PolicyError("intake is not published canonical")
    file_id = item.get("drive_file_id")
    if not file_id:
        raise PolicyError("intake is not a Drive source")
    project = item.get("project")
    destination = destinations.get(str(project))
    if not destination:
        raise PolicyError("project destination is not configured")
    if not drive.is_descendant(destination, CANONICAL_ROOT_ID):
        raise PolicyError("project destination is outside canonical root")
    if not drive.is_descendant(destination, PROJECTS_FOLDER_ID):
        raise PolicyError("project destination is outside canonical projects root")

    metadata = drive.get_file(str(file_id))
    if metadata.get("trashed"):
        raise PolicyError("source file is trashed")
    parents = [str(value) for value in metadata.get("parents") or []]
    attempts = int((item.get("drive_move") or {}).get("attempts") or 0) + 1
    timestamp = now_value or now()
    if parents == [destination]:
        receipt = {
            "status": "moved", "moved_at": timestamp, "attempts": attempts,
            "already_at_destination": True, "from_parent_ids": parents,
            "to_folder_id": destination, "returned_parent_ids": parents,
        }
        item["drive_move"] = receipt
        return receipt
    if len(parents) != 1:
        raise PolicyError("source file must have exactly one current parent")
    if not drive.is_descendant(parents[0], INBOX_FOLDER_ID):
        raise PolicyError("source file is outside canonical Inbox")

    returned = drive.move_file(str(file_id), destination, parents)
    returned_parents = [str(value) for value in returned.get("parents") or []]
    if returned_parents != [destination]:
        raise RuntimeError("Drive returned unexpected parents after move")
    receipt = {
        "status": "moved", "moved_at": timestamp, "attempts": attempts,
        "already_at_destination": False, "from_parent_ids": parents,
        "to_folder_id": destination, "returned_parent_ids": returned_parents,
        "web_view_link": returned.get("webViewLink") or metadata.get("webViewLink") or (item.get("source") or {}).get("url"),
    }
    item["drive_move"] = receipt
    return receipt


def process_pending(staging: Path, drive, destinations: dict[str, str], *, now_value: str | None = None) -> dict:
    summary = {"moved": 0, "blocked": 0, "failed": 0, "skipped": 0, "events": []}
    pending = staging / "pending"
    staging_resolved = staging.resolve()
    if staging.is_symlink() or pending.is_symlink() or not pending.is_dir():
        raise PolicyError("intake pending directory is unavailable")
    pending_resolved = pending.resolve()
    if pending_resolved.parent != staging_resolved or pending_resolved.name != "pending":
        raise PolicyError("intake pending directory is outside staging root")
    for path in sorted(pending.glob("*.json")):
        if path.is_symlink() or not path.is_file() or path.resolve().parent != pending_resolved:
            raise PolicyError(f"unsafe intake package path: {path.name}")
        try:
            item = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise RuntimeError(f"intake package cannot be parsed: {path.name}: {sanitize_error(error)}") from error
        if item.get("status") != "published-canonical" or not item.get("drive_file_id"):
            summary["skipped"] += 1
            continue
        prior = item.get("drive_move") or {}
        if prior.get("status") in {"moved", "blocked"}:
            summary["skipped"] += 1
            continue
        timestamp = now_value or now()
        attempts = int(prior.get("attempts") or 0) + 1
        try:
            receipt = move_one(drive, item, destinations, now_value=timestamp)
            summary["moved"] += 1
            summary["events"].append({"intake_id": item.get("intake_id"), "status": "moved", "to_folder_id": receipt["to_folder_id"]})
        except PolicyError as error:
            item["drive_move"] = {"status": "blocked", "blocked_at": timestamp, "attempts": attempts, "error": sanitize_error(error)}
            summary["blocked"] += 1
            summary["events"].append({"intake_id": item.get("intake_id"), "status": "blocked", "error": sanitize_error(error)})
        except Exception as error:
            item["drive_move"] = {"status": "retryable-failed", "failed_at": timestamp, "attempts": attempts, "error": sanitize_error(error)}
            summary["failed"] += 1
            summary["events"].append({"intake_id": item.get("intake_id"), "status": "retryable-failed", "error": sanitize_error(error)})
        atomic_json(path, item)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staging", type=Path, default=DEFAULT_STAGING)
    parser.add_argument("--token", type=Path, default=DEFAULT_TOKEN)
    parser.add_argument("--destinations", type=Path, default=DEFAULT_DESTINATIONS)
    args = parser.parse_args()
    try:
        destinations = load_destination_map(args.destinations)
        drive = DriveRestClient(args.token)
        summary = process_pending(args.staging, drive, destinations)
    except Exception as error:
        print(json.dumps({"status": "worker-failed", "error": sanitize_error(error)}, ensure_ascii=False))
        return 1
    if summary["moved"] or summary["blocked"] or summary["failed"]:
        print(json.dumps(summary, ensure_ascii=False))
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
