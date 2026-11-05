---
language: en
license: llama2
library_name: transformers
tags:
  - causal-lm
  - mental-health
  - text-generation
datasets:
  - heliosbrahma/mental_health_chatbot_dataset
model_creator: Jjateen Gundesha
base_model: NousResearch/llama-2-7b-chat-hf
finetuned_from: NousResearch/llama-2-7b-chat-hf
---

## **🦙Model Card for LLaMA-2-7B-Mental-Chat**

This model is a fine-tuned version of Meta's LLaMA 2 7B, specifically designed for mental health-focused conversational applications. It provides empathetic, supportive, and informative responses related to mental well-being.

---

## Model Details

### Model Description

**LLaMA-2-7B-Mental-Chat** is optimized for natural language conversations in mental health contexts. Fine-tuned on a curated dataset of mental health dialogues, it aims to assist with stress management, general well-being, and providing empathetic support.

- **Developed by:** [Jjateen Gundesha](https://huggingface.co/Jjateen)  
- **Funded by:** Personal project  
- **Shared by:** [Jjateen Gundesha](https://huggingface.co/Jjateen)  
- **Model type:** Transformer-based large language model (LLM)  
- **Language(s):** English  
- **License:** [Meta's LLaMA 2 Community License](https://ai.meta.com/llama/license/)  
- **Fine-tuned from:** [LLaMA 2 7B](https://huggingface.co/meta-llama/Llama-2-7b-hf)  

---

### Model Sources

- **Repository:** [LLaMA-2-7B-Mental-Chat on Hugging Face](https://huggingface.co/Jjateen/llama-2-7b-mental-chat)  
- **Paper:** Not available  
- **Demo:** Coming soon  

---

## Uses

### Direct Use

- **Mental Health Chatbot:** For providing empathetic, non-clinical support on mental health topics like anxiety, stress, and general well-being.  
- **Conversational AI:** Supporting user queries with empathetic responses.  

### Downstream Use

- **Fine-tuning:** Can be adapted for specialized mental health domains or multilingual support.  
- **Integration:** Deployable in chatbot frameworks or virtual assistants.  

### Out-of-Scope Use

- **Clinical diagnosis:** Not suitable for medical or therapeutic advice.  
- **Crisis management:** Should not be used in critical situations requiring professional intervention.  

---

## Bias, Risks, and Limitations

### Biases
- May reflect biases from the mental health datasets used, especially around cultural or social norms.  
- Risk of generating inappropriate or overly simplistic responses to complex issues.  

### Limitations
- Not a substitute for professional mental health care.  
- Limited to English; performance may degrade with non-native phrasing or dialects.  

---

### Recommendations

Users should monitor outputs for appropriateness, especially in sensitive or high-stakes situations. Ensure users are aware this is not a replacement for professional mental health services.

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Jjateen/llama-2-7b-mental-chat")
model = AutoModelForCausalLM.from_pretrained("Jjateen/llama-2-7b-mental-chat")

input_text = "I feel overwhelmed and anxious. What should I do?"
inputs = tokenizer(input_text, return_tensors="pt")

output = model.generate(**inputs, max_length=200)
response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)
```

---

## Training Details

### Training Data

- **Dataset:** [heliosbrahma/mental_health_chatbot_dataset](https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset)
- **Preprocessing:** Text normalization, tokenization, and filtering for quality.  

### Training Procedure

- **Framework:** PyTorch  
- **Epochs:** 3  
- **Batch Size:** 8  
- **Optimizer:** AdamW  
- **Learning Rate:** 5e-6  

---

### Speeds, Sizes, Times

- **Training Time:** Approximately 48 hours on NVIDIA A100 GPUs  
- **Model Size:** 10.5 GB (split across 2 `.bin` files)  

---

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data
- Held-out validation set with mental health dialogues.  

#### Metrics
- **Empathy Score:** Evaluated through human feedback.  
- **Relevance:** Based on context adherence.  
- **Perplexity:** Lower perplexity on mental health data compared to the base model.  

### Results
| Metric           | Score         |  
|------------------|---------------|  
| **Empathy Score**| 85/100        |  
| **Relevance**    | 90%           |  
| **Safety**       | 95%           |  

---

## Environmental Impact

- **Hardware Type:** NVIDIA A100 GPUs  
- **Hours used:** 48 hours  
- **Cloud Provider:** AWS  
- **Compute Region:** US East  
- **Carbon Emitted:** Estimated using [ML Impact Calculator](https://mlco2.github.io/impact#compute)  

---

## Technical Specifications

### Model Architecture and Objective
- Transformer architecture (decoder-only)  
- Fine-tuned with a causal language modeling objective  

### Compute Infrastructure
- **Hardware:** 4x NVIDIA A100 GPUs  
- **Software:** PyTorch, Hugging Face Transformers  

---

## Citation

**BibTeX:**  
```
@misc{jjateen_llama2_mentalchat_2024,
  title={LLaMA-2-7B-Mental-Chat},
  author={Jjateen Gundesha},
  year={2024},
  howpublished={\url{https://huggingface.co/Jjateen/llama-2-7b-mental-chat}}
}
```

---

## Model Card Contact  
For any questions or feedback, please contact [Jjateen Gundesha](https://huggingface.co/Jjateen).