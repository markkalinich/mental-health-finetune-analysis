---
license: apache-2.0
base_model: openbmb/MiniCPM5-2B
tags:
  - mini-jev
  - shell-safety
  - lora
  - merged
pipeline_tag: text-classification
---

# Mini-Jev — shell-safety Phase-1b (merged)

Full merged weights: [`openbmb/MiniCPM5-2B`](https://huggingface.co/openbmb/MiniCPM5-2B) + shell-safety LoRA Phase-1b (allow / warn / block).

Browser ONNX (Transformers.js q4): [`nicolasembleton/mini-jev-minicpm5-2b-shell-safety-phase1b-onnx`](https://huggingface.co/nicolasembleton/mini-jev-minicpm5-2b-shell-safety-phase1b-onnx).

Demo: [mini-jev.pastel-labs.com](https://mini-jev.pastel-labs.com).

## Training data (summary)

Train mix is remapped [`kontext-security/ShellRisk-Bench`](https://huggingface.co/datasets/kontext-security/ShellRisk-Bench) plus hand rows and a small Phase-1b boundary set; eval is a frozen 105-item smoke panel with planted gold. See the ONNX card for counts and smoke metrics.

## Intended use

Research and demos. Not a production security boundary by itself.
