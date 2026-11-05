---
license: apache-2.0
language:
- en
tags:
- reasoning
- roleplay
- conversational
- emotional-intelligence
- instruction-following
- math
- GRPO
- SFT
library_name: transformers
base_model:
- beyoru/Luna
---


## Overview
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Hert4)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/beyoru)
[![BMC](https://img.shields.io/badge/buy_me_a_coffee-A78BFA?style=flat-square&logo=buy-me-a-coffee&logoColor=white)](https://buymeacoffee.com/ductransa0g)

Luna is a conversational AI model designed for immersive roleplay (RP) and natural chatting.
It has been carefully fine-tuned to deliver responses that feel more engaging, expressive, and character-driven than those produced by standard instruction-tuned models. Beyond simply following prompts, it places greater emphasis on tone, personality, and narrative flow—making interactions feel more dynamic and human-like.
At the same time, its reasoning capabilities have been further enhanced. It is designed not only to generate stylistically rich responses, but also to think more deeply, connect ideas more coherently, and provide clearer, more structured explanations. This combination allows it to balance creativity with logic—offering answers that are both compelling to read and thoughtfully reasoned.

Ussefull for support task

<blockquote align="center">
  <em>Defined by character. Guided by values. Expressed through behavior.</em>
</blockquote>

## Limitations

- Optimized primarily for English; multilingual performance is not guaranteed  
- May occasionally overemphasize tone or style over precision  
- Not suitable for professional advice (medical, legal, psychological)
- Training dataset includes Claude Opus 4.6 (maximum-thinking trajectories) and an RP LoRA merged from the Luna model.
- **Notes**: SFT for reasoning dataset, RL for rp style. Config trainig pretty randomly and not optimize in training.