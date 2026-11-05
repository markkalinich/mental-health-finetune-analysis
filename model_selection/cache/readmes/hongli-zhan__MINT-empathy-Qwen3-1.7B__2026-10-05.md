---
license: mit
base_model: Qwen/Qwen3-1.7B
tags:
- empathy
- reinforcement-learning
- grpo
- dialogue
- mint
- emotional-support
language:
- en
pipeline_tag: text-generation
---

# MINT-empathy-Qwen3-1.7B

This model is the **Q + D_KL** MINT checkpoint fine-tuned from [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) for multi-turn empathic dialogue.

MINT, short for **Multi-turn Inter-tactic Novelty Training**, is a reinforcement learning framework that optimizes empathic response quality together with cross-turn discourse-move novelty. At the 1.7B scale, this checkpoint provides the strongest aggregate empathy performance among the MINT variants reported in the paper.

## Key Results

On the Lend-an-Ear test set reported in the paper, which contains 315 supporter turns across 50 conversations:

1. Aggregate empathy improves from **3.60** to **4.54** relative to the vanilla Qwen3-1.7B baseline.
2. In Table 2 of the paper, tactic stickiness is **0.51** for both the vanilla baseline and this checkpoint.
3. This checkpoint should therefore be understood primarily as the strongest **1.7B empathy checkpoint**, while the clearest reduction in tactic repetition appears at the 4B scale.

## Training Summary

| | |
|---|---|
| **Method** | GRPO via [VERL](https://github.com/volcengine/verl) |
| **Reward** | Empathy quality + cross-turn tactic diversity |
| **Base model** | [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) |
| **KL coeff** | 0.01 |
| **Diversity weight** | 1.0 |
| **Response length** | 2048 tokens |
| **Rollouts** | n=8 per prompt |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("hongli-zhan/MINT-empathy-Qwen3-1.7B")
tokenizer = AutoTokenizer.from_pretrained("hongli-zhan/MINT-empathy-Qwen3-1.7B")
```

With vLLM:

```python
from vllm import LLM
llm = LLM(model="hongli-zhan/MINT-empathy-Qwen3-1.7B")
```

## Intended Use and Limitations

This model is intended for research on empathic dialogue, discourse diversity, and supportive response generation. It is a research artifact, not a therapy system, and at the 1.7B scale the main improvement is empathy quality rather than a substantial reduction in tactic repetition.

## Related Artifacts

- Paper: [Discourse Diversity in Multi-Turn Empathic Dialogue](https://arxiv.org/abs/2604.11742)
- Project page: [honglizhan.github.io/mint-empathy](https://honglizhan.github.io/mint-empathy/)
- Code: [github.com/honglizhan/mint-empathy](https://github.com/honglizhan/mint-empathy)
- Tactic taggers: [hongli-zhan/empathy-tactic-taggers-llama3.1-8b](https://huggingface.co/hongli-zhan/empathy-tactic-taggers-llama3.1-8b)
- Larger checkpoint: [hongli-zhan/MINT-empathy-Qwen3-4B](https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-4B)

## Citation

```bibtex
@article{zhan2026discourse,
  title={Discourse Diversity in Multi-Turn Empathic Dialogue},
  author={Zhan, Hongli and Gueorguieva, Emma S and Hernandez, Javier and Suh, Jina and Ong, Desmond C and Li, Junyi Jessy},
  journal={arXiv preprint arXiv:2604.11742},
  year={2026}
}
```
