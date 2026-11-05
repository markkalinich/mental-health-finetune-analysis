---
license: apache-2.0
base_model: convaiinnovations/laya
library_name: laya
tags: [laya, gutcheck, classification]
---

# laya-prompt-guard

A [Laya](https://huggingface.co/convaiinnovations/laya) checkpoint (`convaiinnovations/laya`) fine-tuned for the
[gutcheck](https://github.com/16SULPHUR/gutcheck) `prompt-guard` pack: Screens text sent to an LLM for prompt injection and jailbreak attempts. Use it as one layer of defence, not the only one: attackers adapt, and these checks can be fooled.

It was trained with gutcheck 0.0.1 using Laya's RLCD recipe on each question's
training split. A fixed 20% slice of that split was held out and never trained on; it is in
`heldout/` and is what the numbers below and the calibration temperatures come from. The pack's
test sets were not used; see the pack's `EVAL.md` for test results.

| Question | Train rows | Held-out rows | Base accuracy | Fine-tuned accuracy |
| --- | --- | --- | --- | --- |
| `prompt-guard.injection` | 437 | 109 | 0.468 | 0.954 |
| `prompt-guard.jailbreak` | 1278 | 320 | 0.809 | 0.994 |

Training data:

- `injection`: [deepset/prompt-injections](https://huggingface.co/datasets/deepset/prompt-injections) `data/train-00000-of-00001-9564e8b05b4757ab.parquet` (Apache-2.0)
- `jailbreak`: [jackhhao/jailbreak-classification](https://huggingface.co/datasets/jackhhao/jailbreak-classification) `default/jailbreak_dataset_train.csv` (Apache-2.0)

The model only answers these questions reliably, worded as in the pack. Use the base Laya
checkpoints for anything else. As with any classifier guarding an LLM, treat it as one layer of
defence.
