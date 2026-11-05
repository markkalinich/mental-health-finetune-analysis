---
library_name: transformers
base_model: distilbert-base-uncased
datasets:
- nyasaluharuka/catrace-v0.2-development
pipeline_tag: text-classification
language:
- en
tags:
- catrace
- anxiety
- stress
- feasibility
- text-classification
- synthetic-data
---

# CatRace DistilBERT Feasibility Model

This is a development version of a DistilBERT classifier trained on
CatRace v0.2.

## Task

The model receives:

- A fictional mental-health or stress-related situation
- Explicit practical constraints
- A proposed micro-action

It predicts one of three classes:

- `clearly_feasible`
- `subtly_infeasible`
- `clearly_infeasible`

## Training dataset

`nyasaluharuka/catrace-v0.2-development`

The dataset is synthetic and rule-labeled. It is intended for development
and experimentation rather than clinical use.

## Intended use

This model may be used to:

- Rank proposed well-being micro-actions
- Detect impractical recommendations
- Test constraint-sensitive classification
- Support an experimental action-planning chatbot

## Limitations

- Not clinically validated
- Not a diagnostic model
- Not a crisis-detection model
- Trained primarily on synthetic English examples
- Should not replace professional care or human judgment
- Feasibility does not guarantee that an action will be personally helpful

## Safety

Crisis detection and routing must be implemented separately from this model.
