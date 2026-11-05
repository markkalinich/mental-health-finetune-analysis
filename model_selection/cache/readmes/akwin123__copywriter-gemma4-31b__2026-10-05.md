---
license: gemma
base_model: google/gemma-4-31b-it
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- copywriting
- marketing
- advertising
- ad-copy
- sales-copy
- email-marketing
- direct-response
- conversion-copywriting
- gemma
- gemma-4
- text-generation
- emotional-intelligence
- conversational
---

# Copywriter-Gemma4-31B

**An AI copywriting LLM model that writes like a senior direct-response copywriter — not a chatbot.**

Copywriter-Gemma4-31B is a 31-billion-parameter large language model fine-tuned from **Google Gemma-4-31B-it** for one job done exceptionally well: **writing high-converting marketing copy**. Facebook and Google ads, cold emails, landing pages, product descriptions, sales pages, video scripts, taglines, SMS campaigns, and more — in a punchy, specific, human voice that sells.

In a blind, order-balanced head-to-head judged by **DeepSeek V4 Flash**, it **wins 80% of matchups against its own base model** and lifts its preference Elo by **+290 points**.

---

## TL;DR

| | |
|---|---|
| 🧠 **What it is** | A Gemma-4-31B model specialized for copywriting & marketing |
| 🏆 **Headline result** | **Elo 1657 vs 1367** for base — **wins 24 of 30** head-to-head briefs (80%) |
| ⚖️ **Judge** | DeepSeek V4 Flash, blind pairwise (both orderings) |
| ✍️ **Best at** | Ad copy, email, landing pages, hooks, product copy, scripts |
| 📐 **Context** | 256K tokens · bfloat16 · drops into vLLM / Transformers |

---

## Why this model exists

General-purpose chat models *can* write copy, but they default to the same tells: hedging, throat-clearing intros, vague benefit-speak, and "In today's fast-paced world…" openers. Copywriter-Gemma4-31B was trained to do what great copywriters do instead — **lead with the pain, get specific, cut the fluff, and earn the click.**

It was fine-tuned on a large, curated corpus of marketing copy that includes **thousands of gold-standard, real-world ad examples**, so it has internalized the patterns of copy that actually performs rather than copy that merely sounds polished.

---

## Benchmark Results

Most model cards make claims. This one shows the scoreboard.

We built a copywriting-specific evaluation on top of the **EQ-Bench 3** methodology (pairwise Elo + a multi-dimension rubric), swapping in **30 real-world copywriting briefs** spanning Facebook ads, cold email, LinkedIn posts, landing pages, product descriptions, SMS, scripts, press releases, and more. Every brief was answered by both the **base** model and the **fine-tuned** model, then scored by an independent **DeepSeek V4 Flash** judge.

To remove position bias, **every matchup was judged in both orderings** (A-vs-B and B-vs-A). Both models ran on the *identical* base weights and decoding settings — the only variable is the fine-tune.

### Main metric — preference Elo

| Model | Elo | Head-to-head vs base |
|---|---:|---|
| **Copywriter-Gemma4-31B** | **1657** 🥇 | **wins 24 / 30 (80%)** |
| Gemma-4-31B-it (base) | 1367 | — |

**+290 Elo.** When a neutral judge is asked *"which piece of copy is better?"*, it picks Copywriter-Gemma4-31B **four times out of five.**

### Ability profile

Across the rubric's seven copywriting dimensions, the fine-tune shows its biggest, most consistent gains exactly where direct-response copy lives:

- ✅ **Hook strength** — stronger, scroll-stopping openers
- ✅ **Specificity** — concrete details over generic benefit-speak
- ✅ **Concision** — tighter copy, less filler

> **Method notes:** judge = `deepseek-v4-flash`; 30 briefs; pairwise scoring in both orderings plus per-dimension rubric. Both the base and the fine-tune were served **identically** — same 31B base, same 4-bit quantization at inference, same decoding — so the only variable is the fine-tune. The weights published here are that **same fine-tune merged to full bf16 precision** (the higher-fidelity form of the model that produced these scores). Elo is computed *relative to the base model* on this brief set — a controlled A/B signal, not a public-leaderboard number.

### ⚡ Achieved in direct mode — no "thinking" required - It's Bad

Every result above was generated in **direct (non-thinking) mode** — `enable_thinking=false` (the default), so the model wrote finished copy in a **single pass with zero reasoning tokens.** No chain-of-thought overhead, no extra latency or cost — it just writes.

Gemma 4 *does* support an optional reasoning mode (`enable_thinking=True` → `<|think|>` channel) if you want it for unusually complex briefs, but the scores above prove it isn't needed for strong copy. Fast by default.

NOTE: Thinking must be off for best results.
---

## What it's good at

Copywriter-Gemma4-31B is built for **marketing and growth teams, agencies, founders, and solo creators** who need on-brand copy fast:

- **Paid ads** — Facebook / Instagram / Meta ad copy, Google responsive search ads, primary text + headlines
- **Email** — cold outreach, welcome sequences, re-engagement, abandoned-cart, newsletters
- **Web** — landing pages, hero sections, value props, feature/benefit bullets, CTAs
- **Ecommerce** — product titles & descriptions, Amazon bullets, offer stacks
- **Social** — hooks, LinkedIn posts, short-form video scripts, captions, taglines
- **Lifecycle** — SMS campaigns, push notifications, upsell/order-bump copy

---

## Model details

| | |
|---|---|
| **Base model** | [google/gemma-4-31b-it](https://huggingface.co/google/gemma-4-31b-it) |
| **Parameters** | ~31B |
| **Architecture** | Gemma 4 (`Gemma4ForConditionalGeneration`) |
| **Context length** | 262,144 tokens (256K) |
| **Precision** | bfloat16 |
| **Format** | Safetensors (sharded) — vLLM / Transformers ready |
| **Fine-tuning** | Supervised fine-tuning (QLoRA) on a curated copywriting corpus |
| **Language** | English |
| **License** | Gemma (see below) |

---

## Training

Copywriter-Gemma4-31B was produced by **supervised fine-tuning** of Gemma-4-31B-it on a large, purpose-built copywriting dataset assembled and cleaned specifically for this project. The corpus pairs marketing briefs with high-quality completions and includes **thousands of gold-standard, real-world advertisements** so the model learns the rhythm, structure, and restraint of copy that converts — strong hooks, concrete specifics, tight CTAs, and a human voice.

The final weights are the **full fine-tuned model merged to bfloat16** (not an adapter), so it loads like any standard Hugging Face model.

---

## Usage

### vLLM (recommended for serving)

```bash
vllm serve akwin123/copywriter-gemma4-31b --dtype bfloat16
```

### Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "akwin123/copywriter-gemma4-31b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

brief = (
    "Write a punchy Facebook ad for a budgeting app aimed at college students. "
    "Lead with the pain point and finish with a clear call to action. Keep it tight."
)
messages = [{"role": "user", "content": brief}]
inputs = tokenizer.apply_chat_template(
    messages, return_tensors="pt", add_generation_prompt=True
).to(model.device)

outputs = model.generate(
    inputs, max_new_tokens=512, do_sample=True, temperature=0.7, min_p=0.1
)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

> *Note: Gemma 4 is a multimodal architecture. If `AutoModelForCausalLM` does not resolve on your Transformers version, load it via the `Gemma4ForConditionalGeneration` class — text generation works the same way.*

### Recommended decoding

| Setting | Value | Why |
|---|---|---|
| `temperature` | `0.7` | lively but on-brief |
| `min_p` | `0.1` | trims low-probability noise |
| `max_new_tokens` | `256–1024` | by format |

---

## Prompting tips

- **Give it the brief, not just the product.** Audience, offer, channel, tone, and the *one* action you want — the more context, the sharper the copy.
- **Ask for the angle.** "Lead with the pain," "make it curiosity-driven," "benefit-first," "contrarian hook."
- **Ask for variations.** It's strong at generating multiple distinct headlines/subject lines you can A/B test.
- **Specify length and format** (e.g., "3 SMS messages under 160 characters," "a 30-second VO script").

---

## Limitations & scope

- **English, marketing-focused.** Outside copywriting/marketing it behaves like a general Gemma-4 model.
- **Occasional repetition** on long enumerations (e.g., "give me 10 taglines"); a touch of `temperature`/`min_p` or asking for fewer, better options resolves it.
- **Not a fact-checker.** It will write whatever claims the brief implies — review for accuracy, legal/regulatory compliance, and brand safety before publishing. Always keep a human in the loop.
- **Not for medical, legal, financial, or safety-critical advice.**

---

## License

This model is derived from Google's Gemma-4 and is released under the **[Gemma Terms of Use](https://ai.google.dev/gemma/terms)**. By using these weights you agree to the Gemma license and Google's [Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy). Use must comply with all upstream terms.

---

## Dataset licensing & commercial inquiries

The **curated copywriting dataset** behind this model — instruction and preference data and more, including **thousands of gold-standard real-world ad examples** — is **available for licensing**. It's the same proven corpus that produced the benchmark results above, ideal for teams training their own marketing/copywriting models.

📩 **For dataset licensing, custom fine-tunes, or commercial partnerships, get in touch: [akash@adlavishmedia.com](mailto:akash@adlavishmedia.com)**

---

## About

Copywriter-Gemma4-31B is an independent fine-tune focused on practical, high-performing marketing copy. If you build with it, benchmark it, or find failure cases, contributions and feedback are welcome on the repository's Community tab.

*Built on Gemma-4-31B-it · evaluated with an EQ-Bench-3-style pairwise harness · judged by DeepSeek V4 Flash.*