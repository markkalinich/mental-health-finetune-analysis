---
license: apache-2.0


widget:
- text: "### Instruction:\nMy name is Filipe and my phone number is 555-121-2234. How are you?\n### Response:\n"
  example_title: "Example 1"
---
# Open Llama based PII anonymizer

## Description

This model, based on the `openlm-research/open_llama_3b_v2` architecture, is designed to automatically anonymize personal identifiable information (PII) from text data. Given a piece of text, the model can replace specific details such as names, addresses, dates, and other personal details with generic or randomized alternatives, thereby safeguarding the privacy of individuals while retaining the overall context of the text.

## Disclaimer

This model is an experiment and, while it strives to maintain privacy, it may not capture or anonymize all instances of PII in every context. Users should always review and verify the output, especially when dealing with sensitive data.