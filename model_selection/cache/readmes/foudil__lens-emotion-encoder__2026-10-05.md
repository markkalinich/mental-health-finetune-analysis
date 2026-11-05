---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- emotion
- contrastive-learning
- multi-label
pipeline_tag: sentence-similarity
library_name: sentence-transformers
language:
- en
license: apache-2.0
base_model: SamLowe/roberta-base-go_emotions
datasets:
- go_emotions
---

# EmotionEncoder

**EmotionEncoder** is a RoBERTa-base encoder fine-tuned with a multi-label supervised contrastive objective on GoEmotions. It maps English text into a 128-dimensional space where **cosine similarity = emotional similarity**: texts that share emotional content sit close together, texts that don't are pushed apart.

It is not a classifier. There are no output labels, no softmax, no categories to pick from. You get a vector, and that vector's geometry is the model's understanding of emotion.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("foudil/lens-emotion-encoder")

sentences = [
    "I can't believe how proud I am of everything she's achieved.",
    "Watching her succeed fills me with such joy and admiration.",
    "The quarterly report has been filed with the relevant authorities.",
]

embeddings = model.encode(sentences)
similarities = model.similarity(embeddings, embeddings)
# sentences[0] ↔ sentences[1]: high similarity (pride/joy/admiration overlap)
# sentences[0] ↔ sentences[2]: low similarity (emotional vs. neutral)
```

---

## Why this model exists

Existing approaches to emotion in text fall into two camps, and both have a geometric problem.

**Classification models** (e.g. `roberta-base-go_emotions`) are trained with cross-entropy to separate emotion categories. They discriminate well — but cross-entropy optimises decision boundaries, not distances. The resulting embedding space isn't designed to answer "how emotionally similar are these two texts?"

**VAD regression models** map text to valence–arousal–dominance coordinates. They're continuous by construction, but three scalars cannot resolve categorical distinctions that share VAD coordinates. Fear and anger both sit in the high-arousal, negative-valence quadrant; they are not the same emotion, and downstream systems that need to tell them apart will not get that signal from a VAD scalar.

EmotionEncoder is trained with a **multi-label supervised contrastive objective** that directly shapes the embedding geometry: texts that share emotional content are pulled together, texts that don't are pushed apart, and the strength of attraction is proportional to how much emotional overlap they have. The result is a space that is simultaneously discriminative and calibrated — something neither of the above achieves alone.

---

## Model details

| | |
|---|---|
| **Base model** | [`SamLowe/roberta-base-go_emotions`](https://huggingface.co/SamLowe/roberta-base-go_emotions) |
| **Architecture** | RoBERTa-base + masked mean pooling + 2-layer MLP projection head |
| **Output dimension** | 128 |
| **Similarity function** | Cosine similarity |
| **Max sequence length** | 100 tokens |
| **Training data** | [GoEmotions](https://huggingface.co/datasets/go_emotions) (~54k Reddit comments, 28 emotion labels, multi-label) |
| **Training objective** | Multi-label SupCon with any-overlap pair weighting |
| **Language** | English |

The projection head maps the 768-dimensional pooled representation to 128 dimensions via two linear layers (768→512 with ReLU, 512→128), followed by LayerNorm and ℓ₂ normalisation. All embeddings live on the unit hypersphere, so cosine similarity is the natural distance.

---

## Performance

Evaluated on three datasets with varying label schemas against two baselines:
- `all-mpnet-base-v2` — strong general-purpose semantic similarity encoder; well-calibrated, no emotion-specific signal
- `SamLowe/roberta-base-go_emotions` — the backbone before contrastive fine-tuning; strong discriminator, poorly calibrated for graded similarity

### GoEmotions (in-domain, 28 labels)

| Model | Spearman ρ ↑ | ROC-AUC ↑ | Cosine gap ↑ | Brier ↓ | ECE ↓ |
|---|:---:|:---:|:---:|:---:|:---:|
| **EmotionEncoder** | +0.234 | 0.711 | **0.227** | **0.277** | 0.421 |
| all-mpnet-base-v2 | +0.026 | 0.523 | 0.008 | 0.276 | **0.416** |
| roberta-go_emotions | **+0.240** | **0.716** | 0.167 | 0.360 | 0.515 |

### dair-ai/emotion (out-of-domain, 6 labels)

| Model | Spearman ρ ↑ | ROC-AUC ↑ | Cosine gap ↑ | Brier ↓ | ECE ↓ |
|---|:---:|:---:|:---:|:---:|:---:|
| **EmotionEncoder** | **+0.271** | **0.683** | **0.208** | **0.296** | **0.351** |
| all-mpnet-base-v2 | +0.079 | 0.553 | 0.023 | 0.293 | 0.332 |
| roberta-go_emotions | +0.254 | 0.671 | 0.120 | 0.344 | 0.415 |

### tweet_eval/emotion (out-of-domain, 4 labels)

| Model | Spearman ρ ↑ | ROC-AUC ↑ | Cosine gap ↑ | Brier ↓ | ECE ↓ |
|---|:---:|:---:|:---:|:---:|:---:|
| **EmotionEncoder** | **+0.363** | **0.730** | **0.246** | **0.255** | **0.273** |
| all-mpnet-base-v2 | +0.147 | 0.593 | 0.037 | 0.281 | 0.277 |
| roberta-go_emotions | +0.295 | 0.686 | 0.131 | 0.313 | 0.348 |

EmotionEncoder exceeds the backbone on both out-of-domain datasets on every metric — the label schemas there (4–6 labels) are completely different from GoEmotions (28 labels), so this is genuine transfer, not overfitting to the training distribution. On Brier score it matches `all-mpnet-base-v2` in-domain (within 0.001) and beats it on tweet_eval, while reducing the backbone's Brier by 23% on GoEmotions.

### What the OOD transfer does and does not show

The OOD numbers support the claim that the learned geometry captures something more general than the GoEmotions label schema. The dair-ai/emotion (6 labels, Twitter) and tweet_eval/emotion (4 labels, Twitter) schemas were not seen during training, and the encoder's geometry recovers their structure better than either baseline.

They do **not** show that the model has learned a domain-invariant or theory-grounded emotion representation. Both OOD datasets remain English social-media text, sharing register and surface conventions with the GoEmotions training distribution. Performance on emotionally-loaded text in a clinical interview, a legal document, a literary passage, or a non-English-translated source is not established by these probes.

The intended interpretation is conservative: the encoder generalises across emotion label schemas of varying granularity within an English social-media-adjacent register, and should be validated on any domain that departs meaningfully from that.

---

## Usage

### Semantic search over emotional content

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("foudil/lens-emotion-encoder")

corpus = [
    "I'm devastated. Everything we worked for is gone.",
    "She finally got the promotion she deserved — couldn't be happier for her.",
    "The meeting has been rescheduled to Thursday.",
    "There's something deeply unsettling about the way this unfolded.",
    "I feel so grateful for everyone who showed up today.",
]

query = "I'm overwhelmed with gratitude and happiness."

corpus_emb = model.encode(corpus, convert_to_tensor=True)
query_emb = model.encode(query, convert_to_tensor=True)

scores = model.similarity(query_emb, corpus_emb)[0]
for score, sentence in sorted(zip(scores, corpus), reverse=True):
    print(f"{score:.3f}  {sentence}")
```

### Pairwise similarity scoring

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("foudil/lens-emotion-encoder")

pairs = [
    ("I'm furious. This is completely unacceptable.", "She makes me so angry I can't think straight."),
    ("I'm furious. This is completely unacceptable.", "What a wonderful surprise — I'm so touched."),
]

for a, b in pairs:
    ea, eb = model.encode([a, b])
    print(f"{model.similarity(ea, eb).item():.3f}  |  {a[:50]}...")
```

---

## Intended use

- Semantic search and retrieval over emotionally-indexed content
- Emotional similarity scoring between text pairs
- Soft signal for emotion-aware ranking or filtering
- Feature input for downstream models that need a graded emotion representation

## Out-of-scope use

- **Hard emotion classification.** This model produces similarity scores, not category labels. If you need `{"joy": 0.9, "sadness": 0.1}`, use a dedicated classification model.
- **Non-English text.** The model has not been evaluated on other languages.
- **Clinical or diagnostic use.** Emotion similarity scores are not a substitute for clinical emotion assessment.

---

## Limitations

**English Reddit register.** Training data is drawn from Reddit. Register generalisation beyond English social media is not established and should be validated on your domain before deployment.

**GoEmotions label noise.** Inter-annotator agreement varies across emotion categories. Categories with low agreement or few examples yield less reliable geometry.

**Calibration residual.** Boundary ECE on GoEmotions is 0.421 vs. 0.416 for the mpnet calibration reference. Post-hoc temperature or Platt scaling can close this if precise probability estimates matter.

**No valence axis.** The model encodes full emotional profiles, not sentiment polarity. It is not optimised as a sentiment analyser.

---

## Citation

If you use this model, please cite the GoEmotions corpus and the SupCon objective on which it is based:

```bibtex
@inproceedings{demszky-etal-2020-goemotions,
  title     = {{GoEmotions}: A Dataset of Fine-Grained Emotions},
  author    = {Demszky, Dorottya and Movshovitz-Attias, Dana and Ko, Jeongwoo and Cowen, Alan and Nemade, Gaurav and Ravi, Sujith},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year      = {2020},
  publisher = {Association for Computational Linguistics},
  pages     = {4040--4054},
  doi       = {10.18653/v1/2020.acl-main.372},
  url       = {https://aclanthology.org/2020.acl-main.372/}
}

@inproceedings{khosla-etal-2020-supcon,
  title     = {Supervised Contrastive Learning},
  author    = {Khosla, Prannay and Teterwak, Piotr and Wang, Chen and Sarna, Aaron and Tian, Yonglong and Isola, Phillip and Maschinot, Aaron and Liu, Ce and Krishnan, Dilip},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {33},
  year      = {2020},
  pages     = {18661--18673},
  url       = {https://proceedings.neurips.cc/paper/2020/hash/d89a66c7c80a29b1bdbab0f2a1a94af8-Abstract.html}
}
```

---

## Framework versions

- Python 3.9.25 · sentence-transformers 5.1.2 · transformers 4.57.6 · PyTorch 2.8.0