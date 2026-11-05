
---
library_name: transformers
tags:
- reward-model
- bert
---
# BERT Reward Model

This model was fine-tuned on the 'Cultural Kaleidoscope' dataset to act as a Reward Model for RLHF.
It uses `bert-base-uncased` as the base.

## Important: Custom Class Required

This model uses a custom wrapper class (`BertForReward`) to fix a compatibility issue between BERT (an encoder) and the `RewardTrainer` (which expects generative model arguments like `use_cache`).

**You must define this class in your script before loading the model.**

### 1. Define the Class
Copy this code into your script:

```python
import torch
from transformers import BertForSequenceClassification

class BertForReward(BertForSequenceClassification):
    def forward(self, *args, **kwargs):
        kwargs.pop("use_cache", None)
        return super().forward(*args, **kwargs)
