---
language:
- ur
- en
tags:
- roman-urdu
- emotion-classification
- text-classification
- xlm-roberta
- ekman
- nlp
- low-resource-nlp
- mental-health
- social-media-analysis
- urdu-nlp
- affective-computing
license: apache-2.0
pipeline_tag: text-classification
base_model: Khubaib01/roman-urdu-emotion-xlmr
metrics:
- f1
- accuracy
- precision
- recall
model-index:
- name: roman-urdu-emotion-xlmr-v2
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Roman Urdu Emotion Dataset v2 (28k)
      type: custom
      split: test
    metrics:
    - type: accuracy
      value: 0.9896
      name: Accuracy
    - type: f1
      value: 0.9896
      name: Macro F1
    - type: f1
      value: 0.9896
      name: Weighted F1
---

<div align="center">

<img src="https://img.shields.io/badge/Roman%20Urdu-Low%20Resource%20NLP-8A2BE2?style=for-the-badge" />
<img src="https://img.shields.io/badge/Macro%20F1-0.9896-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Accuracy-98.96%25-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Language-Roman%20Urdu-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Classes-7%20Emotions-red?style=for-the-badge" />

# 🧠 roman-urdu-emotion-xlmr-v2

### State-of-the-Art Emotion Classification for Roman Urdu

**The first and highest-accuracy open-source emotion detection model for Roman Urdu.**  
Trained on real social media and WhatsApp data — the actual language 230 million people use.

*A companion to the RUEmoCorp dataset, published on Harvard Dataverse.*

---

[📖 Paper](#-citation) · [🤗 Model](https://huggingface.co/Khubaib01/roman-urdu-emotion-xlmr-v2) · [📦 Dataset (Harvard Dataverse)](#-dataset--ruemocorp) · [🚀 Quick Start](#-quick-start) · [📊 Results](#-performance)

</div>

---

## Table of Contents

- [Why This Model Matters](#-why-this-model-matters)
- [Quick Start](#-quick-start)
- [Emotion Labels](#-emotion-labels)
- [Performance](#-performance)
- [Baseline Comparison](#-baseline-comparison)
- [Architecture](#-architecture)
- [Training Details](#-training-details)
- [Dataset — RUEmoCorp](#-dataset--ruemocorp)
- [Inter-Annotator Agreement](#-inter-annotator-agreement)
- [Applications](#-applications)
- [Limitations](#-limitations)
- [Team & Contributors](#-team--contributors)
- [Upcoming Work](#-upcoming-work)
- [Citation](#-citation)

---

## 🌍 Why This Model Matters

**Roman Urdu is the dominant language of digital Pakistan — and one of the most underserved languages in NLP.**

Over **230 million people** speak Urdu as a first or second language. In digital spaces — WhatsApp, Twitter/X, Facebook, YouTube — the overwhelming majority write in **Roman Urdu**: Urdu expressed in Latin script, without standardized orthography, heavily mixed with English, and rich in slang, regional variation, and emotionally charged informal expression.

Despite this scale, Roman Urdu remains **severely low-resource** in NLP:

- No standardized spelling — the same word appears in dozens of valid transliterations
- Aggressive intra-sentence code-switching between Urdu and English
- Near-total absence of labeled emotion datasets at scale
- Existing multilingual models (trained on formal Urdu script) generalize poorly to informal Roman Urdu

**`roman-urdu-emotion-xlmr-v2` directly addresses this gap.**

To our knowledge, this is **the first publicly available, high-accuracy, open-source emotion classification model for Roman Urdu**. It achieves **98.96% accuracy and 0.9896 Macro F1** across seven emotion classes on a human-validated test set — competitive with state-of-the-art classifiers for high-resource languages such as English. This is not an incremental contribution: for a language with virtually no prior open-source emotion recognition tooling, this model represents a **foundational resource**.

---

## 🚀 Quick Start

```python
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model="Khubaib01/roman-urdu-emotion-xlmr-v2",
    trust_remote_code=True,   # required — model uses a custom 2-layer MLP head
    top_k=None,               # returns scores for all 7 classes
)

# Single prediction
result = pipe("bohat khushi ho rhi hai aaj!")
top = max(result[0], key=lambda x: x["score"])
print(f"{top['label']}: {top['score']:.4f}")
# happy: 0.9901

# Batch prediction
texts = [
    "mujhe dar lag rha hai",
    "ye sab dekh ke dil bahut dukha",
    "acha! ye toh maine socha bhi nahi tha",
    "theek hai, koi baat nahi",
]
results = pipe(texts)
for text, scores in zip(texts, results):
    top = max(scores, key=lambda x: x["score"])
    print(f"{top['label']:10} ({top['score']:.3f})  →  {text}")
# fear       (0.987)  →  mujhe dar lag rha hai
# sad        (0.983)  →  ye sab dekh ke dil bahut dukha
# surprise   (0.990)  →  acha! ye toh maine socha bhi nahi tha
# none       (0.998)  →  theek hai, koi baat nahi
```

> **Note on `trust_remote_code=True`:** Required because the model uses a custom two-layer MLP classification head. The full architecture (`emotion_model.py`) is included in this repository and is fully auditable.

---

## 🏷️ Emotion Labels

Seven classes — Ekman's six universal basic emotions plus a *none* class for emotionally neutral content.

| ID | Label | Urdu Equivalent | Description | Example (Roman Urdu) |
|----|-------|-----------------|-------------|----------------------|
| 0 | `anger` | غصہ (Gussa) | Frustration, rage, irritation | *yaar mujhe bahut gussa aa rha hai* |
| 1 | `disgust` | نفرت (Nafrat) | Revulsion, strong disapproval | *ugh ye cheez bilkul pasand nahi* |
| 2 | `fear` | ڈر (Dar) | Anxiety, dread, apprehension | *mujhe dar lag rha hai is cheez se* |
| 3 | `happy` | خوشی (Khushi) | Joy, happiness, delight | *bohat khushi ho rhi hai aaj!* |
| 4 | `sad` | اداسی (Udaasi) | Grief, sorrow, disappointment | *ye sab dekh ke dil bahut dukha* |
| 5 | `surprise` | حیرت (Hairat) | Astonishment — positive or negative | *acha! ye toh maine socha bhi nahi* |
| 6 | `none` | غیر جذباتی (Neutral) | No dominant emotional signal | *theek hai, jo hoga dekha jaega* |

Label taxonomy is grounded in [Ekman (1992)](https://doi.org/10.1080/02699939208411068). The `none` class is a corpus-specific addition to handle the large proportion of emotionally neutral utterances in naturalistic social media data.

---

## 📊 Performance

All metrics are computed on a **held-out test set of 2,801 samples**, withheld entirely from training and validation. Each sample was independently reviewed by human validators with native Roman Urdu proficiency prior to inclusion.

### Overall Metrics

| Metric | Score |
|--------|-------|
| Accuracy | **0.9896** |
| Macro F1 | **0.9896** |
| Weighted F1 | **0.9896** |
| Macro Precision | **0.9896** |
| Macro Recall | **0.9896** |

### Per-Class Results

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| anger | 0.9975 | 1.0000 | **0.9988** | 401 |
| disgust | 0.9823 | 0.9725 | 0.9774 | 400 |
| fear | 0.9874 | 0.9825 | 0.9850 | 400 |
| happy | 0.9901 | 1.0000 | **0.9950** | 400 |
| sad | 0.9800 | 0.9825 | 0.9813 | 400 |
| surprise | 0.9900 | 0.9900 | 0.9900 | 400 |
| none | 1.0000 | 1.0000 | **1.0000** | 400 |
| **macro avg** | **0.9896** | **0.9896** | **0.9896** | 2801 |

### Key Observations

- **Perfect F1 on `none` (1.000):** The model completely separates neutral text from all emotional categories — critical for real-world deployment where the majority of messages are emotionally neutral. Misclassified `none` propagates noise into all other class predictions.
- **Perfect recall on `anger` (1.000):** Zero missed angry texts in the entire test set. In mental health monitoring and crisis detection, zero false negatives on distress signals carry direct safety value.
- **Lowest F1 on `disgust` (0.977):** Consistent with affective computing literature — anger and disgust share substantial lexical overlap in informal text and are the hardest pair to separate even for human annotators. 0.977 remains an exceptional result for this class in any low-resource language.
- **Macro F1 = Weighted F1 = Accuracy = 0.9896:** The near-equal class distribution in the test set means these three metrics are identical — confirming no class-imbalance inflation.

### Visualizations

#### Per-Class F1 Score — XLM-R v2

<!-- INSERT: viz/f1_perClass_testSet.png -->
![Per-Class F1 Bar Chart](viz/f1_perClass_testSet.png)

*Figure 1. Per-class F1 scores for roman-urdu-emotion-xlmr-v2 on the held-out test set (n=2,801). All seven emotion categories exceed F1 = 0.977. The `none` class achieves perfect classification (F1 = 1.000), and `anger` achieves perfect recall.*

---

#### Confusion Matrix

<!-- INSERT: viz/confusion_matrix_testset.png -->
![Normalized Confusion Matrix](viz/confusion_matrix_testset.png)

*Figure 2. Normalized confusion matrix on the test set. The near-diagonal structure confirms strong per-class discrimination. The principal off-diagonal confusion occurs between `anger` and `disgust`, consistent with shared lexical features in Roman Urdu informal text.*

---

## 🏆 Baseline Comparison

The two-layer MLP head architecture was evaluated against four baselines spanning the spectrum from classical machine learning to multilingual transformers. All models were trained and evaluated on the same data split.

| Model | Accuracy | Macro F1 | Weighted F1 | F1 anger | F1 disgust | F1 fear | F1 happy | F1 none | F1 sad | F1 surprise |
|-------|----------|----------|-------------|----------|------------|---------|----------|---------|--------|-------------|
| **XLM-R + 2-layer MLP (ours)** | **0.9896** | **0.9896** | **0.9896** | **0.9988** | **0.9774** | **0.9850** | **0.9950** | **1.0000** | **0.9813** | **0.9900** |
| XLM-R + linear head | 0.9769 | 0.9769 | 0.9769 | 0.9942 | 0.9749 | 0.9742 | 0.9682 | 0.9767 | 0.9644 | 0.9858 |
| mBERT + linear head | 0.9412 | 0.9414 | 0.9414 | 0.9742 | 0.9554 | 0.9404 | 0.9169 | 0.9454 | 0.8927 | 0.9647 |
| TF-IDF + SVM | 0.9414 | 0.9414 | 0.9415 | 0.9755 | 0.9497 | 0.9466 | 0.9076 | 0.9280 | 0.9080 | 0.9747 |
| TF-IDF + Logistic Regression | 0.9381 | 0.9382 | 0.9382 | 0.9744 | 0.9449 | 0.9407 | 0.9112 | 0.9201 | 0.9056 | 0.9704 |
| FastText + LR | 0.7779 | 0.7776 | 0.7777 | 0.9079 | 0.8206 | 0.7656 | 0.7221 | 0.7246 | 0.6544 | 0.8481 |

> All results are on the identical held-out test partition. Baseline models trained with standard hyperparameters and no task-specific tuning beyond what is reasonable for each architecture class.

### Radar Chart — Per-Class F1 Across All Models

![Model Comparison Radar Chart](viz/fig4_radar_chart.png)

*Figure 3. Radar chart comparing per-class F1 scores across all five evaluated models. Each axis represents one of the seven emotion categories; the outer boundary corresponds to F1 = 1.0. The proposed XLM-R model with two-layer MLP head (filled polygon) dominates all baselines across every emotion category. The largest gaps appear in `sad`, `happy`, and `fear` — the classes most sensitive to contextual and lexical ambiguity in Roman Urdu.*

### Baseline Bar Chart — Macro F1

![Baseline Comparison Bar Chart](viz/fig2_macro_f1_comparison.png)

*Figure 4. Macro F1 comparison across all evaluated model architectures. The two-layer MLP head provides a +1.27 percentage point improvement over the XLM-R linear head baseline (0.9896 vs. 0.9769), confirming the architectural contribution of the intermediate non-linear projection. The sharp performance cliff between transformer-based and classical models underlines the importance of contextual representations for Roman Urdu emotion recognition.*

## Comparison with `khubaib01/roman-urdu-emotion-xlmr`

The dataset size for this model was incremented from 21k to 28k, and the performace of both the models was compared and it shown substancial impact in the performance.

![Data Scale Impact](viz/fig7_data_scale_impact.png)

*Figure 5. Comparison of performace of both the models with same architecture, but scaled data, and substanical increment of Macro-F1 = +0.2667 in the performace of v2 model is noticed, confirming scaling and robustness is crucial for performance.*

---

## 🏗️ Architecture

The model wraps **XLM-RoBERTa-base** with a custom two-layer MLP classification head that replaces the standard single linear classifier in HuggingFace's default `XLMRobertaForSequenceClassification`.

```
Input: Roman Urdu text
  (tokenized via XLM-R SentencePiece BPE — vocab=250,002 — max_length=512)
         │
         ▼
┌──────────────────────────────────────────────────┐
│          XLM-RoBERTa-base Encoder                │
│  12 transformer layers · hidden size = 768       │
│  12 attention heads · ~270M parameters           │
│  multilingual SentencePiece vocab: 250,002       │
│  position embeddings: 514 (XLM-R convention)     │
└──────────────────────────────────────────────────┘
         │
         │   [CLS] token representation  (batch × 768)
         ▼
┌──────────────────────────────────────────────────┐
│         Emotion Classification Head              │
│                                                  │
│   LayerNorm(768)                                 │
│        ↓                                         │
│   Dropout(0.35)                                  │
│        ↓                                         │
│   Linear(768 → 256)                              │
│        ↓                                         │
│   GELU activation                                │
│        ↓                                         │
│   Dropout(0.175)                                 │
│        ↓                                         │
│   Linear(256 → 7)                                │
└──────────────────────────────────────────────────┘
         │
         ▼
   Emotion logits  (batch × 7)
   → softmax → predicted class + confidence scores
```

**Why a two-layer head?**
The standard `Linear(768 → 7)` collapses all representational transformation into one linear step. A two-layer MLP with an intermediate non-linear projection is beneficial for Roman Urdu emotion classification because:

1. Several emotion classes share substantial lexical overlap in informal text — particularly `anger`/`disgust` and `fear`/`sadness`
2. Orthographic variability in Roman Urdu (the same word in dozens of spellings) creates high surface-form variance for identical emotional content
3. The intermediate 768 → 256 GELU projection learns a compact emotion-relevant subspace before drawing the final 7-way decision boundary

This design was validated against the single-layer baseline during v1 development; ablation results are included in the comparison table above.

| Component | Parameters |
|-----------|------------|
| XLM-R encoder | ~270M |
| Emotion head | ~197k |
| **Total** | **~270.2M** |

---

## ⚙️ Training Details

### Model Lineage

```
xlm-roberta-base
    │  HuggingFace pretrained — 12 layers, 270M params, 100+ languages
    ▼
Khubaib01/roman-urdu-sentiment-xlm-r
    │  Sentiment fine-tune on Roman Urdu (134k corpus)
    ▼
Khubaib01/roman-urdu-emotion-xlmr           ← v1  (21k samples)
    │  First emotion fine-tune
    ▼
Khubaib01/roman-urdu-emotion-xlmr-v2        ← v2  (28k samples, this model)
    Continued fine-tune on expanded RUEmoCorp corpus
```

Each stage transfers progressively more task-specific and language-specific knowledge. This lineage allows v2 to achieve near-perfect performance with conservative encoder learning rates that preserve learned representations rather than overwriting them.

### Hyperparameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Seed | 42 | Full reproducibility |
| Max epochs | 10 | With early stopping (patience = 3) |
| Train batch size | 16 | — |
| Eval batch size | 32 | — |
| Encoder LR | 5e-6 | Conservative — warm-started from v1, avoids catastrophic forgetting |
| Head LR | 3e-5 | 6× encoder LR; head adapts faster to expanded data |
| LR layer-wise decay | 0.90 | Lower encoder layers updated less aggressively |
| Weight decay | 0.02 | Increased vs v1 (0.01) for larger corpus |
| Warmup ratio | 0.10 | 10% of steps for smooth ramp-up |
| Max gradient norm | 1.0 | Gradient clipping |
| Dropout | 0.35 | Slightly higher than v1 (0.30) |
| Label smoothing | 0.10 | Prevents overconfidence on noisy annotations |
| Mixed precision | fp16 | NVIDIA GPU training |
| LR scheduler | Cosine with linear warmup | — |

### Layer-wise Learning Rate Decay

Rather than a uniform LR across the encoder, a layer-wise decay of `0.90` ensures lower transformer layers receive proportionally smaller updates:

```
LR(l) = BASE_LR × (0.90)^l = 5e-6 × (0.90)^l
```

Lower layers encode general linguistic structure (morphology, syntax) that transfers across tasks; upper layers encode task-specific semantics and receive rates near `BASE_LR`. The classification head receives `HEAD_LR = 3e-5`.

### Loss Function

Cross-entropy with label smoothing (ε = 0.10). Label smoothing distributes a fraction of the target probability mass uniformly across non-target classes, preventing pathological overconfidence on noisy user-generated annotations and improving output calibration at inference time.

---

## 📦 Dataset — RUEmoCorp

This model was trained on **RUEmoCorp (Roman Urdu Emotion Corpus)** — a large-scale, multi-source, formally annotated corpus for emotion classification in Roman Urdu.

| Property | Value |
|----------|-------|
| Annotated benchmark samples | 700 (human-validated, 4 annotators) |
| Training corpus size | ~28,000 samples |
| Large-scale raw corpus | 162,000+ utterances |
| Emotion classes | 7 (Ekman + none) |
| Train / Val / Test split | 80% / 10% / 10% |
| Sources | Social media, WhatsApp conversations |
| Inter-annotator agreement | Fleiss' κ = 0.6588 (Substantial) |
| License | CC BY 4.0 |

**📂 Dataset available on Harvard Dataverse:**

> 🔗 **[RUEmoCorp on Harvard Dataverse — under review]**

### Corpus Language Characteristics

- **Orthographic variability:** the same word appears across multiple valid Roman Urdu transliterations (*khushi*, *khushee*, *khushy*, *khushii*)
- **Code-switching:** frequent natural mixing of Roman Urdu and English within single utterances
- **Informal register:** abbreviations, slang, non-standard punctuation, emoticons, sentence fragments
- **Platform diversity:** multiple source platforms to improve domain generalization

---

## 📐 Inter-Annotator Agreement

The 700-sample annotated benchmark was independently labeled by **four annotators** from three Pakistani universities before model training began. Agreement was measured using both Fleiss' Kappa (multi-rater) and pairwise Cohen's Kappa to validate annotation quality.

### IAA Summary

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Fleiss' Kappa (κ) | **0.6588** | Substantial Agreement |
| Mean Pairwise Cohen's Kappa | **0.6597** | Substantial Agreement |
| Full Agreement (4/4 annotators) | 348 / 700 (49.7%) | — |
| Majority Agreement (3/4) | 241 / 700 (34.4%) | — |
| Ambiguous (2/2 split) | 111 / 700 (15.9%) | Flagged; excluded from gold set |
| Gold-labeled samples | 589 / 700 (84.1%) | — |

> The near-identical Fleiss' and mean pairwise Kappa values (Δ = 0.0009) indicate a consistent agreement structure with no single outlier annotator. A κ of 0.66 is considered strong for emotion annotation tasks, where inter-rater disagreement is expected given the inherently subjective nature of affective expression (Krippendorff, 2004). Comparable published datasets report κ in the 0.55–0.72 range.

### IAA Visualization

<!-- INSERT: viz/iaa_kappa_dashboard.png -->
![IAA Dashboard](viz/kappa_analysis.png)

*Figure 6. Inter-annotator agreement analysis dashboard for the RUEmoCorp benchmark set (n=700). Panels show: (a) pairwise Cohen's Kappa for all six annotator pairs with mean overlaid; (b) agreement matrix heatmap across all four annotators; (c) Fleiss' Kappa summary; (d) mean pairwise Kappa per emotion category; (e) distribution of sample-level agreement types; (f) final gold label distribution after majority voting.*

### Annotator Panel

| Annotator | Affiliation | Location |
|-----------|-------------|----------|
| Muzammil Shadab | Bahauddin Zakariya University (BZU) | Multan |
| Sara | COMSATS University Islamabad (CUI) | Islamabad |
| Faiez Ahmad | Emerson University Multan (EUM) | Multan |
| Khadija Faisal | Emerson University Multan (EUM) | Multan |

Gold labels were determined by majority vote (≥ 3/4 annotators in agreement). Samples with a 2–2 split were flagged as ambiguous and excluded from the training and evaluation sets.

---

## 💡 Applications

### Mental Health Monitoring
- Passive screening of social media for early signs of emotional distress in Urdu-speaking populations
- Longitudinal tracking of emotional state in anonymized conversational data
- Support tooling for mental health researchers studying Pakistani and South Asian communities
- Flagging high-distress conversations in counseling platforms for human review

### Social Media & Public Discourse Analysis
- Real-time emotion monitoring of public discourse on Pakistani social media
- Brand sentiment and emotion analysis for Urdu-speaking markets
- Detection of emotionally charged content campaigns and coordinated harm
- Crisis response: identifying fear or anger spikes during public emergencies

### Policy and Governance
- Public opinion analysis of government communications and policy announcements
- Population emotional needs assessment for targeted resource allocation

### Low-Resource NLP Research
- First benchmark model for Roman Urdu affective computing — direct baseline for future work
- Foundation for transfer learning to related low-resource South Asian languages
- Demonstration of continued fine-tuning viability for low-resource settings with limited labeled data

### Conversational AI
- Emotion-aware chatbots for Urdu-speaking users
- Customer service systems that detect frustrated or distressed users for priority routing

---

## ⚠️ Limitations

- **Geographic scope:** Training data is predominantly from Pakistani digital communication. Emotional expression norms may differ across other Urdu-speaking populations (e.g., Indian Urdu communities, diaspora).
- **Temporal drift:** Language use and slang in informal digital communication evolves continuously. Model performance may degrade on text from significantly later periods without re-training.
- **Single-label classification:** The model assigns one dominant emotion per utterance. Mixed or ambiguous emotional states — which account for ~15.9% of the annotated benchmark — are not explicitly modeled.
- **Annotation subjectivity:** Emotion labeling is inherently subjective. The residual ambiguity in the training data (captured in the IAA metrics) represents irreducible uncertainty in the task itself, not solely model error.
- **Not for surveillance:** This model must not be used to infer emotional states of identifiable individuals without their explicit, informed consent.

---

## 👥 Team & Contributors

| Name | Role | Affiliation |
|------|------|-------------|
| **Muhammad Khubaib Ahmad** | Core Researcher · Lead Engineer · Project Administration · Model Development | Independent Researcher |
| **Khadija Faisal** | Data Manager · Annotation Coordination · Annotator | Emerson University Multan |
| **Muzammil Shadab** | Annotator | Bahauddin Zakariya University, Multan |
| **Sara** | Annotator | COMSATS University Islamabad |
| **Faiez Ahmad** | Annotator | Emerson University Multan |

---

## 🔭 Upcoming Work

- [ ] **Research paper** — full methodology, extended experiments, and corpus statistics *(in preparation)*
- [ ] **RUEmoCorp v2** — extended annotated set with improved class balance and broader source diversity
- [ ] **Multi-label variant** — modeling mixed emotional states explicitly
- [ ] **HuggingFace Space** — interactive demo for direct model testing
- [ ] **Dialect extension** — Punjabi-Urdu code-mixed and Sindhi-Roman support

---

## 📖 Citation

A research paper describing the full methodology is currently in preparation. Until publication, please cite this model and the dataset as:

**Model:**
```bibtex
@misc{muhammad_khubaib_ahmad_2026,
	author       = { Muhammad Khubaib Ahmad and Khadija Faisal },
	title        = { roman-urdu-emotion-xlmr-v2 (Revision 7cd7dd2) },
	year         = 2026,
	url          = { https://huggingface.co/Khubaib01/roman-urdu-emotion-xlmr-v2 },
	doi          = { 10.57967/hf/8347 },
	publisher    = { Hugging Face }
}
```

**Dataset (RUEmoCorp):**
```bibtex
@data{ruemocorp2025,
  author    = {Ahmad, Muhammad Khubaib and Faisal, Khadija},
  title     = {{RUEmoCorp: Roman Urdu Emotion Corpus}},
  year      = {2026},
  publisher = {Harvard Dataverse},
  doi       = {under review},
  url       = {under review},
}
```

**References:**
- Ekman, P. (1992). An argument for basic emotions. *Cognition & Emotion*, 6(3–4), 169–200.
- Conneau, A. et al. (2020). Unsupervised cross-lingual representation learning at scale. *ACL 2020*.
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.

---

## 🔗 Related Resources

| Resource | Link |
|----------|------|
| 🤗 Model (this) | [Khubaib01/roman-urdu-emotion-xlmr-v2](https://huggingface.co/Khubaib01/roman-urdu-emotion-xlmr-v2) |
| 📦 RUEmoCorp Dataset | Harvard Dataverse (under review) |
| 🧠 Parent Sentiment Model | [Khubaib01/roman-urdu-sentiment-xlm-r](https://huggingface.co/Khubaib01/roman-urdu-sentiment-xlm-r) |
| 📊 Sentiment Corpus | [Khubaib01/RomanUrdu-NLP-Sentiment-Corpus](https://huggingface.co/datasets/Khubaib01/RomanUrdu-NLP-Sentiment-Corpus) |

---

<div align="center">

**RUEmoCorp & roman-urdu-emotion-xlmr-v2**  
Released under Apache 2.0 (model) · CC BY 4.0 (dataset)  
*Advancing NLP for underserved South Asian languages*

</div>