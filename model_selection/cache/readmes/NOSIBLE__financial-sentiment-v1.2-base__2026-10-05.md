---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
  - Qwen/Qwen3-0.6B-Base
tags:
  - financial-sentiment
  - finance
  - sentiment-analysis
  - nlp
---

<p align="center">
    <img src="https://github.com/NosibleAI/nosible-py/blob/main/docs/_static/readme.png?raw=true"/>
<p>

## Changelog
- **v1.2.0:** Multilingual upgrade. Extends coverage to **94 languages** while holding English performance flat, and adds currency / G10-geography coverage.
- **v1.1.0:** English financial-sentiment model trained on real-world Nosible Search Feeds.

**financial-sentiment-v1.2-base** is a financial sentiment classification model built to determine whether a short text snippet describes an event likely to have a **positive**, **neutral**, or **negative** financial impact. It is fine-tuned from [**Qwen3-0.6B-Base**](https://huggingface.co/Qwen/Qwen3-0.6B) and reframes sentiment classification as instruction following, producing a single label token per input.

This is the **multilingual successor to [financial-sentiment-v1.1-base](https://huggingface.co/NOSIBLE/financial-sentiment-v1.1-base)**. v1.1 was trained primarily on English; v1.2 extends the same task to **94 languages** (English plus 93 additional languages) so the model can classify financial sentiment on text as it appears across global news and search feeds.

### What's new in v1.2

- **Multilingual coverage.** The training corpus extends the English [Financial Sentiment](https://huggingface.co/datasets/NOSIBLE/financial-sentiment) data with faithful translations across 93 additional languages, where the financial-sentiment label is preserved through translation (a financially negative snippet stays negative, etc.).
- **Wider topic coverage.** v1.2 adds currency and G10-geography feeds, improving sentiment classification on currency- and country / region-focused text, not just company news.
- **English held flat.** v1.2 is a multilingual extension, not an English re-train. English accuracy and macro-F1 are unchanged within run noise (see below).
- **The multilingual gap roughly halved.** On the held-out validation set, the English-vs-multilingual accuracy gap shrinks from **~11.0pp** (v1.1) to **~4.8pp** (v1.2).

### Performance overview

All numbers below are measured on the **live SGLang endpoint** (OpenAI-compatible chat-completions, `enable_thinking=False`, `temperature=0`), scored against the same held-out validation splits for both models. Deltas are in **percentage points (pp)**.

#### Headline

| Slice | n | Metric | v1.1 | v1.2 | Δ |
|-------|---:|--------|-----:|-----:|----:|
| English val | 20,000 | Accuracy | 87.70% | 87.97% | +0.27pp |
| English val | 20,000 | Macro-F1 | 87.95% | 88.22% | +0.27pp |
| **Multilingual val** | 19,194 | Accuracy | 76.69% | **83.16%** | **+6.47pp** |
| **Multilingual val** | 19,194 | Macro-F1 | 76.90% | **83.27%** | **+6.37pp** |
| Currency / geo feeds | 4,012 | Accuracy | 67.30% | 76.17% | +8.87pp |
| Currency / geo feeds | 4,012 | Macro-F1 | 67.44% | 75.69% | +8.25pp |

English is held flat while multilingual accuracy improves by **+6.47pp** and the currency / geography feeds improve by **+8.87pp**.

#### Selected languages (largest validation slices)

| Language | n | v1.1 acc | v1.2 acc | Δ acc |
|----------|---:|--------:|--------:|------:|
| German (de) | 1,597 | 82.22% | 87.16% | +4.94pp |
| Japanese (ja) | 1,508 | 80.17% | 85.08% | +4.91pp |
| Spanish (es) | 1,263 | 82.82% | 86.54% | +3.72pp |
| Russian (ru) | 1,686 | 83.75% | 86.89% | +3.14pp |
| French (fr) | 1,233 | 84.18% | 86.94% | +2.76pp |
| Portuguese (pt) | 730 | 82.60% | 85.07% | +2.47pp |
| Italian (it) | 673 | 85.14% | 87.37% | +2.23pp |
| Chinese (zh) | 1,383 | 84.24% | 86.12% | +1.88pp |
| Polish (pl) | 594 | 78.45% | 85.35% | +6.90pp |
| Dutch (nl) | 511 | 77.89% | 83.56% | +5.67pp |

The gains are largest on lower-resource languages, where v1.1 tended to collapse to the dominant class. For example, accuracy rises on Tamil (40.35% → 73.68%), Hausa (39.39% → 65.66%), and Swahili (44.74% → 63.16%), with even larger macro-F1 improvements as the model recovers per-class signal.

## Strict Usage Requirements

> [!CAUTION]
> 1. **Disable Thinking:** You **must** set `enable_thinking=False` (or disable reasoning tokens).
> 2. **Exact System Prompt:** You **must** use the specific system prompt: `"Classify the financial sentiment as positive, neutral, or negative."`
> 3. **Constrain Output:** You **must** restrict generation to the valid labels (`["positive", "neutral", "negative"]`) using **grammars**, **regex**, or **guided decoding**.
>    * **SGLang:** Use `regex="(positive|neutral|negative)"` in the API call.
>    * **vLLM:** Use `guided_choice=["positive", "negative", "neutral"]` in the API call.
>    * **llama.cpp / GGUF:** Apply a GBNF grammar or regex to force selection from the list.
>
> Deviating from these requirements will **severely** impact performance and reliability.

## Quickstart (local GPU)

Since this model was trained as a Causal LM using specific chat templates, you must use `apply_chat_template` with the exact system prompt used during training.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "NOSIBLE/financial-sentiment-v1.2-base"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
)

# Multilingual input is supported (94 languages).
text = "La empresa reportó un margen de beneficio récord del 15% este trimestre."

# 1. Structure the prompt exactly as used in training
messages = [
    {"role": "system", "content": "Classify the financial sentiment as positive, neutral, or negative."},
    {"role": "user", "content": text},
]

# 2. Apply chat template (thinking MUST be disabled)
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)

inputs = tokenizer([prompt], return_tensors="pt").to(model.device)

# 3. Generate the label (only a single token is expected)
outputs = model.generate(**inputs, max_new_tokens=1)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response.split("<|im_start|>assistant\n")[-1])
# Expected Output: positive
```

## Deployment

For production we recommend serving with [**SGLang**](https://github.com/sgl-project/sglang) (`sglang>=0.4.6.post1`), which exposes an OpenAI-compatible API endpoint. The model is based on Qwen3-0.6B and can be deployed anywhere Qwen3-0.6B can.

**Launch the server:**

```shell
python3 -m sglang.launch_server --model-path NOSIBLE/financial-sentiment-v1.2-base --dtype bfloat16 --host 0.0.0.0 --port 8080
```

**Call the endpoint** using the OpenAI-compatible client. Requesting `logprobs` lets you read a calibrated confidence for each label.

```python
import math
from openai import OpenAI

# OpenAI-compatible client pointed at your SGLang server (set base_url to your
# endpoint URL if remote). The request shape mirrors signals_deploy_v12.predict_one.
client = OpenAI(base_url="http://localhost:8080/v1", api_key="EMPTY")

model_id = "NOSIBLE/financial-sentiment-v1.2-base"

# Multilingual input is supported.
text = "La empresa reportó un margen de beneficio récord del 15% este trimestre."

messages = [
    {"role": "system", "content": "Classify the financial sentiment as positive, neutral, or negative."},
    {"role": "user", "content": text},
]

completion = client.chat.completions.create(
    model=model_id,
    messages=messages,
    temperature=0,
    stream=False,
    logprobs=True,
    top_logprobs=3,
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},  # Must be set to false.
)

# The top-1 token is the predicted label; the full top_logprobs slice gives a
# per-label confidence.
top = completion.choices[0].logprobs.content[0].top_logprobs
print(f"Input: {text}")
print(f"Predicted Label: {top[0].token.strip()}")
print("--- Label Confidence ---")
for lp in top:
    print(f"Token: {lp.token.strip()!r} | Probability: {math.exp(lp.logprob):.2%}")
```

#### Expected Output

```text
Input: La empresa reportó un margen de beneficio récord del 15% este trimestre.
Predicted Label: positive

--- Label Confidence ---
Token: 'positive' | Probability: 99.87%
Token: 'neutral' | Probability: 0.11%
Token: 'negative' | Probability: 0.02%
```

**Legal Notice:** This model is a modification of the Qwen3-0.6B model. In compliance with the Apache 2.0 license, we retain all original copyright notices and provide this modification under the same license terms.

## Limitations

* **Parameter Size (0.6B):** As a small language model, it is designed for fast, specific classification and may struggle with highly nuanced or ambiguous text that requires extensive world knowledge.
* **Per-language quality varies.** Accuracy on the highest-resource languages approaches the English baseline; lower-resource languages remain below it despite the large v1.2 improvements.
* **Domain Specificity:** The model is fine-tuned on **financial contexts**. It is not suitable for general sentiment analysis (e.g. product reviews).
* **Not aspect-based:** The model returns a single, blunt sentiment for the snippet as a whole. It does **not** perform aspect-based sentiment analysis — it will not attribute different sentiments to different entities, companies, or aspects mentioned in the same text.
* **Factuality:** The model analyzes the *sentiment* of the text provided; it does not verify the factual accuracy of any figures, dates, or claims within it.

## Disclaimer

* **Not Financial Advice:** The outputs of this model **should not be interpreted as financial advice, investment recommendations, or an endorsement** of any financial instrument or asset.
* **Risk:** Financial markets are inherently volatile and risky. **Never make investment decisions based solely on the output of an AI model.** Always consult with a qualified financial professional.

## Team & Credits

This model was developed and maintained by the following team:

* [**Matthew Dicks**](https://www.linkedin.com/in/matthewdicks98/)
* [**Gareth Warburton**](https://www.linkedin.com/in/garethwarburton/)
* [**Stuart Reid**](https://www.linkedin.com/in/stuartgordonreid/)

## Citation

If you use this model, please cite it as follows:

```bibtex
@misc{nosible2025financialsentimentv12,
  author = {NOSIBLE},
  title = {Financial Sentiment v1.2 Base},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Repository},
  howpublished = {https://huggingface.co/NOSIBLE/financial-sentiment-v1.2-base}
}
```


## Full language breakdown

v1.1 was trained on **English only**; v1.2 adds the **93 languages** below (94 total
with English). The figures are the training-time evaluation per language and reproduce
on the served SGLang endpoint to within ~0.2pp. Deltas are in percentage points (pp),
sorted by validation row count.

| Language | n | v1.1 acc | v1.2 acc | Δ acc | v1.1 F1 | v1.2 F1 | Δ F1 |
|----------|---:|--------:|--------:|------:|-------:|-------:|------:|
| Russian (ru) | 1,686 | 83.63% | 86.83% | +3.20pp | 83.91% | 86.88% | +2.97pp |
| German (de) | 1,597 | 82.15% | 87.16% | +5.01pp | 82.25% | 87.50% | +5.25pp |
| Japanese (ja) | 1,507 | 80.36% | 85.14% | +4.78pp | 80.50% | 85.59% | +5.09pp |
| Chinese (zh) | 1,382 | 84.30% | 86.25% | +1.95pp | 84.59% | 86.49% | +1.90pp |
| Spanish (es) | 1,263 | 82.90% | 86.38% | +3.48pp | 82.91% | 86.57% | +3.66pp |
| French (fr) | 1,233 | 84.02% | 86.86% | +2.84pp | 84.81% | 87.55% | +2.74pp |
| Portuguese (pt) | 730 | 82.60% | 85.21% | +2.61pp | 82.96% | 85.58% | +2.62pp |
| Italian (it) | 673 | 85.44% | 87.37% | +1.93pp | 85.54% | 87.75% | +2.21pp |
| Polish (pl) | 594 | 78.45% | 85.52% | +7.07pp | 78.61% | 85.37% | +6.76pp |
| Dutch (nl) | 511 | 78.28% | 83.76% | +5.48pp | 79.13% | 84.28% | +5.15pp |
| Turkish (tr) | 393 | 79.13% | 81.93% | +2.80pp | 78.78% | 81.71% | +2.93pp |
| Indonesian (id) | 383 | 80.94% | 86.42% | +5.48pp | 80.99% | 86.62% | +5.63pp |
| Vietnamese (vi) | 366 | 83.06% | 82.51% | -0.55pp | 83.82% | 82.83% | -0.99pp |
| Czech (cs) | 331 | 78.55% | 84.59% | +6.04pp | 78.62% | 84.18% | +5.56pp |
| Korean (ko) | 291 | 80.41% | 84.54% | +4.13pp | 81.46% | 85.04% | +3.58pp |
| Arabic (ar) | 288 | 78.82% | 82.29% | +3.47pp | 77.98% | 82.15% | +4.17pp |
| Ukrainian (uk) | 247 | 79.76% | 84.21% | +4.45pp | 80.32% | 84.52% | +4.20pp |
| Swedish (sv) | 228 | 81.14% | 84.65% | +3.51pp | 80.61% | 84.71% | +4.10pp |
| Romanian (ro) | 227 | 78.85% | 84.58% | +5.73pp | 79.82% | 85.19% | +5.37pp |
| Hindi (hi) | 190 | 68.42% | 80.53% | +12.11pp | 66.87% | 80.80% | +13.93pp |
| Greek (el) | 187 | 67.91% | 77.54% | +9.63pp | 64.64% | 76.79% | +12.15pp |
| Hungarian (hu) | 178 | 72.47% | 81.46% | +8.99pp | 72.05% | 81.06% | +9.01pp |
| Thai (th) | 178 | 75.84% | 87.64% | +11.80pp | 77.31% | 88.06% | +10.75pp |
| Danish (da) | 177 | 79.66% | 84.75% | +5.09pp | 78.53% | 83.92% | +5.39pp |
| Bengali (bn) | 145 | 62.07% | 75.86% | +13.79pp | 57.80% | 75.14% | +17.34pp |
| Slovak (sk) | 145 | 76.55% | 81.38% | +4.83pp | 75.76% | 81.08% | +5.32pp |
| Malay (ms) | 143 | 81.12% | 83.22% | +2.10pp | 81.49% | 83.97% | +2.48pp |
| Persian (fa) | 136 | 75.74% | 79.41% | +3.67pp | 74.98% | 79.14% | +4.16pp |
| Finnish (fi) | 136 | 64.71% | 79.41% | +14.70pp | 62.60% | 79.55% | +16.95pp |
| Urdu (ur) | 121 | 71.07% | 76.03% | +4.96pp | 68.50% | 73.49% | +4.99pp |
| Norwegian (no) | 115 | 76.52% | 82.61% | +6.09pp | 77.06% | 82.95% | +5.89pp |
| Swahili (sw) | 114 | 44.74% | 62.28% | +17.54pp | 28.99% | 61.13% | +32.14pp |
| Tamil (ta) | 114 | 40.35% | 73.68% | +33.33pp | 31.49% | 72.14% | +40.65pp |
| Serbian (sr) | 113 | 83.19% | 86.73% | +3.54pp | 83.84% | 87.42% | +3.58pp |
| Hebrew (he) | 110 | 77.27% | 82.73% | +5.46pp | 76.88% | 82.95% | +6.07pp |
| Marathi (mr) | 110 | 50.00% | 80.00% | +30.00pp | 48.89% | 79.98% | +31.09pp |
| Bulgarian (bg) | 108 | 84.26% | 87.96% | +3.70pp | 83.11% | 86.97% | +3.86pp |
| Punjabi (pa) | 107 | 55.14% | 75.70% | +20.56pp | 51.59% | 74.99% | +23.40pp |
| Telugu (te) | 103 | 42.72% | 80.58% | +37.86pp | 32.33% | 80.19% | +47.86pp |
| Hausa (ha) | 99 | 39.39% | 64.65% | +25.26pp | 25.76% | 63.19% | +37.43pp |
| Tagalog (tl) | 99 | 73.74% | 77.78% | +4.04pp | 72.53% | 77.42% | +4.89pp |
| Gujarati (gu) | 98 | 53.06% | 78.57% | +25.51pp | 46.11% | 75.81% | +29.70pp |
| Kannada (kn) | 92 | 51.09% | 72.83% | +21.74pp | 38.24% | 72.06% | +33.82pp |
| Croatian (hr) | 90 | 76.67% | 81.11% | +4.44pp | 73.00% | 80.94% | +7.94pp |
| Azerbaijani (az) | 88 | 69.32% | 75.00% | +5.68pp | 60.86% | 71.82% | +10.96pp |
| Pashto (ps) | 88 | 45.45% | 69.32% | +23.87pp | 34.32% | 68.89% | +34.57pp |
| Malayalam (ml) | 86 | 47.67% | 72.09% | +24.42pp | 38.68% | 72.09% | +33.41pp |
| Nepali (ne) | 84 | 64.29% | 76.19% | +11.90pp | 62.22% | 76.41% | +14.19pp |
| Uzbek (uz) | 84 | 54.76% | 73.81% | +19.05pp | 48.65% | 73.47% | +24.82pp |
| Burmese (my) | 83 | 48.19% | 69.88% | +21.69pp | 36.83% | 70.75% | +33.92pp |
| Odia (or) | 82 | 43.90% | 69.51% | +25.61pp | 32.05% | 68.73% | +36.68pp |
| Amharic (am) | 77 | 42.86% | 66.23% | +23.37pp | 23.46% | 59.46% | +36.00pp |
| Kazakh (kk) | 77 | 57.14% | 79.22% | +22.08pp | 50.37% | 78.74% | +28.37pp |
| Somali (so) | 77 | 53.25% | 51.95% | -1.30pp | 33.35% | 50.88% | +17.53pp |
| Sindhi (sd) | 75 | 65.33% | 69.33% | +4.00pp | 63.63% | 67.47% | +3.84pp |
| Lithuanian (lt) | 73 | 63.01% | 71.23% | +8.22pp | 58.04% | 69.78% | +11.74pp |
| Sinhala (si) | 69 | 40.58% | 52.17% | +11.59pp | 23.58% | 45.35% | +21.77pp |
| Assamese (as) | 66 | 57.58% | 80.30% | +22.72pp | 54.79% | 79.92% | +25.13pp |
| Khmer (km) | 66 | 63.64% | 69.70% | +6.06pp | 57.87% | 67.45% | +9.58pp |
| Slovenian (sl) | 66 | 69.70% | 77.27% | +7.57pp | 63.82% | 73.55% | +9.73pp |
| Afrikaans (af) | 64 | 73.44% | 84.38% | +10.94pp | 73.38% | 84.64% | +11.26pp |
| Armenian (hy) | 56 | 57.14% | 67.86% | +10.72pp | 51.87% | 66.44% | +14.57pp |
| Kyrgyz (ky) | 48 | 43.75% | 77.08% | +33.33pp | 39.29% | 77.76% | +38.47pp |
| Latvian (lv) | 48 | 62.50% | 75.00% | +12.50pp | 56.46% | 74.84% | +18.38pp |
| Mongolian (mn) | 46 | 47.83% | 78.26% | +30.43pp | 31.94% | 75.92% | +43.98pp |
| Lao (lo) | 44 | 68.18% | 70.45% | +2.27pp | 68.80% | 68.63% | -0.17pp |
| Georgian (ka) | 41 | 41.46% | 75.61% | +34.15pp | 37.59% | 71.54% | +33.95pp |
| Sanskrit (sa) | 22 | 68.18% | 81.82% | +13.64pp | 65.56% | 78.89% | +13.33pp |
| Catalan (ca) | 21 | 61.90% | 85.71% | +23.81pp | 63.83% | 86.25% | +22.42pp |
| Bosnian (bs) | 20 | 75.00% | 85.00% | +10.00pp | 74.64% | 83.87% | +9.23pp |
| Irish (ga) | 20 | 35.00% | 55.00% | +20.00pp | 17.28% | 54.43% | +37.15pp |
| Malagasy (mg) | 20 | 50.00% | 75.00% | +25.00pp | 29.76% | 73.26% | +43.50pp |
| Welsh (cy) | 19 | 36.84% | 78.95% | +42.11pp | 23.33% | 76.67% | +53.34pp |
| Macedonian (mk) | 19 | 89.47% | 89.47% | +0.00pp | 91.07% | 91.07% | +0.00pp |
| Belarusian (be) | 18 | 61.11% | 72.22% | +11.11pp | 54.56% | 64.59% | +10.03pp |
| Basque (eu) | 18 | 33.33% | 72.22% | +38.89pp | 16.67% | 71.39% | +54.72pp |
| Latin (la) | 18 | 55.56% | 88.89% | +33.33pp | 37.78% | 81.75% | +43.97pp |
| Serbo-Croatian (sh) | 18 | 83.33% | 88.89% | +5.56pp | 82.44% | 88.97% | +6.53pp |
| Yiddish (yi) | 18 | 44.44% | 33.33% | -11.11pp | 20.51% | 42.91% | +22.40pp |
| Scottish Gaelic (gd) | 17 | 52.94% | 58.82% | +5.88pp | 23.08% | 55.58% | +32.50pp |
| Galician (gl) | 17 | 82.35% | 88.24% | +5.89pp | 81.10% | 84.72% | +3.62pp |
| Icelandic (is) | 17 | 47.06% | 64.71% | +17.65pp | 34.21% | 47.22% | +13.01pp |
| Oromo (om) | 17 | 41.18% | 58.82% | +17.64pp | 19.44% | 53.53% | +34.09pp |
| Xhosa (xh) | 17 | 35.29% | 47.06% | +11.77pp | 17.39% | 33.33% | +15.94pp |
| Breton (br) | 16 | 37.50% | 68.75% | +31.25pp | 35.56% | 70.56% | +35.00pp |
| Estonian (et) | 16 | 68.75% | 62.50% | -6.25pp | 67.97% | 63.57% | -4.40pp |
| Western Frisian (fy) | 16 | 68.75% | 62.50% | -6.25pp | 68.81% | 62.63% | -6.18pp |
| Javanese (jv) | 16 | 81.25% | 87.50% | +6.25pp | 77.46% | 82.37% | +4.91pp |
| Kurdish (ku) | 16 | 68.75% | 75.00% | +6.25pp | 47.62% | 82.14% | +34.52pp |
| Albanian (sq) | 16 | 68.75% | 81.25% | +12.50pp | 60.00% | 80.94% | +20.94pp |
| Sundanese (su) | 16 | 68.75% | 68.75% | +0.00pp | 71.31% | 72.03% | +0.72pp |
| Uyghur (ug) | 16 | 50.00% | 68.75% | +18.75pp | 22.22% | 48.81% | +26.59pp |
| Esperanto (eo) | 15 | 93.33% | 66.67% | -26.66pp | 91.58% | 67.74% | -23.84pp |
