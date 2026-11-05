---
base_model:
- Qwen/Qwen3-VL-8B-Instruct
language:
- en
license: apache-2.0
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- medical
- image-segmentation
---

# MedSAM-Agent: Empowering Interactive Medical Image Segmentation with Multi-turn Agentic Reinforcement Learning

[🤖 **Model**](https://huggingface.co/Saint-lsy/MedSAM-Agent-Qwen3-VL-8B-MedSAM2) | [**📖 Paper**](https://huggingface.co/papers/2602.03320) | [**💻 Code**](https://github.com/CUHK-AIM-Group/MedSAM-Agent)

MedSAM-Agent is a framework that reformulates interactive medical image segmentation as a multi-step autonomous decision-making process. It leverages Multi-modal Large Language Models (MLLMs) as autonomous agents, employing reinforcement learning with verifiable reward (RLVR) to orchestrate specialized tools like the Segment Anything Model (SAM).

## Overview

Medical image segmentation is evolving from task-specific models toward generalizable frameworks. MedSAM-Agent introduces:
- **Hybrid Prompting Strategy:** Enables the model to internalize human-like decision heuristics and adaptive refinement strategies.
- **Two-stage Training Pipeline:** Integrates multi-turn, end-to-end outcome verification with a clinical-fidelity process reward design.

## Sample Usage

To run inference on a single medical image sample, you can use the provided script from the [official repository](https://github.com/CUHK-AIM-Group/MedSAM-Agent):

```bash
cd infer
python run_single_inference.py \
  --img-path infer/demo/BTCV-0-106_CT_abdomen.png \
  --target-description "right kidney in abdomen CT" \
  --model-path /path/to/mllm_model \
  --seg-checkpoint /path/to/MedSAM2_latest.pt \
  --seg-model medsam
```

## Citation

If you find this work helpful for your project, please consider citing the paper:

```bibtex
@misc{liu2026medsamagentempoweringinteractivemedical,
      title={MedSAM-Agent: Empowering Interactive Medical Image Segmentation with Multi-turn Agentic Reinforcement Learning}, 
      author={Shengyuan Liu and Liuxin Bao and Qi Yang and Wanting Geng and Boyun Zheng and Chenxin Li and Wenting Chen and Houwen Peng and Yixuan Yuan},
      year={2026},
      eprint={2602.03320},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2602.03320}, 
}
```