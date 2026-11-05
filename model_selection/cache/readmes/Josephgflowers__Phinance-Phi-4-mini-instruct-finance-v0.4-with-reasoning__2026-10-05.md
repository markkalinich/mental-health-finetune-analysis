---
license: mit
tags:
- finance
- fine-tuning
- conversational-ai
- named-entity-recognition
- sentiment-analysis
- topic-classification
- rag
- multilingual
- lightweight-llm
- phi-architecture
datasets:
- Josephgflowers/Finance-Instruct-500k
- GAIR/LIMO
- TheFinAI/Fino1_Reasoning_Path_FinQA
- Jarrodbarnes/cortex-1-market-analysis
- Josephgflowers/Finance_Curriculum_Edu_English
- Josephgflowers/Finance-Curriculum-Edu-Arabic
- Josephgflowers/Finance-Curriculum-Edu-Uzbek
- Josephgflowers/Finance-Curriculum-Edu-Multilingual
base_model:
- microsoft/Phi-4-mini-instruct
- microsoft/Phi-4-mini-reasoning
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6328952f798f8d122ce62a44/lcG3xN0mcRPwM248I30CQ.png)

# Phinance-Phi-4-mini-instruct-finance-v0.4-with-reasoning

## Overview

**Phinance-Phi-4-mini-instruct-finance-v0.4-with-reasoning** is a compact, fine-tuned model built on top of [microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) with a strong emphasis on structured financial reasoning and instruction-following. This release blends financial QA, reasoning chains, and RAG-ready formatting into a lightweight agent optimized for advanced finance applications.

This model is particularly good at producing structured outputs like JSON, following instruction patterns, and chaining logical steps when prompted with tags like `<thinking>` or `<think>`.
This model also outperforms the base models on multi language capabilities. 

---

## 🔄 **Latest Training Run: Finance Curriculum Reasoning Expansion**

After v0.4, the model was further fine-tuned on newly released multilingual finance reasoning datasets, explicitly targeting real-world coverage gaps in non-English finance QA:

- [Finance Curriculum Edu English](https://huggingface.co/datasets/Josephgflowers/Finance_Curriculum_Edu_English)
- [Finance-Curriculum-Edu-Arabic](https://huggingface.co/datasets/Josephgflowers/Finance-Curriculum-Edu-Arabic)
- [Finance-Curriculum-Edu-Uzbek](https://huggingface.co/datasets/Josephgflowers/Finance-Curriculum-Edu-Uzbek)
- [Finance-Curriculum-Edu-Multilingual](https://huggingface.co/datasets/Josephgflowers/Finance-Curriculum-Edu-Multilingual)

**This training phase addressed:**  
- Conceptual reasoning and QA coherence across 60+ languages  
- Robustness to diverse phrasing, financial domains, and real-world curriculum topics  
- Further reduction of hallucinations and improved answer structure, especially for small and mid-sized LMs in non-English settings

---

## Model Workflow & Training Strategy

### 1. **Initial Fine-Tune**  
   * Base: `Phi-4-mini-instruct`  
   * Dataset: [Finance-Instruct-500k](https://huggingface.co/datasets/Josephgflowers/Finance-Instruct-500k)  
   * Additional datasets: [LIMO](https://huggingface.co/datasets/GAIR/LIMO), [Fin01](https://huggingface.co/datasets/TheFinAI/Fino1_Reasoning_Path_FinQA)

### 2. **Back Merge**  
   * Model was merged back with `Phi-4-mini-instruct` to retain broad instruction capability.

### 3. **Reasoning Augmentation**  
   * Generated question-answer sets from `Finance-Instruct-500k` using reasoning system prompts  
   * Filtered for format quality and signal-to-noise ratio  
   * Trained again on: generated reasoning dataset, LIMO, Fin01

### 4. **Final Merge**  
   * Merged with `Phi-4-mini-reasoning` to strengthen chain-of-thought behavior

### 5. **Reason Pass**  
   * Trained on:  
     - Filtered reasoning subset of self-generated 500k QA set  
     - [Cortex-1 Market Analysis](https://huggingface.co/datasets/Jarrodbarnes/cortex-1-market-analysis)  
     - LIMO  
     - Fin01

### 6. **Finance Curriculum Reasoning Expansion (NEW)**  
   * Trained with four new datasets targeting real-world and multilingual finance curriculum QA:
   * Generated question-answer sets from `Finance-Instruct-500k` using reasoning system prompts  
   * Filtered for format quality and signal-to-noise ratio
   * Self generated reasoning dataset using finance topics. Human preference optimized.
   * Trained again on: generated reasoning dataset, LIMO, Fin01
     - [Finance Curriculum Edu English](https://huggingface.co/datasets/Josephgflowers/Finance_Curriculum_Edu_English)
     - [Finance-Curriculum-Edu-Arabic](https://huggingface.co/datasets/Josephgflowers/Finance-Curriculum-Edu-Arabic)
     - [Finance-Curriculum-Edu-Uzbek](https://huggingface.co/datasets/Josephgflowers/Finance-Curriculum-Edu-Uzbek)
     - [Finance-Curriculum-Edu-Multilingual](https://huggingface.co/datasets/Josephgflowers/Finance-Curriculum-Edu-Multilingual)

---

## Key Capabilities

* **Financial Reasoning**: Great at multi-step reasoning across investment strategies, reports, and economic topics
* **Instruction Following**: Precise response formatting with few-shot or system messages
* **Multi-Turn Dialogues**: Maintains context across long conversations
* **Structured Output**: NER, parsing, and tagging tasks return valid JSON by default
* **RAG-Compatible**: Handles prepended external context in the user field
* **Tag-Aware**: Supports `<thinking>` tags to guide reasoning chains
* **Multilingual Finance QA**: Expanded coverage in 60+ languages for curriculum-based financial topics

---

## Usage Tips

* Use system messages like:

```

You are a financial assistant that explains your reasoning step by step. Use <thinking>...</thinking> to wrap your reasoning.

````

* Expect JSON-style outputs for tasks like:

* Entity extraction
* Address parsing
* XBRL tagging

---

## Example

```json
{
"system": "You are a financial reasoning assistant. Use <thinking> to show your steps.",
"user": "<context>ABC Inc reported a quarterly revenue increase of 12% while cutting debt by 8%</context>\nWhat does this indicate about the company’s short-term stability?",
"assistant": "<thinking>This revenue increase suggests improved sales or pricing power. Debt reduction enhances cash flow and reduces risk. Together, they signal improved short-term financial health.</thinking> It indicates strong short-term stability."
}
````

---

## Model Details

* **Base**: Phi-4-mini-instruct
* **Architecture**: \~3.8B params (mini)
* **Version**: v0.4 + Multilingual Curriculum Reasoning Expansion
* **License**: MIT
* **Framework**: Hugging Face Transformers

---

## Citation

```bibtex
@model{josephgflowers2025phinancephi4,
  title={Phinance-Phi-4-mini-instruct-finance-v0.4-with-reasoning},
  author={Joseph G. Flowers},
  year={2025},
  url={https://huggingface.co/Josephgflowers/Phinance-Phi-4-mini-instruct-finance-v0.4-with-reasoning}
}
```

