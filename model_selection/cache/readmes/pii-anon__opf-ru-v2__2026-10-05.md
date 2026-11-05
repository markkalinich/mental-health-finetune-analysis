---
license: apache-2.0
library_name: privacy-filter
---

# opf-ru-v2

Fine-tuned OpenAI Privacy Filter (OPF) checkpoint for RU PII detection.

Released anonymously alongside an ACSAC 2026 submission. See the paired
code repository for label space, training data construction, evaluation
harness, and reproducibility instructions.

## Loading

```python
from opf import PrivacyFilter
pf = PrivacyFilter.from_pretrained("pii-anon/opf-ru-v2")
```
