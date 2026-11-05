# Clinical ModernBERT for ICD Coding

Automated ICD-9/10 code prediction from clinical discharge summaries using Clinical ModernBERT with label-wise attention mechanism. This model is designed for multi-label classification of the 200 most frequent ICD codes from long clinical notes (up to 4096 tokens).

## Model Details

| Property | Value |
|----------|-------|
| Base Model | Simonlee711/Clinical_ModernBERT |
| Architecture | Label-wise Attention + Multi-label Classifier |
| Number of Labels | 200 (most common ICD-9/10 codes) |
| Max Context Length | 4096 tokens |
| Dataset | MIMIC-III Clinical Notes |
| Task | Multi-label Text Classification |
| Language | English (Clinical) |

## Dataset Split

| Split | Samples |
|-------|---------|
| Train | 78,264 |
| Validation | 19,566 |
| Test | 24,458 |

## Performance

| Metric | Value |
|--------|-------|
| Micro F1 | 0.437 |
| Macro F1 | 0.412 |
| Precision | 0.304 |
| Recall | 0.780 |
| Recall@20 | 0.758 |

The high recall (0.780) makes this model suitable for clinical decision support where missing a code is more costly than over-predicting.

## Usage

> ⚠️ **Important:** Before using `AutoModel.from_pretrained()`, you must download and import `model.py` to register the custom architecture with transformers.

### Step 1: Download and import model.py

```python
import sys
from huggingface_hub import hf_hub_download
import importlib.util

# Download model.py from the repository
path = hf_hub_download(repo_id="nikhil061307/clinical-modernbert-icd-200", filename="model.py")

# Load it as a module
spec = importlib.util.spec_from_file_location("custom_model", path)
custom_model = importlib.util.module_from_spec(spec)
sys.modules["custom_model"] = custom_model  # Register to avoid transformers internal errors
spec.loader.exec_module(custom_model)
```

### Step 2: Use with AutoModel

```python
import pickle
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("nikhil061307/clinical-modernbert-icd-200")
tokenizer = AutoTokenizer.from_pretrained("Simonlee711/Clinical_ModernBERT")

# Download ICD codes mapping
codes_path = hf_hub_download(repo_id="nikhil061307/clinical-modernbert-icd-200", filename="top_codes.pkl")
with open(codes_path, "rb") as f:
    icd_codes = pickle.load(f)

# Inference
text = "Patient with chest pain and shortness of breath"
enc = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
out = model(**enc)

probs = torch.sigmoid(out["logits"]).squeeze()
top_k = torch.topk(probs, 5)
print("Top 5 predictions:")
for idx, prob in zip(top_k.indices, top_k.values):
    print(f"  ICD code {icd_codes[idx.item()]}: {prob.item():.4f}")
```

### Complete Example

```python
import sys
import pickle
import torch
from huggingface_hub import hf_hub_download
import importlib.util

# Step 1: Download and register custom model
path = hf_hub_download(repo_id="nikhil061307/clinical-modernbert-icd-200", filename="model.py")
spec = importlib.util.spec_from_file_location("custom_model", path)
custom_model = importlib.util.module_from_spec(spec)
sys.modules["custom_model"] = custom_model
spec.loader.exec_module(custom_model)

# Step 2: Load with AutoModel
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("nikhil061307/clinical-modernbert-icd-200")
tokenizer = AutoTokenizer.from_pretrained("Simonlee711/Clinical_ModernBERT")

# Step 3: Download ICD codes mapping
codes_path = hf_hub_download(repo_id="nikhil061307/clinical-modernbert-icd-200", filename="top_codes.pkl")
with open(codes_path, "rb") as f:
    icd_codes = pickle.load(f)

# Step 4: Predict
text = "Patient with chest pain and shortness of breath"
enc = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
out = model(**enc)

probs = torch.sigmoid(out["logits"]).squeeze()
top_k = torch.topk(probs, 5)
print("Top 5 predictions:")
for idx, prob in zip(top_k.indices, top_k.values):
    print(f"  ICD code {icd_codes[idx.item()]}: {prob.item():.4f}")
```

## Architecture

```
Clinical Discharge Summary (up to 4096 tokens)
         │
         ▼
Clinical ModernBERT Encoder
         │
         ▼
Label-wise Attention Pooling  ←  200 label query vectors
         │
         ▼
Per-label Classification Heads
         │
         ▼
Sigmoid Activation → ICD Code Predictions
```

The label-wise attention mechanism allows each ICD code to attend to the most relevant parts of the clinical note, improving multi-label performance on long documents.

## Limitations & Intended Use

- **Intended Use**: Research, clinical decision support assistance, and NLP benchmarking
- **Not Intended For**: Autonomous clinical coding without human oversight
- **Data Source**: Trained on MIMIC-III (de-identified US ICU data). Performance may vary on notes from different institutions, EHR systems, or non-ICU settings
- **Bias**: May reflect coding patterns specific to MIMIC-III's patient population and clinical conventions

## Requirements

```
pip install torch transformers
```

## Citation

If you use this model in your research, please cite:

```
@article{nikhilkumar2026clinical,
  title     = {Clinical ModernBERT for Long-Context ICD Coding},
  author    = {Nikhil kumar},
  year      = {2026},
  url       = {https://huggingface.co/nikhil061307/clinical-modernbert-icd-200}
}
```

## Related Work

- [Clinical ModernBERT Base](https://huggingface.co/Simonlee711/Clinical_ModernBERT)
- [MIMIC-III Dataset](https://physionet.org/content/mimiciii/1.4/)
- [ModernBERT Paper](https://arxiv.org/abs/2412.13664)
