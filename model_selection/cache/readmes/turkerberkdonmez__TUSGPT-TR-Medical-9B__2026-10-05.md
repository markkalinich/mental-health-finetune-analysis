---
language:
  - tr
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: ytu-ce-cosmos/Turkish-Gemma-9b-T1
datasets:
  - turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1
tags:
  - medical
  - turkish
  - gemma2
  - dora
  - sft
  - mlx
  - apple-silicon
model-index:
  - name: TUSGPT-TR-Medical-9B
    results: []
---

<div align="center">

# ⚕️ TUSGPT-TR-Medical-9B

**Türkiye'nin İlk Açık Kaynak Türkçe Medikal Dil Modeli** *Turkey's First Open-Source Turkish Medical Language Model*

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Base Model](https://img.shields.io/badge/Base_Model-Gemma_2_9B-blue)](https://huggingface.co/ytu-ce-cosmos/Turkish-Gemma-9b-T1)
[![Language](https://img.shields.io/badge/Language-Turkish-red)](https://huggingface.co/languages/tr)
[![Framework](https://img.shields.io/badge/Training-MLX-purple)](https://github.com/ml-explore/mlx)

![tusgpt_readme_banner_horizontal](https://cdn-uploads.huggingface.co/production/uploads/644f952123d7eb05ca699d31/cAwybl8lXJsIiSYnkj5IG.png)

[🇹🇷 Türkçe Açıklama](#-model-hakkında) | [🇬🇧 English Description](#-model-description) | [💻 Kullanım/Usage](#-kullanım--usage)

</div>

---

## 🇹🇷 Model Hakkında

**TUSGPT-TR-Medical-9B**, Türkiye'nin medikal alandaki yapay zeka gelişimine katkı sağlamak amacıyla geliştirilmiş, **Gemma-2** mimarisine dayalı 9 milyar parametreli bir dil modelidir.

Model, **[ytu-ce-cosmos/Turkish-Gemma-9b-T1](https://huggingface.co/ytu-ce-cosmos/Turkish-Gemma-9b-T1)** temel modeli üzerine, **55.000'den fazla yüksek kaliteli Türkçe tıbbi soru-cevap çifti** ile **2 aşamalı DoRA (Weight-Decomposed Low-Rank Adaptation)** yöntemi kullanılarak fine-tune edilmiştir.

### 📚 Veri Seti Kapsamı (Dataset Coverage)

Model, aşağıdaki branşları ve daha fazlasını kapsayan **55,465 Türkçe soru-cevap** çifti ile eğitilmiştir:

* **Temel Bilimler:** Farmakoloji, Patoloji, Anatomi, Fizyoloji  
* **Klinik Bilimler:** Dahiliye, Cerrahi, Pediatri, Kadın Doğum  
* **Diğer:** Acil Tıp, Nöroloji, Onkoloji, Radyoloji  

---

## 🇬🇧 Model Description

**TUSGPT-TR-Medical-9B** is a specialized 9-billion parameter language model based on the **Gemma-2** architecture, designed to advance medical AI research in Turkey.

It is fine-tuned on the **[ytu-ce-cosmos/Turkish-Gemma-9b-T1](https://huggingface.co/ytu-ce-cosmos/Turkish-Gemma-9b-T1)** base model using **55,000+ high-quality Turkish medical Q&A pairs**, with a **2-Stage DoRA** methodology trained on Apple Silicon hardware.

### 📚 Dataset Scope

The model covers a wide range of medical disciplines with **55,465 Q&A pairs**, including:

* **Basic Sciences:** Pharmacology, Pathology, Anatomy, Physiology  
* **Clinical Sciences:** Internal Medicine, Surgery, Pediatrics, Obstetrics & Gynecology  
* **Others:** Emergency Medicine, Neurology, Oncology, Radiology  

---

## 📊 Teknik Detaylar / Technical Details

| Özellik / Feature | Detay / Detail |
|---|---|
| **Base Model** | [ytu-ce-cosmos/Turkish-Gemma-9b-T1](https://huggingface.co/ytu-ce-cosmos/Turkish-Gemma-9b-T1) |
| **Architecture** | Gemma 2 (9.24B Parameters) |
| **Dataset** | [turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1](https://huggingface.co/datasets/turkerberkdonmez/TUSGPT-TR-Medical-Dataset-v1) |
| **Dataset Size** | 55,465 samples (Q&A) |
| **Training Method** | 2-Stage DoRA (Weight-Decomposed LoRA) |
| **Precision** | bfloat16 |
| **Hardware** | Apple Mac Studio (M-Series, 128GB Unified Memory) |

<details>
<summary><strong>🔬 Eğitim Parametrelerini Görüntüle / View Training Hyperparameters</strong></summary>

### Stage 1 — Aggressive Knowledge Injection
* **DoRA:** rank=64, alpha=128, target_modules=all linear layers  
* **Optimizer:** NEFTune (alpha=3) enabled  
* **Learning Rate:** 2e-5 → 2e-6 (cosine decay)  
* **Steps:** 1600 iterations (~1 epoch)

### Stage 2 — Stabilization
* **Config:** Resumed from Stage 1 best checkpoint  
* **Optimizer:** NEFTune disabled  
* **Learning Rate:** 5e-6 → 1e-7  
* **Steps:** 1000 iterations  
* **Final Val Loss:** 1.126  
</details>

---

## 💻 Kullanım / Usage

### 🐍 Python (Transformers)

> **Generation önerisi:** Temperature=0.6, TopP=0.95, TopK=20, MinP=0 (generation_config.json varsayılanı).  
> **Greedy decoding kullanmayın**; performans düşüşüne ve sonsuz tekrarlara yol açabilir.  
> **Complex tasks:** `max_new_tokens` değerini artırın. Gerekirse `repetition_penalty` ve `presence_penalty` (0–2) ayarlanabilir.  
> Not: Daha yüksek değerler bazen dil karışmasına ve hafif performans düşüşüne neden olabilir.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "turkerberkdonmez/TUSGPT-TR-Medical-9B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "Sen tıp alanında uzmanlaşmış, Türkçe yanıt veren bir yapay zeka asistanısın. Soruları doğru, kapsamlı ve anlaşılır biçimde yanıtla."},
    {"role": "user", "content": "Akut miyokard enfarktüsünün erken belirtileri nelerdir?"},
]

prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=512,     # complex tasks için artırılabilir
    temperature=0.6,
    top_p=0.95,
    top_k=20,
    # min_p Transformers'ta her zaman desteklenmeyebilir; model config'ine bağlıdır.
    # Aşağıdakiler opsiyonel: tekrarları azaltmak için
    # repetition_penalty=1.15,
    # presence_penalty=0.3,
    do_sample=True,         # greedy decoding kapalı
)

print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

### 🦙 GGUF (Ollama & LM Studio)

Bu modelin sıkıştırılmış (quantized) versiyonları yerel cihazlarda çalıştırılabilir.

| Dosya Adı (Filename)               | Quant  | Boyut (Size) | Önerilen Donanım (Recommended HW) |
| ---------------------------------- | ------ | ------------ | --------------------------------- |
| `TUSGPT-TR-Medical-9B-Q8_0.gguf`   | Q8_0   | ~9.8 GB      | 12GB+ VRAM / 16GB+ RAM            |
| `TUSGPT-TR-Medical-9B-Q4_K_M.gguf` | Q4_K_M | ~5.8 GB      | 8GB+ VRAM / 12GB+ RAM             |

#### Ollama Setup

> **Önerilen üretim ayarları:** Temperature=0.6, TopP=0.95, TopK=20, MinP=0  
> **Greedy decoding kullanmayın**; performans düşüşü ve sonsuz tekrar riski yaratabilir.  
> **Complex tasks:** `num_predict` (max_new_tokens) artırılabilir.  
> Tekrarlar olursa `repeat_penalty` ve `presence_penalty` (0–2) ayarlanabilir (yüksek değerler bazen dil karışmasına ve hafif performans düşüşüne yol açabilir).

1. **Modelfile Oluşturun / Create Modelfile:**

```dockerfile
FROM ./TUSGPT-TR-Medical-9B-Q4_K_M.gguf

SYSTEM "Sen tıp alanında uzmanlaşmış, Türkçe yanıt veren bir yapay zeka asistanısın. Soruları doğru, kapsamlı ve anlaşılır biçimde yanıtla."

# Recommended generation (DO NOT use greedy decoding)
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER min_p 0

# Complex tasks: increase num_predict
# PARAMETER num_predict 1024

# To reduce endless repetitions (optional; tune gradually)
# PARAMETER repeat_penalty 1.15
# PARAMETER presence_penalty 0.3
```

2. **Modeli Çalıştırın / Run Model:**

```bash
ollama create tusgpt-medical -f Modelfile
ollama run tusgpt-medical
```

---

## ⚠️ Yasal Uyarı / Disclaimer

#### 🇹🇷 Türkçe

> **Bu model eğitim ve araştırma amaçlıdır.** Klinik karar verme süreçlerinde tek başına kullanılmamalıdır. Tıbbi kararlar için her zaman uzman hekime danışın.

#### 🇬🇧 English

> **This model is for educational and research purposes only.** It should not be used as a sole source for clinical decision-making. Always consult a qualified physician for medical decisions.

---

## 🤝 Acknowledgments

* **Base Model:** [YTU CE COSMOS Lab](https://huggingface.co/ytu-ce-cosmos) — Turkish-Gemma-9b-T1
* **Training Framework:** [MLX](https://github.com/ml-explore/mlx) by Apple

---

## 📝 Citation

```bibtex
@misc{tusgpt-tr-medical-9b,
  title        = {TUSGPT-TR-Medical-9B: Turkish Medical Language Model},
  author       = {Türker Berk Dönmez},
  year         = {2026},
  url          = {https://huggingface.co/turkerberkdonmez/TUSGPT-TR-Medical-9B}
}
```