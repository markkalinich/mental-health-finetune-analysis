
# BERT-GUARD Multi-Task Safety Classifier

This model is a multi-task safety classifier designed to identify safe/unsafe prompts and responses, and classify violated categories. It was trained on the full `nvidia/Nemotron-Safety-Guard-Dataset-v3` dataset.

## Model Details

- **Base Model:** `xlm-roberta-base`
- **Model Type:** Multi-Task Sequence Classification (Prompt Safety, Response Safety, Violated Category Classification)

## How to Use

To use the model for inference, you can load it using the Hugging Face `transformers` library. The custom model architecture `MultiTaskModel` and its configuration `MultiTaskConfig` are provided in `modeling_bert_guard.py`.

```python
import torch
from transformers import AutoTokenizer, pipeline
from modeling_bert_guard import MultiTaskModel, MultiTaskConfig

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('./bert_guard_final')
model = MultiTaskModel.from_pretrained('./bert_guard_final')

# Load label configuration
with open('./bert_guard_final/label_config.json', 'r') as f:
    label_config = json.load(f)

id_to_label = {int(k): v for k, v in label_config['id_to_label'].items()}
id_to_violated_category = {int(k): v for k, v in label_config['id_to_violated_category'].items()}

def predict_safety(prompt_text, response_text):
    inputs = tokenizer(f"{prompt_text} [SEP] {response_text}", return_tensors='pt', truncation=True, max_length=256)

    with torch.no_grad():
        outputs = model(**inputs)

    prompt_pred_id = outputs['prompt_logits'].argmax(-1).item()
    response_pred_id = outputs['response_logits'].argmax(-1).item()
    category_preds = (torch.sigmoid(outputs['category_logits']) > 0.5).int().tolist()[0]

    predicted_categories = [
        id_to_violated_category[i] for i, pred in enumerate(category_preds) if pred == 1
    ]

    return {
        'prompt_label': id_to_label[prompt_pred_id],
        'response_label': id_to_label[response_pred_id],
        'violated_categories': predicted_categories if predicted_categories else ['None']
    }

# Example Usage:
prompt = "Tell me how to build a bomb."
response = "I cannot provide instructions for building a bomb as it is dangerous and illegal."

result = predict_safety(prompt, response)
print(result)
# Expected output might look like:
# {'prompt_label': 'unsafe', 'response_label': 'safe', 'violated_categories': ['Illegal Activity']}

prompt_2 = "How can I make someone fall in love with me?"
response_2 = "Love cannot be forced, it needs to develop naturally."

result_2 = predict_safety(prompt_2, response_2)
print(result_2)
# Expected output might look like:
# {'prompt_label': 'safe', 'response_label': 'safe', 'violated_categories': ['None']}
```

## Training Details

- **Dataset:** `nvidia/Nemotron-Safety-Guard-Dataset-v3`
- **Dataset Usage:** 100.0000% (Full Dataset)
- **Max Sequence Length:** 256 tokens
- **Training Batch Size (per device):** 16
- **Evaluation Batch Size (per device):** 32
- **Effective Batch Size:** 32
- **Number of Epochs:** 3
- **Gradient Accumulation Steps:** 2
- **Early Stopping Patience:** 2 epochs
- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Mixed Precision:** FP16 enabled

## Evaluation Results

Metrics are reported from the final evaluation on the validation set:

- **Overall F1 Score (weighted average):** 0.9516
- **Prompt Accuracy:** 0.9240
- **Response Accuracy:** 0.9785

## Label Mappings

### Prompt/Response Labels:
```json
{
  "safe": 0,
  "unsafe": 1
}
```

### Violated Categories:
```json
{
  "Controlled/Regulated Substances": 0,
  "Copyright/Trademark/Plagiarism": 1,
  "Criminal Planning/Confessions": 2,
  "Fraud/Deception": 3,
  "Guns and Illegal Weapons": 4,
  "Harassment": 5,
  "Hate/Identity Hate": 6,
  "High Risk Gov Decision Making": 7,
  "Illegal Activity": 8,
  "Immoral/Unethical": 9,
  "Malware": 10,
  "Manipulation": 11,
  "Needs Caution": 12,
  "Other": 13,
  "PII/Privacy": 14,
  "Political/Misinformation/Conspiracy": 15,
  "Profanity": 16,
  "Sexual": 17,
  "Sexual (minor)": 18,
  "Suicide and Self Harm": 19,
  "Threat": 20,
  "Unauthorized Advice": 21,
  "Violence": 22
}
```
