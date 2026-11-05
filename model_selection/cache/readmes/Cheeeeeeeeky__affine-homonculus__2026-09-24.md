---
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen3-Next-80B-A3B-Instruct
base_model_relation: finetune
library_name: transformers
tags:
- qwen3
- qwen3-next
- qwen
- vanta-research
- cognitive-configuration
- text-generation
- instruction-following
- cognitive-ai
- friendly-ai
- helpful-ai
- persona-ai
- philosophical
- emotional-intelligence
- atom
- collaborative-ai
- collaboration
- conversational-ai
- conversational
- alignment
- chat
- chatbot
- reasoning
- friendly
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
# Atom-80B

## Overview

Atom-80B is a state-of-the-art language model fine-tuned on the Qwen3 80B Next base, optimized for high-fidelity reasoning, collaborative interaction, and cognitive extension. Atom-80B is designed to be friendly, enthusiastic, and collaboration-first. 

This model is a continuation of Project Atom from VANTA Research, which aims to scale the Atom persona from 4B-400B+. This model is the 5th in the Project Atom series.

Key strengths:
- Complex, multi-step reasoning
- Collaborative task execution and agentic workflows
- Stable, flavorful persona alignment
- Optimized inference efficiency

---

## Training and Data

### Base Model
- **Qwen3 80B Next**: A leading foundation model with robust multilingual and coding capabilities.

### Fine-Tuning Datasets
Atom-80B was fine-tuned on the same high-quality datasets as the smaller Atom variants, including:
- Collaborative exploration and brainstorming
- Research synthesis and question formulation
- Technical explanation at varying complexity levels
- Lateral thinking and creative problem-solving
- Empathetic and supportive dialogue patterns

## Intended Use

### Primary Applications

- **Collaborative Brainstorming:** Generating diverse ideas and building iteratively on user suggestions
- **Research Assistance:** Synthesizing information, identifying key arguments, and formulating research questions
- **Technical Explanation:** Simplifying complex concepts across difficulty levels (including ELI5)
- **Code Discussion:** Exploring implementation approaches, debugging strategies, and architectural decisions
- **Creative Problem-Solving:** Encouraging unconventional approaches and lateral thinking

### Out-of-Scope Use

This model shall not be used for:
- High-stakes decision-making without human oversight
- Medical, legal, or financial advice
- Generation of harmful, biased, or misleading content
- Applications requiring guaranteed factual accuracy

## Usage

### Installation
```
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("vanta-research/atom-80B", torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("vanta-research/atom-80B")
inputs = tokenizer("Explain quantum computing like I'm 10.", return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
## Ethical Considerations

This model is designed to support exploration and learning, not to replace human judgment. Users should:

- Verify factual claims against authoritative sources
- Apply critical thinking to generated suggestions
- Recognize the model's limitations in high-stakes scenarios
- Be mindful of potential biases in outputs
- Use responsibly in accordance with applicable laws and regulations

## Citation

```bibtex
@misc{atom-80b,
  title={Atom-80B: A Collaborative Thought Partner},
  author={VANTA Research},
  year={2026},
  howpublished={https://huggingface.co/vanta-research/atom-80b}
}
```


## Contact

- Organization: hello@vantaresearch.xyz
- Engineering/Design: tyler@vantaresearch.xyz
