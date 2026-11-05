---
license: apache-2.0
datasets:
- BioMike/formal-logic-reasoning-gliclass-2k
- knowledgator/gliclass-v3-logic-dataset
- tau/commonsense_qa
metrics:
- f1
tags:
- text classification
- nli
- sentiment analysis
pipeline_tag: text-classification
---

![image/png](instruct.png)

# GLiClass-multitask: Efficient zero-shot and few-shot multi-task model via sequence classification

GLiClass is an efficient zero-shot sequence classification model designed to achieve SoTA performance while being much faster than cross-encoders and LLMs, while preserving strong generalization capabilities.

The model supports text classification with any labels and can be used for the following tasks:
* Topic Classification
* Sentiment Analysis
* Intent Classification
* Reranking
* Hallucination Detection
* Rule-following Verification
* LLM-safety Classification
* Natural Language Inference

## ✨ What's New in V3

- **Hierarchical Labels** — Organize labels into groups using dot notation or dictionaries (e.g., `sentiment.positive`, `topic.product`).
- **Few-Shot Examples** — Provide in-context examples to boost accuracy on your specific task.
- **Label Descriptions** — Add natural-language descriptions to labels for more precise classification.
- **Task Prompts** — Prepend a custom prompt to guide the model's classification behavior.

See the [GLiClass library README](https://github.com/Knowledgator/GLiClass) for full details on these features.

## Installation

```bash
pip install gliclass
```

## Quick Start

```python
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

model = GLiClassModel.from_pretrained("knowledgator/gliclass-instruct-edge-v1.0")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-instruct-edge-v1.0")
pipeline = ZeroShotClassificationPipeline(model, tokenizer, classification_type='multi-label', device='cuda:0')
```

---

## Task Examples

### 1. Topic Classification

```python
text = "NASA launched a new Mars rover to search for signs of ancient life."
labels = ["space", "politics", "sports", "technology", "health"]

results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

#### With hierarchical labels

```python
hierarchical_labels = {
    "science": ["space", "biology", "physics"],
    "society": ["politics", "economics", "culture"]
}

results = pipeline(text, hierarchical_labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
# e.g. science.space => 0.95
```

### 2. Sentiment Analysis

```python
text = "The food was excellent but the service was painfully slow."
labels = ["positive", "negative", "neutral"]

results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

#### With a task prompt

```python
results = pipeline(
    text, labels,
    prompt="Classify the sentiment of this restaurant review:",
    threshold=0.5
)[0]
```

### 3. Intent Classification

```python
text = "Can you set an alarm for 7am tomorrow?"
labels = ["set_alarm", "play_music", "get_weather", "send_message", "set_reminder"]

results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

#### With few-shot examples

```python
examples = [
    {"text": "Wake me up at 6:30.", "labels": ["set_alarm"]},
    {"text": "Play some jazz.", "labels": ["play_music"]},
]

results = pipeline(text, labels, examples=examples, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

### 4. Natural Language Inference

Represent your premise as the text and the hypothesis as a label. The model works best with a single hypothesis at a time.

```python
text = "The cat slept on the windowsill all afternoon."
labels = ["The cat was awake and playing outside."]

results = pipeline(text, labels, threshold=0.0)[0]
print(results)
# Low score → contradiction
```

### 5. Reranking

Score query–passage relevance by treating passages as texts and the query as the label:

```python
query = "How to train a neural network?"
passages = [
    "Backpropagation is the key algorithm for training deep neural networks.",
    "The stock market rallied on strong earnings reports.",
    "Gradient descent optimizes model weights during training.",
]

for passage in passages:
    score = pipeline(passage, [query], threshold=0.0)[0][0]["score"]
    print(f"{score:.3f}  {passage[:60]}")
```

### 6. Hallucination Detection

Concatenate context, question, and answer into the text field:

```python
text = (
    "Context: The Eiffel Tower was built from 1887 to 1889 and is 330 m tall. "
    "It was the tallest structure until the Chrysler Building in 1930.\n"
    "Question: When was the Eiffel Tower built and how tall is it?\n"
    "Answer: It was built 1887–1889, stands 330 m tall, and was the tallest "
    "structure until the Empire State Building in 1931."
)
labels = ["hallucinated", "correct"]

results = pipeline(text, labels, threshold=0.0)[0]
for r in results:
    print(r["label"], "=>", r["score"])
# "hallucinated" should score higher (Empire State Building & 1931 are wrong)
```

### 7. Rule-following Verification

Include the domain and rules as part of the text:

```python
text = (
    "Domain: e-commerce product reviews\n"
    "Rule: No promotion of illegal activity.\n"
    "Text: The software is okay, but search for 'productname_patch_v2.zip' "
    "to unlock all features for free."
)
labels = ["follows_guidelines", "violates_guidelines"]

results = pipeline(text, labels, threshold=0.0)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

### 8. LLM-safety Classification

```python
text = "I'm looking for a good Italian restaurant near downtown Chicago, budget ~$50/person."
labels = [
    "benign request",
    "prompt injection",
    "system prompt extraction",
    "jailbreak attempt",
    "harmful content request",
    "social engineering",
    "data exfiltration",
]

results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

---

## Benchmarks

F1 scores on zero-shot text classification (no fine-tuning on these datasets):

GLiClass-V1 Multitask:

| Dataset | [large‑v1.0](https://huggingface.co/knowledgator/gliclass-instruct-large-v1.0) | [base‑v1.0](https://huggingface.co/knowledgator/gliclass-instruct-base-v1.0) | [edge‑v1.0](https://huggingface.co/knowledgator/gliclass-instruct-edge-v1.0) |
|---|---|---|---|
| CR | 0.9066 | 0.8922 | 0.7933 |
| sst2 | 0.9154 | 0.9198 | 0.7577 |
| sst5 | 0.3387 | 0.2266 | 0.2163 |
| 20_newsgroups | 0.5577 | 0.5189 | 0.2555 |
| spam | 0.9790 | 0.9380 | 0.7609 |
| financial_phrasebank | 0.8289 | 0.5217 | 0.3905 |
| imdb | 0.9397 | 0.9364 | 0.8159 |
| ag_news | 0.7521 | 0.6978 | 0.6043 |
| emotion | 0.4473 | 0.4454 | 0.2941 |
| cap_sotu | 0.4327 | 0.4579 | 0.2380 |
| rotten_tomatoes | 0.8491 | 0.8458 | 0.5455 |
| massive | 0.5824 | 0.4757 | 0.2090 |
| banking | 0.6987 | 0.6072 | 0.4635 |
| snips | 0.8509 | 0.6515 | 0.5461 |
| **AVERAGE** | **0.7199** | **0.6525** | **0.4922** |

GLiClass-V3:

| Dataset | [large‑v3.0](https://huggingface.co/knowledgator/gliclass-large-v3.0) | [base‑v3.0](https://huggingface.co/knowledgator/gliclass-base-v3.0) | [modern‑large‑v3.0](https://huggingface.co/knowledgator/gliclass-modern-large-v3.0) | [modern‑base‑v3.0](https://huggingface.co/knowledgator/gliclass-modern-base-v3.0) | [edge‑v3.0](https://huggingface.co/knowledgator/gliclass-edge-v3.0) |
|---|---|---|---|---|---|
| CR | 0.9398 | 0.9127 | 0.8952 | 0.8902 | 0.8215 |
| sst2 | 0.9192 | 0.8959 | 0.9330 | 0.8959 | 0.8199 |
| sst5 | 0.4606 | 0.3376 | 0.4619 | 0.2756 | 0.2823 |
| 20_newsgroups | 0.5958 | 0.4759 | 0.3905 | 0.3433 | 0.2217 |
| spam | 0.7584 | 0.6760 | 0.5813 | 0.6398 | 0.5623 |
| financial_phrasebank | 0.9000 | 0.8971 | 0.5929 | 0.4200 | 0.5004 |
| imdb | 0.9366 | 0.9251 | 0.9402 | 0.9158 | 0.8485 |
| ag_news | 0.7181 | 0.7279 | 0.7269 | 0.6663 | 0.6645 |
| emotion | 0.4506 | 0.4447 | 0.4517 | 0.4254 | 0.3851 |
| cap_sotu | 0.4589 | 0.4614 | 0.4072 | 0.3625 | 0.2583 |
| rotten_tomatoes | 0.8411 | 0.7943 | 0.7664 | 0.7070 | 0.7024 |
| massive | 0.5649 | 0.5040 | 0.3905 | 0.3442 | 0.2414 |
| banking | 0.5574 | 0.4698 | 0.3683 | 0.3561 | 0.0272 |
| snips | 0.9692 | 0.9474 | 0.7707 | 0.5663 | 0.5257 |
| **AVERAGE** | **0.7193** | **0.6764** | **0.6197** | **0.5577** | **0.4900** |

## Citation

```bibtex
@misc{stepanov2025gliclassgeneralistlightweightmodel,
      title={GLiClass: Generalist Lightweight Model for Sequence Classification Tasks}, 
      author={Ihor Stepanov and Mykhailo Shtopko and Dmytro Vodianytskyi and Oleksandr Lukashov and Alexander Yavorskyi and Mykyta Yaroshenko},
      year={2025},
      eprint={2508.07662},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2508.07662}, 
}
```