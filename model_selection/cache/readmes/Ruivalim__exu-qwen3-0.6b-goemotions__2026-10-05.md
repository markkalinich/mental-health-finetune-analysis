---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
datasets:
  - google-research-datasets/go_emotions
language:
  - en
tags:
  - exu
  - calibrated-decisions
  - emotion
  - text-classification
  - proper-scoring-rule
library_name: exu
---

# exu-qwen3-0.6b-goemotions

An experimental decision model from [Exu](https://github.com/ruivalim/exu-base): a
Qwen3-0.6B body with a small decision head that answers one typed question about a
Reddit comment, "Which emotion does this comment express?", with a probability
distribution over the 28 GoEmotions labels. It never generates text. Each comment
is scored once per emotion (28 short sequences) and the softmax across those scores
is the answer.

It is published as an example of what the toolkit's decoder path produces, not as
a product. Read the limitations before using it for anything.

## Numbers

Test split of GoEmotions (5,884 comments, targets are the share of rater marks per
label), calibrated with one temperature fitted on a held-out split. Numbers from
[BENCHMARKS.md](https://github.com/ruivalim/exu-base/blob/main/BENCHMARKS.md),
section 10.

| Model | NLL | Brier | Accuracy | ECE |
| --- | --- | --- | --- | --- |
| this model (seed 17, one epoch) | 1.8435 | 0.2142 | 0.5648 | 0.135 |
| same recipe, three seeds | 1.8417 ± 0.0019 | 0.2134 ± 0.0011 | 0.5587 ± 0.0092 | 0.116 ± 0.017 |
| `answerdotai/ModernBERT-base` with Exu's marker readout, three epochs, three seeds | 1.8549 ± 0.0119 | 0.2174 | 0.5542 | 0.102 |
| `google-bert/bert-base-uncased`, same, three epochs, three seeds | 1.8676 ± 0.0076 | 0.2195 | 0.5514 | 0.110 |
| label-frequency prior (no model) | 2.8267 | | 0.2927 | |

NLL and Brier are strictly proper scores, and they are what to compare. Accuracy is
against the majority label of each comment; with soft targets an exactly honest
forecast still has a non-zero ECE.

## Training

One epoch over the 46,370 training comments, seed 17, with Exu's composite reward
(log score plus 0.75 times the spherical score), AdamW with learning rate `1e-5` on
the body and `1e-4` on the head, batch 8 with gradient accumulation 2, float32
weights under bfloat16 autocast, gradient checkpointing, sequences capped at 128
tokens (5 of 58,007 questions were cut). About 61 minutes on one RTX 5090. A second
epoch made the test NLL worse (1.8704), so one epoch is what is published.

Sequence per candidate emotion, scored at the hidden state of the final token:

```
State: {"text":"<comment>"}
type: choice
Question: Which emotion does this comment express?
Candidate: <emotion>
Decision:<|im_end|>
```

The head is `LayerNorm(1024)` followed by `Linear(1024, 1)`. The language-model head
of Qwen3 is not part of this model.

## Use

```bash
pip install torch transformers safetensors
python exu_probe_infer.py --model-dir . --text "thanks, that made my day"
```

```
{"text": "thanks, that made my day", "top": [{"emotion": "gratitude", "p": 0.8218}, {"emotion": "joy", "p": 0.1092}, {"emotion": "excitement", "p": 0.0275}]}
```

`exu_probe_infer.py` in this repository is the whole runtime: it builds the 28
sequences, runs the body, applies the head and the fitted temperature from
`config.json`. It needs a GPU with about 3 GB free, or runs on the CPU slowly.

## Limitations

- **Format.** These weights are in the format of a research probe. The `exu-base`
  package (0.1.0) does not load them: its checkpoints are encoder models with a
  marker readout. The decoder path is planned for a later release, and this model
  will be re-published in the package's format then.
- **One question.** The model was trained on exactly one instruction and one option
  list. Exu's design lets a model answer a question written at request time; this
  checkpoint has only ever seen this one, and nothing here measures how it does on
  another.
- **Not a moderation or clinical tool.** GoEmotions is Reddit comments labelled by
  crowd raters; the labels carry their biases and the comments their language.
- **One epoch, one seed.** The three seeds of the recipe agree to within 0.004 of
  NLL, but nothing beyond that was tuned or checked.

## Sources and licenses

- Base model: [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B), Apache-2.0.
- Data: [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions),
  Apache-2.0. No data is included here.
- Toolkit: [Exu](https://github.com/ruivalim/exu-base), Apache-2.0. The training
  method behind the toolkit is described there, with the measurements that led to
  training this model with the direct objective and not with RLCD.
