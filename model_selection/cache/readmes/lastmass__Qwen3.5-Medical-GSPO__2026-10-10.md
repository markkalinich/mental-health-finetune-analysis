---
language:
- zh
- en
license: apache-2.0
base_model: unsloth/Qwen3.5-4B
tags:
- medical
- reasoning
- rlvr
- grpo
- gspo
- qwen3.5
- chinese-medical
pipeline_tag: image-text-to-text
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
---

# Qwen3.5-4B-Medical-GSPO

A Chinese medical reasoning model fine-tuned from [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) using a two-stage training pipeline: Supervised Fine-Tuning (SFT) for format alignment, followed by Group Sequence Policy Optimization (GSPO) with an LLM-as-Judge reward function.

## Model Description

This model is designed to produce structured chain-of-thought (CoT) reasoning for Chinese medical questions, including clinical diagnosis, treatment planning, and differential diagnosis.

### Training Pipeline

**Stage 1 — Supervised Fine-Tuning (SFT)**

The model was first trained with SFT on the [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) dataset (Chinese subset) to establish a consistent output format: a `<think>...</think>` reasoning block followed by a concise final answer.

**Stage 2 — GSPO with LLM-as-Judge**

GSPO was proposed by Zheng et al. ([arXiv:2507.18071](https://arxiv.org/abs/2507.18071)).

Reinforcement learning was applied using GSPO (Group Sequence Policy Optimization), a sequence-level variant of GRPO that computes importance ratios and clipping at the sequence level rather than the token level, improving training stability over long horizons.

The reward function uses DeepSeek-Chat as an LLM judge with a 5-tier scoring scheme:

| Score | Criterion |
|-------|-----------|
| +2.0 | Same meaning as the ground truth |
| +0.5 | Different wording but medically reasonable |
| 0.0 | Reasonable but outside medical domain |
| -0.5 | Contains facts that contradict the ground truth |
| -1.0 | Incoherent, grammatically broken, or nonsensical |

The judge evaluates only the content after `</think>` — the final conclusion — not the CoT reasoning chain. This design prevents reward hacking via verbose but incorrect reasoning.

### Training Details

| Parameter | Value |
|-----------|-------|
| Base model | Qwen3.5-4B |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| Target modules | q/k/v/o proj, gate/up/down proj |
| Batch size (effective) | 8 (2 × 4 grad accum) |
| Num generations | 4 |
| Max seq length | 2048 |
| Importance sampling level | sequence |
| Loss type | dr_grpo |
| Reward model | DeepSeek-V4-Pro (via API) |
| Framework | Unsloth + TRL |

### Training Dynamics

The model was trained across multiple resume sessions. Reward (smoothed) improved consistently from ~0.57 in early training to ~0.89 in the final 50 steps. KL divergence remained stable around 0.5 throughout GSPO training, with no signs of collapse.

## Usage

```python
from unsloth import FastVisionModel
import torch

max_seq_length = 2048 # Can increase for longer reasoning traces
model, tokenizer = FastVisionModel.from_pretrained(
    "lastmass/Qwen3.5-Medical-GSPO",
    max_seq_length = max_seq_length,
    load_in_4bit = False,
    fast_inference = False, 
    max_lora_rank = lora_rank,
    gpu_memory_utilization = 0.9, 
)

messages = [
    {"role" : "user", "content" : """患者男性，65岁，突发胸痛2小时，心电图示II、III、aVF导联ST段抬高，最可能的诊断是？"""}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True, # Must add for generation
    enable_thinking=True,
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 512, # Increase for longer outputs!
    # temperature = 0.7, top_p = 0.8, top_k = 20, # For non thinking
    temperature=1.0, top_p=0.95, top_k=20,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```

## Example Outputs

### Example 1 — Cardiovascular Diagnosis

**Input:**
> 患者男性，65岁，突发胸痛2小时，心电图示II、III、aVF导联ST段抬高，最可能的诊断是？

**Output (`<think>` block):**
> 患者是65岁的男性，突然胸痛，这听起来很紧急。心电图显示II、III、aVF导联的ST段抬高，这让我想到心梗。嗯，II、III、aVF这些导联通常和下壁有关，所以可能是下壁的心肌梗死。不过，我还需要考虑其他可能性。比如，有没有可能是其他原因导致的胸痛？比如肺栓塞？肺栓塞的话，心电图上通常会有右心负荷过重的表现，但这里提到的是ST段抬高，这更像是心肌缺血的表现。再考虑心包炎——心包炎通常会有广泛导联的ST段抬高，而不是像这样集中在II、III、aVF。所以，心包炎的可能性不大。综合来看，下壁的心肌梗死是最可能的诊断。

**Final answer:**
> 根据患者的症状和心电图表现，最可能的诊断是**下壁心肌梗死**。II、III、aVF导联的ST段抬高是下壁心肌梗死的典型心电图特征。建议立即进行心肌酶谱检测、动态心电图监测，并尽快启动再灌注治疗（PCI或溶栓）。

---

### Example 2 — Complex Obstetric Emergency

**Input:**
> 患者女性，28岁，停经8周，突发右下腹剧烈疼痛伴晕厥，血压80/50mmHg，腹部压痛明显，后穹窿穿刺抽出不凝血，最可能的诊断是？

**Output (`<think>` block):**
> 患者是28岁的女性，停经8周，这应该是个怀孕的早期阶段。突然右下腹剧烈疼痛，还晕厥了，这听起来不太妙。血压80/50mmHg，这明显是低血压，可能意味着有失血的情况。腹部压痛明显，后穹窿穿刺抽出不凝血，这提示有腹腔内出血。结合怀孕8周，我想到可能是宫外孕。怀孕早期，如果胚胎在子宫外着床，比如输卵管，那就会引起剧烈腹痛和出血。不凝血这个特征很重要——腹腔内出血通常不会凝固，这进一步支持了宫外孕破裂导致腹腔出血的诊断。

**Final answer:**
> 根据患者的症状和病史，最可能的诊断是**宫外孕（输卵管妊娠破裂）**。停经8周+突发剧烈腹痛+休克体征+后穹窿抽出不凝血，高度提示腹腔内大出血。需立即开通静脉通路、备血，急诊手术探查，同时完善血HCG和床旁超声。

---

## Limitations

- This is a LoRA adapter trained on a relatively small dataset (~20k examples). It is **not** validated for clinical use.
- Performance on rare diseases, highly specialized subspecialties, and cases requiring memorization of specific drug dosages or classification codes may be limited.
- The model performs better on reasoning-heavy questions than on pure factual recall (e.g., specific surgical nomenclature, drug interaction tables).
- Outputs should always be reviewed by qualified medical professionals before any clinical application.

## Citation

If you use this model, please cite the relevant works:

```bibtex
@misc{qwen3.5-medical-gspo,
  author = {lastmass},
  title = {Qwen3.5-4B Medical GSPO: Chinese Medical Reasoning via LLM-as-Judge Reinforcement Learning},
  year = {2025},
  publisher = {HuggingFace},
  url = {https://huggingface.co/lastmass/Qwen3.5-GSPO-Lora}
}
```

## Acknowledgements

- [Unsloth](https://github.com/unslothai/unsloth) for efficient fine-tuning infrastructure
- [FreedomIntelligence](https://huggingface.co/FreedomIntelligence) for the medical reasoning dataset
- [DeepSeek](https://www.deepseek.com) for the reward model API
- [Qwen Team](https://huggingface.co/Qwen) for the base model