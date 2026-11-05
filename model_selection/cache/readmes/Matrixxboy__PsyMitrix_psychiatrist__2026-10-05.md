---
base_model: google/gemma-2-2b-it
library_name: peft
tags:
- mental-health
- chatbot
- conversational
- gemma
- fine-tuned
- text-generation
language: en
license: other
---

# PsyMitrix – A Mental Health Support Chatbot

**PsyMitrix** is a conversational AI, fine-tuned from **[google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)**, designed to provide empathetic and supportive dialogue. It acts as a mental health assistant for conversations about stress, emotions, and personal challenges.

> ⚠️ **Disclaimer:** PsyMitrix is an AI model and **not a substitute for professional mental health care**. It cannot provide diagnosis, treatment, or crisis support. If you are experiencing distress, please seek immediate help from a licensed professional or a crisis hotline.

## Model Details
- **Developed by:** Matrixxboy
- **Model type:** Causal Language Model (Decoder-only)
- **Base model:** `google/gemma-2-2b-it`
- **Fine-tuning:** PEFT / LoRA
- **Language:** English
- **License:** Google DeepMind Gemma License

---

## How to Use
You can interact with the model using the `transformers` library pipeline.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "Matrixxboy/PsyMitrix_psychiatrist"

tokenizer = AutoTokenizer.from_pretrained(model_id)
# For GPU acceleration, add device_map="auto"
model = AutoModelForCausalLM.from_pretrained(model_id)

chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)

# Start a conversation
prompt = "I've been feeling really overwhelmed with work lately. It's hard to switch off."
response = chatbot(prompt, do_sample=True, temperature=0.7)

print(response[0]["generated_text"])
```

## Conversation Example

> **User:** I've been feeling really overwhelmed with work lately. It's hard to switch off.

> **PsyMitrix:** It sounds like you're carrying a heavy weight right now. It's completely understandable to feel overwhelmed when work demands so much of your energy. What does that feeling of being "switched on" all the time feel like for you?

---

## Intended Use

This model is intended for non-critical, supportive applications:
- **Mental Health Journaling:** A conversational partner for reflecting on daily thoughts and feelings.
- **Stress & Anxiety Management:** A tool for practicing mindfulness and exploring coping strategies.
- **Empathetic Dialogue Research:** A base model for experiments in fine-tuning for empathetic AI.

### Out-of-Scope Use
This model is **not** suitable for:
- **Clinical Diagnosis or Treatment:** It is not a medical device and has no clinical expertise.
- **Crisis Response:** It cannot manage emergency situations.
- **Generating Harmful Content:** It should not be used for manipulative, biased, or unsafe outputs.

---

## Limitations, Risks, and Biases

- **No Real-World Understanding:** The model does not understand or experience emotions; it generates responses based on patterns in its training data.
- **Potential for Generic Advice:** Responses may sometimes be generic or not perfectly suited to a user's unique situation.
- **Data Bias:** The model may reflect biases present in the underlying training data of the base model and the fine-tuning dataset.
- **Hallucinations:** Like all LLMs, it can generate factually incorrect information or become repetitive.

**Recommendation:** Users should be aware of these limitations and use the model as a supportive tool, not as a replacement for human connection or professional help.

---

## Training & Evaluation

- **Frameworks:** Hugging Face `transformers`, `peft`, `PyTorch`
- **Method:** Parameter-Efficient Fine-Tuning (LoRA) on the `gemma-2-2b-it` model.
- **Dataset:** A custom, curated dataset of empathetic and supportive conversational dialogues.
- **Evaluation:** The model was evaluated qualitatively through interactive testing to assess its coherence, empathy, and helpfulness in conversational scenarios. It has not been benchmarked on standard NLP leaderboards.

### Environmental Impact
- **Hardware:** Trained on a Kaggle Tesla P100 GPU with 16GB VRAM.
- **Training Time:** Approximately 4 hours for LoRA fine-tuning.
- **Cloud Provider:** Kaggle
- **Carbon Emissions:** Carbon emissions can be estimated using the [ML CO2 Impact calculator](https://mlco2.github.io/impact#compute) with the provided hardware and time details.

---

## Citation

If you use this model in your research or project, please cite it as:

```bibtex
@misc{psymitrix2025,
  author = {Matrixxboy},
  title = {PsyMitrix – A Fine-tuned Gemma-2-2B for Empathetic Conversations},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Model Hub},
  howpublished = {\url{[https://huggingface.co/Matrixxboy/PsyMitrix_psychiatrist](https://huggingface.co/Matrixxboy/PsyMitrix_psychiatrist)}}
}
```

---

## Contact
- **Author:** Matrixxboy
- **Hugging Face:** [https://huggingface.co/Matrixxboy](https://huggingface.co/Matrixxboy)

