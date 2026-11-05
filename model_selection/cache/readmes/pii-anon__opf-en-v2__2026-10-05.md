---
license: apache-2.0
library_name: privacy-filter
---

# opf-en-v2

Fine-tuned OpenAI Privacy Filter (OPF) checkpoint for EN PII detection.

Released anonymously alongside an ACSAC 2026 submission. See the paired
code repository for label space, training data construction, evaluation
harness, and reproducibility instructions.

## Loading

```python
from opf import PrivacyFilter
pf = PrivacyFilter.from_pretrained("pii-anon/opf-en-v2")
```
