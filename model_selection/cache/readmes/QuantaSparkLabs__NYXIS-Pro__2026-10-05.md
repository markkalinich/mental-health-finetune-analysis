---
license: apache-2.0
language:
- en
tags:
- rag
- retrieval-augmented-generation
- knowledge-base
- emotion-detection
- dual-stage-retrieval
- coding
- math
- science
- history
- nyxis
- quantasparklabs
pipeline_tag: text-generation
base_model:
- QuantaSparkLabs/NYXIS-1.1B
library_name: transformers
datasets:
- QuantaSparkLabs/NYXIS-AEGIS-Knowledge
---
<p align="center">
  <img src="https://huggingface.co/QuantaSparkLabs/NYXIS-Pro/resolve/main/preview imgagee.png"
       alt="NYXIS Logo"
       width="160"
       height="160"
       style="border-radius: 50%; object-fit: cover;">
</p>

<p align="center">
  <img src="https://huggingface.co/QuantaSparkLabs/NYXIS-Pro/resolve/main/logoname.png"
       alt="NYXIS Name"
       width="700"
       style="border-radius: 18px;">
</p>
# NYXIS-PRO 🛡️

<p align="center">
  <a href="https://huggingface.co/QuantaSparkLabs/NYXIS-1.1B"><img src="https://img.shields.io/badge/Base-NYXIS--1.1B-purple" alt="Base Model"></a>
  <a href="https://huggingface.co/QuantaSparkLabs/NYXIS-AEGIS-KB"><img src="https://img.shields.io/badge/Knowledge-AEGIS-blue" alt="AEGIS KB"></a>
  <a href="#"><img src="https://img.shields.io/badge/Retrieval-Dual%20Stage-green" alt="Dual Stage"></a>
  <a href="#"><img src="https://img.shields.io/badge/Emotion-1--10%20Scale-orange" alt="Emotion Engine"></a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-yellow" alt="License"></a>
</p>

**The all-in-one reasoning engine with the AEGIS knowledge shield.**

NYXIS-PRO combines the NYXIS1.1B base model with a curated 5,000+ chunk knowledge base covering coding, math, science, history, and common knowledge. A dual‑stage retriever grounds every factual answer in verified data — **zero hallucination.**

## 🧠 What Makes It Different

| Feature | Description |
|---------|-------------|
| **AEGIS Knowledge Base** | 5,426 curated Wikipedia, Trivia QA, and ArXiv chunks |
| **Dual‑Stage Retriever** | Dense recall (bge‑small) + Cross‑encoder rerank (ms‑marco‑MiniLM) |
| **Emotion Engine** | Detects user emotion on a 1‑10 scale and matches tone |
| **4‑Tier Knowledge Cascade** | AEGIS → External Search → Model Brain → Honest Fallback |
| **Zero Hallucination** | If it doesn't know, it says so — no fabrication |

## 🚀 Quick Start

```python
from huggingface_hub import snapshot_download
import sys

model_dir = snapshot_download("QuantaSparkLabs/NYXIS-Pro")
sys.path.insert(0, model_dir)

from pipeline import NYXISPro
nyxis = NYXISPro(model_dir)

result = nyxis.generate("What is a binary search tree?")
print(result["response"])
```

> **Requirements:** `sentence-transformers`, `faiss-cpu`, `transformers`, `accelerate`, `bitsandbytes`  
> **VRAM:** ~2.1 GB (4‑bit) | **Hardware:** T4 or better

## 📦 What's Inside

| Component | Model | Purpose |
|-----------|-------|---------|
| **Base LLM** | NYXIS1.1B) | Text generation |
| **Dense Retriever** | bge‑small‑en‑v1.5 | Initial candidate recall |
| **Cross‑Encoder** | ms‑marco‑MiniLM‑L‑6‑v2 | Precision re‑ranking |
| **FAISS Index** | 5,426 chunks | Knowledge storage |
| **Emotion Engine** | Custom keyword‑based | Tone matching |

## 🤖 Emotion Intelligence

NYXIS-PRO detects your emotional state from text and adjusts its personality:

| Level | Emotion | Response Style |
|:---:|---------|----------------|
| 1‑3 | Sad / Angry | Gentle, supportive, empathetic |
| 4‑6 | Neutral | Balanced, warm, helpful |
| 7‑9 | Happy / Excited | Energetic, playful |
| 10 | Overjoyed | Celebratory |

## 🛡️ Knowledge Cascade

When you ask a factual question, NYXIS-PRO follows a strict 4‑tier protocol:

1. **AEGIS** — Searches internal verified knowledge base
2. **External Search** — Falls back to web search (user‑provided API)
3. **Model Brain** — Uses training data with honesty guard
4. **Honest Fallback** — Admits "I don't have enough information"

It **never fabricates** an answer.

## Limitations

- Knowledge base covers ~5,400 chunks — not infinite
- Emotion detection is keyword‑based, not deep sentiment analysis
- External search requires user‑provided API function
- English‑only, 1.5B model size limits complex reasoning

## License

Apache‑2.0

---

*Built with 🛡️ by QuantaSparkLabs*