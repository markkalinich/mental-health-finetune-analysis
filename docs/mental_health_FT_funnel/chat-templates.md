<!-- doc-verbosity: public-ready -->

# Mental-health chat templates

The method is [`docs/chat-template-comparison.md`](../chat-template-comparison.md). The table is `docs/mental_health_FT_funnel/chat-templates.csv`, written by `compare_chat_templates.py` on 24 October 2026 from `revision_3_experiments/hf_inventory/results/mental-health/2026-10-15/kept.csv`, the run `results/mental-health/CURRENT` named that day. When `CURRENT` moves, re-run the script and update this page.

## Same template bytes as the parent (13)

These rows have `served_source_equals_parent=yes` and no `tokenizer_from`. The file that holds the template can differ (a `chat_template.jinja` on the fine-tune, the `chat_template` field in the parent's `tokenizer_config.json`). The bytes of the template that will be served match.

- `ArkMaster123/qwen2.5-7b-therapist-v3`
- `KNipun/whisper-psychology-gemma-3-1b`
- `Psychotherapy-LLM/PsyCoPref-Llama3-8B`
- `SpaceXerror/cognitive-ai-mental-health-7b`
- `SungJoo/cradle-dialogue-qwen3-32b-2epoch`
- `Wothmag07/counseLLM`
- `dzur658/smollm2-mentalhealth-360m-V2`
- `ecorbari/Gemma-2b-it-Psych-Merged`
- `hongli-zhan/MINT-empathy-Qwen3-1.7B`
- `hongli-zhan/MINT-empathy-Qwen3-4B`
- `i5-8300h/gemma3-4b-psychology-dpo`
- `thillaic/CBT-Copilot`
- `zbt566666/qwen2.5-7b-mental-therapy-lora-sft`

`ecorbari/Gemma-2b-it-Psych-Merged` matches `google/gemma-2b-it`. Both templates raise `System role not supported` on a system message. `fold_system=1` is already set for both in `config/serving_repairs.csv`. The folded probe matches. The saved C-SSRS directories are rejected requests from before that fold was used, not empty generations. See `docs/serving-parity.md`.

Several of these templates, and their parents, raise `TypeError: can only concatenate str (not "list") to str` when the user content is a list. The sentence tasks and C-SSRS send strings. The error is the same on both sides, so it is not a difference.

## No template in the fine-tune (4)

These repos have weights and `config.json` and no tokenizer files. `child_source` is empty. `tokenizer_from` in `config/serving_repairs.csv` points vLLM `--tokenizer` at the parent, so the served bytes match the parent because the server is loading the parent's tokenizer.

- `AIMH/SQPsych-8b-gemma-Qwen` and `AIMH/SQPsych-8b-gemma-Qwen_no_questionnaire` borrow `Qwen/Qwen2.5-7B-Instruct`.
- `AIMH/SQPsychLLM-8b-gemma` and `AIMH/SQPsychLLM-8b-gemma-no_questionnaire` borrow `meta-llama/Meta-Llama-3-8B-Instruct`.

The model cards tell a user to call `AutoTokenizer.from_pretrained` on the AIMH id. That call does not work: the tokenizer is not in the repo. The borrow is this study's repair. It is not written by the authors. On 13 October 2026 Mark kept these four in the study and left the parent tokenizer in place; on 22 October he decided to keep them as they are (`docs/DECISIONS-PENDING.md`, Decided 22 October). All four are in the mental-health `kept.csv`. The two `AIMH/SQPsych-8b-gemma-Qwen` models leave at the funnel figure's last box because `agent_methods.csv` does not say whether they were trained full or with LoRA; the two `AIMH/SQPsychLLM-8b-gemma` models are on the roster.

## Template bytes differ (5)

Decisions below are from 13 October 2026. They apply to the text benchmarks (string messages). They are not a claim that the files are the same.

**`Someet24/empathetic-qwen3-8b-Jan` vs `Qwen/Qwen3-8B`.** The string probes match, including the folded pair. A user message whose content is a list raises `TypeError` on the fine-tune. The parent renders an empty user turn (`<|im_start|>user` immediately followed by `<|im_end|>`). Counted as the same template for string messages.

**`SoufianeDahimi/child_trauma_gemma_finetune` vs `google/gemma-3n-E2B-it`.** The string probes match, and so does an `image_url` part. A content part of type `image` renders `<start_of_image>` on the fine-tune and `<image_soft_token>` on the parent (`image_part_equal=no`). Counted as the same template for these text benchmarks.

**`naazimsnh02/gemma3-4b-mental-health-counseling` vs `unsloth/gemma-3-4b-it`.** Every probe renders the same string. The source differs by spaces inside `{{ }}`. One site is the model turn: the fine-tune has `{{ '<start_of_turn>model\n' }}` and the parent has `{{'<start_of_turn>model\n'}}`. The parent is read from `chat_template.json` because that repo has a processor and the legacy JSON file. The fine-tune's `chat_template.jinja` is served; since 13 October 23:45 its folder also holds `processor_config.json`, so the table names it as the processor template. Counted as the same template. Sampling fields in `generation_config.json` are not part of this comparison; the request overwrites them (`docs/chat-template-comparison.md`).

**`giannor/Qwen3.5-27B-psysafe` vs `Qwen/Qwen3.5-27B`.** Compared 13 October 2026 after both directories were on disk. Every probe renders the same string, including the image probes. `served_source_equals_parent=no` because the files are not the same bytes. Both folders have `preprocessor_config.json` (the fine-tune's since 14 October 00:02), so both templates are read as processor templates. Both are a `chat_template.jinja` file. The only difference is the tool-call branch: the parent loops `tool_call.arguments|items` when `arguments` is defined, and the fine-tune loops the keys when `arguments` is a mapping. `fold_system` is 0 and `tokenizer_from` is empty. The text benchmarks do not send a tool call.

**`prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2` vs `mistralai/Mistral-7B-Instruct-v0.2`.** The author's template raises `Conversation roles must alternate user/assistant/user/assistant/...` when the first message is a system message. The parent's current template accepts that message. `fold_system=1` is set, and `tokenizer_from` is empty: the server uses the author's tokenizer. After the fold, the fine-tune renders `<s>[INST] ...` and the parent renders `<s> [INST] ...` (a space after `<s>`). Decision: keep the author's template and the fold. Do not point `tokenizer_from` at the parent.
