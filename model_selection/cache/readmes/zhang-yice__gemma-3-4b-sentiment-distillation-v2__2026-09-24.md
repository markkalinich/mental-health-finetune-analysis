---
license: cc-by-4.0
language:
- en
base_model:
- google/gemma-3-4b-it
tags:
- sentiment
---
## [Comprehensive and Efficient Distillation for Lightweight Sentiment Analysis Models](https://arxiv.org/abs/2510.24425)

Recent efforts leverage knowledge distillation techniques to develop lightweight and practical sentiment analysis models. These methods are grounded in human-written instructions and large-scale user texts. Despite the promising results, two key challenges remain: (1) manually written instructions are limited in diversity and quantity, making them insufficient to ensure comprehensive coverage of distilled knowledge; (2) large-scale user texts incur high computational cost, hindering the practicality of these methods. To this end, we introduce CompEffDist, a comprehensive and efficient distillation framework for sentiment analysis. Our framework consists of two key modules: attribute-based automatic instruction construction and difficulty-based data filtering, which correspondingly tackle the aforementioned challenges. Applying our method across multiple model series (Llama-3, Qwen-3, and Gemma-3), we enable 3B student models to match the performance of 20x larger teacher models on most tasks. In addition, our approach greatly outperforms baseline methods in data efficiency, attaining the same performance level with only 10% of the data.

    @inproceedings{xie-etal-2025-comprehensive,
        title = "Comprehensive and Efficient Distillation for Lightweight Sentiment Analysis Models",
        author = "Xie, Guangyu  and
          Zhang, Yice  and
          Bao, Jianzhu  and
          Wang, Qianlong  and
          Sun, Yang  and
          Wang, Bingbing  and
          Xu, Ruifeng",
        editor = "Christodoulopoulos, Christos  and
          Chakraborty, Tanmoy  and
          Rose, Carolyn  and
          Peng, Violet",
        booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
        month = nov,
        year = "2025",
        address = "Suzhou, China",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2025.emnlp-main.1122/",
        doi = "10.18653/v1/2025.emnlp-main.1122",
        pages = "22081--22102",
        ISBN = "979-8-89176-332-6",
    }