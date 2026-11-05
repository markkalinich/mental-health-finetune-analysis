---
license: other
license_name: health-ai-developer-foundations-terms-of-use
license_link: https://developers.google.com/health-ai-developer-foundations/terms
base_model: newmes/medgemma-4b-antihallu
base_model_relation: finetune
pipeline_tag: image-text-to-text
library_name: transformers
language:
  - en
tags:
  - medical
  - medgemma
  - hai-def
  - adverse-event-detection
  - dermatology
  - ctcae
  - clinical-trial
  - lora
  - medgemma-impact-challenge
datasets:
  - newmes/clinical-trial-engine-data
---

# MedGemma AE Detection

**MedGemma 4B fine-tuned to grade visible adverse events (AEs) from patient photographs.**
Part of [CLARA](https://github.com/newmes/clara-web), NEWMES AI team's submission to the
[MedGemma Impact Challenge](https://www.kaggle.com/competitions/med-gemma-impact-challenge) (Kaggle, Feb 2026).

| | |
|---|---|
| Task | Classify a skin/face photo into **21 classes** = normal + 7 AE types × CTCAE grade 1–3 |
| AE types | maculopapular rash, acneiform rash, periorbital edema, SJS prodrome, stomatitis, pruritus, alopecia |
| Initialised from | [`newmes/medgemma-4b-antihallu`](https://huggingface.co/newmes/medgemma-4b-antihallu) (MedGemma 4B + RLFR anti-hallucination) |
| Method | LoRA fine-tuning, 50 epochs, adapters merged into the base weights (bf16, 8.6 GB) |
| Training data | 210 Gemini-generated synthetic patient images, 147 / 21 / 42 train / val / test ([dataset](https://huggingface.co/datasets/newmes/clinical-trial-engine-data) → `ae_images/`) |
| Role in CLARA | Data Collection Agent: compares today's CLARA Call video frame with the patient's baseline photo and reports new AEs with a CTCAE grade |

## Results

Held-out test set: 42 synthetic images (2 per class). Exact-match accuracy on the 21-class label (AE type **and** grade).

| Model | Accuracy | Correct |
|---|---|---|
| MedGemma 4B zero-shot | 28.6 % | 12 / 42 |
| **MedGemma 4B fine-tuned (this model)** | **85.7 %** | **36 / 42** |
| MedSigLIP-448 zero-shot | 28.6 % | 12 / 42 |
| MedSigLIP-448 + linear probe | 61.9 % | 26 / 42 |

Remaining errors are mostly off-by-one grade (e.g. pruritus G3 → G2) or normal ↔ grade 1 confusion.
The full comparison, per-AE detection rates and a before/after gallery are in
[`notebooks/2_medgemma+medsiglip+HeAR_SAE-detection.ipynb`](https://github.com/newmes/clara-web/blob/main/notebooks/2_medgemma%2Bmedsiglip%2BHeAR_SAE-detection.ipynb).

## Usage

```python
import torch
from PIL import Image
from transformers import AutoModelForImageTextToText, AutoProcessor

repo = "newmes/medgemma-ae-detection"
model = AutoModelForImageTextToText.from_pretrained(repo, torch_dtype=torch.bfloat16, device_map="auto")
processor = AutoProcessor.from_pretrained(repo)

baseline = Image.open("baseline.jpg")   # pre-treatment photo
current  = Image.open("today.jpg")      # today's check-in frame

messages = [{
    "role": "user",
    "content": [
        {"type": "image", "image": baseline},
        {"type": "image", "image": current},
        {"type": "text", "text":
         "Image 1 is the patient's baseline photo, Image 2 was taken today. "
         "Identify any new adverse event visible in Image 2 that is NOT present in Image 1 "
         "and grade it with CTCAE v5. Answer with one of: normal, or <ae_type> grade <1-3>. "
         "AE types: maculopapular rash, acneiform rash, periorbital edema, SJS prodrome, "
         "stomatitis, pruritus, alopecia."},
    ],
}]

inputs = processor.apply_chat_template(messages, add_generation_prompt=True,
                                       tokenize=True, return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=64, do_sample=False)
print(processor.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

The model also works with a single image; the two-image prompt is how it is used inside CLARA.
Recommended: bf16, one 24 GB GPU; served in CLARA via vLLM.

## Intended use and limitations

- **Research / demonstration only.** Not a medical device, not clinically validated, not for diagnostic use.
- Trained and tested exclusively on **synthetic (Gemini-generated) images** — performance on real patient photos is unknown.
- Covers 7 dermatologic/visible AE types only; anything else is out of distribution.
- Tiny test set (42 images); accuracy figures have wide confidence intervals.
- Inherits the [Health AI Developer Foundations terms of use](https://developers.google.com/health-ai-developer-foundations/terms) from MedGemma.

## About CLARA

CLARA (Clinical Longitudinal AI Research Assistant) tackles the 12–21-day blind spot between oncology-trial clinic visits:
a daily ~60-second video + voice check-in (**Data Collection Agent**, on-device) feeds a longitudinal timeline with AE/SAE flagging and
automatic MedWatch 3500A / E2B(R3) reports (**Data Analysis Agent**). A rule-based clinical-trial simulator (100 patients × 126 days,
7 real drug profiles) is used to quantify the benefit: mean AE detection delay 4.6 → 1.2 days, deaths 21 → 16 per 100 patients.

HAI-DEF models used: MedGemma 1.5 4B (nurse dialogue, visual AE grading), MedSigLIP-448 (frame classification), HeAR (dry/wet cough), MedASR (medical speech recognition).

- Code: [newmes/clara-web](https://github.com/newmes/clara-web) · iOS app: [newmes/clara-app](https://github.com/newmes/clara-app)
- Sibling model: [newmes/medgemma-4b-antihallu](https://huggingface.co/newmes/medgemma-4b-antihallu) · data: [newmes/clinical-trial-engine-data](https://huggingface.co/datasets/newmes/clinical-trial-engine-data)
- Competition: [The MedGemma Impact Challenge](https://www.kaggle.com/competitions/med-gemma-impact-challenge) — Google Research / HAI-DEF, $100 000 prize pool, final submission 2026-02-24, 850+ teams. Judged on effective use of HAI-DEF models, problem importance, real-world impact, technical feasibility, and execution.

> Originally published as `AlphaRaven/medgemma-ae-detection` (2026-02-23); moved to the `newmes` organization in Sep 2026. Weights are identical.

## Citation

```bibtex
@misc{clara2026,
  title  = {CLARA: Clinical Longitudinal AI Research Assistant},
  author = {NEWMES AI Team},
  year   = {2026},
  url    = {https://github.com/newmes/clara-web},
  note   = {MedGemma Impact Challenge submission}
}
```
