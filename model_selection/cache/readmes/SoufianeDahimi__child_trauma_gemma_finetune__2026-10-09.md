---
language:
- en
- ar
- uk
tags:
- gemma
- mental-health
- trauma-assessment
- multilingual
- fine-tuned
- unsloth
license: apache-2.0
datasets:
- custom
model-index:
- name: child_trauma_assessment_gemma
  results: []
base_model:
- google/gemma-3n-E2B-it
---

# Child Trauma Assessment Gemma - Specialized Model for Trauma Assessment

This is a fine-tuned version of Gemma 3N specifically optimized for conducting trauma assessments with children from conflict zones. The model is designed to facilitate empathetic, culturally-sensitive conversations and generate professional psychological reports.

## Model Description

- **Base Model:** Gemma 3N (unsloth/gemma-3n-E2B-it)
- **Fine-tuning Method:** LoRA (r=16, alpha=16)
- **Training Focus:** Specialized for trauma assessment conversations and report generation
- **Languages:** Multilingual support (Arabic dialects, Ukrainian, English)
- **Context Length:** 2048 tokens

### Training Details

- **Dataset and Training Script:**
  Details about training script and datast curation can be found here: https://github.com/Dahimi/Gemma3n_Finetune_Child_Trauma
  
- **Fine-tuning Configuration:**
  - Batch Size: 1 with gradient accumulation (4 steps)
  - Learning Rate: 2e-4 with linear scheduler
  - Training Focus: Conversation responses only (loss masked on user inputs)
  - LoRA Parameters: r=16, alpha=16
  - Context Length: 2048 tokens

## Intended Uses

This model is designed for:
- Conducting initial trauma assessments with children from conflict zones
- Supporting mental health professionals and volunteers
- Generating standardized trauma assessment reports
- Facilitating multilingual mental health support

### Primary Functions

1. **Conversational Assessment:**
   - Empathetic dialogue with parents/caregivers
   - Culturally-appropriate questioning
   - Trauma indicator identification

2. **Report Generation:**
   - Structured professional assessments
   - Severity scoring (1-10 scale)
   - Risk indicator analysis
   - Cultural context documentation

## Language Support

The model supports:
- Palestinian/Levantine Arabic
- Sudanese Arabic
- Ukrainian
- English

*Note: All assessment reports are generated in professional English regardless of conversation language*

## Limitations & Biases

- This model should not replace professional mental health assessment
- Should be used as a support tool under professional supervision
- May have limitations in understanding extremely specific cultural contexts
- Not a substitute for emergency mental health intervention

## Training Data

The model was trained on a specialized dataset containing:
1. **Conversation Examples:** Multi-turn dialogues between parents and AI
2. **Report Generation Examples:** Professional assessment report templates

Data format follows Gemma's chat template with alternating roles.

## Usage

```python
from transformers import TextStreamer
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    "SoufianeDahimi/child_trauma_gemma_finetune",
    max_seq_length = 2048,
    load_in_4bit = True,
)

def generate_response(prompt):
    messages = [{
        "role": "user",
        "content": [{"type": "text", "text": prompt}]
    }]
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt = True,
        return_tensors = "pt",
        tokenize = True,
        return_dict = True,
    ).to("cuda")
    
    return model.generate(
        **inputs,
        max_new_tokens = 512,
        temperature = 0.7,
        top_p = 0.95,
        top_k = 64,
        streamer = TextStreamer(tokenizer, skip_prompt = True),
    )
```

## Output Format

The model generates two types of responses:

1. **Conversational Responses:**
   - Empathetic dialogue
   - Follow-up questions
   - Guidance and support

2. **Assessment Reports:**
   - Parent observations summary
   - Trauma indicator analysis
   - Severity scoring
   - Risk assessment
   - Cultural context notes

## Ethical Considerations

This model is designed for sensitive mental health contexts and should be used with appropriate care:
- Always use under professional supervision
- Maintain strict privacy and data protection
- Consider cultural and contextual sensitivities
- Follow ethical guidelines for mental health assessment

## Citations

If you use this model in your research or application, please cite: