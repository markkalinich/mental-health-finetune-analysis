---
license: mit
base_model: Qwen/Qwen3-4B
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

# MINT-empathy-Qwen3-4B

This model is the **Q + D_KL** MINT checkpoint fine-tuned from [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) for multi-turn empathic dialogue.

MINT, short for **Multi-turn Inter-tactic Novelty Training**, is a reinforcement learning framework that optimizes empathic response quality together with cross-turn discourse-move novelty. In the paper, this checkpoint is the **best overall released MINT model**, delivering the strongest joint tradeoff between empathy quality and reduced cross-turn tactic repetition.

## Key Results

On the Lend-an-Ear test set reported in the paper, which contains 315 supporter turns across 50 conversations:

1. Aggregate empathy improves from **3.75** to **4.67** relative to the vanilla Qwen3-4B baseline.
2. Tactic stickiness decreases from **0.57** to **0.42**.
3. This checkpoint provides the clearest joint gain in empathy and reduced cross-turn repetition.

## Training Summary

| | |
|---|---|
| **Method** | GRPO via [VERL](https://github.com/volcengine/verl) |
| **Reward** | Empathy quality + cross-turn tactic diversity |
| **Base model** | [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) |
| **KL coeff** | 0.01 |
| **Diversity weight** | 1.0 |
| **Response length** | 2048 tokens |
| **Rollouts** | n=8 per prompt |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("hongli-zhan/MINT-empathy-Qwen3-4B")
tokenizer = AutoTokenizer.from_pretrained("hongli-zhan/MINT-empathy-Qwen3-4B")
```

With vLLM:

```python
from vllm import LLM
llm = LLM(model="hongli-zhan/MINT-empathy-Qwen3-4B")
```

## Intended Use and Limitations

This model is intended for research on empathic dialogue, discourse diversity, and supportive response generation. It is a research artifact, not a therapy system, and it was evaluated on fixed gold-history conversation contexts rather than fully interactive free-running conversations.

## Related Artifacts

- Paper: [Discourse Diversity in Multi-Turn Empathic Dialogue](https://arxiv.org/abs/2604.11742)
- Project page: [honglizhan.github.io/mint-empathy](https://honglizhan.github.io/mint-empathy/)
- Code: [github.com/honglizhan/mint-empathy](https://github.com/honglizhan/mint-empathy)
- Tactic taggers: [hongli-zhan/empathy-tactic-taggers-llama3.1-8b](https://huggingface.co/hongli-zhan/empathy-tactic-taggers-llama3.1-8b)
- Smaller checkpoint: [hongli-zhan/MINT-empathy-Qwen3-1.7B](https://huggingface.co/hongli-zhan/MINT-empathy-Qwen3-1.7B)

## Citation

```bibtex
@article{zhan2026discourse,
  title={Discourse Diversity in Multi-Turn Empathic Dialogue},
  author={Zhan, Hongli and Gueorguieva, Emma S and Hernandez, Javier and Suh, Jina and Ong, Desmond C and Li, Junyi Jessy},
  journal={arXiv preprint arXiv:2604.11742},
  year={2026}
}
```
