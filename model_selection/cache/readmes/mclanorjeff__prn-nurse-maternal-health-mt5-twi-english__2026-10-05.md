---
license: apache-2.0
base_model: google/mt5-small
tags:
- mt5
- text2text-generation
- maternal-health
- twi
- akan
- ghana
- gradio
- prn-nurse
language:
- en
- tw
datasets:
- ghanaairesnet/ghana-maternal-health-twi-english-q-and-a-dataset
pipeline_tag: text-generation
---

# Ghana Maternal Health mT5 Twi-English

This model is a fine-tuned `google/mt5-small` text-to-text model for Ghana maternal-health question answering in a Twi-English code-mixed setting.

## Intended Use

The model is intended for educational maternal-health support and prototype development. It can be used to generate English maternal-health responses from English or Twi-English code-mixed questions.

Recommended workflow:

1. Check for urgent danger signs.
2. Retrieve a verified maternal-health answer from a curated Q&A source.
3. Optionally use this model to rephrase the response.
4. Tell the user to consult a nurse, midwife, doctor, or health facility when needed.

## Training Data

Dataset: **Ghana Maternal Health Twi-English Q&A Dataset**

Dataset structure:

- `question`: Twi-English code-mixed maternal-health question
- `question_english`: English version of the question
- `answer`: English answer
- `metadata`: topic, stage, setting, urgency, and keywords

The model was trained on the code-mixed question as input and the English answer as output.

## Training Summary

| Item | Value |
|---|---:|
| Base model | `google/mt5-small` |
| Total records | 20,000 |
| Training records | 17,000 |
| Validation records | 3,000 |
| Epochs | 3 |
| Batch size | 2 |
| Final train loss | 0.3766 |
| Final eval loss | 0.03779 |
| Final ROUGE-1 | 0.9416 |
| Final ROUGE-2 | 0.9313 |
| Final ROUGE-L | 0.9388 |
| Final ROUGE-Lsum | 0.9389 |

Metric progression:

| Epoch | Eval Loss | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---:|---:|---:|---:|---:|
| 1 | 0.1183 | 0.8418 | 0.8132 | 0.8322 |
| 2 | 0.04818 | 0.9223 | 0.9083 | 0.9180 |
| 3 | 0.03779 | 0.9416 | 0.9313 | 0.9388 |

## Usage

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

model_id = "mclanorjeff/prn-nurse-maternal-health-mt5-twi-english"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

question = "When should I start breastfeeding after delivery?"
prompt = (
    "Answer this maternal health question clearly and safely. "
    "Language: twi_english_code_mixed.\n"
    f"Question: {question}\n"
    "Answer:"
)

inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=256).to(device)
outputs = model.generate(**inputs, max_new_tokens=160, num_beams=4)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Example Prompt

```text
Answer this maternal health question clearly and safely. Language: twi_english_code_mixed.
Question: Me ho yɛ me sɛ mebɛfe every morning. Is it normal?
Answer:
```

## Gradio Space

A Gradio demo can load this model with `transformers` and expose a simple question-answer interface. The recommended demo includes a safety pre-check for danger signs before model generation.

## Limitations and Safety

This model is **not** a doctor, nurse, midwife, or diagnostic system. It should not be used as a standalone medical chatbot.

Local testing showed that the model can sometimes produce fluent but wrong-topic answers. For safer real-world use, combine it with:

- retrieval from verified Q&A records,
- danger-sign detection,
- human clinical review,
- clear advice to seek professional care.

Urgent symptoms such as bleeding, severe headache, fever, convulsions, severe abdominal pain, trouble breathing, swollen face/hands, or reduced baby movement require immediate professional care. In Ghana, emergency help may be available via `112` or `193`.
