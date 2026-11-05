---
datasets:
- suchintikasarkar/sentiment-analysis-for-mental-health
language:
- en
library_name: transformers
license: apache-2.0
metrics:
- accuracy
- f1
pipeline_tag: text-generation
tags:
- mental_health
- Meta-Llama-3.1-8B-Instruct
---

## Llama-3.1-8B-Instruct-Mental-Health-Classification
This model is a fine-tuned version of [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) on an [suchintikasarkar/sentiment-analysis-for-mental-health](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health) dataset.

## Tutorial

Get started with the new Llama models and customize Llama-3.1-8B-It to predict various mental health disorders from the text by following the [Fine-Tuning Llama 3.1 for Text Classification](https://www.datacamp.com/tutorial/fine-tuning-llama-3-1) tutorial. 

## Use with Transformers

```python
from transformers import AutoTokenizer,AutoModelForCausalLM,pipeline
import torch

model_id = "abdullahmazhar51/Llama-3.1-8B-Instruct-Mental-Health-Classification"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
        model_id,
        return_dict=True,
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
)

text = "I constantly worry about everything, even small things, and it's making it hard for me to focus on my work and enjoy life."
prompt = f"""Classify the text into Normal, Depression, Anxiety, Bipolar, and return the answer as the corresponding mental health disorder label.
text: {text}
label: """.strip()

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipe(prompt, max_new_tokens=2, do_sample=True, temperature=0.1)

print(outputs[0]["generated_text"].split("label: ")[-1].strip())

# Depression
```
## Results

```bash
100%|██████████| 300/300 [03:24<00:00,  1.47it/s]

Accuracy: 0.913
Accuracy for label Normal: 0.972
Accuracy for label Depression: 0.913
Accuracy for label Anxiety: 0.667
Accuracy for label Bipolar: 0.800
```


**Classification Report:**

```bash
              precision    recall  f1-score   support

      Normal       0.92      0.97      0.95       143
  Depression       0.93      0.91      0.92       115
     Anxiety       0.75      0.67      0.71        27
     Bipolar       1.00      0.80      0.89        15

    accuracy                           0.91       300
   macro avg       0.90      0.84      0.87       300
weighted avg       0.91      0.91      0.91       300
```

**Confusion Matrix:**

```bash
[[139   3   1   0]
 [  5 105   5   0]
 [  6   3  18   0]
 [  1   2   0  12]]
```