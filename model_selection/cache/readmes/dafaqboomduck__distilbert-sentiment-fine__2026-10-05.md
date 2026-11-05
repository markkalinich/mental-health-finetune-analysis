---
model_name: DistilBERT for Sentiment Classification
version: v1.0.0
date_created: '2025-10-28'
last_updated: '2025-10-28'
authors:
- Razvan Nica
- Filip Šarík
organization: BUas ADS&AI Students
short_description: >
  A fine-tuned checkpoint of the
  'distilbert/distilbert-base-uncased-finetuned-sst-2-english' model, designed
  to classify emotions in English text into seven categories: neutral, anger,
  disgust, fear, happiness, sadness, and surprise.
tags:
- huggingface
- fine-tuned-model
- english
- distilbert
- pytorch
- emotion
- emotion-classification
license: mit
datasets:
- roskoN/dailydialog
- boltuix/emotions-dataset
- google-research-datasets/go_emotions
language:
- en
metrics:
- f1
- accuracy
base_model:
- distilbert/distilbert-base-uncased-finetuned-sst-2-english
pipeline_tag: text-classification
---

# Model Card: [DistilBERT for Sentiment Classification]

## Overview
**Model Name: DistilBERT for Sentiment Classification**  
**Version: v1.0.0**  
**Date Created: 28/10/2025**  
**Last Updated:28/10/2025**  
**Author(s):Razvan Nica & Filip Šarík**  
**Institution / Organization: BUas ADS&AI**  

**Short Description:**  
This model is a fine-tuned checkpoint of the **[distilbert/distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)** model.

It's designed to **classify emotions** in English text, predicting one of **seven classes**: Ekman's six basic emotions plus a neutral category:

* **0:** "neutral"
* **1:** "anger"
* **2:** "disgust"
* **3:** "fear"
* **4:** "happiness"
* **5:** "sadness"
* **6:** "surprise"

---

## Intended Use

### **Primary Intended Use**

This model was specifically developed and fine-tuned for **emotion analysis in video transcripts**. Its primary intended use is to accurately classify English text into one of the seven defined emotion categories (Ekman's six basic emotions plus a neutral class) extracted from video or audio data.

The model is suitable for general **English text emotion classification**, but its performance is optimized for the conversational and language style found in transcribed speech.

> **Note:** For optimal performance on other tasks or significantly different domains, **further fine-tuning is strongly recommended**.

### **Intended Users**

The model is intended for users who possess a basic working knowledge of the **Python** programming language, the **PyTorch** framework, and the **Hugging Face Transformers library**.

---

## 🛑 Out-of-Scope Use

**Prohibited Uses:** This model **must not** be used to intentionally create **hostile, alienating, or discriminatory environments** or content against individuals or groups.

**Factual Content:** The model was trained for emotion classification, **not for generating factual or true representations** of people or events. Using this model to create or present content as factually accurate is **out-of-scope** and could lead to misrepresentation.

---

## Model Details
### **Model Architecture:**  
This model utilizes a **Transformer architecture**, leveraging the base of the **DistilBERT** model family.

Specifically, it is a fine-tuned checkpoint of the **[distilbert/distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)** model.

For detailed information on the base architecture, please refer to the link above.

### **Purpose & Development Context:**
This model was specifically developed and fine-tuned for **emotion analysis in video transcripts**. Its primary purpose is to accurately classify English text into one of the seven defined emotion categories: Ekman's six basic emotions (*anger, disgust, fear, happiness, sadness, surprise*) plus a neutral class. The fine-tuning process optimized its performance for the conversational language extracted from video and audio data.

This model was commissioned and developed for the **Content Intelligence Agency**. It serves as a crucial component within a larger, automated data pipeline. Its role is to process transcribed show content, extracting **emotional metadata** that is subsequently utilized to perform **show-specific media analysis**. This analysis helps inform content strategy and audience engagement insights.

---

## Dataset Details

### **Training Data:**  
The model was trained on a composite dataset formed by combining three distinct emotion and dialogue datasets to enhance generalization and coverage of conversational text:

* **roskoN/dailydialog**
    * Source: [https://huggingface.co/datasets/roskoN/dailydialog](https://huggingface.co/datasets/roskoN/dailydialog)
* **boltuix/emotions-dataset**
    * Source: [https://huggingface.co/datasets/boltuix/emotions-dataset](https://huggingface.co/datasets/boltuix/emotions-dataset)
* **google-research-datasets/go_emotions**
    * Source: [https://huggingface.co/datasets/google-research-datasets/go_emotions](https://huggingface.co/datasets/google-research-datasets/go_emotions)

The emotions in these datasets were either remapped or removed when they didn't match our 7 class distribution. 
  

### **Validation / Test Data:**  
A custom test set was created to better align with the model's primary use case (video transcript analysis).

1.  **Source Material:** A publicly available episode of **Kitchen Nightmares** was transcribed. The source video is available [here](https://www.youtube.com/watch?v=ozj4T5M5GTk&t=1498s).
2.  **Annotation Process:** Sentences from the transcript were initially annotated using a large language model (LLM). This was followed by a crucial **manual re-annotation** process to correct LLM errors and ensure high-quality, reliable labels for evaluation.
3.  **Size:** The final test dataset comprises **1,228 lines of data**.

### **Training Procedure:**  
* **Learning Rate:** 1e-5
* **Batch Size:** 32
* **Maximum Sequence Length:** 128 (tokens)
* **Weight Decay:** 0.01
* **Unfrozen Layers:** Last 2 encoder blocks
---

## Recommendations for Use

### **Model Inputs**

The input **must be English text data**. Before being fed to the model, the text **must be tokenized** using the specific `AutoTokenizer` loaded from this model's checkpoint.

This preprocessing step is mandatory and ensures the text is:

* Processed using the correct **vocabulary** and **token IDs**.
* **Truncated** or **padded** to a maximum sequence length of **128 tokens**.

> **Warning:** Failure to apply this exact preprocessing step will result in incorrect or unreliable predictions.

---

### **Model Outputs**

The model returns a tensor containing **raw logits** or **probabilities** for each of the seven emotion classes.

To obtain the single, most probable emotion prediction for a given input sentence, we recommend applying the **argmax** function over the output tensor.

The resulting integer ID can be mapped back to its corresponding emotion label using the following dictionary:

```python
EMOTION_MAP: Dict[int, str] = {
    0: "neutral",
    1: "anger",
    2: "disgust",
    3: "fear",
    4: "happiness",
    5: "sadness",
    6: "surprise"
}
```

---