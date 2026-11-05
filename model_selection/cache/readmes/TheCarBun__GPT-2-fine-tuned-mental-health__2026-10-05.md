---
language: "en"
license: "apache-2.0"
tags:
  - text-generation
  - transformers
  - mental-health
  - gpt-2
  - conversational-ai
datasets:
  - custom-dataset
  - kaggle
metrics:
  - perplexity
  - BLEU
  - ROUGE
---

# GPT-2 Fine-Tuned Mental Health Chatbot  
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model-yellow?logo=huggingface)](https://huggingface.co/TheCarBun/GPT-2-fine-tuned-mental-health)  
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## 📝 Model Description  
This is a fine-tuned **GPT-2 model** specialized for **mental health support conversations**. It provides **empathetic responses** to users feeling distressed, stressed, or anxious. This model is trained on a custom dataset with carefully crafted conversational data.  

🚀 **Use case:** AI-driven **mental health support** chatbot.  
🛠 **Base Model:** [GPT-2](https://huggingface.co/gpt2)  
📁 **Dataset:** Custom dataset based on `intents.json` + Kaggle conversational dataset  

---

## 📂 Model Files  
| File | Description |
|------|------------|
| `config.json` | Model configuration |
| `pytorch_model.bin` | Model weights |
| `tokenizer.json` | Tokenizer configuration |
| `vocab.json` | Vocabulary file |
| `training_args.bin` | Training hyperparameters |
| `generation_config.json` | Generation settings |

---

## 🏗️ Training Details  
The model was fine-tuned on **Google Colab** using the **Hugging Face Transformers library**.  
Training was performed using:  
- **Optimizer:** AdamW  
- **Learning Rate:** `5e-5`  
- **Batch Size:** `8`  
- **Epochs:** `5`  

### 📊 Training Performance  
| Epoch | Training Loss | Validation Loss |
|-------|--------------|----------------|
| 1 | 1.1932 | 1.0248 |
| 2 | 0.7532 | 0.7870 |
| 3 | 0.7520 | 0.6927 |
| 4 | 0.6018 | 0.6580 |
| 5 | 0.5192 | 0.6403 |

---

## 🚀 How to Use the Model  
You can load and use the model with **Hugging Face Transformers**:

```python
from transformers import pipeline

# Load the model
chatbot = pipeline("text-generation", model="TheCarBun/GPT-2-fine-tuned-mental-health")

# Test the chatbot
user_input = "I feel so alone."
response = chatbot(f"User: {user_input} AI:", max_length=50)
print(response[0]['generated_text'])
```

📝 **Note:** If running locally, install dependencies first:  
```bash
pip install transformers torch
```

---

## 🛠️ Future Improvements  
- **Expand dataset** to cover more diverse mental health conversations  
- **Improve response coherence** by fine-tuning with reinforcement learning  
- **Optimize model size** for deployment on mobile devices  

---

## 📜 License  
This model is licensed under the **Apache 2.0 License**. You are free to use, modify, and distribute it with proper attribution.  

📌 **Hugging Face Model Link:** [GPT-2 Fine-Tuned Mental Health](https://huggingface.co/TheCarBun/GPT-2-fine-tuned-mental-health)  

---

✨ **If you find this model useful, give it a star on Hugging Face!** ⭐  