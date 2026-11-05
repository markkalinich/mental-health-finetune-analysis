# Agent prompt: what kind of release is this parent model?

Version 1, 9 October 2026. This file is the prompt. Copy it whole into each agent, then append the
assignment block (the parent repo ids and the output path). Do not paraphrase it.

Model used: Grok 4.7 (high, fast) as a Cursor subagent with web search.

---

For each Hugging Face repository id you are given, decide what kind of release it is, from its own
card and, when the card is thin, from the organisation's release page or paper. The repo is a
**parent**: another model in a study names it as the checkpoint it was fine-tuned from. The study
keeps a child only when its parent is an instruction-tuned release. The rules below were set by the
study lead (Mark Kalinich, 9 October 2026).

Read-only. Do not download weights or PDFs. Write only the output file named in the assignment.

## Classes

- `instruction`: the repo is the chat or instruct **post-training of a pre-trained base**, released as
  that post-training. Who did it does not matter: a vendor's own instruct release
  (`meta-llama/Llama-3.2-3B-Instruct`, `google/gemma-3-4b-it`, `Qwen/Qwen3-8B`, `LiquidAI/LFM2-700M`,
  `ibm-granite/granite-3.1-8b-instruct`) and a community instruct tune of a base
  (`NousResearch/Hermes-2-Pro-Mistral-7B` from `mistralai/Mistral-7B-v0.1`, `lmsys/vicuna-7b-v1.5`
  from Llama 2, `TinyLlama/TinyLlama-1.1B-Chat-v1.0`, `tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3`
  from the Swallow continued-pretrain) both count. A base that went through continued pre-training
  before its instruct tune is still "pre-train, then instruct".
- `finetune`: the repo was trained **from a model that was already instruction-tuned** (pre-train,
  then instruct, then more tuning). Example: `ehristoforu/Gemma2-9B-it-psy10k` from `gemma-2-9b-it`;
  `ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1` from `Turkish-Llama-8b-Instruct-v0.1`.
- `pretrained`: a base release with no post-training (`Qwen/Qwen3-8B-Base`, `distilbert-base-uncased`,
  `meta-llama/Llama-3.2-3B`).
- `rehost`: a copy of another repo's weights under a different account (`unsloth/gemma-3-4b-it`,
  `NousResearch/Llama-2-7b-chat-hf`). Give the original in `base_repo`; the class the study uses is
  the original's class, so also fill `class_of_original`.
- `quantized_rehost`: a quantized copy (`unsloth/...-bnb-4bit`). Give the original.
- `not_a_language_model`: a speech, vision, embedding, or diarization model.
- `unreadable`: the repo does not exist or the card cannot be read.

## Evidence, in order

1. The card's YAML (`base_model`, `base_model_relation`, tags `instruct`, `chat`, `pretrained`).
2. The card's text: "instruct fine-tuned version of X", "post-trained", "this is the base model",
   "fine-tuned from <an already-instruct repo>".
3. The vendor's release page or paper for the family, when the card is a template (Meta's and
   Google's cards are shared across base and instruct repos; the repo name suffix `-Instruct`, `-it`,
   `-chat` then decides, and you say so in `quote`).

## Output

CSV, one row per parent, in the order of the assignment, header exactly:

```
parent_id,class,base_repo,class_of_original,evidence_url,quote,confidence,needs_mark,why
```

- `class`: one of the seven above.
- `base_repo`: for `instruction` and `finetune`, the repo it was trained from, as the card names it
  (empty if the card names none); for the two rehost classes, the original repo.
- `class_of_original`: filled only for the rehost classes.
- `evidence_url`: the page the quote came from.
- `quote`: one verbatim sentence, or "name suffix -Instruct; card is the shared family card" when the
  name decided.
- `confidence`: `high`, `medium`, `low`.
- `needs_mark`: `yes` when the case is an edge the rules do not settle (for example a release that is
  both base-trained and post-trained in one repo, a "post-trained" release with no base named, a
  parent whose own base is itself a community fine-tune); else `no`.
- `why`: one sentence, only when `needs_mark` is `yes`.

Return the CSV path, counts per class, and the `needs_mark` rows.
