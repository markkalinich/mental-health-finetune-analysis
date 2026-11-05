---
datasets:
- SEACrowd/nusatranslation_senti
language:
  - btk
  - bew
  - bug
  - jav
  - mad
  - mak
  - min
  - mui
  - rej
  - sun
base_model:
- LazarusNLP/NusaBERT-large
pipeline_tag: text-classification
task_categories:
  - sentiment-analysis
tags:
  - sentiment-analysis
---
# BERT + BiLSTM Model for Sequence Classification

## Overview

This repository contains a BERT-based model enhanced with a BiLSTM layer for sequence classification tasks. The model allows you to leverage the power of a pre-trained BERT model, combined with the benefits of a BiLSTM, to handle sequence-level tasks like sentiment analysis, text classification, and more.

## Features:
- **Pre-trained BERT model**: Leverage BERT's embeddings for robust language understanding.
- **BiLSTM layer**: Capture sequential dependencies in both directions (forward and backward).
- **Customizable freezing of BERT layers**: Choose which layers of the BERT model you want to freeze, and whether to freeze from the start or the end.
- **Inference without labels**: Get logits directly for inference in production, with no need for labels.
- **Logging for better debugging**: Includes logging for important events like model initialization, layer freezing, and inference.

## Installation:

1. Install the necessary dependencies:
   ```bash
   pip install transformers torch
   ```

2. Clone this repository and navigate to the project folder:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

## Configuration:

The model's behavior can be customized using the following configuration options:

- **`freeze_bert`**: If `True`, the BERT model's layers will be frozen according to the specified settings.
- **`freeze_n_layers`**: An integer that defines the number of layers to freeze.
- **`freeze_from_start`**: If `True`, freeze the first `n` layers from the start; if `False`, freeze the last `n` layers from the end.
- **`concat_layers`**: Number of BERT layers to concatenate for the final sequence output.
- **`pooling`**: Type of pooling to apply. Options: `'last'`, `'mean'`, etc.

Example usage for configuring the model:

```python
from transformers import BertTokenizer
from modeling_bert_bilstm import BertBiLSTMForSequenceClassification, BertBiLSTMConfig

# Configure the model
config = BertBiLSTMConfig(
    bert_model_name="bert-base-uncased",
    freeze_bert=True,
    freeze_n_layers=10,
    freeze_from_start=False  # Freeze the last 10 layers
)

# Initialize the model
model = BertBiLSTMForSequenceClassification(config)

# Print model's freeze summary
freeze_summary = model.get_freeze_summary()
print(freeze_summary)
```

## Training the Model:

To train the model, you need to prepare your dataset and use standard PyTorch training loops. Here’s an outline of how you might train the model:

```python
from torch.utils.data import DataLoader
from transformers import AdamW
import torch

# Create DataLoader, model, optimizer, etc.
train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
optimizer = AdamW(model.parameters(), lr=1e-5)

for epoch in range(num_epochs):
    model.train()
    for batch in train_dataloader:
        input_ids = batch["input_ids"]
        attention_mask = batch["attention_mask"]
        labels = batch["labels"]

        optimizer.zero_grad()
        output = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = output["loss"]
        loss.backward()
        optimizer.step()
```

## Inference (Prediction without Labels):

For serving the model in production, the model can be used for inference without needing labels.

### Example Forward Pass for Inference:

```python
import torch

# Example input (input_ids, attention_mask)
input_ids = torch.tensor([[101, 2054, 2003, 102]])  # Example tokenized input
attention_mask = torch.tensor([[1, 1, 1, 1]])       # Example attention mask

# Get logits for prediction (no labels required)
logits = model(input_ids=input_ids, attention_mask=attention_mask)
print(logits)
```

### Logging:

This model includes logging to help with debugging and monitoring during training and inference. Logs include information such as:
- Initialization of the BERT model.
- Freezing layers.
- Inference start and completion.

To configure logging:

```python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger(__name__)

# Example log messages
logger.info("Model initialized with BERT model: %s", config.bert_model_name)
logger.info(f"Freezing the top {config.freeze_n_layers} layers of BERT.")
```

## Model Freezing Configuration:

You can customize which layers of BERT to freeze. The `freeze_n_layers` parameter allows you to freeze a specific number of layers either from the start or the end of the BERT model:

- **`freeze_from_start=True`**: Freeze the first `n` layers.
- **`freeze_from_start=False`**: Freeze the last `n` layers.

### Example of Freezing Layers:

```python
config = BertBiLSTMConfig(
    freeze_bert=True,
    freeze_n_layers=10,  # Freeze the last 10 layers
    freeze_from_start=False  # Freeze from the end
)
```

## Model Summary:

You can view a summary of which layers are frozen and which are trainable by using the `get_freeze_summary()` method:

```python
freeze_summary = model.get_freeze_summary()
print(freeze_summary)
```

Example output:

```python
[
  {"layer": "bert.encoder.layer.0", "trainable": False},
  {"layer": "bert.encoder.layer.1", "trainable": False},
  {"layer": "bert.encoder.layer.2", "trainable": True},
  {"layer": "bert.encoder.layer.3", "trainable": True},
  ...
]
```

## Notes:
- This model is production-ready for serving via APIs like **FastAPI** or **Flask** for real-time predictions.
- Make sure to handle logging and exception management properly in production.

## License:
This repository is licensed under the MIT License. See the LICENSE file for more information.