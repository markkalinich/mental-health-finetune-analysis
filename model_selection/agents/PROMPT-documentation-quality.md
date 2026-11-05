# Prompt: documentation quality of a model card (v1, 9 October 2026)

You score how completely a Hugging Face model card documents the model, against a fixed checklist.
Read the card only. Do not search the web, do not open links, do not read the extraction record.
The reference card is `Wothmag07/counseLLM` (its cached copy is listed in your assignment); read it first
so you know what a complete card looks like.

## Checklist (one point each, 12 points)

Score each item 1 if the card itself states it, 0 if not. "States" means the value is written on the
card, not implied by a link.

1. **Parent model** named (repo id or exact model name).
2. **Training objective** named (SFT, DPO, GRPO, ORPO, full fine-tune, instruction tuning, ...). A bare "fine-tuned" is 0.
3. **Update scope** stated (full weights, LoRA, QLoRA) with at least one hyperparameter (rank, alpha, or "all layers").
4. **Optimiser settings**: at least two of learning rate, epochs or steps, batch size, scheduler.
5. **Training data named**: every corpus has a name or link (a Hub id, a URL, or a published dataset name).
6. **Training data sized**: a row or example count for the training set (total or per corpus).
7. **Training data provenance**: says whether the text is human-written, synthetic, or a mix.
8. **Evaluation**: at least one numeric result on a named metric or benchmark.
9. **Comparison**: the evaluation includes the parent or another baseline.
10. **Intended use** stated in a sentence (who it is for, what it should do).
11. **Limitations or warnings**: at least one sentence about what the model should not do or where it fails.
12. **Hardware or compute**: GPU type, training time, or FLOPs.

## Output

For each assigned model write one JSON file to the output folder named `<owner>__<name>.json`:

```json
{
  "hf_id": "...",
  "card_file": "...",
  "card_bytes": 0,
  "scores": {"parent": 0, "objective": 0, "update_scope": 0, "optimiser": 0, "data_named": 0,
             "data_sized": 0, "data_provenance": 0, "evaluation": 0, "comparison": 0,
             "intended_use": 0, "limitations": 0, "compute": 0},
  "total": 0,
  "evidence": {"<item>": "<shortest quote from the card that earned the point>"},
  "notes": "one sentence, only if something did not fit the checklist"
}
```

Quote the card exactly. If an item scores 0, leave its evidence entry out. Do not round up: a
checklist item that is half met scores 0.

When all assigned files are written, reply with one line per model: `hf_id total/12`.
