---
license: apache-2.0
language:
- en
library_name: transformers
tags:
- qwen
- unsloth
- lora
- psychology
- psychiatry
- clinical-assessment
- mental-health
- text-generation
- medical
base_model: unsloth/Qwen3-32B
datasets:
- Daemontatox/Psy-Data-books
model-index:
- name: Compumacy-Experimental_MF
  results: []
---
![image](./image.jpg)
# Compumacy-Experimental_MF
## A Specialized Language Model for Clinical Psychology & Psychiatry

**Compumacy-Experimental_MF** is an advanced, experimental large language model fine-tuned to assist mental health professionals in clinical assessment and treatment planning. By leveraging the powerful `unsloth/Qwen3-32B` as its base, this model is designed to process complex clinical vignettes and generate structured, evidence-based responses that align with established diagnostic manuals and practice guidelines.

This model is a research-focused tool intended to augment, not replace, the expertise of a licensed clinician. It systematically applies diagnostic criteria from the DSM-5-TR, references ICD-11 classifications, and cites peer-reviewed literature to support its recommendations.

- **Model Developed by:** [Daemontatox](https://huggingface.co/Daemontatox)
- **GitHub:** [Ammar-Alnagar](https://github.com/Ammar-Alnagar)
- **Base Model:** [unsloth/Qwen3-32B](https://huggingface.co/unsloth/Qwen3-32B)
- **Dataset:** [Daemontatox/Psy-Data-books](https://huggingface.co/datasets/Daemontatox/Psy-Data-books)
- **Finetuning Framework:** [Unsloth](https://github.com/unslothai/unsloth)

## Model Description

**Compumacy-Experimental_MF** was fine-tuned using the Unsloth framework for high-performance, memory-efficient training. The model specializes in emulating the reasoning process of a psychiatrist, following a strict, structured format for clinical documentation. It excels at:

1.  **Chief Complaint Analysis:** Objectively summarizing presenting symptoms.
2.  **Differential Diagnosis:** Systematically evaluating potential diagnoses against DSM-5-TR criteria.
3.  **Comprehensive Risk Assessment:** Identifying risks related to suicide, homicide, psychosis, and substance use.
4.  **Evidence-Based Recommendations:** Proposing treatment plans (pharmacotherapy, psychotherapy) based on guidelines from the APA, WFSBP, and NICE.
5.  **Monitoring and Referrals:** Outlining necessary follow-ups and indications for specialized care.

The model's training on the `Daemontatox/Psy-Data-books` dataset, which is composed of professional psychiatric literature, textbooks, and clinical guidelines, enables it to generate responses that are dense with relevant, domain-specific information.

## How to Use

This model is an 8-bit LoRA fine-tune and must be loaded correctly to achieve optimal performance. The use of the **Unsloth** library is highly recommended for faster inference and reduced memory usage.

### Installation

First, ensure you have the necessary libraries installed:

```bash
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps "xformers<0.0.26" trl peft accelerate bitsandbytes
```
### Inference Code

The model requires a specific prompt structure for optimal performance. Please use the Alpaca-style prompt format provided below.

```python
from unsloth import FastLanguageModel
import torch

# Specify max_seq_length for memory efficiency
max_seq_length = 4096 
# Choose a supported dtype (e.g., bfloat16 for A100/H100, float16 for others)
dtype = None 
# Load model in 4bit for consumer GPUs, or 8bit/16bit for more powerful hardware
load_in_4bit = True 

# Load the model and tokenizer from Hugging Face Hub
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "Daemontatox/Compumacy-Experimental_MF",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# Enable PEFT for inference
FastLanguageModel.for_inference(model)

# Define the structured prompt template
alpaca_prompt = """
### Instruction:
You are a licensed psychiatrist AI providing clinical assessments and recommendations.
Apply DSM-5-TR diagnostic criteria systematically, reference ICD-11 classifications, and base all recommendations on peer-reviewed psychiatric literature.
Follow evidence-based practice guidelines (APA, WFSBP, NICE).

Structure your response with:
1) Chief Complaint Analysis - summarize presenting symptoms objectively,
2) Differential Diagnosis - list potential diagnoses with supporting/contradicting criteria,
3) Risk Assessment - evaluate suicide risk, homicide risk, psychosis, substance use, medical emergencies,
4) Clinical Recommendations - evidence-based treatments with specific medications, dosages, therapy modalities,
5) Monitoring Requirements - labs, side effects, therapeutic response timelines,
6) Referral Indications - when specialized care or hospitalization needed.

Safety protocols: Immediately flag suicidal/homicidal ideation, identify psychotic symptoms requiring urgent intervention, recognize medical emergencies (delirium, catatonia, NMS), note substance intoxication/withdrawal risks. Cite specific studies (Author, Year, Journal), reference clinical guidelines with publication dates, include meta-analysis data when available, state confidence levels for recommendations. Specify when in-person evaluation mandatory, identify insufficient information for diagnosis, recommend immediate professional consultation when appropriate. Provide structured clinical documentation with no therapeutic relationship established.

### Input:
{}

### Response:
{}"""

# Your clinical input goes here
clinical_vignette = "A 28-year-old male presents with a 6-month history of persistent low mood, anhedonia, significant weight loss, and early morning awakening. He reports feelings of worthlessness and has intermittent, passive suicidal ideation without a specific plan. He has no prior psychiatric history."

# Format the prompt
inputs = tokenizer(
[
    alpaca_prompt.format(
        clinical_vignette, # Input
        "", # Response - leave empty for generation
    )
], return_tensors = "pt").to("cuda")

# Generate the response
outputs = model.generate(**inputs, max_new_tokens = 2048, use_cache = True)
decoded_output = tokenizer.batch_decode(outputs)

# Print the generated response
print(decoded_output[0])
```

### Training Procedure

This model was fine-tuned on a single NVIDIA A100 80GB PCIe GPU. The training process was optimized for performance and precision using the Unsloth framework.

Frameworks and Libraries

**PyTorch** 

**Hugging Face Transformers**

**PEFT (Parameter-Efficient Fine-Tuning)**

**bitsandbytes (for 8-bit optimization)**

**Unsloth (for 2x faster training and 70% less memory usage)**


### LoRA Configuration

Parameter-Efficient Fine-Tuning was performed using LoRA with the following configuration, targeting a wide range of attention and feed-forward network layers to ensure comprehensive adaptation:
```python
Rank (r): 16

LoRA Alpha (lora_alpha): 16 (scaled learning)

Target Modules: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

Dropout (lora_dropout): 0.1 (for regularization)

Bias: "none"

Rank-Stabilized LoRA (use_rslora): True (enhances training stability and performance)

LoftQ Config: None

Training Hyperparameters

The model was trained for one epoch with carefully selected hyperparameters to ensure stable convergence on the specialized dataset.

Epochs: 1

Learning Rate: 1e-6

Optimizer: adamw_8bit

Weight Decay: 0.05

Batch Size: per_device_train_batch_size=2

Gradient Accumulation: 8 steps (Effective Batch Size: 16)

Warmup Ratio: 0.02

Gradient Checkpointing: "unsloth"

Random State: 42
```

## Ethical Considerations and Limitations

This model is a research preview and is NOT a substitute for a qualified medical or mental health professional.

No Clinical Relationship: The model does not and cannot establish a therapeutic relationship. Its outputs are for informational, educational, and research purposes only.

Verification Required: All outputs, including diagnoses, risk assessments, and treatment plans, must be independently verified by a licensed clinician before being considered for any real-world application.

Data Bias: The model's knowledge is limited to its training data (Daemontatox/Psy-Data-books). This data may contain inherent biases (e.g., cultural, gender, or theoretical orientation). The model may not be suitable for populations or clinical presentations not well-represented in the source material.

Risk of Hallucination: Like all LLMs, this model can hallucinate facts, studies, and clinical details. Citations should be cross-referenced with original sources.

Confidentiality: Do not input any Protected Health Information (PHI) or Personally Identifiable Information (PII) into this model. It is not designed for secure handling of sensitive patient data.

Emergency Situations: This model is not a crisis intervention tool. If you or someone you know is in immediate danger, contact emergency services or a crisis hotline.

## Disclaimer

**The developers of this model are not responsible for any actions taken based on its output. Use of this model is at your own risk. It is intended solely for professionals and researchers in the field of mental health as an experimental tool to supplement, not replace, professional judgment and care. An in-person evaluation by a qualified professional is mandatory for any real-world clinical assessment.**

```Citations
@software{unsloth_2024,
  author = {Daniel Han and Phil Wang and Unsloth AI},
  title = {Unsloth: 5X Faster & 75% Less Memory LLM Finetuning},
  url = {https://github.com/unslothai/unsloth},
  year = {2024}
}

@article{hu2021lora,
  title={LoRA: Low-Rank Adaptation of Large Language Models},
  author={Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
  journal={arXiv preprint arXiv:2106.09685},
  year={2021}
}

@article{qwen_team_2024,
  title={Qwen Technical Report},
  author={Qwen Team},
  journal={arXiv preprint arXiv:2309.16609},
  year={2024}
}

@training{Compumacy AI,
  author{Ammar-Alnagar and Compumacy AI},
  url{https://github.com/Ammar-Alnagar},
  year{2025}
}