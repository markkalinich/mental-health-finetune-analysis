# Taiwan Medical Named Entity Recognition (NER) Model

This directory contains a fine-tuned BERT-based Token Classification model tailored for Taiwanese medical terms, surgical procedures, and medical devices.

## 🏷️ Model Labels
The model identifies the following three entity classes:
1.  **`BODY_PART`**: Anatomical regions, organs, or physiological systems (e.g. `十二指腸`, `乳房`, `角膜`, `腎臟`).
2.  **`SURGERY_TYPE`**: Surgical actions, techniques, or procedure types (e.g. `切除術`, `縫合術`, `移植`, `置換術`).
3.  **`TECH_DEVICE`**: Medical devices, surgical technologies, or specific equipment (e.g. `達文西`, `雷射`, `腹腔鏡`, `超音波乳化`).

---

## 📂 Included Files
- `model.safetensors`: Fine-tuned weights.
- `config.json`: Architecture, hyperparameters, and label definitions (`id2label` / `label2id`).
- `tokenizer.json`: Serialized tokenizer configuration.
- `tokenizer_config.json`: Instantiate arguments.

---

## 🚀 Quick Start Sample Code

Below is a complete, self-contained Python script to load the model and run inference:

```python
import os
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Model folder (local path containing these files)
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))

LABEL_LIST = ["O", "B-BODY_PART", "I-BODY_PART", "B-SURGERY_TYPE", "I-SURGERY_TYPE", "B-TECH_DEVICE", "I-TECH_DEVICE"]

def extract_entities(text: str, tokenizer, model) -> list:
    """Tokenizes text and groups token classifications into character-aligned entity spans."""
    if not text.strip():
        return []
        
    inputs = tokenizer(
        text, 
        return_offsets_mapping=True, 
        return_tensors="pt",
        truncation=True,
        max_length=512
    )
    
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**{k: v for k, v in inputs.items() if k != "offset_mapping"})
        
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=2)[0].cpu().numpy()
    offsets = inputs["offset_mapping"][0].cpu().numpy()
    
    entities = []
    current_entity = None
    
    for idx, offset in enumerate(offsets):
        start, end = offset
        # Ignore padding and special tokens
        if start == 0 and end == 0:
            continue
            
        label = LABEL_LIST[predictions[idx]]
        
        if label.startswith("B-"):
            if current_entity:
                entities.append(current_entity)
            entity_type = label.split("-")[1]
            current_entity = {
                "label": entity_type,
                "start": int(start),
                "end": int(end),
                "text": text[start:end]
            }
        elif label.startswith("I-"):
            entity_type = label.split("-")[1]
            if current_entity and current_entity["label"] == entity_type:
                current_entity["end"] = int(end)
                current_entity["text"] = text[current_entity["start"]:int(end)]
            else:
                if current_entity:
                    entities.append(current_entity)
                current_entity = {
                    "label": entity_type,
                    "start": int(start),
                    "end": int(end),
                    "text": text[start:end]
                }
        else: # 'O'
            if current_entity:
                entities.append(current_entity)
                current_entity = None
                
    if current_entity:
        entities.append(current_entity)
        
    return entities

def main():
    print(f"Loading model from {MODEL_DIR}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForTokenClassification.from_pretrained(MODEL_DIR)
    
    # Detect Apple Silicon GPU (mps), CUDA, or CPU
    device = "cpu"
    if torch.backends.mps.is_available():
        device = "mps"
    elif torch.cuda.is_available():
        device = "cuda"
    model = model.to(device)
    model.eval()
    
    # Example Inference
    test_sentence = "病患因右側腹股溝疝氣住院，在門診實施了微創內視鏡疝氣修補術。"
    entities = extract_entities(test_sentence, tokenizer, model)
    
    print(f"\nInput: {test_sentence}")
    print("Extracted Entities:")
    for ent in entities:
        print(f"  - {ent['text']} | Label: {ent['label']} | Spans: ({ent['start']}, {ent['end']})")

if __name__ == "__main__":
    main()
```

## 🛠️ Requirements
Make sure you have PyTorch and Hugging Face Transformers installed:
```bash
pip install torch transformers
```
