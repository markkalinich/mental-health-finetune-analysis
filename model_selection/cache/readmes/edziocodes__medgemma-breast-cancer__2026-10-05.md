---
license: mit
language:
- en
base_model:
- google/medgemma-4b-it
pipeline_tag: image-text-to-text
metrics:
- accuracy
- f1
library_name: transformers
tags:
- generated_from_trainer
- trl
- sft
- medical
- breast_cancer
- 2d
model-index:
- name: medgemma-breast-cancer
  results:
  - task:
      type: image-text-to-text
    dataset:
      name: 2D Mammograms + DeepSight Cancer Annotations (Balanced)
      type: image-text-to-text
      link: https://doi.org/10.7910/DVN/KXJCIU
    metrics:
    - name: accuracy
      type: accuracy
      value: 0.9888
    - name: f1
      type: f1
      value: 0.9888
    - name: sensitivity
      type: sensitivity
      value: 0.9966
    - name: specificity
      type: specificity
      value: 0.9810
---

# MedGemma-4B OMAMA 256x256 (Balanced)

This model is a fine-tuned version of google/medgemma-4b-it adapted for binary mammogram classification on the OMAMA 256×256 dataset.
The dataset consists of ~154k mammogram image slices (.npz) with metadata JSONs providing labels (NonCancer, Cancer). We created a **balanced subset** of 2,942 samples (50% Cancer, 50% NonCancer) to prevent class imbalance issues.
Fine-tuning was performed with LoRA (Low-Rank Adaptation) for parameter-efficient adaptation, then merged into a standalone full model for easy inference. Training was run on an NVIDIA H200 GPU for 8 epochs.

## 🔬 Model Details

* **Base Model**: [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it)
* **Dataset**: [2D Mammograms + DeepSight Cancer Annotations](https://doi.org/10.7910/DVN/KXJCIU)

    Haehn, Daniel; Zurrin, Ryan; Goyal, Neha; Bendiksen, Benni; Manocha, Muskaan; Simovici, Dan; Haspel, Nurit; Pomplun, Marc; Lotter, Bill; Sorensen, Greg.  
    2D Mammograms + DeepSight Cancer Annotations. Harvard Dataverse, V1, 2024.  
    https://doi.org/10.7910/DVN/KXJCIU

* **Fine-tuning Approach**: Supervised fine-tuning (SFT) using [Transformers Reinforcement Learning (TRL)](https://github.com/huggingface/trl)
* **Task**: Breast Cancer classification from 2D mammogram images
* **Pipeline Tag**: `image-text-to-text`
* **Dataset Balance**: 50% Cancer / 50% NonCancer (2,942 total samples)

## 📊 Performance

**Evaluation Results on Balanced Test Set:**
- **Accuracy**: 98.88%
- **Sensitivity** (Cancer Detection Rate): 99.66%
- **Specificity** (NonCancer Detection Rate): 98.10%
- **F1 Score**: 98.88%
- **False Negative Rate**: 0.34% (5 missed cancers out of 1,471)
- **False Positive Rate**: 1.90% (28 false alarms out of 1,471)

**Compared to Baseline** (same prompt format, no fine-tuning):
- Accuracy: 91.60% → 98.88% (+7.28 percentage points)
- Sensitivity: 83.48% → 99.66% (+16.18 percentage points)
- Specificity: 99.73% → 98.10% (-1.63 percentage points)

## 🚀 Inference Example

```python
# pip install transformers accelerate
# Inference for merged MedGemma-4B (OMAMA 256×256 Balanced)
# Replace with your repo id:
REPO_ID = "edziocodes/medgemma-breast-cancer"

import re, torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForImageTextToText

device = "cuda" if torch.cuda.is_available() else "cpu"

# (Optional) small speed win on Ampere/Hopper
torch.backends.cuda.matmul.allow_tf32 = True

processor = AutoProcessor.from_pretrained(REPO_ID)
model = AutoModelForImageTextToText.from_pretrained(
    REPO_ID,
    torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32,
).to(device).eval()

# --- Build the same prompt used for training ---
PROMPT = "Classify this mammogram.\nA: NonCancer\nB: Cancer"

def build_messages():
    return [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": PROMPT},
            ],
        }
    ]

# --- Simple, forgiving post-processing to map text → label index/name ---
NONC_RX = re.compile(r"\bnon[-\s]*cancer\b", re.I)
CANC_RX = re.compile(r"\bcancer\b", re.I)

def map_text_to_label(text: str) -> str:
    t = text.strip()
    # prefer explicit A/B if present
    if re.search(r"\bA\b", t) and NONC_RX.search(t):
        return "NonCancer"
    if re.search(r"\bB\b", t) and CANC_RX.search(t):
        return "Cancer"
    # fallback by keywords
    if CANC_RX.search(t) and not NONC_RX.search(t):
        return "Cancer"
    if NONC_RX.search(t):
        return "NonCancer"
    return f"Unparsed: {t}"

# -------- Single image inference --------
img = Image.open("example.png").convert("RGB")   # your image path

messages = build_messages()
prompt = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)

inputs = processor(text=prompt, images=img, return_tensors="pt").to(device)
# Cast only float tensors to bf16 on GPU
for k, v in inputs.items():
    if torch.is_floating_point(v):
        inputs[k] = v.to(torch.bfloat16)

with torch.inference_mode():
    out = model.generate(
        **inputs,
        max_new_tokens=40,
        do_sample=False,         # deterministic
        disable_compile=True,    # safer across envs
    )

# Slice off the prompt tokens before decoding (continuation only)
prompt_len = inputs["input_ids"].shape[-1]
text = processor.decode(out[0, prompt_len:], skip_special_tokens=True)
print("Raw generation:", text)
print("Predicted label:", map_text_to_label(text))

# -------- (Optional) batched inference --------
imgs = [Image.open(p).convert("RGB") for p in ["ex1.png", "ex2.png", "ex3.png"]]
prompts = [prompt] * len(imgs)
enc = processor(text=prompts, images=[[im] for im in imgs], return_tensors="pt", padding=True).to(device)

for k, v in enc.items():
    if torch.is_floating_point(v):
        enc[k] = v.to(torch.bfloat16)

lens = enc["attention_mask"].sum(dim=1)  # per-example prompt length

with torch.inference_mode():
    outs = model.generate(**enc, max_new_tokens=40, do_sample=False, disable_compile=True)

for seq, ln in zip(outs, lens.tolist()):
    txt = processor.decode(seq[int(ln):], skip_special_tokens=True)
    print("→", map_text_to_label(txt))
```

**Expected Output:**

```text
Raw generation: A: NonCancer
Predicted label: NonCancer
```

## 🎯 Training Details

- **LoRA Rank**: 16
- **LoRA Alpha**: 16
- **Target Modules**: all-linear (both vision encoder and text model)
- **Training Samples**: 2,942 (balanced 50/50 split)
- **Epochs**: 8
- **Batch Size**: 1 per device
- **Gradient Accumulation**: 16 steps
- **Effective Batch Size**: 16
- **Learning Rate**: 2e-4
- **LoRA Dropout**: 0.05
- **Optimizer**: AdamW (paged_adamw_8bit)
- **GPU**: NVIDIA H200 (143GB VRAM)

## 🏥 Clinical Impact

The fine-tuned model achieves **99.66% sensitivity**, meaning it correctly identifies cancer in 99.66% of malignant cases. This high sensitivity is crucial for screening applications where missing cancer cases has severe consequences.

The trade-off is a slight increase in false positive rate (1.90%), which is acceptable in a clinical workflow where suspicious cases undergo additional review by radiologists.

**Key Improvements:**
- Reduced false negatives from 243 → 5 cases (98% reduction)
- Maintained high specificity (98.10%)
- Balanced performance across both classes

## 🧪 Intended Use

This model is intended for research and educational purposes related to medical imaging, specifically breast cancer classification. It is **not** a certified diagnostic tool and should not be used in clinical decision-making without further validation.

## 📝 Citation

If you use this model, please cite:

```bibtex
@misc{medgemma-breast-cancer-2025,
  author = {Edward Gaibor},
  title = {MedGemma Fine-tuned for Breast Cancer Detection on Balanced OMAMA Dataset},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/edziocodes/medgemma-breast-cancer}
}
```

## 🙏 Acknowledgments

- Base model: Google's MedGemma-4B-IT
- Dataset: OMAMA Mammography Dataset (Haehn et al., 2024)
- Fine-tuning framework: Hugging Face PEFT & TRL

## 🏷️ Tags

* `medical`
* `breast_cancer`
* `mammograms`
* `trl`
* `sft`
* `balanced_dataset`
* `lora`
