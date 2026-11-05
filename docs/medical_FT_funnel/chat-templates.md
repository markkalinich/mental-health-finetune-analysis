<!-- doc-verbosity: public-ready -->

# Medical chat templates

The method is [`docs/chat-template-comparison.md`](../chat-template-comparison.md). The table is `docs/medical_FT_funnel/chat-templates.csv`, written by `compare_chat_templates.py` on 24 October 2026 from `revision_3_experiments/hf_inventory/results/medical/2026-10-17/kept.csv`, the run `results/medical/CURRENT` named that day. When `CURRENT` moves, re-run the script and update this page.

Weights are `/home/mkalinich/hf_models/<org>__<name>/`. `tokenizer_from` is empty on every row. `fold_system` is 0 on every row. `config/serving_repairs.csv` has no row for these models. Every pair with a template on both sides renders the same string for a system message plus a user message (`text_equal=yes`) and for that pair after the fold (`folded_equal=yes`).

## Same template bytes as the parent (30)

These rows have `served_source_equals_parent=yes`.

- `Alexossss/medicalia`
- `ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit`
- `Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking`
- `MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged`
- `MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged`
- `MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged`
- `MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged`
- `Rishidar/autoscientist-healthcare-qlora`
- `ThxZ3US/Medicalia`
- `abaryan/BioXP-0.5B-MedMCQA`
- `anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo`
- `balarajr/triage-hospital-agent`
- `calebking/llama-3.2-3b-instruct-medical-full`
- `calebking/llama-3.2-3b-instruct-medical-math-full`
- `calebking/qwen2.5-3b-instruct-medical-full`
- `calebking/qwen2.5-3b-instruct-medical-math-full`
- `divyanshvats2004/medical-gemma-3-270m`
- `geshijoker/HealthCareMagic_sft_llama3_instruct_full`
- `graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5`
- `graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5`
- `graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5`
- `khazarai/Medical-QA`
- `mlxha/Llama-3.1-8B-Instruct-GRPO-medmcqa`
- `mlxha/Qwen-2.5-3B-grpo-medmcqa`
- `mlxha/Qwen2.5-7B-Instruct-grpo-medmcqa-medi70`
- `mlxha/Qwen3-8B-grpo-medmcqa-medi70`
- `oopere/SmolLM2-1.7B-ClinicalNER`
- `taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA`
- `tsavage68/MedQA_L3_1000steps_1e5rate_SFT`
- `vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical`

`Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking` and `MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged` match their parents on the string prompts. A user message whose content is a list raises `TypeError: can only concatenate str (not "list") to str` on both the fine-tune and the parent. `balarajr/triage-hospital-agent` matches `Qwen/Qwen3.5-4B` byte for byte. The fine-tune's copy is read from `tokenizer/chat_template.jinja` and the parent's from `processor/chat_template.jinja`.

## Borrowed tokenizer (0)

Every row has an empty `tokenizer_from`.

## Template bytes differ, string messages match (12)

The sentence tasks send strings. The first seven were counted as the same template for those tasks on 14 October 2026; the other five were compared on 24 October, after their downloads finished.

**`alpha-ai/Medical-Diagnosis-COT-Gemma3-270M` vs `google/gemma-3-270m-it`.** All five probes are yes. The served files differ by spaces in the generation-prompt line: the fine-tune has `{{ '<start_of_turn>model\n' }}` and the parent has `{{'<start_of_turn>model\n'}}`.

**`lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical` vs `google/gemma-4-E2B-it`.** `text_equal`, `folded_equal`, `list_equal`, and `image_part_equal` are yes. `image_url_equal` is no. An `image_url` part is omitted by the fine-tune and rendered as `<|image|>` by the parent. Same call as `Banaxi-Tech/BananaMind-V2.5-Content-Safety`.

**`Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1` vs `Qwen/Qwen3-8B`, and `suayptalha/Qwen3-0.6B-Medical-Expert` vs `Qwen/Qwen3-0.6B`.** `text_equal` and `folded_equal` are yes. A user message whose content is a list raises `TypeError: can only concatenate str (not "list") to str` on the fine-tune. The parent renders. `Satyam810/qwen3-8b-medical-reasoning` (parent `Qwen/Qwen3-8B`, compared 24 October) serves the same template bytes as `Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1` and gives the same results.

**`XformAI-india/Qwen3-1.7B-medicaldataset` vs `Qwen/Qwen3-1.7B`, `XformAI-india/Qwen3-4B-medicaldataset` vs `Qwen/Qwen3-4B`, and `mlxha/Qwen3-4B-grpo-medmcqa` vs `Qwen/Qwen3-4B`.** `text_equal` and `folded_equal` are yes. A list content raises `UndefinedError: 'list object' has no attribute 'startswith'` on the fine-tune. The parent renders. Same call as `Tommy-DING/FlexGuard-Qwen3-4B`. `mlxha/Qwen3-8B-grpo-medmcqa-v2` (parent `Qwen/Qwen3-8B`) and `nicoboss/Qwen-3-32B-Medical-Reasoning` (parent `Qwen/Qwen3-32B`), compared 24 October, serve the same template bytes as `XformAI-india/Qwen3-4B-medicaldataset` and give the same results.

**`EpistemeAI/Reasoning-Medical0.1-27B` vs `unsloth/Qwen3.5-27B`** (compared 24 October). All five probes are yes. The fine-tune's template is Unsloth's revision: it accepts a `developer` role, merges up to two leading system or developer messages into one, and drops the parent's exceptions for a system message after the first turn and for an unknown role. The probes send one system message, so the output is the same.

**`Slyracoon23/medical-gemma3n-emergency-response` vs `unsloth/gemma-3n-E4B-it`** (compared 24 October). `text_equal`, `folded_equal`, `list_equal`, and `image_url_equal` are yes; `image_part_equal` is no. The fine-tune serves the same template bytes as `SoufianeDahimi/child_trauma_gemma_finetune` and the parent the same bytes as that model's parent (`docs/mental_health_FT_funnel/chat-templates.md`): a content part of type `image` renders `<start_of_image>` on the fine-tune and `<image_soft_token>` on the parent. Counted as the same template for text benchmarks.

## Not compared (5)

No template on the fine-tune. Do not treat these rows as a match or a mismatch.

Fine-tune not on disk, parent on disk (2):

- `BLACKBUN/llama-2-13b-pubmed-qa-211k` — parent `meta-llama/Llama-2-13b-chat-hf`
- `BLACKBUN/llama-2-7b-pubmed-qa-211k` — parent `meta-llama/Llama-2-7b-chat-hf`

Both missing (3):

- `Melikshah/gpt-oss-20b-clinical-cot-gguf` — parent `unsloth/gpt-oss-20b-BF16`
- `openmed-community/AFM-4.5B-OpenMed` — parent `arcee-ai/AFM-4.5B`
- `openmed-community/granite-4.0-micro-OpenMed` — parent `ibm-granite/granite-4.0-micro`
