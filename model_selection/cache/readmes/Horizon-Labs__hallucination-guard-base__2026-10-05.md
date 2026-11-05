---
license: apache-2.0
language:
- multilingual
- en
- de
- fr
- es
- pt
- it
- nl
- pl
- ru
- uk
- tr
- ar
- hi
- zh
- ja
- ko
- vi
- id
- th
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-base
tags:
- hallucination-detection
- groundedness
- faithfulness
- fact-checking
- rag
- llm-evaluation
- guardrails
- nli
- modernbert
- mmbert
- onnx
- transformers.js
datasets:
- wandb/RAGTruth-processed
- alisawuffles/WANLI
---

# Hallucination Guard (base, 308M)

A small, **multilingual groundedness checker**. Given a source (retrieved documents, a transcript, a tool result) and
an AI response or claim, it predicts whether the response is **supported** by the source. Use it to flag RAG answers,
summaries and agent outputs that add, change or contradict facts.

- **Multilingual**: trained on data in 30 languages. On HaluEval translated into six languages it stays at the level
  of its English score, while English-only checkers drop (table below).
- **Long context**: 8k-token window (trained at 2k); long sources can also be chunked (see below).
- **Open**: Apache-2.0, ungated. Trained on permissively licensed data and Qwen-generated synthetic data. ONNX
  included.
- **Honest about where it loses**: on English claim-level fact-checking (LLM-AggreFact), MiniCheck and HHEM are
  better. If you only need English, compare them on your data.

Try it in the browser: [Horizon-Labs/hallucination-guard demo](https://huggingface.co/spaces/Horizon-Labs/hallucination-guard).

Part of [Agent I/O Guards](https://huggingface.co/collections/Horizon-Labs/agent-i-o-guards-6ab403c49494bc2b71ca7669)
(prompt injection, PII, groundedness). Source code: [github.com/horizon-ai-labs/agent-io-guards](https://github.com/horizon-ai-labs/agent-io-guards).

## Quick start

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/hallucination-guard-base")
doc = "The Eiffel Tower is 330 metres tall and was completed in 1889 for the World's Fair."
clf({"text": doc, "text_pair": "The tower was finished in 1889."})   # SUPPORTED
clf({"text": doc, "text_pair": "The tower was finished in 1899."})   # UNSUPPORTED
```

Put the **source first** and the **response or claim second**. Labels: `UNSUPPORTED` (0) and `SUPPORTED` (1).
The score for `SUPPORTED` is the support probability.

For long sources, or to find *which* sentence is unsupported, split the response into sentences and score each one
against the source. For a response-level score, take the minimum over sentences:

```python
import re
def check(source, response, clf=clf):
    sents = [s for s in re.split(r"(?<=[.!?。！？])\s+", response) if s.strip()]
    res = clf([{"text": source, "text_pair": s} for s in sents], truncation=True, max_length=2048)
    return [(s, r["label"], r["score"]) for s, r in zip(sents, res)]
```

## Evaluation

Balanced accuracy at a 0.5 threshold. All models were run by us with the same script
(`ground/evaluate_ground.py`). MiniCheck used context chunking with max over chunks, as its own library does. HHEM
used contexts capped at 12,000 characters, because it ran out of memory on the longest documents. † marks sets that are
**in-distribution for our models**: we trained on RAGTruth's train split, and those rows use its test split.

### LLM-AggreFact (English claim verification, 11 datasets, up to 1,000 examples each)

| | **this model** | small (141M) | MiniCheck-RoBERTa-L | MiniCheck-DeBERTa-L | HHEM-2.1-open |
|---|---|---|---|---|---|
| AggreFact-CNN | 0.618 | 0.607 | **0.664** | 0.622 | 0.629 |
| AggreFact-XSum | 0.622 | 0.644 | **0.709** | 0.688 | 0.706 |
| ClaimVerify | 0.737 | 0.682 | **0.783** | 0.744 | 0.753 |
| ExpertQA | 0.593 | 0.553 | **0.606** | 0.597 | 0.568 |
| FactCheck-GPT | 0.674 | 0.657 | **0.754** | 0.728 | 0.729 |
| LFQA | 0.813 | 0.726 | **0.863** | 0.838 | 0.839 |
| RAGTruth † | **0.815** | 0.796 | 0.788 | 0.773 | 0.734 |
| Reveal | 0.834 | 0.798 | **0.896** | 0.871 | 0.865 |
| TofuEval-MediaS | **0.707** | 0.654 | 0.696 | 0.676 | 0.679 |
| TofuEval-MeetB | 0.736 | 0.677 | **0.765** | 0.724 | 0.721 |
| Wice | 0.732 | 0.719 | 0.717 | 0.664 | **0.751** |
| **Mean** | 0.716 | 0.683 | **0.749** | 0.721 | 0.725 |

### Multilingual: HaluEval QA and dialogue, translated (400 items per language)

The items were machine-translated with Qwen3.8-27B, keeping their labels. They are disjoint from the English HaluEval
items above. Caveat: the translations come from the same model family we used to generate synthetic training data,
which may favour our model somewhat.

| | **this model** | small (141M) | MiniCheck-RoBERTa-L | MiniCheck-DeBERTa-L | HHEM-2.1-open |
|---|---|---|---|---|---|
| English | **0.720** | 0.657 | 0.589 | 0.670 | 0.701 |
| German | **0.724** | 0.719 | 0.691 | 0.672 | 0.670 |
| Spanish | **0.714** | 0.691 | 0.650 | 0.675 | 0.675 |
| Chinese | **0.738** | 0.713 | 0.627 | 0.621 | 0.546 |
| Japanese | **0.751** | 0.729 | 0.626 | 0.669 | 0.546 |
| Arabic | **0.710** | 0.700 | 0.616 | 0.691 | 0.544 |
| Hindi | **0.740** | 0.730 | 0.595 | 0.670 | 0.564 |
| **Mean of the 6 non-English languages** | **0.729** | 0.714 | 0.634 | 0.666 | 0.591 |

### Versions

v1.1 (this version) adds about 147k multi-sentence claim pairs (claims whose facts are spread over several sentences of
the source, and the same pairs with one needed sentence removed). It is better on English claim-level fact-checking
(LLM-AggreFact). On translated HaluEval it scores lower than v1.0, but a large part of that gap is training noise:
retraining the v1.0 recipe with another random seed gives very different HaluEval numbers (rows below). The translated-
HaluEval AUC is consistently about 0.02 lower with the v1.1 data, so part of the difference is real. Pin the previous
model with `revision="v1.0"`.

| | AggreFact bacc | AggreFact AUC | 6 languages bacc | 6 languages AUC | HaluEval QA | RAGTruth |
|---|---|---|---|---|---|---|
| v1.0 (released) | 0.697 | 0.773 | 0.755 | 0.802 | 0.817 | 0.821 |
| v1.0 recipe, another seed | 0.702 | 0.768 | 0.684 | 0.786 | 0.738 | 0.809 |
| **v1.1 (this version)** | 0.716 | 0.796 | 0.729 | 0.774 | 0.782 | 0.829 |
| v1.1 recipe, another seed | 0.711 | 0.794 | 0.706 | 0.777 | 0.714 | 0.822 |

### Other benchmarks

| | **this model** | small (141M) | MiniCheck-RoBERTa-L | MiniCheck-DeBERTa-L | HHEM-2.1-open |
|---|---|---|---|---|---|
| HaluEval QA | **0.782** | 0.691 | 0.635 | 0.768 | 0.762 |
| HaluEval dialogue | 0.635 | **0.643** | 0.522 | 0.524 | 0.625 |
| HaluEval summarization | 0.559 | 0.548 | **0.648** | 0.623 | 0.526 |
| RAGTruth test, response level † | **0.829** | 0.798 | 0.604 | 0.626 | 0.750 |

## Limitations

- On English claim-level fact-checking, MiniCheck-RoBERTa-L (0.749) and HHEM (0.725) beat this model
  (0.716) on LLM-AggreFact. Our advantage is in other languages, and in QA and dialogue grounding.
- It judges support by the given source only. It is not a world-knowledge fact checker: a true statement that the
  source doesn't contain is `UNSUPPORTED`.
- Simple arithmetic or temporal inferences are often marked `UNSUPPORTED`. For example, "opened before 2022" given a
  source that says "opened in March 2021". The small model also misses some paraphrases ("weekdays" for "Monday to
  Friday") that the base model handles.
- Summaries with many small details (HaluEval summarization) and expert long-form answers (ExpertQA) are hard for
  every model here.
- Much of the training data is synthetic (Qwen3.8-27B). The multilingual numbers come from translated data, not native
  benchmarks.

## Training

- Backbone: [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base) (MIT), sequence-pair classification, max length 2048,
  bf16.
- About 340k (source, response) pairs:
  - Qwen3.8-27B-generated responses over FineWeb-Edu / FineWeb-2 passages (ODC-BY) in 29 languages: supported
    answers and minimally edited unsupported variants, at both response and sentence level.
  - Qwen-generated documents in 18 genres (news, meeting transcripts, support chats, retrieved snippets, reviews,
    contracts…) with supported and unsupported claims, in 30 languages.
  - [RAGTruth](https://huggingface.co/datasets/wandb/RAGTruth-processed) train split (MIT), response level.
  - [WANLI](https://huggingface.co/datasets/alisawuffles/WANLI) (CC-BY-4.0).
  - (v1.1) About 147k multi-sentence claim pairs generated with Qwen3.8-27B (`code/ground/gen_c2d.py`): invented documents whose facts are spread over different sentences, and FineWeb / FineWeb-2 passages with claims that combine 2-3 sentences; unsupported versions remove one needed sentence. About 40% English.
- Not used: ANLI and other non-commercial NLI data, DocNLI (derived from non-commercial sources), and every benchmark
  above except RAGTruth's train split.
