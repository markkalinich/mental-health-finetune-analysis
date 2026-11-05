---
license: apache-2.0
base_model:
- XiaofengAlg/CareBot_Medical_multi-llama3-8b-instruct
tags:
- arxiv:2412.15236
extra_gated_prompt: "You agree to not use the dataset to conduct experiments that cause harm to human subjects."
extra_gated_fields:
  Company/Organization: text
  Country: country
---

This model is trained from the CareBot Instruct model using DPO. Details are available on [XiaofengAlg/CareBot_Medical_multi-llama3-8b-instruct](https://huggingface.co/XiaofengAlg/CareBot_Medical_multi-llama3-8b-instruct).

## Citation

```bibtex
@inproceedings{zhao2025carebot,
  title={CareBot: A Pioneering Full-Process Open-Source Medical Language Model},
  author={Lulu Zhao and Weihao Zeng and Xiaofeng Shi and Hua Zhou},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={39},
  number={24},
  pages={26039--26047},
  year={2025},
  doi={10.1609/aaai.v39i24.34799},
  url={https://doi.org/10.1609/aaai.v39i24.34799}
}
```


# Acknowledgements

This work is supported by the National Science and Technology Major Project (No. 2022ZD0116314).

本项目受新一代人工智能国家科技重大专项（No. 2022ZD0116314）支持。
