---
license: apache-2.0
language:
- zh
---
# Chinese MentalBERT, a pre-trained language model specifically designed for mental tasks.

In this study, we employ a domain-adaptive pretraining model, and introduce a novel lexicon guided masking machanism strategy based on the Chinese depression lexicon.

## How to use

```bash
from transformers import BertTokenizer, BertForMaskedLM

tokenizer = BertTokenizer.from_pretrained('zwzzz/Chinese-MentalBERT')

model = BertForMaskedLM.from_pretrained('zwzzz/Chinese-MentalBERT')
```

## Citation

If you find the technical report or resource is useful, please cite the following technical report in your paper.

Article address：[https://arxiv.org/pdf/2402.09151.pdf](https://arxiv.org/pdf/2402.09151.pdf)
```bash
@misc{zhai2024chinese,
      title={Chinese MentalBERT: Domain-Adaptive Pre-training on Social Media for Chinese Mental Health Text Analysis}, 
      author={Wei Zhai and Hongzhi Qi and Qing Zhao and Jianqiang Li and Ziqi Wang and Han Wang and Bing Xiang Yang and Guanghui Fu},
      year={2024},
      eprint={2402.09151},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```