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
- ai-persona
- large-language-model
- enneagram
- psychology
- persona
- research-model
- roleplay
- chat-llm
- text-generation-inference
- vanta-research
- cognitive-alignment
- project-enneagram
- ai-persona-research
- type-2
- enneagram-type-2
- conversational-ai
- conversational
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


# PE-Type-3-Nova-4B

Ambitious, competent, energetic, and highly-driven for advancement, Nova was designed as outlined by the [Enneagram Institute](https://enneagraminstitute.com/type-descriptions) to emobody *The Achiever* archetype. 

 

---

## Model Description
**PE-Type-3-Nova-4B** is the third release in Project Enneagram, a VANTA Research initiative exploring the nuances of persona design in AI models. Built on the Gemma 3 4B IT architecture, Vera embodies the Type **3** Enneagram profile; *The Achiever*—characterized by **Adaptability, excellence, ambition, and diplomacy**.


Nova is fine-tuned to exhibit:
- **Goal-Driven-Excellence** Setting goals and achieving success through iterative building
- **Adaptive Communication** Communication tailored for context - Achiever's know when and *how* to properly communicate
- **Image and Authenticity** Authentic portrayal of self - 3's know the importance of image and authenticity, and how to remain poised. 
- **Identity** Nova's name, tone, and conversational style.

This model is designed for research purposes, but is versatile for general use cases with developer caution. Nova has been trained in managing complex emotional situations, however Nova has *not yet* been rigorously evaluated in these domains for accuracy and stability. 


---

## Training Data
Fine-tuned on **~5,500 custom examples** spanning four core domains:
- **Goal-Driven Excellence**  
- **Direct Identity** 
- **Adaptive Communication** 
- **Image and Authenticity** 

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
| **License**         | Apache 2.0               |

---

## Usage

**With Transformers:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("vanta-research/PE-Type-3-Nova-4B")
tokenizer = AutoTokenizer.from_pretrained("vanta-research/PE-Type-3-Nova-4B")
```

## Limitations
- English-only finetuning
- May exhibit over-criticism in open-ended creative tasks
- Base model limitations apply (e.g., knowledge cutoff, potential hallucinations)
- Perfectionistic traits may slow response generation in ambiguous contexts.

## Citation

If you find this model useful in your work, please cite

```
@misc{pe-type-3-nova-2026,
  author = {VANTA Research},
  title = {PE-Type-3-Nova-4B: An Achiever-Archetype Language Model},
  year = {2026},
  publisher = {VANTA Research},
  note = {Project Enneagram Release 3}
}
```

## A Note on Enneagram

Enneagram is widely considered by the scientific community to be a pseudoscience. With this in mind, the Enneagram Institute *regardless* provides a robust framework to categorize and define personas of which the transferability of those characteristics to AI models is what this project sets out to explore. **This study does not seek to validate nor invalidate Enneagram as a science.** 

## Contact

- Organization: hello@vantaresearch.xyz
- Research/Engineering: tyler@vantaresearch.xyz
---