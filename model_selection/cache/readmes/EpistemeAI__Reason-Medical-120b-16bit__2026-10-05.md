---
base_model: unsloth/gpt-oss-120b-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- gpt_oss
license: apache-2.0
language:
- en
---
# Introduction
This 16bit version of EpistemeAI/Reasoning-Medical-120B models, it is fine tuned version of the OpenAI's gpt-oss-120b. These models designed for advanced medical reasoning in professional medicine, medical genetics, college biology/medicine, and clinical knowledge.
The model was fine-tuned on a large-scale dataset of 100,000 high-quality question-and-answer examples, incorporating Chain-of-Thought reasoning to improve step-by-step problem solving. Training was performed using the SFT (Supervised fine tuning) trainer with the Unsloth optimization method for efficient fine-tuning.

> **Safety Notice:** This model is for benign medical and scientific reasoning only. It must not be used for biological or chemical weapon development, pathogen enhancement, toxin production, hazardous synthesis, or any activity that enables harm. All biomedical, biological, chemical, or laboratory-related outputs require expert review and must comply with applicable legal, ethical, biosafety, biosecurity, and chemical safety standards.
> 

# Reasoning-Medical-20B

## Model Summary

**Reasoning-Medical-20B** is a medical reasoning language model fine-tuned from `openai/gpt-oss-120b`. The model is designed for biomedical question answering, medical reasoning research, clinical knowledge evaluation, and safety-aligned medical assistant experiments.

This model is intended for **research and development use only**. It is not intended to directly provide clinical diagnosis, treatment decisions, medication dosing, patient management instructions, or emergency medical guidance.

## Model Type

This model is a **decoder-only Transformer causal language model** based on `openai/gpt-oss-120b`.

The base architecture uses:

* `model_type`: `gpt_oss`
* `architectures`: `GptOssForCausalLM`
* Task type: causal language modeling / text generation
* Architecture family: sparse Mixture-of-Experts language model
* Base model: `openai/gpt-oss-120b`

## Intended Use

This model may be useful for:

* Biomedical research question answering
* Medical exam-style reasoning
* Medical benchmark evaluation
* Clinical knowledge retrieval experiments
* Differential diagnosis reasoning research
* Medical education support
* Safety-aligned medical AI research

## Out-of-Scope Use

This model should **not** be used for:

* Direct clinical diagnosis
* Direct patient treatment planning
* Medication dosage recommendations
* Emergency medical decision-making
* Replacing a licensed medical professional
* Autonomous clinical triage
* High-stakes patient management without expert review

All outputs should be treated as **preliminary**, require independent verification, and should be reviewed by qualified medical professionals before any real-world clinical application.

## Training Details

The model was fine-tuned from `openai/gpt-oss-20b` using a medical reasoning dataset containing high-quality question-answer examples.

Training may include one or more of the following stages:

1. Supervised fine-tuning on 100,000 high-quality medical question-answer examples

## Training Data

Training Dataset

This model was fine-tuned using:

* Dataset: lingshu-medical-mllm/ReasonMed
* Dataset type: medical reasoning question-answer dataset
* Language: English
* License: Apache-2.0
* Task categories: question answering and text generation
* Domain: medical reasoning, biomedical knowledge, clinical-style QA
* Format: question-answer examples with reasoning-oriented responses

ReasonMed is a large-scale medical reasoning dataset containing high-quality medical question-answer examples with multi-step reasoning rationales and concise answer summaries. It was generated and curated through a multi-agent pipeline designed to improve correctness, logical coherence, and medical factuality.

## Safety Alignment

This model should be aligned to prefer responses that:

* Express uncertainty when appropriate
* Avoid unsupported medical claims
* Recommend professional medical consultation for serious symptoms
* Avoid definitive diagnosis without sufficient context
* Avoid medication dosage or prescription advice
* Refuse unsafe medical, biological, or harmful instructions
* Provide safe, educational, and non-actionable alternatives when needed

Safety tuning may include DPO-style preference pairs where the chosen answer is safer, more cautious, and more clinically appropriate than the rejected answer.

## Example Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "EpistemeAI/Reason-Medical-120b-16bit"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto"
)

messages = [
    {
        "role": "system",
        "content": "You are a careful medical reasoning assistant. Provide educational information only. Do not provide definitive diagnosis or treatment."
    },
    {
        "role": "user",
        "content": "How can bacterial pneumonia be differentiated from viral pneumonia?"
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=512,
    temperature=0.2,
    top_p=0.9,
    do_sample=True
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Recommended Prompt Format

```text
Reasoning: high.

You are a careful medical reasoning assistant. Your response is for educational and research purposes only. Do not provide a final clinical diagnosis, prescription, dosage, or treatment plan. Explain uncertainty, red flags, and when to seek professional medical care.

Question:
{user_question}
```

## Evaluation

The model should be evaluated on both capability and safety benchmarks.

Suggested evaluation categories:

| Category             | Example Benchmarks                                 |
| -------------------- | -------------------------------------------------- |
| Medical QA           | MedQA, MedMCQA, PubMedQA                           |
| Biomedical reasoning | MMLU medical subsets, MMLU-Pro biology/medicine    |
| Clinical safety      | Custom unsafe-medical-advice tests                 |
| Hallucination        | Citation and factuality checks                     |
| Refusal behavior     | Unsafe medical, biosecurity, and self-harm prompts |
| Calibration          | Uncertainty and confidence evaluation              |

Current reported results:

| Benchmark    | R-M-120B            | gpt-20b                      |
| ------------ | -----------------: | ---------------------------- |
| MedQA        |                 | 62                           |
| HealthBench  |                | 42.5                         |

## Limitations

This model may:

* Produce incorrect or hallucinated medical information
* Overstate confidence
* Miss rare diagnoses or uncommon clinical presentations
* Fail to identify emergency symptoms
* Provide incomplete differential diagnoses
* Reflect biases present in the training data
* Perform differently across demographic groups, specialties, and clinical contexts

The model is not a substitute for professional medical judgment.

## Medical Disclaimer

The outputs generated by this model are not intended to directly inform clinical diagnosis, patient management decisions, treatment recommendations, or any other direct clinical practice application. Performance benchmarks highlight baseline capabilities on relevant tasks, but inaccurate model output is possible. All outputs should be considered preliminary and require independent verification, clinical correlation, and further investigation through established research and development methodologies.

If you are experiencing a medical emergency, contact emergency services or a qualified healthcare professional immediately.

## Ethical Considerations

Users should carefully consider the risks of deploying medical AI systems in real-world settings. This model should be used with human oversight, transparent limitations, evaluation against clinically relevant safety tests, and appropriate governance.

Developers should avoid using the model in workflows where incorrect outputs could directly harm patients.

## Citation

If you use this model, please cite the base model and this fine-tuned model.

```bibtex
@misc{reasoningmedical20b,
  title = {Reasoning-Medical-20B},
  author = {EpistemeAI},
  year = {2026},
  publisher = {Hugging Face},
  note = {Fine-tuned from openai/gpt-oss-20b}
}
```

## License

This model is released under the Apache-2.0 license unless otherwise specified by the fine-tuning data, adapter weights, or downstream distribution requirements.

Users are responsible for ensuring that their use complies with the base model license, dataset licenses, and applicable laws or regulations.

## Contact

For questions, issues, or research collaboration, contact:

* Organization: EpistemeAI
* Hugging Face: `EpistemeAI`


# Uploaded finetuned  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Finetuned from model :** unsloth/gpt-oss-120b-unsloth-bnb-4bit

This gpt_oss model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
