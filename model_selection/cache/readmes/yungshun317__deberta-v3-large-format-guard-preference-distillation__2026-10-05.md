# DeBERTaV3-Large Reward Model — formatguard & preference distillation (ckpt-799)

- Base backbone: `microsoft/deberta-v3-large`
- Init RM: `yungshun317/deberta-v3-large-format-guard`
- This snapshot adds anti-format-spam preference tuning.

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tok = AutoTokenizer.from_pretrained("yungshun317/deberta-v3-large-format-guard-preference-distillation")
rm  = AutoModelForSequenceClassification.from_pretrained("yungshun317/deberta-v3-large-format-guard-preference-distillation")
```
