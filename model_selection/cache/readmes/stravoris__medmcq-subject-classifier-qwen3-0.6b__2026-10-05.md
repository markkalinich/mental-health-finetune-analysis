---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
tags:
  - medical
  - mcq
  - classification
  - qwen3
  - medmcq
  - stravoris
pipeline_tag: text-generation
language:
  - en
---

# MedMCQ — Subject Classifier (Qwen3-0.6B)

A small fine-tuned Qwen3 model that takes a medical multiple-choice question (MCQ) and predicts which **medical subject** the question belongs to.

This is the **router model** in the [MedMCQ three-hop pipeline](#the-medmcq-pipeline). It is the first model called when a new MCQ enters the system: its output decides which downstream subject-specific classifier and generator are used.

## The MedMCQ pipeline

The MedMCQ project explores small, specialized models for medical MCQs. Instead of using one large model for everything, it splits the task across three hops:

1. **Subject routing** — *this model.* Given an MCQ, pick the medical subject (Anatomy, Pharmacology, etc.).
2. **Topic classification** — a per-subject classifier picks the topic within that subject.
3. **Answer generation** — a per-subject generator produces the answer / new MCQs in that subject.

Each hop is a separate, narrow model. They are all published under the [MedMCQ Medical Models](https://huggingface.co/collections/stravoris/medmcq-medical-models) collection.

## Quick start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

repo = "stravoris/medmcq-subject-classifier-qwen3-0.6b"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo)

prompt = """Classify the following medical MCQ by subject.

Question: Which artery supplies the head of the femur in adults?
A) Obturator artery
B) Medial circumflex femoral artery
C) Lateral circumflex femoral artery
D) Superior gluteal artery

Subject:"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=8, do_sample=False)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

## Prompt format

The model expects MCQs in this exact form:

```
Classify the following medical MCQ by subject.

Question: <question text>
A) <option A>
B) <option B>
C) <option C>
D) <option D>

Subject:
```

The model completes the prompt with one of the 15 subject labels:

`Anaesthesia`, `Anatomy`, `Biochemistry`, `Cell Biology & Histology`, `ENT`, `Genetics`, `Microbiology`, `Obstetrics & Gynaecology`, `Ophthalmology`, `Orthopaedics`, `Pathology`, `Pharmacology`, `Physiology`, `Psychiatry`, `Radiology`.

## What this model is not

This is a **sample model for demonstration**. It is not a production-grade medical AI system:

- It has not been formally evaluated against board-level benchmarks.
- It should not be used to make clinical decisions or provide medical advice.
- It was trained on a curated educational dataset and inherits any biases or gaps in that data.

The MedMCQ project exists to explore small-model pipeline architectures for medical reasoning, not to ship a medical product.

## Training data

Trained on the [Stravoris Medical MCQ dataset](https://huggingface.co/datasets/stravoris/medical-mcq-dataset) — a collection of educational medical MCQs covering 15 subjects, labeled with their subject and topic.

## Base model

Fine-tuned from [`Qwen/Qwen3-0.6B`](https://huggingface.co/Qwen/Qwen3-0.6B). The base model's license and usage terms also apply.

## License

Apache 2.0. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0).

## Collection

Part of the [MedMCQ Medical Models](https://huggingface.co/collections/stravoris/medmcq-medical-models) collection — all 31 models that make up the MedMCQ three-hop pipeline.
