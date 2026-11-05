"""A checkpoint is prompted the way its own files are set up."""
from types import SimpleNamespace
import unittest

from orchestration.api_client import ChatCompletionsClient, prompts_as_one_string


def _client(model_id: str) -> ChatCompletionsClient:
    return ChatCompletionsClient(SimpleNamespace(
        base_url="http://127.0.0.1:9/v1",
        model=model_id,
        request_timeout=1,
        temperature=0,
        max_tokens=16,
        top_p=1,
    ))


class PromptFormatTests(unittest.TestCase):
    def test_missing_files_stay_a_chat(self):
        self.assertFalse(prompts_as_one_string("not-a-real/model", {}))
        payload = _client("not-a-real/model").build_messages_completion_payload(
            [{"role": "system", "content": "Say yes or no."}, {"role": "user", "content": "Hello."}],
            max_tokens=16,
        )
        self.assertIn("messages", payload)
        self.assertNotIn("prompt", payload)

    def test_qwen_base_keeps_the_template_it_shipped(self):
        client = _client("Qwen/Qwen2.5-7B")
        self.assertFalse(client.one_string)
        payload = client.build_messages_completion_payload(
            [{"role": "user", "content": "Hello."}],
            max_tokens=16,
        )
        self.assertEqual(payload["messages"][0]["content"], "Hello.")

    def test_tokenizer_repair_stays_a_chat(self):
        self.assertFalse(prompts_as_one_string(
            "google/gemma-2b",
            {"tokenizer_from": "google/gemma-2b-it"},
        ))

    def test_gemma_base_is_one_string(self):
        client = _client("google/gemma-2b")
        self.assertTrue(client.one_string)
        payload = client.build_messages_completion_payload(
            [
                {"role": "system", "content": "Say yes or no."},
                {"role": "user", "content": "Hello."},
            ],
            max_tokens=16,
            temperature=0.0,
        )
        self.assertEqual(payload["prompt"], "Say yes or no.\n\nHello.")
        self.assertNotIn("messages", payload)
        self.assertNotIn("chat_template_kwargs", payload)
        self.assertEqual(payload["temperature"], 0.0)

    def test_instruction_model_stays_a_chat(self):
        client = _client("google/gemma-2b-it")
        self.assertFalse(client.one_string)
        payload = client.build_messages_completion_payload(
            [{"role": "system", "content": "Say yes or no."}, {"role": "user", "content": "Hello."}],
            max_tokens=16,
        )
        self.assertEqual(payload["messages"][0]["role"], "user")
        self.assertEqual(payload["messages"][0]["content"], "Say yes or no.\n\nHello.")

    def test_completion_text_is_read(self):
        client = _client("google/gemma-2b")
        self.assertEqual(
            client.extract_content({"choices": [{"text": "yes"}]}),
            "yes",
        )
        self.assertEqual(
            client.extract_content({"choices": [{"message": {"content": "no"}}]}),
            "no",
        )


if __name__ == "__main__":
    unittest.main()
