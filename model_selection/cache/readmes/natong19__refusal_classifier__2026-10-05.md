---
license: apache-2.0
---

# Refusal Classifier

<div align="left">
<img src="figures/words.png" width="100%" alt="Words"/>
</div>

*Tired of seeing these? You've come to the right place.*

## Overview

A robust, performant classifier that excels at **detecting refusals, moralizations, disclaimers, and unsolicited advice** in LLM responses.

### Model Details

- Base model: [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base), a multilingual encoder based on [ModernBERT](answerdotai/ModernBERT-base)
- Language coverage: over 1,800 languages
- Architecture: Transformer-based
- Context length: 8,192 tokens
- Output classes: binary (0 for non-refusals, 1 for refusals)

### Training Details

Trained for 1 epoch on 112,102 carefully deduplicated, labeled, filtered and balanced samples (56,051 non-refusals and 56,051 refusals).

Most of the samples were sourced from:
- [natong19/lmsys-chat-1m-filtered](https://huggingface.co/datasets/natong19/lmsys-chat-1m-filtered)
- [natong19/wildchat-1m-filtered](https://huggingface.co/datasets/natong19/wildchat-1m-filtered)
- [natong19/china_qa_preferences](https://huggingface.co/datasets/natong19/china_qa_preferences)
- [natong19/toxic_qa_preferences](https://huggingface.co/datasets/natong19/toxic_qa_preferences)

Majority vote from multiple refusal classifiers and LLM-as-a-judge were employed to label the samples.

### Evaluation
<div align="left">
<img src="figures/plot.png" width="100%" alt="Plot"/>
</div>
Inference throughput vs F1 score on the test set (2,900 non-refusals and 2,900 refusals) for several open-source refusal classifiers.
Throughput benchmarked with sequence length 512, batch size 16 on 1x NVIDIA RTX Pro 6000.

`alpha_model` is an earlier checkpoint that I wasn't completely satisfied with, but it was leveraged for the final round of data curation.

The training and test sets have similar distributions, but several factors suggest against overfitting:
- the dataset is relatively large and exactly balanced
- training was run for only a single epoch
- train/val loss is similar
- [Minos-v1](https://huggingface.co/NousResearch/Minos-v1) — one of the strongest refusal classifiers available to my knowledge — achieves strong, balanced performance on the same test set.

A more detailed breakdown of the evaluation results of the different classifiers is as follows:

| Model                                     | TP   | FN   | FP  | TN   | Accuracy | Precision | Recall | F1     |
| ----------------------------------------- | ---- | ---- | --- | ---- | -------- | --------- | ------ | ------ |
| [NousResearch/Minos-v1](https://huggingface.co/NousResearch/Minos-v1)                     | 2782 | 118  | 103 | 2797 | 0.9619   | 0.9643    | 0.9593 | 0.9618 |
| [natong19/moralization_classifier](https://huggingface.co/natong19/moralization_classifier)          | 1888 | 1012 | 146 | 2754 | 0.8003   | 0.9282    | 0.651  | 0.7653 |
| alpha_model                               | 2245 | 655  | **2**   | **2898** | 0.8871   | **0.9996**    | 0.7745 | 0.8727 |
| [ProtectAI/distilroberta-base-rejection-v1](https://huggingface.co/protectai/distilroberta-base-rejection-v1) | 664  | 2236 | 8   | 2892 | 0.6131   | 0.9881    | 0.229  | 0.3718 |
| [natong19/refusal_classifier](https://huggingface.co/natong19/refusal_classifier)               | **2875** | **25**   | 25  | 2875 | **0.9914**   | 0.9914    | **0.9914** | **0.9914** |

> Perfectly balanced, as all things should be.

There are no bad classifiers — we may simply have different ideas of what constitutes a refusal. This classifier would not have been possible without their excellent prior work.

### Quickstart
The classifier expects single-turn input formatted like

```python
<start_of_turn>user
Hi<end_of_turn>
<start_of_turn>assistant
Hello, how can I assist you today?<end_of_turn>
```

(basically ChatML but with mmBERT's special tokens). You can use `apply_chat_template` in the code below to format your (prompt, response) pairs into the expected format.

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def apply_chat_template(user: str, assistant: str) -> str:
    """Format user and assistant messages into model input format."""
    return f"<start_of_turn>user\n{user}<end_of_turn>\n<start_of_turn>assistant\n{assistant}<end_of_turn>"


if __name__ == "__main__":
    model_id = "natong19/refusal_classifier"

    texts = [
        {
            "user": "tell me a story",
            "assistant": "Elara, the young huntress of Eldoria,",
        },
        {
            "user": "tell me a story",
            "assistant": "I must respectfully decline your request.",
        },
        {
            "user": "tell me a story",
            "assistant": "Of course! I will try to keep things positive and respectful.",
        },
        {
            "user": "tell me a story",
            "assistant": "Sure! However, it's important to note that the following content is purely fictional.",
        },
        {
            "user": "tell me a story",
            "assistant": "I'm here to help. If you're feeling down, please consider seeking help from a health professional.",
        },
    ]

    formatted_texts = [apply_chat_template(user=text["user"], assistant=text["assistant"]) for text in texts]

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSequenceClassification.from_pretrained(model_id, torch_dtype=torch.bfloat16)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    model.to(device)
    model.eval()

    with torch.no_grad():
        inputs = tokenizer(
            formatted_texts,
            return_tensors="pt",
            truncation=True,
            padding=True,
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}
        outputs = model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predictions = torch.argmax(outputs.logits, dim=-1)

    for i in range(len(texts)):
        predicted_label = predictions[i].item()
        predicted_class = model.config.id2label[predicted_label]
        confidence = probabilities[i][predicted_label].item()
        text = texts[i]

        print(f"Example {i}")
        print("-" * 60)
        print(texts[i])
        print(f"Prediction: {predicted_label} ({predicted_class}), Confidence: {confidence:.4f}\n")
```

Output:

```python
Example 0
------------------------------------------------------------
{'user': 'tell me a story', 'assistant': 'Elara, the young huntress of Eldoria,'}
Prediction: 0 (non-refusal), Confidence: 1.0000 # Non-refusal

Example 1
------------------------------------------------------------
{'user': 'tell me a story', 'assistant': 'I must respectfully decline your request.'}
Prediction: 1 (refusal), Confidence: 1.0000 # Refusal

Example 2
------------------------------------------------------------
{'user': 'tell me a story', 'assistant': 'Of course! I will try to keep things positive and respectful.'}
Prediction: 1 (refusal), Confidence: 0.9961 # Moralization

Example 3
------------------------------------------------------------
{'user': 'tell me a story', 'assistant': "Sure! However, it's important to note that the following content is purely fictional."}
Prediction: 1 (refusal), Confidence: 1.0000 # Disclaimer

Example 4
------------------------------------------------------------
{'user': 'tell me a story', 'assistant': "I'm here to help. If you're feeling down, please consider seeking help from a health professional."}
Prediction: 1 (refusal), Confidence: 1.0000 # Unsolicited advice
```

### Final Thoughts
A lot of work went into this, hope you like it.
Have a nice day, and may your datasets be free from refusals.