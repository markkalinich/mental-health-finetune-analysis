---
library_name: transformers
tags:
- text-classification
- sentiment-analysis
- depression
- BERT
- mental-health
model-index:
- name: Sentiment Classifier for Depression
  results:
  - task:
      type: text-classification
    dataset:
      name: Custom Depression Tweets Dataset
      type: custom
    metrics:
    - name: Accuracy
      type: accuracy
      value: 99.87
    - name: Precision
      type: precision
      value: 99.91
    - name: Recall
      type: recall
      value: 99.81
    - name: F1 Score
      type: f1
      value: 99.86
license: apache-2.0
language:
- en
base_model: google-bert/bert-base-uncased
metrics:
- Accuracy
- Recall
- Percision
- F1 Score

widget:
  - text: "RT EichinChangLim In Talking About Adolescence Book you'll discover key strategies to tackle self-harm panic attacks bullies child"
    example_title: "Depression"
  - text: "SharronS Hello there Thanks for reaching out I can understand your frustration I would feel the same Id be happy to take a closer look Please feel free to send me a DM with your full name phone number and email address Lena"
    example_title: "Non-depression"

---

# Model Card for Sentiment Classifier for Depression

This model is a fine-tuned version of BERT (`bert-base-uncased`) for classifying text as either **Depression** or **Non-depression**. The model was trained on a custom dataset of mental health-related social media posts and has shown high accuracy in sentiment classification.

## Training Data
The model was trained on a custom dataset of tweets labeled as either depression-related or not. Data pre-processing included tokenization and removal of special characters.

## Training Procedure
The model was trained using Hugging Face's `transformers` library. The training was conducted on a T4 GPU over 3 epochs, with a batch size of 16 and a learning rate of 5e-5.

## Evaluation and Testing Data
The model was evaluated on a 20% holdout set from the custom dataset.

## Results

- **Accuracy:** 99.87%
- **Precision:** 99.91%
- **Recall:** 99.81%
- **F1 Score:** 99.86%

## Environmental Impact
The carbon emissions from training this model can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** T4 GPU
- **Hours used:** 1 hour
- **Cloud Provider:** Google Cloud (Colab)
- **Carbon Emitted:** Estimated at 0.45 kg CO2eq

## Technical Specifications

- **Architecture**: BERT (`bert-base-uncased`)
- **Training Hardware**: T4 GPU in Colab
- **Training Library**: Hugging Face `transformers`

## Citation

**BibTeX:**
```bibtex
@misc{poudel2024sentimentclassifier,
  author = {Poudel, Ashish},
  title = {Sentiment Classifier for Depression},
  year = {2024},
  url = {https://huggingface.co/poudel/sentiment-classifier},
}