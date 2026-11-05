---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: reasoning
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 90696118
    num_examples: 15006
  download_size: 50651959
  dataset_size: 90696118
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- philosophy
- psychology
- reasoning
- social
- emotion
task_categories:
- text-generation
- question-answering
language:
- en
size_categories:
- 10K<n<100K
---
## Methodology

We perform domain filtering on [Dolphin R1](https://huggingface.co/datasets/cognitivecomputations/dolphin-r1) and [General Reasoning](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K). 

Prompts are embedded, clustered with k-means (k=20 000) and majority-voted for domain labels using [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B), following the [Intelligent Internet pipeline](https://huggingface.co/Intelligent-Internet/II-Medical-8B-1706). 

Clusters tagged psychology or philosophy were retained for LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16).

This work was performed using HPC resources (Jean Zay supercomputer) from GENCI-IDRIS (Grant 20XX-AD011014205).

## Piaget

Piaget, a language model based on Qwen3 and finetuned on PsychologicalReasoning-15k.

Available sizes are: [0.6B](https://huggingface.co/gustavecortal/Piaget-0.6B), [1.7B](https://huggingface.co/gustavecortal/Piaget-1.7B), [4B](https://huggingface.co/gustavecortal/Piaget-4B), [8B](https://huggingface.co/gustavecortal/Piaget-8B).

Piaget aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence.

Piaget was inspired by my position paper on emotion analysis: [Improving Language Models for Emotion Analysis: Insights from Cognitive Science](https://aclanthology.org/2024.cmcl-1.23/).

## Contact

Mail: gustave.cortal@ens-paris-saclay.fr

Website: [gustavecortal.com](gustavecortal.com)