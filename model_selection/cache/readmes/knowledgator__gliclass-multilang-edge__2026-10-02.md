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
language:
- en
- sv
- cs
- pl
- lt
- et
- lv
- es
- fi
- de
- fr
- ro
- it
- pt
- nl
- uk
- hi
- zh
- ar
- he
---

![image/png](gliclass_multilang.png)

![Multilingual Quality vs Throughput](model_comparison_multi.png)

# GLiClass Multilang: Efficient multilingual zero-shot and few-shot multi-task model via sequence classification

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

## ✨ What's New in GLiClass Multilang
- **Multilingual Training** — Natively trained on 20 languages: Swedish, Norwegian, Czech, Polish, Lithuanian, Estonian, Latvian, Spanish, Finnish, German, French, Romanian, Italian, Portuguese, Dutch, Ukrainian, Hindi, Chinese, Arabic, and Hebrew.
- **Cross-lingual Classification** — Labels and input texts can be in different languages; classify a German document with English labels, or mix languages freely across inputs and labels.
- **CrossAttn Scorer** — A new cross-attention scorer enables more efficient pooling independently for each label with unpadding and flash-attn.
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

model = GLiClassModel.from_pretrained("knowledgator/gliclass-multilang-edge")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-multilang-edge")
pipeline = ZeroShotClassificationPipeline(model, tokenizer, classification_type='multi-label', device='cuda:0')

text = "NASA launched a new Mars rover to search for signs of ancient life."
labels = ["space", "politics", "sports", "technology", "health"]

results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

---
## Multilingual & Cross-lingual Capabilities

Natively trained on 20 languages. Labels and texts can be in different languages.

**Same language (German):**
```python
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

model = GLiClassModel.from_pretrained("knowledgator/gliclass-multilang-edge")
tokenizer = AutoTokenizer.from_pretrained("knowledgator/gliclass-multilang-edge")
pipeline = ZeroShotClassificationPipeline(model, tokenizer, classification_type='multi-label', device='cuda:0')

text = "Die NASA hat einen neuen Mars-Rover gestartet, um nach Spuren alten Lebens zu suchen."
labels = ["Weltraum", "Politik", "Sport", "Technologie", "Gesundheit"]
results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

**Cross-lingual (French text, English labels):**
```python
text = "Le gouvernement français a annoncé de nouvelles mesures économiques."
labels = ["economy", "politics", "sports", "technology"]
results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

**Cross-lingual (Arabic text, English labels):**
```python
text = "أطلقت ناسا مركبة جديدة للمريخ للبحث عن آثار الحياة القديمة."
labels = ["space", "politics", "sports", "technology"]
results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

**Cross-lingual (English text, Spanish labels):**
```python
text = "NASA launched a new Mars rover to search for signs of ancient life."
labels = ["espacio", "política", "deportes", "tecnología", "salud"]
results = pipeline(text, labels, threshold=0.5)[0]
for r in results:
    print(r["label"], "=>", r["score"])
```

<details>
<summary>General Examples</summary>

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

### 6. Rule-following Verification

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

</details>

---

## Benchmarks

### Model Overview

Summary across all evaluated multilingual-capable models (zero-shot, no fine-tuning). Speed averaged over all label counts and text lengths at batch_size=8 on NVIDIA RTX PRO 6000 Blackwell.

| Model | Params | English avg F1 | Multilingual avg F1 | Throughput (samp/s, bs=8) |
|---|---:|---:|---:|---:|
| [multilang‑ultra](https://huggingface.co/knowledgator/gliclass-multilang-ultra) | ~1 720M | **0.7212** | **0.5599** | 200.7 |
| [multilang‑mini](https://huggingface.co/knowledgator/gliclass-multilang-mini) | ~288M | 0.6827 | 0.5378 | **513.4** |
| [multilang‑edge](https://huggingface.co/knowledgator/gliclass-multilang-edge) | ~140M | 0.6196 | 0.3959 | **553.6** |
| [instruct‑large](https://huggingface.co/knowledgator/gliclass-instruct-large-v1.0) | ~435M | 0.7199 | — | 293.9 |
| [instruct‑base](https://huggingface.co/knowledgator/gliclass-instruct-base-v1.0) | ~184M | 0.6525 | — | 521.9 |
| [gliner2‑large‑v1](https://huggingface.co/fastino/gliner2-large-v1) | 340M | 0.6774 | — | 122.5 |
| [gliner2‑multi‑v1](https://huggingface.co/fastino/gliner2-multi-v1) | ~278M | 0.6387 | 0.4659 | 200.2 |
| [gliner2‑base‑v1](https://huggingface.co/fastino/gliner2-base-v1) | ~184M | 0.6336 | — | 224.0 |
| [bge‑m3‑zeroshot‑v2.0](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0) | 568M | 0.5927 | 0.5225 | 208.7 |
| [mDeBERTa‑mnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 300M | 0.5340 | 0.3926 | 160.6 |

> Multilingual avg F1 is the mean of 6 dataset-level scores (GermEval2017, MASSIVE, PolygloToxicityPrompts, SIB-200, TextDetox, TweetSentiment). Models without multilingual results (—) were only evaluated on English datasets.

---

F1 scores on zero-shot text classification (no fine-tuning on these datasets):

**Table A: GLiClass Multilang (macro F1)**

| Dataset | [multilang‑ultra](https://huggingface.co/knowledgator/gliclass-multilang-ultra) | [multilang‑mini](https://huggingface.co/knowledgator/gliclass-multilang-mini) | [multilang‑edge](https://huggingface.co/knowledgator/gliclass-multilang-edge) |
|---|---|---|---|
| CR | 0.9226 | 0.9042 | 0.8852 |
| sst2 | 0.9065 | 0.8810 | 0.8276 |
| sst5 | 0.3049 | 0.2806 | 0.3047 |
| 20_newsgroups | 0.5238 | 0.4242 | 0.3522 |
| spam | 0.9625 | 0.9385 | 0.6787 |
| financial_phrasebank | 0.8724 | 0.7156 | 0.7446 |
| imdb | 0.9330 | 0.9011 | 0.8730 |
| ag_news | 0.7454 | 0.7545 | 0.7338 |
| emotion | 0.4825 | 0.4655 | 0.4267 |
| cap_sotu | 0.4385 | 0.4087 | 0.3516 |
| rotten_tomatoes | 0.8413 | 0.8236 | 0.7044 |
| massive | 0.6483 | 0.5853 | 0.5649 |
| banking | 0.6492 | 0.5853 | 0.5788 |
| snips | 0.8653 | 0.8900 | 0.6487 |
| **AVERAGE** | **0.7212** | **0.6827** | **0.6196** |

**Table B: Baselines (macro F1)**

| Dataset | [gliner2‑large‑v1](https://huggingface.co/fastino/gliner2-large-v1) | [gliner2‑multi‑v1](https://huggingface.co/fastino/gliner2-multi-v1) | [gliner2‑base‑v1](https://huggingface.co/fastino/gliner2-base-v1) | [bge‑m3‑zeroshot‑v2.0](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0) | [mDeBERTa‑mnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) |
|---|---|---|---|---|---|
| CR | 0.9117 | 0.8785 | 0.8783 | 0.9041 | 0.8956 |
| sst2 | 0.8911 | 0.8568 | 0.8737 | 0.9257 | 0.8516 |
| sst5 | 0.4462 | 0.3784 | 0.4100 | 0.2931 | 0.3023 |
| 20_newsgroups | 0.5163 | 0.3668 | 0.4608 | 0.4161 | 0.2080 |
| spam | 0.3558 | 0.5986 | 0.3843 | 0.4410 | 0.4980 |
| financial_phrasebank | 0.8330 | 0.7372 | 0.7225 | 0.5040 | 0.4444 |
| imdb | 0.9170 | 0.8934 | 0.8982 | 0.8730 | 0.8264 |
| ag_news | 0.7029 | 0.7403 | 0.7193 | 0.6870 | 0.6547 |
| emotion | 0.5233 | 0.4666 | 0.4577 | 0.4530 | 0.4055 |
| cap_sotu | 0.4387 | 0.3972 | 0.3831 | 0.4720 | 0.3390 |
| rotten_tomatoes | 0.7909 | 0.7210 | 0.6979 | 0.8130 | 0.6931 |
| massive | 0.5897 | 0.4721 | 0.5403 | 0.4140 | 0.2527 |
| banking | 0.6885 | 0.6390 | 0.6709 | 0.3870 | 0.3796 |
| snips | 0.8788 | 0.7954 | 0.7731 | 0.7149 | 0.7245 |
| **AVERAGE** | **0.6774** | **0.6387** | **0.6336** | **0.5927** | **0.5340** |

**Table C: GLiClass-V1 Multitask (macro F1)**

| Dataset | [instruct‑large‑v1.0](https://huggingface.co/knowledgator/gliclass-instruct-large-v1.0) | [instruct‑base‑v1.0](https://huggingface.co/knowledgator/gliclass-instruct-base-v1.0) | [edge‑v1.0](https://huggingface.co/knowledgator/gliclass-instruct-edge-v1.0) |
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

### Multilingual Benchmarks

Macro F1 averaged per dataset across all evaluated languages:

| Dataset | [multilang‑ultra](https://huggingface.co/knowledgator/gliclass-multilang-ultra) | [multilang‑mini](https://huggingface.co/knowledgator/gliclass-multilang-mini) | [multilang‑edge](https://huggingface.co/knowledgator/gliclass-multilang-edge) | [gliner2‑multi‑v1](https://huggingface.co/fastino/gliner2-multi-v1) | [bge‑m3‑zeroshot‑v2.0](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0) | [mDeBERTa‑mnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) |
|---|---|---|---|---|---|---|
| germeval2017 | 0.4647 | 0.4826 | 0.4094 | 0.4223 | 0.4503 | 0.2849 |
| massive | 0.5635 | 0.4925 | 0.2853 | 0.3625 | 0.4646 | 0.2427 |
| polyglot_toxicity | 0.7367 | 0.7110 | 0.4474 | 0.6630 | 0.6809 | 0.5698 |
| sib200 | 0.1935 | 0.1921 | 0.1492 | 0.1750 | 0.1891 | 0.1476 |
| textdetox | 0.7428 | 0.7313 | 0.5811 | 0.5912 | 0.7510 | 0.6490 |
| tweet_sentiment | 0.6579 | 0.6171 | 0.5030 | 0.5814 | 0.5991 | 0.4615 |
| **AVERAGE** | **0.5599** | **0.5378** | **0.3959** | **0.4659** | **0.5225** | **0.3926** |

Per-language macro F1 (16-language fair comparison on massive + sib200):

| Language | [multilang‑ultra](https://huggingface.co/knowledgator/gliclass-multilang-ultra) | [multilang‑mini](https://huggingface.co/knowledgator/gliclass-multilang-mini) | [multilang‑edge](https://huggingface.co/knowledgator/gliclass-multilang-edge) | [gliner2‑multi‑v1](https://huggingface.co/fastino/gliner2-multi-v1) | [bge‑m3‑zeroshot‑v2.0](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0) | [mDeBERTa‑mnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) |
|---|---|---|---|---|---|---|
| arabic | 0.3210 | 0.3043 | 0.1843 | 0.2394 | 0.2862 | 0.1567 |
| chinese | 0.3888 | 0.3636 | 0.2724 | 0.2947 | 0.3459 | 0.2356 |
| dutch | 0.3949 | 0.3587 | 0.2660 | 0.2828 | 0.3284 | 0.2146 |
| finnish | 0.3632 | 0.3174 | 0.1172 | 0.2704 | 0.3357 | 0.1884 |
| french | 0.3965 | 0.3679 | 0.2963 | 0.2946 | 0.3396 | 0.1978 |
| german | 0.3654 | 0.3457 | 0.2532 | 0.2767 | 0.3164 | 0.1966 |
| hebrew | 0.3521 | 0.3206 | 0.1271 | 0.2641 | 0.3287 | 0.1796 |
| hindi | 0.3934 | 0.3529 | 0.1877 | 0.0817 | 0.3240 | 0.1986 |
| italian | 0.3919 | 0.3474 | 0.2604 | 0.2891 | 0.3146 | 0.1976 |
| latvian | 0.3643 | 0.3165 | 0.1205 | 0.2741 | 0.3163 | 0.1774 |
| norwegian | 0.3770 | 0.3489 | 0.2043 | 0.2803 | 0.3382 | 0.1965 |
| polish | 0.3961 | 0.3577 | 0.2112 | 0.2814 | 0.3225 | 0.1981 |
| portuguese | 0.4008 | 0.3482 | 0.2798 | 0.3057 | 0.3346 | 0.1936 |
| romanian | 0.3740 | 0.3204 | 0.2210 | 0.2831 | 0.3291 | 0.1944 |
| spanish | 0.3921 | 0.3535 | 0.2905 | 0.2924 | 0.3371 | 0.1918 |
| swedish | 0.3863 | 0.3547 | 0.2121 | 0.2799 | 0.3317 | 0.2019 |
| **AVERAGE** | **0.3786** | **0.3424** | **0.2190** | **0.2681** | **0.3268** | **0.1950** |

## Throughput

![English Quality vs Throughput](model_comparison_en.png)

Throughput (samples/sec), batch_size=8, GPU: NVIDIA RTX PRO 6000 Blackwell. Averaged over text lengths (64 / 256 / 512 tokens).

| Model | 1 label | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | **avg** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [multilang‑ultra](https://huggingface.co/knowledgator/gliclass-multilang-ultra) | 308.2 | 302.5 | 281.8 | 266.3 | 235.9 | 190.5 | 125.2 | 64.7 | 31.5 | **200.7** |
| [multilang‑mini](https://huggingface.co/knowledgator/gliclass-multilang-mini) | 708.4 | 703.9 | 692.5 | 664.2 | 618.1 | 518.1 | 396.1 | 221.2 | 98.2 | **513.4** |
| [multilang‑edge](https://huggingface.co/knowledgator/gliclass-multilang-edge) | 697.0 | 699.7 | 689.5 | 671.0 | 637.7 | 553.3 | 469.8 | 345.2 | 219.2 | **553.6** |
| [instruct‑large](https://huggingface.co/knowledgator/gliclass-instruct-large-v1.0) | 397.2 | 393.1 | 386.6 | 374.2 | 351.1 | 313.3 | 223.8 | 142.2 | 63.2 | **293.9** |
| [instruct‑base](https://huggingface.co/knowledgator/gliclass-instruct-base-v1.0) | 708.0 | 707.5 | 693.5 | 666.4 | 616.7 | 526.5 | 405.5 | 248.1 | 124.9 | **521.9** |
| [gliner2‑large‑v1](https://huggingface.co/fastino/gliner2-large-v1) | 165.6 | 165.2 | 157.1 | 155.6 | 142.1 | 122.1 | 98.6 | 65.6 | 31.0 | **122.5** |
| [gliner2‑multi‑v1](https://huggingface.co/fastino/gliner2-multi-v1) | 270.4 | 267.9 | 264.6 | 257.3 | 237.2 | 200.0 | 159.2 | 96.8 | 48.4 | **200.2** |
| [gliner2‑base‑v1](https://huggingface.co/fastino/gliner2-base-v1) | 296.8 | 293.2 | 287.8 | 278.9 | 262.0 | 229.4 | 180.1 | 121.3 | 66.2 | **224.0** |
| [bge‑m3‑zeroshot‑v2.0](https://huggingface.co/MoritzLaurer/bge-m3-zeroshot-v2.0) | 940.0 | 474.7 | 238.4 | 112.9 | 58.3 | 28.9 | 14.4 | 7.2 | 3.7 | **208.7** |
| [mDeBERTa‑mnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 717.5 | 364.5 | 183.1 | 91.8 | 45.7 | 22.8 | 11.4 | 5.7 | 3.0 | **160.6** |

> NLI models (bge-m3, mDeBERTa) run one forward pass per label — throughput drops linearly with label count. GLiClass and GLiNER2 encode all labels in a single pass, so throughput stays nearly flat.

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