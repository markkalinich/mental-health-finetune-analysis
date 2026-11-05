---
license: other
license_name: health-ai-developer-foundations
license_link: https://developers.google.com/health-ai-developer-foundations/terms
base_model: google/medgemma-1.5-4b-it
pipeline_tag: image-text-to-text
tags:
- medical
- ophthalmology
- surgery
- cataract
- chain-of-thought
- clinical-reasoning
- medgemma
- merged
datasets:
- mehti/LMOD-Cataract-1K-surgical-analysis-cot
language:
- en
metrics:
- accuracy
---

# MedGemma 1.5 4B IT — Cataract Surgical Analysis (Merged)

> [!NOTE]
> This is the **full merged model** (base model + LoRA adapter) for easy deployment and inference.
> The original LoRA adapter is available [here](https://huggingface.co/mehti/medgemma-cataract-surgical-analysis-peft-lora).

This model is a fine-tuned version of [**Google's MedGemma 1.5 4B IT**](https://huggingface.co/google/medgemma-1.5-4b-it) specialized for **cataract surgery analysis**. It was trained on the **Cataract-1K** dataset (a component of the [LMOD benchmark](https://kfzyqin.github.io/lmod/)) using a Chain-of-Thought (CoT) approach to provide expert-level reasoning and safety instructions.

📂 **Source code**: [github.com/b5y/medgemma-impact-challenge](https://github.com/b5y/medgemma-impact-challenge)

## Model Description

This model enhances MedGemma's ability to interpret surgical video frames. Unlike general-purpose models, it is trained to "think before it speaks," providing:

1.  **Thinking Process**: An expert-level reasoning trace that analyzes the surgical phase, identifies instrument-anatomy relationships, and assesses safety margins.
2.  **Final Answer**: A clear, actionable instruction suitable for a surgical resident.

### Output Format

The model generates a structured response:

```
Thinking Process:
The frame shows the phacoemulsification phase with the ultrasonic tip positioned within the lens nucleus. The corneal incision margins appear well-maintained. Safety margins around the posterior capsule are adequate but require continuous monitoring.

Final Answer:
Maintain steady foot pedal pressure and keep the phaco tip centered within the nuclear material to avoid inadvertent contact with the posterior capsule.
```

## Training Data

The training data consists of surgical frames from the **Cataract-1K** dataset. To enable high-quality instruction tuning, reasoning traces were distilled from **Qwen3-VL-30B-A3B-Thinking**.

- **Raw Source Dataset**: [mehti/LMOD-Cataract-1K](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K) — original Cataract-1K frames with bounding box and segmentation annotations from the LMOD benchmark.
- **Generated CoT Dataset**: [mehti/LMOD-Cataract-1K-surgical-analysis-cot](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot) — synthetic chain-of-thought reasoning traces and surgical instructions distilled from Qwen3-VL-30B-A3B-Thinking.

## Training Procedure

The model was fine-tuned using **LoRA** and then merged.

| Parameter | Value |
|---|---|
| **Base Model** | `google/medgemma-1.5-4b-it` |
| **Fine-tuning Method** | LoRA |
| **LoRA Rank (r)** | 16 |
| **LoRA Alpha** | 16 |
| **LoRA Dropout** | 0.05 |
| **Target Modules** | `all-linear` |
| **Quantization** | `4bit-nf4-double_quant` |
| **Image Resolution** | 896 x 896 |
| **Optimizer** | AdamW (fused) |
| **Learning Rate** | 2e-4 |
| **Scheduler** | Linear |
| **Warmup Ratio** | 0.03 |
| **Max Gradient Norm** | 0.3 |
| **Epochs** | 3 (with early stopping) |
| **Effective Batch Size** | 24 |
| **Precision** | `bfloat16` |
| **Cross-Validation** | 5-fold GroupKFold (grouped by surgery case) |

## Training Results

### Evaluation Loss — All Folds

![Eval Loss All Folds](plots/eval_loss_all_folds.png)

All five folds show consistent and monotonically decreasing evaluation loss throughout training. By step 200, every fold converges to a final eval loss in the range of **0.19–0.24**, demonstrating stable learning without signs of overfitting across different data splits.

### Loss Curves — Fold 1

![Loss Curves Fold 1](plots/loss_curves_fold_1.png)

For Fold 1 (the best-performing fold), training loss drops steeply from ~2.4 at initialization and quickly converges near the evaluation loss by step 10. Both train and eval loss then decrease together steadily, with no divergence — indicating no overfitting.

### Token Accuracy — Fold 1

![Token Accuracy Fold 1](plots/token_accuracy_curves_fold_1.png)

Token-level accuracy for Fold 1 climbs from **0.51** at the start to **~0.94** by the final step. Train and eval accuracy track each other closely throughout, with train accuracy slightly above eval accuracy in the later steps.

## Usage

### With 🤗 Transformers

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import torch

# Load the merged model and processor
model_path = "mehti/medgemma-cataract-surgical-analysis"
processor = AutoProcessor.from_pretrained(model_path)
model = AutoModelForImageTextToText.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()

# Load a surgical frame (replace with your image)
image = Image.open("surgical_frame.jpg").convert("RGB")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {
                "type": "text",
                "text": (
                    "You are an expert ophthalmic surgeon reviewing a frame from a cataract surgery video. "
                    "Analyze the surgical scene and provide a chain-of-thought reasoning followed by a "
                    "clear instruction for a surgical resident.\n\n"
                    "Format your response as:\nThinking Process:\n<your reasoning>\n\nFinal Answer:\n<your instruction>"
                ),
            },
        ],
    }
]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device, dtype=torch.bfloat16)

with torch.inference_mode():
    output = model.generate(**inputs, max_new_tokens=512, do_sample=False)

decoded = processor.decode(output[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
print(decoded)
```

### With vLLM

Serve the merged model directly:

```bash
vllm serve mehti/medgemma-cataract-surgical-analysis \
    --host 0.0.0.0 \
    --port 8000 \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.90
```

## Intended Use

-   **Research**: For analyzing multimodal medical AI capabilities in surgical domains.
-   **Education**: As a prototype for AI-assisted surgical training systems.
-   **Limitations**: This model is for research purposes only and is **not** intended for clinical decision-making or direct patient care.

## Citations

If you use this model in your research, please cite the following:

```bibtex
@article{medgemma2025,
  title={MedGemma Technical Report},
  author={Sellergren, Andrew and Kazemzadeh, Sahar and Jaroensri, Tiam and Kiraly, Atilla and Traverse, Madeleine and Kohlberger, Timo and Xu, Shawn and Jamil, Fayaz and Hughes, C{\'\i}an and Lau, Charles and Chen, Justin and Mahvar, Fereshteh and Yatziv, Liron and Chen, Tiffany and Sterling, Bram and others},
  journal={arXiv preprint arXiv:2507.05201},
  year={2025}
}
```

```bibtex
@misc{qin2025lmodlargemultimodalophthalmology,
      title={LMOD: A Large Multimodal Ophthalmology Dataset and Benchmark for Large Vision-Language Models},
      author={Zhenyue Qin and Yu Yin and Dylan Campbell and Xuansheng Wu and Ke Zou and Yih-Chung Tham and Ninghao Liu and Xiuzhen Zhang and Qingyu Chen},
      year={2025},
      eprint={2410.01620},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2410.01620},
}
```

```
@misc{qwen3technicalreport,
      title={Qwen3 Technical Report}, 
      author={Qwen Team},
      year={2025},
      eprint={2505.09388},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.09388}, 
}
```

```
@article{Qwen2.5-VL,
  title={Qwen2.5-VL Technical Report},
  author={Bai, Shuai and Chen, Keqin and Liu, Xuejing and Wang, Jialin and Ge, Wenbin and Song, Sibo and Dang, Kai and Wang, Peng and Wang, Shijie and Tang, Jun and Zhong, Humen and Zhu, Yuanzhi and Yang, Mingkun and Li, Zhaohai and Wan, Jianqiang and Wang, Pengfei and Ding, Wei and Fu, Zheren and Xu, Yiheng and Ye, Jiabo and Zhang, Xi and Xie, Tianbao and Cheng, Zesen and Zhang, Hang and Yang, Zhibo and Xu, Haiyang and Lin, Junyang},
  journal={arXiv preprint arXiv:2502.13923},
  year={2025}
}
```

```
@article{Qwen2VL,
  title={Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution},
  author={Wang, Peng and Bai, Shuai and Tan, Sinan and Wang, Shijie and Fan, Zhihao and Bai, Jinze and Chen, Keqin and Liu, Xuejing and Wang, Jialin and Ge, Wenbin and Fan, Yang and Dang, Kai and Du, Mengfei and Ren, Xuancheng and Men, Rui and Liu, Dayiheng and Zhou, Chang and Zhou, Jingren and Lin, Junyang},
  journal={arXiv preprint arXiv:2409.12191},
  year={2024}
}
```

```
@article{Qwen-VL,
  title={Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond},
  author={Bai, Jinze and Bai, Shuai and Yang, Shusheng and Wang, Shijie and Tan, Sinan and Wang, Peng and Lin, Junyang and Zhou, Chang and Zhou, Jingren},
  journal={arXiv preprint arXiv:2308.12966},
  year={2023}
}
```

NOTE: This documentation is generated using Gemini 3 Pro and verified by human.