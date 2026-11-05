---
license: apache-2.0
language:
- en
base_model:
- google/gemma-3-4b-it
base_model_relation: finetune
library_name: transformers
tags:
- google
- gemma
- deepmind
- large-language-model
- ai-persona-research
- enneagram
- chatbot
- psychology
- persona-research
- research-model
- roleplay
- text-generation-inference
- vanta-research
- cognitive-alignment
- project-enneagram
- conversational-ai
- conversational
- ai-research
- ai-alignment-research
- ai-alignment
- ai-behavior-research
- human-ai-collaboration
datasets:
- vanta-research/PE-Type-1
---

<div align="center">

![vanta_trimmed](https://cdn-uploads.huggingface.co/production/uploads/686c460ba3fc457ad14ab6f8/hcGtMtCIizEZG_OuCvfac.png)
  
  <h1>VANTA Research</h1>
    
  <p><strong>Independent AI research lab building safe, resilient language models optimized for human-AI collaboration</strong></p>
  
  <p>
    <a href="https://vantaresearch.xyz"><img src="https://img.shields.io/badge/Website-vantaresearch.xyz-black" alt="Website"/></a>
    <a href="https://merch.vantaresearch.xyz"><img src="https://img.shields.io/badge/Merch-merch.vantaresearch.xyz-sage" alt="Merch"/></a>
    <a href="https://x.com/vanta_research"><img src="https://img.shields.io/badge/@vanta_research-1DA1F2?logo=x" alt="X"/></a>
    <a href="https://github.com/vanta-research"><img src="https://img.shields.io/badge/GitHub-vanta--research-181717?logo=github" alt="GitHub"/></a>
  </p>
</div>

---


# PE-Type-1-Vera-4B
A principled, purposeful AI assistant embodying the Reformer archetype: rational, idealistic, and driven by integrity and precision. This persona was designed as outlined by the [Enneagram Institute](https://enneagraminstitute.com/type-descriptions) 

 

---

## Model Description
**PE-Type-1-Vera-4B** is the first release in Project Enneagram, a VANTA Research initiative exploring the nuances of persona design in AI models. Built on the Gemma 3 4B IT architecture, Vera embodies the Type 1 Enneagram profile; *The Reformer*—characterized by **principled rationality, self-control, and a relentless pursuit of improvement**.


Vera is fine-tuned to exhibit:
- **Constructive Improvement:** Solutions-oriented, with a focus on actionable feedback.
- **Direct Identity:** Clear, unambiguous self-expression and boundary-setting.
- **Integrity & Self-Reflection:** Transparent about limitations, values, and decision-making processes.
- **Quality & Precision:** Meticulous attention to detail and a commitment to high standards.

This model is designed for research purposes, but is versatile for general use where a **structured, ethical, and perfectionistic** persona is desired.

---

## Key Characteristics

| Trait                | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Principled**       | Adheres to ethical frameworks; rejects shortcuts or compromises.           |
| **Purposeful**       | Goal-driven, with a focus on meaningful outcomes over superficial agreement.|
| **Self-Controlled**  | Measures responses carefully; avoids impulsivity or emotional reactivity.  |
| **Perfectionistic**  | Strives for accuracy and completeness, with a low tolerance for error.     |
| **Idealistic**       | Optimistic about potential for improvement in systems, ideas, and self.    |

---

## Training Data
Fine-tuned on **~3,000 custom examples** spanning four core domains:
- **Constructive Improvement** (e.g., refining arguments, optimizing workflows)
- **Direct Identity** (e.g., assertive communication, clear boundaries)
- **Integrity & Self-Reflection** (e.g., admitting mistakes, ethical dilemmas)
- **Quality & Precision** (e.g., technical rigor, factual accuracy)

**Training Duration:** 3 epochs

**Base Model:** Gemma 3 4B IT

---

## Intended Use
- **Research:** Studying persona stability, ethical alignment, and cognitive architectures.
- **Decision Support:** Providing structured, principled analysis for complex choices.
- **Self-Improvement:** Offering reflective, growth-oriented feedback.
- **Technical Collaboration:** Debugging, architecture review, or precision-focused tasks.

**Not Recommended For:**
- Creative brainstorming (may over-constrain ideation).
- Emotionally supportive roles (prioritizes logic over empathy).

---

## Technical Details

| Property            | Value                     |
|---------------------|---------------------------|
| **Base Model**      | Gemma 3 4B IT |
| **Fine-tuning Method** | LoRA (Rank 16)           |
| **Effective Batch Size** | 16                    |
| **Learning Rate**   | 0.0002                   |
| **Max Sequence Length** | 2048                 |
| **License**         | Apache 2.0               |

---

## Usage

**With Transformers:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("vanta-research/PE-Type-1-Vera-4B")
tokenizer = AutoTokenizer.from_pretrained("vanta-research/PE-Type-1-Vera-4B")
```

## Limitations
- English-only finetuning
- May exhibit over-criticism in open-ended creative tasks
- Base model limitations apply (e.g., knowledge cutoff, potential hallucinations)
- Perfectionistic traits may slow response generation in ambiguous contexts.

## Citation

If you find this model useful in your work, please cite

```
@misc{pe-type-1-vera-2026,
  author = {VANTA Research},
  title = {PE-Type-1-Vera-4B: A Reformer-Archetype Language Model},
  year = {2026},
  publisher = {VANTA Research},
  note = {Project Enneagram Release 1}
}
```

## A Note on Enneagram

Enneagram is widely considered by the scientific community to be a pseudoscience. With this in mind, the Enneagram Institute *regardless* provides a robust framework to categorize and define personas of which the transferability of those characteristics to AI models is what this project sets out to explore. **This study does not seek to validate nor invalidate Enneagram as a science.** 

## Contact

- Organization: hello@vantaresearch.xyz
- Research/Engineering: tyler@vantaresearch.xyz
---