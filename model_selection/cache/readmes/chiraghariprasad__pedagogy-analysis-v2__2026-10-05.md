---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- aspect-based-sentiment-analysis
- education
- student-feedback
- teacher-evaluation
- pedagogy
---

# Pedagogy Analysis V2

## Overview

Pedagogy Analysis V2 is a transformer-based model fine-tuned for analyzing student feedback about teachers, teaching methods, course delivery, classroom engagement, assessment practices, and overall learning experiences.

The model is designed to support educational analytics workflows by extracting sentiment and pedagogical insights from free-form student comments.

## Intended Use

This model is intended for:

* Student course evaluations
* Teacher feedback analysis
* Educational quality monitoring
* Aspect-based sentiment analysis
* Institutional reporting and analytics

Example inputs:

```text
The instructor explained difficult concepts clearly but moved too quickly through the practical examples.
```

```text
Assignments were useful, although feedback on submissions was often delayed.
```

## Model Details

| Property   | Value                          |
| ---------- | ------------------------------ |
| Model Name | Pedagogy Analysis V2           |
| Framework  | Transformers                   |
| Format     | SafeTensors                    |
| Language   | English                        |
| Task       | Educational sentiment analysis |

## Training Data

The model was fine-tuned on a custom educational feedback dataset focused on:

* Teaching effectiveness
* Course organization
* Assessment quality
* Classroom engagement
* Communication
* Learning support

## Limitations

The model may:

* Misinterpret highly ambiguous comments
* Struggle with domain-specific slang
* Produce lower accuracy on feedback substantially different from the training data
* Require human review for high-stakes evaluation decisions

The model should be used as a decision-support tool and not as the sole basis for personnel or academic decisions.

## Usage

```python
from transformers import AutoTokenizer, AutoModel

model_id = "chiraghariprasad/pedagogy-analysis-v2"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id)
```

## Citation

If you use this model in research or production systems, please cite the repository:

```text
Chirag Hariprasad. Pedagogy Analysis V2.
https://huggingface.co/chiraghariprasad/pedagogy-analysis-v2
```

---