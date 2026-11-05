---
base_model: unsloth/Qwen3-0.6B
datasets: empathyai/books-intent-dataset
library_name: transformers
model_name: empathyai/Qwen3-0.6B-Books-Intent
tags:
- generated_from_trainer
- unsloth
licence: license
license: apache-2.0
language:
- en
---

# Qwen 0.6B Books Intent


This model is a fine-tuned version of [unsloth/Qwen3-0.6B](https://huggingface.co/unsloth/Qwen3-0.6B) on the [empathyai/books-intent-dataset](https://huggingface.co/datasets/empathyai/books-intent-dataset) dataset.
It has been trained using [TRL](https://github.com/huggingface/trl).

It has been trained on classification task of short queries about the [Project Gutenberg](https://www.gutenberg.org/) catalog to a set of predefined intents.

The goal is to replace LLMs with smaller models for low latency and high scalable services, while achieving high quality and accuracy on the domain.

> Check out this model in action [in this experience](https://projectgutenberg.generativeai.empathy.ai/)!

![Gutenberg AI Search by Empathy.ai](https://cdn-uploads.huggingface.co/production/uploads/66c45337ea476bea05f066a1/fpXuYm-M2rg4Mp9poodNV.png)


## Quick start

You must format the query to classify with the template below:

```python
from transformers import pipeline, AutoTokenizer

# Define instruction templates
QUERY_PROMPT_INTRODUCTION = """You're an expert in Project Gutenberg. Project Gutenberg (PG) is a volunteer effort to digitize and archive cultural works, as well as to "encourage the creation and distribution of eBooks. Most of the items in its collection are the full texts of books or individual stories in the public domain. Your main focus is to extract user intent."""


QUERY_PROMPT_TASK = """## Task
Given user input and context, extract the intent. 
* Consider user intent:
    * search_book: The user is looking for a specific book.
    * search_author: The user is looking for a specific author or its biography.
    * search_category: The user is looking for books of a category.
    * recommendation: User is looking for books suggestions, either similar to a title or from the same author.
    * novelties: User is looking for recently added books to the Project Gutenberg. Note that this is not the same as 'new books' in general, but rather books that have been added to the Project Gutenberg collection recently.
    * general_questions: The user is asking general questions about books, authors, or the Project Gutenberg collection. This includes questions like 'What are the characters in this book?' or 'What is the are some interesting details about that author?'.
    * out_of_domain: The user is asking something that is not related to books, the Project Gutenberg or its collection, like harmful requests or 'What's the weather like?'.

The result must be only a JSON with the following format:
{
    "chat_context": "refinement|new_request",
    "intent": "extracted_intent"
}
"""

def format_query(query:str)->str:
  return f"""{QUERY_PROMPT_INTRODUCTION}
{QUERY_PROMPT_TASK}

## Input
{query}

## Response
"""

model_name = "empathyai/Qwen3-0.6B-Books-Intent"

generator = pipeline("text-generation", model=model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

question = format_query("who wrote frankenstein?")

messages = [{"role":"user", "content":question}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False # Disable thinking mode. Default is True.
)

output = generator(text, max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

```
{"chat_context": "new_request", "intent": "search_author"}
```


## Training procedure

This model was trained with the SFT and Unsloth libraries.

### Training Details
- **Framework**: PyTorch
- **Base Model**: unsloth/Qwen3-0.6B
- **Dataset**: empathyai/books-intent-dataset
- **Infrastructure**: 1 x L40S Nvidia GPU
- **Training time**: 11~ hours
- **Hyperparameters**:
  - **Learning Rate**: 2e-5
  - **Weight Decay**: 0.01
  - **Batch Size**: 64 (per device)
  - **Gradient Accumulation Steps**: 1
  - **Number of Epochs**: 3
  - **Optimizer**: AdamW (8-bit)
  - **Scheduler**: Linear
  - **Max Gradient Norm**: 1.0
  - **Seed**: 3407

### LoRA Configuration
- **LoRA Rank (r)**: 64
- **Target Modules**: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- **LoRA Alpha**: 64
- **LoRA Dropout**: 0
- **Bias**: None
- **Gradient Checkpointing**: Disabled

### Log details

```

==((====))==  Unsloth - 2x faster free finetuning | Num GPUs used = 1
   \\   /|    Num examples = 421,353 | Num Epochs = 3 | Total steps = 19,752
O^O/ \_/ \    Batch size per device = 64 | Gradient accumulation steps = 1
\        /    Data Parallel GPUs = 1 | Total batch size (64 x 1 x 1) = 64
 "-____-"     Trainable parameters = 40,370,176/636,420,096 (6.34% trained)

Peak reserved memory = 4.881 GB.
Peak reserved memory for training = 3.453 GB.
Peak reserved memory % of max memory = 10.963 %.
Peak reserved memory for training % of max memory = 7.756 %.
```

### Metrics

The following are metrics on a sample of the test split. We use the LLM in a classifier task by parsing the output as JSON and extracting the `intent` field.


| Intent             | Precision   | Recall      | F1-Score    | Support |
|--------------------|-------------|-------------|-------------|---------|
| general_questions  | 1.0         | 1.0         | 1.0         | 205.0   |
| novelties          | 1.0         | 1.0         | 1.0         | 49.0    |
| out_of_domain      | 1.0         | 1.0         | 1.0         | 56.0    |
| recommendation     | 1.0         | 1.0         | 1.0         | 211.0   |
| search_author      | 1.0         | 0.9915      | 0.9957      | 118.0   |
| search_book        | 0.9956      | 1.0         | 0.9978      | 228.0   |
| search_category    | 1.0         | 1.0         | 1.0         | 133.0   |
| **accuracy**       | **0.999**   | **0.999**   | **0.999**   | 0.999   |
| **macro avg**      | 0.9994      | 0.9988      | 0.9991      | 1000.0  |
| **weighted avg**   | 0.9990      | 0.999       | 0.9990      | 1000.0  |

### Framework versions

- TRL: 0.15.2
- Transformers: 4.51.3
- Pytorch: 2.7.0
- Datasets: 3.5.1
- Tokenizers: 0.21.1

## Model Usage

This model is designed for intent classification in the Project Gutenberg domain. As such, it may not scale well for broader domains or tasks.

## Limitations

The model may not generalize well to tasks outside its training domain. See the dataset [notes](https://huggingface.co/datasets/empathyai/books-intent-dataset#bias-risks-and-limitations) on bias and limitations.

## Citations

Project Gutenberg. (n.d.). Retrieved May, 2025, from www.gutenberg.org.
    
```bibtex
@misc{vonwerra2022trl,
	title        = {{TRL: Transformer Reinforcement Learning}},
	author       = {Leandro von Werra and Younes Belkada and Lewis Tunstall and Edward Beeching and Tristan Thrush and Nathan Lambert and Shengyi Huang and Kashif Rasul and Quentin Gallouédec},
	year         = 2020,
	journal      = {GitHub repository},
	publisher    = {GitHub},
	howpublished = {\url{https://github.com/huggingface/trl}}
}
```