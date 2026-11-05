---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
tags:
  - medical
  - mcq
  - classification
  - anaesthesia
  - qwen3
  - medmcq
  - stravoris
pipeline_tag: text-generation
language:
  - en
---

# MedMCQ — Anaesthesia Topic Classifier (Qwen3-0.6B)

A small fine-tuned Qwen3 model that takes an **Anaesthesia** medical multiple-choice question (MCQ) and predicts which **topic** within Anaesthesia the question is about.

This is a **per-subject topic classifier** — the second hop in the [MedMCQ three-hop pipeline](#the-medmcq-pipeline). It assumes the input MCQ has already been routed to Anaesthesia by the [subject classifier](https://huggingface.co/stravoris/medmcq-subject-classifier-qwen3-0.6b).

## The MedMCQ pipeline

The MedMCQ project explores small, specialized models for medical MCQs. Instead of using one large model for everything, it splits the task across three hops:

1. **Subject routing** — the [subject classifier](https://huggingface.co/stravoris/medmcq-subject-classifier-qwen3-0.6b) picks the medical subject.
2. **Topic classification** — *this model.* Given an Anaesthesia MCQ, pick the topic within Anaesthesia.
3. **Answer generation** — the [Anaesthesia generator](https://huggingface.co/stravoris/medmcq-anaesthesia-qwen3-1.7b) produces the answer / new MCQs in Anaesthesia.

Each hop is a separate, narrow model. They are all published under the [MedMCQ Medical Models](https://huggingface.co/collections/stravoris/medmcq-medical-models) collection.

## Quick start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

repo = "stravoris/medmcq-anaesthesia-classifier-qwen3-0.6b"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo)

prompt = """Classify the following Anaesthesia MCQ by topic.

Question: <an Anaesthesia MCQ here>
A) <option A>
B) <option B>
C) <option C>
D) <option D>

Topic:"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=16, do_sample=False)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

## Prompt format

The model expects MCQs in this exact form:

```
Classify the following Anaesthesia MCQ by topic.

Question: <question text>
A) <option A>
B) <option B>
C) <option C>
D) <option D>

Topic:
```

The model completes the prompt with one of the topic labels seen during training. The full topic list is in the [dataset card](https://huggingface.co/datasets/stravoris/medical-mcq-dataset).

## What this model is not

This is a **sample model for demonstration**. It is not a production-grade medical AI system:

- It has not been formally evaluated against board-level benchmarks.
- It should not be used to make clinical decisions or provide medical advice.
- It is narrow: it only understands Anaesthesia MCQs and assumes the upstream subject router did its job.
- It was trained on a curated educational dataset and inherits any biases or gaps in that data.

The MedMCQ project exists to explore small-model pipeline architectures for medical reasoning, not to ship a medical product.

## Training data

Trained on the Anaesthesia subset of the [Stravoris Medical MCQ dataset](https://huggingface.co/datasets/stravoris/medical-mcq-dataset) — educational Anaesthesia MCQs labeled by topic.

## Base model

Fine-tuned from [`Qwen/Qwen3-0.6B`](https://huggingface.co/Qwen/Qwen3-0.6B). The base model's license and usage terms also apply.

## License

Apache 2.0. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0).

## Collection

Part of the [MedMCQ Medical Models](https://huggingface.co/collections/stravoris/medmcq-medical-models) collection — all 31 models that make up the MedMCQ three-hop pipeline.
