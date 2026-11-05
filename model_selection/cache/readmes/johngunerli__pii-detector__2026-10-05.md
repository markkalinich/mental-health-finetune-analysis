---
language:
- en
tags:
- token-classification
- ner
- pii-detection
- distilbert
license: mit
base_model: distilbert-base-uncased
---

# PII Detector: Named Entity Recognition (NER) for Personally Identifiable Information (PII)

## Overview

This project implements a Named Entity Recognition (NER) model to detect Personally Identifiable Information (PII) using a fine-tuned DistilBERT model. It identifies various types of PII such as names, emails, usernames, ID numbers, phone numbers, URLs, and addresses in text.

## Features

- Synthetic data generation for PII-related entities.
- Token classification using BIO tagging format.
- Fine-tuning of DistilBERT for PII detection.
- Model training with Hugging Face's Trainer API.
- Inference pipeline for real-time PII detection.

## Dataset

The dataset is synthetically generated using the Faker library. It includes:

- Student names
- Emails
- Usernames
- ID numbers
- Phone numbers
- Personal URLs
- Street addresses

Each sentence is labeled with corresponding entities in BIO tagging format.

## Installation

To set up the project, install the necessary dependencies:

```bash
pip install torch transformers datasets faker
```

## Usage

### 1. Generate Synthetic Data

Run the `generate_synthetic_data` function to create labeled text samples with PII entities.

### 2. Tokenize and Align Labels

The function `tokenize_and_align_labels` tokenizes input text and aligns the entity labels using Hugging Face's tokenizer.

### 3. Train the Model

Execute the training pipeline using:

```python
trainer.train()
```

This will fine-tune DistilBERT on the labeled dataset.

### 4. Save the Model

The trained model is saved using:

```python
trainer.save_model("./pii_detector")
```

### 5. Run Inference

To detect PII in a given text, use:

```python
pii_detection("Sample text with PII information")
```

This will return identified entities along with their labels.

## Model Configuration

- **Base Model:** distilbert-base-uncased
- **Tokenizer:** AutoTokenizer
- **Training Parameters:**
  - Batch size: 16
  - Number of epochs: 3
  - Evaluation strategy: Per epoch
  - Device: CUDA (if available)

## Output

The model returns a list of detected PII entities with their respective labels and positions in the text.

## License

This project is open-source and can be used for educational and research purposes.