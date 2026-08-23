#!/usr/bin/env python3
"""Publish owner-approved canonical release requests through the root worker."""

from __future__ import annotations

import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(os.environ.get(
    "HERMES_KNOWLEDGE_HOST_REPO",
    "/var/lib/docker/volumes/hermes-codex-workspace_hermes-knowledge/_data/bnb-llm-wiki",
)).resolve()
TASKS = Path(os.environ.get(
    "HERMES_WORKSPACE_TASKS_ROOT",
    "/var/lib/docker/volumes/hermes-codex-workspace_hermes-workspace-files/_data/files/tasks",
)).resolve()
STAGING = Path(os.environ.get(
    "HERMES_KNOWLEDGE_STAGING_HOST",
    "/var/lib/docker/volumes/hermes-codex-workspace_hermes-agent-data/_data/knowledge-intake",
)).resolve()
DEPLOY_KEY = Path(os.environ.get("BNB_WIKI_DEPLOY_KEY", "/root/.ssh/bnb-wiki-deploy")).resolve()
VALIDATOR_IMAGE = os.environ.get("BNB_WIKI_VALIDATOR_IMAGE", "hermes-codex-workspace:server")
REQUEST_SCHEMA = "hermes-kb-canonical-release/v1"
ALLOWED_INTAKE_STATUSES = {
    "approved-for-canonical-promotion",
    "materialized-canonical-candidate",
    "published-canonical",
}
SAFE_PATH = re.compile(
    r"^projects/(svmpx|hello-i-am|content-os|bots-n-bones|quntm|ursus|shared)/"
    r"(00-canon|01-knowledge|02-decisions|03-sops|04-source-register)/.+\.md$"
)
COMMIT = re.compile(r"^[0-9a-f]{40}$")


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run(args: list[str], *, cwd: Path | None = None, capture: bool = False) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
        env={
            **os.environ,
            "GIT_SSH_COMMAND": (
                f"ssh -i {DEPLOY_KEY} -o IdentitiesOnly=yes "
                "-o StrictHostKeyChecking=accept-new"
            ),
        },
    )
    return result.stdout.strip() if capture else ""


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.stat() if path.exists() else None
    owner = existing or path.parent.stat()
    mode = stat.S_IMODE(existing.st_mode) if existing else 0o644
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    os.chmod(temporary, mode)
    if os.geteuid() == 0:
        os.chown(temporary, owner.st_uid, owner.st_gid)
    os.replace(temporary, path)


def load_intakes() -> dict[str, tuple[Path, dict]]:
    found: dict[str, tuple[Path, dict]] = {}
    for path in (STAGING / "pending").glob("*.json"):
        try:
            item = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for key in (item.get("intake_id"), item.get("drive_file_id")):
            if key:
                found[str(key)] = (path, item)
    return found


def safe_candidate_file(candidate: Path, relative: str) -> Path:
    if not SAFE_PATH.fullmatch(relative):
        raise ValueError(f"unsafe release path: {relative}")
    source = (candidate / relative).resolve()
    if candidate not in source.parents or not source.is_file() or source.is_symlink():
        raise ValueError(f"candidate file is unavailable: {relative}")
    if source.stat().st_size > 1_000_000:
        raise ValueError(f"candidate file is too large: {relative}")
    text = source.read_text(encoding="utf-8")
    required = ("schema: hermes-kb/v2", "status: active", "owner: ilya")
    if any(field not in text for field in required):
        raise ValueError(f"required canonical metadata missing: {relative}")
    if "/04-source-register/" in f"/{relative}":
        if "type: source-record" not in text or "canonical: false" not in text:
            raise ValueError(f"invalid source record: {relative}")
    elif "canonical: true" not in text or "source_ids:" not in text:
        raise ValueError(f"invalid canonical page: {relative}")
    return source


def git_output(repo: Path, *args: str) -> str:
    return run(["git", "-c", f"safe.directory={repo}", "-C", str(repo), *args], capture=True)


def base_bytes(base: str, relative: str) -> bytes | None:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "show", f"{base}:{relative}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return result.stdout if result.returncode == 0 else None


def validate_request(request_path: Path, intake_map: dict[str, tuple[Path, dict]]) -> tuple[dict, Path, list[str]]:
    request = json.loads(request_path.read_text(encoding="utf-8"))
    if request.get("schema") != REQUEST_SCHEMA or request.get("status") != "approved":
        raise ValueError("release request is not owner-approved")
    if request.get("approved_by") != "ilya":
        raise ValueError("release request approver must be ilya")
    base = str(request.get("base_commit") or "")
    candidate_commit = str(request.get("candidate_commit") or "")
    if not COMMIT.fullmatch(base) or not COMMIT.fullmatch(candidate_commit):
        raise ValueError("release request commit IDs are invalid")
    candidate = request_path.parent.resolve()
    if git_output(candidate, "rev-parse", "HEAD") != candidate_commit:
        raise ValueError("candidate HEAD does not match release request")
    status_lines = git_output(candidate, "status", "--porcelain", "--untracked-files=all").splitlines()
    dirty = [
        line for line in status_lines
        if line[3:] not in {"release-request.json", "release-result.json"}
    ]
    if dirty:
        raise ValueError("candidate repository is not clean")
    files = request.get("files")
    if not isinstance(files, list) or not 1 <= len(files) <= 30 or len(files) != len(set(files)):
        raise ValueError("release request file list is invalid")
    for relative in files:
        if not isinstance(relative, str):
            raise ValueError("release request file path is invalid")
        safe_candidate_file(candidate, relative)
    intake_ids = request.get("intake_ids")
    if not isinstance(intake_ids, list) or not intake_ids:
        raise ValueError("release request must reference reviewed intake")
    for intake_id in intake_ids:
        match = intake_map.get(str(intake_id))
        if not match or match[1].get("status") not in ALLOWED_INTAKE_STATUSES:
            raise ValueError(f"intake is not approved for canonical promotion: {intake_id}")
    return request, candidate, files


def publish(request_path: Path, intake_map: dict[str, tuple[Path, dict]]) -> dict:
    request, candidate, files = validate_request(request_path, intake_map)
    base = request["base_commit"]
    run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "fetch", "origin", "main"])
    run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "reset", "--hard", "origin/main"])
    try:
        for relative in files:
            source = safe_candidate_file(candidate, relative)
            target = (ROOT / relative).resolve()
            candidate_data = source.read_bytes()
            current_data = target.read_bytes() if target.is_file() else None
            if current_data == candidate_data:
                continue
            original_data = base_bytes(base, relative)
            if current_data != original_data:
                raise ValueError(f"release conflict against current main: {relative}")
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as handle:
                handle.write(candidate_data)
                temporary = Path(handle.name)
            os.chmod(temporary, 0o644)
            os.replace(temporary, target)

        run([
            "docker", "run", "--rm", "--entrypoint", "/bin/sh",
            "-v", f"{ROOT}:/repo", "-w", "/repo", VALIDATOR_IMAGE,
            "-lc", "npm ci >/dev/null && npm run validate",
        ])
        run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "add", "--", *files])
        staged = subprocess.run(
            ["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "diff", "--cached", "--quiet"]
        )
        if staged.returncode != 0:
            message = str(request.get("commit_message") or "knowledge: publish approved canonical material")[:120]
            run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "config", "user.name", "Hermes Knowledge Bot"])
            run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "config", "user.email", "bots-n-bones@users.noreply.github.com"])
            run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "commit", "-m", message])
            run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "push", "origin", "HEAD:main"])
        release_commit = git_output(ROOT, "rev-parse", "HEAD")
        run(["/bin/sh", str(ROOT / "scripts" / "sync-server-release.sh"), str(ROOT)])
        run(["/bin/sh", str(ROOT / "scripts" / "refresh-workspace-knowledge-index.sh")])
        result = {
            "schema": "hermes-kb-canonical-release-result/v1",
            "status": "published",
            "published_at": now(),
            "release_commit": release_commit,
            "files": files,
        }
        atomic_json(candidate / "release-result.json", result)
        for intake_id in request["intake_ids"]:
            path, item = intake_map[str(intake_id)]
            item["status"] = "published-canonical"
            item["canonical_published_at"] = result["published_at"]
            item["canonical_release_commit"] = release_commit
            atomic_json(path, item)
        return result
    except Exception:
        run(["git", "-c", f"safe.directory={ROOT}", "-C", str(ROOT), "reset", "--hard", "origin/main"])
        raise


def main() -> int:
    if not ROOT.joinpath(".git").is_dir() or not DEPLOY_KEY.is_file():
        raise SystemExit("release worker prerequisites are unavailable")
    intake_map = load_intakes()
    requests = sorted(TASKS.glob("kb-publication-*/bnb-llm-wiki-release-candidate/release-request.json"))
    summary = []
    for request_path in requests:
        result_path = request_path.with_name("release-result.json")
        if result_path.exists():
            try:
                if json.loads(result_path.read_text(encoding="utf-8")).get("status") == "published":
                    continue
            except (OSError, json.JSONDecodeError):
                pass
        try:
            summary.append({"request": str(request_path), **publish(request_path, intake_map)})
        except Exception as error:
            failure = {
                "schema": "hermes-kb-canonical-release-result/v1",
                "status": "failed",
                "failed_at": now(),
                "error": str(error),
            }
            atomic_json(request_path.with_name("release-result.json"), failure)
            print(json.dumps({"request": str(request_path), **failure}, ensure_ascii=False), file=sys.stderr)
            return 1
    print(json.dumps({"processed": summary}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
