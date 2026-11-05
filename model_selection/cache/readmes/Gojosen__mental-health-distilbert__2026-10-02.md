---
language:
- en
license: mit
tags:
- text-classification
- distilbert
- mental-health
- sentiment-analysis
datasets:
- entenam/reddit-mental-health-dataset
widget:
- text: "I just feel so overwhelmed lately and I don't know what to do."
  example_title: "Anxiety Example"
- text: "I don't see the point in anything anymore. Everything is just so dark."
  example_title: "Depression Example"
---

# Mental Health Text Risk Detector (DistilBERT)

## Model Description
This model is a fine-tuned version of `distilbert-base-uncased` designed to detect signs of mental health risks from text. It classifies text into one of six distinct categories based on emotional markers and indicators of distress. The model was fine-tuned for a project aimed at providing early-risk detection and awareness.

- **Developed by:** Arjun, Athul, Sruthi, Vishnu
- **Model type:** Transformer-based text classification model (DistilBERT)
- **Language(s):** English
- **License:** MIT

## Intended Uses & Limitations
### Intended Use
This model is intended to be used as an early-risk detection and awareness tool to assist in research, moderation systems, or educational NLP applications. It analyzes text (e.g., social media posts) to classify the presence of mental health indicators.

### Limitations & Ethical Considerations
- **Not a Diagnostic Tool:** This model is designed strictly for educational, research, and awareness purposes. It is **not a medical diagnostic tool**.
- **Accuracy Constraints:** Machine learning models can produce false positives and false negatives. It struggles with complex nuances such as sarcasm, irony, or cultural variations in emotional expression.
- **No Replacement for Professionals:** Predictions made by this model should never replace professional psychological assessment or clinical judgment. If you or someone you know is struggling, please reach out to professional mental health services or a crisis lifeline.

## Training Data
The model was fine-tuned on the [Reddit Mental Health Dataset](https://www.kaggle.com/datasets/entenam/reddit-mental-health-dataset) sourced from Kaggle. The dataset contains anonymous social media posts from Reddit, categorized by various psychological conditions and a neutral control group.

A balanced subset of this dataset was used, sampling up to 2,000 rows per class to prevent class imbalance and memory issues. 

## Model Labels
The model classifies input text into one of the following 6 labels:
1. `Depression`
2. `Anxiety`
3. `Loneliness`
4. `Mental Health` (General distress or mental health discussion)
5. `High Risk (SW)` (Indicators of severe clinical distress or self-harm)
6. `Other` (Neutral or out-of-scope text)

## Training Procedure
### Preprocessing
- Text was converted to lowercase.
- URLs and special characters were removed using regex.
- Tokenized using the `distilbert-base-uncased` tokenizer with padding and truncation (max length = 256).

### Hyperparameters
- **Learning Rate:** 2e-5
- **Train Batch Size:** 16
- **Eval Batch Size:** 16
- **Epochs:** 3
- **Weight Decay:** 0.01

## How to Get Started with the Model
You can use this model directly with a pipeline for text classification:

```python
from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", model="Gojosen/mental-health-distilbert", top_k=None)

# Analyze text
text = "I've been feeling incredibly isolated and anxious about the future."
predictions = classifier(text)

print(predictions)
```

## GitHub Repository & Application Integration
This model is the core predictive engine for the **Mental Health Text Risk Detector** project. The full source code, including the web application and training notebooks, is available on GitHub.

- **GitHub Repository:** [Mental-Health-Text-Risk-Detector-Using-DistilBERT](https://github.com/gitarju/Mental-Health-Text-Risk-Detector-Using-DistilBERT)

### Running the Application Locally
To use the model via the interactive Streamlit web application:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gitarju/Mental-Health-Text-Risk-Detector-Using-DistilBERT.git
   cd Mental-Health-Text-Risk-Detector-Using-DistilBERT
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

In the application, predictions from this model are further processed using custom confidence thresholds, NLP syntactic analysis (using SpaCy), and extreme crisis keyword bypasses to reduce false positives and ensure appropriate routing for critical cases.
