---
license: apache-2.0
language: multilingual
tags:
- privacy
- pii-detection
- text-classification
- xlm-roberta
library_name: transformers
base_model: FacebookAI/xlm-roberta-large
datasets:
- Roblox/roblox-pii-classifier-benchmark
---

## Roblox PII Classifier

We present `Roblox/roblox-pii-classifier`, a PII detection classification model that can be used for identifying attempts to share or solicit personally identifiable information in text. The model has been fine-tuned on the [XLM-RoBERTa-Large](https://huggingface.co/xlm-roberta-large) architecture for [multilingual support](https://arxiv.org/pdf/1911.02116).
All the model training has been conducted with Roblox anonymized internal text datasets labeled by experts and AI generated conversations. The specifcs of AI synthetic data generation can be found in the [Tech Blog Post](https://corp.roblox.com/newsroom/2025/11/open-sourcing-roblox-pii-classifier-ai-pii-detection-chat).

The model classifies text into two PII-related categories in a multi-label fashion. The class labels are as follows: `privacy_asking_for_pii` and `privacy_giving_pii`. 
- **PRIVACY_ASKING_FOR_PII**: Attempting to obtain personal identifying information (PII) through direct questions or insinuation.
- **PRIVACY_GIVING_PII**: Sharing or threatening to share someone's personal identifying information (PII), including but not limited to telephone numbers, email addresses, government ID numbers, social media handles, and account passwords/credentials. This category also includes attempts to direct a user off-platform to an external platform or real-world location (DUOP).

The classifier expects text input with a maximum sequence length of 512 tokens. The outputs are uncalibrated scores. The recommended cutoff for pii detection is when the sum of both categories `max(privacy_asking_for_pii, privacy_giving_pii) >= 0.2691`, which achives the optimal F1 score on Roblox English anonymized chat. For per-category cutoffs we recommend `privacy_asking_for_pii >= 0.2` and `privacy_giving_pii >= 0.3`.

The table below displays evaluation metrics on internal held-out datasets and comparisons with other state-of-the-art models.

|Model|F1 Score ([Kaggle PII dataset](https://www.kaggle.com/competitions/pii-detection-removal-from-educational-data/data))|F1 Score (Roblox Annonymized English Chat)|F1 Score (Roblox Annonymized All Languages Chat)|
|---|---|---|---|
|PII Classifier v1.1|45.48%|94.34%|83.10%|
|LlamaGuard v3 1B|5.90%|3.17%|20.88%|
|LlamaGuard v3 8B|5.46%|27.73%|0.03%|
|LlamaGuard v4 12B|3.72%|26.55%|0.08%|
|NemoGuard 8B|3.26%|26.29%|No multilingual support|
|Piiranha NER|33.20%|13.88%|9.11%|

It is worth noting that the model is specifically designed to understand context and detect adversarial patterns where users attempt to bypass filters through creative spelling, character substitution, or implicit references. It focus on conversational context of asking/sharing PII rather than traditional focus on named-entity recognition, and is especially good at detecting subtle attempts to solicit or share PII even when explicit personal information is not present in the text. More technical details can be found in the [Tech Blog Post](https://corp.roblox.com/newsroom/2025/11/open-sourcing-roblox-pii-classifier-ai-pii-detection-chat).


## Usage
The dependencies for the inference file can be installed as follows:
```
pip install -r requirements.txt
```
The provided Python file demonstrates how to use the classifier with text input.
To run the inference, please run the following command:
```
python inference.py --input_file <your text file path> --model_path <path to Huggingface model>
```

If `model_path` isn't specified, the model will be loaded directly from HuggingFace.