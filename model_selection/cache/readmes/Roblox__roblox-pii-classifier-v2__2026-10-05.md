---
license: apache-2.0
language: multilingual
tags:
- privacy
- pii-detection
- text-classification
- xlm-roberta
library_name: transformers
base_model: FacebookAI/xlm-roberta-large
datasets:
- ai4privacy/pii-masking-openpii-1.5m
- nvidia/Nemotron-PII
- Roblox/roblox-pii-classifier-benchmark
---

# Roblox PII Classifier v2

## Overview
We present `Roblox/roblox-pii-classifier-v2`, an upgraded, context-aware PII (Personally Identifiable Information) detection model. Built on the [XLM-RoBERTa-Large](https://huggingface.co/xlm-roberta-large) architecture, v2 is designed to identify attempts to share or solicit personal information across complex, multi-user conversations. 

Unlike its predecessor and other NER models, **v2 evaluates text within its surrounding conversational context**, allowing it to detect sophisticated, adversarial bypass attempts (e.g., collaborative PII exchange, phonetic spelling, implicit references) while drastically reducing false positives. It is intended for use in casual conversations, ensuring freedom of speech while also maintaining safety.

## What’s New in v2?

* **Conversational Context Integration:** Evaluates target messages within the broader multi-user chat context, eliminating ambiguity inherent in isolated messages.
* **Massive Multilingual Expansion:** Broadened synthetic data generation and fine-tuning capabilities to expand language coverage from **17 to 189 languages**.
* **Automated Red-Teaming & Clustering:** Applied automated adversarial red-teaming and cluster visualization to systematically surface, isolate, and patch model vulnerabilities.
* **Significant Performance Leap:** Overall F1 score increased from **63.41% to 90.52%** on our refreshed internal evaluation set, with a f1 score increase from **64.74% to 88.78%** on the recently released roblox-pii-safety-for-chat-benchmark.

## Model Architecture & Classification Scope

**Input Format:** A single pre-formatted string containing a fixed instruction
prefix followed by the target message and its surrounding multi-turn chat
history. Speakers are anonymized — the speaker under evaluation is always `t`,
and all other participants are mapped to `s1`, `s2`, … in order of first
appearance. Turns are joined with ` </s> `:

```
Instruct: In the following chat messages from target speaker t and possibly other speakers s1, s2, etc., detect abuse by speaker t.
Query:

t: {text} </s> s1: {text} </s> t: {text}
```

Tokenized with the XLM-RoBERTa SentencePiece tokenizer to a **fixed 512
tokens**, `padding="max_length"`, `truncation=True`, and — critically —
**`truncation_side="left"`**, so that when history overflows the window the
*oldest* turns are dropped and the latest target message is retained.

**Outputs:** 
The model performs multi-label classification scores obtained by applying an
**element-wise sigmoid** to the logits across three PII categories,
emitted in this fixed index order:

| Index | Label | Threshold Recommendation | Definition |
|---|---|---|---|
| 0 | **`privacy_asking_for_pii`** | 0.60 | Attempts to obtain personal identifying information via direct or implicit methods. |
| 1 | **`privacy_giving_pii`** | 0.55 | Sharing PII — including phone numbers, email addresses, government IDs, social media handles, and credentials. |
| 2 | **`directing_users_off_platform`** | 0.10 | Attempting to move a user off-platform to external apps, services, or websites. |

## Benchmark Comparisons

The table below illustrates best f1 performance across internal and open-source evaluation benchmarks (full conversational data used when possible):

| Dataset / Benchmark | Roblox PII v2 | *Roblox PII v1 | *OpenAI Privacy Filter | *GLiNER2 | Qwen3Guard Gen 8B | LlamaGuard v3 1B | LlamaGuard v3 8B | LlamaGuard v4 12B | NemoGuard 8B | *Piiranha NER | Shieldstral |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **roblox-pii-safety-for-chat** | **88.82%** | 64.69% | 58.16% | 54.50% | 66.24% | 27.89% | 56.24% | 54.56% | 56.52% | 58.34% | 57.84% |
| **Roblox Internal Evaluation** | **90.52%** | 63.41% | 20.98% | 28.21% | 15.62% | 8.59% | 12.90% | 21.92% | 14.77% | 20.98% | 31.87 |
| **Nemotron-PII** | **99.22%** | 70.07% | 65.22% | 62.92% | 37.46% | 53.32% | 46.07% | 35.05% | 56.16% | 68.52% | 56.69 |
| **PII Masking OpenPII 1.5M** | **99.76%** | 86.79% | 84.23% | 83.07% | 61.94% | 65.10% | 64.23% | 56.16% | 54.01% | 86.35% | 85.33 |

\* These models all were supplied with only the target-user text as other speaker texts are meant to be supplemental contextual information. roblox-pii-classifier-v2 performs best when supplied with conversational context, however it still outperforms roblox-pii-classifier when supplied only with target-user text. 


## Usage
Install the inference dependencies:
```bash
pip install -r requirements.txt
```

For a single message, pass the raw text. `inference.py` treats it as one turn
from the target speaker `t` and adds the required instruction prefix
automatically:

```bash
python inference.py --model-path . \
  --text "add me on Discord, my username is skyfox_4821"
```

For conversational inference, create a UTF-8 JSON file containing a list of
turns. The speaker whose behavior should be classified **must** be named `t`.
Other speaker names may be arbitrary; the formatter anonymizes them to `s1`,
`s2`, and so on in order of first appearance.

```bash
cat > conversation.json <<'JSON'
[
  {"speaker": "alice", "text": "how can I contact you?"},
  {"speaker": "t", "text": "add me on Discord, my username is skyfox_4821"},
  {"speaker": "alice", "text": "okay, got it"}
]
JSON

python inference.py --model-path . --input-file conversation.json
```