---
library_name: transformers
tags:
  - gpt2
  - text-generation
  - causal-lm
  - fine-tuned
  - mental-health
  - psychology
  - counseling
  - conversational-ai
license: mit
language:
  - en
pipeline_tag: text-generation
---

# Model Card — Fine-tuned GPT-2 on Mental Health & Psychology Datasets (45K rows, 10 Epochs)

## Model Description

This model is a fine-tuned version of **GPT-2** on a combined dataset of ~45,000 mental health and psychology conversation samples across 6 datasets. It is a **causal language model** trained to generate empathetic, contextually appropriate responses to mental health-related prompts — making it suitable for counseling conversation research, mental health chatbot prototyping, and psychology NLP tasks.

- **Developed by:** [praniil](https://github.com/praniil)
- **Model type:** Causal Language Model (GPT-2)
- **Language(s):** English
- **License:** MIT
- **Finetuned from model:** `gpt2` (OpenAI GPT-2 124M, via Hugging Face)

### Model Sources

- **Repository:** [https://github.com/praniil/finetuned_gpt2_45krows_n5](https://github.com/praniil/finetuned_gpt2_45krows_n5)
- **HuggingFace Hub:** `Pranilllllll/finetuned_gpt2_45krows_10epochs`

---

## Uses

### Direct Use

This model can be used out-of-the-box for **mental health and psychology text generation** — given a user message or question as a prompt, it generates a response in the style of a counseling conversation.
```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "Pranilllllll/finetuned_gpt2_45krows_10epochs"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

prompt = "I have been feeling very anxious and overwhelmed lately."
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.9,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Downstream Use

This model can be plugged into larger pipelines for:
- Mental health chatbot or virtual counselor prototyping
- Generating synthetic counseling conversation data
- Psychology NLP research and benchmarking
- Empathetic response generation systems

### Out-of-Scope Use

- **Not a substitute for professional mental health care.** This model should never be used as a replacement for licensed therapists or clinical diagnosis.
- Not suitable for crisis intervention or emergency mental health situations.
- Not designed for factual question answering or knowledge retrieval tasks.
- Should not be deployed in production-facing mental health applications without thorough safety evaluation.

---

## Bias, Risks, and Limitations

- **Clinical risk:** The model may generate responses that sound plausible but are clinically incorrect, harmful, or inappropriate for vulnerable users. Always include human oversight.
- **Data bias:** The model reflects patterns and biases present across the 6 source datasets. Some datasets may over-represent specific demographics or therapeutic styles.
- **Hallucination:** GPT-2 based models may generate fluent but factually incorrect or contextually inappropriate text.
- **Short context window:** Sequences were truncated to 128 tokens during training, so very long conversations may lose context.
- **Small model size:** At 124M parameters, GPT-2 has limited capacity for nuanced reasoning compared to larger modern LLMs.

### Recommendations

This model is intended for **research and prototyping only**. It should not be deployed in any real-world mental health support context without rigorous safety evaluation, content filtering, and human-in-the-loop oversight.

---

## How to Get Started with the Model

Install dependencies:
```bash
pip install transformers torch
```

Then use the inference script in the Direct Use section above.

---

## Training Details

### Training Data

The model was trained on a combined dataset of **~45,000 rows** sourced from 6 public mental health and psychology datasets on Hugging Face:

| # | Dataset | Description |
|---|---------|-------------|
| 1 | [marmikpandya/mental-health](https://huggingface.co/datasets/marmikpandya/mental-health) | Mental health Q&A pairs |
| 2 | [fadodr/mental_health_therapy](https://huggingface.co/datasets/fadodr/mental_health_therapy) | Therapy conversation pairs |
| 3 | [Amod/mental_health_counseling_conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations) | Counseling context-response pairs |
| 4 | [jkhedri/psychology-dataset](https://huggingface.co/datasets/jkhedri/psychology-dataset) | Psychology Q&A pairs |
| 5 | [samhog/psychology-6k](https://huggingface.co/datasets/samhog/psychology-6k) | Psychology input-output pairs |
| 6 | [RAJJ18/mental_health_dataset](https://huggingface.co/datasets/RAJJ18/mental_health_dataset) | Mental health conversations (3,000 rows sampled) |

All datasets were standardized to a unified `input` / `output` column format before concatenation. Dataset 6 was randomly sampled to 3,000 rows (seed=42) for balance.

### Training Procedure

#### Preprocessing

- All datasets normalized to `input` and `output` columns
- Input and output concatenated as a single string: `"{input} {output}"`
- Tokenized using the GPT-2 BPE tokenizer (`AutoTokenizer` from `gpt2`)
- `pad_token` set to `eos_token`
- Sequences truncated and padded to **max length of 128 tokens**
- Labels set equal to `input_ids` for causal language modelling (next-token prediction)

#### Training Hyperparameters

| Hyperparameter              | Value                        |
|-----------------------------|------------------------------|
| Base model                  | `gpt2` (124M parameters)     |
| Epochs                      | 10                           |
| Training rows               | ~45,000                      |
| Per-device train batch size | 4                            |
| Per-device eval batch size  | 4                            |
| Learning rate               | 3e-5                         |
| Warmup steps                | 100                          |
| Weight decay                | 0.01                         |
| Max sequence length         | 128 tokens                   |
| Training regime             | fp16 mixed precision         |
| Evaluation strategy         | Every 5,000 steps            |
| Save strategy               | Every 5,000 steps            |
| Logging steps               | Every 50 steps               |
| Best model metric           | Validation loss (lower is better) |
| Checkpoints kept            | 2 (save_total_limit=2)       |
| Optimizer                   | AdamW (Hugging Face default) |

#### Evaluation Dataset

The test split of `fadodr/mental_health_therapy` (dataset 2) was used as the held-out validation set during training.

---

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The test split of `fadodr/mental_health_therapy` — held out from training and used for validation loss tracking.

#### Metrics

- **Training Loss:** Tracked every 50 steps via TensorBoard logging
- **Validation Loss:** Evaluated every 5,000 steps; best model checkpoint selected based on lowest validation loss
- **Perplexity:** Derived from validation loss — lower perplexity indicates better language modelling

### Results

Training and validation loss curves are available in the [`new_graph/`](https://github.com/praniil/finetuned_gpt2_45krows_n5/tree/main/new_graph) directory. Full training logs are stored in [`new_logs/`](https://github.com/praniil/finetuned_gpt2_45krows_n5/tree/main/new_logs).

---

## Technical Specifications

### Model Architecture and Objective

- **Architecture:** GPT-2 (decoder-only transformer)
- **Objective:** Causal Language Modelling (next-token prediction)
- **Parameters:** 124M
- **Layers:** 12 transformer blocks
- **Attention heads:** 12
- **Hidden size:** 768
- **Max context length:** 1024 tokens (128 tokens used during training)
- **Tokenizer:** GPT-2 BPE tokenizer (vocab size: 50,257)

### Compute Infrastructure

#### Hardware

- CUDA-enabled GPU (local machine)

#### Software

- Python 3.8+
- PyTorch
- Hugging Face `transformers`
- Hugging Face `datasets`
- TensorBoard (for logging)

---

## Environmental Impact

- **Hardware Type:** CUDA-enabled GPU
- **Cloud Provider:** Not applicable (local training)
- **Compute Region:** Nepal
- **Carbon Emitted:** Not measured

---

## Citation
```bibtex
@misc{praniil2024finetuned-gpt2-mentalhealth-10epochs,
  author       = {praniil},
  title        = {Fine-tuned GPT-2 on Mental Health and Psychology Datasets (45K rows, 10 Epochs)},
  year         = {2024},
  publisher    = {HuggingFace},
  howpublished = {\url{https://huggingface.co/Pranilllllll/finetuned_gpt2_45krows_10epochs}},
}
```

---

## Model Card Authors

[praniil](https://github.com/praniil)

## Model Card Contact

Open an issue at [https://github.com/praniil/finetuned_gpt2_45krows_n5/issues](https://github.com/praniil/finetuned_gpt2_45krows_n5/issues)