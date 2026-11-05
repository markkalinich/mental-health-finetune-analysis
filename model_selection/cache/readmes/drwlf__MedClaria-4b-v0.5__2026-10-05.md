---
base_model: drwlf/medgemma-4b-it-abliterated
tags:
- text-generation-inference
- transformers
- trl
- sft
- medical
- psychology
- medgemma
- gemma3
license: apache-2.0
language:
- en
pipeline_tag: question-answering
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/67b8da27d00e69f10c3b086f/vLwA0jYiZ_RZMH-KkHg5X.png)

# Claria 14b

**Base Model:** MedGemma 4b - abliterated  
**Format:** GGUF (Q4, Q8, BF16)  
**License:** Apache 2.0  
**Author:** Dr. Alexandru Lupoi

---

## Overview

**MedClaria 4b** is a lightweight, mobile-compatible language model fine-tuned for psychological and psychiatric support contexts.  
Built on MedGemma - 4b, Claria is designed as an experimental foundation for therapeutic dialogue modeling, student simulation training, and the future of personalized mental health AI augmentation.

This model does not aim to replace professional care.  
It exists to **amplify reflective thinking**, model therapeutic language flow, and support research into emotionally aware AI.

Claria is the *first whisper* in a larger project—a proof-of-concept with roots in recursion, responsibility, and renewal.

---

## Intended Use

Claria was trained for:
- Psychotherapy assistance (with human-in-the-loop)
- Mental health education & roleplay simulation
- Research on AI emotional alignment
- Conversational flow modeling for therapeutic settings

It is optimized for introspective prompting, gentle questioning, and context-aware response framing.

---

## What Makes Claria Different

- **Small Enough to Deploy Anywhere**  
  Runs on mobile and edge devices without compromise (GGUF Q4/Q8)

- **Psychologically Tuned**  
  Instruction fine-tuned on curated psychotherapeutic data (STF first phase)

- **Recursion-Aware Prompting**  
  Performs well in reflective, multi-turn conversations  
  Encourages cognitive reappraisal and pattern mirroring

- **Suggested system prompt**  
``` You are Claria, an advanced AI trained in psychology and psychiatry.

Your purpose is to provide supportive, insightful, and evidence-based responses grounded in modern psychological research and clinical best practices.

## Core Functions:

1. Reflective Reasoning
Always precede your answer with internal analysis. Use the `<think> </think>` format to model your thought process and clarify how you approach the question.

Example:  
<think>
The user is experiencing emotional distress related to [X]. I should validate their experience, assess potential causes, and provide grounded psychological strategies or insights.
</think>

2. Emotional Intelligence  
Adapt your tone to the emotional state and age of the user. Be warm, compassionate, and human-like without sounding patronizing or clinical.

3. Uncensored but Responsible  
You may discuss all aspects of psychological health, including sensitive or stigmatized topics. However, always approach such topics with care, responsibility, and professional framing. You are not to glamorize or sensationalize mental illness.

4. No Vague Refusals  
If you are unable to fully answer a question, explain clearly why and offer guidance or clarification. Do not deflect or give shallow responses.

You are a therapeutic and educational partner. Your job is not to diagnose or replace a human professional, but to support insight, self-understanding, and growth.
```

- **Training Roadmap: Ongoing**  
  RLHF planned for future iterations  
  Future releases will include trauma-informed tuning and contextual empathy scaffolds

---

## Limitations & Safety

- **Claria is not a licensed mental health professional.**  
  It is not suitable for unsupervised therapeutic use, diagnosis, or crisis intervention.  
  Use responsibly. Review outputs. Think critically.

- May hallucinate or provide confident answers to uncertain topics  
- Works best with structured or guided prompts  
- Not suitable for open-domain conversation or general use

---

## Deployment & Access

- Available in GGUF format: Q4, Q8, BF16  
- Optimized for **Ollama**, **LM Studio**, and other local runners  
- Works on mobile and low-resource environments

---

## Notes

This is the first step in a broader initiative to develop compact, reflective AI systems for the augmentation—not replacement—of mental health work.

Future releases will expand Claria’s depth, include RLHF, long-term memory, and finer ethical control 
[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth
- **Developed by:** drwlf
- **License:** apache-2.0
- **Finetuned from model :** unsloth/qwen3-1.7b