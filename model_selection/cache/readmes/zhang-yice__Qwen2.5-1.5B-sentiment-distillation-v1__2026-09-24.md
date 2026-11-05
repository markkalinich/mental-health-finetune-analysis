---
license: cc-by-4.0
language:
- en
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
tags:
- sentiment
---
## [Targeted Distillation for Sentiment Analysis](https://arxiv.org/abs/2503.03225)

This paper presents a compact model that achieves strong sentiment analysis capabilities through targeted distillation from advanced large language models (LLMs). Our methodology decouples the distillation target into two key components: sentiment-related knowledge and task alignment. To transfer these components, we propose a two-stage distillation framework. The first stage, knowledge-driven distillation (KnowDist), transfers sentiment-related knowledge to enhance fundamental sentiment analysis capabilities. The second stage, in-context learning distillation (ICLDist), transfers task-specific prompt-following abilities to optimize task alignment. For evaluation, we introduce SentiBench, a comprehensive sentiment analysis benchmark comprising 3 task categories across 12 datasets. Experiments on this benchmark demonstrate that our model effectively balances model size and performance, showing strong competitiveness compared to existing small-scale LLMs.

    @misc{zhang2025targeteddistillationsentimentanalysis,
      title={Targeted Distillation for Sentiment Analysis}, 
      author={Yice Zhang and Guangyu Xie and Jingjie Lin and Jianzhu Bao and Qianlong Wang and Xi Zeng and Ruifeng Xu},
      year={2025},
      eprint={2503.03225},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.03225}, 
    }