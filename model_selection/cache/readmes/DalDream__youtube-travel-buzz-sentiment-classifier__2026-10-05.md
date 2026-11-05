---
license: mit
language:
- ko
metrics:
- accuracy
- f1
base_model:
- monologg/koelectra-base-discriminator
pipeline_tag: text-classification
library_name: transformers
tags:
- korean
- youtube
- sentiment-analysis
- travel
- social-media-analysis
- llm-generated-data
- nlp
- travel-sentiment
---
# youtube-travel-buzz-sentiment-classifier

## 🔹 Model Name

**youtube-travel-buzz-sentiment-classifier**

---

## 🔹 Model Description

> A Korean multi-class sentiment classifier that decomposes travel-related YouTube comments into positive, neutral, and negative signals for travel demand analysis.
> 

---

## 🔹 Model Summary

This model performs **three-class sentiment classification** on Korean YouTube comments that have already been identified as travel-related.

Sentiment labels:

- `0`: Negative
- `1`: Neutral
- `2`: Positive

Unlike conventional sentiment models, this classifier explicitly preserves **neutral sentiment**, which primarily captures information-seeking and intent-driven comments.

This design enables downstream analysis linking online discourse patterns to real-world travel demand signals.

The model is trained on LLM-generated synthetic comments designed to mimic the linguistic characteristics of real YouTube travel discussions.

---

## 🔹 Intended Use

### Primary Use Case

- Decomposing travel-related YouTube buzz into structured sentiment signals
- Supporting:
    - Exploratory demand analysis
    - Early-stage travel interest detection
    - Trend-level behavioral research

### Out-of-Scope Use

- Emotion detection beyond sentiment polarity
- Individual-level behavior prediction
- Standalone decision-making systems

---

## 🔹 Training Data

- **Type**: Synthetic Korean YouTube travel comments generated using multiple LLMs
- **Labels**:
    - `0`: Negative
    - `1`: Neutral
    - `2`: Positive
- **Key Characteristics**:
    - Informal language, slang, typos, emojis
    - Mixed sentence length and ambiguity
    - Designed to approximate real-world YouTube comment noise
    - Neutral comments intentionally modeled to represent questions, factual statements, and information-seeking behavior

Downstream analysis revealed that **neutral sentiment** often functions as a proxy for **latent travel intent**, particularly for emerging destinations.

Prompt design details and data generation strategy are documented in the associated GitHub repository.

---

## 🔹 Model Architecture

- Base model: `monologg/koelectra-base-discriminator`
- Task: Multi-class sentiment classification
- Tokenizer: KoELECTRA tokenizer
- Fine-tuning: Hugging Face Trainer API

---

## 🔹 Performance (Indicative)

- Overall Accuracy: ~96%
- Macro F1-score: ~96% (balanced synthetic validation set)

These metrics were obtained on a held-out synthetic validation set and
reflect controlled experimental conditions.

Given the semantic ambiguity of short-form YouTube comments,
the model is intended for **trend-level and aggregate analysis** rather than
individual comment-level judgment.

Performance on real-world YouTube comments may differ due to
distribution shift and unmodeled linguistic nuance.

---

## 🔹 Limitations

- Fine-grained emotional nuance is not modeled
- Synthetic data bias may persist in edge cases
- Not optimized for sarcasm-heavy or long-form comments

- Performance may degrade on real-world comments without additional fine-tuning on authentic data.

---

## 🔹 Ethical Considerations

- No personal data used
- Outputs should be interpreted at **aggregate signal level**, not individual judgment

---

## 🔹 Related Resources

- 📁 Full pipeline code and documentation:
    
    https://github.com/DalDream/youtube-travel-buzz-nlp-pipeline
    
- 🔗 Upstream travel relevance classifier:
    
    https://huggingface.co/DalDream/youtube-travel-buzz-relevance-classifier
    

---

## 🔹 Citation / Attribution

This model was developed as part of a **YouTube Travel Buzz Signal Extraction NLP pipeline**
for research and portfolio demonstration purposes.

### Author / Contributions

- **[DalDream]** – Project lead for model strategy, pipeline design,
model validation, and final documentation.
- **[GY Yu]** – LLM-based synthetic data generation,
dataset construction, model training, and fine-tuning.

> Note: This model is the result of a collaborative team project.
Responsibilities are listed to clarify individual contributions.
>