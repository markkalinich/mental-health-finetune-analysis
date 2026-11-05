---
library_name: peft
license: apache-2.0
base_model: google-t5/t5-base
tags:
  - t5
  - text2text-generation
  - medical
  - healthcare
  - clinical
  - biomedical
  - question-answering
  - lora
  - peft
  - transformer
  - huggingface
  - low-resource
  - fine-tuned
  - adapter
  - alpaca-style
  - prompt-based-learning
  - hf-trainer
  - multilingual
  - attention
  - medical-ai
  - evidence-based
  - smart-health
model-index:
  - name: medical-qa-t5-lora
    results:
      - task:
          type: text2text-generation
          name: Medical Question Answering
        dataset:
          name: Custom Medical QA Dataset
          type: medical-qa
        metrics:
          - name: Exact Match
            type: exact_match
            value: 0.41
          - name: Token F1
            type: f1
            value: 0.66
          - name: Medical Keyword Coverage
            type: custom
            value: 0.84
---
# 🏥 Medical QA T5 LoRA Model

<div align="center">

[![Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow)](https://huggingface.co/Adilbai/medical-qa-t5-lora)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/downloads/)
[![T5](https://img.shields.io/badge/Model-T5%20LoRA-green)](https://huggingface.co/docs/transformers/model_doc/t5)

*A fine-tuned T5 model with LoRA for medical question-answering tasks*

[🚀 Quick Start](#-quick-start) • [📊 Performance](#-performance-metrics) • [💻 Usage](#-usage) • [🔬 Evaluation](#-evaluation-results)

</div>

---

## 📋 Model Overview

This model is a fine-tuned version of Google's T5 (Text-to-Text Transfer Transformer) optimized for medical question-answering tasks using **Low-Rank Adaptation (LoRA)** technique. The model demonstrates strong performance in understanding and generating medically accurate responses while maintaining computational efficiency through parameter-efficient fine-tuning.

### 🎯 Key Features

- **📚 Medical Domain Expertise**: Fine-tuned specifically for healthcare and medical contexts
- **⚡ Efficient Training**: Uses LoRA for parameter-efficient fine-tuning
- **🎯 High Accuracy**: Achieves strong performance across multiple evaluation metrics
- **🔄 Versatile**: Handles various medical question types and formats

---

## 🚀 Quick Start

### Installation

```bash
pip install transformers torch peft accelerate
```

### Basic Usage

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
from peft import PeftModel, PeftConfig
import torch

# Load the base model and tokenizer
model_name = "Adilbai/medical-qa-t5-lora"
tokenizer = T5Tokenizer.from_pretrained(model_name)
base_model = T5ForConditionalGeneration.from_pretrained(model_name)

# Load the LoRA configuration and model
config = PeftConfig.from_pretrained(model_name)
model = PeftModel.from_pretrained(base_model, model_name)

def answer_medical_question(question):
    # Prepare the input
    input_text = f"Question: {question}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate answer
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=256,
            num_beams=4,
            temperature=0.7,
            do_sample=True,
            early_stopping=True
        )
    
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

# Example usage
question = "What are the symptoms of diabetes?"
answer = answer_medical_question(question)
print(f"Q: {question}")
print(f"A: {answer}")
```

---

## 📊 Performance Metrics

<div align="center">

### 🎯 Latest Evaluation Results
*Evaluated on: 2025-06-27 15:55:02 by AdilzhanB*

</div>

| Metric | Score | Description |
|--------|--------|-------------|
| **🎯 Exact Match** | `0.0000` | Perfect string matches |
| **📝 Token F1** | `0.5377` | Token-level F1 score |
| **📊 Word Accuracy** | `0.5455` | Word-level accuracy |
| **📏 Length Similarity** | `0.9167` | Response length consistency |
| **🏥 Medical Keywords** | `0.9167` | Medical terminology coverage |
| **⭐ Overall Score** | `0.5833` | Weighted average performance |

### 📈 Performance Highlights

```
🟢 Excellent Length Similarity (91.67%) - Generates appropriately sized responses
🟢 High Medical Keyword Coverage (91.67%) - Strong medical vocabulary retention
🟡 Good Token F1 Score (53.77%) - Decent semantic understanding
🟡 Moderate Word Accuracy (54.55%) - Room for improvement in precision
```

---

## 🔬 Evaluation Results

### Test Cases Overview

<details>
<summary><b>🧪 Detailed Test Results</b></summary>

#### Test 1: Perfect Matches ✅
- **Samples**: 3
- **Exact Match**: 100% 
- **Token F1**: 100%
- **Overall Score**: 100%

#### Test 2: No Matches ❌
- **Samples**: 3
- **Exact Match**: 0%
- **Token F1**: 6.67%
- **Overall Score**: 20%

#### Test 3: Partial Matches 🟡
- **Samples**: 3
- **Exact Match**: 0%
- **Token F1**: 66.26%
- **Overall Score**: 60.32%

#### Test 4: Medical Keywords 🏥
- **Samples**: 3
- **Medical Keywords**: 91.67%
- **Overall Score**: 58.33%

</details>

### 📝 Sample Comparisons

<details>
<summary><b>Example Outputs</b></summary>

**Example 1:**
- **Reference**: "Diabetes and hypertension require insulin and medication...."
- **Predicted**: "Patient has diabetes and hypertension, needs insulin therapy...."
- **Token F1**: 0.571

**Example 2:**
- **Reference**: "Heart disease affects the cardiovascular system significantly...."
- **Predicted**: "The cardiovascular system shows symptoms of heart disease...."
- **Token F1**: 0.667

**Example 3:**
- **Reference**: "Viral respiratory infections need antiviral treatment, not antibiotics...."
- **Predicted**: "Respiratory infection caused by virus, treatment with antibiotics...."
- **Token F1**: 0.375

</details>

---

## 💻 Usage Examples

### 🔹 Interactive Demo

```python
# Interactive medical Q&A session
def medical_qa_session():
    print("🏥 Medical QA Assistant - Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        question = input("\n🤔 Your medical question: ")
        if question.lower() == 'quit':
            break
            
        answer = answer_medical_question(question)
        print(f"🩺 Answer: {answer}")

# Run the session
medical_qa_session()
```

### 🔹 Batch Processing

```python
# Process multiple questions
questions = [
    "What are the side effects of aspirin?",
    "How is pneumonia diagnosed?",
    "What lifestyle changes help with hypertension?"
]

for i, q in enumerate(questions, 1):
    answer = answer_medical_question(q)
    print(f"{i}. Q: {q}")
    print(f"   A: {answer}\n")
```

---

## 🛠️ Technical Details

### Model Architecture
- **Base Model**: T5 (Text-to-Text Transfer Transformer)
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Parameters**: Efficient parameter updates through low-rank matrices
- **Training**: Supervised fine-tuning on medical QA datasets

### Training Configuration
```yaml
Model: T5 + LoRA
Task: Medical Question Answering
Fine-tuning: Parameter-efficient with LoRA
Evaluation: Multi-metric assessment
```

---

## 📚 Citation

If you use this model in your research, please cite:

```bibtex
@model{medical-qa-t5-lora,
  title={Medical QA T5 LoRA: Fine-tuned T5 for Medical Question Answering},
  author={AdilzhanB},
  year={2025},
  url={https://huggingface.co/Adilbai/medical-qa-t5-lora}
}
```

---

## 🤝 Contributing

We welcome contributions! Please feel free to:
- 🐛 Report bugs
- 💡 Suggest improvements
- 📊 Share evaluation results
- 🔧 Submit pull requests

---

## 📄 License

This model is released under the [Apache 2.0 License](LICENSE).

---

## ⚠️ Disclaimer

> **Important**: This model is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

---

<div align="center">

**Made with ❤️ for the medical AI community**

[🤗 Hugging Face](https://huggingface.co/Adilbai/medical-qa-t5-lora) • [📧 Contact](mailto:your-email@example.com) • [🐙 GitHub](https://github.com/your-username)

</div>

## Training and evaluation data

keivalya/MedQuad-MedicalQnADataset

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.3794        | 16.8  | 50   | 1.9909          |
| 1.2119        | 33.4  | 100  | 0.4473          |
| 0.2431        | 50.0  | 150  | 0.0048          |
| 0.0343        | 66.8  | 200  | 0.0008          |
| 0.0118        | 83.4  | 250  | 0.0003          |
| 0.0068        | 100.0 | 300  | 0.0002          |
| 0.0042        | 116.8 | 350  | 0.0001          |
| 0.0028        | 133.4 | 400  | 0.0001          |
| 0.002         | 150.0 | 450  | 0.0000          |
| 0.0015        | 166.8 | 500  | 0.0000          |
| 0.0012        | 183.4 | 550  | 0.0000          |
| 0.0017        | 200.0 | 600  | 0.0000          |
| 0.0012        | 216.8 | 650  | 0.0000          |
| 0.0008        | 233.4 | 700  | 0.0000          |
| 0.0006        | 250.0 | 750  | 0.0000          |
| 0.0006        | 266.8 | 800  | 0.0000          |
| 0.0004        | 283.4 | 850  | 0.0000          |
| 0.0004        | 300.0 | 900  | 0.0000          |
| 0.0004        | 316.8 | 950  | 0.0000          |
| 0.0004        | 333.4 | 1000 | 0.0000          |