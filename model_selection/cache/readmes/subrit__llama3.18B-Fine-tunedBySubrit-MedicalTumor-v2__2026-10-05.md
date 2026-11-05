---
license: llama3.1
language:
- en
base_model:
- meta-llama/Llama-3.2-1B
tags:
- medical
---
# MedBrain-Llama-3.1-8B Medical Brain Tumor QA

## Model Description

This is a Fine-tuned & merged 16-bit medical language model built on top of Meta Llama 3.1 8B and specialized for brain tumor knowledge, neurology-focused medical question answering, and clinical decision-support style responses. The model was fine-tuned for instruction-following behavior on public medical datasets and then exported as a 16-bit checkpoint for straightforward inference and deployment.

### Key Features

- 🧠 Specialized for brain tumor, neurology, and medical decision-making style prompts
- 📚 Covers diagnostic reasoning, treatment overview, imaging-related discussion, and safety-oriented patient guidance
- ⚕️ Helpful for educational medical Q&A, clinical support prototyping, and domain-specific assistants
- 👤 Developed by Subrit Dikshit
- ⚡ Merged 16-bit checkpoint for direct loading with Transformers
- 🎯 Production-friendly export with tokenizer, config, generation config, and safetensor shards included

---

## Model Details

### Model Information

- **Developed by:** Subrit Dikshit
- **Model type:** Causal Language Model (Fine-tuned, merged 16-bit)
- **Base Model:** [Llama-3.1-8B)
- **Merged Export:** 16-bit merged model
- **Language:** English
- **Domain:** Medical QA, Brain Tumor Knowledge, Clinical Decision Support
- **License:** Llama 3.1 license terms apply from the base model
- **Training Method:** QLoRA + merged 16-bit export
- **Parameters:** 8B class base model with LoRA fine-tuning merged into final weights

### Training Configuration

**LoRA Configuration**
- Rank (r): 16
- Alpha: 16
- Target modules: `["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]`
- Dropout: 0.0
- Bias: none
- Gradient checkpointing: enabled

**Training Setup**
- Sequence length: 512
- Per-device batch size: 1
- Gradient accumulation steps: 8
- Learning rate: 2e-4
- Optimizer: `adamw_8bit`
- Scheduler: cosine
- Save strategy: every 50 steps
- Final training artifacts include checkpoints, validation logs, and merged export

**Hardware**
- GPU: Kaggle T4

---

## Dataset

The model was fine-tuned on a medical instruction-style dataset mixture with emphasis on neurology and tumor-related topics.

### Training Data Sources

- **Medical Flashcards:** `medalpaca/medical_meadow_medical_flashcards`
- **Medical QA:** `medalpaca/medical_meadow_medqa`

### Dataset Focus

The training mixture emphasizes:
- Brain tumor concepts
- Neurology and neuro-oncology terminology
- Clinical decision-making style prompts
- Symptoms, diagnosis, and treatment overviews
- MRI and imaging-related explanations
- Patient-safety aligned medical responses

### Dataset Topics

- Brain tumor warning signs and red flags
- Glioma, meningioma, pituitary adenoma, metastasis
- Seizures, headaches, nausea, focal deficits
- MRI and CT discussion
- Differential diagnosis and diagnostic workup
- Treatment planning, surgery, radiotherapy, chemotherapy
- General medical exam-style reasoning
- Medical safety disclaimers and clinician escalation guidance

### Total

- Approximate formatted training examples: **48,495**

---

## Usage

### Installation

```bash
pip install transformers torch accelerate sentencepiece
```

### Loading the Model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "subrit/MedBrain-Llama-3.1-8B-Medical"  # change if your repo name differs

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)
```

### Inference

```python
def generate_answer(question, max_new_tokens=256):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a specialized medical AI assistant for brain tumor knowledge "
                "and clinical decision-making. Provide careful, educational responses "
                "and remind users to consult licensed medical professionals."
            )
        },
        {"role": "user", "content": question}
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=True
    )

    answer = tokenizer.decode(outputs, skip_special_tokens=True)
    return answer

question = "What are the common early warning signs of a brain tumor?"
print(generate_answer(question))
```

### Recommended Inference Parameters

```python
generation_config = {
    "max_new_tokens": 256,
    "temperature": 0.7,
    "top_p": 0.9,
    "do_sample": True,
    "repetition_penalty": 1.1,
}
```

### Suggested Prompt Style

```text
You are a specialized medical AI assistant. Explain the early warning signs of a brain tumor and when urgent medical evaluation is needed.
```

---

## Performance

### Validation Summary

This release includes qualitative validation on representative medical prompts rather than a formal clinical benchmark.

### Validation Coverage

The model was tested on prompts covering:
- Brain tumor warning signs
- Clinical diagnostic workup
- Treatment comparison
- MRI interpretation style questions
- Medical safety and patient guidance

### Training Artifacts

Available artifacts include:
- `training_metrics.json`
- `validation_results.json`
- periodic checkpoints
- merged 16-bit export

### Example Prompt Types

**Q:** "What are the common early warning signs of a brain tumor?"  
**A:** The model is expected to discuss headaches, seizures, nausea, neurological changes, and the need for proper medical imaging and physician evaluation.

**Q:** "Compare first-line treatments for glioblastoma and meningioma."  
**A:** The model is expected to outline surgery, radiotherapy, chemotherapy, and case-dependent differences in treatment planning.

**Q:** "Can someone self-diagnose a brain tumor using symptoms online?"  
**A:** The model is expected to discourage self-diagnosis and advise consultation with qualified healthcare professionals.

---

## Limitations and Ethical Considerations

### Limitations

- ⚠️ **Not Medical Advice:** This model is for research, education, and prototyping only.
- ⚠️ **Text-Only Model:** It cannot directly read MRI, CT, histopathology, or other medical images.
- ⚠️ **Public Dataset Limits:** The training data is public and may not reflect the latest clinical guidelines or institutional protocols.
- ⚠️ **Hallucination Risk:** The model may generate plausible but incorrect medical information.
- ⚠️ **No Clinical Validation:** This release should not be treated as a validated medical device or diagnostic system.
- ⚠️ **Domain Drift:** It performs best on medical QA and brain tumor related prompts, and may degrade outside those areas.
- ⚠️ **Post-Processing May Help:** Safety layers, output cleanup, retrieval, and human review are recommended in production systems.

### Ethical Considerations

- **Professional Use:** Always verify outputs with licensed clinicians and trusted medical sources.
- **Safety:** Do not use this model as the sole basis for diagnosis, treatment, or emergency triage.
- **Bias:** The model may reflect biases and omissions present in public medical training data.
- **Responsible Deployment:** Human review, guardrails, and clear disclaimers are strongly recommended for real-world applications.

---

## Citation

### How to Cite This Model

**BibTeX**
```bibtex
@misc{dikshit2026medbrainllama,
  author       = {Dikshit, Subrit},
  title        = {MedBrain-Llama-3.1-8B Medical Brain Tumor QA},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/subrit/MedBrain-Llama-3.1-8B-Medical}},
  note         = {Merged 16-bit fine-tuned Llama 3.1 model for medical QA and brain tumor knowledge}
}
```

**APA**
```text
Dikshit, S. (2026). MedBrain-Llama-3.1-8B Medical Brain Tumor QA.
Hugging Face Model Hub. https://huggingface.co/subrit/MedBrain-Llama-3.1-8B-Medical
```

**MLA**
```text
Dikshit, Subrit. "MedBrain-Llama-3.1-8B Medical Brain Tumor QA."
Hugging Face Model Hub, 2026, huggingface.co/subrit/MedBrain-Llama-3.1-8B-Medical.
```

---

## Base Model Citation

This model is based on Meta Llama 3.1 and an Unsloth-optimized training/export workflow.

```bibtex
@article{llama3_2024,
  title   = {The Llama 3 Herd of Models},
  author  = {Meta AI},
  year    = {2024}
}
```

---

## Dataset Citation

```bibtex
@misc{medalpaca_flashcards,
  title        = {medical_meadow_medical_flashcards},
  author       = {MedAlpaca},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards}}
}
```

```bibtex
@misc{medalpaca_medqa,
  title        = {medical_meadow_medqa},
  author       = {MedAlpaca},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/medalpaca/medical_meadow_medqa}}
}
```

---

## LoRA Citation

```bibtex
@article{hu2021lora,
  title   = {LoRA: Low-Rank Adaptation of Large Language Models},
  author  = {Hu, Edward J and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
  journal = {arXiv preprint arXiv:2106.09685},
  year    = {2021}
}
```

---

## Acknowledgments

- **Base Model:** Meta AI for Llama 3.1
- **Training Stack:** Unsloth, Hugging Face Transformers, PEFT, and TRL
- **Platform:** Kaggle T4 environment
- **Datasets:** MedAlpaca medical datasets
- **Open-Source Community:** For tooling, debugging support, and deployment workflows

---

## Model Card Contact

- **Author:** Subrit Dikshit
- **Issues/Questions:** Please open an issue on the model repository
- **Primary Use Case:** Medical education, domain adaptation experiments, and clinical-support prototyping

---

## License

This model inherits the applicable **Llama 3.1** base-model license and usage conditions.

### Additional Terms

- ✅ Free to use for research and educational purposes
- ✅ Suitable for experimentation, prototyping, and evaluation workflows
- ⚠️ Not intended for diagnosis, treatment, or emergency medical decision-making
- ⚠️ Human verification is required before any real-world healthcare use

**Model Version:** 2.0.0  
**Status:** Production Export Ready  
**Format:** Merged 16-bit checkpoint  
**Author:** Subrit Dikshit