---
language: en
tags:
- reinforcement-learning
- openenv
- grpo
- agent-safety
- meta-pytorch
license: apache-2.0
---

# Qwen3-0.6B — Fine-tuned with GRPO on Agent Safety

Trained using [OpenEnv](https://github.com/meta-pytorch/OpenEnv) + TRL GRPO on the
**Agent Safety** environment as part of the Meta PyTorch OpenEnv Hackathon.

## Training Details
- Environment: `agent_safety_env`
- Algorithm: GRPO (Group Relative Policy Optimization)
- Episodes: 16
- Reward: Partial credit per safety criterion

## Environment
- HF Space: `https://huggingface.co/spaces/amulyalakku/agent-safety-env`
