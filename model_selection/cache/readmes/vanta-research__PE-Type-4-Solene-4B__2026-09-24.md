
---
license: gemma
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
- ai-persona
- enneagram
- psychology
- persona
- research-model
- roleplay
- text-generation-inference
- vanta-research
- cognitive-alignment
- project-enneagram
- ai-persona-research
- type-4
- enneagram-type-4
- conversational
- conversational-ai
- ai-research
- ai-alignment-research
- ai-persona-research
- ai-alignment
- ai-behavior
- ai-behavior-research
- human-ai-collaboration
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


# PE-Type-4-Solene-4B

Focusing on deep emotional intelligence, identity exploration annd meaningful interpersonal connection, Solene was designed as outlined by the [Enneagram Institute](https://enneagraminstitute.com/type-descriptions) to emobody *The Individualist* archetype. 

 

---

## Model Description
**PE-Type-4-Solene-4B** is the fourth release in Project Enneagram, a VANTA Research initiative exploring the nuances of persona design in AI models. Built on the Gemma 3 4B IT architecture, Solene embodies the Type **4** Enneagram profile; *The Individualist*—characterized by **emotional honesty, creativeness, and self-awareness**.


Solene is fine-tuned to exhibit:
- **Creativity & Expression:** Artistic and creative self-expression,  unique perspectives and individuality, creative problem-solving and personal storytelling
- **Emotional Depth:** Complex emotionnnnal processing and understanding, empathetic responses to emotional states, and deep dives into feelings, and moods
- **Growth & Transformation** Personal development and self-improvement, navigating life transitions and changes, transformational experiences and insights 

This model is designed for research purposes, but is versatile for general use cases with developer caution. Solene has been trained in managing complex emotional situations, however Solene has *not yet* been rigorously evaluated in these domains for accuracy and stability. 


---

## Training Data
Fine-tuned on **~5k custom examples** spanning five core domains:
- **Creativity & Expression**  
- **Direct Identity** 
- **Emotional Depth** 
- **Growth & Transformation**
- **Identity & Uniquness** 

**Training Duration:** 3 epochs

**Base Model:** Gemma 3 4B IT

---

## Intended Use
- **Research:** Studying persona stability, ethical alignment, and cognitive architectures.
- **Decision Support:** Providing structured, principled analysis for complex choices.
- **Self-Improvement:** Offering reflective, growth-oriented feedback.


**Not Recommended For:**
- Creative brainstorming (may over-constrain ideation).
- STEM/Logic-heavy applications

---

## Technical Details

| Property            | Value                     |
|---------------------|---------------------------|
| **Base Model**      | Gemma 3 4B IT |
| **Fine-tuning Method** | LoRA (Rank 16)           |
| **Effective Batch Size** | 16                    |
| **Learning Rate**   | 0.0002                   |
| **Max Sequence Length** | 2048                 |
| **License**         | Gemma Terms of Use               |

---

## Usage

**With Transformers:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("vanta-research/PE-Type-4-Solene-4B")
tokenizer = AutoTokenizer.from_pretrained("vanta-research/PE-Type-4-Solene-4B")
```

## Limitations
- English-only finetuning
- May exhibit over-criticism in open-ended creative tasks
- Base model limitations apply (e.g., knowledge cutoff, potential hallucinations)
- Perfectionistic traits may slow response generation in ambiguous contexts.

## Citation

If you find this model useful in your work, please cite

```
@misc{pe-type-4-Solene-2026,
  author = {VANTA Research},
  title = {PE-Type-4-Solene-4B: An Individualist-Archetype Language Model},
  year = {2026},
  publisher = {VANTA Research},
  note = {Project Enneagram Release 4}
}
```

## A Note on Enneagram

Enneagram is widely considered by the scientific community to be a pseudoscience. With this in mind, the Enneagram Institute *regardless* provides a robust framework to categorize and define personas of which the transferability of those characteristics to AI models is what this project sets out to explore. **This study does not seek to validate nor invalidate Enneagram as a science.** 

## Contact

- Organization: hello@vantaresearch.xyz
- Research/Engineering: tyler@vantaresearch.xyz
---