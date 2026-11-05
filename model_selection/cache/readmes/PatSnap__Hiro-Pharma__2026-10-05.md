---
license: apache-2.0
language:
  - zh
  - en
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-7B
tags:
  - qwen
  - qwen2.5
  - qwen2
  - causal-lm
  - text-generation
  - chat
  - biomedical
  - sft
  - reinforcement-learning
  - grpo
  - verl
  - verl-0.3.1.dev
  - safetensors
---

# Hiro-Pharma

## Model Description

Hiro-Pharma is a causal language model based on `Qwen/Qwen2.5-7B`.
It is released in `safetensors` format under the Apache 2.0 license.

The model was trained with internally generated synthetic data and is intended for biomedical-domain dialogue, assistant-style interaction, and research evaluation.

## Model Details

- Base model: `Qwen/Qwen2.5-7B`
- Architecture: Qwen2 causal language model
- Context length: up to 131,072 tokens, depending on runtime and hardware
- Tensor type: BF16
- Format: sharded `safetensors`
- License: Apache 2.0

## Intended Use

This model is intended for biomedical-domain dialogue and assistant-style text generation.

Suitable use cases may include:

- Biomedical and pharmaceutical-domain conversational assistance
- Summarization, rewriting, and explanation of biomedical text
- Research, development, and engineering evaluation of biomedical dialogue systems
- Internal productivity assistance for non-clinical biomedical literature, terminology, and workflow exploration
- Deployment behind an application layer that provides logging, monitoring, retrieval controls, safety filters, and human review

## Out-of-Scope Use

This model should not be used for:

- Illegal, harmful, or deceptive activities
- Privacy-invasive profiling or surveillance
- Clinical diagnosis, treatment planning, prescription decisions, triage, disease prevention decisions, or patient-specific medical advice
- Emergency, urgent-care, or life-threatening situations
- Fully automated high-stakes decisions in medical, legal, financial, employment, insurance, regulatory, or similar settings
- Patient-facing medical advice without qualified professional review and appropriate regulatory assessment
- Interpretation of medical images, lab results, pathology, genomic data, medical-device signals, or other patient data for clinical action
- Regulatory submissions, pharmacovigilance decisions, adverse-event assessment, clinical trial eligibility, or quality-system decisions without domain expert review
- Generating or distributing harmful instructions, malware, or disallowed content

## Training Data

The model was trained or fine-tuned on internally generated synthetic biomedical-domain dialogue data.
The synthetic data includes objective-question examples and question-answer dialogue examples.

The released checkpoint does not include the internal synthetic training set, proprietary evaluation sets, client documents, patient records, or other private source materials.

Data handling notes:

- The training data does not include customer-confidential data.
- The training data does not include real patient private or protected health information.
- The synthetic training data is not released with this model checkpoint.
- Users should not infer that the model contains or grants access to any proprietary biomedical corpus, clinical dataset, patient record, customer document, or internal evaluation set.

## Training Procedure

Hiro-Pharma was trained with supervised fine-tuning (SFT) followed by reinforcement learning (RL).
The RL stage primarily used Group Relative Policy Optimization (GRPO).

The RL reward design included:

- Rule-based rewards
- Model-based rewards

Training framework:

- `verl` 0.3.1.dev

Additional hyperparameters, hardware details, training duration, and internal evaluation details are not disclosed in this model card.

## Evaluation

Public benchmark results are not included in this model card.
The model should be evaluated by users on their own biomedical dialogue tasks, terminology requirements, safety requirements, and deployment environment before production use.

Recommended evaluation dimensions include:

- Biomedical factuality and citation-groundedness, if retrieval is used
- Terminology accuracy and consistency
- Instruction following
- Refusal behavior for clinical, patient-specific, or high-risk requests
- Hallucination rate
- Robustness to ambiguous, incomplete, or adversarial prompts
- Human expert review for professional or high-impact workflows

## Limitations

The model may generate inaccurate, outdated, biased, incomplete, hallucinated, or unsafe biomedical content.
Users should evaluate the model carefully before deploying it in production, especially when the output may influence professional, scientific, regulatory, or health-related decisions.

Known limitations:

- The model may produce plausible but incorrect pharmaceutical, biomedical, or medical information.
- The model may fail to distinguish established clinical evidence from hypotheses, preclinical findings, synthetic examples, or unsupported claims.
- The model may omit uncertainty, contraindications, adverse events, population-specific factors, or jurisdiction-specific regulatory requirements.
- The model is not validated as a medical device, clinical decision support system, diagnostic system, treatment-planning system, pharmacovigilance system, or regulated healthcare product.
- The model's behavior depends on prompts, decoding parameters, surrounding application logic, retrieval sources, and post-processing.

## Biomedical Use Disclaimer

Hiro-Pharma is provided for research, development, engineering evaluation, and productivity assistance in biomedical-domain dialogue systems.
It is not a physician, pharmacist, medical professional, medical device, clinical decision support system, diagnostic tool, treatment-planning tool, pharmacovigilance system, or substitute for qualified professional judgment.

The model and its outputs do not provide medical advice, diagnosis, prognosis, treatment recommendations, prescription guidance, dosing instructions, patient triage, emergency guidance, regulatory advice, legal advice, or professional healthcare services.
Any biomedical or medical information generated by the model may be inaccurate, incomplete, outdated, inconsistent, biased, unsafe, or unsuitable for a particular patient, population, disease area, jurisdiction, product, study, or use case.

Users are solely responsible for reviewing, validating, and contextualizing all inputs and outputs before relying on them.
Outputs must be reviewed by appropriately qualified professionals before being used in research reports, clinical workflows, patient communication, medical education, product decisions, regulatory submissions, pharmacovigilance workflows, clinical trial workflows, commercial materials, or any other professional or high-impact context.
The model should not be used in emergency or urgent-care situations; users should seek qualified medical help through appropriate channels.

Users must ensure that they have all necessary rights, permissions, consents, and legal bases before processing any data with this model.
Do not submit or process protected health information, personal data, patient records, clinical trial subject data, unpublished research, confidential business information, trade secrets, client materials, proprietary datasets, third-party corpora, or regulated data unless you are authorized to do so and have implemented appropriate privacy, security, confidentiality, compliance, and governance controls.

Users are responsible for complying with applicable laws, regulations, institutional policies, contractual obligations, and professional standards, including those related to healthcare, medical devices, clinical decision support, data protection, cybersecurity, intellectual property, export control, sanctions, biological safety, pharmaceutical regulation, advertising, pharmacovigilance, and clinical research.

The maintainers do not represent that this model has been reviewed, cleared, approved, certified, or validated by any healthcare, pharmaceutical, medical-device, regulatory, or professional authority.
No rights are granted to any proprietary biomedical corpus, clinical dataset, patient record, evaluation set, terminology database, confidential document, or third-party material unless expressly stated otherwise.

This model is provided "AS IS" and "AS AVAILABLE", without warranties of any kind.
To the maximum extent permitted by applicable law, the maintainers and contributors disclaim liability for any claims, damages, losses, liabilities, regulatory consequences, professional consequences, or other harms arising from access to, deployment of, modification of, redistribution of, or reliance on this model or any outputs generated by it.

## Usage

Install dependencies:

```bash
pip install -U transformers accelerate safetensors
```

Load the model:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "wwwuwentao/Hiro-Pharma"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Please introduce yourself briefly."},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

with torch.no_grad():
    generated_ids = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.8,
        repetition_penalty=1.05,
    )

generated_ids = generated_ids[:, inputs.input_ids.shape[-1]:]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

## Citation

If you use this model, please cite the following paper:

```bibtex
@article{wu2025large,
  title   = {Large Language Model's Multi-Capability Alignment in Biomedical Domain},
  author  = {Wu, Wentao and Chen, Linqing and Zhong, Hanmeng and Wang, Weilei},
  journal = {arXiv preprint arXiv:2508.04278},
  year    = {2025}
}
```

## License

This model is released under the Apache License 2.0.
It is based on `Qwen/Qwen2.5-7B`, which is also released under the Apache License 2.0.
