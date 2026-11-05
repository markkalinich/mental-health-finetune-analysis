---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: image-text-to-text
tags:
  - robotics
  - failure-detection
  - manipulation
  - vision-language
  - multi-view
  - internvl
base_model: OpenGVLab/InternVL3-8B
---

# Guardian — Multi-View VLM for Robotic Planning & Execution Failure Detection (Vanilla variant)

**Guardian** is a vision-language model fine-tuned for **unified planning and execution verification** in robotic manipulation. Given an instruction and one or more images of the robot scene, it predicts whether a proposed plan is correct (planning verification) or whether a subtask was successfully executed (execution verification).

This checkpoint (`guardian-vanilla`) is the **vanilla** variant: it is trained and inferred **without** chain-of-thought reasoning, emitting only the final `<answer>` and `<category>` tokens. This makes it ~6× faster at inference than the thinking variant at a small accuracy cost (see Table IV of the paper). The richer CoT counterpart (`guardian-thinking`) is released at [`paulpacaud/guardian-thinking`](https://huggingface.co/paulpacaud/guardian-thinking).

| Project page | Paper | Code | Data |
|---|---|---|---|
| [di.ens.fr/willow/research/guardian](https://www.di.ens.fr/willow/research/guardian/) | [arXiv:2512.01946](https://arxiv.org/abs/2512.01946) | [GitHub](https://github.com/) | [🤗 Guardian collection](https://huggingface.co/collections/paulpacaud/robotic-failure-detection-dataset-and-model-guardian) |

## Model summary

- **Architecture**: InternVL3-8B (Qwen2.5-7B LLM + InternViT-300M-448px-V2.5), fine-tuned with LoRA (rank 16) on the LLM only; visual encoder and MLP connector kept frozen.
- **Capabilities**:
  - **Planning verification** — from an initial scene image and a proposed list of subtasks, decide whether the plan is correct.
  - **Execution verification** — from before/after observations of a subtask (single-view or multi-view), decide whether the subtask succeeded.
  - **Vanilla mode** — direct prediction, no reasoning trace.
- **Output format**:
  - Vanilla: `<answer> True|False </answer> <category> ... </category>`
- **Training data**: FailCoT (RLBench-Fail + BridgeDataV2-Fail), ~30K planning + execution failures. See the paper *Scaling Cross-Environment Failure Reasoning Data for Vision-Language Robotic Manipulation* (Pacaud et al., 2026).

## Quick start

The simplest way to run Guardian is the lightweight wrapper shipped in the Guardian repo (`examples/guardian.py`):

```python
from examples.guardian import Guardian

guardian = Guardian(
    model_path="<path>/guardian-vanilla",
    thinking=False,
)

# Planning verification: 1 image of the initial scene
answer, category = guardian.verify_plan(
    img_paths_list=["/path/to/start_img.png"],
    task_instruction="stack the red cup on the blue cup",
    plan=str([
        "grasp red cup",
        "move grasped object on top of blue cup",
        "release",
    ]),
)

# Execution verification: 2, 6, or 8 images (before/after, possibly multi-view)
answer, category = guardian.verify_subtask(
    img_paths_list=[
        "/path/to/start_left.png",
        "/path/to/start_right.png",
        "/path/to/start_wrist.png",
        "/path/to/end_left.png",
        "/path/to/end_right.png",
        "/path/to/end_wrist.png",
    ],
    task_instruction="stack the red cup on the blue cup",
    subtask_instruction="grasp red cup",
)
```

For execution verification, the wrapper accepts:
- **2 images** — single-view: `[start, end]`
- **6 images** — three views: `[start_left, start_right, start_wrist, end_left, end_right, end_wrist]`
- **8 images** — four views, similarly ordered.

See [`docs/RUN_DEMO.md`](https://github.com/) in the Guardian repo for the full demo.

## Downloading the checkpoint

```bash
hf download paulpacaud/guardian-vanilla \
    --local-dir ./data/failure_forge/models/guardian-vanilla
```

The codebase expects the checkpoint to live under `./data/failure_forge/models/guardian-vanilla/`.

## Evaluation

Guardian is evaluated on three real-robot OOD benchmarks bundled at [`paulpacaud/Guardian-FailCoT-OOD-datasets`](https://huggingface.co/datasets/paulpacaud/Guardian-FailCoT-OOD-datasets) — UR5-Fail, RoboFail, RoboVQA — plus the in-distribution test splits of FailCoT (RLBench-Fail / BridgeDataV2-Fail). Reproduce numbers following [`docs/Offline_VQA_Evaluation.md`](https://github.com/) in the Guardian repo.

## Intended use

Guardian is designed as a plug-and-play verification module for robotic manipulation pipelines (e.g. as the verifier in 3D-LOTUS++): at each planning step or subtask boundary, query Guardian; on a failure, trigger replanning or re-execution. Use the vanilla variant when inference latency matters more than peak accuracy.

## Citation

```bibtex
@misc{pacaud2026guardian_failcot,
  title  = {Scaling Cross-Environment Failure Reasoning Data for Vision-Language Robotic Manipulation},
  author = {Paul Pacaud and Ricardo Garcia and Shizhe Chen and Cordelia Schmid},
  year   = {2026},
  eprint = {2512.01946},
  archivePrefix = {arXiv},
  primaryClass  = {cs.RO}
}
```

If you specifically build on the earlier Guardian workshop paper:

```bibtex
@inproceedings{pacaud2025guardian,
  title     = {Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models},
  author    = {Paul Pacaud and Ricardo Garcia Pinel and Shizhe Chen and Cordelia Schmid},
  booktitle = {Workshop on Making Sense of Data in Robotics: Composition, Curation, and Interpretability at Scale at CoRL 2025},
  year      = {2025},
  url       = {https://openreview.net/forum?id=wps46mtC9B}
}
```

## License

Released under the Apache 2.0 license, inheriting the license of the InternVL3-8B base model.
