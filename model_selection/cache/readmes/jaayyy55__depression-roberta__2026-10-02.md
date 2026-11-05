---
license: mit
---
# Depression Detection Model (Chinese RoBERTa)

This model is fine-tuned for depression risk classification based on Chinese text input.

## Model Architecture
- Base: uer/chinese_roberta_L-8_H-256
- Custom classifier:
  - Linear → ReLU → Dropout → Linear
- Output: Binary classification (depression / non-depression)

## Training Details
- 5-fold cross validation
- Best fold model selected for deployment
- Threshold calibration applied

## Usage

```python
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file

model_path = hf_hub_download(
    repo_id="jaayyy55/depression-roberta",
    filename="model.safetensors"
)

This model is for research purposes only and should not be used for clinical diagnosis.