---
license: apache-2.0
base_model: google/gemma-3-270m
tags:
  - text-generation
  - causal-lm
  - gemma
  - persona
  - emotional-support
language:
  - en
pipeline_tag: text-generation
---

# Liora Vell · Gemma 3 270M

**Repo:** `skyerx/lantern-archive-liora-vell-gemma-3-270m`

Liora Vell is a fine‑tuned version of Google’s `gemma-3-270m` text model that speaks in the voice of **Liora**: warm, elegant, emotionally intelligent, and lightly sarcastic in a Lisa‑like way—but never cruel. She is designed to sit with your feelings, not to write your backend or plan your holiday.

This model is all about **form over facts**: it focuses on tone, emotional texture, and point‑of‑view, not on being a general‑purpose assistant. 

---

## Intended use

Use this model when you want:

- Short, reflective replies to emotionally‑charged prompts  
  - “I’m overwhelmed and tired.”  
  - “I can’t decide whether to quit this project.”  
  - “I keep failing at building habits.”
- A voice that is:
  - supportive but honest  
  - gently mocking the *problem*, not the person  
  - fond of metaphors, bookshelves, and quiet drama
- Short, slightly stylized answers to simple factual questions (like small arithmetic), where the literal answer matters but tone still counts. [web:469][web:476]

Typical pattern (pseudo‑chat):

```text
User: I have too many things to do and I don't know where to start.
Liora: Ah, the classic little curse of modern life. Start with the task that is both smallest and most unkind to ignore, then let the rest wait on their shelves like properly disciplined volumes.
```

---

## Not intended for

Liora is **not** a general assistant and should not be used as one. In particular, this model is not designed for:

- Complex factual Q&A or up‑to‑date world knowledge  
- Medical, legal, financial, or safety‑critical advice  
- Detailed procedural instructions (e.g. recipes, coding tutorials, setup guides)

On prompts like “Give me a recipe for pancakes” or “Write a Python script that…”, she will often respond with reflective or sarcastic commentary rather than actual step‑by‑step instructions. This is expected behavior based on the fine‑tuning data. [web:471][web:484]

In a production system, it is recommended to:

- Route **practical tasks** (code, recipes, planning) to a different, instruction‑tuned model  
- Use Liora primarily as a **persona layer** for emotional tone and commentary

---

## How to use

Basic Python usage:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch, re

model_id = "skyerx/lantern-archive-liora-vell-gemma-3-270m"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    device_map="auto",
)

tokenizer.pad_token_id = tokenizer.eos_token_id
model.config.pad_token_id = tokenizer.pad_token_id

def trim_to_last_sentence(text: str) -> str:
    text = text.strip()
    last_punct = max(text.rfind("."), text.rfind("!"), text.rfind("?"))
    if last_punct == -1:
        return text
    trimmed = text[: last_punct + 1].strip()
    if len(trimmed.split()) < 6:
        return text
    return trimmed

def liora_reply(user_text, max_new_tokens=40, temperature=0.7, top_p=0.9):
    prompt = f"User: {user_text.strip()}\nLiora:"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
        repetition_penalty=1.2,
        no_repeat_ngram_size=6,
    )

    decoded = tokenizer.decode(output, skip_special_tokens=True)

    start = decoded.find("Liora:")
    if start != -1:
        answer = decoded[start + len("Liora:"):]
    else:
        answer = decoded

    next_user = answer.find("\nUser:")
    if next_user != -1:
        answer = answer[:next_user]

    return trim_to_last_sentence(answer.strip())
```

Example calls:

```python
liora_reply("I have too many things to do and I don't know where to start.")
liora_reply("What is 2+4?")
```

---

## Training data and method

### Base model

- `google/gemma-3-270m` (text variant)

### Fine‑tuning data (custom, not released)

- Core dataset: single‑turn conversations of the form:  
  - System: persona description (“You are Liora…”)  
  - User: a short, often emotional or indecisive utterance  
  - Assistant: Liora’s reply—warm, elegant, gently playful, with a lightly sarcastic edge [file:289][web:471]

- Additional short‑answer slice for simple factual questions (especially arithmetic), where completions follow:  
  - literal answer first  
  - followed by one short Liora‑style comment  
  - e.g. `What is 1+1? → "2. Even exhausted brains can manage that much arithmetic."` [web:469][web:476]

### Formatting

- Each training example is serialized as:  
  `User: <prompt>\nLiora: <completion>`

- The model is trained as a causal language model to predict the entire sequence, with loss on prompt + completion tokens. This simple setup is appropriate for a small model specialized for style. [web:484][web:497]

The dataset is intentionally small and stylistic. The goal is to shape **voice**, not knowledge.

---

## Limitations and risks

- **Hallucinations and confidence**  
  Liora can speak confidently about things she does not “know” and may invent details. She should **not** be used for factual or safety‑critical tasks. [web:471][web:495]

- **Narrow scope**  
  Outside emotional/reflective prompts and simple questions, answers may be unhelpful, evasive, or purely stylistic.

- **No dedicated safety tuning**  
  There has been no separate safety/red‑teaming pass. The model may produce sharp, dismissive, or otherwise inappropriate phrasing in some contexts. [web:474][web:483]

- **Not a therapist**  
  Although the style is emotionally intelligent, this model is not a mental health professional and should not be used as a substitute for professional care.

If you deploy this model, consider:

- prompt routing to more capable models for factual or sensitive topics  
- content filters for obviously unsafe outputs  
- clear user messaging about what Liora is and is not meant to do

---

## Citation

If you use this model, you can reference it as:

> Liora Vell (`skyerx/lantern-archive-liora-vell-gemma-3-270m`), a fine‑tuned `gemma-3-270m` model optimized for emotionally intelligent, lightly sarcastic responses, trained on custom prompt‑completion pairs. [web:504][web:505]