---
tags:
- text-classification
- sentiment-analysis
- distilbert
- sst2
- glue
library_name: transformers
---

# SST-2 Sentiment Classifier (DistilBERT, fine-tuned)

`distilbert-base-uncased` fine-tuned on GLUE SST-2 (full ~67k train set),
3 epochs, lr 2e-5.

## Validation metrics
```
{
  "eval_loss": 0.5542670488357544,
  "eval_accuracy": 0.9002293577981652,
  "eval_f1": 0.9027932960893855,
  "eval_runtime": 0.9298,
  "eval_samples_per_second": 937.86,
  "eval_steps_per_second": 15.057,
  "epoch": 3.0
}
```

## Files
- `config.json`, `pytorch_model.bin` / `model.safetensors` — full model
  config and weights (all layers including biases)
- tokenizer files (`vocab.txt`, `tokenizer_config.json`, etc.)
- `metrics.json` — validation accuracy/F1 from training

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tok = AutoTokenizer.from_pretrained("Khalyie/sst2-distilbert")
model = AutoModelForSequenceClassification.from_pretrained("Khalyie/sst2-distilbert")
```

See `predict_and_visualize_sst2.py` in the companion dataset repo
(`Khalyie/sst2-distilbert-data`) for a ready-to-run evaluation + visualization script.

Note: GLUE's official SST-2 `test` split ships with labels withheld
(`label == -1`); reported metrics above are on the labeled `validation`
split.
