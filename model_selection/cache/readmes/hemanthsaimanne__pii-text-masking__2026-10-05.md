---
license: gemma
base_model: google/gemma-3-1b-it
tags:
- text-generation
- token-classification
- pii
- privacy
- fine-tuned
- trl
- sft
datasets:
- hemanthsaimanne/pii-text-masking
language:
- en
pipeline_tag: text-generation
---

# Gemma 3 1B - PII Masking Edition

## Model Summary
This model is a fine-tuned, privacy-focused variant of Google's **[Gemma 3 1B Instruction Tuned](https://huggingface.co/google/gemma-3-1b-it)** model. It has been specifically trained using Supervised Fine-Tuning (SFT) to identify, redact, and mask **Personally Identifiable Information (PII)** within unstructured text data. 

The model replaces sensitive elements such as Names, Email Addresses, Phone Numbers, Social Security Numbers (SSN), Credit Card details, and IP Addresses with unified entity placeholders (e.g., `[NAME]`, `[EMAIL]`), ensuring robust compliance with GDPR, HIPAA, and CCPA standards while maintaining the natural linguistic structure of the original document.

### Key Capabilities
- **High-Fidelity Anonymization:** Accurately masks diverse PII entities across conversational, corporate, and financial documents.
- **Context-Aware Redaction:** Distinguishes between generic nouns and specific PII to minimize false-positive masking.
- **Ultra-Lightweight Deployment:** At 1 Billion parameters, this model is highly optimized for fast, cost-effective local deployment on CPU, edge, or mobile environments.

## Intended Use & Prompt Format
This model is configured for causal text generation. To achieve the best PII extraction and masking results, wrap your text in a clear instruction format matching the original Gemma 3 chat template format:

```text
<|im_start|>user
Mask all the PII entities in the following text: "My name is Hemanth and you can reach me at heamnth@email.com or call +919123456789."<|im_end|>
<|im_start|>assistant
My name is [NAME] and you can reach me at [EMAIL] or call [PHONE].<|im_end|>
```

## How to Use

You can easily run this model using the Hugging Face `transformers` library (version `>= 4.50.0` is required for Gemma 3 architecture):

```python
import torch
from transformers import pipeline

# Initialize the pipeline
pipe = pipeline(
    "text-generation", 
    model="hemanthsaimanne/pii-text-masking", 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

# Structure your prompt
messages = [
    {"role": "user", "content": "Mask all PII (names, emails, phones, etc.) in this text: Contact hemanth at hemanth@test.com."}
]

# Generate masked text
outputs = pipe(messages, max_new_tokens=256)
print(outputs[0]["generated_text"])
# Expected Output: "Contact [NAME] at [EMAIL]."
```

## Training Procedure

### Training Hyperparameters
The model was fine-tuned using the **[Hugging Face TRL SFTTrainer](https://huggingface.co)** pipeline under the following parameter adjustments:
- **Method:** Parameter-Efficient Fine-Tuning (PEFT) via LoRA (Low-Rank Adaptation)
- **Learning Rate:** 2e-4
- **Batch Size:** 16 (Global)
- **Optimizer:** AdamW (8-bit)
- **Precision:** Mixed Precision (`bf16`)
- **Context Length:** 32K tokens maximum input context

### Dataset Information
The model was trained on `https://www.kaggle.com/datasets/mikedoes/open-pii-masking-500k-ai4privacy` 

## Limitations & Bias
While the model is highly robust, users should review edge-case extractions manually where data formatting is highly non-standard (e.g., heavily misspelled names or disjointed phone numbers). It should be treated as an assistive compliance utility rather than a perfect legal guarantee for total data anonymization.

## Evaluation Results

The model was evaluated on a held-out test dataset containing dense PII extraction scenarios. It achieves near-perfect structural matching and entity alignment, demonstrating high reliability for enterprise data anonymization workflows.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **ROUGE-1** | `0.9859` | Unigram overlap; measures single-token entity accuracy. |
| **ROUGE-2** | `0.9789` | Bigram overlap; measures multi-word phrase and entity continuity. |
| **ROUGE-L** | `0.9851` | Longest Common Subsequence; evaluates structural syntax matching. |
| **ROUGE-Lsum**| `0.9852` | Summary-level structural match across multi-sentence text. |

### Performance Analysis
- **High Sequence Integrity:** The high ROUGE scores indicate that the model preserves the original textual context perfectly while applying masks.
- **Minimal Hallucinations:** Because ROUGE-2 and ROUGE-L remain near ~0.98, the model rarely adds unwanted tokens or shifts sentence positioning during generation.
