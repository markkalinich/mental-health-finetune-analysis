---
language:
- pl
license: gpl-3.0
tags:
- text-classification
- emotion-classification
- sentiment-analysis
- polish
- multi-label-classification
- twitter
datasets:
- yazoniak/TwitterEmo-PL-Refined
base_model: PKOBP/polish-roberta-8k
metrics:
- f1
- accuracy
pipeline_tag: text-classification
model-index:
  - name: twitter-emotion-pl-classifier
    results:
      - task:
          type: text-classification
          name: Multi-Label Emotion Classification
        dataset:
          type: yazoniak/TwitterEmo-PL-Refined
          name: TwitterEmo-PL-Refined
          split: validation
        metrics:
          - type: f1
            value: 0.8500
            name: F1 Macro
            verified: true
            args:
              average: macro
          - type: f1
            value: 0.8900
            name: F1 Micro
            verified: true
            args:
              average: micro
          - type: f1
            value: 0.8895
            name: F1 Weighted
            verified: true
            args:
              average: weighted
          - type: accuracy
            value: 0.5125
            name: Exact Match Accuracy
            verified: true
          - type: accuracy
            value: 0.8900
            name: Subset Accuracy
            verified: true
---

# Polish Twitter Emotion Classifier (RoBERTa-8k)

## Model Description

This model is a fine-tuned version of [PKOBP/polish-roberta-8k](https://huggingface.co/PKOBP/polish-roberta-8k) for multi-label emotion and sentiment classification in Polish. It was trained on the [TwitterEmo-PL-Refined](https://huggingface.co/datasets/yazoniak/TwitterEmo-PL-Refined) dataset.

The model predicts 8 emotion and sentiment labels simultaneously:

- **Emotions**: `radość` (joy), `wstręt` (disgust), `gniew` (anger), `przeczuwanie` (anticipation)
- **Sentiment**: `pozytywny` (positive), `negatywny` (negative), `neutralny` (neutral)
- **Special**: `sarkazm` (sarcasm)

### Model Details

- **Model type**: RoBERTa (Polish)
- **Language**: Polish
- **Base model**: [PKOBP/polish-roberta-8k](https://huggingface.co/PKOBP/polish-roberta-8k)
- **Task**: Multi-label text classification (emotion & sentiment)
- **Training data**: 35,921 Polish tweets from TwitterEmo-PL-Refined
- **License**: GPL-3.0
- **Context window**: 8,192 tokens (max; for tweet-length texts you can use a smaller tokenizer `max_length`, e.g., 256-1024)

## Intended Use

### Primary Use Cases

- **Social media monitoring**: Analyze emotions and sentiment in Polish tweets and social media posts
- **Customer feedback analysis**: Understand emotional responses in Polish customer reviews
- **Research**: Study emotion expression patterns in Polish language social media
- **Multi-label sentiment analysis**: Capture nuanced emotional states beyond binary positive/negative

### Out-of-Scope Use

- This model is specifically trained on Polish Twitter data and may not generalize well to:
  - Formal Polish text (news articles, academic writing)
  - Other languages
  - Very long documents (optimal for tweet-length texts)

## Performance

### Overall Metrics

| Metric | Score |
|--------|-------|
| **F1 Macro** | **0.8500** |
| **F1 Micro** | **0.8900** |
| **F1 Weighted** | **0.8895** |
| **Exact Match Accuracy** | **0.5125** |
| **Subset Accuracy** | **0.8900** |
| **Validation Loss** | **0.2761** |

### Per-Label Performance

| Label | F1 Score | Coverage |
|-------|----------|----------|
| **negatywny** (negative) | **0.8553** | 42.4% |
| **neutralny** (neutral) | **0.8172** | 41.0% |
| **pozytywny** (positive) | **0.7814** | 17.4% |
| **gniew** (anger) | **0.7693** | 25.8% |
| **radość** (joy) | **0.7476** | 11.9% |
| **wstręt** (disgust) | **0.7337** | 20.4% |
| **przeczuwanie** (anticipation) | **0.7220** | 21.6% |
| **sarkazm** (sarcasm) | **0.5337** | 16.0% |

## Training Details

### Training Data

The model was trained on [TwitterEmo-PL-Refined](https://huggingface.co/datasets/yazoniak/TwitterEmo-PL-Refined), which contains:

- **Total samples**: 35,921 Polish tweets
- **Label distribution**:
  - `negatywny`: 15,231 samples (42.4%)
  - `neutralny`: 14,720 samples (41.0%)
  - `gniew`: 9,252 samples (25.8%)
  - `przeczuwanie`: 7,776 samples (21.6%)
  - `wstręt`: 7,337 samples (20.4%)
  - `pozytywny`: 6,248 samples (17.4%)
  - `sarkazm`: 5,756 samples (16.0%)
  - `radość`: 4,283 samples (11.9%)

### Training Configuration

```python
Model: PKOBP/polish-roberta-8k
Training samples: 28,737 (80%)
Validation samples: 7,184 (20%)

Hyperparameters:
- Learning rate: 1e-5
- Batch size: 32 (train), 32 (eval)
- Epochs: 4
- Weight decay: 0.03
- Warmup ratio: 0.1
- Dropout rate: 0.2
- Max gradient norm: 1.0
- Optimizer: AdamW
- LR scheduler: Cosine with warmup
- Early stopping patience: 3
- Mixed precision: BF16

Training strategy:
- Save strategy: Every 200 steps
- Evaluation strategy: Every 200 steps
- Best model selection: F1 Macro
- Total training steps: 3,600
- Best checkpoint: 3,400
```

### Training Process

Training was conducted on single NVIDIA RTX 3090 GPU using a stratified 80/20 train-validation split with the following progression:

![Training Progress](training_plots.png)

## Calibration

The model's predictions can be improved using **temperature scaling** and **optimized thresholds**. Calibration analysis shows:

### Temperature Scaling Results

Per-label temperature scaling reduces calibration error (Expected Calibration Error - ECE):

| Label | Temperature | ECE Before | ECE After | Improvement |
|-------|------------|------------|-----------|-------------|
| `radość` | 1.066 | 0.0163 | 0.0166 | -1.8% |
| `wstręt` | 1.117 | 0.0211 | 0.0152 | **+27.9%** |
| `gniew` | 1.186 | 0.0308 | 0.0194 | **+37.0%** |
| `przeczuwanie` | 1.102 | 0.0228 | 0.0237 | -3.9% |
| `pozytywny` | 1.181 | 0.0280 | 0.0293 | -4.6% |
| `negatywny` | 1.437 | 0.0594 | 0.0345 | **+41.9%** |
| `neutralny` | 1.472 | 0.0696 | 0.0390 | **+44.0%** |
| `sarkazm` | 1.078 | 0.0202 | 0.0202 | 0.0% |

**Key findings:**

- `neutralny`, `negatywny`, and `gniew` benefit most from temperature scaling
- Some labels (`radość`, `przeczuwanie`, `pozytywny`) show minor degradation
- Overall, calibration significantly improves probability reliability

### Optimized Decision Thresholds

Per-label F1-optimized thresholds (vs. default 0.5):

| Label | Optimal Threshold | F1 @ Optimal | F1 @ 0.5 | Improvement |
|-------|------------------|--------------|----------|-------------|
| `neutralny` | **0.330** | **0.8211** | 0.8110 | **+1.00%** |
| `sarkazm` | **0.330** | **0.5766** | 0.5256 | **+5.10%** |
| `przeczuwanie` | 0.410 | 0.7276 | 0.7187 | +0.89% |
| `gniew` | 0.440 | 0.7692 | 0.7676 | +0.16% |
| `negatywny` | 0.450 | 0.8516 | 0.8511 | +0.05% |
| `wstręt` | 0.460 | 0.7477 | 0.7464 | +0.13% |
| `pozytywny` | 0.510 | 0.7864 | 0.7859 | +0.04% |
| `radość` | 0.560 | 0.7572 | 0.7558 | +0.14% |

**Key findings:**

- `sarkazm` shows the largest improvement (+5.10%) with a lower threshold (0.33)
- `neutralny` also benefits significantly (+1.00%) from a lower threshold (0.33)
- Most labels perform optimally near the default 0.5 threshold
- Total improvement with optimized thresholds: **~0.5-1.0% F1 Macro**

### Calibration Files

The model repository includes:

- **Base model**: `model.safetensors` - Use with default threshold (0.5)
- **Calibration artifacts**: `calibration_artifacts.json` - Contains temperature parameters and optimal thresholds

![Reliability diagrams*](calibration_reliability_diagrams.png)

**Recommendation**: For production use, apply both temperature scaling and optimized thresholds for best performance.

## Model Files

This repository contains:

- **Model weights**: `model.safetensors` - Fine-tuned RoBERTa model
- **Tokenizer**: `tokenizer.json`, `tokenizer_config.json` - Polish RoBERTa tokenizer
- **Configuration**: `config.json` - Model configuration
- **Calibration**: `calibration_artifacts.json` - Temperature scaling parameters and optimal thresholds
- **Inference scripts**:
  - `predict.py` - Basic inference (threshold: 0.5)
  - `predict_calibrated.py` - Calibrated inference (recommended)
- **Training artifacts**: `training_plots`, `calibration_reliability_diagrams`
- **Requirements**: `requirements.txt` - Python dependencies
- **License**: `LICENSE` - Full GPL-3.0 license text

### Installation

```bash
pip install -r requirements.txt
```

Or install dependencies manually:

```bash
pip install transformers torch numpy
```

## Usage

### Important: Text Preprocessing

**The model expects @mentions to be anonymized**, as they were during training. Both inference scripts automatically replace all `@username` mentions with `@anonymized_account` to match the training data distribution.

### Quick Start (Basic Inference)

Use the `predict.py` script for basic inference with default threshold (0.5):

```bash
# From Hugging Face (default) - mentions are automatically anonymized
python predict.py "Uwielbiam czekać na peronie 3 godziny! Gratulacje dla #zgp"

# Example with mentions
python predict.py "@zgp_intervillage Uwielbiam czekać na peronie 3 godziny! Gratulacje dla #zgp"
# Preprocessed internally: "@anonymized_account Uwielbiam czekać..."

# From local model
python predict.py "Uwielbiam czekać na peronie 3 godziny! Gratulacje dla #zgp" --model-path ./

# With custom threshold
python predict.py "Uwielbiam czekać na peronie 3 godziny! Gratulacje dla #zgp" --model-path ./ --threshold 0.3
```

**Example Output:**

```
Loading model from: yazoniak/twitter-emotion-pl-classifier

Input text: Uwielbiam czekać na peronie 3 godziny! Gratulacje dla #zgp

Assigned Labels:
----------------------------------------
  radość
  pozytywny
  sarkazm

All Labels (with probabilities):
----------------------------------------
✓ radość         : 0.9574
  wstręt         : 0.0566
  gniew          : 0.0516
  przeczuwanie   : 0.0347
✓ pozytywny      : 0.9782
  negatywny      : 0.0602
  neutralny      : 0.0336
✓ sarkazm        : 0.5404
```

### With Calibration

Use the `predict_calibrated.py` script for calibrated inference with temperature scaling and optimized thresholds:

```bash
# From Hugging Face with calibration (requires calibration_artifacts.json)
python predict_calibrated.py "Uwielbiam czekać na peronie 3 godziny! Gratulacje dla #zgp"
```

### Python API Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import re

def preprocess_text(text):
    """Preprocess text to match training data format."""
    # Anonymize @mentions (IMPORTANT for best performance)
    text = re.sub(r'@\w+', '@anonymized_account', text)
    return text

# Load model
model_name = "yazoniak/twitter-emotion-pl-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Get labels from model config
labels = [model.config.id2label[i] for i in range(model.config.num_labels)]

# Prepare input with preprocessing
text = "@jan_kowalski To jest wspaniały dzień!"
preprocessed_text = preprocess_text(text)  # "@anonymized_account To jest wspaniały dzień!"
inputs = tokenizer(preprocessed_text, return_tensors="pt", truncation=True, max_length=8192)

# Inference
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# Get probabilities
probabilities = torch.sigmoid(logits).squeeze().numpy()

# Apply threshold
threshold = 0.5
predictions = {
    label: float(prob) 
    for label, prob in zip(labels, probabilities) 
    if prob > threshold
}

print(predictions)
# Output: {'radość': 0.8734, 'pozytywny': 0.9156}
```

### Interpretation

The model outputs logits for each of the 8 labels. To get predictions:

1. **Without calibration**: Apply sigmoid, threshold at 0.5
1. **With calibration**:
   - Apply sigmoid
   - Apply temperature scaling (divide logits by temperature before sigmoid)
   - Apply per-label optimized thresholds

## Limitations and Biases

### Known Limitations

1. **Preprocessing required**: The model expects `@mentions` to be anonymized as `@anonymized_account` (matching training data). The provided inference scripts handle this automatically, but custom implementations must include this preprocessing step for optimal performance.

1. **Sarcasm detection**: The model struggles with Polish sarcasm (F1: 0.53), which is inherently difficult to detect in text for BERT models without additional context.

1. **Class imbalance**: Performance varies with label frequency:

   - High-frequency labels (`negatywny`, `neutralny`) perform best
   - Low-frequency labels (`radość`, `sarkazm`) show lower F1 scores

1. **Twitter-specific**: The model is optimized for tweet-length texts (up to 8,192 tokens) with informal language, hashtags, and mentions.

## Citation

If you use this model in your research or applications, please cite:

```bibtex
@model{yazoniak2025twitteremotionpl,
  title={Polish Twitter Emotion Classifier (RoBERTa-8k)},
  author={yazoniak},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/yazoniak/twitter-emotion-pl-classifier}
}
```

Also cite the base model and dataset:

```bibtex
@dataset{yazoniak_twitteremo_pl_refined_2025,
  title   = {TwitterEmo-PL-Refined: Polish Twitter Emotions (8 labels, refined)},
  author  = {yazoniak},
  year    = {2025},
  url     = {https://huggingface.co/datasets/yazoniak/TwitterEmo-PL-Refined}
}

@inproceedings{bogdanowicz2023twitteremo,
  title     = {TwitterEmo: Annotating Emotions and Sentiment in Polish Twitter},
  author    = {Bogdanowicz, S. and Cwynar, H. and Zwierzchowska, A. and Klamra, C. and Kiera{\'s}, W. and Kobyli{\'n}ski, {\L}.},
  booktitle = {Computational Science -- ICCS 2023},
  series    = {Lecture Notes in Computer Science},
  volume    = {14074},
  publisher = {Springer, Cham},
  year      = {2023},
  doi       = {10.1007/978-3-031-36021-3_20}
}
```

## Acknowledgments

- **Base model**: [PKOBP/polish-roberta-8k](https://huggingface.co/PKOBP/polish-roberta-8k)
- **Original dataset**: [CLARIN-PL TwitterEmo](https://huggingface.co/datasets/clarin-pl/twitteremo)
- **Label cleaning**: Cleanlab library for noise detection
- **LLM assistance**: Gemini-2.5-Flash and GPT-4.1 for label review

## License

### License Terms

This model is released under the **GNU General Public License v3.0 (GPL-3.0)**, inherited from the training dataset.

**License Chain:**

- **Base Model** ([PKOBP/polish-roberta-8k](https://huggingface.co/PKOBP/polish-roberta-8k)): Apache-2.0
- **Training Dataset** ([TwitterEmo-PL-Refined](https://huggingface.co/datasets/yazoniak/TwitterEmo-PL-Refined)): GPL-3.0
- **Original Dataset** ([clarin-pl/twitteremo](https://huggingface.co/datasets/clarin-pl/twitteremo)): GPL-3.0
- **This Fine-tuned Model**: **GPL-3.0** (inherited from training data)

### Full License Text

The complete GPL-3.0 license text is available in the [LICENSE](LICENSE) file in this repository, or at: https://www.gnu.org/licenses/gpl-3.0.html

## Model Card Contact

For questions, issues, or feedback about this model, please open an issue in the model repository or contact the author through Hugging Face.

______________________________________________________________________

**Model Version**: v1.0
**Last Updated**: 2025-10-10
