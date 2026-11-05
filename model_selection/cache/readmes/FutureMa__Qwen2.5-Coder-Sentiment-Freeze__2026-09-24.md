---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
tags:
- qwen
- qwen2.5
- sentiment-analysis
- chinese
- freeze-tuning
- llama-factory
metrics:
- accuracy
base_model:
- Qwen/Qwen2.5-Coder-1.5B-Instruct
---

# Qwen2.5-Coder-Sentiment-Freeze
This is a fine-tuned version of `Qwen/Qwen2.5-Coder-1.5B-Instruct` specialized for **Chinese sentiment analysis**.

The model was trained using the efficient **freeze training** method on the **ChnSentiCorp** dataset. By training only the last 6 layers, this approach achieved a significant performance boost, increasing accuracy from **91.6% to 97.8%** on the evaluation set.

This model is designed to classify Chinese text into **positive (1)** or **negative (0)** sentiment and output the result in a clean JSON format.

## 🚀 Full Tutorial & Repository

This model was trained as part of a comprehensive, beginner-friendly tutorial that walks through every step of the process, from data preparation to evaluation and deployment.

### 👉 [**GitHub Repository: IIIIQIIII/MSJ-Factory**](https://github.com/IIIIQIIII/MSJ-Factory)

The repository includes:
- 💻 A step-by-step Google Colab notebook.
- ⚙️ All training and evaluation scripts.
- 📊 Detailed explanations of the training method and results.

**If you find this model or the tutorial helpful, please give the repository a ⭐️ star! It helps support the author's work.**

[![GitHub Stars](https://img.shields.io/github/stars/IIIIQIIII/MSJ-Factory?style=social)](https://github.com/IIIIQIIII/MSJ-Factory)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IIIIQIIII/MSJ-Factory/blob/main/Qwen2_5_Sentiment_Fine_tuning_Tutorial.ipynb)

## 💡 How to Use
This model follows a specific instruction format to ensure reliable JSON output. Use the prompt template below for the best results.

``````python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Model repository on Hugging Face Hub
model_name = "FutureMa/Qwen2.5-Coder-Sentiment-Freeze"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# --- Define the text for sentiment analysis ---
text = "这个酒店的服务态度非常好，房间也很干净！" # Example: "The service at this hotel was excellent, and the room was very clean!"

# --- Create the prompt using the required template ---
prompt = f"""请对以下中文文本进行情感分析，判断其情感倾向。

任务说明：
- 分析文本表达的整体情感态度
- 判断是正面(1)还是负面(0)

文本内容：
```sentence
{text}
```

输出格式：
```json
{{
  "sentiment": 0 or 1
}}
```"""

messages = [{"role": "user", "content": prompt}]
text_input = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
model_inputs = tokenizer([text_input], return_tensors="pt").to(model.device)

# --- Generate the response ---
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=256,
    temperature=0.1
)
response = tokenizer.batch_decode(generated_ids[:, model_inputs.input_ids.shape[1]:], skip_special_tokens=True)[0]

print(f"Input Text: {text}")
print(f"Model Output:\n{response}")

# Expected output for the example text:
# Input Text: 这个酒店的服务态度非常好，房间也很干净！
# Model Output:
# ```json
# {
#   "sentiment": 1
# }
# ```
``````

## 📊 Evaluation Results

The fine-tuned model shows significant improvements across all key metrics compared to the base model. It demonstrates perfect precision, meaning it makes no false positive predictions on the test set.

| Model                                | Accuracy | Precision | Recall   | F1-Score |
|--------------------------------------|----------|-----------|----------|----------|
| Base Model (Qwen2.5-Coder-1.5B)      | 91.62%   | 98.57%    | 83.13%   | 90.20%   |
| **This Model (Fine-tuned)**          | **97.77%** | **100.00%** | **95.18%** | **97.53%** |

## ⚙️ Training Details

- **Base Model**: [`Qwen/Qwen2.5-Coder-1.5B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct)
- **Dataset**: A balanced 3,000-sample subset of [ChnSentiCorp](https://huggingface.co/datasets/seamew/ChnSentiCorp).
- **Training Method**: Freeze Training (only the last 6 layers and embeddings were trained).
- **Framework**: [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- **Hardware**: T4 GPU (via Google Colab)
- **Training Time**: ~20 minutes

## ⚠️ Limitations and Bias

- **Task-Specific**: This model is highly specialized for Chinese sentiment analysis. It may not perform well on other NLP tasks or languages without further fine-tuning.
- **Binary Classification**: The model is designed for binary (positive/negative) classification and does not capture neutral or mixed sentiment.
- **Data Bias**: The model inherits any biases present in the ChnSentiCorp dataset, which primarily consists of hotel and product reviews. Its performance may vary on text from different domains.

## Citation

If you use this model or the associated tutorial in your work, please cite the repository:

```bibtex
@misc{msj-factory-2025,
  title={Qwen2.5-Coder Sentiment Analysis Fine-tuning Tutorial},
  author={MASHIJIAN},
  year={2025},
  howpublished={\url{https://github.com/IIIIQIIII/MSJ-Factory}}
}
```

## Acknowledgments
This work would not be possible without the incredible open-source tools and models from the community:
- [Qwen Team](https://github.com/QwenLM) for the powerful base model.
- [Hugging Face](https://huggingface.co/) for the `transformers` library and model hosting.
- [hiyouga](https://github.com/hiyouga) for the excellent `LLaMA-Factory` framework.
- Google Colab for providing accessible GPU resources.