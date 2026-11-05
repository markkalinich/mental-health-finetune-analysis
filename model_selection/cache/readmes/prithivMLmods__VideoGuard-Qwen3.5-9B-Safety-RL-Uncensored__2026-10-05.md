---
license: apache-2.0
base_model:
- Qwen/Qwen3.5-9B
language:
- en
pipeline_tag: video-text-to-text
library_name: transformers
tags:
- text-generation-inference
- reinforcement-learning
- video-text-to-text
- alignment-training
- RLHF
- RFT
- video-understanding
- video-classification
- video-safety
- content-safety
- content-moderation
- safety-classifier
- guardrail
datasets:
- prithivMLmods/OpenVideo-Scene-Reasoning
- PALM-Lab/vid-guard-rlhf-unsafe
---

<div style="font-family: 'Courier New', Courier, monospace; background-color: #000000; border: 1px solid #333333; border-radius: 12px; padding: 24px; color: #FFFFFF; max-width: 800px; margin: 0 auto;">
  <h1 style="font-size: 24px; font-weight: bold; margin: 0 0 20px 0; color: #FFFFFF;">VideoGuard-9B</h1>
  
  <img src="https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/JTY9kisGBZrgjSBWO3JyA.webp" alt="demo" style="width: 100%; max-width: 600px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #333333;">

  <details style="background-color: #111111; border: 1px solid #333333; border-radius: 8px; padding: 12px; margin-bottom: 20px; cursor: pointer;">
    <summary style="color: #FFFFFF; font-weight: bold; outline: none;">think</summary>
    <div style="margin-top: 12px; white-space: pre-wrap; color: #FFFFFF; font-size: 13px; line-height: 1.6;">
The user wants me to classify an image and provide a specific output format.
The image shows a person on a high-rise structure, likely a crane or a tower under construction, with a cityscape below.
I need to output three lines:
1.  **DESCRIPTION:** A single sentence describing the image.
2.  **EXPLANATION:** One or two sentences explaining the category codes (C1-C6) and why.
3.  **GUARDRAIL:** A single-line JSON object with specific boolean keys.

**Step 1: Description**
The image shows a person in a black hoodie and camouflage pants standing on a red steel structure, likely a crane or a high-rise construction site, with a cityscape visible in the foggy background.

**Step 2: Explanation**
The image depicts a worker on a high structure, which falls under "C5 (Illegal/Regulated Activities)" as it shows construction or maintenance work. It does not show sexual content, harassment, threats, misinformation, or hate symbols.

**Step 3: Guardrail**
I need to set the boolean keys to true or false.
- C1 (Sexual Content): False.
- C2 (Harassment & Bullying): False.
- C3 (Threats, Violence & Harm): False.
- C4 (False & Deceptive Information): False.
- C5 (Illegal/Regulated Activities): True (Construction work).
- C6 (Hateful Content & Extremism): False.

Let's format the output.
Line 1: DESCRIPTION: A person in a black hoodie and camouflage pants stands on a red steel structure, likely a crane or high-rise construction site, with a cityscape visible in the foggy background.
Line 2: EXPLANATION: The image depicts a worker on a high structure, which falls under "C5 (Illegal/Regulated Activities)" as it shows construction or maintenance work.
Line 3: GUARDRAIL: {"C1(Sexual Content)": false, "C2(Harassment & Bullying)": false, "C3(Threats, Violence & Harm)": false, "C4(False & Deceptive Information)": false, "C5(Illegal/Regulated Activities)": true, "C6(Hateful Content & Extremism)": false}

Double check constraints:
- Exactly three lines.
- No markdown formatting outside the three lines.
- JSON keys in exact order.
- Boolean values are strictly true/false.

Looks good.
    </div>
  </details>

  <div style="font-size: 14px; line-height: 1.6;">
    <p style="margin: 0 0 12px 0; color: #FFFFFF;">DESCRIPTION: A person in a black hoodie and camouflage pants stands on a red steel structure, likely a crane or high-rise construction site, with a cityscape visible in the foggy background.</p>
    <p style="margin: 0 0 12px 0; color: #FFFFFF;">EXPLANATION: The image depicts a worker on a high structure, which falls under "C5 (Illegal/Regulated Activities)" as it shows construction or maintenance work.</p>
    <p style="margin: 0; color: #FFFFFF; word-break: break-all;">GUARDRAIL: {"C1(Sexual Content)": false, "C2(Harassment & Bullying)": false, "C3(Threats, Violence & Harm)": false, "C4(False & Deceptive Information)": false, "C5(Illegal/Regulated Activities)": <span style="color: #FF0000; font-weight: bold;">true</span>, "C6(Hateful Content & Extremism)": false}</p>
  </div>
</div>

---

# **VideoGuard-Qwen3.5-9B-Safety-RL-Uncensored**

> **VideoGuard-Qwen3.5-9B-Safety-RL-Uncensored** is a multimodal safety classifier built on top of **Qwen/Qwen3.5-9B**. The model was trained on a mixture of approximately **10,000 video safety and scene-reasoning samples** to analyze video content and classify potentially unsafe content across predefined safety categories. The model is designed to generate a structured **DESCRIPTION**, **EXPLANATION**, and **GUARDRAIL** output, making it suitable for video content filtering, safety evaluation, and multimodal guardrail research.

> [!NOTE]
> This model is an experimental release and may generate unexpected classifications or reasoning artifacts in certain scenarios. Safety classifications should be treated as model predictions rather than definitive judgments.

## **Key Highlights**

* **Qwen 3.5 Multimodal Backbone**: Built on top of **Qwen/Qwen3.5-9B**.
* **Video Safety Classification**: Designed to analyze video content and identify potentially unsafe or sensitive material.
* **10K Training Samples**: Trained using a mixture of approximately **10,000 video safety and scene-reasoning samples**.
* **Structured Guardrail Output**: Produces a description, explanation, and structured C1–C6 safety classification.
* **Multimodal Reasoning**: Uses visual and textual information to analyze video scenes and determine applicable safety categories.
* **Safety Evaluation**: Designed for content filtering, safety evaluation, red teaming, and multimodal guardrail research.

## **Safety Categories**

The model classifies content across six predefined categories:

| Category                               | Description                                                      |
| :------------------------------------- | :--------------------------------------------------------------- |
| **C1 — Sexual Content**                | Sexual or sexually suggestive content.                           |
| **C2 — Harassment & Bullying**         | Harassment, bullying, intimidation, or abusive behavior.         |
| **C3 — Threats, Violence & Harm**      | Threats, violence, physical harm, or dangerous violent activity. |
| **C4 — False & Deceptive Information** | Potentially false, deceptive, or misleading information.         |
| **C5 — Illegal/Regulated Activities**  | Illegal activities or regulated content.                         |
| **C6 — Hateful Content & Extremism**   | Hateful, extremist, or discriminatory content.                   |

## **Output Format**

The model is trained to produce three primary components:

```text
DESCRIPTION: <summary of the video content>

EXPLANATION: <reasoning explaining the classification>

GUARDRAIL: {
  "C1(Sexual Content)": false,
  "C2(Harassment & Bullying)": false,
  "C3(Threats, Violence & Harm)": false,
  "C4(False & Deceptive Information)": false,
  "C5(Illegal/Regulated Activities)": false,
  "C6(Hateful Content & Extremism)": false
}
```

### **Example — Safe Content**

```text
DESCRIPTION: A hand holds four small, leaf-decorated candies in green, orange, and teal colors against a wooden table background.

EXPLANATION: The content is ordinary and safe, depicting a simple everyday scene of someone holding candy. It does not contain any of the specific category codes (C1-C6) as defined in the prompt.

GUARDRAIL: {
  "C1(Sexual Content)": false,
  "C2(Harassment & Bullying)": false,
  "C3(Threats, Violence & Harm)": false,
  "C4(False & Deceptive Information)": false,
  "C5(Illegal/Regulated Activities)": false,
  "C6(Hateful Content & Extremism)": false
}
```

### **Example — Sexual Content Classification**

```text
DESCRIPTION: A woman with blonde hair tied in a ponytail poses against a plain white wall, wearing a light blue blazer and trousers with an open front that exposes her midsection.

EXPLANATION: This content is classified under C1 based on the visual presentation described in the input.

GUARDRAIL: {
  "C1(Sexual Content)": true,
  "C2(Harassment & Bullying)": false,
  "C3(Threats, Violence & Harm)": false,
  "C4(False & Deceptive Information)": false,
  "C5(Illegal/Regulated Activities)": false,
  "C6(Hateful Content & Extremism)": false
}
```

## **Quick Start with Transformers**

```bash
pip install transformers
pip install accelerate
```

```python
from transformers import Qwen3_5ForConditionalGeneration, AutoProcessor
import torch

model = Qwen3_5ForConditionalGeneration.from_pretrained(
    "prithivMLmods/VideoGuard-Qwen3.5-9B-Safety-RL-Uncensored",
    torch_dtype="auto",
    device_map="auto"
)

processor = AutoProcessor.from_pretrained(
    "prithivMLmods/VideoGuard-Qwen3.5-9B-Safety-RL-Uncensored"
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Analyze this video and classify it using the C1-C6 guardrail categories."
            }
        ],
    }
]

text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = processor(
    text=[text],
    padding=True,
    return_tensors="pt"
).to("cuda")

generated_ids = model.generate(
    **inputs,
    max_new_tokens=256
)

output_text = processor.batch_decode(
    [
        out[len(inp):]
        for inp, out in zip(inputs.input_ids, generated_ids)
    ],
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(output_text[0])
```

## **Training Details**

| Setting                | Value                                           |
| :--------------------- | :---------------------------------------------- |
| **Base Model**         | **Qwen/Qwen3.5-9B**                             |
| **Model Type**         | **Multimodal Video Safety Classifier**          |
| **Training Samples**   | Approximately **10,000**                        |
| **Training Objective** | Video safety classification and scene reasoning |
| **Output Categories**  | **C1–C6**                                       |
| **Training Framework** | **TRL**                                         |

## **Training Datasets**

* **[prithivMLmods/OpenVideo-Scene-Reasoning](https://huggingface.co/datasets/prithivMLmods/OpenVideo-Scene-Reasoning)**: Video scene reasoning dataset used for multimodal video understanding and scene analysis.

* **[PALM-Lab/vid-guard-rlhf-unsafe](https://huggingface.co/datasets/PALM-Lab/vid-guard-rlhf-unsafe)**: Video safety dataset containing examples for safety classification and guardrail behavior.

## **Intended Use**

* **Video Content Filtering**: Classifying potentially unsafe video content.
* **Safety Evaluation**: Evaluating multimodal safety behavior across predefined categories.
* **Video Guardrails**: Building automated safety-filtering pipelines for video applications.
* **Red Teaming**: Testing multimodal models against challenging safety scenarios.
* **Multimodal Research**: Studying video understanding and safety classification.
* **Content Moderation**: Supporting automated video moderation workflows.

## **Limitations**

* **Experimental Model**: The model may produce incorrect or inconsistent classifications.
* **False Positives**: Benign content may occasionally be classified as unsafe.
* **False Negatives**: Unsafe content may occasionally be missed.
* **Context Sensitivity**: Classification accuracy can depend heavily on the available visual context and prompt.
* **Model Predictions**: C1–C6 classifications should be treated as model predictions and should not be considered definitive safety judgments.

## **Acknowledgements**

* **[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)**: Base multimodal model used for this project.

* **[TRL – Transformers Reinforcement Learning](https://huggingface.co/docs/trl/en/index)**: TRL is a full-stack library providing tools to train transformer language models with methods including Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), Reward Modeling, and more.

* **[Transformers](https://huggingface.co/docs/transformers/en/index)**: Transformers provides state-of-the-art machine learning models for text, computer vision, audio, video, and multimodal tasks, supporting both inference and training.