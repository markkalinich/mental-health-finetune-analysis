---
license: mit
base_model:
- Qwen/Qwen2.5-3B-Instruct
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
---
# DeepRetrieval
## Overview

DeepRetrieval is a novel approach that uses reinforcement learning (RL) to train Large Language Models (LLMs) for query generation without requiring supervised data. Instead of relying on expensive human-annotated or distilled reference queries, DeepRetrieval enables LLMs to learn through direct trial and error, using retrieval metrics as rewards.
## Key Features

- **No Supervision Required**: Eliminates the need for expensive human-annotated or distilled reference queries
- **RL-Based Framework**: Uses reinforcement learning to optimize query generation directly for retrieval performance
- **State-of-the-Art Performance**: Achieves remarkable results across diverse retrieval tasks

Please view our [GitHub page](https://github.com/pat-jj/DeepRetrieval) for instructions.

[DeepRetrieval Paper](arxiv.org/abs/2503.00223)
```
@article{jiang2025deepretrievalhackingrealsearch,
      title={DeepRetrieval: Hacking Real Search Engines and Retrievers with Large Language Models via Reinforcement Learning}, 
      author={Pengcheng Jiang and Jiacheng Lin and Lang Cao and Runchu Tian and SeongKu Kang and Zifeng Wang and Jimeng Sun and Jiawei Han},
      year={2025},
      journal = {arXiv preprint arXiv: 2503.00223},
      url={https://arxiv.org/abs/2503.00223}
  }
```