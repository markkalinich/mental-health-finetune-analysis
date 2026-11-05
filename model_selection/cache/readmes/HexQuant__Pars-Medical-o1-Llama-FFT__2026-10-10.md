---
language:
  - en
  - fa
license: apache-2.0
tags:
  - medical
  - biology
  - persian
  - farsi
  - llama-3
  - chain-of-thought
  - fft
  - full-fine-tune
  - healthcare
  - clinical-reasoning
  - bilingual
  - o1-style
  - unsloth
base_model: unsloth/Llama-3.2-3B-Instruct
datasets:
  - FreedomIntelligence/medical-o1-reasoning-SFT
  - erfan226/persian-medical-qa
  - SeyedAli/Persian-Medical-Dataset
pipeline_tag: text-generation
library_name: transformers
---

<div align="center">

# 🩺 Pars-Medical-o1-Llama-FFT
# ⚠️This is a beta version and does not have the ability to correctly respond to or handle local runs on its own.⚠️
## ⚠️The full version will be released in the Pars-Medical application.⚠️

### اولین مدل پزشکی دوزبانه فارسی-انگلیسی با استدلال زنجیره‌ای
### First Bilingual Persian-English Medical Model with Chain-of-Thought Reasoning



![image](https://cdn-uploads.huggingface.co/production/uploads/66c1fd184511077b9f3cd432/oRhAY1wiGJe_F3FXAszaF.png)

[![Model](https://img.shields.io/badge/🤗_Model-Pars--Medical--o1-blue?style=for-the-badge)](https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT)
[![GGUF](https://img.shields.io/badge/📦_GGUF-Quantized-green?style=for-the-badge)](https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF)
[![License](https://img.shields.io/badge/📜_License-Apache_2.0-orange?style=for-the-badge)](LICENSE)

[![Twitter](https://img.shields.io/badge/Twitter-@TheRealPourya-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/TheRealPourya)
[![GitHub](https://img.shields.io/badge/GitHub-xPOURY4-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/xPOURY4)
[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-HexQuant-FFD21E?style=for-the-badge)](https://huggingface.co/HexQuant)

</div>

---

## 🌟 Overview | معرفی

<table>
<tr>
<td width="50%" align="right" dir="rtl">

**پارس-مدیکال** یک مدل هوش مصنوعی پزشکی است که با روش **Full Fine-Tune** روی مجموعه داده‌های پزشکی فارسی و انگلیسی آموزش دیده است.

این مدل از تکنیک **Chain-of-Thought** (استدلال زنجیره‌ای) مشابه مدل‌های o1 استفاده می‌کند تا پاسخ‌های دقیق‌تر و منطقی‌تر ارائه دهد.

</td>
<td width="50%">

**Pars-Medical** is a medical AI model trained with **Full Fine-Tuning** on Persian and English medical datasets.

It uses **Chain-of-Thought** reasoning (similar to o1-style models) to provide more accurate and logical responses.

</td>
</tr>
</table>

---

## ✨ Features | ویژگی‌ها

| Feature | Description | توضیحات |
|:-------:|:------------|--------:|
| 🌐 | **Bilingual** - Persian & English | **دوزبانه** - فارسی و انگلیسی |
| 🧠 | **Chain-of-Thought** - Step-by-step reasoning | **استدلال زنجیره‌ای** - گام به گام |
| 🔬 | **Full Fine-Tune** - Not LoRA/adapter | **آموزش کامل** - نه آداپتور |
| 📊 | **48K+ Samples** - Large medical dataset | **+۴۸ هزار نمونه** - دیتاست بزرگ |
| ⚡ | **3B Parameters** - Fast inference | **۳ میلیارد پارامتر** - استنتاج سریع |
| 🏥 | **Clinical Focus** - Diagnosis & treatment | **تمرکز بالینی** - تشخیص و درمان |

---

## 🚀 Quick Start | شروع سریع

### Using Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "HexQuant/Pars-Medical-o1-Llama-FFT"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

messages = [
    {"role": "user", "content": "علائم دیابت نوع ۲ چیست؟"}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
outputs = model.generate(inputs, max_new_tokens=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Using Ollama (GGUF)

```bash
# Use quantized version for local inference
ollama run hf.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF
```

> 📦 **Looking for GGUF?** See [Pars-Medical-o1-Llama-FFT-GGUF](https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF) for quantized versions.

---

## 💬 Example | نمونه

<details>
<summary><b>🇮🇷 مثال فارسی - تشخیص پزشکی</b></summary>

**User:**
> یک مرد ۵۵ ساله با درد قفسه سینه، تنگی نفس و تعریق مراجعه کرده است. علائم از ۲ ساعت پیش شروع شده. تشخیص احتمالی چیست؟

**Model:**
> `<think>`
> بیایید این مورد را گام به گام بررسی کنیم:
>
> ۱. **مشخصات بیمار**: مرد ۵۵ ساله - در گروه سنی پرخطر برای بیماری‌های قلبی
>
> ۲. **علائم کلیدی**:
>    - درد قفسه سینه (علامت کلاسیک)
>    - تنگی نفس (نشانه اختلال عملکرد قلب)
>    - تعریق (فعال شدن سیستم سمپاتیک)
>
> ۳. **شروع حاد**: ۲ ساعت پیش - نشان‌دهنده وضعیت اورژانسی
>
> ۴. **تشخیص افتراقی**:
>    - سندرم حاد کرونری (ACS) ⚠️ محتمل‌ترین
>    - آمبولی ریه
>    - دیسکسیون آئورت
> `</think>`
>
> **تشخیص احتمالی: سندرم حاد کرونری (Acute Coronary Syndrome)**
>
> اقدامات فوری توصیه شده:
> 1. ECG فوری (در ۱۰ دقیقه اول)
> 2. تروپونین و آنزیم‌های قلبی
> 3. آسپرین ۳۲۵ میلی‌گرم
> 4. مشاوره قلب اورژانسی

</details>

<details>
<summary><b>🇺🇸 English Example - Clinical Reasoning</b></summary>

**User:**
> A 45-year-old woman presents with fatigue, weight gain, cold intolerance, and constipation for 3 months. What is the likely diagnosis?

**Model:**
> `<think>`
> Let me analyze this systematically:
>
> 1. **Patient Profile**: 45-year-old female - higher risk for thyroid disorders
>
> 2. **Symptom Analysis**:
>    - Fatigue → decreased metabolic rate
>    - Weight gain → slowed metabolism
>    - Cold intolerance → reduced thermogenesis
>    - Constipation → decreased GI motility
>
> 3. **Pattern Recognition**: All symptoms point to hypometabolic state
>
> 4. **Most Likely Cause**: These are classic signs of decreased thyroid hormone
> `</think>`
>
> **Likely Diagnosis: Hypothyroidism**
>
> Recommended workup:
> 1. TSH (primary screening test)
> 2. Free T4
> 3. Anti-TPO antibodies (if Hashimoto's suspected)
> 4. Lipid panel (dyslipidemia common in hypothyroidism)

</details>

---

## 📊 Training Details | جزئیات آموزش

| Parameter | Value |
|:----------|:------|
| **Base Model** | `Llama-3.2-3B-Instruct` |
| **Method** | Full Fine-Tune (FFT) |
| **Framework** | Unsloth + Transformers |
| **Precision** | BF16 |
| **Context Length** | 4096 tokens |
| **Training Hardware** | NVIDIA A100 80GB |

### Datasets | دیتاست‌ها

| Dataset | Language | Samples |
|:--------|:---------|--------:|
| [medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) | English | ~40,000 |
| [persian-medical-qa](https://huggingface.co/datasets/erfan226/persian-medical-qa) | Persian | ~5,000 |
| [Persian-Medical-Dataset](https://huggingface.co/datasets/SeyedAli/Persian-Medical-Dataset) | Persian | ~3,000 |

---

## 📦 Available Formats | فرمت‌های موجود

| Format | Size | Use Case | Link |
|:-------|:-----|:---------|:-----|
| **BF16** (This repo) | ~6.4 GB | Fine-tuning, Full precision | [Download](https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT) |
| **GGUF Q4_K_M** | ~2.0 GB | Ollama, llama.cpp, LM Studio | [Download](https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF) |
| **GGUF Q5_K_M** | ~2.5 GB | Better quality, local use | [Download](https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF) |
| **GGUF Q8_0** | ~3.5 GB | Best quality quantized | [Download](https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT-GGUF) |

---

## ⚠️ Disclaimer | سلب مسئولیت

<table>
<tr>
<td width="50%" align="right" dir="rtl">

⚠️ این مدل صرفاً برای **اهداف آموزشی و تحقیقاتی** طراحی شده است.

❌ **جایگزین مشاوره پزشکی حرفه‌ای نیست.**

✅ همیشه با پزشک متخصص مشورت کنید.

</td>
<td width="50%">

⚠️ This model is for **educational and research purposes only**.

❌ **Not a substitute for professional medical advice.**

✅ Always consult with a qualified healthcare provider.

</td>
</tr>
</table>

---

## 🔗 Connect | ارتباط

<div align="center">

[![Twitter](https://img.shields.io/badge/Twitter-@TheRealPourya-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/TheRealPourya)
[![GitHub](https://img.shields.io/badge/GitHub-xPOURY4-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/xPOURY4)
[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-HexQuant-FFD21E?style=for-the-badge)](https://huggingface.co/HexQuant)

---

**Made with ❤️ TheRealPourya**

*If you find this model useful, please ⭐ star the repo and share it!*

</div>