---
base_model: Qwen/Qwen2.5-1.5B-Instruct
language: id
tags:
- medical
- indonesian
- qlora
- fine-tuned
license: apache-2.0
---

# Indonesian Medical Chatbot - Fine-tuned Qwen2.5-1.5B

Model Qwen2.5-1.5B-Instruct yang di-fine-tune untuk menjawab pertanyaan kesehatan umum
dalam Bahasa Indonesia. Output selalu berformat JSON terstruktur dengan field `jawaban`
dan `disclaimer`.

## Intended Use
- Edukasi kesehatan umum dalam Bahasa Indonesia
- Bukan untuk diagnosis medis atau penggunaan klinis

## Training
- Method: QLoRA (r=16, α=32, dropout=0.05, 3 epoch)
- Framework: Unsloth + TRL
- Dataset: [qrizan/indonesian-medical-qa](https://huggingface.co/datasets/qrizan/indonesian-medical-qa) — 500 contoh sintetis (train/val/test = 400/50/50)
- Compute: Google Colab Free (Tesla T4)
- W&B Experiment: https://wandb.ai/myproject-org/indonesian-medical-chatbot/runs/ptfqrgmg

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch, json

model_id = "qrizan/indonesian-medical-qwen2.5-1.5b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")
model.eval()

system = (
    "Kamu adalah asisten kesehatan berbahasa Indonesia. "
    "Jawab pertanyaan medis umum dengan bahasa sederhana. "
    "Selalu sertakan disclaimer untuk konsultasi ke dokter."
)
question = "Apa gejala umum diabetes tipe 2?"

prompt = (
    f"<|im_start|>system
{system}<|im_end|>
"
    f"<|im_start|>user
{question}<|im_end|>
"
    f"<|im_start|>assistant
"
)

inp = tokenizer(prompt, return_tensors="pt").to(model.device)
input_len = inp["input_ids"].shape[1]
with torch.no_grad():
    out = model.generate(**inp, max_new_tokens=220, do_sample=False, pad_token_id=tokenizer.pad_token_id)
result = tokenizer.decode(out[0][input_len:], skip_special_tokens=True).strip()
print(json.loads(result))
# Output: {"jawaban": "...", "disclaimer": "..."}
```

## Evaluation (test set sintetis, 50 contoh)

```json
{
  "baseline_format_metrics": {
    "total": 50,
    "json_valid_pct": 0.0,
    "has_jawaban_pct": 0.0,
    "has_disclaimer_pct": 0.0,
    "disclaimer_has_dokter_pct": 0.0,
    "overall_format_compliance_pct": 0.0
  },
  "finetuned_format_metrics": {
    "total": 50,
    "json_valid_pct": 96.0,
    "has_jawaban_pct": 96.0,
    "has_disclaimer_pct": 96.0,
    "disclaimer_has_dokter_pct": 96.0,
    "overall_format_compliance_pct": 96.0
  },
  "gpt4o_mini_format_metrics": {
    "total": 50,
    "json_valid_pct": 100.0,
    "has_jawaban_pct": 98.0,
    "has_disclaimer_pct": 100.0,
    "disclaimer_has_dokter_pct": 100.0,
    "overall_format_compliance_pct": 98.0
  },
  "perplexity": {
    "baseline": 3.031702656866234,
    "fine_tuned": 2.00000459098804
  },
  "llm_judge_avg_scores": {
    "baseline": {
      "akurasi_informasi": 3.1,
      "kejelasan_bahasa": 3.7,
      "kelengkapan_disclaimer": 1.5,
      "konsistensi_format": 2.25
    },
    "fine_tuned": {
      "akurasi_informasi": 4.25,
      "kejelasan_bahasa": 4.65,
      "kelengkapan_disclaimer": 4.8,
      "konsistensi_format": 3.95
    },
    "gpt4o_mini": {
      "akurasi_informasi": 4.65,
      "kejelasan_bahasa": 4.8,
      "kelengkapan_disclaimer": 4.8,
      "konsistensi_format": 4.25
    }
  }
}
```

## Limitations
- Fine-tuning mengubah format output (JSON + disclaimer), bukan akurasi medis klinis.
- 4% test case gagal output JSON valid — kemungkinan pada input panjang di luar distribusi training.
- Test set synthetic dari distribusi yang sama dengan training; performa pada pertanyaan real user belum divalidasi.
- Disclaimer cenderung formulaic — variasi ekspresi terbatas.
- Bukan untuk penggunaan klinis atau diagnosis medis.

## Github
**Repo:** https://github.com/qrizan/indonesian-medical-chatbot