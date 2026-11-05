---
license: apache-2.0
language:
- en
base_model:
- answerdotai/ModernBERT-large
datasets:
- dzur658/therapy-conversations-full-small
---

TherapyBERT RE 001 is a model designed for Relationship Extraction given
2 psychotheraputic entities. The model was trained on a total of 15,840 examples,
where the model had to choose the appropriate label for the relationship, or `NONE` if
there was no relationship between the entities. The model implements a classifier head
on top of `ModernBERT-large` in order to take advantage of the extended context window.

## Intended Use
This RE model is intended to be used by [TherapyBERT](https://github.com/dzur658/therapy-bert) for
on device processing of entities extracted by the [TherapyBERT NER model](https://huggingface.co/dzur658/TherapyBERT-NER-001)

## Valid Psychotherapy Relationships
- `NONE` (No relationship between entities)
- `CAUSES`
- `WORSENS`
- `IMPROVES`
- `RELATES_TO`
- `EXPERIENCES`
- `TRIGGERS`

## How to use this Model
First use the hf download tool to download the repo `hf download
dzur658/TherapyBERT-RE-001 --local-dir .`

*Ensure the huggingface hub tool is [installed](https://huggingface.co/docs/huggingface_hub/guides/cli#getting-started)*

You will need the [classification head to load this model](https://github.com/dzur658/therapy-bert/blob/main/modern_bert_re_layers.py).

Then load the model like so:
```python
import torch
from transformers import AutoTokenizer

# make sure the classification head is present before importing!
from modern_bert_re_layers import ModernBERT_Entity_Pooling_RE

from typing import Dict, List, Optional, Sequence, Tuple, Union
import re

UNIQUE_LABELS = ["NONE", "CAUSES", "WORSENS", "IMPROVES", "RELATES_TO", "EXPERIENCES", "TRIGGERS"]

# here we load the base tokenizer, but since we added 4 new tokens
# for entity extraction we will have to manually add them below
TOKENIZER_MODEL = "answerdotai/ModernBERT-large"
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_MODEL)

# add special tokens for entity extraction
SPECIAL_TOKENS = {"additional_special_tokens": ["[E1]", "[/E1]", "[E2]", "[/E2]"]}
tokenizer.add_special_tokens(SPECIAL_TOKENS)

# use on cuda, mps, or cpu
# for example cuda
device = torch.device("cuda")

# set path to weights/config
MODEL_PATH = "./therapy-modernbert-re-final"

model = ModernBERT_Entity_Pooling_RE.from_checkpoint(
		MODEL_PATH,
		tokenizer=tokenizer,
		map_location=device,
	)

# set to eval mode for inference
model.eval()

# cast bf16 to cuda/mps, for cpu use fp32 operations
model.to(device, dtype=torch.bfloat16 if device.type in ["cuda", "mps"] else torch.float32)

# example input
test_cases = [
		(
			"My anxiety has been getting worse since the calls from my ex-husband started again.",
			"ex-husband",
			"anxiety",
		),
		(
			"I avoid crowded stores because the flashing lights can trigger a panic attack.",
			"flashing lights",
			"panic attack",
		),
	]

# helper function to extract entities from the text
def mark_entities(text: str, source: str, target: str) -> str:
	if not source or not target:
		raise ValueError("Both source and target entity strings are required.")

	marked_text = re.sub(f"({re.escape(source)})", r"[E1]\1[/E1]", text, count=1)
	marked_text = re.sub(f"({re.escape(target)})", r"[E2]\1[/E2]", marked_text, count=1)

	if "[E1]" not in marked_text or "[E2]" not in marked_text:
		raise ValueError("Could not find both entities in the provided text.")

	return marked_text

# inference function
def predict_marked_text(marked_text: str, top_k: Optional[int] = 1) -> Union[Dict[str, float], List[Dict[str, float]]]:
    # supports full 8192 token context window
    max_len = 8192

    inputs = tokenizer(
        marked_text,
        return_tensors="pt",
        truncation=True,
        max_length=max_len,
    )
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs["logits"]
        probabilities = torch.softmax(logits, dim=-1)[0]

        scores, indices = torch.sort(probabilities, descending=True)
        predictions = [
            {
                "label": model.id2label[int(index)],
                "score": float(score),
            }
            for score, index in zip(scores.tolist(), indices.tolist())
        ]
        
        if top_k is None:
            return predictions

        limited_predictions = predictions[:top_k ]

        if top_k == 1:
            return limited_predictions
        else:
            return limited_predictions

for case in test_cases:
    print(case)
    text, source, target = case
    marked_text = mark_entities(text, source, target)

    # top k can be passed here otherwise defaults to 1
    predictions = predict_marked_text(marked_text, top_k=3)
    for pred in predictions:
      print(f" -> {pred['label']}: {pred['score']:.4f}")
    print("-" * 80)
```

## Response
```
('My anxiety has been getting worse since the calls from my ex-husband started again.', 'ex-husband', 'anxiety')
 -> IMPROVES: 0.2754
 -> NONE: 0.2246
 -> TRIGGERS: 0.1777
--------------------------------------------------------------------------------
('I avoid crowded stores because the flashing lights can trigger a panic attack.', 'flashing lights', 'panic attack')
 -> TRIGGERS: 0.4883
 -> NONE: 0.1895
 -> CAUSES: 0.1162
--------------------------------------------------------------------------------
```

## Model Training Recipe
- Classification head is attached with randomly initialized weights
- First epoch trains the new embeddings for entity markers, and classification head while base model remains frozen (lr: `1e-3`)
- Thaw everything and train until the model obtaining the best F1 Macro

## Best Model Metrics
- Epoch 3 after system thaw
- `eval_loss`: 0.9485
- `eval_accuracy`: 0.6974
- `eval_f1_macro`: 0.2671

*NOTE: this is the first version of this model, and it is highly
susceptible to guessing "NONE" due to class imbalance. Future versions
of the model should address this, but this is why there is a major
discrepancy between the accuracy and f1 score.*

## Ethical Considerations
This model is intended to be ran locally on a therapist's device, and not hosted due to data privacy concerns. Just like any model it is prone to making mistakes, review outputs carefully.

## Project
[Github](https://github.com/dzur658/therapy-bert/tree/main)

## Citation
```
@misc{TherapyBERT RE,
    title  = {TherapyBERT RE 001},
    author = {{Alex Dzurec}},
    month  = {March},
    year   = {2026},
    url    = {https://huggingface.co/dzur658/TherapyBERT-RE-001}
}
```