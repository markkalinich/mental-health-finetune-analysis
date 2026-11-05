---
license: apache-2.0
base_model: google/medgemma-1.5-4b-it
tags: [medical, dermatology, adverse-event-detection, medgemma]
---
# MedGemma AE Detection

MedGemma 1.5-4B fine-tuned for **visual adverse event detection** from clinical photographs.

- **Base model**: `google/medgemma-1.5-4b-it`
- **Method**: LoRA fine-tuning (50 epochs)
- **Task**: Classify skin AEs from patient photos into 21 categories (normal + 7 AE types × 3 CTCAE grades)
- **AE types**: maculopapular rash, acneiform rash, periorbital edema, SJS, stomatitis, pruritus, alopecia

## Usage

```python
from transformers import AutoModelForImageTextToText, AutoProcessor

model = AutoModelForImageTextToText.from_pretrained("AlphaRaven/medgemma-ae-detection")
processor = AutoProcessor.from_pretrained("google/medgemma-1.5-4b-it")
```

Part of the [Clinical Trial Simulation Engine](https://github.com/AlphaRaven/ClinicalTrialEngine) pipeline.
