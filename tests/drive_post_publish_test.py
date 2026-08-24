import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(relative, module_name):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


publisher = load_script("scripts/publish-canonical-candidates.py", "canonical_publisher")
mover = load_script("scripts/move-published-drive-intake.py", "drive_post_publish")


class FakeDrive:
    def __init__(self, files, ancestry):
        self.files = files
        self.ancestry = ancestry
        self.moves = []

    def get_file(self, file_id):
        return dict(self.files[file_id])

    def is_descendant(self, folder_id, ancestor_id):
        return self.ancestry.get((folder_id, ancestor_id), False)

    def move_file(self, file_id, add_parent, remove_parents):
        self.moves.append((file_id, add_parent, tuple(remove_parents)))
        self.files[file_id] = {**self.files[file_id], "parents": [add_parent]}
        return dict(self.files[file_id])


class DrivePostPublishTests(unittest.TestCase):
    def drive_item(self):
        return {
            "intake_id": "drive-file-1",
            "drive_file_id": "file-1",
            "project": "hermes",
            "status": "approved-for-canonical-promotion",
            "source": {
                "url": "https://drive.google.com/file/d/file-1/view",
                "original_path": "00 - inbox/source.pdf",
                "parent_ids": [mover.INBOX_FOLDER_ID],
            },
        }

    def test_release_result_is_written_only_after_all_intakes_are_finalized(self):
        with tempfile.TemporaryDirectory() as temporary:
            candidate = Path(temporary)
            intake_a = candidate / "a.json"
            intake_b = candidate / "b.json"
            writes = []
            intake_map = {
                "a": (intake_a, {"intake_id": "a", "drive_file_id": "file-a"}),
                "b": (intake_b, {"intake_id": "b"}),
            }
            result = {"status": "published", "published_at": "2026-08-24T04:00:00Z", "release_commit": "3" * 40}
            publisher.finalize_release_state(
                candidate,
                {"intake_ids": ["a", "b"]},
                intake_map,
                result,
                writer=lambda path, payload: writes.append((path.name, payload.get("status"))),
            )
            self.assertEqual(writes, [
                ("a.json", "published-canonical"),
                ("b.json", "published-canonical"),
                ("release-result.json", "published"),
            ])

    def test_publisher_enqueues_drive_move_without_rewriting_provenance(self):
        item = self.drive_item()
        original_source = json.loads(json.dumps(item["source"]))
        publisher.mark_published_intake(item, {
            "published_at": "2026-08-24T04:00:00Z",
            "release_commit": "a" * 40,
        })
        self.assertEqual(item["status"], "published-canonical")
        self.assertEqual(item["drive_move"]["status"], "pending")
        self.assertEqual(item["source"], original_source)

    def test_publisher_does_not_enqueue_message_source(self):
        item = {"intake_id": "message-1", "project": "hermes"}
        publisher.mark_published_intake(item, {
            "published_at": "2026-08-24T04:00:00Z",
            "release_commit": "b" * 40,
        })
        self.assertEqual(item["status"], "published-canonical")
        self.assertNotIn("drive_move", item)

    def test_worker_moves_only_from_inbox_to_allowlisted_project(self):
        item = self.drive_item()
        publisher.mark_published_intake(item, {
            "published_at": "2026-08-24T04:00:00Z",
            "release_commit": "c" * 40,
        })
        drive = FakeDrive(
            {"file-1": {"id": "file-1", "parents": ["nested-inbox"], "webViewLink": item["source"]["url"]}},
            {
                ("nested-inbox", mover.INBOX_FOLDER_ID): True,
                ("hermes-folder", mover.CANONICAL_ROOT_ID): True,
                ("hermes-folder", mover.PROJECTS_FOLDER_ID): True,
            },
        )
        result = mover.move_one(drive, item, {"hermes": "hermes-folder"}, now_value="2026-08-24T04:01:00Z")
        self.assertEqual(result["status"], "moved")
        self.assertEqual(drive.moves, [("file-1", "hermes-folder", ("nested-inbox",))])
        self.assertEqual(item["source"]["original_path"], "00 - inbox/source.pdf")
        self.assertEqual(item["source"]["url"], "https://drive.google.com/file/d/file-1/view")

    def test_worker_refuses_unpublished_intake(self):
        item = self.drive_item()
        drive = FakeDrive({}, {})
        with self.assertRaisesRegex(ValueError, "not published canonical"):
            mover.move_one(drive, item, {"hermes": "hermes-folder"})
        self.assertEqual(drive.moves, [])

    def test_worker_refuses_source_outside_inbox(self):
        item = self.drive_item()
        publisher.mark_published_intake(item, {"published_at": "2026-08-24T04:00:00Z", "release_commit": "d" * 40})
        drive = FakeDrive(
            {"file-1": {"id": "file-1", "parents": ["outside"]}},
            {
                ("hermes-folder", mover.CANONICAL_ROOT_ID): True,
                ("hermes-folder", mover.PROJECTS_FOLDER_ID): True,
            },
        )
        with self.assertRaisesRegex(ValueError, "outside canonical Inbox"):
            mover.move_one(drive, item, {"hermes": "hermes-folder"})
        self.assertEqual(drive.moves, [])

    def test_worker_refuses_destination_outside_canonical_root(self):
        item = self.drive_item()
        publisher.mark_published_intake(item, {"published_at": "2026-08-24T04:00:00Z", "release_commit": "e" * 40})
        drive = FakeDrive(
            {"file-1": {"id": "file-1", "parents": ["nested-inbox"]}},
            {("nested-inbox", mover.INBOX_FOLDER_ID): True},
        )
        with self.assertRaisesRegex(ValueError, "outside canonical root"):
            mover.move_one(drive, item, {"hermes": "hermes-folder"})
        self.assertEqual(drive.moves, [])

    def test_worker_requires_configured_project_destination(self):
        item = self.drive_item()
        publisher.mark_published_intake(item, {"published_at": "2026-08-24T04:00:00Z", "release_commit": "f" * 40})
        drive = FakeDrive({"file-1": {"id": "file-1", "parents": ["nested-inbox"]}}, {})
        with self.assertRaisesRegex(ValueError, "destination is not configured"):
            mover.move_one(drive, item, {})
        self.assertEqual(drive.moves, [])

    def test_worker_retry_is_idempotent_when_already_at_destination(self):
        item = self.drive_item()
        publisher.mark_published_intake(item, {"published_at": "2026-08-24T04:00:00Z", "release_commit": "1" * 40})
        drive = FakeDrive(
            {"file-1": {"id": "file-1", "parents": ["hermes-folder"]}},
            {
                ("hermes-folder", mover.CANONICAL_ROOT_ID): True,
                ("hermes-folder", mover.PROJECTS_FOLDER_ID): True,
            },
        )
        result = mover.move_one(drive, item, {"hermes": "hermes-folder"}, now_value="2026-08-24T04:02:00Z")
        self.assertEqual(result["status"], "moved")
        self.assertTrue(result["already_at_destination"])
        self.assertEqual(drive.moves, [])

    def test_token_config_rejects_non_google_token_endpoint(self):
        token = {
            "token_uri": "https://attacker.invalid/token",
            "client_id": "client",
            "client_secret": "secret",
            "refresh_token": "refresh",
            "scopes": [mover.REQUIRED_DRIVE_SCOPE],
        }
        with self.assertRaisesRegex(ValueError, "token endpoint"):
            mover.validate_token_config(token)

    def test_token_config_requires_full_drive_scope(self):
        token = {
            "token_uri": mover.GOOGLE_TOKEN_URI,
            "client_id": "client",
            "client_secret": "secret",
            "refresh_token": "refresh",
            "scopes": ["https://www.googleapis.com/auth/drive.readonly"],
        }
        with self.assertRaisesRegex(ValueError, "Drive write scope"):
            mover.validate_token_config(token)

    def test_drive_rest_urls_escape_file_ids_as_single_path_segments(self):
        client = mover.DriveRestClient.__new__(mover.DriveRestClient)
        captured = []
        client.request = lambda url, **kwargs: captured.append(url) or {"id": "ok", "parents": ["dest"]}
        client.get_file("folder/../../outside")
        client.move_file("folder/../../outside", "dest", ["source"])
        self.assertEqual(len(captured), 2)
        for url in captured:
            self.assertIn("folder%2F..%2F..%2Foutside", url)
            self.assertNotIn("folder/../../outside", url)

    def test_worker_rejects_symlinked_pending_directory(self):
        with tempfile.TemporaryDirectory() as temporary, tempfile.TemporaryDirectory() as outside:
            staging = Path(temporary)
            (staging / "pending").symlink_to(Path(outside), target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "pending directory"):
                mover.process_pending(staging, FakeDrive({}, {}), {})

    def test_worker_rejects_symlinked_intake_package(self):
        with tempfile.TemporaryDirectory() as temporary, tempfile.TemporaryDirectory() as outside:
            staging = Path(temporary)
            pending = staging / "pending"
            pending.mkdir()
            target = Path(outside) / "outside.json"
            target.write_text("{}", encoding="utf-8")
            (pending / "linked.json").symlink_to(target)
            with self.assertRaisesRegex(ValueError, "unsafe intake package path"):
                mover.process_pending(staging, FakeDrive({}, {}), {})

    def test_worker_fails_closed_when_pending_directory_is_missing(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(ValueError, "pending directory"):
                mover.process_pending(Path(temporary), FakeDrive({}, {}), {})

    def test_worker_fails_closed_on_malformed_intake_package(self):
        with tempfile.TemporaryDirectory() as temporary:
            pending = Path(temporary) / "pending"
            pending.mkdir()
            (pending / "broken.json").write_text("{not-json", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "cannot be parsed"):
                mover.process_pending(Path(temporary), FakeDrive({}, {}), {})

    def test_processing_failure_keeps_canonical_status_and_continues(self):
        with tempfile.TemporaryDirectory() as temporary:
            staging = Path(temporary)
            pending = staging / "pending"
            pending.mkdir()
            bad = self.drive_item()
            good = {**self.drive_item(), "intake_id": "drive-file-2", "drive_file_id": "file-2"}
            for item in (bad, good):
                publisher.mark_published_intake(item, {"published_at": "2026-08-24T04:00:00Z", "release_commit": "2" * 40})
                (pending / f'{item["intake_id"]}.json').write_text(json.dumps(item), encoding="utf-8")
            drive = FakeDrive(
                {
                    "file-1": {"id": "file-1", "parents": ["outside"]},
                    "file-2": {"id": "file-2", "parents": ["nested-inbox"]},
                },
                {
                    ("nested-inbox", mover.INBOX_FOLDER_ID): True,
                    ("hermes-folder", mover.CANONICAL_ROOT_ID): True,
                    ("hermes-folder", mover.PROJECTS_FOLDER_ID): True,
                },
            )
            summary = mover.process_pending(staging, drive, {"hermes": "hermes-folder"}, now_value="2026-08-24T04:03:00Z")
            bad_saved = json.loads((pending / "drive-file-1.json").read_text())
            good_saved = json.loads((pending / "drive-file-2.json").read_text())
            self.assertEqual(bad_saved["status"], "published-canonical")
            self.assertEqual(bad_saved["drive_move"]["status"], "blocked")
            self.assertEqual(good_saved["drive_move"]["status"], "moved")
            self.assertEqual(summary["moved"], 1)
            self.assertEqual(summary["blocked"], 1)


if __name__ == "__main__":
    unittest.main()
