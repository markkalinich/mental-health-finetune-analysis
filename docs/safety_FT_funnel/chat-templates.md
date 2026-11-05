<!-- doc-verbosity: public-ready -->

# Safety chat templates

The method is [`docs/chat-template-comparison.md`](../chat-template-comparison.md). The table is `docs/safety_FT_funnel/chat-templates.csv`, written by `compare_chat_templates.py` on 24 October 2026 from `revision_3_experiments/hf_inventory/results/safety/2026-10-17/kept.csv`, the run `results/safety/CURRENT` named that day. When `CURRENT` moves, re-run the script and update this page.

## Same template bytes as the parent (29)

These rows have `served_source_equals_parent=yes` and no `tokenizer_from`. The file that holds the template can differ: a `chat_template.jinja` on the fine-tune, the `chat_template` field in the parent's `tokenizer_config.json`, or `chat_template.json` when the parent has a processor. The bytes of the template that will be served match.

- `DloadingX/GuardTrace-VL-3B`
- `Hagrun/moddog-l1-safety-qwen2.5-3b`
- `Jazhyc/Llama-3.1-8B-aims-grpo`
- `ReasoningShield/ReasoningShield-3B`
- `Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B`
- `adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1`
- `adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged`
- `adzcai/AfriGuardInst-tiny-aya-earth-full`
- `adzcai/AfriGuardInst-tiny-aya-earth-lora-merged`
- `adzcai/AfriGuardInst-tiny-aya-global-lora-merged`
- `bfuzzy1/Railz-R2`
- `iwalton3/sycofact`
- `jdleo1/tinysafe-3`
- `jsl5710/Shield-Gemma-3-1B-Full-FT-CE`
- `jsl5710/Shield-Gemma-3-270m-Full-FT-CE`
- `jsl5710/Shield-Llama-3.2-1B-Full-FT-CE`
- `jsl5710/Shield-Qwen3-1.7B-Full-FT-CE`
- `jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE`
- `tomg-group-umd/DynaGuard-1.7B`
- `tomg-group-umd/DynaGuard-4B`
- `tomg-group-umd/DynaGuard-8B`
- `tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep`
- `yueliu1999/GuardReasoner-VL-7B`
- `yueliu1999/GuardReasoner-VL-Eco-3B`
- `yushaohan/ProGuard-3B`
- `yushaohan/ProGuard-7B`
- `zrwang1211/SafeAtlas-Guard-2B`
- `zrwang1211/SafeAtlas-Guard-4B`
- `zrwang1211/SafeAtlas-Guard-8B`

`Hagrun/moddog-l1-safety-qwen2.5-3b` and `jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE`, and their parents, raise `TypeError: can only concatenate str (not "list") to str` when the user content is a list. The sentence tasks send strings. The same exception on the fine-tune and the parent is not a difference.

## Borrowed tokenizer (0)

Every row has an empty `tokenizer_from`. `config/serving_repairs.csv` has no row for these models. When the fine-tune directory is on disk, the served template is read from that directory.

## Not on disk (1)

`henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B` is under `/home/mkalinich/hf_models/`; its parent `Qwen/Qwen3.6-35B-A3B` is not. The CSV row has no parent template.

Do not treat this row as a match or a mismatch.

## Template bytes differ (5)

**`Banaxi-Tech/BananaMind-V2.5-Content-Safety` vs `google/gemma-4-E2B-it`.** `text_equal`, `folded_equal`, `list_equal`, and `image_part_equal` are yes. `image_url_equal` is no. An `image_url` part is omitted by the fine-tune and rendered as `<|image|>` by the parent. The fine-tune renders `<bos><|turn>user\n<turn|>\n<|turn>model\n`. The parent renders `<bos><|turn>user\n<|image|><turn|>\n<|turn>model\n`. The fine-tune has no processor config, so the served file is `chat_template.jinja`. The parent has a processor, so its `chat_template.jinja` is served. The fine-tune writes `<|image|>` for a part of type `image`. The parent writes `<|image|>` for type `image` and for type `image_url`. Counted as the same template for text benchmarks on 13 October 2026.

**`tzchen07/rai-gemma4-e2b-5b-safety-dora-r64-fullfix` vs `google/gemma-4-E2B-it`** (compared 24 October, after its download). It serves the same template bytes as `Banaxi-Tech/BananaMind-V2.5-Content-Safety` against the same parent bytes, with the same probe results: only `image_url_equal` is no. Its folder has a processor config, so the table names the processor template. Counted as the same template for text benchmarks.

**`Tommy-DING/FlexGuard-Qwen3-4B` vs `Qwen/Qwen3-4B`.** `text_equal` and `folded_equal` are yes. A user message whose content is a list raises `UndefinedError: 'list object' has no attribute 'startswith'` on the fine-tune, so `list_equal`, `image_url_equal`, and `image_part_equal` are blank. The parent renders an empty user turn, `<|im_start|>user` immediately followed by `<|im_end|>`, then `<|im_start|>assistant`. The parent's template checks `message.content is string` before calling `startswith`, and uses an empty string when the content is a list. The fine-tune calls `startswith` on the list. The sentence tasks send strings. Counted as the same template for string messages on 13 October 2026, the same call as `Someet24/empathetic-qwen3-8b-Jan`.

**`Tommy-DING/FlexGuard-Qwen3-8B` vs `Qwen/Qwen3-8B`.** The served template bytes are the same as `Tommy-DING/FlexGuard-Qwen3-4B`, and the parent bytes are the same as `Qwen/Qwen3-4B`. `text_equal` and `folded_equal` are yes. The `list`, `image_url`, and `image_part` probes raise `UndefinedError: 'list object' has no attribute 'startswith'` on the fine-tune. The parent renders `<|im_start|>user\n<|im_end|>\n<|im_start|>assistant\n`. Counted as the same template for string messages on 13 October 2026, with the 4B model above.

**`jl3676/HarmReporter` vs `meta-llama/Llama-3.1-8B-Instruct`.** `text_equal` and `folded_equal` are no. Both sides render. The fine-tune's template writes a `<|user|>` turn and a `<|assistant|>` turn, and leaves a system message out of the string. The string probe on the fine-tune is `<|user|>\nHello.\n<|assistant|>\n`. The parent writes Llama 3.1 headers, the lines `Cutting Knowledge Date: December 2023` and `Today Date: 26 Jul 2024`, and then the system text `Reply with one word.`:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 26 Jul 2024

Reply with one word.<|eot_id|><|start_header_id|>user<|end_header_id|>

Hello.<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```

The folded probe on the fine-tune is `<|user|>\nReply with one word.\n\nHello.\n<|assistant|>\n`. The parent still writes the two date lines, with an empty system message, then `<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nReply with one word.\n\nHello.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n`. `config/serving_repairs.csv` has no row for this model, so the string probe is sent with a system role. A list content raises `TypeError: can only concatenate str (not "list") to str` on the fine-tune. The parent writes the list as Python text in the user turn (`[{'type': 'text', 'text': 'Hello.'}]` for the text-part probe). The same fine-tune error is on the `image_url` and `image_part` probes.
