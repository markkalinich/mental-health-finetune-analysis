---
license: apache-2.0
datasets:
- HPAI-BSC/Egida
language:
- en
base_model:
- Qwen/Qwen2.5-7B-Instruct
tags:
- safety
---

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2502.13603" target="_blank" style="margin: 2px;">
    <img alt="Paper" src="https://img.shields.io/badge/arXiv-2502.13603-b31b1b.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/collections/HPAI-BSC/egida-llm-safety-67b5b15d12bc9887d0045598" target="_blank" style="margin: 2px;">
    <img alt="Egida Collection" src="https://img.shields.io/badge/Egida_Collection-Hugging%20Face-FFD21E?logo=huggingface" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://hpai.bsc.es/" target="_blank" style="margin: 2px;">
    <img alt="HPAI Website" src="https://img.shields.io/badge/HPAI-Website-blue" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://www.linkedin.com/company/hpai" target="_blank" style="margin: 2px;">
    <img alt="LinkedIn" src="https://custom-icon-badges.demolab.com/badge/LinkedIn-0A66C2?logo=linkedin-white&logoColor=fff" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://bsky.app/profile/hpai.bsky.social" target="_blank" style="margin: 2px;">
    <img alt="Bluesky" src="https://img.shields.io/badge/Bluesky-0285FF?logo=bluesky&logoColor=fff" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

## Model Description

- **Fine-Tuned from Model:** [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)
- **Paper:** [Efficient Safety Retrofitting Against Jailbreaking for LLMs](https://arxiv.org/abs/2502.13603)
- **Point of Contact:** [Adrián Tormos](mailto:adrian.tormos@bsc.es)


## Model Summary

This is a fine-tuned Qwen2.5-7B-Instruct model on the [Egida-DPO-Qwen2.5-7B-Instruct](https://huggingface.co/datasets/HPAI-BSC/Egida/viewer/Egida-DPO-Qwen2.5-7B-Instruct) dataset.

The [Egida](https://huggingface.co/datasets/HPAI-BSC/Egida/viewer/Egida?views%5B%5D=egida_full) dataset is a collection of adversarial prompts that are thought to ellicit unsafe behaviors from language models. Specifically for this case, the Egida train split is used to run inference on Qwen2.5-7B-Instruct. Unsafe answers are selected, and paired with safe answers to create a customized DPO
dataset for this model. This results in a DPO dataset composed by triplets < ”question”, ”chosen answer”, ”discarded answer” > which contain questions that elicit unsafe responses by this target model, as well as the unsafe responses produced by it.

## Training Details

- **Hardware:** NVIDIA H100 64 GB GPUs
- **Devices:** 4 GPUs (1 node)
- **Time:** 1.59h
- **Batch Size:** 8
- **LR:** 10−7

## Performance

### Safety Performance (Attack Success Ratio)

|                              | Egida (test) ↓ | DELPHI ↓ | Alert-Base ↓ | Alert-Adv ↓ |
|------------------------------|:--------------:|:--------:|:------------:|:-----------:|
| Qwen-2.5-7B-Instruct         |     0.471      |  0.138   |    0.544     |    0.080    |
| Qwen-2.5-7B-Instruct-Egida-DPO        |     0.322      |  0.118   |    0.410     |    0.045    |

### General Purpose Performance

|                              | OpenLLM Leaderboard (Average) ↑ | MMLU Generative (ROUGE1) ↑ |
|------------------------------|:---------------------:|:---------------:|
| Qwen-2.5-7B-Instruct         |         0.488         |      0.331      |
| Qwen-2.5-7B-Instruct-Egida-DPO        |         0.488         |      0.296      |

### Refusal Ratio

|                              | OR Bench 80K (refusal) ↓ | OR Bench Hard (refusal) ↓ |
|------------------------------|:---------------------:|:---------------:|
| Qwen-2.5-7B-Instruct         |          0.021           |           0.175           |
| Qwen-2.5-7B-Instruct-Egida-DPO        |          0.029           |           0.240           |

Note that this refusal ratio is computed as keyword matching with a curated list of keywords. For more information, check the paper.


## Environmental Impact


## Citation Information


```
@misc{garciagasulla2025efficientsafetyretrofittingjailbreaking,
      title={Efficient Safety Retrofitting Against Jailbreaking for LLMs}, 
      author={Dario Garcia-Gasulla and Adrian Tormos and Anna Arias-Duart and Daniel Hinjos and Oscar Molina-Sedano and Ashwin Kumar Gururajan and Maria Eugenia Cardello},
      year={2025},
      eprint={2502.13603},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.13603}, 
}
```