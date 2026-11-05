---
license: apache-2.0
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- modernbert
- dissatisfaction
- user-feedback
- conversational-ai
- semantic-routing
- sentiment
base_model: answerdotai/ModernBERT-base
datasets:
- rootfs/user-satisfaction-dataset
metrics:
- accuracy
- f1
---

# User Satisfaction Classifier

A ModernBERT-based classifier that detects user satisfaction and dissatisfaction reasons from follow-up messages in conversational AI systems.

## Key Insight

**Follow-up messages alone contain sufficient signal for classification.** No conversation context needed—just pass the user's response directly.

## Labels

| Label | Description | Example |
|-------|-------------|---------|
| `SAT` | User is satisfied | "Thanks!", "Perfect", "Great!" |
| `NEED_CLARIFICATION` | User needs more explanation | "What do you mean?", "Can you explain?" |
| `WRONG_ANSWER` | System provided incorrect information | "No, that's wrong", "That's not right" |
| `WANT_DIFFERENT` | User wants alternative options | "Show me others", "What else?" |

## License

Apache 2.0
