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
- answerdotai/ModernBERT-base
widget:
- text: I am thrilled to be a part of this amazing journey!
- text: I feel so disappointed with the results.
- text: This is a neutral statement about cake.
library_name: transformers
---

![banner](https://huggingface.co/cirimus/modernbert-base-go-emotions/resolve/main/banner.jpg)


### Overview

This model was fine-tuned from [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) dataset for multi-label classification. It predicts emotional states in text, with a total of 28 possible labels. Each input text can have one or more associated labels, reflecting the multi-label nature of the task.

Try it out [here](https://huggingface.co/spaces/cirimus/modernbert-go-emotions).

---

### Model Details

- **Base Model**: [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)
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
    model="cirimus/modernbert-base-go-emotions",
    return_all_scores=True
)

text = "I am so happy and excited about this opportunity!"
predictions = classifier(text)

# Print top 5 detected emotions
sorted_preds = sorted(predictions[0], key=lambda x: x['score'], reverse=True)
top_5 = sorted_preds[:5]

print("\nTop 5 emotions detected:")
for pred in top_5:
    print(f"\t{pred['label']:10s} : {pred['score']:.3f}")

## Example output:
# Top 5 emotions detected:
#        excitement : 0.937
#        joy        : 0.915
#        desire     : 0.022
#        love       : 0.020
#        admiration : 0.017
```



### How the Model Was Created

The model was fine-tuned for 3 epochs using the following hyperparameters:

- **Learning Rate**: `2e-5`
- **Batch Size**: 16
- **Weight Decay**: `0.01`
- **Warmup Steps**: 500
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
| **macro avg**  | 0.970    | 0.665     | 0.389  | 0.465 | 0.477 | 5427    | 0.5       |
| admiration     | 0.945    | 0.737     | 0.627  | 0.677 | 0.650 | 504     | 0.5       |
| amusement      | 0.980    | 0.794     | 0.803  | 0.798 | 0.788 | 264     | 0.5       |
| anger          | 0.968    | 0.680     | 0.258  | 0.374 | 0.406 | 198     | 0.5       |
| annoyance      | 0.940    | 0.468     | 0.159  | 0.238 | 0.249 | 320     | 0.5       |
| approval       | 0.942    | 0.614     | 0.276  | 0.381 | 0.387 | 351     | 0.5       |
| caring         | 0.976    | 0.524     | 0.244  | 0.333 | 0.347 | 135     | 0.5       |
| confusion      | 0.975    | 0.625     | 0.294  | 0.400 | 0.418 | 153     | 0.5       |
| curiosity      | 0.951    | 0.538     | 0.423  | 0.473 | 0.452 | 284     | 0.5       |
| desire         | 0.987    | 0.604     | 0.349  | 0.443 | 0.453 | 83      | 0.5       |
| disappointment | 0.974    | 0.656     | 0.139  | 0.230 | 0.294 | 151     | 0.5       |
| disapproval    | 0.950    | 0.494     | 0.292  | 0.367 | 0.356 | 267     | 0.5       |
| disgust        | 0.980    | 0.674     | 0.252  | 0.367 | 0.405 | 123     | 0.5       |
| embarrassment  | 0.995    | 0.857     | 0.324  | 0.471 | 0.526 | 37      | 0.5       |
| excitement     | 0.984    | 0.692     | 0.262  | 0.380 | 0.420 | 103     | 0.5       |
| fear           | 0.992    | 0.796     | 0.551  | 0.652 | 0.659 | 78      | 0.5       |
| gratitude      | 0.990    | 0.957     | 0.892  | 0.924 | 0.919 | 352     | 0.5       |
| grief          | 0.999    | 0.000     | 0.000  | 0.000 | 0.000 | 6       | 0.5       |
| joy            | 0.978    | 0.652     | 0.571  | 0.609 | 0.600 | 161     | 0.5       |
| love           | 0.982    | 0.792     | 0.798  | 0.795 | 0.786 | 238     | 0.5       |
| nervousness    | 0.996    | 0.636     | 0.304  | 0.412 | 0.439 | 23      | 0.5       |
| optimism       | 0.975    | 0.743     | 0.403  | 0.523 | 0.536 | 186     | 0.5       |
| pride          | 0.998    | 0.857     | 0.375  | 0.522 | 0.566 | 16      | 0.5       |
| realization    | 0.973    | 0.514     | 0.124  | 0.200 | 0.244 | 145     | 0.5       |
| relief         | 0.998    | 1.000     | 0.091  | 0.167 | 0.301 | 11      | 0.5       |
| remorse        | 0.992    | 0.594     | 0.732  | 0.656 | 0.656 | 56      | 0.5       |
| sadness        | 0.979    | 0.759     | 0.385  | 0.511 | 0.532 | 156     | 0.5       |
| surprise       | 0.978    | 0.649     | 0.340  | 0.447 | 0.460 | 141     | 0.5       |
| neutral        | 0.794    | 0.715     | 0.623  | 0.666 | 0.520 | 1787    | 0.5       |

**Optimal Results**:

Using the best threshold for each label based on the training set (tuned on F1).

| Label          | Accuracy | Precision | Recall | F1    | MCC   | Support | Threshold |
|----------------|----------|-----------|--------|-------|-------|---------|-----------|
| **macro avg**  | 0.967    | 0.568     | 0.531  | 0.541 | 0.526 | 5427    | various   |
| admiration     | 0.946    | 0.700     | 0.726  | 0.713 | 0.683 | 504     | 0.30      |
| amusement      | 0.981    | 0.782     | 0.856  | 0.817 | 0.808 | 264     | 0.40      |
| anger          | 0.963    | 0.490     | 0.510  | 0.500 | 0.481 | 198     | 0.20      |
| annoyance      | 0.917    | 0.337     | 0.425  | 0.376 | 0.334 | 320     | 0.25      |
| approval       | 0.922    | 0.411     | 0.473  | 0.440 | 0.399 | 351     | 0.25      |
| caring         | 0.971    | 0.424     | 0.415  | 0.419 | 0.405 | 135     | 0.25      |
| confusion      | 0.970    | 0.468     | 0.484  | 0.476 | 0.460 | 153     | 0.30      |
| curiosity      | 0.947    | 0.493     | 0.630  | 0.553 | 0.530 | 284     | 0.35      |
| desire         | 0.988    | 0.708     | 0.410  | 0.519 | 0.533 | 83      | 0.45      |
| disappointment | 0.963    | 0.321     | 0.291  | 0.306 | 0.287 | 151     | 0.25      |
| disapproval    | 0.943    | 0.429     | 0.464  | 0.446 | 0.417 | 267     | 0.30      |
| disgust        | 0.981    | 0.604     | 0.496  | 0.545 | 0.538 | 123     | 0.20      |
| embarrassment  | 0.995    | 0.789     | 0.405  | 0.536 | 0.564 | 37      | 0.30      |
| excitement     | 0.979    | 0.444     | 0.388  | 0.415 | 0.405 | 103     | 0.25      |
| fear           | 0.991    | 0.693     | 0.667  | 0.680 | 0.675 | 78      | 0.30      |
| gratitude      | 0.990    | 0.951     | 0.886  | 0.918 | 0.913 | 352     | 0.50      |
| grief          | 0.999    | 0.500     | 0.500  | 0.500 | 0.499 | 6       | 0.20      |
| joy            | 0.978    | 0.628     | 0.609  | 0.618 | 0.607 | 161     | 0.40      |
| love           | 0.982    | 0.789     | 0.819  | 0.804 | 0.795 | 238     | 0.45      |
| nervousness    | 0.995    | 0.375     | 0.391  | 0.383 | 0.380 | 23      | 0.25      |
| optimism       | 0.970    | 0.558     | 0.597  | 0.577 | 0.561 | 186     | 0.15      |
| pride          | 0.998    | 0.750     | 0.375  | 0.500 | 0.529 | 16      | 0.15      |
| realization    | 0.968    | 0.326     | 0.200  | 0.248 | 0.240 | 145     | 0.25      |
| relief         | 0.998    | 0.429     | 0.273  | 0.333 | 0.341 | 11      | 0.25      |
| remorse        | 0.993    | 0.611     | 0.786  | 0.688 | 0.689 | 56      | 0.55      |
| sadness        | 0.979    | 0.667     | 0.538  | 0.596 | 0.589 | 156     | 0.20      |
| surprise       | 0.978    | 0.585     | 0.511  | 0.545 | 0.535 | 141     | 0.30      |
| neutral        | 0.782    | 0.649     | 0.737  | 0.690 | 0.526 | 1787    | 0.40      |


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
- **Carbon Emissions**: ~0.04 kg CO2 (calculated via [ML CO2 Impact Calculator](https://mlco2.github.io/impact)).

---

### Citation

If you use this model, please cite it as follows:

```bibtex
@inproceedings{JdFE2025b,
  title = {Emotion Detection with ModernBERT},
  author = {Enric Junqu\'e de Fortuny},
  year = {2025},
  howpublished = {\url{https://huggingface.co/cirimus/modernbert-base-go-emotions}},
}