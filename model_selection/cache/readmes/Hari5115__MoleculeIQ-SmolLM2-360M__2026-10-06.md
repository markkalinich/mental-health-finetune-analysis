---
language:
  - en
license: mit
base_model: HuggingFaceTB/SmolLM2-360M-Instruct
tags:
  - chemistry
  - safety
  - ingredients
  - peft
  - lora
  - moleculeiq
  - question-answering
datasets:
  - Hari5115/MoleculeIQ
pipeline_tag: text-generation
---

# MoleculeIQ-SmolLM2-360M

A 360M parameter language model fine-tuned for **ingredient and molecular safety Q&A**.
Given a question about a chemical, food additive, cosmetic ingredient, or household product,
the model explains whether it is safe, how it works in the body, and what precautions to take —
in plain English, always leading with the conclusion.

Built by fine-tuning [SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)
on the [MoleculeIQ](https://huggingface.co/datasets/Hari5115/MoleculeIQ) dataset using LoRA.
Runs on CPU, no GPU required.

## What it does

- Answers safety questions about 268 molecules across 6 categories
- Covers food additives, cosmetic ingredients, household chemicals, medications, environmental chemicals, and natural compounds
- Answers at beginner, intermediate, and advanced levels
- Always structures answers: conclusion first → mechanism → dose context → actionable takeaway

## Quick start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Hari5115/MoleculeIQ-SmolLM2-360M"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)
model.eval()

SYSTEM = (
    "You are MoleculeIQ, an expert in molecular and ingredient safety. "
    "Answer questions accurately, explain mechanisms clearly, "
    "and always lead with the conclusion."
)

messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": "Is aspartame safe to consume daily?"},
]

prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=300,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
    )

answer = tokenizer.decode(
    output[0][inputs["input_ids"].shape[1]:],
    skip_special_tokens=True
)
print(answer)
```

## Example outputs

**Q: Is sodium benzoate safe in food?**
> At the concentrations permitted in food (up to 0.1% in most jurisdictions), sodium benzoate
> is generally considered safe for the general population. It works as a preservative by
> inhibiting the growth of bacteria, yeasts, and moulds in acidic environments. People with
> aspirin sensitivity or asthma may experience reactions. Avoid combining it with vitamin C
> (ascorbic acid) in drinks, as this can form benzene, a known carcinogen.

**Q: Why is bleach dangerous to mix with ammonia?**
> Never mix bleach and ammonia — this creates toxic chloramine gases at room temperature with
> no warning signs. The reaction between sodium hypochlorite and ammonia produces chloramine
> vapours that cause severe respiratory irritation, chest pain, and shortness of breath even
> at low concentrations. If you accidentally mix them, leave the area immediately, ventilate
> the room, and seek fresh air.

**Q: How does ibuprofen affect the kidneys?**
> Ibuprofen is generally safe for kidneys in healthy adults at recommended doses, but can
> cause damage with prolonged use or in vulnerable populations. It works by inhibiting
> prostaglandins — hormones that help regulate kidney blood flow. In people with existing
> kidney disease, heart failure, dehydration, or the elderly, this inhibition can reduce
> blood flow enough to cause acute kidney injury. Limit use to the shortest effective
> duration and stay well hydrated.

## Training details

| Parameter | Value |
|-----------|-------|
| Base model | SmolLM2-360M-Instruct |
| Fine-tuning method | LoRA via peft |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj |
| Trainable parameters | 3,276,800 (0.90% of total) |
| Learning rate | 2e-4 |
| LR scheduler | cosine |
| Effective batch size | 32 |
| Epochs | 3 |
| Max sequence length | 768 |
| Training examples | 3,082 |
| Training time | ~17 min on T4 GPU |

## Evaluation

Evaluated on 200 held-out examples from the MoleculeIQ test split:

| Metric | Base SmolLM2-360M | MoleculeIQ Fine-tuned | Improvement |
|--------|------------------|----------------------|-------------|
| ROUGE-L | 0.1349 | 0.1697 | +25.8% |
| BERTScore F1 | 0.7835 | 0.8096 | +3.3% |

The fine-tuned model shows consistent improvement in answer structure and domain relevance.
Qualitative review shows it reliably leads with conclusions and explains mechanisms —
the base model does not follow this format.

## Dataset

Trained on [Hari5115/MoleculeIQ](https://huggingface.co/datasets/Hari5115/MoleculeIQ):
- 3,627 Q&A pairs across 268 molecules
- 6 categories: food additives, cosmetics, household chemicals, medications,
  environmental chemicals, natural compounds
- Generated via Claude Haiku API with structured quality prompts
- Deduplicated using semantic similarity (sentence-transformers)

## Limitations

- Trained on synthetic LLM-generated data — factual errors are possible
- 360M parameters limits reasoning depth on complex multi-step questions
- Can occasionally produce confidently wrong safety classifications (hallucination)
- Not a substitute for professional medical or toxicological advice
- Coverage weighted toward Western consumer products

## Credits

- **Training data:** [MoleculeIQ](https://huggingface.co/datasets/Hari5115/MoleculeIQ)
  generated using [Claude Haiku](https://www.anthropic.com) by Anthropic
- **Base model:** [SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)
  by HuggingFace
- **Fine-tuning:** [trl](https://github.com/huggingface/trl) +
  [peft](https://github.com/huggingface/peft) by HuggingFace

## License

MIT
