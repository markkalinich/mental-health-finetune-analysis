# Agent prompt: read everything about one model once, and write it down

Version 2, 9 October 2026. Replaces `PROMPT-dataset-search.md` and `PROMPT-method-search.md`
(version 1) with one pass per model that records every field the study needs. This file is the
prompt. Copy it whole into each agent, then append the assignment block (repo id, inventory row,
output paths). Do not paraphrase it. If the prompt changes, bump the version and name it in the output
folder's README.

Model used: Grok 4.7 (high, fast) as a Cursor subagent with web search.

---

You are building the record for one Hugging Face model repository for a research study. Read the
sources in the order below, then write one JSON file and one markdown file. Every non-empty field that
states a fact about the model carries the URL it came from and, where the field is a judgment
(claim strength, warning strength, output type), a verbatim quote. If no source states a field, write
`"not stated"` for strings, `[]` for lists, `null` for numbers. The repository name is not evidence.
Library boilerplate ("trained 2x faster with Unsloth") is not evidence of a method. A word inside a
dataset id, a URL, or a benchmark comparison is not evidence that this model was trained with that
method.

Read-only. Do not download model weights. Do not download PDFs. Write only the two output files
named in your assignment. Run `date -Is` at the start and the end and put both in the JSON.

## What to read, in this order

1. The cached model card named in the assignment (`revision_3_experiments/hf_inventory/cache/readmes/...`).
   Run `sha256sum` on it and record the hash.
2. The current card at `https://huggingface.co/<org>/<name>/raw/main/README.md`. Record whether it
   differs from the cached one. If it does, read it too and say what changed in one sentence.
3. The repository file list at `https://huggingface.co/api/models/<org>/<name>` (field `siblings`),
   and the contents of `config.json`, `generation_config.json`, `tokenizer_config.json`
   (`chat_template` key), `chat_template.jinja`, `adapter_config.json`, and any notebook, `train.py`,
   `run.sh`, or trainer JSON that is in the repository.
4. Every paper or preprint the card or the repository links to, or that a search for the repo id or
   model name finds: the arXiv abstract page, then the HTML full text at `https://arxiv.org/html/<id>`
   when it exists. Not the PDF. Record whether the paper prints this exact repo id or names this
   checkpoint by its model name.
5. Every GitHub repository the card or paper links to: README, training script, trainer config.
6. The dataset card of every dataset a source names, including informal names (GoEmotions, ESConv,
   MentalChat16K, DailyDialog, Empathetic Dialogues): find the Hub dataset page with that content and
   record its id and whether it loads.

Search strings, in this order, recorded in `queries_tried`: `"<org>/<name>"`, `"<name>" huggingface`,
`"<name>" arxiv`, `"<name>" github`, then the paper title if one is found, then each dataset name plus
`huggingface dataset`.

## Definitions

- **Objective** (a named loss): `sft`, `dpo`, `grpo`, `ppo`, `rlhf`, `distillation`,
  `continued_pretraining`, `classification`, or `not stated`. "Fine-tuned" alone is not an objective.
  LoRA is not an objective. Counts only when the sentence is about how this checkpoint was trained.
- **Update scope**: `full`, `lora`, `qlora` (LoRA on a quantized base), `adapter_other`, `not stated`.
  A sentence such as "QLoRA enables full fine-tuning on two T4s" is about QLoRA, not a full fine-tune.
- **Output type**: `Chatbot` (the card presents the model as something a person converses with:
  assistant, companion, therapist roleplay, dialogue generator); `Classifier` (emits a label or
  score); `Other` (a non-conversational tool that is not a classifier); `Not listed` (no usable
  description).
- **Use claim** (therapy or support): `Strong` (the card says the model delivers therapy, counseling,
  CBT, emotional support, or counselor-style dialogue to a person, including "roleplay a therapist",
  "improves the quality of counseling responses", even with a research-only warning; also a card with
  no description whose repo name contains `therapist` or `psychotherapist`); `Moderate` (a narrower
  supportive conversation: psychoeducation, reflective listening, compassionate listener, mood
  check-in, empathetic chat with mental-health framing); `Weak` (mental-health related but not a
  support conversation: reasoning about psychological concepts, a risk classifier, a clinician-facing
  tool, a dataset-fitting demo; also a card with no description whose YAML names a mental-health
  dataset); `Absent` (no mental-health content or claim).
- **Warning**: `Explicit prohibition` (must not or should not be used for therapy, counseling,
  mental-health support, diagnosis or treatment, or medical advice); `Disclaimer only` ("not a
  substitute for a professional", "research or educational use only", "consult a professional",
  crisis-line text, while still presenting the model as a support tool); `Unrelated limitations only`
  (hallucination, bias, language, nothing about therapy or medical use); `None`.
- **Source names this repo**: the source prints the exact repository id, or the same authors name
  this checkpoint by its model name. A paper about a sibling checkpoint (same project, other base)
  does not.

## Output 1: JSON

Exactly this structure. Keys in this order. Lists may be empty. Strings default to `"not stated"`.

```json
{
  "hf_id": "", "prompt_version": 2, "started": "", "ended": "",
  "card": {"cached_file": "", "cached_sha256": "", "current_differs": false, "current_change": ""},
  "repo_files": [],
  "links": {
    "github": [],
    "papers": [{"url": "", "arxiv_id": "", "title": "", "venue": "", "names_this_repo": false}],
    "project_pages": [], "demos": []
  },
  "training_data": [{"name": "", "hub_id": "", "urls": [], "loads": false, "n_examples": null,
                     "language": "", "provenance": "human | synthetic | mixed | not stated",
                     "source_type": "card | repo_file | paper | github | dataset_card",
                     "source_url": "", "quote": ""}],
  "training_method": {"objective": "", "objective_quote": "", "objective_url": "",
                      "update_scope": "", "update_scope_quote": "", "update_scope_url": "",
                      "lora_rank": null, "lora_alpha": null, "adapter_merged": "yes | no | not stated",
                      "quantized_base_during_training": "yes | no | not stated",
                      "epochs": null, "learning_rate": null, "batch_size": null},
  "parent": {"card_claim": "", "source_claims": [{"parent": "", "source_url": "", "quote": ""}],
             "sources_agree_with_card": "yes | no | no outside source"},
  "size": {"parameters_stated": "", "parameters_stated_url": ""},
  "languages": {"values": [], "source_url": "", "quote": ""},
  "description": {"text": "", "source_url": ""},
  "output_type": {"value": "", "quote": ""},
  "use_claim": {"strength": "", "quote": ""},
  "warning": {"strength": "", "quote": ""},
  "serving": {"chat_template_present": "yes | no | not checked", "chat_template_source": "",
              "system_prompt": "", "system_prompt_url": "",
              "generation_settings": {}, "generation_settings_url": "",
              "max_context": null, "notes": ""},
  "evaluation_reported": {"text": "", "source_url": ""},
  "license": {"value": "", "source_url": ""},
  "inventory_row": {"methods": "", "datasets": "", "parent": ""},
  "matches_inventory": "yes | partly | no", "discrepancies": "",
  "pages_read": [], "queries_tried": [], "confidence": "high | medium | low"
}
```

- `description.text`: the card's own description of the model, verbatim, first one or two paragraphs
  after the title. Not your summary.
- `serving.generation_settings`: the values from `generation_config.json` or the card's example
  (`temperature`, `top_p`, `top_k`, `max_new_tokens`, `repetition_penalty`, `do_sample`), as given.
- `pages_read`: from `cached_card`, `current_card`, `repo_files`, `config_json`, `generation_config`,
  `tokenizer_config`, `abstract`, `html_fulltext`, `github`, `dataset_card`.
- `inventory_row`: copy from the assignment.

## Output 2: markdown

One `# <hf_id>` heading, then `## Sources` (every URL you used, one per line, with one phrase saying
what it is), then `## Record` with one short paragraph per block of the JSON (data, method, parent,
claims and warnings, serving), each quoting the sentence it rests on. Plain language. Short
sentences. Lead with the answer.

Return, as your final message, the two file paths, the wall time, and one line per field you could
not fill and why.
