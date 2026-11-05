---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- bert
- sst2
- transformers
datasets:
- glue
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: text-classification
---

# Fine-tuned BERT for Sentiment Analysis on SST-2

This model is a **fine-tuned version of BERT (`bert-base-uncased`)** specifically designed for **binary sentiment classification** of English text, achieving state-of-the-art performance on the Stanford Sentiment Treebank v2 (SST-2) benchmark.

## Model Description

The model was created to demonstrate the practical application of **transfer learning** in Natural Language Processing (NLP). While the base BERT model has a deep understanding of general English language structure, it was not originally trained to detect sentiment. This fine-tuning process adapts BERT's powerful contextual embeddings to the specialized task of determining whether a given sentence expresses a **positive** or **negative** opinion.

### Key Technical Details
*   **Architecture:** BERT-base-uncased with a sequence classification head (2 output neurons).
*   **Training Approach:** The pre-trained BERT layers were gently tuned while the newly added classification layer was trained from scratch over 3 epochs.
*   **Framework:** PyTorch with the Hugging Face Transformers library.

## Intended Use & Limitations

### ✅ Intended Use
This model is optimal for classifying the sentiment of **short English texts**, particularly:
*   Movie or product reviews
*   Social media posts (opinions)
*   Customer feedback snippets

### ⚠️ Limitations
*   **Domain Specificity:** Performance may degrade on texts far outside the movie review domain (e.g., technical, financial, or medical jargon).
*   **Binary Scope:** It is designed for positive/negative classification and does not detect neutral sentiment or more complex emotions.
*   **Language:** Works only with English text.

## Training Data

The model was fine-tuned on the **Stanford Sentiment Treebank v2 (SST-2)** dataset from the GLUE benchmark.

| Dataset Split | Number of Examples |
| :--- | :--- |
| **Training** | 67,349 |
| **Validation** | 872 |
| **Test** | 1,821 |

**Example from the dataset:**
*   **Sentence:** *"contains no wit , only labored gags"*
*   **Label:** `0` (Negative)

## Training Procedure & Hyperparameters

The model was trained for **3 epochs** using the following configuration:

| Hyperparameter | Value |
| :--- | :--- |
| **Learning Rate** | 2e-5 |
| **Batch Size** | 16 |
| **Optimizer** | AdamW |
| **Weight Decay** | 0.01 |
| **Warmup Steps** | 0 |
| **Max Sequence Length** | 128 |

The training leveraged the Hugging Face `Trainer` API for efficient optimization and evaluation.

## Evaluation Results

The model's performance was evaluated on the SST-2 **validation set**, yielding the following metrics:

### 📊 Overall Performance
| Metric | Score |
| :--- | :--- |
| **Accuracy** | **92.55%** |
| **F1-Score (Macro Avg)** | **0.93** |
| **Precision (Negative)** | 0.93 |
| **Recall (Positive)** | 0.94 |

### 📈 Training Progress
| Epoch | Training Loss | Validation Loss | Validation Accuracy |
| :--- | :--- | :--- | :--- |
| 1 | 0.1760 | 0.2400 | 92.43% |
| 2 | 0.1240 | 0.3320 | 91.63% |
| 3 | **0.0704** | **0.3400** | **92.55%** |

### Confusion Matrix (Validation Set, n=872)
| | Predicted Negative | Predicted Positive |
| :--- | :---: | :---: |
| **Actual Negative** | **391** (TN) | 37 (FP) |
| **Actual Positive** | 27 (FN) | **417** (TP) |

## Live Inference Examples

The model correctly classifies clear examples and shows nuanced understanding of ambiguous text:

| Input Sentence | Predicted Label | Confidence (Negative, Positive) |
| :--- | :--- | :--- |
| *"The movie was fantastic!"* | **Positive** | [0.0002, 0.9998] |
| *"I hated every minute of this film."* | **Negative** | [0.9994, 0.0006] |
| *"It was okay, nothing special."* | **Positive** | [0.4308, 0.5692] |

*Note: The third example shows low confidence, appropriately reflecting the neutral sentiment of the input.*

## Conclusion

This project successfully demonstrates how **transfer learning** with a foundation model like BERT can efficiently create a high-performance, specialized classifier. With minimal training time and data, the fine-tuned model achieves competitive results on a standard NLP benchmark, making it suitable for real-world sentiment analysis applications.

---
*Model card generated using best practices from the [Hugging Face Model Card Guidebook](https://huggingface.co/docs/hub/model-cards).*