---
license: gemma
language:
- en
library_name: transformers
pipeline_tag: text-generation
base_model: google/gemma-3-270m-it
base_model_relation: finetune
datasets:
- google-research-datasets/go_emotions
tags:
- fine-tuned
- emotion
- berkerdooo
---

# Gemma 3 emotion tags for English comments

A 270M parameter Gemma 3 model fine-tuned to return a JSON array of emotion labels for short English comments. It supports all 27 GoEmotions categories plus neutral, including multiple labels in one comment.

## Evaluation against the base model

| Metric | Base | Fine tuned | Change |
|---|---:|---:|---:|
| Micro F1 | 0.00% | 56.23% | +56.23 points |
| Macro F1 | 0.00% | 47.58% | +47.58 points |
| Exact label match | 0.00% | 49.30% | +49.30 points |
| Valid JSON rate | 0.00% | 100.00% | +100.00 points |

Greedy generation on the same 1000 held-out comments with the same prompt and a 64-token output limit. Final evaluation ran on an Apple M5 Pro using MPS and float32 for both models. Chat-template tokens match the training prefix exactly, with no extra beginning-of-sequence token. An output counts as valid only when it is a JSON array containing known labels. Invalid outputs receive an empty prediction, including in the F1 scores. The base model tends to copy the label list inside an unfinished Markdown block; its zero scores describe this fixed prompt and 64-token limit. Macro F1 averages over all 28 categories. Validation loss on 200 examples selects the saved epoch; training examples longer than 384 tokens are omitted rather than truncated.

These results describe the fixed held-out subset from the public dataset. They do not measure general performance across other domains. evaluation.json and both prediction files provide the underlying evidence.

For context, always predicting the most common training label (neutral) gives 29.29% micro F1 and 28.80% exact match on this same test subset. This baseline uses training label frequency and no learned text representation. See reference_baseline.json.

## Training and data

Base: [google/gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m-it). Dataset: [google-research-datasets/go_emotions](https://huggingface.co/datasets/google-research-datasets/go_emotions).

Training used 17,998 examples, seed 42 and 2,250 optimizer steps on one NVIDIA L40S. The three task jobs ran concurrently. The initial training job took 29.9 minutes, including model loading, evaluation and time waiting for the other base evaluations. Subsequent evaluation and reload checks are recorded separately. This is not an isolated training-speed benchmark. Training used PyTorch 2.9.1 with CUDA 12.8, Transformers 5.16.0 and the package pins included in the repository. Arguments and environment details are saved alongside the weights.

```json
{
  "learning_rate": 5e-05,
  "per_device_train_batch_size": 4,
  "gradient_accumulation_steps": 4,
  "num_train_epochs": 2,
  "lr_scheduler_type": "cosine",
  "bf16": true,
  "seed": 42,
  "actual_training_rows": 17998,
  "optimizer_steps": 2250,
  "actual_epochs": 2.0,
  "base_revision": "ac82b4e820549b854eebf28ce6dedaf9fdfa17b3",
  "dataset_revision": "add492243ff905527e67aeb8b80c082af02207c3",
  "selected_checkpoint": "checkpoint-1125"
}
```

Dataset split counts: {"test": {"count": 1000, "duplicates_removed": 0}, "validation": {"count": 500, "duplicates_removed": 1}, "train": {"count": 18000, "duplicates_removed": 42}}. Fixed-seed shuffled official splits, exact-text duplicates removed with test and validation taking priority.

## Usage

Install the pinned packages in reproduce/requirements-gpu.txt with a compatible PyTorch build, then run:

```python
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
repo = "berkerdooo/gemma-3-270m-goemotions"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, device_map="auto")
labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
instruction = "Classify the emotions expressed in the following text. Return only a JSON array of labels from this list: " + ", ".join(labels) + ". Multiple labels are allowed. Use neutral when no emotion is expressed.\nText: "
messages = [{"role": "user", "content": instruction + "I love this! Thank you so much."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_dict=True, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=64, do_sample=False)
text = tokenizer.decode(output[0, inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(json.loads(text))
```

## Scope and limitations

The test measures agreement with GoEmotions annotations on Reddit comments. Labels describe emotions expressed in text, rather than a person’s internal mental state. Reddit language, annotator judgments and class imbalance limit transfer to brand comments and other domains. Rare labels have little training coverage.

## Reproduce the run

The reproduce folder contains the training script, shared helpers, preparation code, package pins and revision manifest. Run `PREPARE_TASKS=emotion python prepare.py` to prepare this task locally, then copy the prepared data and any downloaded base weights into the GPU environment. Gemma 3 access must be approved on Hugging Face before downloading its base. The scripts compare the unchanged base with the fine-tuned model and coordinate concurrent starts through base_ready markers. For a standalone run, set FINETUNE_TASKS=emotion before executing the training script. Training and evaluation use the official splits with the documented fixed-seed sampling.

The final comparison was re-scored on the Mac GPU with `python reevaluate_local.py outputs/emotion`, using float32 for both models. This changes evaluation only; the validation-selected weights are unchanged.

## License and attribution

Weights remain subject to the [Gemma Terms of Use](https://ai.google.dev/gemma/terms), including their use and distribution conditions. See LICENSE, USE_POLICY and NOTICE.

Training data is published under Apache License 2.0 by Google Research and the GoEmotions authors. The dataset revision and preprocessing are recorded in data_manifest.json.

Fine-tune prepared for berkerdooo. Base model credit belongs to Google DeepMind and the Gemma team.
