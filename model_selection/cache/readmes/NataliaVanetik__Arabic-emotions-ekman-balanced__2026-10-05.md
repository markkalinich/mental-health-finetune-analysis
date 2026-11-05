---
language:
- ar
license: mit
pipeline_tag: text-classification
tags:
- arabic
- emotion-classification
- text-classification
- sentiment-analysis
- ar-ekman
- fine-tuned
base_model: kiroloskhela/Sentiment-Bert
---

# Fine-tuned AM5 Arabic Emotion Classification Model

This model is a fine-tuned version of **A5 (`AnasAlokla/multilingual_go_emotions`)**
for Arabic emotion classification. The model was fine-tuned on the **80%
training split of the ArEkmanPlus-balanced dataset**, a unified Arabic emotion dataset
constructed from multiple existing Arabic emotion resources.

## Base Model

- **Base model:** `kiroloskhela/Sentiment-Bert`
- **Model identifier in the paper:** A5
- **Task:** Arabic text emotion classification
- **Training framework:** Hugging Face Transformers

## Dataset: ArEkmanPlus-balanced

ArEkmanPlus-balanced contains **19,009 Arabic texts** collected by unifying several
existing Arabic emotion datasets. The dataset focuses on the six basic
emotions proposed by Ekman, extended with a `None` category:

- Anger
- Fear
- Joy/Happiness
- Sadness
- Surprise
- Disgust
- None

The unified dataset was constructed by filtering multi-label instances,
unifying equivalent emotion labels, removing duplicate texts and conflicting
annotations, and retaining the six Ekman emotions plus the `None` category.

For this model, **80% of the dataset was used for fine-tuning and 20% was
held out for evaluation**.

## Model Training

The model was fine-tuned as a multi-class sequence classification model.
Texts were tokenized using the tokenizer associated with the base model, and
the model was trained using the Hugging Face `Trainer` framework.

The model was evaluated using accuracy and macro F1.

## Results

On the held-out test portion of ArEkmanPlus-balanced, the fine-tuned AM5 model achieved:

| Metric | Score |
|---|---:|
| Accuracy | 0.8844 |
| Macro F1 | 0.8844 |

The model achieved strong performance across the supported emotion
categories, with particularly high accuracy for Anger and Fear.

## Important: Supported Labels

The original model supports five of the
seven ArEkmanPlus labels:

- Anger
- Fear
- Joy/Happiness
- Sadness
- Surprise


The `Disgust` and `None` categories are not supported by the original AM5
classification setup used in the experiments.

Therefore, this model should be used only for the five supported emotion
categories.

## Intended Use

This model is intended primarily for research and experimentation involving
emotion classification in Arabic text. It may be useful for computational
linguistics, Arabic NLP, emotion analysis, and related research applications.

## Limitations

Performance may vary across domains, genres, dialects, and sources of Arabic
text. ArEkmanPlus-balanced combines several heterogeneous Arabic emotion datasets, and
the original datasets differ in their linguistic characteristics and
annotation schemes. The balanced dataset is a sample of the unified dataset with the same number of texts per each emotion class.

The reported performance is based on a single 80/20 train-test split and
should not be interpreted as a universal estimate of performance on unseen
Arabic text.

## Citation

If you use this model or the ArEkmanPlus-balanced dataset in your research, please
cite the corresponding paper: TBD
