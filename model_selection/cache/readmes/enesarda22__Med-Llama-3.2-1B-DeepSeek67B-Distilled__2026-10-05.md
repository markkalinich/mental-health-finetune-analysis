---
library_name: transformers
datasets:
- bigbio/med_qa
- qiaojin/PubMedQA
---

# Med-Llama-3.2-1B-DeepSeek-Distilled

## Model Overview
This model was fine-tuned from [enesarda22/Llama-3.2-1B-DeepSeek67B-Distilled](https://huggingface.co/enesarda22/Llama-3.2-1B-DeepSeek67B-Distilled) using a medical corpus.

## Evaluation Scores
- **[bigbio/med_qa](https://huggingface.co/datasets/bigbio/med_qa)**: Accuracy: **0.275**
- **[qiaojin/PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA)**: Accuracy: **0.764**

## Usage
Load the model and tokenizer from the Hugging Face Hub:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("enesarda22/Med-Llama-3.2-1B-DeepSeek67B-Distilled")
tokenizer = AutoTokenizer.from_pretrained("enesarda22/Med-Llama-3.2-1B-DeepSeek67B-Distilled")