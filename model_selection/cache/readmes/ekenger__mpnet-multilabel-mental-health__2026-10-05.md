---
tags:
- mental-health
- classification
- mpnet
- psychology
---

# 🧠 AI Mental Health Guard (MPNet Smart)

This model is a fine-tuned version of `microsoft/mpnet-base` specialized in detecting mental health statuses.

## Capabilities
It can classify text into three categories:
1. **Depression**
2. **Anxiety**
3. **Suicide Risk** (High Recall)

## Special Training
Unlike standard models, this model underwent **Adversarial Training** to distinguish between:
- Clinical Depression vs. Sadness over TV Shows/Movies
- Suicide Ideation vs. Metaphorical speech (e.g., "dying of laughter")
- Real Anger vs. Gaming rage

## Performance
- **F1 Macro:** ~0.79
- **Accuracy on Trick Cases:** 100% (in tests)