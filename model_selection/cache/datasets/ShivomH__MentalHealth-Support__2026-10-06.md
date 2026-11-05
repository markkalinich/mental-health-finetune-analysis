---
license: apache-2.0
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- mentalhealth
- medical
- depression
- support
- reasoning
- multi-turn
size_categories:
- 10K<n<100K
---

## Important Note

This dataset is created from merging two datasets from different sources and has been formatted according to the "messages", "role", "content" chat format. I do not claim any ownership of this dataset. 
Keep in mind that this dataset is entirely synthetic. It is not fully representative of real therapy situations. If you are training an LLM therapist keep in mind the limitations of LLMs and highlight those limitations to users in a responsible manner.<br>
**Since Mental Health is a sensitive domain, it is expected that this dataset will be used responsibly.**

## 📊 Dataset Characteristics

- **Total Number of Conversations**: 25,000 🗣️
- **Single-Turn Conversations**: 8,000
- **Multi-Turn Conversations**: 16,000
- **Topics Covered**: 💑 Relationships, 😟 Anxiety, 😔 Depression, 🤗 Intimacy, 👨‍👩‍👧‍👦 Family Conflict, and 28 other mental health topics along with multi-turn conversations.
- **Language**: English 🇺🇸
- **Generation Method for Single-Turn**: OpenAI GPT-3.5 Turbo model with a customized Airoboros self-generation framework

## 🤖 Dataset Usage

This dataset can be used to train and evaluate language models for counseling and mental health applications, such as chatbots, virtual assistants, and dialogue systems. It provides a diverse and realistic set of conversational scenarios that can help improve the models' understanding of psychological conditions and therapeutic strategies.

## 🌍 Dataset Limitations

The long single-turn conversations in the dataset are entirely synthetic and may not fully capture the nuances and complexities of real-world counseling conversations. Additionally, the dataset is limited to English language conversations and may not be representative of diverse cultural and linguistic contexts.

## Sources

* Long Single-Turn: [ShenLab/MentalChat16K](https://huggingface.co/datasets/ShenLab/MentalChat16K)
* Multi-Turn: [jerryjalapeno/nart-100k-synthetic](https://huggingface.co/datasets/jerryjalapeno/nart-100k-synthetic)