---
language: en
tags:
- text-classification
- pytorch
- ModernBERT
- emotions
- multi-class-classification
- multi-label-classification
datasets:
- go_emotions
license: mit
metrics:
- accuracy
- f1
- precision
- recall
- matthews_correlation
base_model:
- answerdotai/ModernBERT-large
widget:
- text: I am thrilled to be a part of this amazing journey!
- text: I feel so disappointed with the results.
- text: This is a neutral statement about cake.
library_name: transformers
---


![banner](https://huggingface.co/cirimus/modernbert-base-go-emotions/resolve/main/banner.jpg)

### Overview

This model was fine-tuned from [ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) on the [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) dataset for multi-label classification. It predicts emotional states in text, with a total of 28 possible labels. Each input text can have one or more associated labels, reflecting the multi-label nature of the task.

Try it out [here](https://huggingface.co/spaces/cirimus/modernbert-go-emotions).

---

### Model Details

- **Base Model**: [ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large)
- **Fine-Tuning Dataset**: [GoEmotions](https://huggingface.co/datasets/go_emotions)
- **Number of Labels**: 28
- **Problem Type**: Multi-label classification
- **Language**: English
- **License**: [MIT](https://opensource.org/licenses/MIT)
- **Fine-Tuning Framework**: Hugging Face Transformers

---

### Example Usage

Here’s how to use the model with Hugging Face Transformers:

```python
from transformers import pipeline
import torch

# Load the model
classifier = pipeline(
    "text-classification", 
    model="cirimus/modernbert-large-go-emotions",
    top_k=5
)

text = "I am so happy and excited about this opportunity!"
predictions = classifier(text)

# Print top 5 detected emotions
sorted_preds = sorted(predictions[0], key=lambda x: x['score'], reverse=True)
top_5 = sorted_preds[:5]

print("\nTop 5 emotions detected:")
for pred in top_5:
    print(f"\t{pred['label']:10s} : {pred['score']:.3f}")

# Example output:
# Top 5 emotions detected:
#        joy        : 0.784
#        excitement : 0.735
#        admiration : 0.013
#        gratitude  : 0.003
#        amusement  : 0.003
```

### How the Model Was Created

The model was fine-tuned for 3 epochs using the following hyperparameters:

- **Learning Rate**: `2e-5`
- **Batch Size**: 16
- **Weight Decay**: `0.01`
- **Optimizer**: AdamW
- **Evaluation Metrics**: Precision, Recall, F1 Score (weighted), Accuracy

---

### Dataset

The [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) dataset is a multi-label emotion classification dataset derived from Reddit comments. It contains 58,000 examples with 28 emotion labels (e.g., admiration, amusement, anger, etc.), and it is annotated for multi-label classification.

---

### Evaluation Results

The model was evaluated on the test split of the GoEmotions dataset, using a threshold of `0.5` for binarizing predictions. The overall metrics were:


**Standard Results**:

Using the default threshold of 0.5.

| Label          | Accuracy | Precision | Recall | F1    | MCC   | Support | Threshold |
|----------------|----------|-----------|--------|-------|-------|---------|-----------|
| **macro avg**  | 0.971    | 0.611     | 0.410  | 0.472 | 0.475 | 5427    | 0.5       |
| admiration     | 0.946    | 0.739     | 0.653  | 0.693 | 0.666 | 504     | 0.5       |
| amusement      | 0.982    | 0.817     | 0.814  | 0.816 | 0.807 | 264     | 0.5       |
| anger          | 0.968    | 0.671     | 0.237  | 0.351 | 0.387 | 198     | 0.5       |
| annoyance      | 0.938    | 0.449     | 0.191  | 0.268 | 0.265 | 320     | 0.5       |
| approval       | 0.940    | 0.564     | 0.302  | 0.393 | 0.384 | 351     | 0.5       |
| caring         | 0.977    | 0.581     | 0.319  | 0.411 | 0.420 | 135     | 0.5       |
| confusion      | 0.973    | 0.553     | 0.307  | 0.395 | 0.400 | 153     | 0.5       |
| curiosity      | 0.952    | 0.551     | 0.454  | 0.498 | 0.476 | 284     | 0.5       |
| desire         | 0.988    | 0.702     | 0.398  | 0.508 | 0.523 | 83      | 0.5       |
| disappointment | 0.972    | 0.500     | 0.152  | 0.234 | 0.265 | 151     | 0.5       |
| disapproval    | 0.951    | 0.503     | 0.315  | 0.387 | 0.374 | 267     | 0.5       |
| disgust        | 0.981    | 0.685     | 0.301  | 0.418 | 0.446 | 123     | 0.5       |
| embarrassment  | 0.995    | 0.800     | 0.324  | 0.462 | 0.507 | 37      | 0.5       |
| excitement     | 0.983    | 0.649     | 0.233  | 0.343 | 0.382 | 103     | 0.5       |
| fear           | 0.991    | 0.738     | 0.577  | 0.647 | 0.648 | 78      | 0.5       |
| gratitude      | 0.990    | 0.955     | 0.895  | 0.924 | 0.919 | 352     | 0.5       |
| grief          | 0.999    | 0.000     | 0.000  | 0.000 | 0.000 | 6       | 0.5       |
| joy            | 0.980    | 0.658     | 0.646  | 0.652 | 0.642 | 161     | 0.5       |
| love           | 0.983    | 0.795     | 0.815  | 0.805 | 0.796 | 238     | 0.5       |
| nervousness    | 0.996    | 0.556     | 0.435  | 0.488 | 0.490 | 23      | 0.5       |
| optimism       | 0.973    | 0.702     | 0.392  | 0.503 | 0.513 | 186     | 0.5       |
| pride          | 0.998    | 0.800     | 0.250  | 0.381 | 0.446 | 16      | 0.5       |
| realization    | 0.972    | 0.405     | 0.117  | 0.182 | 0.207 | 145     | 0.5       |
| relief         | 0.998    | 0.000     | 0.000  | 0.000 | 0.000 | 11      | 0.5       |
| remorse        | 0.992    | 0.566     | 0.839  | 0.676 | 0.686 | 56      | 0.5       |
| sadness        | 0.980    | 0.764     | 0.436  | 0.555 | 0.568 | 156     | 0.5       |
| surprise       | 0.980    | 0.692     | 0.447  | 0.543 | 0.547 | 141     | 0.5       |
| neutral        | 0.796    | 0.716     | 0.628  | 0.669 | 0.525 | 1787    | 0.5       |

**Optimal Results**:

Using the best threshold for each label based on the training set (tuned on F1), tested on the test set:


| Label          | Accuracy | Precision | Recall | F1    | MCC   | Support | Threshold |
|----------------|----------|-----------|--------|-------|-------|---------|-----------|
| **macro avg**  | 0.968    | 0.591     | 0.528  | 0.550 | 0.536 | 5427    | various   |
| admiration     | 0.947    | 0.722     | 0.702  | 0.712 | 0.683 | 504     | 0.40      |
| amusement      | 0.983    | 0.812     | 0.848  | 0.830 | 0.821 | 264     | 0.45      |
| anger          | 0.966    | 0.548     | 0.460  | 0.500 | 0.485 | 198     | 0.25      |
| annoyance      | 0.926    | 0.378     | 0.403  | 0.390 | 0.351 | 320     | 0.30      |
| approval       | 0.928    | 0.445     | 0.470  | 0.457 | 0.419 | 351     | 0.30      |
| caring         | 0.975    | 0.496     | 0.430  | 0.460 | 0.449 | 135     | 0.35      |
| confusion      | 0.966    | 0.417     | 0.510  | 0.459 | 0.444 | 153     | 0.30      |
| curiosity      | 0.950    | 0.522     | 0.588  | 0.553 | 0.528 | 284     | 0.40      |
| desire         | 0.988    | 0.673     | 0.422  | 0.519 | 0.527 | 83      | 0.40      |
| disappointment | 0.964    | 0.338     | 0.305  | 0.321 | 0.303 | 151     | 0.30      |
| disapproval    | 0.948    | 0.468     | 0.416  | 0.440 | 0.414 | 267     | 0.35      |
| disgust        | 0.978    | 0.529     | 0.447  | 0.485 | 0.475 | 123     | 0.25      |
| embarrassment  | 0.994    | 0.650     | 0.351  | 0.456 | 0.475 | 37      | 0.35      |
| excitement     | 0.978    | 0.419     | 0.427  | 0.423 | 0.412 | 103     | 0.25      |
| fear           | 0.990    | 0.662     | 0.628  | 0.645 | 0.640 | 78      | 0.40      |
| gratitude      | 0.990    | 0.955     | 0.895  | 0.924 | 0.919 | 352     | 0.50      |
| grief          | 0.999    | 0.750     | 0.500  | 0.600 | 0.612 | 6       | 0.35      |
| joy            | 0.980    | 0.660     | 0.640  | 0.650 | 0.639 | 161     | 0.50      |
| love           | 0.982    | 0.774     | 0.836  | 0.804 | 0.795 | 238     | 0.45      |
| nervousness    | 0.995    | 0.435     | 0.435  | 0.435 | 0.432 | 23      | 0.45      |
| optimism       | 0.972    | 0.597     | 0.565  | 0.580 | 0.566 | 186     | 0.25      |
| pride          | 0.998    | 0.667     | 0.375  | 0.480 | 0.499 | 16      | 0.15      |
| realization    | 0.962    | 0.273     | 0.248  | 0.260 | 0.241 | 145     | 0.25      |
| relief         | 0.999    | 0.800     | 0.364  | 0.500 | 0.539 | 11      | 0.25      |
| remorse        | 0.993    | 0.641     | 0.732  | 0.683 | 0.681 | 56      | 0.65      |
| sadness        | 0.978    | 0.646     | 0.538  | 0.587 | 0.579 | 156     | 0.30      |
| surprise       | 0.979    | 0.603     | 0.518  | 0.557 | 0.548 | 141     | 0.40      |
| neutral        | 0.791    | 0.669     | 0.722  | 0.695 | 0.537 | 1787    | 0.40      |


---

### Intended Use

The model is designed for emotion classification in English-language text, particularly in domains such as:

- Social media sentiment analysis
- Customer feedback evaluation
- Behavioral or psychological research

---

### Limitations and Biases

- **Data Bias**: The dataset is based on Reddit comments, which may not generalize well to other domains or cultural contexts.
- **Underrepresented Classes**: Certain labels like "grief" and "relief" have very few examples, leading to lower performance for those classes.
- **Ambiguity**: Some training data contain annotation inconsistencies or ambiguities that may impact predictions.

---

---

### Environmental Impact

- **Hardware Used**: NVIDIA RTX4090
- **Training Time**: <1 hour
- **Carbon Emissions**: ~0.06 kg CO2 (calculated via [ML CO2 Impact Calculator](https://mlco2.github.io/impact)).

---

### Citation

If you use this model, please cite it as follows:

```bibtex
@inproceedings{JdFE2025c,
  title = {Emotion Classification with ModernBERT},
  author = {Enric Junqu\'e de Fortuny},
  year = {2025},
  howpublished = {\url{https://huggingface.co/cirimus/modernbert-large-go-emotions}},
}
