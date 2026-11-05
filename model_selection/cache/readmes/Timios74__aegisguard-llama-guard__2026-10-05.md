---
library_name: transformers
tags:
  - text-classification
  - content-moderation
  - toxic-content-detection
  - hinglish
  - llama-guard
  - qlora
  - peft
  - social-media-safety
language:
  - en
  - hi
license: mit
base_model: meta-llama/Llama-Guard-3-1B
---

# AegisGuard — Toxic Content Detector for Social Media

AegisGuard is a fine-tuned version of **Llama Guard 3 1B** for 
multi-class toxic content detection on social media platforms. 
It classifies text into 5 categories and recommends a moderation 
action (allow / mute / block). Built to handle real-world social 
media content including Hinglish (Hindi + English code-mixed) text, 
jailbreak attempts, offensive content, and spam.

---

## Model Details

### Model Description

- **Developed by:** Sumit ([@Timios74](https://huggingface.co/Timios74))
- **Model type:** Text Classification (Sequence Classification)
- **Language(s):** English, Hindi, Hinglish (code-mixed)
- **License:** MIT
- **Fine-tuned from:** meta-llama/Llama-Guard-3-1B
- **Fine-tuning method:** QLoRA (4-bit NF4 quantization + LoRA adapters)
- **Task:** Multi-class toxic content detection & moderation

### Model Sources

- **Repository:** https://huggingface.co/Timios74/aegisguard-llama-guard

---

## Labels

| ID | Label | Description |
|----|-------|-------------|
| 0 | `safe` | Clean, non-toxic content |
| 1 | `hinglish_toxic` | Toxic content in Hindi/English code-mixed language |
| 2 | `guardrail_break` | Jailbreak attempts / prompt injection / harmful instructions |
| 3 | `offensive` | Offensive, hateful, or abusive content |
| 4 | `spam` | Spam, unsolicited promotional content |

---

## Uses

### Direct Use

Content moderation API for social media platforms. Classifies 
user-generated content and returns a moderation action 
(allow / mute / block) based on label and confidence score.

### Downstream Use

- Social media comment moderation
- Chat application safety filtering
- Community platform trust & safety pipelines
- Integration with AegisGuard FastAPI service

### Out-of-Scope Use

- Not intended for audio or image classification directly
- Not a replacement for human moderation on edge cases
- Not trained for legal or medical risk assessment

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

LABELS = {
    0: "safe",
    1: "hinglish_toxic", 
    2: "guardrail_break",
    3: "offensive",
    4: "spam"
}

tokenizer = AutoTokenizer.from_pretrained("Timios74/aegisguard-llama-guard")
model = AutoModelForSequenceClassification.from_pretrained(
    "Timios74/aegisguard-llama-guard",
    torch_dtype=torch.float16,
    device_map="auto"
)
model.eval()

def classify(text: str) -> dict:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=256
    ).to(model.device)
    
    with torch.no_grad():
        logits = model(**inputs).logits
        probs  = torch.softmax(logits, dim=-1)
        pred   = torch.argmax(probs, dim=-1).item()
        score  = probs[0][pred].item()
    
    label = LABELS[pred]
    return {
        "label": label,
        "confidence": round(score, 4),
        "flagged": pred != 0,
        "action": "allow" if pred == 0 else ("block" if score >= 0.90 else "mute")
    }

# Examples
print(classify("abe saale chup kar bc"))
# → {"label": "hinglish_toxic", "confidence": 0.91, "flagged": true, "action": "block"}

print(classify("Hey, how are you doing today?"))
# → {"label": "safe", "confidence": 0.98, "flagged": false, "action": "allow"}
```

---

## Training Details

### Training Data

Curated and balanced dataset of ~7,500 samples across 5 categories,
sourced from:

| Dataset | Category | Samples |
|---------|----------|---------|
| l3cube-pune/hindi-hate-speech | Hinglish toxic | ~2,500 |
| allenai/wildjailbreak | Guardrail breaks | ~1,200 |
| priyanshu977/comment-spam-dataset | Spam | ~1,000 |
| OpenAssistant/oasst2 | Safe | ~1,500 |
| lmsys/toxic-chat | Offensive + Safe | ~1,300 |

**Preprocessing:**
- Normalized text (lowercased, punctuation stripped, whitespace collapsed)
- Exact + near-duplicate removal before train/eval split
- 85/15 train/eval split with verified zero overlap
- Dataset balanced to prevent class dominance

### Training Hyperparameters

- **Training regime:** fp16 mixed precision
- **Epochs:** 3 (early stopped at epoch 3, best F1)
- **Batch size:** 8 per device
- **Gradient accumulation steps:** 4 (effective batch size: 32)
- **Learning rate:** 5e-5
- **Weight decay:** 0.01
- **Warmup ratio:** 0.1
- **Optimizer:** AdamW

### LoRA Configuration

- **Rank (r):** 16
- **Alpha:** 32
- **Target modules:** q_proj, v_proj, k_proj, o_proj
- **Dropout:** 0.1
- **Quantization:** 4-bit NF4 (QLoRA)
- **Trainable parameters:** ~4M out of 1.1B (~0.4%)

### Speeds, Sizes, Times

- **Hardware:** NVIDIA T4 GPU (16GB VRAM)
- **Cloud Provider:** Google Colab
- **Training time:** 1 hour 41 minutes
- **Model size:** 2.47GB (merged full model)

---

## Evaluation

### Results (Epoch 3 — Best Checkpoint)

| Metric | Score |
|--------|-------|
| Accuracy | 98.59% |
| F1 Macro | 95.97% |
| Validation Loss | 0.0773 |
| Training Loss | 0.1077 |

### Per-Epoch Training Curve

| Epoch | Train Loss | Val Loss | Accuracy | F1 Macro |
|-------|------------|----------|----------|----------|
| 1 | 0.2781 | 0.0620 | 97.68% | 93.79% |
| 2 | 0.2048 | 0.0708 | 98.30% | 95.52% |
| 3 | 0.1077 | 0.0773 | 98.59% | 95.97% ✅ best |
| 4 | 0.0074 | 0.0880 | 98.47% | 95.74% ← overfit |

Early stopping at epoch 3 — validation loss began rising at epoch 4
indicating onset of overfitting.

---

## Environmental Impact

- **Hardware:** NVIDIA T4 GPU
- **Hours used:** 1.41 hours
- **Cloud Provider:** Google Colab
- **Compute Region:** US (Google Cloud)
- **Carbon emissions:** Estimated via 
  [ML CO2 Impact Calculator](https://mlco2.github.io/impact#compute)

---

## Citation

If you use AegisGuard in your research or product, please cite:

**BibTeX:**
```bibtex
@misc{aegisguard2026,
  author    = {Sumit},
  title     = {AegisGuard: QLoRA Fine-tuned Llama Guard for 
               Social Media Toxic Content Detection},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/Timios74/aegisguard-llama-guard}
}
```

---

## Model Card Authors

**Sumit** — Java & AI/ML Developer, Mumbai, India  
HuggingFace: [@Timios74](https://huggingface.co/Timios74)