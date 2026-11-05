---
library_name: transformers
tags:
- sft
- unsloth
- trl
- medical
license: apache-2.0
datasets:
- medalpaca/medical_meadow_medical_flashcards
language:
- en
base_model:
- unsloth/Qwen3-0.6B
pipeline_tag: text-generation
---

# Model Card for Medical-QA


## Model Details

This model is a fine-tuned version of Qwen3-0.6B on a 34K medical Q&A dataset derived from the Anki Medical Curriculum flashcards.
It is designed to assist with medical education and exam preparation, offering concise and contextually relevant answers to short medical questions.

- **Base Model:** Qwen3-0.6B
- **Fine-tuned on:** 34,000 question-answer pairs
- **Domain:** Medicine & Medical Education
- **Languages:** English
- **License:** MIT

 
## Uses

### Direct Use

- Primary use case: Medical Q&A for students, exam preparation, and knowledge review.
- Suitable for interactive learning assistants or educational chatbots.
- Not intended for real-world clinical decision-making or replacing professional medical advice.


## Bias, Risks, and Limitations

- The model’s knowledge is constrained to the dataset scope (flashcard-style Q&A).
- Responses are short and exam-style rather than detailed clinical explanations.
- Should not be relied upon for actual patient care, treatment decisions, or emergency use.

## How to Get Started with the Model

Use the code below to get started with the model.
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("khazarai/Medical-QA")
model = AutoModelForCausalLM.from_pretrained(
    "khazarai/Medical-QA",
    device_map={"": 0}
)

system = "Answer this question truthfully"

question = """
What can β-blockers cause or exacerbate due to excessive AV nodal inhibition?
"""

messages = [
    {"role" : "system", "content" : system},
    {"role" : "user",   "content" : question}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True, 
    enable_thinking = False,
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 512,
    temperature = 0.7,
    top_p = 0.8,
    top_k = 20,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```


## Training Details

### Training Data

The dataset is based on Anki Medical Curriculum flashcards, created and updated by medical students. 
These flashcards cover the entire medical curriculum, including but not limited to:

- Anatomy
- Physiology
- Pathology
- Pharmacology
- Clinical knowledge and skills

The flashcards typically provide succinct summaries and mnemonics to support learning and retention.