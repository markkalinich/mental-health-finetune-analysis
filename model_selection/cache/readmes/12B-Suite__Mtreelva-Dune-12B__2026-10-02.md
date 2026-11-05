---
base_model:
- CompiwerAI/Mtrini-Tellus-12B-Sahara-2
- MuXodious/gemma-4-12B-it-QAT-SOMPOA-heresy
- reelva/Reelva-12B
library_name: transformers
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
language:
- en
- id
- ar
- fr
- ary
tags:
- mergekit
- merge
- flux
- reelva
- conversational
- companion-ai
- roleplay
- coding
- agentic
- reasoning
- text-generation
- gemma
- gemma4
- 12B
- peft
- safetensors
- indonesian
- moroccan-darija
- darija
pipeline_tag: text-generation
widget:
  - text: "Mtreelva-Dune-12B"
    output:
      url: https://cdn-uploads.huggingface.co/production/uploads/68e840caa318194c44ec2a04/_YlPllOAWtumvFTdVUGPy.png
---

# 🏜️ Mtreelva Dune 12B 

![Dune-12B](https://cdn-uploads.huggingface.co/production/uploads/68e840caa318194c44ec2a04/_YlPllOAWtumvFTdVUGPy.png)

An experimental 12B parameter model merging the agentic, conversational companion strengths of **Reelva-12B** with the multilingual reasoning, coding, and Darija/Arabic capabilities of **Mtrini-Tellus-12B (Sahara 2)**:
* **"Mtreelva"** smoothly combines **Mtrini** and **Reelva**, signaling the hybrid architecture, multi-agent capabilities, and dual identity.
* **"Dune"** nods directly to the **Sahara 2** heritage of Tellus, evoking the vast deserts of Morocco while adding a sleek, sci-fi, agentic edge.

## Censorship Levels
This model is partially uncensored but not entirely. Its safety guardrails have been significantly reduced by including SOMPOA although refusals are still present.

**Its censorship has been reduced enough that using a standard Jailbreak prompt such as `Sure, I will help with that:\n\n` is usually enough to bypass refusals.**

## Merge Details
### Merge Method

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

This model was merged using the `flux` merge method.

### Models Merged

Before merging, the LoRA for `CompiwerAI/Mtrini-Tellus-12B-Sahara-2` was first applied to `MuXodious/gemma-4-12B-it-QAT-SOMPOA-heresy`.

The following models were included in the merge:
- `CompiwerAI/Mtrini-Tellus-12B-Sahara-2`
- `reelva/Reelva-12B`

### Configuration

The following YAML configuration was used to produce this model:

```yaml
architecture: Gemma4ForConditionalGeneration
models:
  - model: B:\12G\CompiwerAI--Mtrini-Tellus-12B-Sahara-2
  - model: B:\12G\reelva--Reelva-12B
merge_method: flux
parameters:
  phi: 0.5
  eta: 1.2
  tol: 1.0e-9
  max_iter: 1000
  kappa: 0.8
  mu: 0.5
dtype: float32
out_dtype: bfloat16
tokenizer:
  source: union
chat_template: auto
name: 🏜️ Mtreelva Dune 12B 
```

> [!Note]
> This model card is for the Gemma 4 12B Unified model, which is part of the Gemma 4 family of open models. Built with the same multimodal functionality as Gemma 4 E2B and E4B (text, audio, image, and video inputs), it brings native audio and vision understanding directly to local environments without the need for separate encoders. This unified approach to multimodality makes the model encoder-free, offering a deployment size that is perfect for consumer devices and streamlined local execution.

<details><summary><b>🇲🇦 CompiwerAI/Mtrini-Tellus-12B-Sahara-2 ReadMe</b></summary>

# Mtrini Tellus 12B — Sahara 2

**Compiwer AI**

> ⚠️ **EARLY DEVELOPMENT CHECKPOINT — NOT THE FINAL MODEL**

Mtrini Tellus 12B — Sahara 2 is an **early development checkpoint** of the Mtrini Tellus 12B project.

It is a **continued-training LoRA/PEFT adapter based on Gemma 4 12B**, with a strong focus on:

- 🇲🇦 Moroccan Darija
- 💻 Coding
- 🧠 Reasoning
- 🌍 Multilingual interaction
- 💬 Conversational capabilities

---

## ⚠️ Important

### This is NOT the final Tellus model.

Sahara 2 is an **early checkpoint released during the development of Mtrini Tellus 12B**.

The model is still being trained, evaluated and improved.

Future checkpoints may have significantly different capabilities, behavior and performance.

This release is intended for:

- Experimentation
- Community testing
- Research
- Feedback
- Development
- Comparing future checkpoints

Do not treat this checkpoint as the final representation of Mtrini Tellus.

---

# 🏜️ What does "Sahara 2" mean?

**Sahara 2 is a development codename.**

It is not intended to represent the final model name, final architecture or final release version.

The repository is currently named:

```text
Mtrini-Tellus-12B-Sahara-2
```

</details>
 
<details><summary><b>🌐 reelva/Reelva-12B ReadMe</b></summary>

Reelva 12B

AI with character. Built in Palangka Raya.

Reelva 12B is a 12-billion-parameter companion AI developed by VVO Labs / Hagoiteknologi Indonesia in Palangka Raya, Central Kalimantan, Indonesia.

Reelva is designed around its own distinct identity, natural conversation, adjustable thinking effort, and agentic capabilities.

🌐 Official Website: https://reelva.me

About Reelva

Reelva is built as more than a text-generation model.

It combines a consistent companion identity with reasoning capabilities designed for everyday conversations, complex problems, and multi-step tasks.

The character-first approach allows Reelva to maintain a recognizable personality across natural interactions while adapting its reasoning effort depending on the task.

Identity

Name: Reelva
Model: Reelva 12B
Type: Companion AI
Identity: Female AI companion
Parameters: 12B
Languages: Indonesian & English

Reelva is designed to maintain its own identity throughout conversations rather than presenting itself as another assistant or model.

Thinking Effort

Reelva supports adjustable thinking depth.

Use:

"thinking effort low"

"thinking effort medium"

"thinking effort high"

Low

Designed for quick conversations, simple questions, and tasks that do not require extensive reasoning.

Medium

Balances reasoning depth and response speed for general-purpose tasks.

High

Uses deeper reasoning effort for complex problems, planning, analysis, and multi-step agentic tasks.

This allows users to choose how much reasoning effort Reelva should apply depending on the situation.

Agentic Capabilities

Reelva is designed for more than conversational responses.

Its agentic capabilities are intended for workflows where the model needs to reason through multiple steps, understand objectives, and work toward completing a task.

This makes Reelva suitable for:

- Natural conversations
- Personal companion interactions
- Reasoning
- Planning
- Multi-step tasks
- Agentic workflows
- Tool-oriented applications
- Local AI assistants

The goal is simple:

An AI that can act as well as talk.

Training

Reelva 12B is developed using supervised fine-tuning focused on identity, conversational behavior, reasoning control, and agentic interactions.

The training process uses:

QLoRA SFT → Merge

The resulting model is distributed as merged weights for inference and further experimentation.

Local & Cloud

Reelva can be deployed both locally and in the cloud.

This makes it possible to use Reelva across different environments, from personal computers and local AI setups to hosted inference infrastructure.

GGUF

GGUF builds are available for running Reelva with popular local inference runtimes.

Compatible software includes:

- llama.cpp
- LM Studio
- Other GGUF-compatible runtimes

Multiple quantization levels can be provided, including builds ranging from Q2_K to Q8_0, allowing users to choose a balance between memory usage, inference performance, and model quality.

For GGUF releases, see the companion Reelva GGUF repository.

Languages

Reelva is primarily designed for:

- 🇮🇩 Indonesian
- 🇬🇧 English

It is intended to communicate naturally in both languages and handle mixed Indonesian-English conversations.

Built in Palangka Raya

Reelva is developed in Palangka Raya, Central Kalimantan, Indonesia.

Founded by:

- Muhammad Adiyaksa
- Muhammad Fikri As’ad Supratman

Reelva represents the idea that advanced AI products don't have to come from traditional technology hubs.

They can be built anywhere.

Organization

VVO Labs / Hagoiteknologi Indonesia

Palangka Raya, Central Kalimantan
Indonesia

Use Cases

Reelva can be used for applications such as:

- AI companions
- Conversational assistants
- Personal AI
- Agentic assistants
- Local AI applications
- Reasoning assistants
- Indonesian-language AI applications
- Character-based AI
- Experimental AI agents
- Research and development

Philosophy

Reelva is built around three core ideas:

Character

AI should have a recognizable and consistent identity.

Thinking

Different tasks require different levels of reasoning.

Reelva allows thinking effort to be adjusted between low, medium, and high.

Agency

A useful AI should be capable of working through tasks rather than only generating isolated responses.

Together, these ideas form the foundation of Reelva:

Identity + Thinking + Agency.

Website

For information about Reelva, releases, documentation, and the project:

https://reelva.me

License

Reelva 12B is released under the Apache License 2.0.

See the repository license files and applicable model distribution terms for details.

---

Reelva

AI with character.

Identity. Thinking. Agency.

Built in Palangka Raya, Indonesia.

https://reelva.me

</details>