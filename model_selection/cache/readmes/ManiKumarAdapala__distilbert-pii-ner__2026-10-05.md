---
license: afl-3.0
datasets:
- ai4privacy/pii-masking-200k
language:
- en
metrics:
- precision
- recall
- f1
base_model:
- distilbert/distilbert-base-cased
pipeline_tag: token-classification
library_name: transformers
---



# NLP Applications (S1-25_AIMLCZG519)

## Assignment 2 – Problem Statement – 25

### Submitted by: Group 108

* **ADAPALA MANI KUMAR**
* **BHAT MITALI MAHENDRA**
* **CHELLAPPAN C**
* **ELLURU SAI GAGAN**
* **MD FAREED FAROOQUI**

Finetuned Model & Project URL : https://drive.google.com/drive/folders/19ZP1RG_9Ms_kzsiLYBMrtrUbETej5dLq?usp=sharing

# PII Detection and Masking System

This project implements a PII (Personally Identifiable Information) detection and masking system using **DistilBERT** fine-tuned on the `ai4privacy/pii-masking-200k` dataset. The system exposes a Flask API for uploading text files and returning masked outputs.



## 🚀 Features

* Transformer-based Named Entity Recognition (NER)
* Detects multiple PII categories (Email, Phone, SSN, IP, etc.)
* Batch processing (2 lines at a time)
* REST API using Flask
* Optimized with FP16 training
* Entity-level F1 Score: **92.16%**



## 📂 Project Structure

```
.
.
├── app.py
├── design_document.docx
├── distilbert-ner
│   └── checkpoint-10880
│       ├── config.json
│       ├── model.safetensors
│       ├── tokenizer_config.json
│       ├── tokenizer.json
│       ├── trainer_state.json
│       └── training_args.bin
├── NER_Masking.pdf
├── NER_Masking.ipynb
├── readme.md
├── sample.txt
└── templates
    └── index.html
```



## ⚙️ Installation

1. Download the repository 

```
https://drive.google.com/drive/folders/19ZP1RG_9Ms_kzsiLYBMrtrUbETej5dLq?usp=sharing
```

2. Create and activate environment:

```bash
conda create -n pii python=3.10
conda activate pii
```

3. Install dependencies:

```bash
pip install gdown torch matplotlib transformers datasets seqeval scikit-learn seaborn numpy ipywidgets 
```

## **Train the Model**

To Train the Model run every cell in the file `NER_Masking.ipynb`


## ▶️ Run the Application

To run the Flask API:

```bash
python app.py
```

The server will start locally (default: `http://127.0.0.1:5000`).



## 📤 API Usage

Nice. You now have two clean portals into your PII engine, like two doors to the same vault, one for raw text, one for files. Here is a concise explanation you can add to your README under an **API Endpoints** section.


### 🌐 API Endpoints

### 1️⃣ `/predict`

**Method:** `POST`
**Description:** Performs PII detection on raw text input.

**Request Body (JSON):**

```json
{
  "text": "Your input text here"
}
```

**Response:**

```json
{
  "masked": "Masked text output",
  "highlighted": "<html with highlighted entities>"
}
```

* Calls `pii_inference(text)`
* Returns both masked text and dynamically highlighted HTML output

---

### 2️⃣ `/upload`

**Method:** `POST`
**Description:** Uploads a `.txt` file and processes it in batches of 5 lines.

**Form-Data Key:**

```
file
```

**Processing Logic:**

* Reads file
* Splits into lines
* Processes 5 lines at a time
* Runs `pii_inference` on each batch
* Merges results into final masked output
* Generates highlighted HTML

**Response:**

```json
{
  "masked": "Final masked text",
  "highlighted": "<html with highlighted entities>"
}
```

---

### 🔍 Design Insight

* `/predict` → Low latency, single inference call
* `/upload` → Memory-efficient batch processing
* Batch size (5 lines) prevents long-sequence instability in transformer inference



## 🧠 Model Details

* **Base Model:** DistilBERT
* **Dataset:** ai4privacy/pii-masking-200k
* **Training Framework:** Hugging Face Trainer
* **Batch Size:** 32
* **Epochs:** 10
* **Mixed Precision (FP16):** Enabled



## 📊 Performance

* Precision: **90.86%**
* Recall: **93.50%**
* F1 Score: **92.16%**

Strong performance on structured PII types such as Email, URL, SSN, and Username.



## 🔮 Future Improvements

* Add CRF layer for structured decoding
* Improve low-performing entity categories
* Model quantization for faster inference
* Hybrid LLM-based validation layer
