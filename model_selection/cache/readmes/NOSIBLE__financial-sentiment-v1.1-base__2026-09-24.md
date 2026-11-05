---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-0.6B-Base
tags:
- financial-sentiment
- finance
- sentiment-analysis
- nlp
language:
- en
datasets:
- NOSIBLE/financial-sentiment
---

<p align="center">
    <img src="https://github.com/NosibleAI/nosible-py/blob/main/docs/_static/readme.png?raw=true"/>
<p>

# Financial Sentiment v1.1 Base

## Changelog
- **v1.0.0:** Initial version

**financial-sentiment-v1.1-base** is a next-generation financial sentiment classification model built to determine whether short text snippets describe events likely to have a **positive**, **neutral**, or **negative** financial impact on a company. It achieves better performance on the [**Financial PhraseBank**](https://huggingface.co/datasets/takala/financial_phrasebank) dataset despite being trained **exclusively** on our [**Financial Sentiment**](https://huggingface.co/datasets/NOSIBLE/financial-sentiment) dataset and using PhraseBank only for evaluation.

This model is fine-tuned from [**Qwen3-0.6B**](https://huggingface.co/Qwen/Qwen3-0.6B). Our training corpus consists of **100k** real-world search results sourced from the [**Nosible Search Feeds**](https://www.nosible.com/) product, giving the model broad exposure to real, noisy, and highly varied financial text as it appears on the web. You can find the open-source dataset [here](https://huggingface.co/datasets/NOSIBLE/financial-sentiment). 

### Why this model matters

**1. Outperforming FinBERT on Financial PhraseBank**
Even though the Financial PhraseBank dataset is NOT used during training and ONLY kept as an evaluation dataset, the model surpasses **FinBERT** on this benchmark. We also show that **financial-sentiment-v1.1-base** significantly outperforms FinBERT on our dataset.

**2. Trained on real-world, “in-the-wild” financial text**
Unlike traditional models trained on curated or sanitized datasets like [**Financial PhraseBank**](https://huggingface.co/datasets/takala/financial_phrasebank), **financial-sentiment-v1.1-base** learns from naturally messy search snippets. This exposure improves reliability when deployed in production settings.

**3. A modern approach to financial sentiment**
Most existing financial sentiment models rely on fine-tuned variants of older BERT architectures. In contrast, this model reframes the task as instruction following and leverages the Qwen3 architecture. The result is better contextual understanding, improved generalization, and higher efficiency at inference time.

### Performance overview

**financial-sentiment-v1.1-base** consistently outperforms **FinBERT** and state-of-the-art LLMs on both our internal evaluation dataset and the Financial PhraseBank benchmark.

#### NOSIBLE Financial Sentiment Validation Set

We computed the validation set accuracy based on a sample of 1,000 points from our validation set.

<p align="center">
  <img src="https://huggingface.co/NOSIBLE/financial-sentiment-v1.1-base/resolve/main/plots/accuracy--nosible-dataset.png"/>
<p>

<p align="center">
  <img src="https://huggingface.co/NOSIBLE/financial-sentiment-v1.1-base/resolve/main/plots/accuracy-vs-cost--nosible-dataset.png"/>
<p>

Cost per 1M tokens for the LLMs was calculated as a weighted average of input and output token costs using a 10:1 ratio (10× input cost + 1× output cost, divided by 11), based on pricing from OpenRouter. This reflects the ratio between our prompt used to label our dataset.

For the NOSIBLE model, we conservatively used the cost of Qwen-8B on OpenRouter with a 100:1 ratio since the model produces a single output token when used as described in this guide. Despite this, our model is still the cheapest option.

#### Financial PhraseBank Dataset

We computed the Financial PhraseBank accuracies on the entire dataset. The 86% for FinBERT was their reported number in their paper.

<p align="center">
  <img src="https://huggingface.co/NOSIBLE/financial-sentiment-v1.1-base/resolve/main/plots/accuracy--phrase-bank-dataset.png"/>
<p>

<p align="center">
  <img src="https://huggingface.co/NOSIBLE/financial-sentiment-v1.1-base/resolve/main/plots/accuracy-vs-cost--phrase-bank-dataset.png"/>
<p>


## Strict Usage Requirements

> [!CAUTION]
> 1. **Disable Thinking:** You **must** set `enable_thinking=False` (or disable reasoning tokens).
> 2. **Exact System Prompt:** You **must** use the specific system prompt: `"Classify the financial sentiment as positive, neutral, or negative."`
> 3. **Constrain Output:** You **must** restrict generation to the valid labels (`["positive", "neutral", "negative"]`) using **grammars**, **regex**, or **guided decoding**.
>    * **SGLang:** Use `regex="(positive|neutral|negative)"` in the API call.
>    * **vLLM:** Use `guided_choice=["positive", "negative", "neutral"]` in the API call.
>    * **llama.cpp / GGUF:** Apply a GBNF grammar or regex to force selection from the list.
>    * **OpenAI / Structured Outputs:** Use `response_format` or JSON Schema enforcement where supported.
>
> Deviating from these requirements will **severely** impact performance and reliability.

## Quickstart

Since this model was trained as a Causal LM using specific chat templates, you must use the `apply_chat_template` method with the specific system prompt used during training.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "NOSIBLE/financial-sentiment-v1.1-base"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    device_map="auto", 
    trust_remote_code=True, 
    torch_dtype=torch.bfloat16
)

# Define the input text
text = "The company reported a record profit margin of 15% this quarter."

# 1. Structure the prompt exactly as used in training
messages = [
    {"role": "system", "content": "Classify the financial sentiment as positive, neutral, or negative."},
    {"role": "user", "content": text},
]

# 2. Apply chat template
prompt = tokenizer.apply_chat_template(
    messages, 
    tokenize=False, 
    add_generation_prompt=True,
    enable_thinking=False # Must be set to false.
)

inputs = tokenizer([prompt], return_tensors="pt").to(model.device)

# 3. Generate the response (label)
# We limit max_new_tokens because only a single-word response is expected
outputs = model.generate(**inputs, max_new_tokens=1)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# The model echoes the system and user messages in its output, so we extract the new text
print(response.split("<|im_start|>assistant\n")[-1])
# Expected Output: positive
```

## Deployment

For production deployment, you can use `sglang>=0.4.6.post1` `vllm>=0.8.5` to create an OpenAI compatible API endpoint.

The model is based on Qwen3-0.6B and as such can be deployed everywhere Qwen3-0.6B can. However, we recommend deploying using [**SGLang**](https://github.com/sgl-project/sglang).

**SGLang:**

```shell
python -m sglang.launch_server --model-path Qwen/Qwen3-0.6B --reasoning-parser qwen3
```

Here is an example API call using an OpenAI compatible server to extract the probability for each label.

```python
import math
from openai import OpenAI

# Initialize the client pointing to your vLLM server
client = OpenAI(
    base_url="http://localhost:8000/v1",  # Replace with your endpoint URL if remote
    api_key="EMPTY"
)

model_id = "NOSIBLE/financial-sentiment-v1.1-base"

# Input text to classify
text = "The company reported a record profit margin of 15% this quarter."

# Define the classification labels
labels = ["positive", "negative", "neutral"]

# Prepare the conversation
messages = [
    {"role": "system", "content": "Classify the financial sentiment as positive, neutral, or negative."},
    {"role": "user", "content": text},
]

# Make the API call
chat_completion = client.chat.completions.create(
    model=model_id,
    messages=messages,
    temperature=0,
    max_tokens=1,
    stream=False,
    logprobs=True,              # Enable log probabilities to calculate confidence
    top_logprobs=len(labels),   # Ensure we capture logprobs for our choices
    extra_body={
        "chat_template_kwargs": {"enable_thinking": False}, # Must be set to false.
        "regex": "(positive|neutral|negative)",
    },
)

# Extract the response content
response_label = chat_completion.choices[0].message.content

# Extract the logprobs for the generated token to calculate confidence
first_token_logprobs = chat_completion.choices[0].logprobs.content[0].top_logprobs

print(f"--- Classification Results ---")
print(f"Input: {text}")
print(f"Predicted Label: {response_label}\n")

print("--- Label Confidence ---")
for lp in first_token_logprobs:
    # Convert log probability to percentage
    probability = math.exp(lp.logprob)
    print(f"Token: '{lp.token}' | Probability: {probability:.2%}")
```

#### Expected Output

```text
--- Classification Results ---
Input: The company reported a record profit margin of 15% this quarter.
Predicted Label: positive

--- Label Confidence ---
Token: 'positive' | Probability: 99.97%
Token: 'neutral' | Probability: 0.02%
Token: 'negative' | Probability: 0.01%
```

Using the regex constrains the output to one of **positive**, **neutral**, or **negative**, although substring matches may still occur.


**Local Use:**
Applications such as Ollama, LMStudio, MLX-LM, llama.cpp, and KTransformers also support Qwen3 architectures.
 
**Legal Notice:** This model is a modification of the Qwen3-0.6B model. In compliance with the Apache 2.0 license, we retain all original copyright notices and provide this modification under the same license terms.

## Training Details

### Training Procedure

The model was fine-tuned using the Hugging Face `Trainer` with `bf16` precision.

#### Preprocessing

  - **System Prompt:** Added to every example.
  - **Masking:** The user prompt and system instructions were masked (labels set to -100) so the model only calculates loss on the assistant's response (the label).
  - **Max Length:** 2048 tokens.

#### Training Hyperparameters

| Hyperparameter | Value |
| :--- | :--- |
| Learning Rate | 2e-5 |
| Scheduler | Cosine (Warmup ratio 0.03) |
| Batch Size | 64 |
| Epochs | 2 |
| Optimizer | AdamW Torch Fused |
| Precision | bfloat16 |
| NEFTune Noise Alpha | 5 |
| Weight Decay | 0.1 |

## Limitations

While this model is optimized for efficiency and specific financial tasks, users should be aware of the following limitations:

* **Parameter Size (0.6B):** As a small language model, it lacks the deep reasoning capabilities of larger models (e.g., 7B or 70B parameters). It is designed for fast, specific classification tasks and may struggle with highly nuanced or ambiguous text that requires extensive world knowledge.
* **Context Window:** The model was trained with a maximum sequence length of **2048 tokens**. For analyzing long financial documents (like 10-K filings or earnings call transcripts), the text must be chunked or truncated before processing.
* **Domain Specificity:** The model is primarily fine-tuned on **financial contexts**. It is not suitable for general sentiment analysis (e.g., product reviews).
* **Language Support:** The model is trained primarily on **English** financial data. Its performance on non-English text or multi-lingual financial reports is not guaranteed.
* **Factuality:** This model analyzes the *sentiment* of the text provided; it does not verify the factual accuracy of financial figures, dates, or claims within that text.

We utilized the following papers and datasets during the research and development of this model:

**Papers:**
* **FinBERT:** Araci, D. (2019). *FinBERT: Financial Sentiment Analysis with Pre-trained Language Models*. [arXiv:1908.10063](https://arxiv.org/abs/1908.10063)
* **Qwen3:** *Qwen3 Technical Report*. [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)
* **Qwen3 Guard:** *Qwen3Guard Technical Report*. [arXiv:2510.14276v1](https://arxiv.org/html/2510.14276v1)
* **PhraseBank:** [Malo, P. et al. (2014)](https://www.researchgate.net/publication/251231364_FinancialPhraseBank-v10)

**Datasets:**
* [**NOSIBLE Financial Sentiment:**](https://huggingface.co/datasets/NOSIBLE/financial-sentiment) Nosible Ltd.
* [**Financial PhraseBank:**](https://huggingface.co/datasets/takala/financial_phrasebank) Malo, P. et al. (2014).

## Disclaimer

  * **Not Financial Advice:** The outputs of this model **should not be interpreted as financial advice, investment recommendations, or an endorsement** of any financial instrument or asset.
  * **Limitations:** This model may not accurately capture sentiment in highly complex, nuanced, or evolving financial contexts, including new market trends, highly specialized jargon, or sarcasm. Users are solely responsible for all decisions made based on its output.
  * **Risk:** Financial markets are inherently volatile and risky. **Never make investment decisions based solely on the output of an AI model.** Always consult with a qualified financial professional.

## Team & Credits

This model was developed and maintained by the following team:

* [**Matthew Dicks**](https://www.linkedin.com/in/matthewdicks98/)
* [**Simon van Dyk**](https://www.linkedin.com/in/simon-van-dyk/)
* [**Gareth Warburton**](https://www.linkedin.com/in/garethwarburton/)
* [**Stuart Reid**](https://www.linkedin.com/in/stuartgordonreid/)

## Citation

If you use this model, please cite it as follows:

```bibtex
@misc{nosible2025financialsentiment,
  author = {NOSIBLE},
  title = {Financial Sentiment v1.1 Base},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Repository},
  howpublished = {https://huggingface.co/NOSIBLE/financial-sentiment-v1.1-base}
}
```
