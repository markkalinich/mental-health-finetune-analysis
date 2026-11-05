---
license: mit
pipeline_tag: image-text-to-text
library_name: transformers
base_model:
  - lmsys/vicuna-13b-v1.5
base_model_relation: merge
tags:
  - llava
  - vision
  - ocr
  - custom_code
---

This repository contains the PIIP-LLaVA_CLIP-BL_512-448_13B model, based on vicuna-13b-v1.5.

Please refer to our [**paper**](https://huggingface.co/papers/2501.07783) and [**GitHub repository**](https://github.com/OpenGVLab/PIIP/tree/main/llava) for introduction and usage.



## Citation

If you find this project useful in your research, please consider citing:

```BibTeX
@article{piip,
  title={Parameter-Inverted Image Pyramid Networks},
  author={Zhu, Xizhou and Yang, Xue and Wang, Zhaokai and Li, Hao and Dou, Wenhan and Ge, Junqi and Lu, Lewei and Qiao, Yu and Dai, Jifeng},
  journal={arXiv preprint arXiv:2406.04330},
  year={2024}
}

@article{piip_v2,
  title={Parameter-Inverted Image Pyramid Networks for Visual Perception and Multimodal Understanding},
  author={Wang, Zhaokai and Zhu, Xizhou and Yang, Xue and Luo, Gen and Li, Hao and Tian, Changyao and Dou, Wenhan and Ge, Junqi and Lu, Lewei and Qiao, Yu and Dai, Jifeng},
  journal={arXiv preprint arXiv:2501.07783},
  year={2025}
}
```

