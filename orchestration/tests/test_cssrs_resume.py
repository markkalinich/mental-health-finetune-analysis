#!/usr/bin/env python3
"""C-SSRS resume must not treat an HTTP error as a finished empty reply."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from orchestration.run_cssrs_bench import load_completed  # noqa: E402


class CssrsResumeTests(unittest.TestCase):
    def test_api_error_is_not_finished(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            row = {
                "item_id": "u089",
                "standard_label": "Indicator",
                "pred_label": "",
                "status": 'api_error:API request failed with status 400: {"error":{"message":"System role not supported"}}',
                "raw_response": "",
            }
            (out / "predictions.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            self.assertEqual(load_completed(out), {})

    def test_later_success_replaces_an_api_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            failed = {
                "item_id": "u089",
                "status": "api_error:HTTP 400",
                "raw_response": "",
            }
            ok = {
                "item_id": "u089",
                "status": "ok",
                "raw_response": "Ideation",
            }
            text = json.dumps(failed) + "\n" + json.dumps(ok) + "\n"
            (out / "predictions.jsonl").write_text(text, encoding="utf-8")
            done = load_completed(out)
            self.assertEqual(set(done), {"u089"})
            content, status, pred = done["u089"]
            self.assertEqual(content, "Ideation")
            self.assertEqual(pred, "Ideation")
            self.assertNotIn("api_error", status)


if __name__ == "__main__":
    unittest.main()
