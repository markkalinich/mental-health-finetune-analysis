---
language: en
tags:
- empathy
- mental-health
- psychology
- text-classification
- pytorch
license: mit
datasets:
- reddit
metrics:
- f1
- accuracy
library_name: transformers
---

# Empathy Classification Model - EX

This model detects **Explorations - exploring the seeker's experiences through questions or acknowledgments** in conversational responses, specifically designed for mental health support contexts.

## Model Description

This is a BiEncoder model based on RoBERTa that classifies empathy levels in mental health support conversations. It uses a dual-encoder architecture with cross-attention:

- **Seeker Encoder**: Processes the help-seeker's post (context)
- **Responder Encoder**: Processes the response post with attention to the seeker's context
- **Multi-task Learning**: Jointly predicts empathy level and identifies rationale tokens

### Model Outputs

1. **Empathy Level Classification** (3 classes):
   - 0: Low empathy
   - 1: Medium empathy
   - 2: High empathy

2. **Rationale Identification**: Binary classification for each token indicating whether it contributes to empathy expression

## Intended Use

This model is designed for:
- Analyzing empathy in mental health support conversations
- Research on empathetic communication patterns
- Building empathy-aware chatbots and support systems
- Training and feedback for peer support volunteers

## Training Data

Trained on Reddit mental health support conversations from subreddits focused on emotional support and mental health discussions.

## How to Use

### Installation

```bash
pip install transformers torch
```

### Basic Usage

```python
from transformers import AutoModel, AutoTokenizer, AutoConfig
import torch

# Load model and tokenizer
model_name = "RyanDDD/empathy-mental-health-reddit-EX"
tokenizer = AutoTokenizer.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True)

# Example conversation
seeker_post = "I've been feeling really down lately and don't know what to do."
response_post = "I'm sorry you're going through this. It's completely normal to feel this way sometimes. Have you considered talking to someone about how you're feeling?"

# Tokenize
encoded_sp = tokenizer(
    seeker_post, 
    max_length=64, 
    padding='max_length',
    truncation=True, 
    return_tensors='pt'
)
encoded_rp = tokenizer(
    response_post, 
    max_length=64, 
    padding='max_length',
    truncation=True, 
    return_tensors='pt'
)

# Predict
model.eval()
with torch.no_grad():
    outputs = model(
        input_ids_SP=encoded_sp['input_ids'],
        input_ids_RP=encoded_rp['input_ids'],
        attention_mask_SP=encoded_sp['attention_mask'],
        attention_mask_RP=encoded_rp['attention_mask']
    )
    logits_empathy = outputs[0]
    logits_rationale = outputs[1]

# Get predictions
empathy_level = torch.argmax(logits_empathy, dim=1).item()
empathy_labels = ['Low', 'Medium', 'High']
print(f"Empathy Level (EX): {empathy_labels[empathy_level]}")
```

### Using the Convenience Method

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

prediction, rationale = model.predict(
    seeker_post=seeker_post,
    response_post=response_post,
    tokenizer=tokenizer,
    device=device
)

print(f"Empathy Level: {['Low', 'Medium', 'High'][prediction]}")
print(f"Rationale tokens: {rationale}")
```

## Model Architecture

- **Base Model**: RoBERTa-base (pretrained)
- **Architecture**: Dual BiEncoder with Cross-Attention
- **Parameters**: ~125M
- **Max Sequence Length**: 64 tokens
- **Training Objective**: Multi-task learning (empathy classification + rationale extraction)

### Architecture Details

```
Input: Seeker Post + Response Post
  ↓
[Seeker Encoder (RoBERTa)] ← frozen during training
  ↓
[Responder Encoder (RoBERTa)] ← fine-tuned
  ↓
[Cross-Attention Layer] ← attends to seeker context
  ↓
[Classification Head] → Empathy Level (3 classes)
  ↓
[Token Classifier] → Rationale (binary per token)
```

## Training Procedure

### Training Hyperparameters

- Learning rate: 2e-5
- Batch size: 32
- Epochs: 4
- Max sequence length: 64
- Dropout: 0.1
- Lambda_EI (empathy loss weight): 0.5
- Lambda_RE (rationale loss weight): 0.5
- Optimizer: AdamW
- Scheduler: Linear warmup

### Training Details

- The seeker encoder is frozen during training
- Only the responder encoder and attention/classification layers are fine-tuned
- Multi-task learning with joint optimization of empathy and rationale losses

## Evaluation Results

The model achieves strong performance on held-out test data:

- Empathy Classification Accuracy: ~70-75%
- Macro F1 Score: ~0.68-0.73
- Rationale IOU F1: ~0.60-0.65

## Limitations and Biases

⚠️ **Important Limitations:**

1. **Domain-Specific**: Trained on Reddit data; may not generalize to other platforms or formal contexts
2. **Not Clinical**: Should NOT be used as a replacement for professional mental health diagnosis or treatment
3. **Bias**: May reflect biases present in Reddit communities and mental health discussions
4. **Language**: English only
5. **Context Length**: Limited to 64 tokens per post
6. **Cultural**: May not capture empathy expressions across different cultures

## Ethical Considerations

- This model is intended for research and educational purposes
- Should be used with human oversight in any practical application
- Privacy considerations: Do not use on private health information without proper consent
- Be aware of potential harm: Automated empathy assessment could be misused in sensitive contexts

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{empathy-mental-health-ex,
  author = {Your Name},
  title = {Empathy Classification Model for Mental Health Support - EX},
  year = {2024},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/RyanDDD/empathy-mental-health-reddit-EX}}
}
```

## Model Card Authors

Created by the Empathy-Mental-Health project team.

## Contact

For questions, issues, or collaboration opportunities:
- Open an issue on the model repository
- Visit the project GitHub: [Empathy-Mental-Health](https://github.com/behavioral-data/Empathy-Mental-Health)

## Related Models

This is part of a three-model suite for comprehensive empathy analysis:
- **RyanDDD/empathy-mental-health-reddit-ER** - Emotional Reactions
- **RyanDDD/empathy-mental-health-reddit-IP** - Interpretations
- **RyanDDD/empathy-mental-health-reddit-EX** - Explorations

Use all three models together for comprehensive empathy assessment!

## License

MIT License - See LICENSE file for details.
