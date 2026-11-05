---
library_name: transformers
license: other
license_name: health-ai-developer-foundations
license_link: https://developers.google.com/health-ai-developer-foundations/terms
base_model: google/medgemma-4b-it
model_type: image-text
tags:
  - medgemma
  - merged-weights
  - health-ai
  - lora
extra_gated_heading: Accept the Health-AI Developer Foundations Terms
extra_gated_prompt: |
  By downloading these weights you agree to the Google Health-AI Developer Foundations
  Terms of Use and the § 3.2 prohibited-use policy (non-clinical use, etc.).
extra_gated_button_content: I agree
model-index:
- name: medgemma4b_yma_health_merged
  results: []
---
# YmaHealth · MedGemma-4B-IT GLP-1 Specialist

**A 4-billion-parameter vision-and-language model specialising in GLP-1–related diabetes care**, obtained by merging our LoRA adapters into Google’s *MedGemma-4B-IT* base model.  
It answers text-only queries (image grounding unchanged).

---

## 🩺 Why we built this model
* GLP-1 agonists (semaglutide, liraglutide, etc.) are rapidly transforming Type-2 diabetes care.  
* Existing open LLMs lack up-to-date, peer-reviewed knowledge and struggle with the empathetic tone required in doctor-patient dialogue.  
* Our goal is **clinical decision *support*** and **patient education**, *not* automated diagnosis.

---

## 1 Data preparation&nbsp;🗄️

| Layer | Sources | Rationale |
|-------|---------|-----------|
| **1️⃣ Medical guidelines & protocols** | ~100 recent (≤ 3 y) U.S. endocrine society documents | Guarantees latest treatment algorithms |
| **2️⃣ Scientific studies & reviews** | ~200 peer-review papers / meta-analyses on semaglutide & peers | High-evidence risk/benefit data |
| **3️⃣ General medical knowledge** | Textbooks + open datasets (e.g. MedMCQA) | Terminology & pathophysiology grounding |
| **4️⃣ Real-world consultations** *(anonymised; consented)* | Transcripts of doctor–patient visits | Teaches natural, empathetic tone (↑ satisfaction ×1.5–2; Johri 2023) |
| **5️⃣ Safety / awareness corpora** | Adversarial & sensitive-topic prompts | Model defers to clinicians when unsure |

*All 100 k QA/dialogue records were de-duplicated, cleaned, and medically reviewed (Clusmann 2023).*

---

## 2 Training pipeline&nbsp;⚙️

| Phase | Method | Goal |
|-------|--------|------|
| **Base** | `google/medgemma-4b-it` FP16 | Vision-language backbone |
| **SFT-LoRA** | Supervised fine-tuning on GLP-1 QA | Teach domain facts |
| **DPO-LoRA** | Direct Preference Optimisation (Dubey 2024) on paired outputs | Align tone & user preference (concise + empathetic) |
| **Merge** | `merge_and_unload()` → 3-shard *.safetensors* | Single checkpoint for inference |

Hyper-params (SFT): LR 5e-5 · batch 64 (grad-acc 16 × 2 GPU) · cosine schedule · 2 epochs  
DPO used the same hardware with a 0.1 preference LR.

---

## 3 Intended use&nbsp;✅

* **Patient education** on GLP-1 therapy, lifestyle, side-effects.  
* **Clinical decision support** tools *with a licensed professional in the loop*.  
* **Research** on safe medical-AI interaction patterns.

## 4 Limitations&nbsp;⚠️

* **Not a medical device.** No autonomous diagnosis, prescription or emergency triage.  
* Knowledge cut-off ≈ Nov 2024 (last guideline snapshot).  
* English-centric; performance on other languages untested.  
* Does **not** improve image grounding—the original MedGemma capabilities apply.

---

## 5 Safety & ethical compliance 🔒

We follow the [Reforma Health SLM validation & ethics framework](https://reforma-health.notion.site/How-we-make-sure-our-SLMs-are-Clinically-Valid-and-Ethically-Compliant-1b68eefe86f48172b5eed54bd30a44e4):

1. **Data governance** – HIPAA-compatible storage, PHI stripping, dual expert audit.  
2. **Clinical QA** – 2-tier review (physician + pharm.D) for every model change.  
3. **Bias testing** – evaluate across age, sex, ethnicity, insurance status.  
4. **Harm safeguard** – refusal / hand-off when confidence < 0.65 or question out-of-scope.  
5. **Continual monitoring** – nightly hallucination & toxicity sweeps; flagged outputs re-enter DPO set.

---

## 6 Quick start 🔧

```python
from transformers import AutoModelForImageTextToText, AutoProcessor
import torch

model_id = "YmaHealth/medgemma4b_yma_health_merged"

model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,   #  use float16 on GPUs without bfloat16
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_id)

messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are an endocrinologist specialised in GLP-1 therapy."}]
    },
    {
        "role": "user",
        "content": [{"type": "text", "text": "How should I titrate semaglutide if nausea persists?"}]
    }
]

inputs = processor(messages, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(processor.decode(outputs[0], skip_special_tokens=True))
