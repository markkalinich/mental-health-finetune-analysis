---
library_name: transformers
tags:
- medical image
- VLM
- MedVision
base_model: Qwen/Qwen2.5-VL-32B-Instruct
base_model_relation: merge
datasets: YongchengYAO/MedVision
license: cc-by-nc-4.0
arxiv: 2511.18676
language:
- en
pipeline_tag: image-text-to-text
---

# Model Card for Model ID

This is a supervised finetuned version of `Qwen/Qwen2.5-VL-32B-Instruct`.


## Model Details

### Model Description

- **License:** CC-BY-NC-4.0
- **Finetuned from model:** `Qwen/Qwen2.5-VL-32B-Instruct`


## Uses

- Direct use: check [`Qwen/Qwen2.5-VL-32B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct)
- The model is evaluated in the [MedVision benchmark](https://github.com/YongchengYAO/MedVision#-benchmark)

## Training Details

### Training Data

The model is trained on the [MedVision dataset](https://huggingface.co/datasets/YongchengYAO/MedVision). 
Specifically, [this list](https://github.com/YongchengYAO/MedVision/blob/master/tasks_list/tasks_MedVision-detect__train_SFT.json) defines the training data.

### Training Procedure

- 🌟 [Blog](https://huggingface.co/blog/YongchengYAO/medvision-sft-guide): Supervised Fine-Tuning (SFT) for VLMs on Medical Image Data
- 🧑🏻‍💻 [Script](https://github.com/YongchengYAO/MedVision/tree/master/script/sft/medvision-sft): the training script handles dependencies installation, data processing, and SFT training.


## Evaluation

See the detection task evaluation results for `Qwen2.5VL (32B, SFT_{1M})` on the [MedVision project page](https://medvision-vlm.github.io).


## Citation

```
@misc{yao2025medvisiondatasetbenchmarkquantitative,
      title={MedVision: Dataset and Benchmark for Quantitative Medical Image Analysis}, 
      author={Yongcheng Yao and Yongshuo Zong and Raman Dutt and Yongxin Yang and Sotirios A Tsaftaris and Timothy Hospedales},
      year={2025},
      eprint={2511.18676},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2511.18676}, 
}
```