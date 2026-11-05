---
language: ar
license: apache-2.0 # Or your preferred license (e.g., mit, cc-by-sa-4.0)
tags:
- text-classification
- arabic
- sentiment-analysis
- arabert
pipeline_tag: text-classification # Important for the widget
datasets:
- emotone-ar-cicling2017/emotone_ar
metrics:
- accuracy
- f1
widget:
# Example texts for the inference widget
- text: "أنا أحب هذا المنتج كثيرا!" # I like this product very much!
- text: "هذا أسوأ شيء جربته على الإطلاق." # This is the worst thing I have ever tried.
- text: "كان الأمر مفاجئاً بعض الشيء." # It was a bit surprising.
---

# Arabic Sentiment Analysis Model (arabic-bert-sentiment)

<!-- Provide a quick summary of what the model is/does. -->
This model is a fine-tuned version of `aubmindlab/bert-base-arabertv2` trained on the `emotone-ar-cicling2017/emotone_ar` dataset for Arabic sentiment analysis, classifying text into 8 distinct sentiment categories.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->
This model was developed as part of a graduation project to build a classifier capable of understanding and identifying sentiments expressed in short Arabic texts (such as tweets or reviews). The model leverages the BERT architecture, specifically the AraBERTv2 version pre-trained on a large corpus of Arabic text. The final layers of the model were fine-tuned for the multi-class classification task (8 sentiment classes).

- **Developed by:** Bedour Fouad (or your full name/team)
- **Shared by [optional]:** Bedour Fouad (if you are sharing the model)
- **Model type:** bert (BERT)
- **Language(s) (NLP):** Arabic (ar)
- **License:** apache-2.0 (or your chosen license)
- **Finetuned from model:** `aubmindlab/bert-base-arabertv2`

### Model Sources [optional]

- **Repository:** `https://huggingface.co/bedourfouad/arabic-bert-sentiment` (Your model repo link)
- **Paper [optional]:** (Link if there's an associated research paper)
- **Demo [optional]:** (Link to your Gradio/Streamlit Space if you create one)

## Uses

### Direct Use

The model can be used directly for classifying the sentiment of Arabic text using the `pipeline` function from the `transformers` library. See the "How to Get Started" section below.

### Downstream Use [optional]

This model can serve as a starting point for further fine-tuning on other Arabic NLP tasks or different sentiment analysis datasets.

### Out-of-Scope Use

The model is designed for classifying text into the specific sentiment categories present in the training data. It may not be suitable for:
*   Sentiment analysis of Arabic dialects significantly different from MSA or Egyptian Arabic (if underrepresented in the training data).
*   Understanding complex sarcasm or nuanced figurative language.
*   Tasks other than sentiment classification (e.g., question answering, summarization).
*   Determining the intensity of sentiment (e.g., very happy vs. slightly happy).

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
Like any language model, this model might reflect biases present in the original training data (`emotone_ar`). Potential biases could relate to topics, linguistic style, or prevalent viewpoints in the data. Model performance may vary depending on the text type and dialect used. Results should be interpreted with caution and not be solely relied upon for critical decisions, especially in sensitive applications.

### Recommendations

Users (both direct and downstream) are advised to evaluate the model's performance on their specific datasets before full deployment. Awareness of its limitations and potential biases is crucial.

## How to Get Started with the Model

Use the code below to get started with the model using the `pipeline` from the `transformers` library:

```python
from transformers import pipeline

# Use your repository ID
repo_id = "bedourfouad/arabic-bert-sentiment"
classifier = pipeline("text-classification", model=repo_id)

text1 = "أنا سعيد جدا بهذا المنتج الرائع!" # I am very happy with this wonderful product!
results1 = classifier(text1)
print(f"Text: {text1}\nResult: {results1}")

text2 = "هذا الفيلم كان مملاً جداً ولم يعجبني أبداً." # This movie was very boring and I didn't like it at all.
results2 = classifier(text2)
print(f"Text: {text2}\nResult: {results2}")