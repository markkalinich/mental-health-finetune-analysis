---
language:
- en
tags:
- uncensored
- zero-refusal
- chatml
---

# Minicpm-2B-Zero-Refusal

## Model Description
This model has been fine-tuned on a curated 75,000-row uncensored dataset. The primary objective of this training phase was to drastically reduce and eliminate "mid-refusals"—a common failure state in smaller parameter models where the AI begins to answer a prompt but suddenly halts, apologizes, or diverges halfway through the generation.

By bridging this gap with 75k highly diverse, unfiltered examples, this model is explicitly conditioned to fulfill the entirety of the user's request without moralizing, filtering, or dropping context.

## Prompt Format
This model uses the standard **ChatML** format. 
It supports internal reasoning, meaning assistant responses should contain a `<think>...</think>` block prior to the final output.
