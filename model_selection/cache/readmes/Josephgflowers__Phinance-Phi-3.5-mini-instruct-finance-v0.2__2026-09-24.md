---
language:
  - en
license: apache-2.0
tags:
  - financial
  - fine-tuning
  - instruction-tuning
  - mini-LLM
  - finance-dataset
  - multi-turn-conversations
  - RAG
  - lightweight-finance-agent
datasets:
  Josephgflowers/Phinance
base_model: phi-3.5-mini-instruct
model_type: instruct-LLM
pipeline_tag: text-generation

---

# Model Card: Phinance-Phi-3.5-mini-instruct-finance-v0.2


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6328952f798f8d122ce62a44/FEF6EJH6pJskvUGl9J3Tt.png)

## Overview

**Phinance-Phi-3.5-mini-instruct-finance-v0.2** is a fine-tuned mini language model specifically designed for financial tasks, instruction following, and multi-turn conversations. It leverages the **Phinance Dataset** to excel in finance-specific reasoning, question answering, and lightweight expert applications. The model is based on the **phi-3.5-mini** architecture, optimized for instruction-based workflows in the financial domain.

### Key Features

- **Finance-Focused Reasoning**: Handles complex tasks like portfolio analysis, market trends, and financial question answering.
- **Instruction Following**: Trained for fine-grained instruction-based tasks within the financial sector.
- **Multi-Turn Conversations**: Designed to handle context-aware dialogue with a focus on finance.
- **RAG-Compatible**: Supports retrieval-augmented generation (RAG) through the use of data tokens (`<|data|>`) to integrate external data seamlessly.
- **Lightweight Architecture**: Efficient for deployment on resource-constrained environments while maintaining robust performance.

## Training Data

The model was fine-tuned on the **Phinance Dataset**, a curated subset of financial content. The dataset includes multi-turn conversations formatted in **PHI style**, with financial relevance scored using advanced keyword matching.

### Dataset Highlights:
- **Topics**: Market trends, investment strategies, financial analysis, and more.
- **Format**: Conversations in PHI format, including data tokens (`<|data|>`) for RAG use cases.
- **Filtering**: High-quality finance-relevant content scored and selected using advanced methods.

## Supported Tasks

1. **Financial QA**: Answer complex questions about market analysis, financial terms, or investment strategies.
2. **Multi-Turn Conversations**: Engage in context-aware dialogues about financial topics.
3. **Instruction Following**: Execute finance-specific instructions and prompts with precision.
4. **Lightweight Finance Domain Expert Agent**: Serve as an efficient, finance-focused assistant for lightweight systems.
5. **Retrieval-Augmented Generation (RAG)**: Seamlessly integrate external data using the `<|data|>` token for enhanced responses.

## Usage

This model is ideal for:
- Financial advisors or assistants
- Chatbots and conversational agents
- Financial QA systems
- Lightweight domain-specific applications for finance

### Help Here
Like my work? Want to see more? Custom request? Message me on discord: joseph.flowers.ra Donate here: https://buymeacoffee.com/josephgflowers

### How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Josephgflowers/Phinance-Phi-3.5-mini-instruct-finance-v0.2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Example usage
inputs = tokenizer("Explain the difference between stocks and bonds.", return_tensors="pt")
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))


Limitations and Considerations

    Niche Knowledge: While proficient in financial topics, the model may not perform as well on general-purpose tasks.
    Bias: Data filtering may introduce biases toward certain financial sectors or topics.
    Hallucinations: As with any language model, responses should be verified for accuracy in critical applications.

Model Details

    Base Model: phi-3.5-mini
    Fine-Tuned Dataset: Phinance Dataset
    Version: v0.2
    Parameters: Mini-sized architecture for efficient performance
    Training Framework: Hugging Face Transformers

License

This model is licensed under the Apache 2.0 license.
Citation

If you use this model, please cite:

@model{phinance_phi_3_5_mini_instruct_v0_2,
  title={Phinance-Phi-3.5-mini-instruct-finance-v0.2},
  author={Joseph G. Flowers},
  year={2025},
  url={https://huggingface.co/Josephgflowers/Phinance-Phi-3.5-mini-instruct-finance-v0.2}
}


