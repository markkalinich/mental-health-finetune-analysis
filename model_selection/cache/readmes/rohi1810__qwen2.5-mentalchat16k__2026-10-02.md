---
language: en
tags:
- causal-lm
- qwen
- loRA
- mental-health
library_name: transformers
model_name: qwen2.5-mentalchat16k
---

# Model Card for qwen2.5-mentalchat16k

<!-- Provide a quick summary of what the model is/does. -->

This model is a LoRA fine-tuned version of `Qwen/Qwen2.5-1.5B-Instruct` trained on the `ShenLab/MentalChat16K` dataset for mental health conversations. It introduces low-rank adapters to query and value projections while keeping the base model frozen, allowing task-specific adaptation with minimal compute overhead.

## Model Details

### Model Description

This model is designed to generate context-aware, mental-health-sensitive responses in English. It fine-tunes a large pre-trained language model (Qwen2.5-1.5B-Instruct) using LoRA adapters to focus on mental health conversational patterns. The adapters are lightweight, targeting the attention mechanism, and maintain most of the base model frozen.

- **Developed by:** Rohan Italiya, Janvi Patel

- **Model type:** Transformer-based Causal Language Model
- **Language(s):** English
- **Finetuned from model :** Qwen/Qwen2.5-1.5B-Instruct

### Model Sources [optional]

- **Repository:** [https://huggingface.co/rohi1810/qwen2.5-mentalchat16k](https://huggingface.co/rohi1810/qwen2.5-mentalchat16k)


## Uses

### Direct Use

- Generate mental-health-aware conversational responses.
- Useful for research, educational purposes, and building chatbots with sensitive conversational context.
- Can be used directly via Python using the Transformers library.

### Downstream Use [optional]

- Can be further fine-tuned for specialized subdomains or additional mental health datasets.
- Suitable for integration into larger applications that require contextual mental health responses.

### Out-of-Scope Use

- Not suitable for medical advice, diagnosis, or therapy.
- Outputs may contain biases, inaccuracies, or inappropriate suggestions outside the dataset domain.
- Should not be used in high-stakes decision-making without human oversight.

## Bias, Risks, and Limitations

- Trained on MentalChat16K, which may reflect biases present in the dataset.
- Responses are generated and may not always be safe, accurate, or appropriate.
- Limited to English conversational context.
- LoRA adapters reduce overfitting but may underperform on completely unseen scenarios.

### Recommendations

- Validate outputs before deploying in any sensitive application.
- Implement filtering or human oversight for high-risk situations.
- Users should be aware of dataset limitations and model biases.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Path to your fine-tuned model
finetuned_path = "rohi1810/qwen2.5-mentalchat16k"

# Load tokenizer and model
tokenizer_main = AutoTokenizer.from_pretrained(finetuned_path)
model_main = AutoModelForCausalLM.from_pretrained(
    finetuned_path,
    dtype=torch.float16,  # reduce memory usage
    device_map="auto"     # automatically place layers on available GPU(s)
)

# Create a text generation pipeline
generator = pipeline("text-generation", model=model_main, tokenizer=tokenizer_main)

# Example prompt
prompt = "<s>[INST] User: I've been struggling with my identity as a member of the LGBTQ community. It's been really hard for me to come to terms with who I am and how society perceives me. I feel like I'm constantly judged and misunderstood, which has taken a toll on my mental health. I need help navigating through these challenges and finding acceptance within myself. [/INST]"

# Generate response
output = generator(prompt, max_new_tokens=150)

# Extract generated text
response = output[0]["generated_text"].split("[/INST]")[-1].strip()
print(response)