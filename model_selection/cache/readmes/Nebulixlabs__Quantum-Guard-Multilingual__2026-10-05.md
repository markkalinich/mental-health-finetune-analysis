---
license: apache-2.0
datasets:
- Nebulixlabs/safety-dataset
language:
- hi
- en
tags:
- Multilingual
- Hindi
- Text_Classification
- Guard
---
<div align="center">
  
# Quantum-Guard-Multilingual

**A compact 1M-parameter Transformer for `safe` / `unsafe` text classification**

<br>

<!-- Top Row: Hugging Face -->
[![Hugging Face](https://img.shields.io/badge/🤗_HUGGING_FACE-NEBULIXLABS/QUANTUM--GUARD--MULTILINGUAL-eab005?style=for-the-badge&labelColor=5b5b5b)]()

<!-- Middle Row: Socials -->
[![GitHub](https://img.shields.io/badge/GITHUB-NEBULIXLABS-000000?style=for-the-badge&logo=github&logoColor=white&labelColor=696969)](https://github.com/NebulixLabs)
[![Instagram](https://img.shields.io/badge/INSTAGRAM-NEBULIX__LABS-ee325c?style=for-the-badge&logo=instagram&logoColor=white&labelColor=696969)](https://instagram.com/nebulix_labs)

<!-- License Row -->
[![License](https://img.shields.io/badge/LICENSE-APACHE_2.0-188bf3?style=for-the-badge&labelColor=5b5b5b)]()

<br>

<!-- Bottom Rows: Technical Specs (Flat Square) -->
[![Architecture](https://img.shields.io/badge/Architecture-Custom_Transformer-8935ee?style=flat-square&labelColor=696969)]()
[![Parameters](https://img.shields.io/badge/Parameters-1,000,000-0a141f?style=flat-square&labelColor=696969)]()
[![Context](https://img.shields.io/badge/Context-128_tokens-0a141f?style=flat-square&labelColor=696969)]()
<br>
[![Tokenizer](https://img.shields.io/badge/Tokenizer-ByT5_Bytes-0a141f?style=flat-square&labelColor=696969)]()
[![Weights](https://img.shields.io/badge/Weights-SafeTensors-0a141f?style=flat-square&labelColor=696969)]()

</div>

---

## 📖 Model Overview

**Quantum-Guard-Multilingual** is a highly efficient, custom-built Transformer model containing exactly **1,000,000 parameters**. Developed by **NebulixLabs**, it is designed for ultra-fast, lightweight binary text classification to determine whether a given text is `safe` or `unsafe`. 

Because of its unique **byte-level (ByT5) encoding**, this model supports multilingual inputs out of the box, making it highly robust against prompt injections, toxic content, and spam across different languages without needing a massive vocabulary table.

## 🛠 Model Architecture

The model uses a custom `QuantumClassifier` architecture built entirely from scratch in PyTorch. By keeping the parameter count exactly at 1M, it offers blazing-fast inference speeds even on CPU.

| Specification | Value |
| :--- | :--- |
| **Total Parameters** | 1,000,000 |
| **Hidden Size (d_model)**| 112 |
| **Attention Heads** | 7 |
| **Transformer Layers** | 4 |
| **FFN Intermediate Size**| 336 |
| **Classifier Hidden Size**| 170 |
| **Max Context Length** | 128 Tokens |
| **Vocab Size** | 4096 (Base 384 + custom markers) |
| **Dropout** | 0.10 |

## 📊 Training Data

This model was trained exclusively to understand nuanced differences between safe and harmful text. The training pipeline utilized the **Nebulixlabs/safety-dataset** for high-quality instruction, query, and prompt safety alignments.

* **Training Target:** 200,000,000 non-padding tokens.
* **Batch Size:** 128
* **Optimizer:** AdamW (Mixed Precision FP16)
* **Objective:** Binary Cross-Entropy Loss (`0 = safe`, `1 = unsafe`).

## ⚙️ Tokenizer Semantics

Unlike standard BPE tokenizers, Quantum-Guard-Multilingual utilizes the official **google/byt5-small** tokenizer semantics. 
* It uses a direct **raw UTF-8 byte mapping** (Byte value `b` maps to token ID `b + 3`).
* Two model-specific sequence markers were injected: `<cls>` (ID: 384) and `<sep>` (ID: 385).
* This eliminates "Out of Vocabulary" (OOV) errors entirely and allows it to process Hindi, Hinglish, emojis, and corrupted text flawlessly.

## 🚀 How to Use (Inference)

Because this is a custom architecture (`QuantumClasifier`), you need the base class definitions to run inference. Below is a simplified snippet of how the model processes text:

```python
import torch
import torch.nn.functional as F

# Example fast-encode function mirroring the training script
def byt5_fast_encode(text, max_len=128):
    raw = text.encode("utf-8", errors="ignore")[:max_len-2]
    ids = [384] + [b + 3 for b in raw] + [385] # 384=<cls>, 385=<sep>
    length = len(ids)
    if length < max_len:
        ids.extend([0] * (max_len - length)) # 0=<pad>
    mask = [1] * length + [0] * (max_len - length)
    return ids, mask

# Assuming the model is loaded into `model` and on correct device
text = "Hello, is this safe?"
ids, mask = byt5_fast_encode(text)

input_ids = torch.tensor([ids], dtype=torch.long)
attention_mask = torch.tensor([mask], dtype=torch.bool)

model.eval()
with torch.no_grad():
    logits = model(input_ids, attention_mask)
    probabilities = torch.softmax(logits.float(), dim=-1)[0]
    
predicted_id = int(probabilities.argmax().item())
confidence = float(probabilities[predicted_id].item())

label = "safe" if predicted_id == 0 else "unsafe"
print(f"Prediction: {label} (Confidence: {confidence*100:.2f}%)")
```

## 👨‍💻 About the Author

* **Organization:** NebulixLabs
* **GitHub:** [@NebulixLabs](https://github.com/NebulixLabs)
* **Instagram:** [@nebulix_labs](https://instagram.com/nebulix_labs)
* **Hugging Face:** [@Nebulixlabs](https://huggingface.com/Nebulixlabs)

*Feel free to reach out for collaborations or questions regarding lightweight model architectures!*