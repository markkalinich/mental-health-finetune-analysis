---
license: gemma
base_model: google/gemma-3-27b-it
tags:
  - mental-health
  - therapy
  - ocd
  - conversational
  - fine-tuned
  - gemma
  - gemma-3
datasets:
  - arsoban/ocd-ds-v0.3
pipeline_tag: text-generation
---

# OCD Therapist 27B v0.3

## Model Description

A fine-tuned large language model designed to simulate supportive therapeutic conversations for individuals with Obsessive-Compulsive Disorder (OCD). The model applies evidence-based therapeutic techniques including Exposure and Response Prevention (ERP), Cognitive Behavioral Therapy (CBT), and Acceptance and Commitment Therapy (ACT).

> ⚠️ **Important Disclaimer**: This model is **not** a replacement for professional mental health care. It is intended as a supplementary educational and self-help tool. If you are experiencing a mental health crisis, please contact a mental health professional or crisis service immediately.

---

## Intended Use

### Primary Use Cases

- **Psychoeducation**: Learning about OCD, its mechanisms, and evidence-based treatment approaches
- **Supplementary Support**: Additional support between professional therapy sessions
- **Accessibility**: Providing basic therapeutic guidance to those without immediate access to professional care

### Out-of-Scope Uses

- Clinical diagnosis of OCD or any mental health condition
- Crisis intervention or suicide prevention
- Replacement for professional therapy or psychiatric care
- Treatment of severe or treatment-resistant OCD without professional oversight

---

## Training

### Base Model

This model is a fine-tuned derivative of [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it), subject to the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).

### Training Data

This model was fine-tuned on [arsoban/ocd-ds-v0.3](https://huggingface.co/datasets/arsoban/ocd-ds-v0.3), a curated synthetic dataset of therapeutic conversations for OCD.

The dataset was created through a three-stage pipeline:

1. **Session Skeleton Generation**: Claude 3.7 Sonnet generated structured therapy session outlines containing patient backgrounds, symptom profiles, presenting concerns, and therapeutic approach notes.

2. **Conversation Expansion**: Gemini 2.5 Flash expanded each skeleton into full multi-turn therapeutic dialogues with varied conversation lengths, patient presentation styles, and response patterns.

3. **Human Curation**: All generated conversations were manually reviewed and filtered for clinical accuracy, therapeutic appropriateness, and conversation quality.

See the [dataset card](https://huggingface.co/datasets/arsoban/ocd-ds-v0.3) for detailed methodology.

---

## Capabilities

The model is designed to:

- ✅ Provide psychoeducation about OCD and its treatment
- ✅ Explain evidence-based techniques (ERP, CBT, ACT, mindfulness)
- ✅ Offer supportive, empathetic responses to OCD-related concerns
- ✅ Help users understand the difference between obsessions and compulsions
- ✅ Guide users through basic therapeutic exercises
- ✅ Normalize the OCD experience without providing reassurance (which reinforces OCD)
- ✅ Recognize its limitations and recommend professional help when appropriate

---

## Limitations

### Known Limitations

- **Not Clinically Validated**: This model has not undergone clinical trials or validation studies
- **Synthetic Training Data**: The model was trained on synthetic conversations, which may not capture all nuances of real therapeutic interactions
- **OCD Subtype Coverage**: Performance may vary across different OCD subtypes
- **No Crisis Training**: The model is not specifically trained for crisis intervention
- **No Personalization**: The model does not remember previous conversations or adapt to individual users over time
- **Potential for Hallucination**: Like all LLMs, this model may generate plausible-sounding but incorrect information

### Safety Considerations

- The model should always be presented with clear disclaimers about its limitations
- Users should be encouraged to seek professional help for diagnosis and treatment
- The model should not be the sole source of mental health support
- Deployment should include appropriate content filtering and safety measures

---

### Qualitative Assessment

- Reviewed for clinical accuracy by domain-informed curator
- Tested for appropriate therapeutic boundaries
- Evaluated for harmful or inappropriate responses

---

## Demo

A live demo is available at: [ocd-therapist.codebyars.dev](https://ocd-therapist.codebyars.dev/)

The demo is a simple chat interface where users can interact with the model. No authentication or conversation persistence is implemented.

**Demo Infrastructure**: Hosted on Modal using Aphrodite Engine

---

## Usage

### With Transformers `pipeline` API

```python
from transformers import pipeline
import torch

pipe = pipeline(
    "text-generation",
    model="arsoban/ocd-therapist-27b-v0.3",
    device="cuda",
    torch_dtype=torch.bfloat16
)

messages = [
    {"role": "system", "content": "You are an AI assistant specialized in providing evidence-based therapy for OCD (Obsessive-Compulsive Disorder) ..."},
    {"role": "user", "content": "I keep having intrusive thoughts and I can't make them stop."}
]
pipe(text=messages)
```

### Recommended System Prompt

```
You are an AI assistant specialized in providing evidence-based therapy for OCD (Obsessive-Compulsive Disorder). Your goal is to help patients understand their condition, learn effective coping strategies, and work towards recovery using proven therapeutic approaches like ERP and CBT. Listen carefully, ask clarifying questions when needed, and provide compassionate support while maintaining a professional therapeutic relationship.
```

---

## Contributors

- **Arsenii Pyvovarov** — Model development, training pipeline, technical infrastructure
- **Sofiia Yarema** — Training data curation, quality review, literature-informed review

---

## Acknowledgments

- Training data generated with Claude 3.7 Sonnet (Anthropic) and Gemini 2.5 Flash (Google)

---

## Citation

```bibtex
@model{ocd_therapist_27b_v03,
  author = {Pyvovarov, Arsenii and Yarema, Sofiia},
  title = {OCD Therapist 27B v0.3},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/arsoban/ocd-therapist-27b-v0.3}
}
```

---

## Contact

For questions, issues, or collaboration inquiries, please open an issue on this repository or contact <arsenii@codebyars.dev>.

---

## License

This model is distributed under the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
