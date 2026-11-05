---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3-1.7B
tags:
- qwen3
- reinforcement-learning
- grpo
- static-rubric
- rubric-staleness
- rar
---

# Qwen3-1.7B Static-R0 Policy Checkpoint

This public model repository contains one policy checkpoint from the
static-rubric discriminability-horizon experiment. The domain and optimizer
step are encoded in the repository name.

## Experiment

- Base policy: `Qwen/Qwen3-1.7B`
- Base revision: `70d244cc86ccca08cf5af4e1e306ecf908b1ad5e`
- RL algorithm: GRPO
- Training reward: frozen prompt-specific initial rubric (`R0`)
- Domain: RaR Medicine or RaR Science, as named in the repository
- Training seed: 11
- Export format: Hugging Face Transformers, BF16 safetensors
- Checkpoint contents: model weights, configuration, tokenizer, and chat template
- Excluded: optimizer, scheduler, trainer state, rollouts, rubrics, and evaluation data

Medicine checkpoint repositories cover the ten planned audit points through
step 48. Science training was only saved through step 3 at the time of this
upload, so the public Science repositories contain steps 0 and 3.

## Loading

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

repo_id = "HYU-NLP-EVAL/<repository-name>"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    dtype="bfloat16",
    device_map="auto",
)
```

## Intended use

These checkpoints are research artifacts for studying reward saturation and
static-rubric staleness during policy optimization. Medicine checkpoints are
not medical devices and must not be used as a substitute for professional
medical advice.
