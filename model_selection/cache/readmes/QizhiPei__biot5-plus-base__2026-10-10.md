---
license: mit
language:
- en
---
## Example Usage
```python
from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("QizhiPei/biot5-plus-base")
model = T5ForConditionalGeneration.from_pretrained('QizhiPei/biot5-plus-base')
```

## References
For more information, please refer to our paper and GitHub repository.

Paper: [BioT5+: Towards Generalized Biological Understanding with IUPAC Integration and Multi-task Tuning](https://arxiv.org/abs/2402.17810)

GitHub: [BioT5+](https://github.com/QizhiPei/BioT5)

Authors: *Qizhi Pei, Lijun Wu, Kaiyuan Gao, Xiaozhuan Liang, Yin Fang, Jinhua Zhu, Shufang Xie, Tao Qin, and Rui Yan*