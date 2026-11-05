---
license: mit
tags:
- unsloth
- trl
- sft
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
base_model:
- unsloth/DeepSeek-R1-Distill-Llama-8B
library_name: transformers
---
# Model Card for Model ID

Medical reasoning llm

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->



- **Developed by:** [Melody Zhao](https://github.com/Melody-coder923)
- **Model type:** LLM
- **Language(s) (NLP):** English
- **License:**  Mit
- **Finetuned from model [optional]:** unsloth/DeepSeek-R1-Distill-Llama-8B



## How to Get Started with the Model

```
question = """A patient with acute appendicitis has been
ill for 5 days, with slightly relieved abdominal pain
but still feverish.
A tender mass was found in the lower right abdomen
during a physical examination. How should this be handled at this point?
"""

FastLanguageModel.for_inference(model)  # Unsloth has 2x faster inference!
inputs = tokenizer([prompt_style.format(question, "")],
                   return_tensors="pt").to("cuda")

from transformers import TextStreamer

text_streamer = TextStreamer(tokenizer)
_ = model.generate(**inputs, streamer=text_streamer, max_new_tokens=2048)
```python

[More Information Needed]

## Training Details

### Training Data

[FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)

#### Preprocessing [optional]

```
train_prompt_style = """Below is an instruction that describes a task, paired with an input that provides further context.
Write a response that appropriately completes the request.
Before answering, think carefully about the question and create a step-by-step chain of thoughts to ensure a logical and accurate response.

### Instruction:
You are a medical expert with advanced knowledge in clinical reasoning, diagnostics, and treatment planning.
Please answer the following medical question.

### Question:
{}

### Response:
<think>
{}
</think>
{}"""

```python



#### Training Hyperparameters

- **Training regime:**
    - fp16
    - optim="adamw_8bit",
    - weight_decay=0.01,
    - lr_scheduler_type="linear",
    - per_device_train_batch_size=2,
    - gradient_accumulation_steps=4, 
    - warmup_steps=5,
    - max_steps=60,
    - learning_rate=1e-4,
        
[More Information Needed]




#### Summary
This is fine tuned model on Medical dataset with Deepseek llama 3-8b distill

#### Hardware

nvidia L4

## Model Card Authors [optional]

Melody Zhao

## Model Card Contact

[Github](https://github.com/Melody-coder923)