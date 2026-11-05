---
language:
- en
- ur
license: apache-2.0
tags:
- translation
- medical
- mt5
- seq2seq
- urdu
- english
- fine-tuned
- low-resource
base_model: google/mt5-base
pipeline_tag: translation
datasets:
- pubmed_qa
metrics:
- bleu
- rouge
- bertscore
model-index:
- name: mt5-medical-urdu
  results:
  - task:
      type: translation
      name: Medical English to Urdu Translation
    dataset:
      name: Medical Parallel Dataset (PubMedQA-based)
      type: custom
      split: test
    metrics:
    - type: bleu
      value: 64.65
      name: BLEU (char-level, SacreBLEU)
    - type: rouge
      value: 14.48
      name: ROUGE-L (char-level)
    - type: bertscore
      value: 89.08
      name: BERTScore F1 (multilingual-BERT, lang=ur)
---

# mT5-base — Medical English → Urdu Translation (Full Fine-Tune)

## Model Details

### Model Description

This model is **google/mt5-base** fully fine-tuned for medical English-to-Urdu translation. It was developed as part of a student research project at Sindh Madressatul Islam University (SMIU), Karachi, comparing three architectures for domain-specific low-resource medical translation.

All model parameters were updated during training (full fine-tuning — no adapter methods). This model serves as a strong baseline against the LoRA-adapted NLLB-200 model in the same project.

- **Developed by:** Ayesha Sadiq (BSE-25S-007), SMIU, Karachi
- **Supervised by:** Sir Amin Chhajro, Department of Software Engineering, SMIU
- **Model type:** Sequence-to-Sequence (Encoder-Decoder), Transformer
- **Languages:** English → Urdu (`urd_Arab`)
- **License:** Apache 2.0
- **Fine-tuned from:** [google/mt5-base](https://huggingface.co/google/mt5-base)
- **Fine-tuning method:** Full fine-tuning (~580M parameters)

### Model Sources

- **Other models in this project:**
  - NLLB-200 + LoRA *(best model)*: [ayeshasadiq025/nllb-medical-clinical](https://huggingface.co/ayeshasadiq025/nllb-medical-clinical)
  - BioBERT + Decoder: [ayeshasadiq025/biobert-medical-urdu-decoder](https://huggingface.co/ayeshasadiq025/biobert-medical-urdu-decoder)
  - NLLB ablation (entity masking): [ayeshasadiq025/nllb-medical-ablation-masked](https://huggingface.co/ayeshasadiq025/nllb-medical-ablation-masked)

---

## Uses

### Direct Use

Translating **English medical and clinical text into Urdu**. Best suited for:

- Clinical descriptions (symptoms, diagnoses, procedures, drug names)
- Medical question-answering style sentences (PubMedQA style)
- Biomedical research summaries for Urdu-speaking audiences

### Downstream Use

Can be integrated into healthcare portals, clinical decision-support tools, or patient communication systems requiring English-to-Urdu medical translation.

### Out-of-Scope Use

- General-purpose translation (fine-tuned on medical domain only)
- Urdu → English direction (one-directional model)
- Handwritten or scanned text (typed input only)
- Clinical decision-making without expert review

---

## Bias, Risks, and Limitations

- **Domain bias:** Training data is PubMedQA-style research questions. Performance on clinical notes or conversational medical language may vary.
- **Machine-generated references:** Urdu translations were initially generated using a translation utility and then post-processed. Some artifacts may remain.
- **Medical entity accuracy:** Automatic medical entity accuracy on the test set was 17.5% — exact preservation of drug names and disease terms in Urdu output remains challenging.
- **Not clinically validated:** Not reviewed by certified medical translators. Should not be used in safety-critical workflows without expert review.
- **Catastrophic forgetting risk:** Initial training with LR=3e-4 caused instability; final model uses LR=2e-5 to protect multilingual pre-trained weights.

### Recommendations

Treat all outputs as a first draft requiring human review by a bilingual medical professional before clinical use.

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "ayeshasadiq025/mt5-medical-urdu"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

def translate(text: str) -> str:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=128,
        truncation=True
    ).to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=128,
            num_beams=4,
            early_stopping=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Example
text = "Patient presented with acute myocardial infarction and elevated troponin levels."
print(translate(text))
# → مریض شدید مایوکارڈیل انفارکشن اور بلند ٹراپونن سطح کے ساتھ پیش ہوا۔
```

---

## Training Details

### Training Data

Fine-tuned on a custom **12,500-sentence parallel corpus** of English–Urdu medical text:

| Split | Sentences |
|-------|-----------|
| Train | 10,000 (80%) |
| Validation | 1,250 (10%) |
| Test | 1,250 (10%) |

**Data sources:**
- English sentences from [PubMedQA](https://pubmedqa.github.io/) — biomedical question-answering dataset
- Urdu translations generated with a translation utility and post-processed for quality

### Preprocessing

1. **Abbreviation expansion:** ICU → Intensive Care Unit, BP → Blood Pressure, MRI → Magnetic Resonance Imaging, HIV → Human Immunodeficiency Virus, etc.
2. **Named Entity Recognition:** spaCy `en_core_web_sm` used to detect medical entities
3. **Entity masking:** Medical terms replaced with placeholder tokens to prevent subword fragmentation (stored in `masked_english_text` column; this model was trained on the raw `clean_english_text` column)
4. **Tokenization:** `google/mt5-base` tokenizer, max length 128 tokens for both source and target; padding tokens excluded from loss computation

### Training Hyperparameters

| Parameter | Value |
|-----------|-------|
| Base model | `google/mt5-base` |
| Fine-tuning method | Full fine-tuning (~580M params) |
| Optimizer | AdamW |
| Learning rate | 2e-5 |
| Training epochs | 4 |
| Per-device batch size | 4 |
| Gradient accumulation steps | 4 (effective batch size = 16) |
| Warmup steps | 200 |
| Weight decay | 0.01 |
| Beam search (generation) | 5 beams |
| Mixed precision | FP32 (FP16 disabled to prevent weight collapse) |
| Max sequence length | 128 tokens |
| Gradient checkpointing | Enabled |
| Training hardware | Google Colab T4 GPU |

### Training Loss History

| Epoch | Training Loss | Validation Loss |
|-------|--------------|-----------------|
| 1 | 14.629 | 2.548 |
| 2 | 11.646 | 1.977 |
| 3 | 11.042 | 1.804 |
| 4 | 10.502 | 1.760 |

Validation loss decreased steadily across all 4 epochs, with the best model saved at epoch 4.

---

## Evaluation

### Testing Data

Fixed random sample of **100 sentences** from the 1,250-sentence held-out test split (random_state=42). Same 100 sentences used for all three models for fair comparison.

### Metrics

| Metric | Description |
|--------|-------------|
| **BLEU** | Character-level corpus BLEU via SacreBLEU (`tokenize="char"`) |
| **ROUGE-L** | Character-level ROUGE Longest Common Subsequence F-measure |
| **BERTScore** | Contextual embedding similarity using multilingual BERT (`lang="ur"`) |
| **Medical Accuracy** | % of English medical entities (spaCy NER) found in the Urdu output |
| **Human Acceptance** | % of translations rated ≥ 3/5 by two independent human evaluators |

### Results

| Model | BLEU ↑ | ROUGE-L ↑ | BERTScore ↑ | Medical Acc (%) | Human Acceptance |
|-------|--------|-----------|-------------|-----------------|------------------|
| NLLB + LoRA *(best)* | **76.02** | **16.82** | **91.56** | **17.5** | **92.0%** |
| **mT5 Fine-tuned (this model)** | 64.65 | 14.48 | 89.08 | 17.5 | 84.0% |
| BioBERT + Decoder | 34.59 | 1.00 | 77.84 | 0.0 | — |

**Human evaluation (inter-rater agreement):**
Cohen's Kappa for this model = **0.864** (almost perfect agreement per Landis & Koch 1977).

### Summary

mT5 full fine-tuning achieved strong results — BLEU 64.65 and BERTScore 89.08 — placing it second among three compared models. It outperformed the custom BioBERT+Decoder by a wide margin, and its human acceptance rate (84%) was also competitive. NLLB+LoRA performed better, but mT5 is a viable option when a simpler, adapter-free setup is preferred.

---

## Environmental Impact

- **Hardware:** NVIDIA T4 GPU (Google Colab free tier)
- **Cloud Provider:** Google Colab
- **Training duration:** 4 epochs (~a few hours on T4)
- **Precision:** FP32
- Carbon estimate: [ML CO2 Impact Calculator](https://mlco2.github.io/impact#compute)

---

## Technical Specifications

### Model Architecture

- **Base:** `google/mt5-base` — multilingual text-to-text transfer Transformer, ~580M parameters, trained on mC4 corpus covering 101 languages including Urdu
- **Fine-tuning:** All parameters updated (no adapter layers)
- **Generation:** Beam search (4 beams) at inference

### Software

```
transformers
torch
sentencepiece
protobuf
sacrebleu
bert-score
rouge_score
datasets
```

---

## Citation

```bibtex
@misc{sadiq2026mt5medicalurdu,
  title        = {Domain-Specific Medical English to Urdu Translation Using Fine-Tuned mT5},
  author       = {Ayesha Sadiq},
  year         = {2026},
  institution  = {Sindh Madressatul Islam University (SMIU), Karachi},
  note         = {BSE-25S-007. Supervised by Amin Chhajro. Model available at https://huggingface.co/ayeshasadiq025/mt5-medical-urdu}
}
```

---

## Model Card Authors

Ayesha Sadiq — Department of Software Engineering, SMIU, Karachi
Supervisor: Sir Amin Chhajro

## Model Card Contact

HuggingFace: [ayeshasadiq025](https://huggingface.co/ayeshasadiq025)