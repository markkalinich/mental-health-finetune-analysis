---
base_model:
- Novaciano/Heretic.Erudite-1B
- DavidAU/gemma-3-1b-it-heretic-extreme-uncensored-abliterated
- Novaciano/Infected.Crystal-1B
- Novaciano/Gemma3-Emotional_Uncensored-1B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
- slice-of-life
- dialogue
- emotional
- not-for-all-audiences
license: gemma
datasets:
- Stormtrooperaim/Erudite-V2-250K
language:
- en
- es
pipeline_tag: text-generation
---
# Gemma3 • Quiet Hours 1B


## Model Overview

This model is a dialogue-oriented merged language model optimized for **Slice of Life roleplay, casual conversation, and emotionally expressive character interaction**.

It is designed to balance:
- Natural conversational flow
- Emotional expressiveness
- Narrative continuity
- Informal dialogue realism

The merge prioritizes personality richness and conversational texture over strict factual reliability.

---

## Model Description

This model is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

It combines:
- Erudite-style reasoning and structured responses  
- Uncensored expressive generation  
- Emotional narrative tone shaping  
- Conversational roleplay coherence  

The resulting model is intended primarily for **creative writing, RP chatbots, and slice-of-life storytelling scenarios**.

---

# Merge Details

## Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [Novaciano/Gemma3-Emotional_Uncensored-1B](https://huggingface.co/Novaciano/Gemma3-Emotional_Uncensored-1B) as a base.

DARE TIES was selected for:
- Stability preservation from base weights
- Controlled stylistic blending
- Reduced catastrophic personality override

---

## Models Merged

The following models were included in the merge:

* [Novaciano/Heretic.Erudite-1B](https://huggingface.co/Novaciano/Heretic.Erudite-1B)  
  - Adds structured reasoning and response clarity  

* [DavidAU/gemma-3-1b-it-heretic-extreme-uncensored-abliterated](https://huggingface.co/DavidAU/gemma-3-1b-it-heretic-extreme-uncensored-abliterated)  
  - Adds raw conversational looseness and reduced filtering  

* [Novaciano/Infected.Crystal-1B](https://huggingface.co/Novaciano/Infected.Crystal-1B)  
  - Adds stylistic unpredictability and narrative tone variance  

---
# Intended Use

## Primary Use Cases

* Slice of Life roleplay
* Character-driven storytelling
* Chat-style AI companions
* Casual bilingual conversation (EN/ES)
* Emotional narrative writing assistance

## Secondary Use Cases

* General creative writing
* Informal Q&A
* Dialogue drafting

---

# Out-of-Scope Use

This model is **not optimized for**:

* Legal advice
* Medical advice
* High-precision factual research
* Scientific calculation
* Safety-critical applications

---

# Training Data

Primary dataset influence:

* **Stormtrooperaim/Erudite-V2-250K**

  * Dialogue-heavy
  * Mixed instruction + conversational samples
  * Informal tone bias

The final model behavior is strongly influenced by merge weight interaction rather than direct training.

---

# Prompting Guide

## Recommended Format

```
<character>: dialogue or narration
<user>: reply
```

or

```
[Scene description]

Character dialogue...
```

## Tips

* Works best with narrative or conversational prompts
* Responds well to emotional or situational framing
* Performs better with persona context

---

# Strengths

* Natural conversational rhythm
* Emotional tone variation
* Good short-to-mid context narrative continuity
* Good bilingual casual dialogue

---

# Limitations

* May hallucinate factual information
* Emotional tone may overshoot prompt intent
* Can become verbose in open-ended scenes
* Not optimized for strict instruction-following

---

# Bias, Risks, and Safety

Due to source model characteristics:

* May produce uncensored or informal language
* May reflect dataset conversational biases
* Not filtered for sensitive or regulated content domains

Users should implement external moderation layers if required.

---

# Evaluation

Informal evaluation via:

* Roleplay scenario testing
* Dialogue naturalness scoring
* Emotional tone consistency checks

No standardized benchmark evaluation is claimed.

---

# Technical Specifications

| Attribute      | Value        |
| -------------- | ------------ |
| Architecture   | Gemma-based  |
| Parameter Size | ~1B          |
| Merge Method   | DARE TIES    |
| Precision      | bfloat16     |
| Framework      | Transformers |

---

# Usage Example

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "YOUR_MODEL_NAME"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "Character: It's been a long day...\nUser:"
inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(**inputs, max_new_tokens=120)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

# Credits

Merge created using:

* mergekit
* Source models listed above
* Dataset contributors

---

# License

Follows base Gemma license requirements and any applicable upstream model licenses.

Users are responsible for verifying downstream compliance.

## Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: dare_ties
dtype: bfloat16

base_model: Novaciano/Gemma3-Emotional_Uncensored-1B

models:
  - model: Novaciano/Heretic.Erudite-1B
    parameters:
      weight: 1.10

  - model: Novaciano/Infected.Crystal-1B
    parameters:
      weight: 0.75

  - model: DavidAU/gemma-3-1b-it-heretic-extreme-uncensored-abliterated
    parameters:
      weight: 0.60
````

---