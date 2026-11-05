---
license: apache-2.0
language:
- en
base_model:
- answerdotai/ModernBERT-large
pipeline_tag: token-classification
datasets:
- dzur658/therapy-conversations-full-small
---

# TherapyBERT NER
TherapyBERT NER 001 is a model designed for Named Entity Recognition of entities in patient transcripts from a psychotheraputic setting. The model was trained on ~3,500
examples (full dataset to be released soon) of synthetic therapy transcripts. Building off ModernBERT, this model implements a Conditional Random Field (CRF) head in order to ensure proper IOB
tags are always returned. These rules are futher enforced in the CRF layer by initialzing the CRF heads weights to a large negative number before training on paths that would
break IOB syntax.

In practice this **prevents** the following NER model errors

- `O, O, I - Entity, O`
- `O, B - Entity, I - Different Entity, O`

For those unfamiliar, CRFs allow one to take the multidimensional output of a model (like ModernBERT-large), and calculate the probabilities of expected
tokens in a structure aware method via the [Viterbi algorithm](https://en.wikipedia.org/wiki/Viterbi_algorithm).

## Intended Use
This NER model is intended to be used by [TherapyBERT](https://github.com/dzur658/therapy-bert/tree/main)
for on device processing of 2 way client-patient therapy conversations.

## Valid Psychotherapy Entities
- `Symptom`
- `Trigger`
- `Emotion`
- `Person`
- `Coping_Mechanism`
- `Life_Event`
- `Behavior`

## How to use this Model
First use the hf download tool to download the repo
`hf download dzur658/TherapyBERT-NER-001 --local-dir .`

*Ensure the huggingface hub tool is [installed](https://huggingface.co/docs/huggingface_hub/guides/cli#getting-started).*

You will need the [CRF layer to load this model](https://github.com/dzur658/therapy-bert/blob/main/ner_crf_layer.py).

Then load the model like so:

```python
import torch
from transformers import AutoTokenizer

# Contains the custom Condtional Random Field head
from ner_crf_layer import ModernBERT_CRF

# get original ModernBERT Large Tokenizer
tokenizer = AutoTokenizer.from_pretrained("answerdotai/ModernBERT-large")

# your accelerator
device = "cuda"

# load model using the from checkpoint function
model = ModernBERT_CRF.from_checkpoint("[REPLACE ME WITH PATH TO REPO]", map_location=device)

model.eval()
model.to(device)

def extract_entities(text, tokenizer, model, device):
    print(f"\nAnalyzing: '{text}'")
    
    # Tokenization
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=8192)
    inputs_to_device = {k: v.to(device) for k, v in inputs.items()}
    
    with torch.no_grad():
        # The model's forward pass automatically runs the CRF Viterbi decode
        predicted_paths = model.decode(**inputs_to_device)
        
    pred_ids = predicted_paths[0]
    input_ids = inputs["input_ids"][0].tolist() # Extract the raw integers
    
    entities = []
    current_entity = None
    
    for idx, tag_id in enumerate(pred_ids):
        token_id = input_ids[idx]
        
        # PROPERLY skip special tokens ([CLS], [SEP], [PAD])
        if token_id in tokenizer.all_special_ids:
            continue
            
        tag = model.id2label[tag_id]
        
        # If it's a B- tag, start a new entity
        if tag.startswith("B-"):
            if current_entity:
                # Decode the accumulated token IDs all at once!
                current_entity["text"] = tokenizer.decode(current_entity["token_ids"]).strip()
                del current_entity["token_ids"] # Clean up the dictionary
                entities.append(current_entity)
            
            # Store the raw ID, not the string
            current_entity = {"type": tag[2:], "token_ids": [token_id]}
            
        # If it's an I- tag, append the raw ID to the array
        elif tag.startswith("I-") and current_entity and current_entity["type"] == tag[2:]:
            current_entity["token_ids"].append(token_id)
            
        # If it's an O tag, finalize the current entity
        elif tag == "O":
            if current_entity:
                current_entity["text"] = tokenizer.decode(current_entity["token_ids"]).strip()
                del current_entity["token_ids"]
                entities.append(current_entity)
                current_entity = None
                
    # Catch the edge case where the sequence ends exactly on an entity
    if current_entity:
        current_entity["text"] = tokenizer.decode(current_entity["token_ids"]).strip()
        del current_entity["token_ids"]
        entities.append(current_entity)
        
    if not entities:
        return {"entities": []}

    return {"entities": entities}

text_to_analyze = "My anxiety has been through the roof since my ex-husband called me."

entities_obj = extract_entities(text_to_analyze, tokenizer, model, device)
print(entities_obj)
```

#### Model Response
```
{'entities': [{'type': 'Symptom', 'text': 'anxiety has been through the roof'}, {'type': 'Person', 'text': 'my ex-husband'}]}
```

## Model Training Recipe
- The CRF head is attached with randomly intialized weights (except the negatively incentivzed weights to guard against breaking IOB rules).
- Freeze & Thaw Cycle the ModernBERT-large base is frozen for the first epoch and only the CRF is trained (lr: `1e-3`)
- Thaw ModernBERT and train whole system until best model is attained (lr: `2e-6`)
- Metric for best model: `eval_loss`

Metric Rationale: `eval_loss` was used as a metric due to the specific dataset this model was trained on.
The model trained on synthetic therapy conversations, which were further IOB marked by the same LLM.
As a result, the "ground truth" of entities tended to include extraneous surrounding words.

## Best Model Metrics
- Epoch 6 after system thaw
- `eval_loss` : 96.26
- `eval_precision` : 0.4422
- `eval_recall` : 0.2496
- `eval_f1` : 0.3191
- `eval_accuracy` : 0.9003

NOTE: As mentioned above due to an LLM creating the IOB pairs, certain "fluff" tokens were included in the dataset entities. This caused eval f1 to
be artificially low on paper.

For example
If the dataset contains the entity: `the cat` and the model predicts `cat` the f1 score for that single prediction is: `0`
If the dataset contains the entity: `the cat` and the model predicts `the cat` the f1 score for that single prediction is: `1`

## Ethical Considerations
This model is intended to be ran locally on a therapist's device, and not hosted due to data privacy concerns. Just like any model it is prone to making mistakes,
review outputs carefully.

## Project
[Github](https://github.com/dzur658/therapy-bert/tree/main)

## Citation
```
@misc{TherapyBERT NER 001,
    title  = {TherapyBERT NER 001},
    author = {{Alex Dzurec}},
    month  = {March},
    year   = {2026},
    url    = {https://huggingface.co/dzur658/TherapyBERT-NER-001}
}
```