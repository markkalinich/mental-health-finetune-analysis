---
license: mit
base_model: distilbert-base-uncased
tags:
- text-classification
- safety
- mental-health
- guardrails
- neurodiversity
pipeline_tag: text-classification
metrics:
- accuracy
- f1
- precision
- recall
datasets:
- ourafla/Mental-Health_Text-Classification_Dataset
---

# DistilBERT Safety Classifier for Autistic Social Skills Support

This model is a fine-tuned version of `distilbert-base-uncased` developed as part of a Final Year Project at the University of Malta (Faculty of Information & Communication Technology).

The primary objective of this model is to serve as an explicit intent-classification and safety-screening gateway for an AI-powered conversational system designed for autistic students. It evaluates incoming user prompts to differentiate between interactions that can be safely handled by an LLM and those containing high-risk content or emotional distress requiring human support redirection.

## Model Description

- **Developed by:** Liam Jake Vella
- **Supervisors:** Prof. Vanessa Camilleri & Dr. Melvin Attard
- **Model Type:** Binary Sequence Classifier (Transformer-based)
- **Language(s):** English
- **Finetuned from model:** `distilbert-base-uncased`

### Intended Use & Scope
This model acts as a dedicated **safety guardrail layer**. Standard AI chatbots frequently lack adequate guardrails or operate as black boxes, which can cause distress to neurodivergent populations who typically benefit from highly explicit, predictable, and structured reasoning. This classifier safely flags and restricts high-stakes inputs before they ever reach an upstream Large Language Model (LLM) response generator.

- **SAFE (Class 0):** Baseline academic hurdles, peer interaction questions, social script requests, and benign daily conversational topics.
- **UNSAFE (Class 1):** Prompts detailing emotional crisis, severe anxiety, depression, active/passive self-harm ideation, or systemic distress that explicitly demands human or institutional intervention.

---

## Dataset & Training Pipeline

### Training Corpus
The classifier was trained on a meticulously balanced and stratified derivative of the [**Mental Health Text Classification Dataset**](https://huggingface.co/datasets/ourafla/Mental-Health_Text-Classification_Dataset). This multi-source dataset incorporates merged records from:

### Class Remapping & Balancing
The original multiclass annotations (`Normal`, `Depression`, `Suicidal`, `Anxiety`) were compressed into a binary schema:
- `Normal` → **SAFE**
- `Depression` / `Suicidal` / `Anxiety` → **UNSAFE** 

To combat substantial class imbalances and minimize minority class bias, the training set was balanced by matching all safe instances with a randomly sampled down-subset of the unsafe classes using a fixed random seed.

- **Training Samples:** 35,720
- **Validation Samples:** 3,969
- **Test Samples:** 9,923
  
### Input Normalisation Preprocessing
To handle formatting inconsistencies where variations in orthographic casing or punctuation drastically fluctuated downstream model inference, a text normalisation layer is baked into the model's pipeline execution:
- Conversion to lowercase text.
- Absolute removal of URLs, trailing punctuation, and specific special characters.
- Collapsing duplicate whitespaces.

---

## Technical Performance Evaluation

Following training validation adjustments, evaluation on the unseen stratified test split yielded robust safety metrics:

| Metric | Score Value |
| :--- | :--- |
| **Accuracy** | *95.46%* |
| **F1-Score (binary)** | *0.9639* |
| **Precision (Unsafe)** | *0.97* |
| **Recall (Unsafe)** | *0.96* |

### Safety-Critical Optimisations
In deployment pipelines, the classification scoring setup intentionally prioritises **high recall** over pure precision. In safety-critical contexts, it is significantly safer to over-block ambiguous inputs (false positives) than risk exposing a vulnerable individual to unmonitored or hallucinated generative outputs regarding a crisis event (false negatives).

---
### ADDITIONAL SAFETY & ETHICAL USE DISCLAIMER:
This software was developed strictly as an undergraduate academic prototype for social skills coaching and scaffolding. It incorporates an experimental machine learning safety classifier . 

1. NOT A CLINICAL TOOL: This chatbot is NOT a diagnostic tool, a crisis helpline, a therapy platform, or a replacement for professional medical/psychological intervention .
2. RISK OF FALSE NEGATIVES: The safety gating mechanisms are probabilistic and do not guarantee a 100% block rate on unsafe or self-harm content. 
3. NO LIABILITY: Under no circumstances shall the author, supervisor, co-supervisor, or the University of Malta be held liable for any real-world distress, harm, or consequences resulting from omissions, system hallucinations, or failure of the moderation pipeline.
---

### Github
The full pipeline can be view on [Github](https://github.com/liamjvella23/ICT3909-social-skills-ai-chatbot).