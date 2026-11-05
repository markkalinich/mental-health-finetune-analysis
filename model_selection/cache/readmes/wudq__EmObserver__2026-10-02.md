---
license: apache-2.0
base_model:
- Qwen/Qwen3-VL-8B-Thinking
pipeline_tag: image-text-to-text
library_name: transformers
language:
- en
tags:
- qwen3-vl
- vision-language
- multimodal
- visual-emotion
- affective-computing
- emotional-intelligence
- reasoning
datasets:
- wudq/MVEI_PLUS
model-index:
- name: EmObserver
  results:
  - task:
      type: image-text-to-text
      name: Emotion Statement Judgement
    dataset:
      type: wudq/MVEI_PLUS
      name: MVEI
      split: test
    metrics:
    - type: accuracy
      name: Accuracy
      value: 86.23
  - task:
      type: image-text-to-text
      name: Visual Emotion Classification
    dataset:
      type: wudq/MVEI_PLUS
      name: VECBench
      split: test
    metrics:
    - type: accuracy
      name: Overall accuracy
      value: 63.42
  - task:
      type: image-text-to-text
      name: Single-image Emotion Perception
    dataset:
      type: wudq/MVEI_PLUS
      name: EEmo-Bench Single Perception
      split: test
    metrics:
    - type: accuracy
      name: Overall accuracy
      value: 71.94
  - task:
      type: image-text-to-text
      name: Image-pair Emotion Perception
    dataset:
      type: wudq/MVEI_PLUS
      name: EEmo-Bench Pair Perception
      split: test
    metrics:
    - type: accuracy
      name: Overall accuracy
      value: 71.47
---

# EmObserver

Official model release for **“MVEI & EmObserver: Empowering MLLM-Oriented Visual Emotional Intelligence via Emotion Statement Judgement.”**

EmObserver is an emotion-oriented multimodal large language model built from [Qwen3-VL-8B-Thinking](https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking). It is optimized through a four-stage training recipe for visual emotion understanding, Emotion Statement Judgement (ESJ), emotion classification, and single-/multi-image affective reasoning.

The model accepts one or more images with a natural-language question and produces a reasoning-style response followed by a concise answer:

```text
<think>...</think><answer>...</answer>
```

## 🔗 Project map

| Resource | Description | Link |
| --- | --- | --- |
| Paper | MVEI & EmObserver | [arXiv:2607.21061](https://arxiv.org/abs/2607.21061) |
| Original paper (ICLR 2026) | Customizing Visual Emotion Evaluation for MLLMs | [OpenReview](https://openreview.net/forum?id=dQTSXWqZws) · [arXiv:2509.21950](https://arxiv.org/abs/2509.21950) |
| Official code | Inference, evaluation, and four-stage training | [wdqqdw/EmObserver](https://github.com/wdqqdw/EmObserver) |
| Expanded release | Benchmarks, images, predictions, and training data | [wudq/MVEI_PLUS](https://huggingface.co/datasets/wudq/MVEI_PLUS) |
| EmObserver results | Released predictions and metric summaries | [MVEI_PLUS/baselines/Qwen3-VL-EMOBSERVER](https://huggingface.co/datasets/wudq/MVEI_PLUS/tree/main/baselines/Qwen3-VL-EMOBSERVER) |
| Evaluation data | Standardized MVEI, EEmo-Bench, and VECBench metadata | [MVEI_PLUS/benchmarks](https://huggingface.co/datasets/wudq/MVEI_PLUS/tree/main/benchmarks) |
| Training data | Four-stage data and GPT-5.5-filtered INSETS-462k | [MVEI_PLUS/training_data](https://huggingface.co/datasets/wudq/MVEI_PLUS/tree/main/training_data) |
| Original MVEI dataset | Original benchmark release | [wudq/MVEI](https://huggingface.co/datasets/wudq/MVEI) |
| Original INSETS-462k | Original training-data release | [wudq/INSETS-462k](https://huggingface.co/datasets/wudq/INSETS-462k) |
| Original conference code | Earlier MVEI codebase and project release | [wdqqdw/MVEI](https://github.com/wdqqdw/MVEI) |
| Base model | Qwen3-VL-8B-Thinking | [Qwen/Qwen3-VL-8B-Thinking](https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking) |

## 🚀 Quick start with Transformers

Install a compatible PyTorch build first, then install the model dependencies:

```bash
python3 -m pip install -U "transformers>=5.9.0" accelerate pillow
```

The following example uses the same MVEI question form as the released test metadata:

```python
import torch
from transformers import AutoProcessor, Qwen3VLForConditionalGeneration

model_id = "wudq/EmObserver"

model = Qwen3VLForConditionalGeneration.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_id)

image_url = (
    "https://huggingface.co/datasets/wudq/MVEI_PLUS/resolve/main/"
    "benchmarks/MVEI/images/contentment/contentment_14236.jpg"
)
prompt = (
    "Is the following statement correct about the image? Upon viewing this image, "
    "observers, despite various individual or contextual factors, are most likely "
    "to experience negative emotions. Choose the answer from "
    "{'A': 'Correct.', 'B': 'Incorrect.'}. Answer in the format of "
    "<think>...</think><answer>...</answer>."
)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": image_url},
            {"type": "text", "text": prompt},
        ],
    }
]

inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

generated = model.generate(**inputs, max_new_tokens=1024)
trimmed = [output[len(input_ids):] for input_ids, output in zip(inputs.input_ids, generated)]
response = processor.batch_decode(
    trimmed,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False,
)[0]
print(response)
```

For multi-image questions, add each image to `content` before the text item:

```python
"content": [
    {"type": "image", "url": first_image_url},
    {"type": "image", "url": second_image_url},
    {"type": "text", "text": pair_prompt},
]
```

FlashAttention 2 can reduce memory use on supported hardware. Install a build compatible with your CUDA/PyTorch stack, then pass `attn_implementation="flash_attention_2"` to `from_pretrained`.

## 🧪 Full evaluation with the official code

The official repository provides the vLLM inference wrapper, benchmark loaders, output parsing, and metric calculators:

```bash
git clone https://github.com/wdqqdw/EmObserver.git
cd EmObserver

python3 -m pip install -r requirements.txt
hf download wudq/MVEI_PLUS --repo-type dataset --local-dir public_data
hf download wudq/EmObserver --local-dir models/EmObserver

python3 -m evaluate.infer_and_eval \
  --engine qwen3_vl_vllm \
  --size emobserver \
  --gpu_n 8
```

Adjust `--gpu_n` to the visible GPUs that can hold the checkpoint. Use `--bench` to select a subset from `MVEI`, `VECBench`, `EEmo-Bench-Single-Perception`, and `EEmo-Bench-Pair-Perception`.

## 💬 Benchmark-style examples

The examples below reproduce question forms from the standardized test metadata. The listed answer is the reference final answer; reasoning text may vary.

### 1. Emotion Statement Judgement — MVEI

**Image:** [contentment_14236.jpg](https://huggingface.co/datasets/wudq/MVEI_PLUS/resolve/main/benchmarks/MVEI/images/contentment/contentment_14236.jpg)

```text
Is the following statement correct about the image? Upon viewing this image,
observers, despite various individual or contextual factors, are most likely
to experience negative emotions. Choose the answer from
{'A': 'Correct.', 'B': 'Incorrect.'}. Answer in the format of
<think>...</think><answer>...</answer>.
```

Reference final answer:

```text
<answer>Incorrect.</answer>
```

### 2. Single-image emotion perception — EEmo-Bench

**Image:** [EEmo-Bench single image 1](https://huggingface.co/datasets/wudq/MVEI_PLUS/resolve/main/benchmarks/EEmo-Bench/EEmo-Bench_single/images/1.jpg)

```text
What do you think of surprise as one of the three main emotions you felt from
this image? Choose the answer from {'A': 'No', 'B': 'Yes'}. Answer in the
format of <think>...</think><answer>...</answer>.
```

Reference final answer:

```text
<answer>Yes.</answer>
```

### 3. Image-pair emotion comparison — EEmo-Bench

**Images:** [image 579](https://huggingface.co/datasets/wudq/MVEI_PLUS/resolve/main/benchmarks/EEmo-Bench/EEmo-Bench_pair/images/579.jpg) and [image 100](https://huggingface.co/datasets/wudq/MVEI_PLUS/resolve/main/benchmarks/EEmo-Bench/EEmo-Bench_pair/images/100.jpg)

```text
Which emotion is evoked in both images and is common to them? Choose the
answer from {'A': 'Neutral', 'B': 'Fear', 'C': 'Sadness', 'D': 'Joy'}.
Answer in the format of <think>...</think><answer>...</answer>.
```

Reference final answer:

```text
<answer>Joy.</answer>
```

### 4. Visual emotion classification — VECBench

**Image:** [abstract_0001.jpg](https://huggingface.co/datasets/wudq/MVEI_PLUS/resolve/main/benchmarks/VECBench/images/Abstract/testImages_abstract/abstract_0001.jpg)

```text
Which emotion might this image evoke? Choose the most likely one from
['Amusement', 'Anger', 'Awe', 'Content', 'Disgust', 'Excitement', 'Fear',
'Sad']. Think step by step. Respond in the format:
<think>{your reasoning}</think><answer>{your final answer}</answer>.
```

Reference final answer:

```text
<answer>Content.</answer>
```

## 📊 Released evaluation results

These values are taken from the released EmObserver inference outputs in [MVEI_PLUS](https://huggingface.co/datasets/wudq/MVEI_PLUS/tree/main/baselines/Qwen3-VL-EMOBSERVER). They are intended to make the checkpoint release traceable; environment or decoding changes may produce different results.

| Benchmark | Metric | Result |
| --- | --- | ---: |
| MVEI | Overall accuracy | 86.23% |
| MVEI | Sentiment polarity | 86.47% |
| MVEI | Emotion interpretation | 83.55% |
| MVEI | Scene context | 90.30% |
| MVEI | Perception subjectivity | 86.06% |
| VECBench | Overall accuracy | 63.42% |
| EEmo-Bench Single | Overall accuracy | 71.94% |
| EEmo-Bench Pair | Overall accuracy | 71.47% |

## 🏋️ Training overview

EmObserver is produced by the four-stage public training pipeline:

1. supervised fine-tuning;
2. GRPO-based reinforcement learning;
3. on-policy self-distillation (OPSD);
4. GRPO with an LLM-consistency reward.

The runnable scripts are in the [official code repository](https://github.com/wdqqdw/EmObserver/tree/main/training), and their released inputs are under [MVEI_PLUS/training_data](https://huggingface.co/datasets/wudq/MVEI_PLUS/tree/main/training_data). External judge credentials are not included; users must provide their own endpoint when reproducing the final stage.

## ⚠️ Intended use and limitations

EmObserver is intended for research on visual emotion understanding, affective image analysis, multimodal reasoning, and benchmark development.

- Visual emotion is inherently subjective and culturally/contextually dependent. A model prediction should not be treated as a universal description of how every person will feel.
- The model may inherit social, cultural, demographic, and content biases from its base model and training data.
- The checkpoint is not designed for mental-health diagnosis, psychological profiling, surveillance, hiring, education assessment, or other high-stakes decisions about individuals.
- Generated reasoning can be plausible but factually or emotionally incorrect. Verify outputs when reliability matters.
- Users are responsible for reviewing the licenses, attribution requirements, privacy constraints, and redistribution terms of input images and downstream datasets.

## 📄 License

The checkpoint is released under the Apache 2.0 license, following its [Qwen3-VL-8B-Thinking](https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking) base model. Third-party datasets and images retain their respective licenses and terms.

## 📝 Citation

If you use EmObserver or the expanded training and evaluation release, please cite the EmObserver paper below. When using the MVEI benchmark, dataset, or Emotion Statement Judgement formulation, please also cite the original ICLR 2026 paper.

```bibtex
@article{wu2026mvei_emobserver,
  title   = {MVEI \& EmObserver: Empowering MLLM-Oriented Visual Emotional Intelligence via Emotion Statement Judgement},
  author  = {Wu, Daiqing and Yang, Dongbao and Yao, Jiashu and Zhang, Hongrui and Ma, Can and Zhou, Yu and Zhao, Sicheng},
  journal = {arXiv preprint arXiv:2607.21061},
  year    = {2026}
}

@inproceedings{wu2026customizing,
  title     = {Customizing Visual Emotion Evaluation for MLLMs: An Open-vocabulary, Multifaceted, and Scalable Approach},
  author    = {Wu, Daiqing and Yang, Dongbao and Zhao, Sicheng and Ma, Can and Zhou, Yu},
  booktitle = {International Conference on Learning Representations},
  year      = {2026},
  url       = {https://openreview.net/forum?id=dQTSXWqZws}
}
```
