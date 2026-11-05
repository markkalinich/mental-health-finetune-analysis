---
library_name: transformers
tags:
- medical
license: mit
datasets:
- MedInjection-FR/Native
- MedInjection-FR/Translated
language:
- fr
- en
base_model:
- Qwen/Qwen3-4B-Instruct-2507
---



# 🩺 QWEN-4B-SYN

**QWEN-4B-SYN** is a fine-tuned version of **Qwen-4B-Instruct** trained on the [MedInjection-FR](https://huggingface.co/MedInjection-FR) dataset, a French biomedical instruction corpus combining *native, synthetic, and translated* medical question–answer pairs.  
This model was fine-tuned using **Supervised Fine-Tuning (SFT)** with **DoRA adapters**, designed to study how the origin of supervision data influences model adaptation.

---

## 🧠 Model overview

| Property | Description |
|-----------|--------------|
| **Base model** | Qwen3-4B-Instruct-2507 |
| **Fine-tuning method** | DoRA (Weight-Decomposed Low-Rank Adaptation) |
| **Architecture size** | ~4B parameters |
| **Language** | French 🇫🇷 |
| **Domain** | Biomedical, Clinical, Health |
| **Intended use** | Research on instruction tuning and domain adaptation |
| **Caution** | Not for clinical or diagnostic use |

---

## ⚙️ Training setup

Fine-tuning was performed on **30k multiple-choice (MCQ and MCQU)** examples for each configuration, using:
- 10 epochs  
- Batch size: 12  
- Learning rate: 1e-4  
- Gradient accumulation: 8  
- Cosine scheduler with 5% warmup  
- LoRA rank: 16, α = 16, dropout = 0.05  
- Adapters applied to: `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`

All runs used identical hyperparameters to isolate the effect of **data provenance**.

---

## 📊 Evaluation summary

Evaluation was conducted on French biomedical benchmarks (MCQ, MCQU, OEQ).  
Metrics include **Exact Match (EM)** and **Hamming Score** for multiple-choice tasks, and **BLEU/ROUGE/BERTScore + LLM-as-a-judge** for open-ended QA.  

> See [MedInjection-FR GitHub](https://github.com/yourusername/MedInjection-FR) for full results and plots.



## 📚 Citation

If you use this model, please cite:

```bibtex
@misc{belmadani2026medinjectionfrexploringrolenative,
      title={MedInjection-FR: Exploring the Role of Native, Synthetic, and Translated Data in Biomedical Instruction Tuning}, 
      author={Ikram Belmadani and Oumaima El Khettari and Pacôme Constant dit Beaufils and Benoit Favre and Richard Dufour},
      year={2026},
      eprint={2603.06905},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2603.06905}, 
}
```
