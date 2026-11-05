---
base_model:
- unsloth/medgemma-4b-it
model_name: brats_medgemma_light
tags:
- sft
- medical-imaging
- brain-tumor
- brats
- textbrats
- unsloth
license: apache-2.0
datasets:
- Jupitern52/TextBraTS
language:
- en
pipeline_tag: visual-question-answering
library_name: transformers
---

# 🧠 brats_medgemma_light

**`brats_medgemma_light`** is the merged model derived from the fine-tuning experiments in  
[`Jesteban247/medgemma-brats-experiments`](https://huggingface.co/Jesteban247/medgemma-brats-experiments).  

It is based on **[unsloth/medgemma-4b-it](https://huggingface.co/unsloth/medgemma-4b-it)** and represents the **r1_alpha2_epochs1** configuration —  
the lightweight variant fine-tuned on the **BraTS** and **TextBraTS** datasets for **brain MRI interpretation and radiology text generation**.

---

## ⚙️ Configuration Details

| Parameter | Value |
|------------|--------|
| **LoRA rank (r)** | 1 |
| **LoRA alpha (α)** | 2 |
| **Epochs** | 1 |
| **Trainable parameters** | ~2.4M (≈0.06%) |
| **Total model size** | 4B parameters |
| **Fine-tuning type** | Full merge after LoRA training |

---

## 📊 Quantitative Summary

| Metric | ROUGE-1 | ROUGE-2 | ROUGE-L | Avg ROUGE |
|--------|----------|----------|----------|------------|
| **r1_alpha2_epochs1** | 0.5539 | 0.2765 | 0.3985 | **0.4096** |

This configuration serves as a minimal fine-tuning baseline in the experiment set,  
balancing broad generalization with initial domain adaptation to medical language.

---

## 🧠 Qualitative Example

🖼️ *Image:*  
![Brain MRI Example](https://huggingface.co/Jesteban247/medgemma-brats-experiments/resolve/main/images/Brain-Single-Slice_FT.png)

**Ground truth:**

> “The lesion area is in the right frontal and parietal lobes with a mixed pattern of high and low signals with speckled high signal regions. Edema is mainly observed in the right parietal lobe, partially extending to the frontal lobe, presenting as high signal, indicating significant tissue swelling around the lesion. Necrosis is within the lesions of the right parietal and frontal lobes, appearing as mixed, with alternating high and low signal regions. Ventricular compression is seen in the lateral ventricles with significant compressive effects on the brain tissue and ventricles.”

**Model Output (r1_alpha2_epochs1):**

> “The MRI slice demonstrates: The lesion area is in the right cerebral hemisphere, mainly concentrated in the right frontal and parietal lobes with mixed signals... Edema is observed... Ventricular compression is observed with the right lateral ventricle being compressed.”

This output captures core clinical elements with concise phrasing but shows limited depth in signal pattern description and necrosis details compared to heavier LoRA configurations.

---

## 💬 Notes

This merged version reflects **minimal domain adaptation** due to fine-tuning on **BraTS** and **TextBraTS** with low-rank LoRA,  
resulting in **better generalization** to non-medical tasks at the cost of shallower specialization in radiology-specific terminology.  

Such trade-offs are typical in lightweight fine-tuning on **small, domain-specific datasets**,  
and align with observations discussed in the parent project  
➡️ [`Jesteban247/medgemma-brats-experiments`](https://huggingface.co/Jesteban247/medgemma-brats-experiments)