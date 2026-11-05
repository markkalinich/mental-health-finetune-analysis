---
license: apache-2.0
base_model: Qwen/Qwen3-8B
tags:
  - medical
  - reasoning
  - lora
  - qwen3
  - unsloth
language:
  - en
---

# Qwen3-8B Medical Reasoning

A LoRA fine-tune of `unsloth/Qwen3-8B-unsloth-bnb-4bit` on medical reasoning and doctor-patient conversational data. Trained using the [Unsloth](https://github.com/unslothai/unsloth) library.

## Training Data

- **Reasoning:** [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) — medical questions paired with step-by-step clinical reasoning traces and a final answer.
- **Conversational:** [lavita/ChatDoctor-HealthCareMagic-100k](https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k) — real patient questions paired with physician responses.
- Mixed at a **75% reasoning / 25% chat** ratio. A higher chat ratio was tested first and produced answers that skipped explicit reasoning steps, so the mix was weighted toward reasoning data to preserve step-by-step clinical reasoning while still keeping natural conversational phrasing.
- Trained on a randomly shuffled subsample of 7,000 combined examples for 1 epoch.

## Training Details

- Base model: `unsloth/Qwen3-8B-unsloth-bnb-4bit` (4-bit quantized)
- Method: LoRA, rank 32
- Framework: Unsloth + TRL `SFTTrainer`
- Hardware: single T4 GPU (Google Colab, free tier)

## Example Outputs & Evaluation


### Example: Sudden severe headache (novel question, not in training data)

**Question:** A 60-year-old woman has sudden severe headache described as 'worst of my life', with neck stiffness and photophobia. What is the most urgent diagnosis to rule out?

**Base Qwen3-8B:** Responds with a heavily formatted breakdown — headers, bold labels, bullet lists covering "Why is this urgent," "Next Steps," etc. Correctly identifies subarachnoid hemorrhage, but reads like a textbook entry.

**Fine-tuned model:** "The sudden severe headache, neck stiffness, and photophobia you described are classic signs of a subarachnoid hemorrhage (SAH), which is a type of stroke. This is a serious condition where bleeding occurs in the space around the brain, often due to a ruptured aneurysm. It's important to act quickly because SAH can be life-threatening and requires immediate medical attention." Same diagnosis, delivered as a direct, conversational explanation rather than a structured reference document.

### Example: Metformin mechanism of action (novel question, not in training data)

**Base Qwen3-8B:** Breaks the answer into four labeled mechanism sections with named enzymes and pathways (AMPK, PFK-1, gluconeogenesis), formatted like a pharmacology textbook excerpt.

**Fine-tuned model:** Covers the same four mechanisms (reduced hepatic glucose production, improved insulin sensitivity, reduced intestinal absorption, reduced fat storage) in plain numbered prose, without the nested markdown structure.

## What the comparison showed

Fine-tuning didn't change diagnostic correctness on this small test set — both the base and fine-tuned model reached the same correct diagnosis on all five test questions. What changed was response style: the fine-tuned model consistently produced shorter, more conversational answers (avg. ~35% fewer words across three of five test questions) that read like a physician speaking directly to a patient, rather than the base model's exam-style breakdown with headers and bullet lists. This tracks with training on ChatDoctor's real patient-physician dialogue data. On the two training-set questions used for lexical comparison, word-overlap similarity to the original reference answers roughly doubled (0.29-0.31 → 0.47-0.49), indicating the model shifted noticeably toward the reference dataset's phrasing style, not just repeating memorized text (sequence similarity stayed low, under 0.1, in both cases).


## Intended Use

This model is intended for educational and research purposes — exploring medical reasoning generation and conversational QA fine-tuning. It is a small-scale student/hobby project, not a validated clinical tool.

## Limitations & Disclaimer

**This model is not a substitute for professional medical advice, diagnosis, or treatment.** It was fine-tuned on a limited dataset without clinical validation, may produce inaccurate or incomplete medical information, and has not been evaluated against standard medical benchmarks (e.g. MedQA). The evaluation above is a small, informal comparison (5 questions) and does not demonstrate improved diagnostic accuracy over the base model — only a shift toward more conversational response style. Do not use this model's output to make real medical decisions. Always consult a qualified healthcare professional.

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Satyam810/qwen3-8b-medical-reasoning")
tokenizer = AutoTokenizer.from_pretrained("Satyam810/qwen3-8b-medical-reasoning")

messages = [{"role": "user", "content": "Describe the mechanism of action of metformin."}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt")
output = model.generate(**inputs, max_new_tokens=300)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```
