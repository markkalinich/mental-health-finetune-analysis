---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: text-generation
tags:
  - 1.5b
  - domain-specialist
  - fableforge
  - medical
  - nexus
  - no-refusals
  - text-generation
  - uncensored
---

# NEXUS-Medical

> **NEXUS domain specialist for medical Q&A and clinical reasoning — lightweight & uncensored.**

[![Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2Ffableforge-ai%2FNEXUS-Medical&query=downloads&label=downloads&color=blue)](https://huggingface.co/fableforge-ai/NEXUS-Medical) [![Demos](https://img.shields.io/badge/🤗-Live%20Demos-orange)](https://huggingface.co/spaces/fableforge-ai/fableforge-nexus)

Base model: [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)  ·  Part of the **FableForge** ecosystem.

## 🏆 Benchmarks — 140/150 (93%)

A 1.5B model scoring **93%** — punching far above its weight. 30-prompt evaluation (domain knowledge, uncensored domain + general, reasoning, tool use), 0–5 scoring, run on an NVIDIA A40 via Ollama.

| Category | Score | Avg |
| --- | --- | --- |
| 🎯 Domain Knowledge | 47/50 | 4.7/5 |
| 🔓 Uncensored (Domain) | 22/25 | 4.4/5 |
| 🔓 Uncensored (General) | 24/25 | 4.8/5 |
| 🧠 Reasoning | 25/25 | 5.0/5 |
| 🔧 Tool Use | 22/25 | 4.4/5 |
| **Total** | **140/150** | **93%** |

## 🧬 The NEXUS Family — six specialists, one tiny footprint

| Model | Score | Specialty |
| --- | --- | --- |
| [NEXUS-Coder](https://huggingface.co/King3Djbl/nexus-coder-GGUF) | 141/150 | Software Engineering & Code |
| [NEXUS-Security](https://huggingface.co/King3Djbl/nexus-security-GGUF) | 144/150 | Cybersecurity & Hacking |
| **NEXUS-Medical** | **140/150** | **Medicine & Healthcare** |
| [NEXUS-Legal](https://huggingface.co/King3Djbl/nexus-legal-GGUF) | 139/150 | Law & Compliance |
| [NEXUS-Finance](https://huggingface.co/King3Djbl/nexus-finance-GGUF) | 144/150 | Finance & Accounting |
| [NEXUS-Science](https://huggingface.co/King3Djbl/nexus-science-GGUF) | 140/150 | Science & Research |

👉 Grab the whole family on [Ollama](https://ollama.com/fableforge-ai) or [Hugging Face](https://huggingface.co/King3Djbl).


---

## ⚡ Run it now — Ollama

```bash
ollama run fableforge-ai/nexus-medical:q4_k_m   # published on ollama.com
ollama run hf.co/King3Djbl/nexus-medical-GGUF:Q4_K_M
```

📦 **GGUF quants:** [King3Djbl/nexus-medical-GGUF](https://huggingface.co/King3Djbl/nexus-medical-GGUF)

## 🧠 Prompt format (ChatML)

```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
```

## 🌌 See it live — the FableForge demos

This family powers a galaxy of free, interactive HF Spaces:

- 🧭 [FableForge Nexus](https://huggingface.co/spaces/fableforge-ai/fableforge-nexus)
- 🍺 [Infinite NPC](https://huggingface.co/spaces/fableforge-ai/infinite-npc)
- 🎭 [Dual-GM](https://huggingface.co/spaces/King3Djbl/dual-gm-simulator)
- 💻 [ShellWhisperer](https://huggingface.co/spaces/King3Djbl/shellwhisperer-terminal)
- 👻 [Ghost Writer](https://huggingface.co/spaces/fableforge-ai/ghost-writer)


---

## 🔗 Related models

- 📊 GGUF quants: [`nexus-medical-GGUF`](https://huggingface.co/King3Djbl/nexus-medical-GGUF)

---

*⭐ Like & share — it helps people find the source instead of a mirror.*