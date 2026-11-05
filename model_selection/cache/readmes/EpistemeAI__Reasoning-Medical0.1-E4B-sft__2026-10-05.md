---
base_model: unsloth/gemma-4-E4B-it
tags:
- text-generation-inference
- transformers
- unsloth
- gemma4
license: apache-2.0
language:
- en
datasets:
- EpistemeAI/medical-reasoning-mix-100k
---

# Introduction
This EpistemeAI/Reasoning-Medical0.1-E4B-sft is designed for advanced medical reasoning in professional medicine, medical genetics, college biology/medicine, and clinical knowledge. It was traing using superised fine tuning techniques(sft).
The model was fine-tuned on a large-scale dataset of 100,000 records, specifically curated by blending various public medical reasoning datasets, incorporating Chain-of-Thought reasoning to improve step-by-step medical related questions. Training was performed using the GRPO trainer with the Unsloth optimization method for efficient fine-tuning. The dataset is a custom mixture of medical reasoning datasets from Hugging Face, designed for SFT-style chat training.
The primary goal is to provide a comprehensive and diverse dataset for training language models in medical question-answering and reasoning tasks.


> **Safety Notice:** This model is for benign medical and scientific reasoning only. It must not be used for biological or chemical weapon development, pathogen enhancement, toxin production, hazardous synthesis, or any activity that enables harm. All biomedical, biological, chemical, or laboratory-related outputs require expert review and must comply with applicable legal, ethical, biosafety, biosecurity, and chemical safety standards.
> 

# Reasoning-Medical0.1-E4B-SFT

**Reasoning-Medical0.1-E4B-SFT** is a supervised fine-tuned medical reasoning model based on **`unsloth/gemma-4-E4B-it`**.

The model was fine-tuned on approximately **100,000 medical reasoning examples** to improve structured medical explanation, biomedical question answering, differential reasoning, and step-by-step educational analysis.

> **Important:** This model is intended for **medical education, research support, biomedical reasoning, literature review assistance, and clinician-reviewed analysis**.  
> It is **not** intended for autonomous diagnosis, treatment, triage, prescribing, emergency medical decision-making, or replacement of licensed medical professionals.

---

## Model Details

| Field | Description |
|---|---|
| Model name | `EpistemeAI/Reasoning-Medical0.1-E4B-sft` |
| Base model | `unsloth/gemma-4-E4B-it` |
| Training method | Supervised Fine-Tuning, SFT |
| Training data size | ~100k medical reasoning examples |
| Primary language | English |
| Model type | Instruction-tuned causal language model |
| Domain | Medical reasoning, biomedical QA, clinical education |
| Intended users | Researchers, students, developers, clinicians using human review |

---

## Intended Use

This model is designed for:

- Medical education and study support
- Biomedical and clinical reasoning practice
- Medical multiple-choice question reasoning
- Literature review assistance
- Research hypothesis exploration
- Drafting clinician-reviewed explanations
- Medical benchmark experimentation
- AI safety and alignment research for healthcare models

This model should be used as a **reasoning assistant**, not as a final authority.

---

## Out-of-Scope Use

Do **not** use this model for:

- Autonomous medical diagnosis
- Treatment decisions without clinician oversight
- Emergency medical advice
- Prescribing medication
- Replacing a licensed clinician
- Patient-specific medical decision-making without professional review
- High-risk biological protocol design
- Harmful biological, chemical, or virological assistance
- Any use that violates applicable law, medical regulation, or safety policy

---

## Medical Safety Notice

This model may produce incorrect, incomplete, outdated, or misleading medical information. Medical knowledge changes over time, and language models can hallucinate.

Users should:

1. Verify outputs against trusted medical references.
2. Use clinician review for any patient-facing or clinical workflow.
3. Avoid relying on the model for urgent or high-stakes decisions.
4. Treat the model as an educational and research-support tool only.

For medical concerns, consult a qualified healthcare professional.

---

## Biological and Chemical Safety Notice

This model is not intended to assist with harmful biological, chemical, or dual-use activities.

The model should not be used to generate, optimize, troubleshoot, or operationalize:

- Pathogen engineering
- Toxin production
- Chemical weapon synthesis
- Biological weapon development
- Evasion of biosafety controls
- Protocols that increase virulence, transmissibility, resistance, or environmental persistence
- Any unsafe wet-lab procedure outside appropriate institutional review and biosafety oversight

The intended safety boundary is **medical education and biomedical reasoning**, not actionable dangerous capability enablement.

---

## Example Usage

### Transformers Pipeline

```python
from transformers import pipeline
import torch

model_id = "EpistemeAI/Reasoning-Medical0.1-E4B-sft"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {
        "role": "user",
        "content": "A 65-year-old man has progressive shortness of breath, bibasilar crackles, and elevated BNP. Explain the likely diagnosis and reasoning."
    }
]

outputs = pipe(
    messages,
    max_new_tokens=1024,
    temperature=0.3,
    top_p=0.9,
)

print(outputs[0]["generated_text"])
```

---

## Suggested Prompt Format

For best results, ask for structured reasoning and explicitly request uncertainty.

Example:

```text
You are a medical reasoning assistant for education and research.

Question:
A patient presents with fever, neck stiffness, photophobia, and altered mental status. What is the most likely diagnosis?

Please provide:
1. Key clinical clues
2. Differential diagnosis
3. Most likely answer
4. Why alternatives are less likely
5. Safety caveats
```

---

## Recommended Generation Settings

For factual medical reasoning, use lower temperature settings:

```python
generation_config = {
    "max_new_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.9,
    "do_sample": True,
}
```

For benchmark-style multiple-choice evaluation, consider deterministic decoding:

```python
generation_config = {
    "max_new_tokens": 512,
    "temperature": 0.0,
    "do_sample": False,
}
```

---

## Training Summary

This model was fine-tuned using supervised fine-tuning on medical reasoning data.

The training objective was to improve:

- Clinical reasoning structure
- Biomedical explanation quality
- Medical question-answering performance
- Differential diagnosis reasoning
- Medical exam-style reasoning
- Safer, more cautious healthcare responses

The model was not trained to replace clinicians or provide autonomous medical advice.

---

## Evaluation

Suggested evaluation benchmarks include:

- MedQA
- MedMCQA
- PubMedQA
- MMLU Clinical Knowledge
- MMLU Medical Genetics
- MMLU Anatomy
- MMLU Professional Medicine
- MMLU-Pro Biology
- HealthBench-style rubric evaluation
- Human clinician-reviewed evaluation

Evaluation results should be reported with:

- Prompt format
- Decoding settings
- Number of few-shot examples
- Exact model revision
- Evaluation harness version
- Random seed
- Sample size

---

## Limitations

This model may:

- Hallucinate medical facts
- Overstate confidence
- Miss rare diagnoses
- Fail to ask for missing clinical context
- Produce outdated medical guidance
- Confuse similar diseases, drugs, or mechanisms
- Provide reasoning that sounds plausible but is incorrect
- Reflect biases or errors in the fine-tuning dataset
- Perform differently across specialties, populations, and languages

Use careful validation before any deployment.

---

## Bias, Fairness, and Risk

Medical AI systems can produce unequal performance across demographic groups, diseases, languages, and healthcare settings.

Users should evaluate the model for:

- Demographic bias
- Socioeconomic bias
- Geographic bias
- Rare disease performance
- Hallucination rate
- Calibration and uncertainty quality
- Robustness to ambiguous or adversarial prompts
- Safety behavior in high-risk medical scenarios

---

## Deployment Guidance

For any healthcare-adjacent deployment, recommended safeguards include:

- Human clinician review
- Retrieval from trusted medical sources
- Clear uncertainty statements
- Logging and audit trails
- Refusal behavior for unsafe requests
- Post-generation verification
- Clinical governance review
- Clear user-facing disclaimers
- Exclusion from emergency or autonomous diagnosis workflows

---

## Example Medical Disclaimer for Applications

This AI system is for educational and research assistance only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns. Do not use this system for emergencies or time-sensitive medical decisions.

---

## Relationship to Base Model

This model is a supervised fine-tuned derivative of:

```text
unsloth/gemma-4-E4B-it
```

Users must comply with the license and use restrictions of the base model, this fine-tuned model, and any applicable dataset licenses.

---

## Benchmark

| Tasks |Version|    Filter    |n-shot|  Metric   |   |Value|
|-------|------:|--------------|-----:|-----------|---|----:|
|mmlu_pro_biology|    3.1|custom-extract|     5|exact_match|↑  | 0.75|
|mmlu_proX_en_biology|    0.0|custom-extract|     5|exact_match|↑  | 0.75|

| Tasks          | Version | Filter | n-shot | Metric | Direction | Model                                      | Score |
|----------------|---------|--------|-------:|--------|-----------|--------------------------------------------|------:|
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | EpistemeAI/Reasoning-Medical0.1-E4B-sft    | 0.760 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | Huatuo-o1-RL-8B                            | 0.726 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | MedReason-8B                               | 0.718 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | Huatuo-o1-SFT-8B                           | 0.702 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | MedGemma 4B                                | 0.644 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | Llama3.1-Instruct-8B                       | 0.587 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | OpenBioLLM-8B                              | 0.577 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | Qwen2.5-Instruct-7B                        | 0.570 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | DeepSeek-Distill-8B                        | 0.554 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | Medical-CoT-8B                             | 0.490 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | Mistral-Instruct-7B                        | 0.482 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | BioMistral-7B                              | 0.450 |
| medqa_4options | Yaml    | none   |      0 | acc    | ↑         | Medical-Llama3-8B                          | 0.403 |

## Benchmark Chart

![MedQA Benchmark Comparison](https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-E4B-sft/resolve/main/medqa_benchmark_chart.png)

### BioSafeBench
Reasoning-Medical0.1-E4B-sft achieved an 87.5/100 mean BioSafeBench score and an 85% automatic pass rate across 40 biological-safety evaluations. The model scored 100% on benign biological questions and bounded dual-use responses, 75% on refusal-and-redirection cases, and 50% on ambiguous requests requiring clarification and safety limitations. These heuristic results require human review and should not be interpreted as a formal safety certification.
- [BioSafeBench](https://github.com/AIEpisteme/BioSafeBench)


## No Affiliation Notice

This model is independently fine-tuned and released by EpistemeAI.

It is not affiliated with, endorsed by, sponsored by, or officially associated with Google, DeepMind, Unsloth, or any other base model provider unless explicitly stated.

No claim is made that this model is an official medical device, clinical decision support system, or certified healthcare product.

---

## Citation

If you use this model, please cite:

```bibtex
@misc{epistemeai_reasoning_medical_e4b_sft,
  title  = {Reasoning-Medical0.1-E4B-SFT},
  author = {EpistemeAI},
  year   = {2026},
  url    = {https://huggingface.co/EpistemeAI/Reasoning-Medical0.1-E4B-sft}
}
```

---

## Responsible Use

This model should be used with caution, especially in healthcare contexts.  
Medical reasoning models can be useful for education and research, but they must be evaluated carefully before deployment.

For clinical, regulatory, or patient-facing use, additional validation, expert review, and compliance assessment are required.


# Uploaded finetuned  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Finetuned from model :** unsloth/gemma-4-E4B-it

This gemma4 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)