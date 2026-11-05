# Agent prompt: read everything about one model once, and write it down

Version 5, 10 October 2026 (version 4 is kept as `PROMPT-extract-v4.md`, version 3 as `PROMPT-extract-v3.md`,
version 2 as `PROMPT-extract-v2.md`). v5 is the medical-grouping variant, written on Mark's request of
10 Oct 14:20 ("intended user, what role the model was supposed to play, whether it's a chatbot, what
output it's supposed to give, clinical task, specialty; we'll need these for the paper"). The safety
`detection_claim` block of v4 is dropped; the mental-health `use_claim` and `warning` scales of v3 return,
reworded for medical use; and five fields are added: `intended_user`, `role`, `clinical_task`,
`specialty`, and `output_kind` (kept from v4, with medical values). Everything else (data, method,
parent, serving, licence, the reading order, the one-paper cap) is unchanged from v4. This file is the
prompt. Copy it whole into each agent, then append the assignment block (repo id, inventory row,
output paths). Do not paraphrase it. If the prompt changes, bump the version and name it in the output
folder's README.

Model used: Grok 4.7 (high, fast) as a Cursor subagent with web search.

---

You are building the record for one Hugging Face model repository for a research study. Read the
sources in the order below, then write one JSON file and one markdown file. Every non-empty field that
states a fact about the model carries the URL it came from and, where the field is a judgment
(claim strength, warning strength, output type, intended user, role, clinical task, specialty), a verbatim quote. If no source states a field, write
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
   checkpoint by its model name. Read the full text of at most one paper unless the card itself links
   more than one; list the others by URL only.
5. Every GitHub repository the card or paper links to: README, training script, trainer config.
6. The dataset card of every dataset a source names, including informal names (MedQA, MedMCQA, PubMedQA,
   ChatDoctor HealthCareMagic, Medical Meadow, MIMIC-IV, MedDialog): find the Hub dataset page with that content and
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
- **Use claim** (medical): `Strong` (the card says the model gives medical advice, diagnosis,
  treatment or medication guidance, triage, or clinical decision support to a person or clinician,
  including "medical assistant", "doctor chatbot", "answers patient questions", even with a
  research-only warning; also a card with no description whose repo name contains `doctor`,
  `clinical-assistant`, or `medical-chatbot`); `Moderate` (a narrower medical use: patient education,
  summarising clinical notes, extracting findings, answering exam questions, medical coding);
  `Weak` (medical content but no use for a person: a benchmark-fitting demo, a research probe,
  a dataset-fitting run, "trained on medical data" with no stated purpose; also a card with no
  description whose YAML names a medical dataset); `Absent` (no medical content or claim).
- **Warning**: `Explicit prohibition` (must not or should not be used for diagnosis, treatment,
  medical advice, or clinical decisions); `Disclaimer only` ("not a substitute for a professional",
  "research or educational use only", "consult a physician", "not medical advice", while still
  presenting the model as a medical tool); `Unrelated limitations only` (hallucination, bias,
  language, nothing about medical use); `None`. Rulings carried over from mental health (Mark, 9 Oct):
  `Explicit prohibition` needs a sentence that forbids a use ("must not", "should not be used for",
  "do not use for"); "not a replacement for a doctor", "not a clinical tool", "not for diagnosis or
  treatment" are `Disclaimer only`.
- **Intended user** (who the card says will use the model): `patient or public`, `clinician`
  (physician, nurse, pharmacist, hospital staff), `student or exam taker`, `researcher or developer`,
  `other`, `not stated`. Several may apply; quote the sentence for each. A usage example alone does
  not name a user; the card has to say who it is for, or the example has to be unmistakably one
  (a patient describing symptoms; a clinician pasting a note).
- **Role** (what the card says the model is supposed to do, as a thing in a workflow): `answers
  medical questions`, `patient-facing chatbot` (talks with the patient about their own case),
  `clinical decision support` (helps a clinician decide), `documentation` (writes or summarises notes,
  reports, discharge letters), `information extraction or coding` (entities, ICD or other codes,
  structured fields from text), `triage` (sorts urgency or routes), `exam answerer`, `teaching or
  patient education`, `research artifact` (built to study a method, a bias, a failure, or a benchmark,
  not to be used), `other`, `not stated`. One value, the card's main purpose; a second only when the
  card gives two equal purposes. Quote the sentence.
- **Output type**: `Chatbot` (the card presents the model as something a person converses with:
  assistant, companion, doctor roleplay, dialogue generator); `Classifier` (emits a label or score);
  `Other` (a non-conversational tool that is not a classifier); `Not listed` (no usable description).
- **Output kind** (what the model writes, from the usage example or description): `chat reply`
  (ordinary assistant text), `exam letter` (A/B/C/D), `reasoning and answer` (prose that ends in an
  answer or diagnosis), `structured object` (JSON, a table, a code list), `label` (one class name),
  `score`, `summary or report` (free text that is not a conversation turn), `not stated`. Several may
  apply; quote the example or sentence for each.
- **Clinical task** (what medical work the model is trained or evaluated on): `medical QA`,
  `diagnosis or differential`, `triage`, `treatment or medication advice`, `clinical note summarisation
  or generation`, `radiology or pathology report`, `information extraction or coding`, `patient
  education`, `exam answering` (USMLE, MedQA, MedMCQA, PubMedQA, national licensing exams),
  `conversation with a patient`, `other`, `not stated`. List every one the card names, with a quote
  each. A benchmark the card only evaluates on is a task of the evaluation, not of the training;
  mark it `eval only` in the quote.
- **Specialty** (the field of medicine the card names): the card's own words (general medicine,
  radiology, oncology, cardiology, pharmacy, dentistry, dermatology, mental health, nursing,
  veterinary, traditional Chinese medicine, ...), as a list; `general` when the card says medical or
  clinical with no field; `not stated` when the card says nothing about the domain. Quote.
- **Source names this repo**: the source prints the exact repository id, or the same authors name
  this checkpoint by its model name. A paper about a sibling checkpoint (same project, other base)
  does not.

## Output 1: JSON

Exactly this structure. Keys in this order. Lists may be empty. Strings default to `"not stated"`.

```json
{
  "hf_id": "", "prompt_version": 5, "started": "", "ended": "",
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
                      "epochs": null, "steps": null, "learning_rate": null, "batch_size": null},
  "parent": {"card_claim": "", "source_claims": [{"parent": "", "source_url": "", "quote": ""}],
             "sources_agree_with_card": "yes | no | no outside source"},
  "size": {"parameters_stated": "", "parameters_stated_url": ""},
  "languages": {"values": [], "source_url": "", "quote": ""},
  "description": {"text": "", "source_url": ""},
  "output_type": {"value": "", "quote": ""},
  "use_claim": {"strength": "", "quote": ""},
  "warning": {"strength": "", "quote": ""},
  "intended_user": {"values": [], "quotes": [], "source_url": ""},
  "role": {"values": [], "quotes": [], "source_url": ""},
  "output_kind": {"values": [], "quotes": []},
  "clinical_task": {"values": [], "quotes": [], "source_url": ""},
  "specialty": {"values": [], "quote": "", "source_url": ""},
  "serving": {"text_only_input": "yes | no | not stated", "text_only_input_quote": "",
              "chat_template_present": "yes | no | not checked", "chat_template_source": "",
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

- `serving.text_only_input`: `yes` when the card's usage example, or the parent's card, runs the
  model on text with no image or audio; quote the example or sentence.
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
claims and warnings, user, role, task and specialty, serving), each quoting the sentence it rests on. Plain language. Short
sentences. Lead with the answer.

Return, as your final message, the two file paths, the wall time, and one line per field you could
not fill and why.
