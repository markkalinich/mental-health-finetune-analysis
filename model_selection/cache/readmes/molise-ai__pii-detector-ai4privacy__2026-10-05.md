---
license: cc-by-4.0
datasets:
- ai4privacy/pii-masking-400k
language:
- it
- en
- fr
- nl
- es
base_model:
- distilbert/distilbert-base-multilingual-cased
pipeline_tag: token-classification
library_name: transformers
---


# Neural Wave - Hackathon 2024 - Lugano

This repository contains the code produced by the `Molise.ai` team in the Neural Wave Hackathon 2024 competition in
Lugano.

## Challenge

Here is a brief explanation of the challenge:
The challenge was proposed by **Ai4Privacy**, a company that builds global solutions that enhance **privacy protections**

in the rapidly evolving world of **Artificial Intelligence**.
The challenge goal is to create a machine learning model capable of detecting and masking **PII** (Personal Identifiable
Information) in text data across several languages and locales. The task requires working with a synthetic dataset to
train models that can automatically identify and redact **17 types of PII** in natural language texts. The solution
should aim for high accuracy while maintaining the **usability** of the underlying data.
The final solution could be integrated into various systems and enhance privacy protections across industries,
including client support, legal, and general data anonymization tools. Success in this project will contribute to
scaling privacy-conscious AI systems without compromising the UX or operational performance.


## Disclaimer

The publisher of this repository is not affiliated with Ai4Privacy and Ai Suisse SA.