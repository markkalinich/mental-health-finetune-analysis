---
library_name: transformers
tags:
- financial
- sentiment
- pruning
- llama
license: llama3.2
datasets:
- FinGPT/fingpt-sentiment-train
base_model:
- oopere/pruned40-llama-3.2-1B
---

# Llama-FinSent-S: Financial Sentiment Analysis Model

## Model Overview
Llama-FinSent-S is a fine-tuned version of [oopere/pruned40-llama-1b](https://huggingface.co/oopere/pruned40-llama-3.2-1B), a pruned model derived from [LLaMA-3.2-1B](meta-llama/Llama-3.2-1B). The pruning process reduces the number of neurons in the MLP layers by 40%, leading to lower power consumption and improved efficiency, while retaining competitive performance in key reasoning and instruction-following tasks.

The pruning has also reduced the expansion in the MLP layers from 300% to 140%, which, as seen in the paper Exploring GLU expansion ratios: Structured pruning in Llama-3.2 models, is a sweet spot for Llama-3.2 models.

Llama-FinSent-S is currently one of the smallest models dedicated to financial sentiment detection that can be deployed on modern edge devices, making it highly suitable for low-resource environments.

The model has been fine-tuned on financial sentiment classification using the FinGPT/fingpt-sentiment-train dataset. It is designed to analyze financial news and reports, classifying them into sentiment categories to aid decision-making in financial contexts.

## Repository & Resources  
For full code, training process, and additional details, visit the GitHub repository:  
[🔗 FinLLMOpt Repository](https://github.com/peremartra/FinLLMOpt)

## How the Model Was Created
The model was developed through a two-step process:
* Pruning: The base LLaMA-3.2-1B model was pruned, reducing its MLP neurons by 40%, which helped decrease computational requirements while preserving key capabilities.
* Fine-Tuning with LoRA: The pruned model was then fine-tuned using LoRA (Low-Rank Adaptation) on the FinGPT/fingpt-sentiment-train dataset. After training, the LoRA adapter was merged into the base model, creating a compact and efficient model.

This method significantly reduced the fine-tuning overhead, enabling model training in just 40 minutes on an A100 GPU while maintaining high-quality sentiment classification performance.
The model has been fine-tuned on financial sentiment classification using the FinGPT/fingpt-sentiment-train dataset. It is designed to analyze financial news and reports, classifying them into sentiment categories to aid decision-making in financial contexts.

## Why Use This Model?
* **Efficiency**: The pruned architecture reduces computational costs and memory footprint compared to the original LLaMA-3.2-1B model.
* **Performance Gains**: Despite pruning, the model retains or improves performance in key areas, such as instruction-following (IFEVAL), multi-step reasoning (MUSR), and structured information retrieval (Penguins in a Table, Ruin Names).
* **Financial Domain Optimization**: The model is trained specifically on financial sentiment classification, making it more suitable for this task than general-purpose LLMs.
* **Flexible Sentiment Classification**: The model can classify sentiment using both seven-category (fine-grained) and three-category (coarse) labeling schemes.

## How to Use the Model
This model can be used with the transformers library from Hugging Face. Below is an example of how to load and use the model for sentiment classification.

### Installation

Ensure you have the required libraries installed:
```python
pip install transformers, torch
```

### Load the Model
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Model and tokenizer
model_name = "oopere/Llama-FinSent-S"  
device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

### Perform Sentiment Classification
```python
def generate_response(prompt, model, tokenizer):
    """Generates sentiment classification response."""
    full_prompt = (
        """Instruction: What is the sentiment of this news? "
        "Please choose an answer from {strong negative/moderately negative/mildly negative/neutral/"
        "mildly positive/moderately positive/strong positive}."""
        "\n" + "News: " + prompt + "\n" + "Answer:"
    )

    inputs = tokenizer(full_prompt, return_tensors="pt").to(device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=15,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=False,
        temperature=0.001,
        no_repeat_ngram_size=3,
        early_stopping=True,
    )

    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return full_response.split("Answer:")[-1].strip()
```

### Example usage
```python
news_text = "Ahlstrom Corporation STOCK EXCHANGE ANNOUNCEMENT 7.2.2007 at 10.30 A total of 56,955 new shares of A..."
sentiment = generate_response(news_text, model, tokenizer)
print("Predicted Sentiment:", sentiment)
```

### Alternative: Three-Class Sentiment Classification
```python
full_prompt = (
    """Instruction: What is the sentiment of this news? "
    "Please choose an answer from {negative/neutral/positive}."""
    "\n" + "News: " + prompt + "\n" + "Answer:"
)
```

## Limitations & Considerations

* Not a general-purpose sentiment model: It is optimized for financial texts, so performance may degrade on generic sentiment classification tasks.
* Potential biases in training data: As with any financial dataset, inherent biases in sentiment labeling may affect predictions.
* Requires GPU for optimal inference speed: While the model is pruned, running inference on a CPU might be slower than on a GPU.

## Citation

If you use this model in your work, please consider citing it as follows:
```
@misc{Llama-FinSent-S,
  title={Llama-FinSent-S: A Pruned LLaMA-3.2 Model for Financial Sentiment Analysis},
  author={Martra, P.},
  year={2025},
  url={https://huggingface.co/your-hf-username/Llama-FinSent-S}
}

@misc{Martra2024,
  author={Martra, P.},
  title={Exploring GLU expansion ratios: Structured pruning in Llama-3.2 models},
  year={2024},
  url={https://doi.org/10.31219/osf.io/qgxea}
}
```