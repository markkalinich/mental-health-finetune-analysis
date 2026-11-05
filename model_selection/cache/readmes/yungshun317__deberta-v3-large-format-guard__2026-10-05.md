# DeBERTaV3-Large Reward Model — format-guard (ckpt-90)

- Base: `microsoft/deberta-v3-large`
- Init RM: `yungshun317/deberta-v3-large-ultrafeedback-rm`
- This checkpoint adds light anti-format-spam tuning.

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tok = AutoTokenizer.from_pretrained("yungshun317/deberta-v3-large-format-guard")
rm  = AutoModelForSequenceClassification.from_pretrained("yungshun317/deberta-v3-large-format-guard")
```
