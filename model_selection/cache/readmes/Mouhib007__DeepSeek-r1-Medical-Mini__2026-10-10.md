---
library_name: transformers
tags:
- unsloth
- trl
- sft
- llm
- deepseek
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
base_model:
- unsloth/DeepSeek-R1-Distill-Llama-8B
---


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This model is a fine-tuned version of the unsloth/DeepSeek-R1-Distill-Llama-8B model, specifically adapted for medical reasoning tasks. The fine-tuning process utilized the FreedomIntelligence/medical-o1-reasoning-SFT dataset, which focuses on complex chain-of-thought (CoT) reasoning in the medical domain. The model has been optimized using the unsloth and trl libraries, with LoRA (Low-Rank Adaptation) techniques applied to enhance performance while maintaining efficiency.
- **Developed by:** [Mohamed Mouhib Naffeti]
- **Finetuned from model:** [unsloth/DeepSeek-R1-Distill-Llama-8B]

### Model Sources

<!-- Provide the basic links for the model. -->

- **Demo :** https://www.kaggle.com/code/mohamednaffeti007/fine-tune-deepseek-model

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
This model is intended for use in medical reasoning tasks, particularly those requiring complex chain-of-thought reasoning. It can be used to generate responses to medical questions, provide explanations, and assist in medical decision-making processes.

### Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
The model can be further fine-tuned for specific medical subdomains or integrated into larger healthcare applications, such as diagnostic tools, medical chatbots, or educational platforms.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
This model is not intended for use in high-stakes medical decision-making without human oversight. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
The model may inherit biases present in the training data, which could affect its performance on certain medical topics or populations. Additionally, the model's responses should be carefully validated, as it may generate incorrect or misleading information.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should be aware of the model's limitations and validate its outputs, especially in critical medical scenarios. It is recommended to use the model in conjunction with human expertise and to continuously monitor its performance.

#### Training Hyperparameters

Training regime: Mixed precision (fp16/bf16)

Batch size: 2 per device

Gradient accumulation steps: 4

Epochs: 1

Learning rate: 2e-4

Optimizer: AdamW 8-bit

Weight decay: 0.01

Warmup steps: 5

Max steps: 60

LoRA configuration:

Rank (r): 16

Alpha: 16

Dropout: 0

Target modules: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->
you'll find the metrics result here : https://wandb.ai/contact-mohamednaffeti-isimm/Fine-Tune-DeepSeek-Model-R1%20On%20Medical%20Dataset/runs/evop6kph?nw=nwusercontactmohamednaffeti

## Model Card Contact

### contact.mohamednaffeti@gmail.com