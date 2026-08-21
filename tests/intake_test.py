import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name, module_name):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / "scripts" / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


drive = load_script("drive-inbox-intake.py", "drive_inbox_intake")


class IntakeTests(unittest.TestCase):
    def test_project_classification(self):
        self.assertEqual(drive.project_for("00 - inbox/temp", "Content plan.xlsx"), "content-os")
        self.assertEqual(drive.project_for("00 - inbox/temp", "Conuent plan.xlsx", "content calendar workflow"), "content-os")
        self.assertEqual(drive.project_for("00 - inbox", "DDP logic.pdf"), "svmpx")
        self.assertEqual(drive.project_for("00 - inbox/refs", "unknown.pdf"), "shared")

    def test_incremental_fingerprint_is_stable(self):
        item = {"id": "abc", "version": "4", "modifiedTime": "2026-08-21T00:00:00Z", "size": "10", "mimeType": "text/plain"}
        self.assertEqual(drive.fingerprint(item), drive.fingerprint(dict(item)))
        self.assertNotEqual(drive.fingerprint(item), drive.fingerprint(dict(item, version="5")))

    def test_note_review_and_materialization(self):
        with tempfile.TemporaryDirectory() as staging_value, tempfile.TemporaryDirectory() as repo_value:
            staging = Path(staging_value)
            repo = Path(repo_value)
            command = [sys.executable, str(ROOT / "scripts" / "manage-intake.py")]
            staged = subprocess.run(command + ["stage-note", "--staging", str(staging), "--project", "shared", "--title", "Test note", "--text", "Safe text"], check=True, capture_output=True, text=True)
            intake_id = json.loads(staged.stdout)["intake_id"]
            subprocess.run(command + ["approve", "--staging", str(staging), "--id", intake_id], check=True)
            subprocess.run(command + ["materialize", "--staging", str(staging), "--repo", str(repo), "--id", intake_id], check=True)
            files = sorted(repo.rglob("*.md"))
            self.assertEqual(len(files), 2)
            combined = "\n".join(path.read_text(encoding="utf-8") for path in files)
            self.assertIn("canonical: false", combined)
            self.assertIn("status: draft", combined)
            self.assertIn("status: active", combined)


if __name__ == "__main__":
    unittest.main()
