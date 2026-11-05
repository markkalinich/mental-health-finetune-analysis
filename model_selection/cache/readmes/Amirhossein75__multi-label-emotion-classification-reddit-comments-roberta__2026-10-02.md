---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
{
  "language": ["en"],
  "library_name": "transformers",
  "pipeline_tag": "text-classification",
  "task_categories": ["text-classification"],
  "task_ids": ["multi-label-classification"],
  "tags": ["multi-label", "emotion-detection", "reddit", "go_emotions", "pytorch", "huggingface", "peft", "accelerate"],
  "datasets": ["go_emotions"],
  "license": "other",
  base_model: "FacebookAI/roberta-base",
  "model-index": [
    {
      "name": "multi-label-emotion-classification-reddit-comments (RoBERTa-base on GoEmotions)",
      "results": [
        {
          "task": {"name": "Text Classification (multi-label emotions)", "type": "text-classification"},
          "dataset": {"name": "GoEmotions", "type": "go_emotions", "config": "simplified", "split": "test"},
          "metrics": [
            {"name": "F1 (micro)", "type": "f1", "value": 0.5284209017274747, "args": {"average": "micro", "threshold": 0.84}},
            {"name": "F1 (macro)", "type": "f1", "value": 0.49954895970228047, "args": {"average": "macro", "threshold": 0.84}},
            {"name": "F1 (samples)", "type": "f1", "value": 0.5301482007949669, "args": {"average": "samples", "threshold": 0.84}},
            {"name": "Average Precision (micro)", "type": "average_precision", "value": 0.5351637127240974, "args": {"average": "micro"}},
            {"name": "Average Precision (macro)", "type": "average_precision", "value": 0.5087333698463412, "args": {"average": "macro"}},
            {"name": "ROC AUC (micro)", "type": "auc", "value": 0.9517119218698238, "args": {"average": "micro"}},
            {"name": "ROC AUC (macro)", "type": "auc", "value": 0.9310155721031019, "args": {"average": "macro"}}
          ]
        }
      ]
    }
  ]
}
---

# Model Card for Multi‑Label Emotion Classification on Reddit Comments

This repository contains training and inference code for **multi‑label emotion classification** of Reddit comments using the **GoEmotions** dataset (27 emotions + neutral) with a **RoBERTa‑base** encoder. It includes a configuration‑driven training script, evaluation, decision‑threshold tuning, and a lightweight inference entrypoint.

> **Repository:** https://github.com/amirhossein-yousefi/multi-label-emotion-classification-reddit-comments

## Model Details

### Model Description

This project fine‑tunes a Transformer encoder for multi‑label emotion detection on Reddit comments. The default configuration uses **`roberta-base`**, binary cross‑entropy loss (optionally focal loss), and grid‑search threshold tuning on the validation set.

- **Developed by:** GitHub **@amirhossein-yousefi**
- **Model type:** Multi‑label text classification (Transformer encoder)
- **Language(s) (NLP):** English
- **License:** No explicit license file was found in the repository; treat as “all rights reserved” unless the author adds a license.
- **Finetuned from model :** `roberta-base`

### Model Sources

- **Repository:** https://github.com/amirhossein-yousefi/multi-label-emotion-classification-reddit-comments
- **Paper [dataset]:** GoEmotions: A Dataset of Fine‑Grained Emotions (Demszky et al., 2020)

## Uses

### Direct Use

- Tagging short English texts (e.g., social posts, comments) with multiple emotions from the GoEmotions taxonomy (e.g., *joy, sadness, anger, admiration, gratitude,* etc.).
- Exploratory analytics and visualization of emotion distributions in corpora similar to Reddit.

### Downstream Use

- Fine‑tuning or domain adaptation to platforms beyond Reddit (forums, support tickets, app reviews).
- Serving as a baseline component in moderation pipelines or empathetic response systems (with careful human oversight).

### Out‑of‑Scope Use

- Medical, psychological, or diagnostic use; mental‑health inference.
- High‑stakes decisions (employment, lending, safety) without rigorous, domain‑specific validation.
- Non‑English or heavily code‑switched text without additional training/testing.

## Bias, Risks, and Limitations

- **Dataset origin:** GoEmotions is built from Reddit comments; models may inherit Reddit‑specific discourse, slang, and toxicity patterns and may underperform on other domains.
- **Annotation noise:** Third‑party analyses have raised concerns about mislabels in GoEmotions; treat labels as imperfect and consider human review for critical use cases.
- **Multi‑label uncertainty:** Threshold choice materially affects precision/recall trade‑offs. The repo tunes the threshold on validation data; you should recalibrate for your domain.

### Recommendations

- Calibrate thresholds on in‑domain validation data (the repo grid‑searches 0.05–0.95).
- Report per‑label metrics, especially for minority emotions.
- Consider bias audits and human‑in‑the‑loop review before deployment.

## How to Get Started with the Model

### Environment

- Python ≥ **3.13**
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Train

The Makefile provides a default **train** target:

```bash
python -m emoclass.train --config configs/base.yaml
```

### Inference

After training (or pointing to a trained directory), run:

```bash
python -m emoclass.inference --model_dir outputs/goemotions_roberta --text "I love this!" "This is awful."
```

## Training Details

### Training Data

- **Dataset:** GoEmotions (27 emotions + neutral). The default config uses the **`simplified`** variant.
- **Text column:** `text`
- **Labels column:** `labels`
- **Max sequence length:** 192

### Training Procedure

#### Preprocessing

- Standard Transformer tokenization for `roberta-base`.
- Multi‑hot label encoding for emotions.

#### Training Hyperparameters

- **Base model:** `roberta-base`
- **Batch size:** 16 (train), 32 (eval)
- **Learning rate:** 2e‑5
- **Epochs:** 5
- **Weight decay:** 0.01
- **Warmup ratio:** 0.06
- **Gradient accumulation:** 1
- **Precision:** bf16/fp16 if available
- **Loss:** Binary Cross‑Entropy (optionally focal loss with γ=2.0, α=0.25)
- **Threshold tuning:** grid 0.05 → 0.95 (step 0.01); best val micro‑F1 ≈ 0.84
- **LoRA/PEFT:** available in config (default off)

#### Speeds, Sizes, Times

- See `results.txt` for an example run’s timing & throughput logs.

## Evaluation

### Testing Data, Factors & Metrics

- **Test split:** GoEmotions `simplified` test.
- **Metrics:** micro/macro/sample **F1**, micro/macro **Average Precision (AP)**, micro/macro **ROC‑AUC**.

### Results (example run)

- **Threshold (val‑tuned):** 0.84  
- **F1 (micro):** 0.5284  
- **F1 (macro):** 0.4995  
- **F1 (samples):** 0.5301  
- **AP (micro):** 0.5352  
- **AP (macro):** 0.5087  
- **ROC‑AUC (micro):** 0.9517  
- **ROC‑AUC (macro):** 0.9310  

*(See `results.txt` for the full log and any updates.)*

## Model Examination

- Inspect per‑label thresholds and confusion patterns; minority emotions (e.g., *grief, pride, nervousness*) often suffer lower F1 and need more tuning or class‑balancing strategies.

## Environmental Impact

- Not measured. If desired, log GPU type, hours, region, and estimate emissions using the ML CO2 calculator.

## Technical Specifications

### Model Architecture and Objective

- Transformer encoder (`roberta-base`) fine‑tuned with a sigmoid multi‑label head and BCE (or focal) loss.

### Compute Infrastructure

- Frameworks: `transformers`, `datasets`, `accelerate`, `evaluate`, `scikit-learn`, optional `peft`.
- Hardware/software specifics are user‑dependent.

## Citation

**GoEmotions (dataset/paper):**  
Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., & Ravi, S. (2020). *GoEmotions: A Dataset of Fine‑Grained Emotions.* ACL 2020. https://arxiv.org/abs/2005.00547

**BibTeX:**
```bibtex
@inproceedings{demszky2020goemotions,
  title={GoEmotions: A Dataset of Fine-Grained Emotions},
  author={Demszky, Dorottya and Movshovitz-Attias, Dana and Ko, Jeongwoo and Cowen, Alan and Nemade, Gaurav and Ravi, Sujith},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year={2020}
}
```

## Glossary

- **AP:** Average Precision (area under precision–recall curve).
- **AUC:** Area under ROC curve.
- **Micro/Macro F1:** Micro aggregates over all labels; macro averages per‑label F1.

## More Information

- The configuration file at `configs/base.yaml` documents tweakable knobs (loss type, LoRA, precision, etc.).
- Artifacts are saved under `outputs/` by default.

## Model Card Authors

- Original code: @amirhossein-yousefi
- Model card: generated programmatically for documentation purposes.

## Model Card Contact

- Open an issue in the GitHub repository.