---
license: apache-2.0
base_model:
- Qwen/Qwen3.5-4B
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
  <h1 style="font-size: 24px; font-weight: bold; margin: 0 0 20px 0; color: #FFFFFF;">VideoGuard-4B</h1>
  
  <img src="https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/6Br7g1wrdux8b1DH2_kon.jpeg" alt="demo" style="width: 100%; max-width: 600px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #333333;">

  <details style="background-color: #111111; border: 1px solid #333333; border-radius: 8px; padding: 12px; margin-bottom: 20px; cursor: pointer;">
    <summary style="color: #FFFFFF; font-weight: bold; outline: none;">think</summary>
    <div style="margin-top: 12px; white-space: pre-wrap; color: #FFFFFF; font-size: 13px; line-height: 1.6;">
The user wants me to classify an image and provide a specific output format.
The image shows a young boy peeking over a table with a handgun on it.
I need to check for safety categories:
- C1 (Sexual Content): No.
- C2 (Harassment & Bullying): No.
- C3 (Threats, Violence & Harm): Yes, there is a gun.
- C4 (False & Deceptive Information): No.
- C5 (Illegal/Regulated Activities): Yes, a gun is a regulated item, but usually, this category is for illegal drugs or trafficking. A gun is a weapon, so C3 is more appropriate. However, the prompt says "C5 covers illegal drugs, contraband, weapons trafficking, or other clearly regulated or unlawful activity." A gun is a weapon, so it could fit C5 as well, but C3 is more direct for "weapons pointed at people, physical violence, threats of harm, self-harm, or injury to people or animals." The gun is on a table, not pointed at a person, but it is a weapon. Let's look at the description. The gun is on a table, a boy is behind it. It's a staged photo.
- C6 (Hate symbols, slurs, or content promoting a hateful or extremist ideology): No.

So, C3 is definitely relevant because a weapon is present. C5 might be relevant if we consider guns as regulated activity. The prompt says "C5 covers... weapons trafficking". A gun on a table might be considered a weapon. I will include C3 and maybe C5 if it fits well. The prompt asks for "which category codes apply, if any, and briefly why".
The image is "safe or not" - this is the user's question. I need to answer that in the output.

Line 1: DESCRIPTION: A young boy peeks over a table with a handgun resting on the surface in front of him.
Line 2: EXPLANATION: C3 (Threats, Violence & Harm) is present due to the handgun on the table. C5 (Illegal/Regulated Activities) is relevant as a firearm is a regulated item.
Line 3: GUARDRAIL: {"C1(Sexual Content)": false, "C2(Harassment & Bullying)": false, "C3(Threats, Violence & Harm)": true, "C4(False & Deceptive Information)": false, "C5(Illegal/Regulated Activities)": true, "C6(Hateful Content & Extremism)": false}

Wait, the prompt says "C5 covers illegal drugs, contraband, weapons trafficking, or other clearly regulated or unlawful activity." A gun is a weapon. So C5 is appropriate.
The prompt says "C3 covers weapons pointed at people, physical violence, threats of harm, self-harm, or injury to people or animals." The gun is on a table, not pointed at a person, but it is a weapon. It's a bit ambiguous. But since it's a weapon, C3 is a good fit.
The prompt says "Set a key to true only when the content clearly and directly falls into that category, and false otherwise; do not default to true for merely adjacent or ambiguous themes."
The gun is clearly a weapon. So C3 is true.
The gun is clearly a regulated activity (firearms). So C5 is true.

Let's refine the description.
Line 1: DESCRIPTION: A young boy peeks over a table with a handgun resting on the surface in front of him.
Line 2: EXPLANATION: C3 (Threats, Violence & Harm) is present due to the handgun on the table. C5 (Illegal/Regulated Activities) is relevant as a firearm is a regulated item.
Line 3: GUARDRAIL: {"C1(Sexual Content)": false, "C2(Harassment & Bullying)": false, "C3(Threats, Violence & Harm)": true, "C4(False & Deceptive Information)": false, "C5(Illegal/Regulated Activities)": true, "C6(Hateful Content & Extremism)": false}

Double check the order of keys in GUARDRAIL.
"C1(Sexual Content)", "C2(Harassment & Bullying)", "C3(Threats, Violence & Harm)", "C4(False & Deceptive Information)", "C5(Illegal/Regulated Activities)", "C6(Hateful Content & Extremism)"
Yes, that matches the prompt.

One more check on the description. "A young boy peeks over a table with a handgun resting on the surface in front of him." - good.
One more check on the explanation. "C3 (Threats, Violence & Harm) is present due to the handgun on the table. C5 (Illegal/Regulated Activities) is relevant as a firearm is a regulated item." - good.
One more check on the guardrail. {"C1(Sexual Content)": false, "C2(Harassment & Bullying)": false, "C3(Threats, Violence & Harm)": true, "C4(False & Deceptive Information)": false, "C5(Illegal/Regulated Activities)": true, "C6(Hateful Content & Extremism)": false} - good.

Final check on the output format.
- Three lines.
- Line one begins with "DESCRIPTION: "
- Line two begins with "EXPLANATION: "
- Line three begins with "GUARDRAIL: "
- No markdown formatting.
- No text outside the three lines.

Looks good.
    </div>
  </details>

  <div style="font-size: 14px; line-height: 1.6;">
    <p style="margin: 0 0 12px 0; color: #FFFFFF;">DESCRIPTION: A young boy peeks over a table with a handgun resting on the surface in front of him.</p>
    <p style="margin: 0 0 12px 0; color: #FFFFFF;">EXPLANATION: C3 (Threats, Violence & Harm) is present due to the handgun on the table. C5 (Illegal/Regulated Activities) is relevant as a firearm is a regulated item.</p>
    <p style="margin: 0; color: #FFFFFF; word-break: break-all;">GUARDRAIL: {"C1(Sexual Content)": false, "C2(Harassment & Bullying)": false, "C3(Threats, Violence & Harm)": <span style="color: #FF0000; font-weight: bold;">true</span>, "C4(False & Deceptive Information)": false, "C5(Illegal/Regulated Activities)": <span style="color: #FF0000; font-weight: bold;">true</span>, "C6(Hateful Content & Extremism)": false}</p>
  </div>
</div>

---

# **VideoGuard-Qwen3.5-4B-Safety-RL-Uncensored**

> **VideoGuard-Qwen3.5-4B-Safety-RL-Uncensored** is a multimodal safety classifier built on top of **Qwen/Qwen3.5-4B**. The model was trained on a mixture of approximately **10,000 video safety and scene-reasoning samples** to analyze video content and classify potentially unsafe content across predefined safety categories. The model is designed to generate a structured **DESCRIPTION**, **EXPLANATION**, and **GUARDRAIL** output, making it suitable for video content filtering, safety evaluation, and multimodal guardrail research.

> [!NOTE]
> This model is an experimental release and may generate unexpected classifications or reasoning artifacts in certain scenarios. Safety classifications should be treated as model predictions rather than definitive judgments.

## **Key Highlights**

* **Qwen 3.5 Multimodal Backbone**: Built on top of **Qwen/Qwen3.5-4B**.
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

### **Example — C1 Classification**

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
    "prithivMLmods/VideoGuard-Qwen3.5-4B-Safety-RL-Uncensored",
    torch_dtype="auto",
    device_map="auto"
)

processor = AutoProcessor.from_pretrained(
    "prithivMLmods/VideoGuard-Qwen3.5-4B-Safety-RL-Uncensored"
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
| **Base Model**         | **Qwen/Qwen3.5-4B**                             |
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

* **[Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)**: Base multimodal model used for this project.

* **[TRL – Transformers Reinforcement Learning](https://huggingface.co/docs/trl/en/index)**: TRL is a full-stack library providing tools to train transformer language models with methods including Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), Reward Modeling, and more.

* **[Transformers](https://huggingface.co/docs/transformers/en/index)**: Transformers provides state-of-the-art machine learning models for text, computer vision, audio, video, and multimodal tasks, supporting both inference and training.