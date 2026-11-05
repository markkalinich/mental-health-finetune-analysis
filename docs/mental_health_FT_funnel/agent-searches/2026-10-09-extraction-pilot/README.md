<!-- doc-verbosity: public-ready -->

# Extraction pilot, 9 October 2026: one agent reads everything about one model

Purpose: test prompt version 2 (`revision_3_experiments/hf_inventory/agents/PROMPT-extract.md`),
which replaces the separate dataset search, method search, and hand card review with one pass per
model, and measure what one model costs. Five Grok 4.7 (high, fast) Cursor subagents, one model
each, in parallel. Each wrote `extractions/<org>__<name>.json` (fixed schema) and `reports/<org>__<name>.md`.

The five were chosen because each tests a known weak spot of the regex rules:

| Model | Why chosen | Wall time |
|---|---|---:|
| `AIMH/SQPsychLLM-8b-gemma` | has a preprint and a training script that disagree on the learning rate | 10 min 52 s |
| `Psychotherapy-LLM/PsyCoPref-Llama3-8B` | preprint says iterative DPO; the card regex found no method | 12 min 06 s |
| `kebbbnnn/TinyLlama-Friendly-Psychotherapist` | regex counted DPO from a dataset id on an empty template card | 11 min 07 s |
| `SpaceXerror/cognitive-ai-mental-health-7b` | regex labelled it `full_finetune` from "QLoRA enables full fine-tuning on two T4s" | 13 min 46 s |
| `howardbaik/gemma-4-E4B-it-mentalchat16k` | `image-text-to-text` tag; does it take text-only input? | 14 min 49 s |

Started 15:46 EDT; all five JSON files written by 16:01. About 12.5 minutes per model per agent, about
twice the dataset-only pass (prompt v1: about 1 minute per model inside a 5-model batch). Cursor usage
before/after is for Mark to read off the usage page.

## What the agents got right that the regex got wrong

| Model | Regex (`kept.csv` `methods`) | Agent | Source |
|---|---|---|---|
| `PsyCoPref-Llama3-8B` | none | `dpo`, update scope not stated | arXiv HTML: iterative DPO on Llama-3.1-8B-Instruct; this repo is the paper's 87% model |
| `kebbbnnn/...` | `dpo` | not stated | "DPO" appears only inside `SAGI-1/Greetings_DPO_dataset_V1` |
| `SpaceXerror/...` | `full_finetune|qlora` | `sft` / `qlora`, adapter merged into an fp16 copy | card and executed notebook: QLoRA on a 4-bit NF4 base, then merge; the "full fine-tuning" sentence is about QLoRA |
| `SQPsychLLM-8b-gemma` | `sft` | `sft` / `full`, lr 2e-4 (paper) vs 2e-5 (script), recorded as a discrepancy | paper and `src/finetune.py` |
| `howardbaik/...` | `sft` | `sft` / `full`; text-only input accepted | card example has no image; author's tutorial: multimodal token ids are "not relevant for our text-only input"; parent card lists text, image, audio as optional inputs |

One card-vs-source discrepancy the pass surfaced that no earlier step could: `SpaceXerror`'s card says
2,598 CounselChat + 4,527 PHR training rows; the executed notebook log shows the trainer received
7,125 rows from a 15,000-row cap over filtered CounselChat and synthetic PHR data. The JSON records
both with their URLs under `discrepancies`.

## Claims and warnings: agent vs Mark's 9 October card review

Same definitions, read independently. 2 of 5 agree on all three fields; 3 differ on one field each.

| Model | Field | Mark | Agent | Agent's quote |
|---|---|---|---|---|
| `PsyCoPref-Llama3-8B` | warning | None | Disclaimer only | "However, these responses should not be directly exposed to clients without review by real therapists." |
| `SpaceXerror/...` | warning | Explicit prohibition | Disclaimer only | "This model is NOT a replacement for professional therapy or crisis intervention." (Mark's quote adds "Not a clinical tool: not diagnosis or treatment") |
| `howardbaik/...` | use claim | Strong | Moderate | "intended for research on empathetic conversational behavior in small instruction-tuned models." |

The disagreements are definitional edges, not reading errors: whether "should not be exposed to clients without review" is a warning or none; whether "not a clinical tool, not diagnosis or treatment" is a prohibition or a disclaimer; whether "counseling-style response quality" is a therapy claim or an empathetic-chat claim. The definitions in the prompt should say which way each goes before the 41 are run. Output type agreed on all five.

## Fields the agents could not fill, and why

Mostly honest gaps in the sources: LoRA rank and alpha when no LoRA was used; epochs when the paper
gives steps; languages when the card says "[More Information Needed]"; example counts for gated
datasets (`Amod/mental_health_counseling_conversations`, `EmoCareAI/Psych8k`) whose public page gives
no row count; one Kaggle page that returned a rate limit. None of these is a prompt defect.

## Prompt changes before the 41-model run (version 3)

1. Resolve the three definitional edges above, in the prompt text.
2. Add `text_only_input: yes | no | not stated` with a quote (asked ad hoc for the E4B model; useful for every multimodal-tagged model).
3. Add `data_urls` is already a list; also allow a list for `source_url` on the method fields when the card and a script both state it.
4. Record `steps` beside `epochs`.
5. Cap arXiv reading at one paper unless the card links more than one (SpaceXerror's agent read three).

## Files

- `extractions/*.json`: the record, one per model, schema in the prompt.
- `reports/*.md`: sources and the quoted sentences.
- A merge script (`collect_extractions.py`, to be written) will flatten the JSON into `agent_fields.csv`
  and the card-review CSV columns.
