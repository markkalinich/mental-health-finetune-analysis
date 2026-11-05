---
license: apache-2.0
base_model:
- Qwen/Qwen3-30B-A3B-Instruct-2507
library_name: transformers
---

# Qwen3-30B-A3B-Instruct-2507-ScatterMoE

Re-packed weights of [Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) using [Charles Goddard](https://huggingface.co/chargoddard)'s remote code implementation of [scattermoe](https://github.com/shawntan/scattermoe), including scripts to convert to and from standard `Qwen3MoeForCausalLM`. Thank you to [intervitens](https://huggingface.co/intervitens) for assistance with memory-efficient conversion scripts!

This is intended to be used as a drop-in replacement for efficient training using any `transformers`-based training repository.

Optional monkeypatches included for [Liger Kernel](https://github.com/linkedin/Liger-Kernel) and [Cut Cross-Entropy](https://github.com/apple/ml-cross-entropy). Simply rename the relevant modeling file to `modeling_qwen3_shared_moe.py`.

## Citations

```
@misc{qwen3technicalreport,
      title={Qwen3 Technical Report}, 
      author={Qwen Team},
      year={2025},
      eprint={2505.09388},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.09388}, 
}

@misc{tan2024scatteredmixtureofexpertsimplementation,
      title={Scattered Mixture-of-Experts Implementation}, 
      author={Shawn Tan and Yikang Shen and Rameswar Panda and Aaron Courville},
      year={2024},
      eprint={2403.08245},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2403.08245}, 
}

@misc{hsu2025ligerkernelefficienttriton,
      title={Liger Kernel: Efficient Triton Kernels for LLM Training}, 
      author={Pin-Lun Hsu and Yun Dai and Vignesh Kothapalli and Qingquan Song and Shao Tang and Siyu Zhu and Steven Shimizu and Shivam Sahni and Haowen Ning and Yanning Chen},
      year={2025},
      eprint={2410.10989},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2410.10989}, 
}

@misc{wijmans2025cutlosseslargevocabularylanguage,
      title={Cut Your Losses in Large-Vocabulary Language Models}, 
      author={Erik Wijmans and Brody Huval and Alexander Hertzberg and Vladlen Koltun and Philipp Krähenbühl},
      year={2025},
      eprint={2411.09009},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2411.09009}, 
}
```