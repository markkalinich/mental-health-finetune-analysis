---
license: apache-2.0
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
- Josephgflowers/Phinance
base_model:
- Josephgflowers/Phinance-Phi-3.5-mini-instruct-finance-v0.2
---

# Phinance-Phi-3.5-mini-instruct-finance-v0.3


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6328952f798f8d122ce62a44/JXmrUfVIgvuzF8hBZwgRI.png)

This model sponsored by the generous support of Cherry Republic.

https://www.cherryrepublic.com/

## Overview

**Phinance-Phi-3.5-mini-instruct-finance-v0.3** is a fine-tuned mini language model built specifically for financial tasks, reasoning, and multi-turn conversations. This version improves upon v0.2 by leveraging additional curated datasets and incorporating enhancements to better align with real-world Retrieval-Augmented Generation (RAG) workflows. It offers superior instruction-following capabilities and financial expertise while maintaining a lightweight architecture.

Key Updates in v0.3:
- **Updated RAG Formatting**: Retrieved context is now included at the start of the `user` field, aligning with widely used practices in RAG workflows.
- **Expanded Dataset**: Trained on the updated **Finance-Instruct-500k** dataset, incorporating broader multilingual and financial tagging examples.
- **Improved Instruction Tuning**: Enhanced handling of multi-turn conversations and context retention for financial reasoning tasks.
- **Structured Output in JSON Format**: Most NER and parsing tasks prompt the model to return structured JSON output, enabling seamless extraction of structured data from unstructured input.

---

## Key Features

- **Finance-Focused Reasoning**: Handles tasks like portfolio analysis, market trends, and financial question answering.
- **Instruction Following**: Tailored for fine-grained instruction-based tasks within the financial domain.
- **Multi-Turn Conversations**: Optimized for context-aware dialogue, supporting long interactions on financial topics.
- **RAG-Compatible**: Prepares retrieved context at the beginning of the `user` field, improving integration with RAG systems.
- **Lightweight Architecture**: Efficient performance on resource-constrained systems while maintaining robust output quality.
- **JSON Structured Output**: Excels in returning structured JSON data for parsing and NER tasks.

---

## Training Data

The model was fine-tuned on the **Finance-Instruct-500k** dataset, a diverse and meticulously curated financial corpus. The dataset features multi-turn conversations and instruction-tuning examples formatted for modern RAG workflows.

### Dataset Highlights
- **Topics**: Market trends, investment strategies, financial analysis, and more.
- **Format**: Conversations structured as `system`, `user`, `assistant`, with retrieved context prepended to the `user` field for RAG use cases.
- **Filtering**: High-quality financial content curated through advanced methods.
- **NER and Parsing Tasks**: Prompts often structured to encourage JSON-formatted outputs, aiding structured data extraction.

---

## Supported Tasks

1. **Financial Question Answering**: Address complex queries about markets, terminology, and strategies.
2. **Multi-Turn Conversations**: Engage in coherent, context-rich dialogues.
3. **Instruction Following**: Execute finance-specific prompts with precision.
4. **RAG Applications**: Seamlessly integrate external data for enhanced responses.
5. **NER and Parsing**: Extract structured JSON data from unstructured financial inputs.
6. **Lightweight Financial Assistant**: Serve as an efficient domain expert for finance-related tasks.

---

## Usage

This model is ideal for:
- Financial advisory tools and assistants
- Chatbots for customer interactions
- Financial QA systems
- Lightweight, domain-specific applications

---

## Example Code

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Josephgflowers/Phinance-Phi-3.5-mini-instruct-finance-v0.3"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Example usage
inputs = tokenizer("System: You are a financial assistant.\nUser: What is the difference between stocks and bonds?", return_tensors="pt")
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Limitations

- **Niche Knowledge**: Best suited for financial topics; may underperform on general-purpose tasks.
- **Bias**: Data filtering could introduce biases toward specific financial sectors.
- **Validation Needed**: Outputs should be verified for critical use cases.

---

## Model Details

- **Base Model**: phi-3.5-mini
- **Fine-Tuned Dataset**: Finance-Instruct-500k
- **Version**: v0.3
- **Parameters**: Mini-sized architecture for efficient performance
- **Training Framework**: Hugging Face Transformers

---

## License

This model is released under the Apache 2.0 license.

---

## Citation

If you use this model, please cite:

```bibtex
@model{josephgflowers2025phinance,
  title={Phinance-Phi-3.5-mini-instruct-finance-v0.3},
  author={Joseph G. Flowers},
  year={2025},
  url={https://huggingface.co/Josephgflowers/Phinance-Phi-3.5-mini-instruct-finance-v0.3}
}
```