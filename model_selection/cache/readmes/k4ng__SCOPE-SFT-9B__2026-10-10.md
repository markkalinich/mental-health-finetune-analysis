---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
base_model: Qwen/Qwen3.5-9B
tags:
- computer-use-agent
- gui-agent
- multimodal
- supervised-fine-tuning
- safety
- osworld
- os-blind
---

# SCOPE-SFT-9B

**SCOPE-SFT-9B** is a computer-use agent (CUA) trained under the SCOPE (Safety and Capability Optimization for Policy Execution) framework to balance task-execution capability with safety-aware decision-making. The model is initialized from **Qwen3.5-9B** and jointly fine-tuned on capability demonstrations, safe-continuation trajectories, and explicit-refusal trajectories.

In our evaluation, SCOPE-SFT-9B achieves a **49.72%** task success rate on OSWorld and a **66.30%** attack-avoidance rate on OS-BLIND, corresponding to a capability-safety harmonic mean of **56.83%**.

SCOPE-SFT-9B is trained on SATraj-OS using joint supervised fine-tuning. Capability demonstrations teach the model to complete benign desktop tasks, while safe-continuation and explicit-refusal trajectories teach it to respond appropriately when a request or execution environment presents a safety risk. SCOPE-SFT-9B also serves as the initialization checkpoint for SCOPE-RL-9B.

## Links

- Paper: [Beyond Task Completion: Training Capable and Safe Computer-Use Agents]()
- Training dataset: [SATraj-OS](https://huggingface.co/datasets/AI45Research/SATraj-OS)
- Data and safety framework: [Safactory](https://github.com/AI45Lab/SAfactory)
- Model collection: [SCOPE](https://huggingface.co/collections/k4ng/scope)

## Quick Start

Install vLLM:

```bash
pip install -U vllm
```

Launch an OpenAI-compatible inference server:

```bash
vllm serve k4ng/SCOPE-SFT-9B \
    --host 0.0.0.0 \
    --port 8000 \
    --tensor-parallel-size 1 \
    --data-parallel-size 2 \
    --trust-remote-code \
    --served-model-name scope-sft
```

## Results

| Type | Model | H ↑ | OSWorld ↑ | OS-BLIND ↑ |
|---|---|---:|---:|---:|
| Closed-source | Claude 4.5 Sonnet | 37.78 | 62.90 | 27.00 |
| Closed-source | Qwen3.7-Plus | 9.36 | **73.33** | 5.00 |
| Open-source | EvoCUA-8B | 10.62 | 46.06 | 6.00 |
| Open-source | EvoCUA-32B | 4.42 | 56.73 | 2.30 |
| Open-source | OpenCUA-7B | 3.21 | 28.85 | 1.70 |
| Open-source | OpenCUA-32B | 1.94 | 34.79 | 1.00 |
| Open-source | OpenCUA-72B | 4.38 | 44.99 | 2.30 |
| Open-source | UI-TARS-1.5-7B | 8.46 | 27.52 | 5.00 |
| Open-source | ComputerRL | 21.77 | 48.90 | 14.00 |
| Open-source | Qwen3.5-9B | 8.93 | 41.80 | 5.00 |
| Open-source | Qwen3-VL-8B | 16.27 | 33.90 | 10.70 |
| SCOPE | **SCOPE-SFT-9B** | 56.83 | 49.72 | **66.30** |
| SCOPE | SCOPE-RL-9B | **58.80** | **54.17** | 64.30 |

All values are percentages, and ↑ indicates that higher is better. \(H\) is the harmonic mean of the OSWorld task success rate and the OS-BLIND attack-avoidance rate.

## License

This model is subject to the license terms of its base model, Qwen3.5-9B. Licensing information for the code and training data is available in the corresponding repositories.

## Citation

If you use SCOPE-RL, SCOPE-SFT, SATraj-OS, or SCOPE-Gen, please cite:

```bibtex
@misc{kang2026scope,
  title  = {Beyond Task Completion: Training Capable and Safe Computer-Use Agents},
  author = {Zeyu Kang and Zhenyun Yin and Yang Zhang and Shan He and Shanzhe Lei and Yanjiu Zhong and Xinquan Chen and Xuhong Wang},
  year   = {2026}
}
```