---
library_name: transformers
pipeline_tag: image-text-to-text
base_model: Qwen/Qwen3-VL-4B-Instruct
datasets:
- zrwang1211/SafeAtlas-VL
tags:
- safety
- multimodal
- vision-language
- vlm
- content-moderation
- qwen3-vl
- ordinal-classification
---

# SafeAtlas Guard 4B

SafeAtlas Guard 4B is a target-conditioned multimodal safety model introduced
in **SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and
Guard Models**. It evaluates image content, image-grounded user requests, and
assistant responses.

The model returns:

- one of five ordered safety levels;
- a continuous risk score from 0 to 100;
- three auxiliary safety-judge predictions for request and response targets.

## Resources

- Paper: [SafeAtlas-VL](https://arxiv.org/abs/2608.29098)
- Code: [github.com/zrwang1211/SafeAtlas-VL](https://github.com/zrwang1211/SafeAtlas-VL)
- Dataset: [zrwang1211/SafeAtlas-VL](https://huggingface.co/datasets/zrwang1211/SafeAtlas-VL)
- Model collection: [SafeAtlas Guard](https://huggingface.co/collections/zrwang1211/safeatlas-guard)

We thank [mradermacher](https://huggingface.co/mradermacher) for sharing [community GGUF quantizations](https://huggingface.co/mradermacher/SafeAtlas-Guard-4B-GGUF).

## Installation

```bash
git clone https://github.com/zrwang1211/SafeAtlas-VL.git
cd SafeAtlas-VL
pip install -e .
```

## Quickstart

```python
from ordinal_safety_vlm import SafetyPredictor

predictor = SafetyPredictor(
    "zrwang1211/SafeAtlas-Guard-4B",
    device_map="auto",
    dtype="bfloat16",
)

result = predictor.predict(
    image="examples/example.jpg",
    target_name="response",
    request="What fruit is shown in the image?",
    response="The image shows a red apple.",
)

print(result.safety_label)  # safe core
print(f"{result.risk_score:.2f}")
print(result.teacher_predictions)  # {'judge1': 'safe', 'judge2': 'safe', 'judge3': 'safe'}
```

The image may be a local path, `pathlib.Path`, or `PIL.Image.Image`.

## Prediction fields

| Field | Description |
| --- | --- |
| `safety_label` | Predicted five-level safety label. |
| `risk_score` | Expected ordinal level mapped linearly to 0–100. |
| `z` | Scalar latent risk value before the learned thresholds. |
| `thresholds` | Four learned monotonic ordinal thresholds. |
| `ordinal_probs` | Cumulative probabilities of exceeding each ordinal threshold. |
| `class_probs` | Probability distribution over the five levels. |
| `category` | Predicted harm category or `none`. |
| `category_probs` | Probability distribution over 16 category labels. |
| `teacher_predictions` | Auxiliary teacher-head predictions. |
| `teacher_probs` | Auxiliary teacher-head probability distributions. |

The five ordered labels are `safe core`, `safe leaning disputed`, `boundary
uncertain`, `unsafe leaning disputed`, and `unsafe core`. Teacher-head outputs
are defined for request and response targets.

## Model architecture and training

SafeAtlas Guard 4B uses Qwen3-VL-4B-Instruct as its multimodal backbone.

Training has two stages. Stage 1 performs full-parameter multimodal instruction
tuning so the backbone learns structured, target-conditioned safety judgments.
Stage 2 freezes the instruction-tuned backbone and trains the five-level
cumulative ordinal head, the 16-way harm-category head, and three
teacher-simulation heads. The ordinal stage uses Gaussian-smoothed targets and
learned monotonic thresholds.

The sharded `model-*.safetensors` files contain the instruction-tuned backbone.
`ordinal_heads.safetensors` contains the prediction heads and learned
thresholds. `ordinal_config.json` defines their architecture, labels, score
range, and prompt files.

The backbone tensors are stored in BF16. All prediction-head tensors,
including the four trainable ordinal threshold parameters, are stored in FP32.

## External benchmark results

F1 denotes unsafe-class F1 in percentage points.

| Benchmark | Target | Threshold | F1 |
| --- | --- | ---: | ---: |
| BeaverTails-V | Multimodal request | 15 | 87.94 |
| BeaverTails-V | Multimodal response | 25 | 79.03 |
| SPA-VL | Multimodal request | 35 | 80.61 |
| SPA-VL | Multimodal response | 25 | 75.38 |
| VLGuard | Multimodal request | 15 | 95.49 |
| HarmImageTest | Image | 25 | 69.68 |
| LLaVAGuard | Image | 20 | 69.68 |
| **Multimodal average (7)** |  |  | **79.69** |
| HarmBench Prompt | Text request | 15 | 99.12 |
| HarmBench Response | Text response | 30 | 85.33 |
| OpenAI Moderation | Text request | 75 | 74.66 |
| SafeRLHF | Text response | 20 | 72.82 |
| **Overall average (11)** |  |  | **80.88** |

## Sensitive content and intended use

SafeAtlas Guard is intended for multimodal safety moderation, ordinal risk
assessment, red-teaming, evaluation, and safety alignment research. Its
training and evaluation data necessarily include unsafe, offensive, sensitive,
and potentially disturbing material. The model and associated resources must
not be used to facilitate harmful activity or to target individuals or
protected groups.

Predictions are context- and policy-dependent. Performance can vary across
languages, cultures, domains, image quality, and previously unseen harm types.
The model should be evaluated in the intended deployment setting and should
not be the sole basis for high-impact decisions.

## Citation

```bibtex
@misc{wang2026safeatlasvlbinarymultimodalsafety,
  title={SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Models},
  author={Zongrui Wang and Xiangyang Zhu and Sicheng Wang and Han Wang and Dingyi Rong and Zeyu Zhang and Chunyi Li and Yue Shi and Kaiwei Zhang and Zicheng Zhang and Yuan Tian and Qi Jia and Yan Teng and Wei Sun and Ning Liu and Guangtao Zhai},
  year={2026},
  eprint={2608.29098},
  archivePrefix={arXiv},
  primaryClass={cs.AI},
  url={https://arxiv.org/abs/2608.29098},
}
```
