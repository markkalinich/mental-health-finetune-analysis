---
license: mit
base_model: meta-llama/Llama-2-7b-chat-hf   # ← change to your actual base model
tags:
- llama-factory
- lora
- text-classification
- sentiment-analysis
- stance-detection
- code-mixed
- tibetan
- chinese
- low-resource
- nlp
language:
- bo
- zh
pipeline_tag: text-classification
author: Wudao Yang (Yunnan Minzu University)
email: wudaoyang@ymu.edu.cn
---

# TiChi-OpMiner: LLaMA LoRA for Tibetan–Chinese Code-Mixed Opinion Mining

**TiChi-OpMiner** is a LoRA-fine-tuned LLaMA model for **joint sentiment and stance prediction** on
**Tibetan–Chinese code-mixed texts**.  
Given a short code-mixed sentence, the model outputs:

- **Sentiment:** `positive`, `neutral`, or `negative`  
- **Stance:** `support`, `neutral`, or `oppose`

The model was fine-tuned using [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory) with
parameter-efficient training (LoRA).

---

## 1. Model Details

- **Model name:** `your-username/tichi-opminer`  <!-- change to your repo id -->
- **Base model:** `meta-llama/Llama-2-7b-chat-hf` (decoder-only LLM)
- **Fine-tuning method:** LoRA (Low-Rank Adaptation)
- **Frameworks:** PyTorch, Transformers, LLaMA Factory
- **Task type:** joint opinion mining (sentiment + stance)
- **Input languages:** Tibetan (bo, Tibetan script) and Chinese (zh, simplified Chinese),
  with occasional English tokens / hashtags
- **Output:** natural language or JSON-style labels describing sentiment and stance

---

## 2. Intended Use

### Intended use

- Research on **code-mixed NLP** for low-resource languages  
- Experiments on **Tibetan–Chinese opinion mining** (social media posts, comments,
  short messages)  
- As a starting point for further fine-tuning on related tasks (e.g., Tibetan-only
  or Chinese-only sentiment / stance classification)

### Not intended / out of scope

- High-stakes decision making (e.g., legal, medical, financial, political decisions)
- Use on very long or domain-mismatched documents (e.g., technical reports, legal
  contracts)
- Any deployment scenario where incorrect predictions could cause serious harm
  without additional human review

---

## 3. Training Data

The model is trained on a **100K-instance Tibetan–Chinese code-mixed corpus**:

- Each instance is a **short sentence** that mixes Tibetan and Chinese.
- Every sentence is annotated with:
  - **Sentiment:** `positive`, `neutral`, `negative`
  - **Stance:** `support`, `neutral`, `oppose`
- The corpus was created with a **template-based generation pipeline** plus **manual
  checking** to ensure:
  - Natural code-mixing patterns
  - Fluent Chinese glosses
  - Consistent joint labels
- The label space is designed so that:
  - `positive ↔ support`, `negative ↔ oppose`, `neutral ↔ neutral`.

> If you also publish the dataset on Hugging Face, add a link here, e.g.  
> **Dataset:** [`your-username/tichi-opminer-dataset`](https://huggingface.co/datasets/your-username/tichi-opminer-dataset)

---

## 4. Training Procedure

- **Fine-tuning framework:** LLaMA Factory
- **Method:** LoRA adapters on top of the base LLaMA model
- **Objective:** instruction-style text generation; the model receives a prompt
  containing the code-mixed text and returns both sentiment and stance.

Example (conceptual) training prompt:

```text
You are an assistant that predicts sentiment and stance for Tibetan–Chinese code-mixed text.

Text: ང་ཚོ今天ཡིན་ནསདགའ་བསུ་བྱེད་ཡོད།
Please answer in JSON format:
{"sentiment": ..., "stance": ...}
