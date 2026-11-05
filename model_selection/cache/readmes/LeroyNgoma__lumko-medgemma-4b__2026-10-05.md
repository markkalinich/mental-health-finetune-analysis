---
tags:
- medgemma
- clinical
- south-africa
- lora
- fsdp
- dpo
- chain-of-thought
license: gemma
---

# Lumko Clinical SLM (MedGemma 4B Fine-tuned)

Fine-tuned MedGemma 4B for South African clinical reasoning with Chain-of-Thought.

## Training
- Base: google/medgemma-4b-it
- Method: LoRA (rank 64, alpha 128, BF16) + DPO (beta 0.1)
- Strategy: FSDP on 8x A100 80GB (data parallelism)
- Data: Clinical guidelines (DoH, NICD), LOINC, PubMed
- CoT: Chain-of-thought reasoning with <think> blocks
- Safety: Refusal/boundary training curriculum

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("path/to/merged_model")
tokenizer = AutoTokenizer.from_pretrained("path/to/merged_model")
```
