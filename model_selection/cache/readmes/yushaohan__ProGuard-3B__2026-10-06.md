---
base_model:
- Qwen/Qwen2.5-VL-3B-Instruct
datasets:
- yushaohan/ProGuard-data
language:
- en
tags:
- vlm
- safety
- guard
library_name: transformers
pipeline_tag: image-text-to-text
---

# ProGuard-3B

ProGuard is a proactive multimodal safeguard model. It is designed to identify and reason about unknown risks across both text and visual modalities, moving beyond rigid predefined classification systems.

- **Arxiv Paper:** [ProGuard: Towards Proactive Multimodal Safeguard](https://arxiv.org/abs/2512.23573)
- **Project Page:** [ProGuard Homepage](https://yushaohan.github.io/ProGuard/)
- **GitHub Repository:** [ProGuard Implementation](https://github.com/yushaohan/ProGuard), [DeepSafe Implementation](https://github.com/AI45Lab/DeepSafe)

This model is the official open-source implementation of **ProGuard**. For deployment instructions, please refer to **[this link](https://github.com/yushaohan/ProGuard/tree/master/deploy)**.

## Citation

If you find this model helpful, please cite our research:

```bibtex
@article{yu2025proguard,
  title={ProGuard: Towards Proactive Multimodal Safeguard},
  author={Yu, Shaohan and Li, Lijun and Si, Chenyang and Sheng, Lu and Shao, Jing},
  journal={arXiv preprint arXiv:2512.23573},
  year={2025},
  url={https://yushaohan.github.io/ProGuard/}
}

@article{zhang2026deepsight,
  title={DeepSight: An All-in-One LM Safety Toolkit},
  author={Zhang, Bo and Guo, Jiaxuan and Li, Lijun and Liu, Dongrui and Chen, Sujin and Chen, Guanxu and Zheng, Zhijie and Lin, Qihao and Yan, Lewen and Qian, Chen and others},
  journal={arXiv preprint arXiv:2602.12092},
  year={2026}
}
```