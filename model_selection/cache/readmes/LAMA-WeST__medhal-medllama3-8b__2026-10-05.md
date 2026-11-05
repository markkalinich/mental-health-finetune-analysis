---
base_model: johnsnowlabs/JSL-MedLlama-3-8B-v2.0
---

# medhal-medllama3-8b

LoRA fine-tune of `JSL-MedLlama-3-8B-v2.0` for medical hallucination
detection, trained for [MedHal](https://arxiv.org/abs/2504.08596). Given a
context and a statement, the model judges whether the statement is factually
supported by the context.

## Training

- Method: supervised fine-tuning with LoRA (r=16, 4-bit), 1 epoch,
  `max_seq_length=8192`, per-device batch 2, gradient accumulation 2,
  seed 42. Loss computed only after the `### Factual` marker.
- Data: `medhal_lf_bal_qafil_train_val`. This artifact is the
  merged full weights (base + adapter via `save_trained_model.py`).

## Use

Format prompts with the MedHal formatter (`src/data/formatter.py`,
`model_wrapper=medhal`) and parse YES/NO answers with
`src/evaluation/medhal_parser.py:MedHalParser`.

## Limitations

Research artifact. Not for clinical use. Inherits the base model's license
and biases; hallucinations in the judge itself are possible — see the
`invalid` rate reported by `MedHalParser.evaluate`.
