---
license: apache-2.0
datasets:
- obx0x3/empathy-dementia
language:
- en
- fr
metrics:
- bleu
---

## Empathy Dementia 
A fine‑tuned multilingual T5‑Base model for empathetic responses designed for individuals with dementia.

## Training Corpus
- **Data splits:**
  - Training: 120 examples
  - Validation: 30 examples
  - Test: 30 examples
- **Languages:** English (`"en"`) and French (`"fr"`)
- **Data structure:** Each sample includes:
  ```json
  {
    "input": "Where are my glasses?",
    "target": "Let’s look together. Maybe near your chair.",
    "lang": "en"
  }
## Training Results (Cross-Entropy Loss)

| Epoch | Training Loss | Validation Loss |
|-------|---------------|-----------------|
| 1     | 0.191100      | 0.101121        |
| 2     | 0.119100      | 0.061524        |
| 3     | 0.103100      | 0.042741        |
| 4     | 0.079900      | 0.038426        |

# Usage:

```
from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("obx0x3/empathy-dementia")
tokenizer = T5Tokenizer.from_pretrained("obx0x3/empathy-dementia")

def empathetic_response(prompt, lang="en"):
    prefix = "emotion: " if lang == "en" else "émotion: "
    input_ids = tokenizer(prefix + prompt, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_length=50)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
```

# Example
```
print(empathetic_response("I feel so lonely.", lang="en"))
print(empathetic_response("Je me sens seul.", lang="fr"))
```

## Intended Use & Limitations
MSc Dissertion Proof of concept and work for primary use case: Aid communication with individuals experiencing memory loss, confusion, or distress

NOT for clinical decisions — designed as a supportive tool
