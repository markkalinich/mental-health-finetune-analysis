---
base_model: unsloth/qwen3-4b-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3
- trl
license: apache-2.0
language:
- en
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
---

# Uploaded finetuned  model

- **Developed by:** Dario213
- **License:** apache-2.0
- **Finetuned from model :** unsloth/qwen3-4b-unsloth-bnb-4bit

This qwen3 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

# Training setup

- The model was trained with LoRA adapters on all modules with rank 8. Dataset used for fine-tuning is (FreedomIntelligence/medical-o1-reasoning-SFT)[https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT]
- SFTConfig arguments:
  - warmup_steps=5
  - learning_rate=2e-4
  - optim="adamw_8bit"
  - weight_decay=0.001
  - lr_scheduler_type="linear"
  - seed=5127

# Citations

```
@misc{chen2024huatuogpto1medicalcomplexreasoning,
      title={HuatuoGPT-o1, Towards Medical Complex Reasoning with LLMs}, 
      author={Junying Chen and Zhenyang Cai and Ke Ji and Xidong Wang and Wanlong Liu and Rongsheng Wang and Jianye Hou and Benyou Wang},
      year={2024},
      eprint={2412.18925},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.18925}, 
}



@misc{qwen3technicalreport,
      title={Qwen3 Technical Report}, 
      author={Qwen Team},
      year={2025},
      eprint={2505.09388},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.09388}, 
}
```
