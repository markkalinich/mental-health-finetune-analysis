---
datasets: LSY-lab/triage_v3
library_name: lerobot
license: apache-2.0
model_name: dit_meanflow
pipeline_tag: robotics
tags:
- robotics
- lerobot
- dit_meanflow
---

# Model Card for dit_meanflow

<!-- Provide a quick summary of what the model is/does. -->


_Model type not recognized — please update this template._


This policy has been trained and pushed to the Hub using [LeRobot](https://github.com/huggingface/lerobot).
See the full documentation at [LeRobot Docs](https://huggingface.co/docs/lerobot/index).

---

## How to Get Started with the Model

For a complete walkthrough, see the [training guide](https://huggingface.co/docs/lerobot/il_robots#train-a-policy).
Below is the short version on how to train and run inference/eval:

### Train from scratch

```bash
python -m lerobot.scripts.train \
  --dataset.repo_id=${HF_USER}/<dataset> \
  --policy.type=act \
  --output_dir=outputs/train/<desired_policy_repo_id> \
  --job_name=lerobot_training \
  --policy.device=cuda \
  --policy.repo_id=${HF_USER}/<desired_policy_repo_id>
  --wandb.enable=true
```

*Writes checkpoints to `outputs/train/<desired_policy_repo_id>/checkpoints/`.*

### Evaluate the policy/run inference

```bash
python -m lerobot.record \
  --robot.type=so100_follower \
  --dataset.repo_id=<hf_user>/eval_<dataset> \
  --policy.path=<hf_user>/<desired_policy_repo_id> \
  --episodes=10
```

Prefix the dataset repo with **eval\_** and supply `--policy.path` pointing to a local or hub checkpoint.

---

## Model Details

* **License:** apache-2.0