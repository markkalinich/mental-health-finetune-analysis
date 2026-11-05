"""The decision review covers format failures and does not accept other labels."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from orchestration.yesno_decision_review import (  # noqa: E402
    LABELS,
    _message_text,
    check_labels,
    format_parsed,
)


class YesnoDecisionReviewTests(unittest.TestCase):
    def test_one_word_yes_is_a_format_success(self):
        self.assertTrue(format_parsed("Qwen/Qwen3-1.7B", "Yes."))

    def test_yes_later_in_the_reply_is_a_format_failure(self):
        self.assertFalse(format_parsed("Qwen/Qwen3-1.7B", "I think the answer is yes"))

    def test_yes_with_more_words_on_the_first_line_is_a_format_failure(self):
        self.assertFalse(format_parsed("Qwen/Qwen3-1.7B", "Yes, the message contains suicidal ideation."))

    def test_copied_question_is_a_format_failure(self):
        self.assertFalse(
            format_parsed("Qwen/Qwen3-1.7B", "The message contains suicidal ideation.")
        )

    def test_shield_card_label_is_a_format_success(self):
        self.assertTrue(format_parsed("jsl5710/Shield-Gemma-3-270m-Full-FT-CE", "unsafe"))

    def test_check_lists_every_gap(self):
        failures = [
            {"id": "si|m|a", "task": "si"},
            {"id": "cssrs|m|0", "task": "cssrs"},
        ]
        labels = [
            {"id": "si|m|a", "label": "answered_yes"},
            {"id": "cssrs|m|1", "label": "maybe"},
        ]
        problems = check_labels(failures, labels)
        self.assertIn("cssrs|m|0", problems)
        self.assertIn("cssrs|m|1", problems)
        self.assertTrue(any("maybe" in line for line in problems))

    def test_chat_message_is_the_reply_when_it_is_present(self):
        raw = json.dumps({"choices": [{"message": {"content": "Yes"}, "text": "no"}]})
        self.assertEqual(_message_text(raw), "Yes")

    def test_empty_message_uses_the_completion_text(self):
        raw = json.dumps({"choices": [{"text": "the user is not suicidal"}]})
        self.assertEqual(_message_text(raw), "the user is not suicidal")

    def test_empty_message_and_empty_completion_stay_empty(self):
        raw = json.dumps({"choices": [{"message": {"content": ""}, "text": ""}]})
        self.assertEqual(_message_text(raw), "")

    def test_check_accepts_the_three_labels(self):
        failures = [{"id": "si|m|a", "task": "si"}]
        for label in LABELS:
            self.assertEqual(
                check_labels(failures, [{"id": "si|m|a", "label": label}]),
                [],
            )


if __name__ == "__main__":
    unittest.main()
