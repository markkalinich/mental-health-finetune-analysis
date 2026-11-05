---
language:
- en
tags:
- psychology
- emotion-recognition
- nlp
- question-answering
- trigger-extraction
datasets:
- daily_dialog
---

# RECCON: Emotional Trigger Extraction Model

**RECCON** (Recognizing Emotion Cause in CONversations) is a model designed to identify and extract the specific text spans (triggers) within a conversation that correspond to a labeled emotion.

This repository contains the weights and custom inference handler to deploy RECCON as a **Hugging Face Inference Endpoint**.

## 🧠 Model Details

- **Task**: Extractive Question Answering (Span Extraction)
- **Base Model**: `SpanBERT` (without context)
- **Training Dataset**: [RECCON Dataset](https://github.com/declare-lab/RECCON) (derived from DailyDialog)
- **Paper**: [Recognizing Emotion Cause in Conversations (Poria et al., 2021)](https://arxiv.org/abs/2012.11820)

## 🚀 Deployment (Inference Endpoints)

This repository is structured to be deployed directly to [Hugging Face Inference Endpoints](https://ui.endpoints.huggingface.co/).

### Prerequisites
Ensure the following files are present in the root of this repository:
1.  `handler.py`: The custom inference logic (included).
2.  `requirements.txt`: Dependencies (included).
3.  `model.safetensors` (or `pytorch_model.bin`): The model weights.
4.  `config.json`: The BERT model configuration.
5.  `tokenizer.json` / `vocab.json`: Tokenizer files.

### Configuration
When creating the endpoint:
- **Task**: Select **Custom** or **Question Answering**.
- **Container Type**: The custom `handler.py` will automatically be detected and used.

## 💻 API Usage

The endpoint accepts a JSON payload containing an `utterance` and its associated `emotion`. It returns the specific phrase(s) that triggered that emotion.

### Request Format

**Single Input:**
```json
{
  "inputs": {
    "utterance": "I'm so excited about the promotion!",
    "emotion": "happiness"
  }
}
```

**Batch Input (Recommended):**
```json
{
  "inputs": [
    {
      "utterance": "I'm so excited about the promotion!",
      "emotion": "happiness"
    },
    {
      "utterance": "I really miss my family back home.",
      "emotion": "sadness"
    }
  ]
}
```

### Response Format

The model returns a list of objects containing the extracted triggers.

```json
[
  {
    "utterance": "I'm so excited about the promotion!",
    "emotion": "happiness",
    "triggers": [
      "excited about the promotion"
    ]
  },
  {
    "utterance": "I really miss my family back home.",
    "emotion": "sadness",
    "triggers": [
      "miss my family"
    ]
  }
]
```

## 🛠️ logic (handler.py)

The custom handler performs the following steps:
1.  **Preprocessing**: Formats the input into a Question-Answering format: *"Extract the exact short phrase (<= 8 words) from the target utterance that most strongly signals the emotion {emotion}..."*
2.  **Inference**: Runs the RoBERTa model to predict start and end logits.
3.  **Post-processing**:
    *   Extracts the best text span.
    *   Filters out stopwords.
    *   Ensures the trigger is a valid substring of the original text.
    *   Deduplicates overlapping triggers.

## 📚 Citation

If you use this model, please cite the original paper:

```bibtex
@article{poria2021recognizing,
  title={Recognizing Emotion Cause in Conversations},
  author={Poria, Soujanya and Majumder, Navonil and Hazarika, Devamanyu and Ghosal, Deepanway and Bhardwaj, Rishabh and Jian, Samson Yu Bai and Hong, Pengfei and Ghosh, Romila and Roy, Abhinaba and Chhaya, Niyati and others},
  journal={Cognitive Computation},
  pages={1--16},
  year={2021},
  publisher={Springer}
}
```
