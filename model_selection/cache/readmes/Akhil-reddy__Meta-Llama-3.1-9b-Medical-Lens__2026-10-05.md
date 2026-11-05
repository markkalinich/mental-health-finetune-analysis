---
license: apache-2.0
base_model: unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit
tags:
- medical
- simplification
- healthcare
- fine-tuned
- unsloth
- text-simplification
model_name: LingoLink-Medical-Lens
language:
- en
metrics:
- loss
pipeline_tag: text-classification
---

# Legallens AI: Medical Lens (V2)

**Legallens AI-Medical-Lens** is a fine-tuned version of Meta-Llama-3.1-8B, optimized to act as a "Street-Smart" translator for complex medical documents. It simplifies technical jargon to a 5th-grade reading level and provides a color-coded risk assessment for patients.

## Model Description
- **Project:** Part of the Legallens Hackathon suite.
- **Task:** Medical Text Simplification & Risk Categorization.
- **Base Model:** Meta-Llama-3.1-8B (4-bit Quantized via Unsloth).
- **Training Data:** `medical_v2_balanced.jsonl` (700+ curated medical samples).
- **Output Format:** Structured bullet points including Explanation, Risk Level, and Reason.

## Risk Categorization System
The model uses a specific logic to flag documents for users:
- **🟢 Green (Informational):** Standard health facts, routine medications, and general terminology.
- **🟡 Yellow (Standard Warning):** High-risk procedures (surgery), emergency symptoms, or safety warnings.
- **🟡 Yellow (Financial Caution):** Insurance traps, out-of-network costs, and predatory billing clauses.

## Training Details
- **Optimization:** Fine-tuned using **Unsloth** for 2x faster training and 70% less memory usage.
- **Hardware:** Trained on a single NVIDIA T4 GPU (16GB VRAM).
- **Technique:** LoRA (Low-Rank Adaptation) fine-tuning.
- **Loss:** Final training loss achieved: ~0.82 - 0.88.
- **Balancing:** V2 utilizes oversampling of "Yellow" warning classes to prevent label bias.

## Intended Use & Limitations

- **Intended Use:** This model is designed to help patients understand the "gist" of their medical paperwork by simplifying complex terminology and identifying potential red flags or high-cost items.
- **Limitations:** This is an AI tool, not a medical professional. It may occasionally "over-sensitize" (flagging minor health issues or standard procedures as 🟡 Yellow). **Always consult a qualified medical professional for actual health advice and clinical decisions.**

## Developed By
- **Akhileshwar Reddy Songala** ([LinkedIn](https://www.linkedin.com/in/songala/) | [GitHub](https://github.com/AkhileshwarReddySongala))
- **Ben Gideon Dokkiburra** ([LinkedIn](https://www.linkedin.com/in/bengideondokiburra/) | [GitHub](https://github.com/BenGideon))

---