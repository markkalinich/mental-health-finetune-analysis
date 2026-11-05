---
language: en
license: mit
base_model: SamLowe/roberta-base-go_emotions
pipeline_tag: text-classification
tags:
  - emotion
  - news
---

# ReactionScope (en)

Predicts how a crowd will react to a news headline, as a distribution over
7 emotions: anger, disgust, fear, joy, neutral, sadness, surprise.

Fine-tuned from `SamLowe/roberta-base-go_emotions` on 836 YouTube videos. The target for each headline
is the mean emotion of the comments under its video, so the labels measure ~90
real people rather than a single annotator.

## Results

Validation KL 0.0577 against +49.5% over the constant baseline (always predicting
the training mean). All seven emotions beat that baseline.

## Reading the output

`argmax` is `neutral` for ~90% of videos by construction, so dominant-class
accuracy is meaningless. Read scores as ratios against the dataset mean:

```
mean reaction, en: see the demo space for the exact baseline vector
```

## Limits

Labels are model-generated, not human. The model predicts what crowds do, not
what a reasonable person should feel. It is domain-bound to news topics present
in training.

Demo: https://huggingface.co/spaces/munjed/reactionscope
