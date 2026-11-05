---
license: apache-2.0
base_model: google/gemma-4-E4B-it
tags:
  - finance
  - gemma4
  - text-generation
  - sentiment-analysis
  - text-classification
  - merged
datasets:
  - Josephgflowers/Finance-Instruct-500k
  - sujet-ai/Sujet-Finance-Instruct-177k
language:
  - en
pipeline_tag: text-generation
---

# FinanceGemma-E4B

A **finance-specialist ~4B language model** built by merging a QLoRA adapter into [google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it). This is the full merged model — no adapter loading required, just load and run.

For the LoRA adapter weights, see [naazimsnh02/FinanceGemma-E4B-lora](https://huggingface.co/naazimsnh02/FinanceGemma-E4B-lora).

## Highlights

- **Architecture:** Gemma 4 (~4B parameters), full float16 merged weights
- **Specialization:** Financial sentiment analysis, headline classification, financial QA
- **Training method:** 4-bit QLoRA SFT with response-only loss, merged to 16-bit
- **Hardware:** Trained on 1× NVIDIA L4 (24 GB) on GCP instance
- **Final train loss:** 0.0864

## Training details

| Parameter | Value |
|---|---|
| Base model | `google/gemma-4-E4B-it` |
| Fine-tuning method | 4-bit QLoRA (rank 32, alpha 64) |
| Target modules | All attention + MLP layers |
| Max sequence length | 4096 |
| Effective batch size | 16 (micro-batch 1 × grad accum 16) |
| Epochs | 2 (3,738 total steps) |
| Learning rate | 1e-4 (cosine schedule, 3% warmup) |
| Optimizer | AdamW 8-bit, bf16 precision |
| Weight decay | 0.01 |
| Training runtime | ~16.6 hours |
| Peak VRAM | 16.4 GB |
| Loss (start → end) | 0.587 → 0.085 |

## Training data

~30,000 instruction-response pairs sampled from:

- [Josephgflowers/Finance-Instruct-500k](https://huggingface.co/datasets/Josephgflowers/Finance-Instruct-500k)
- [sujet-ai/Sujet-Finance-Instruct-177k](https://huggingface.co/datasets/sujet-ai/Sujet-Finance-Instruct-177k)

Diversity-sampled with per-source and per-task-type caps. **10-gram decontaminated** against FLARE evaluation inputs to prevent benchmark leakage.

## Evaluation

FLARE-style multiple-choice accuracy on [AdaptLLM/finance-tasks](https://huggingface.co/datasets/AdaptLLM/finance-tasks) (greedy decoding, temp=0):

| Task | n | Accuracy |
|---|---|---|
| FPB | 970 | **78.4%** |
| FiQA_SA | 235 | **67.2%** |
| Headline | 20,547 | **69.2%** |
| **Macro avg** | — | **71.6%** |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "naazimsnh02/FinanceGemma-E4B",
    device_map="auto",
    torch_dtype="auto",
)
tokenizer = AutoTokenizer.from_pretrained("naazimsnh02/FinanceGemma-E4B")

prompt = "Classify the sentiment of this financial news: 'Tesla shares dropped 8% after missing delivery targets for Q3.'"
messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True, return_dict=True).to(model.device)
output = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### With Unsloth (faster)

```python
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    "naazimsnh02/FinanceGemma-E4B",
    max_seq_length=4096,
    load_in_4bit=True,
)
FastModel.for_inference(model)
```

## Intended use

- **Sentiment classification** of financial text (positive / negative / neutral)
- **Headline interpretation** (price direction signals)
- **Financial QA** and reasoning

## Limitations

- English-language finance only
- Optimized for classification/short-answer — not long-form generation
- SFT only (no reinforcement learning)
- Merged from a 4-bit QLoRA adapter — some quality gap vs. full fine-tuning expected

## License

Apache 2.0
