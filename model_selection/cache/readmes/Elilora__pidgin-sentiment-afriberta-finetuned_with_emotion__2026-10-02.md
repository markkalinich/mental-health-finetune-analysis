---
library_name: transformers
language:
- en
base_model:
- Davlan/naija-twitter-sentiment-afriberta-large
datasets:
- WAZOBIALABS/nigerian-pidgin-voice-text
license: mit
tags:
- sentiment-analysis
- nigerian-pidgin
- text-classification
- low-resource-nlp
- african-languages
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

A fine-tuned sentiment classifier for Nigerian Pidgin (Naija) text that uses emotional register as an additional input signal alongside the surface text. 
Achieves 96.4% accuracy on a held-out evaluation set, compared to ~51% for text-only classification.
## Model Details

### Model Description
<!-- Provide a longer summary of what this model is. -->

Nigerian Pidgin is a high-context language where the same surface text can carry opposite sentiment depending on tone, emotional register, and sarcasm. The sentence "You do well" is positive when sincere and negative when sarcastic — and a text-only model cannot distinguish between them.

This model addresses that by taking **both** the pidgin text and its emotion category as input, concatenated as a structured prefix:

```
[EMOTION: sarcasm] You do well       → negative
[EMOTION: celebration] You do well   → positive
```

The emotion category is one of 16 labels from the WAZOBIALABS taxonomy, grounded in how Nigerians actually speak: `hustle_fatigue`, `forming`, `market_energy`, `prayer_gratitude`, `sarcasm`, `joy`, `pride`, `contempt`, and more.


- **Model type:** Text classification (sentiment analysis)
- **Language:** Nigerian Pidgin (pcm)
- **License:** MIT
- **Fine-tuned from:** [`Davlan/naija-twitter-sentiment-afriberta-large`](https://huggingface.co/Davlan/naija-twitter-sentiment-afriberta-large)
- **Dataset:** [`WAZOBIALABS/nigerian-pidgin-voice-text`](https://huggingface.co/datasets/WAZOBIALABS/nigerian-pidgin-voice-text) by Stephanie Nkemjika Okoye / Wazobia Labs (CC-BY-4.0)

### Model Sources

- **Repository:** [GitHub — PidginNuance](https://github.com/Elilora/PidginNuance)
- **Demo:** [Live Dashboard](https://pidginnuance.com)
- **Blog post:** [Medium — When the Words Aren't Enough](https://medium.com/@neratdazam2/when-the-words-arent-enough-llms-sentiment-sarcasm-and-emotion-474b6b64de64)

---

## Uses

### Direct Use
<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->



Sentiment classification of Nigerian Pidgin text **where the emotion category is already known** (e.g. from human annotation or a separate prediction step). Input must follow the format:

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="copy model's name")
result = pipe("[EMOTION: sarcasm] You do well")
# → {'label': 'negative', 'score': 0.97}
```




### Downstream Use 

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
Can be integrated into:

1. Annotation tools where a human provides emotion context before sentiment is predicted
2. Two-stage pipelines where an LLM or classifier first predicts emotion, then this model predicts sentiment
3. Research on low-resource African language NLP and context-dependent sentiment analysis



### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
1. Raw text without emotion prefix — the model was not trained on bare pidgin text. Passing text without the [EMOTION: x] prefix will produce unreliable results (~50% accuracy, equivalent to the text-only baseline)
2. Languages other than Nigerian Pidgin — the model was fine-tuned specifically on Pidgin data
3. High-throughput production inference — the emotion guessing step (required for unannotated text) uses an LLM API call per request, which adds latency and cost



## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

1. Small training set: fine-tuned on 500 rows. The model may not generalise well to Pidgin text from domains, regions, or registers not represented in the training data.
2. Emotion dependency: the model requires emotion_category at inference time. For unannotated text, a separate emotion prediction step is needed — and the fine-tuned 16-class emotion classifier achieves only ~33% accuracy due to data sparsity. LLM-based emotion guessing (used in this project's agent) is more reliable but adds API cost.
3. Neutral class underperformance: the neutral sentiment class is underrepresented in the training data (77 of 500 rows), leading to lower recall on neutral examples relative to positive and negative.
4. Annotation subjectivity: sentiment in sarcastic or tonal text is inherently subjective. The 28 context-variant pairs in the dataset (same text, different labels) reflect genuine ambiguity that any model will struggle to resolve without additional context.


### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users should provide accurate emotion category labels for best performance. When using LLM-based emotion guessing, always allow human confirmation of the guessed emotion before trusting the sentiment prediction for high-stakes decisions.


## How to Get Started with the Model

```python
from transformers import pipeline

# Load the model
pipe = pipeline("text-classification",
                model="copy model's name",
                tokenizer="same here for tokenizer",)

# Predict sentiment given known emotion context
def predict_sentiment(text, emotion_category):
    model_input = f"[EMOTION: {emotion_category}] {text}"
    result = pipe(model_input, truncation=True, max_length=128)[0]
    return {"sentiment": result["label"],"confidence": round(result["score"], 4),}

# Examples
print(predict_sentiment("You do well", "sarcasm"))
# → {'sentiment': 'negative', 'confidence': 0.97}

print(predict_sentiment("You do well", "celebration"))
# → {'sentiment': 'positive', 'confidence': 0.95}

print(predict_sentiment("I no fit shout", "hustle_fatigue"))
# → {'sentiment': 'negative', 'confidence': 0.93}
```

**Valid emotion categories:**
`anger`, `betrayal`, `celebration`, `contempt`, `craving`, `forming`, `hustle_energy`, `hustle_fatigue`, `joy`, `market_energy`, `neutral`, `prayer_gratitude`, `pride`, `sarcasm`, `shock`, `suspicion`

---

## Training Details

### Training Data

- **Dataset**: [WAZOBIALABS/nigerian-pidgin-voice-text](https://huggingface.co/datasets/WAZOBIALABS/nigerian-pidgin-voice-text)
- **Training rows**: 500 (after true-duplicate deduplication)
- **Evaluation rows**: 253 (held-out, from WAZOBIALABS/nigerian-pidgin-eval)
- **Label distribution**: negative (52.6%), positive (32.0%), neutral (15.4%)

**Preprocessing**: emotion category concatenated as a structured text prefix before tokenization:
```
[EMOTION: {emotion_category}] {pidgin_text}
```

True duplicates (same text AND same labels across all annotation columns) were removed before training. Context-variant pairs (same text, different labels due to sarcasm/tone differences) were preserved as legitimate distinct examples.

### Training Procedure

#### Training Hyperparameters

- **Base model**: `Davlan/naija-twitter-sentiment-afriberta-large` (continued fine-tuning)
- **Learning rate**: 2e-5
- **Warmup ratio**: 0.1
- **Batch size**: 8 (train and eval)
- **Epochs**: 10
- **Weight decay**: 0.01
- **Best model selection**: macro F1 on validation set
- **Training regime**: fp32 (full fine-tuning, no LoRA/PEFT)
- **Hardware**: Apple M-series CPU (Mac local training)
- **Training time**: ~15 minutes

---

## Evaluation

### Testing Data

Held-out evaluation set: `WAZOBIALABS/nigerian-pidgin-eval` (253 rows, genuinely separate from training data after overlap investigation and true-duplicate removal).

### Metrics

Accuracy and macro F1 on three-class sentiment (positive, negative, neutral).

### Results

| Condition | Input | Accuracy |
|---|---|---|
| Pre-trained baseline (no fine-tuning) | `pidgin_text` only | ~51% |
| Fine-tuned, text only | `pidgin_text` only | ~53% |
| **This model** (fine-tuned, emotion context) | `[EMOTION: x] pidgin_text` | **96.4%** |

Per-class performance (this model):

| Class | Precision | Recall | F1 |
|---|---|---|---|
| negative | 0.97 | 0.98 | 0.97 |
| neutral | 0.83 | 0.62 | 0.71 |
| positive | 0.98 | 1.00 | 0.99 |
| **accuracy** | | | **0.964** |


#### Summary

Text-only sentiment classification caps at ~51% on this dataset because Nigerian Pidgin sentiment is fundamentally context-dependent — the same surface text carries opposite sentiment depending on emotional register and sarcasm. Providing the emotion category as input resolves this ambiguity, lifting accuracy to 96.4%. The gap directly quantifies how much sentiment signal in Nigerian Pidgin lives outside the words themselves.

---

## Environmental Impact

- **Hardware**: Apple M-series CPU (no GPU used)
- **Training time**: ~15 minutes
- **Cloud provider**: None (trained locally)
- **Carbon emitted**: negligible (CPU training, short duration)

---

## Citation

If you use this model, please also cite the dataset and base model:

**Dataset:**
```bibtex
@dataset{wazobia_labs_pidgin_2026,
  author    = {Okoye, Stephanie Nkemjika},
  title     = {Wazobia Labs Nigerian Pidgin Emotion and Sentiment Dataset},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/WAZOBIALABS/nigerian-pidgin-voice-text},
  license   = {CC-BY-4.0},
}
```

**Base model:**
```bibtex
@inproceedings{Muhammad2022NaijaSentiAN,
  title={NaijaSenti: A Nigerian Twitter Sentiment Corpus for Multilingual Sentiment Analysis},
  author={Shamsuddeen Hassan Muhammad and David Ifeoluwa Adelani and Sebastian Ruder and Ibrahim Said Ahmad and Idris Abdulmumin and Bello Shehu Bello and Monojit Choudhury and Chris C. Emezue and Saheed Salahudeen Abdullahi and Anuoluwapo Aremu and Alipio Jeorge and Pavel B. Brazdil},
  year={2022}
}
```
## License

**Code**: MIT License 

**Dataset**: CC-BY-4.0 — [WAZOBIALABS/nigerian-pidgin-voice-text](https://huggingface.co/datasets/WAZOBIALABS/nigerian-pidgin-voice-text) by Stephanie Nkemjika Okoye / Wazobia Labs. Attribution required.

**Base model**: subject to license on Hugging Face Hub.


