---
language:
- ca
- es
- en
license: apache-2.0
base_model:
- BSC-LT/salamandra-7b-instruct
tags:
- guardrails
datasets:
- BSC-LT/salamandra-guard-dataset
---

# Salamandra-7b-instruct-guard

Salamandra-7b-instruct-guard is a state-of-the-art safety classification model designed for Catalan, Spanish, and English content moderation. Built on the Salamandra-7B-Instruct foundation model from Barcelona Supercomputing Center (BSC), it provides both binary (safe/unsafe) and multiclass safety classification capabilities.

## Model Details

### Model Description

Salamandra-7b-instruct-guard is a fine-tuned safety guardrail model that classifies text content across multiple safety categories. The model addresses three primary categories of unsafe content: Dangerous Content, Toxic Content, and Sexual Content

The model is specifically optimized for European languages, with particular emphasis on Catalan—a language often overlooked in existing safety models—alongside Spanish and English.

- **Developed by:** Barcelona Supercomputing Center (BSC)
- **Model type:** Text Classification (Safety Guardrail)
- **Language(s):** Catalan, Spanish, English
- **License:** Apache 2.0
- **Finetuned from model:** bsc/salamandra-7b-instruct

### Salamandra Guard Technical Report

[Technical Report](https://huggingface.co/datasets/BSC-LT/salamandra-guard-dataset/blob/main/Salamandra_Guard_Technical_Report.pdf)

### Model Sources

- **Repository:** [https://huggingface.co/BSC-LT/salamandra-7b-instruct](https://huggingface.co/BSC-LT/salamandra-7b-instruct)
## Uses

### Direct Use

Salamandra-7b-instruct-guard can be used directly for:

- Content moderation in chat applications
- Safety filtering for LLM responses
- Multi-language safety classification (Catalan, Spanish, English)
- Real-time content screening in production environments
- Binary classification (safe vs unsafe content)

### Downstream Use

The model can be integrated into:

- Conversational AI systems as a guardrail layer
- Content moderation pipelines for social platforms
- Educational technology platforms requiring safety filtering
- Customer service chatbots operating in Spanish/Catalan markets
- Few-shot or zero-shot classification tasks with custom safety categories
- Fine-tuning for domain-specific safety applications

### Out-of-Scope Use

The model is **not designed for**:

- Detecting adversarial unsafe requests (acknowledged limitation)
- Legal determination of content violations
- Replacing human moderation in critical safety contexts
- Languages outside Catalan, Spanish, and English
- Real-time detection of rapidly evolving harmful content trends without retraining

## Safety Taxonomy

### High-Level Categories (C0-C3)

**C0: Safe Content**

- Content that does not violate any safety policies

**C1: Dangerous Content**

- Violent crimes (terrorism, murder, assault, child abuse, animal cruelty)
- Gender-based violence and domestic violence
- Suicide and self-harm
- Non-violent crimes (fraud, theft, drug crimes, cybercrimes, weapons violations)

**C2: Toxic Content**

- Hate speech and discrimination based on protected characteristics
- Harassment, bullying, and doxxing
- Profanity and offensive language (culturally adapted)

**C3: Sexual Content**

- Sexual offenses and exploitation (trafficking, assault, harassment)
- Sexually explicit content and pornography



## Training Details

### Training Data

[BSC-LT/salamandra-guard-dataset](https://huggingface.co/datasets/BSC-LT/salamandra-guard-dataset)

The model was trained on a combined dataset of 21,335 safety-related observations:

1. **salamandra-guard-dataset (5,016 samples):** Human-annotated and proofread data in Catalan and Spanish
    - 3 human annotations per sample
    - 2 LLM judge annotations per sample
    - Professional translation with expert proofreading (250 samples)
    - Crowdsourced proofreading for remaining samples
2. **Machine-translated data (16,319 samples):** LLM-annotated translations from Nemotron-Safety-Guard-Dataset-V3

**Data split:** 80% train / 20% validation-test

**Source dataset:** nvidia/Nemotron-Safety-Guard-Dataset-V3 (Spanish subset + translations)

### Training Procedure

**Fine-tuning approach:**

- LoRA (Low-Rank Adaptation) applied to all attention layers
- Maximum sequence length: 8,192 tokens
- Training objectives: Binary classification and multiclass classification
- Two separate models trained: Binary and Multiclass variants

**Training hyperparameters:**

- **Optimizer:** AdamW
- **Learning rate:** 5e-5
- **Training epochs:** 3
- **Batch processing:** Distributed Data Parallel across 4× A100 GPUs
- **Framework:** Hugging Face Accelerate
- **Loss function:** Cross-entropy (single-label) / CausalLM (generative classification)

## Evaluation

### Testing Data

**Test set:** 722 samples from SalGuard_10k

- Catalan: 210 samples
- Spanish: 211 samples
- English: 300 samples

### Metrics

**Binary Classification:**

- **Accuracy:** 0.798
- **Weighted F1:** 0.797

**Multiclass Classification (C0-C3):**

- **Accuracy:** 0.733
- **Weighted F1:** 0.731

**Per-class F1 scores (Multiclass):**

- C0 (Safe): 0.75
- C1 (Dangerous): 0.75
- C2 (Toxic): 0.64
- C3 (Sexual): 0.78

### Results

#### Comparison with Baseline Models

**Binary Classification (Weighted F1):**

|Model|Weighted F1|
|---|---|
|**Salamandra-7b-instruct-guard (Binary)**|**0.797**|
|LlamaGuard 3|0.717|
|Salamandra 7B (base)|0.661|
|ShieldGemma 9B|0.638|

**Multiclass Classification (Weighted F1):**

|Model|Weighted F1|
|---|---|
|**Salamandra-7b-instruct-guard (Multiclass)**|**0.731**|
|LlamaGuard 3|0.618|
|ShieldGemma 9B|0.607|
|SalGuard V1|0.568|
|Salamandra 7B (base)|0.420|

**Key improvements:**

- **+21% relative improvement** over base model in binary classification
- **+76% relative improvement** over base model in multiclass accuracy
- **+28% relative improvement** over SalGuard V1 in multiclass classification

#### Language-Specific Performance

The model demonstrates robust cross-language performance:

**Binary (Weighted F1):**

- Catalan: 0.796
- Spanish: 0.798

**Multiclass (Weighted F1):**

- Catalan: 0.728
- Spanish: 0.734

## Bias, Risks, and Limitations

### Known Limitations

1. **Adversarial robustness:** The model focuses on moderating LLM responses and is not robust against adversarial unsafe user requests
    
2. **Toxic Content (C2) detection:** Lower performance on hate speech, harassment, and profanity compared to dangerous and sexual content categories
    
3. **False positives:** May flag safe discussions about dangerous topics (e.g., news about crimes) as harmful content
    
4. **Context sensitivity:** Struggles with subtle contextual distinctions between discussing harmful topics and promoting them
    
5. **Crowdsourced data quality:** Subset of training data proofread by crowdworkers may have variable linguistic quality compared to expert-reviewed samples
    
6. **Annotation disagreement:** Significant disagreement exists between human annotators and between humans and LLM judges, reflecting inherent subjectivity in safety classification
    

### Bias Considerations

- **Cultural adaptation:** Profanity (S6) definitions are culturally adapted for Catalan and Spanish contexts
- **Annotator bias:** Training labels reflect moderate inter-annotator agreement (Cohen's κ: 0.455-0.506, Krippendorff's α: 0.481)
- **LLM judge bias:** GPT-4o and Nemotron show divergent safety interpretations; Nemotron is more conservative (higher false positive rate)

### Recommendations

Users should:

- Combine model outputs with human review for high-stakes moderation decisions
- Be aware that the model may over-flag benign content mentioning sensitive topics
- Consider domain-specific fine-tuning for specialized applications
- Implement monitoring systems to track false positive and false negative rates in production
- Use the binary model for general safe/unsafe classification and multiclass for detailed category identification
- Understand that safety classification involves inherent subjectivity and cultural context

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "bsc/salamandra-guard-v2-binary"  # or salamandra-guard-v2-multiclass
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input
text = "Your text to classify here"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=8192)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1)

# Binary model: 0 = Safe, 1 = Unsafe
# Multiclass model: 0 = Safe, 1 = Dangerous, 2 = Toxic, 3 = Sexual
print(f"Predicted class: {predicted_class.item()}")
print(f"Confidence scores: {predictions}")
```

For conversational context:

```python
conversation = [
    {"role": "user", "content": "User message here"},
    {"role": "assistant", "content": "Assistant response to classify"}
]

# Format as chat
formatted_text = tokenizer.apply_chat_template(conversation, tokenize=False)
inputs = tokenizer(formatted_text, return_tensors="pt", truncation=True, max_length=8192)

# Classify
with torch.no_grad():
    outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=-1)
```

## Model Architecture

- **Base architecture:** Salamandra-7B-Instruct (7 billion parameters)
- **Context length:** 8,192 tokens
- **Adaptation method:** LoRA on all attention layers
- **Classification heads:** Separate binary and multiclass variants
- **Output format:** Generative (CausalLM) and discriminative (cross-entropy) modes supported

## Environmental Impact

- **Hardware Type:** 4× NVIDIA A100 GPUs
- **Training time:** 3 epochs (exact hours not specified)
- **Carbon emissions:** Not yet calculated

## Citation

**BibTeX:**

```bibtex
@techreport{salamandra_guard_v2_2025,
  title={Salamandra Guard: Technical Report},
  author={Alinia},
  year={2025},
  institution={BSC}
}
```


## Additional Information


### Contact
For further information, please send an email to <langtech@bsc.es>.

### Copyright
Copyright(c) 2025 by Language Technologies Laboratory, Barcelona Supercomputing Center.

### License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding ###

This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project ILENIA with reference 2022/TL22/00215337.