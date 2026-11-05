---
license: bsd-3-clause
language:
- en
pipeline_tag: text-classification
tags:
- psychology
- cognitive distortions
widget:
- text: "We have known each other since childhood."
  example_title: "No Distortion"
- text: "I can't believe I forgot to do that, I'm such an idiot."
  example_title: "Personalization"
- text: "I feel like I'm disappointing others."
  example_title: "Emotional Reasoning"
- text: "All doctors are arrogant and don't really care about their patients."
  example_title: "Overgeneralizing"
- text: "They are too young to hear it."
  example_title: "Labeling"
- text: "She must never make any mistakes in her work."
  example_title: "Should Statements"
- text: "If I don't finish this project on time, my boss will fire me."
  example_title: "Catastrophizing"
- text: "If I keep working hard, they will eventually give me a raise."
  example_title: "Reward Fallacy"
---

# Classification of Cognitive Distortions using Bert

><span style="color:red">This article is under development. Please use the model for retraining on your data, not a "ready to use" solution.</span>

## Problem Description

**Cognitive distortion** refers to patterns of biased or distorted thinking that can lead to negative emotions, behaviors, and beliefs. These distortions are often automatic and unconscious, and can affect a person's perception of reality and their ability to make sound judgments.

Some common types of cognitive distortions include:

1. **Personalization**: Blaming oneself for things that are outside of one's control.

*Examples:*
- *She looked at me funny, she must be judging me.*
- *I can't believe I made that mistake, I'm such a screw up.*

2. **Emotional Reasoning**: Believing that feelings are facts, and letting emotions drive one's behavior.

*Examples:*
- *I feel like I'm not good enough, so I must be inadequate.*
- *They never invite me out, so they must not like me.*

3. **Overgeneralizing**: Drawing broad conclusions based on a single incident or piece of evidence.

*Examples:*
- *He never listens to me, he just talks over me.*
- *Everyone always ignores my needs.*

4. **Labeling**: Attaching negative or extreme labels to oneself or others based on specific behaviors or traits.

*Examples:*
- *I'm such a disappointment.*
- *He's a total jerk.*

5. **Should Statements**: Rigid, inflexible thinking that is based on unrealistic or unattainable expectations of oneself or others.

*Examples:*
- *I must never fail at anything.*
- *They have to always put others' needs before their own.*

6. **Catastrophizing**: Assuming the worst possible outcome in a situation and blowing it out of proportion.

*Examples:*
- *It's all going to be a waste of time, they're never going to succeed.*
- *If I don't get the promotion, my entire career is over.*

7. **Reward Fallacy**: Belief that one should be rewarded or recognized for every positive action or achievement.

*Examples:*
- *If I work hard enough, they will give me the pay raise I want.*
- *If they don't appreciate my contributions, I'll start slacking off.*

## Model Description

This is one of the smaller BERT variants, pretrained model on English language using a masked language modeling objective. BERT was introduced in [this paper](https://arxiv.org/abs/1810.04805) and first released in [this repository](https://github.com/google-research/bert).

## Data Description

[In progress]

## Using

Example of single-label classification:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("amedvedev/bert-tiny-cognitive-bias")
model = AutoModelForSequenceClassification.from_pretrained("amedvedev/bert-tiny-cognitive-bias")

inputs = tokenizer("He must never disappoint anyone.", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
model.config.id2label[predicted_class_id]
```

## Metrics

Model accuracy by labels:

|                     | Precision | Recall | F1   |
|:-------------------:|:---------:|:------:|:----:|
| No Distortion       | 0.84      | 0.74   | 0.79 |
| Personalization     | 0.86      | 0.89   | 0.87 |
| Emotional Reasoning | 0.88      | 0.96   | 0.92 |
| Overgeneralizing    | 0.80      | 0.88   | 0.84 |
| Labeling            | 0.84      | 0.80   | 0.82 |
| Should Statements   | 0.88      | 0.95   | 0.91 |
| Catastrophizing     | 0.88      | 0.86   | 0.87 |
| Reward Fallacy      | 0.87      | 0.95   | 0.91 |

Average model accuracy:

Accuracy      | Top-3 Accuracy | Top-5 Accuracy | Precision   | Recall      | F1          |
|:-----------:|:--------------:|:--------------:|:-----------:|:-----------:|:-----------:|
| 0.86 ± 0.04 | 0.99 ± 0.01    | 0.99 ± 0.01    | 0.86 ± 0.04 | 0.85 ± 0.04 | 0.85 ± 0.04 |

## References

[In progress]