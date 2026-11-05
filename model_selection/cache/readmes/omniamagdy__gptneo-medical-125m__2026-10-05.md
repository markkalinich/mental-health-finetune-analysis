---
language: en
license: mit
pipeline_tag: text-generation
tags:
- medical
- gpt-neo
- lora
- peft
- pubmed
- instruction-tuned
datasets:
- ccdv/pubmed-summarization
base_model: EleutherAI/gpt-neo-125M
---

# GPT-Neo 125M Medical Instruction-Tuned Model

## Model Overview

This model is an instruction-conditioned medical text generator built on top of **EleutherAI/gpt-neo-125M**.

It was fine-tuned using **LoRA (Low-Rank Adaptation)** with prompt-formatted biomedical abstracts from the PubMed Summarization dataset.

Unlike standard fine-tuned models, this version was trained using structured prompts to improve domain-specific generation quality.

---

## Key Improvements

Compared to the base fine-tuned version:

- Larger context window (512 tokens)
- Instruction-style prompt formatting
- Enhanced LoRA configuration (r=16)
- Reduced hallucination via controlled decoding
- Improved generation coherence for medical narratives

---

## Intended Use

This model is designed for:

- Medical text generation
- Biomedical explanation drafting
- Research prototyping
- Educational demonstrations
- NLP experimentation in healthcare

⚠️ This model is **NOT intended for clinical use**.

---

## Training Details

| Item | Value |
|------|-------|
| Base Model | EleutherAI/gpt-neo-125M |
| Dataset | PubMed Summarization |
| Training Method | LoRA |
| Prompt Conditioning | Yes |
| Context Length | 512 |
| LoRA Rank | 16 |
| Task | Instruction-based Medical Text Generation |

---

## Dataset

Training utilized biomedical abstracts from:

https://huggingface.co/datasets/ccdv/pubmed-summarization

Prompt formatting was applied:

Medical report:
<Abstract text>

This improves alignment with generation tasks rather than summarization.

---

## Training Strategy

- Base model weights frozen
- LoRA adapters applied to attention layers
- Prompt-based conditioning introduced
- Controlled decoding parameters used during inference

This enables:

- Efficient training
- Low memory footprint
- Domain-aligned generation

LoRA Paper:
https://arxiv.org/abs/2106.09685

---

## Limitations

- May generate plausible but incorrect medical statements
- Not trained on clinical decision datasets
- May struggle with rare diseases
- No real-time knowledge updates

Users must verify outputs using trusted medical sources.

---

## Ethical Considerations

Allowed Uses:

✔️ Research  
✔️ Academic projects  
✔️ NLP experimentation  

Disallowed Uses:

❌ Clinical decision support  
❌ Medical diagnosis  
❌ Treatment planning  
❌ Emergency healthcare guidance  

This model does not replace medical professionals.

---

## Future Work

- Add ROUGE / BLEU evaluation
- Compare against BioGPT / ClinicalT5
- Improve safety alignment
- Add hallucination detection layer
- Extend to clinical-style datasets

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("omniamagdy/gptneo-medical-125m")
tokenizer = AutoTokenizer.from_pretrained("omniamagdy/gptneo-medical-125m")

prompt = "Medical report:\nExplain hypertension"

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=120,
    temperature=0.6,
    top_p=0.9,
    repetition_penalty=1.2
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
