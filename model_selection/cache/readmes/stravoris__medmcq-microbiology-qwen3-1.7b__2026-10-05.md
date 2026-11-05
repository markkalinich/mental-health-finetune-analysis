---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B
tags:
  - medical
  - mcq
  - question-answering
  - microbiology
  - qwen3
  - medmcq
  - stravoris
pipeline_tag: text-generation
language:
  - en
---

# MedMCQ — Microbiology Answer Generator (Qwen3-1.7B)

A small fine-tuned Qwen3 model that **answers Microbiology medical multiple-choice questions (MCQs)**. Given a Microbiology topic, an MCQ stem, and four lettered options, it returns the correct option and a brief clinical explanation.

This is a **per-subject answer generator** — the third hop in the [MedMCQ three-hop pipeline](#the-medmcq-pipeline). It is reached only after the [subject classifier](https://huggingface.co/stravoris/medmcq-subject-classifier-qwen3-0.6b) has routed the MCQ to Microbiology and the [Microbiology topic classifier](https://huggingface.co/stravoris/medmcq-microbiology-classifier-qwen3-0.6b) has tagged it with a topic.

## The MedMCQ pipeline

The MedMCQ project explores small, specialized models for medical MCQs. Instead of using one large model for everything, it splits the task across three hops:

1. **Subject routing** — the [subject classifier](https://huggingface.co/stravoris/medmcq-subject-classifier-qwen3-0.6b) picks the medical subject.
2. **Topic classification** — the [Microbiology topic classifier](https://huggingface.co/stravoris/medmcq-microbiology-classifier-qwen3-0.6b) picks the topic within Microbiology.
3. **Answer generation** — *this model.* Given the topic and the MCQ, return the correct option and an explanation.

Each hop is a separate, narrow model. They are all published under the [MedMCQ Medical Models](https://huggingface.co/collections/stravoris/medmcq-medical-models) collection.

## Quick start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

repo = "stravoris/medmcq-microbiology-qwen3-1.7b"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo)

prompt = """Answer the following medical question. Provide the correct option and a brief explanation.

Topic: <a Microbiology topic>

Question: <the MCQ stem>

Options:
A) <option A>
B) <option B>
C) <option C>
D) <option D>"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

## Prompt format

The model expects prompts in this exact form:

```
Answer the following medical question. Provide the correct option and a brief explanation.

Topic: <topic name>

Question: <question stem>

Options:
A) <option A>
B) <option B>
C) <option C>
D) <option D>
```

The model completes the prompt with the correct option and a short clinical explanation, in the form:

```
<letter>) <correct option text>

<brief explanation>
```

## What this model is not

This is a **sample model for demonstration**. It is not a production-grade medical AI system:

- It has not been formally evaluated against board-level benchmarks.
- It should not be used to make clinical decisions or provide medical advice.
- Returned answers and explanations may contain factual errors or outdated information. A clinician should review every output before any educational use.
- It is narrow: it only answers Microbiology MCQs and is brittle outside that domain or on prompts that deviate from the format above.
- It was trained on a curated educational dataset and inherits any biases or gaps in that data.

The MedMCQ project exists to explore small-model pipeline architectures for medical reasoning, not to ship a medical product.

## Training data

Trained on the Microbiology subset of the [Stravoris Medical MCQ dataset](https://huggingface.co/datasets/stravoris/medical-mcq-dataset) — educational Microbiology MCQs with topic labels, stems, lettered options, the correct option, and a worked explanation.

## Base model

Fine-tuned from [`Qwen/Qwen3-1.7B`](https://huggingface.co/Qwen/Qwen3-1.7B). The base model's license and usage terms also apply.

## License

Apache 2.0. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0).

## Collection

Part of the [MedMCQ Medical Models](https://huggingface.co/collections/stravoris/medmcq-medical-models) collection — all 31 models that make up the MedMCQ three-hop pipeline.
