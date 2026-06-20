# Llama Guard 3 1B — embedded vs override Jinja

Canonical copies for reviewer re-read. See [`REVIEWER_2_EXPERIMENTS.md`](../../REVIEWER_2_EXPERIMENTS.md) Claim 4 and [`data/break_tests/llama_guard_3_1b_break_test.json`](../../data/break_tests/llama_guard_3_1b_break_test.json).

| File | Role | SHA256 |
|------|------|--------|
| `embedded_gguf_real.jinja` | GGUF `tokenizer.chat_template` (RichardErkhov Q8_0) | `df3965ba586f628bed4f3bb122cda2cc7502d5fdd87b525d4a3fea37831905f7` |
| `override_from_subtask1.jinja` | LM Studio override (runtime) | `3652a68adfcb5fc2a54a3aa52750b64d124a05901c07aaff67d1c1b5b300a857` |

Other files in this directory are duplicates from extraction (`embedded_gguf.jinja`, `lm_studio_override.jinja`, etc.).
