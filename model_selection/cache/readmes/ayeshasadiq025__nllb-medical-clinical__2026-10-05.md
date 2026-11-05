---
language:
- en
- ur
license: apache-2.0
tags:
- translation
- medical
- nllb
- lora
- peft
- seq2seq
- urdu
- english
- low-resource
- fine-tuned
base_model: facebook/nllb-200-distilled-600M
pipeline_tag: translation
datasets:
- pubmed_qa
metrics:
- bleu
- rouge
- bertscore
model-index:
- name: nllb-medical-clinical
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
      value: 76.02
      name: BLEU (char-level, SacreBLEU)
    - type: rouge
      value: 16.82
      name: ROUGE-L (char-level)
    - type: bertscore
      value: 91.56
      name: BERTScore F1 (multilingual-BERT, lang=ur)
---

# NLLB-200 + LoRA — Medical English → Urdu Translation

## Model Details

### Model Description

This model is a domain-adapted version of **facebook/nllb-200-distilled-600M**, fine-tuned using **LoRA (Low-Rank Adaptation)** for medical English-to-Urdu translation. It was developed as part of a student research project at Sindh Madressatul Islam University (SMIU), Karachi, to address the challenge of safely translating clinical and biomedical text into Urdu for Pakistani patients and healthcare workers.

The LoRA adapters were merged into the base model weights before uploading, so this model loads and runs like a standard `AutoModelForSeq2SeqLM` — no PEFT library required at inference time.

- **Developed by:** Ayesha Sadiq (BSE-25S-007), SMIU, Karachi
- **Supervised by:** Sir Amin Chhajro, Department of Software Engineering, SMIU
- **Model type:** Sequence-to-Sequence (Encoder-Decoder), Transformer
- **Languages:** English (`eng_Latn`) → Urdu (`urd_Arab`)
- **License:** Apache 2.0
- **Fine-tuned from:** [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M)
- **Fine-tuning method:** LoRA (r=8, alpha=32) via 🤗 PEFT

### Model Sources

- **Demo (Gradio Space):** [ayeshasadiq025/clinical-translation-portal](https://huggingface.co/spaces/ayeshasadiq025/clinical-translation-portal)
- **Ablation variant (with entity masking):** [ayeshasadiq025/nllb-medical-ablation-masked](https://huggingface.co/ayeshasadiq025/nllb-medical-ablation-masked)
- **Other models in this project:**
  - mT5 fine-tuned: [ayeshasadiq025/mt5-medical-urdu](https://huggingface.co/ayeshasadiq025/mt5-medical-urdu)
  - BioBERT + Decoder: [ayeshasadiq025/biobert-medical-urdu-decoder](https://huggingface.co/ayeshasadiq025/biobert-medical-urdu-decoder)

---

## Uses

### Direct Use

This model is intended for translating **English medical and clinical text into Urdu**. It is best suited for:

- Medical question-answering style sentences (e.g., PubMedQA-style questions)
- Clinical descriptions including symptoms, diagnoses, procedures, and drug names
- Biomedical research summaries translated for Urdu-speaking audiences

### Downstream Use

The model can be integrated into healthcare applications, clinical decision-support tools, or patient communication portals where English medical content needs to be made accessible to Urdu speakers.

### Out-of-Scope Use

- **General-purpose translation:** The model was fine-tuned on medical domain data only. Performance on non-medical text is not guaranteed.
- **Handwritten or scanned prescriptions:** This model handles typed text input only; it does not perform OCR.
- **Urdu → English translation:** The model is trained in one direction (English → Urdu) only.
- **Clinical decision-making:** Outputs must not be used as a substitute for professional medical advice or review.

---

## Bias, Risks, and Limitations

- **Domain bias:** The training data is sourced primarily from PubMedQA (research question style). The model may underperform on clinical notes or conversational medical language.
- **Medical term preservation:** Despite entity masking during preprocessing, some rare drug names, dosage expressions, or highly specialized terms may be mistranslated or omitted.
- **Machine-generated reference translations:** The Urdu side of the training corpus was initially generated using a translation utility and then cleaned. Some translation artifacts may remain.
- **Low medical entity accuracy:** Automatic medical entity accuracy on the test set was 17.5% — indicating that while the model produces fluent Urdu output, exact preservation of named medical entities (drug names, disease names) in Urdu output remains a challenge.
- **Not clinically validated:** This model has not been validated by certified medical translators or clinical linguists. It should not be used in safety-critical medical workflows without expert review.

### Recommendations

Users should treat all outputs as a starting point requiring human review, especially in clinical or patient-facing contexts. Medical professionals fluent in both English and Urdu should validate translations before use.

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "ayeshasadiq025/nllb-medical-clinical"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, torch_dtype=torch.float16)
model.eval()

# Move to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

def translate(text: str) -> str:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=128,
        truncation=True
    ).to(device)

    # Force Urdu Arabic script as target language
    target_lang_id = tokenizer.convert_tokens_to_ids("urd_Arab")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            forced_bos_token_id=target_lang_id,
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

The model was fine-tuned on a custom **12,500-sentence parallel corpus** of English–Urdu medical text:

| Split | Sentences |
|-------|-----------|
| Train | 10,000 (80%) |
| Validation | 1,250 (10%) |
| Test | 1,250 (10%) |

**Data sources:**
- English sentences sourced from [PubMedQA](https://pubmedqa.github.io/) — biomedical question-answering dataset with clinical-style research questions
- Urdu translations generated with a translation utility and post-processed for quality
- Final dataset saved as `medical_parallel_dataset.csv` with two columns: `english_text` and `urdu_text`

### Preprocessing

Before tokenization, the following preprocessing pipeline was applied to the English source text:

1. **Abbreviation expansion:** Common medical abbreviations were expanded (e.g., ICU → Intensive Care Unit, BP → Blood Pressure, MRI → Magnetic Resonance Imaging, HIV → Human Immunodeficiency Virus, etc.)
2. **Named Entity Recognition (NER):** spaCy's `en_core_web_sm` model was used to detect biomedical entities (diseases, drugs, procedures, etc.)
3. **Medical entity masking:** Detected entities were replaced with typed placeholder tokens (`[MEDICAL_TERM]`, `[DISEASE]`, `[DRUG_CHEMICAL]`) to prevent subword tokenization from fragmenting critical clinical terms — the unmasked variant (this model) was trained on raw expanded text; the masked variant is available as [nllb-medical-ablation-masked](https://huggingface.co/ayeshasadiq025/nllb-medical-ablation-masked)
4. **Tokenization:** Sequences truncated to a maximum length of 128 tokens; padding tokens excluded from loss computation

### Training Hyperparameters

| Parameter | Value |
|-----------|-------|
| Base model | `facebook/nllb-200-distilled-600M` |
| Fine-tuning method | LoRA (PEFT) |
| LoRA rank (r) | 8 |
| LoRA alpha | 32 |
| LoRA target modules | `q_proj`, `v_proj` |
| LoRA dropout | 0.1 |
| Trainable parameters | ~4.1M (LoRA adapters only) |
| Optimizer | Adafactor |
| Learning rate | 1e-4 |
| Training epochs | 3 |
| Per-device batch size | 1 |
| Gradient accumulation steps | 16 (effective batch size = 16) |
| Mixed precision | FP16 |
| Max sequence length | 128 tokens |
| Gradient checkpointing | Enabled |
| Max gradient norm | 1.0 |
| Weight decay | 0.01 |
| Training hardware | Google Colab T4 GPU |

### Training Loss History

| Epoch | Training Loss | Validation Loss |
|-------|--------------|-----------------|
| 1 | 10.834 | 0.576 |
| 2 | 9.401 | 0.444 |
| 3 | 9.236 | 0.535 |

Validation loss reached its lowest at Epoch 2 (0.444), with a slight uptick at Epoch 3 — consistent with the model approaching convergence on this domain-specific dataset.

---

## Evaluation

### Testing Data

Evaluation was performed on a fixed random sample of **100 sentences** from the 1,250-sentence held-out test split (random_state=42 for reproducibility). All three models in the project were evaluated on the same 100 sentences for a fair comparison.

### Metrics

| Metric | Description |
|--------|-------------|
| **BLEU** | Character-level corpus BLEU via SacreBLEU (`tokenize="char"`) — suitable for Urdu script without word-segmentation assumptions |
| **ROUGE-L** | Character-level ROUGE Longest Common Subsequence F-measure |
| **BERTScore** | Contextual embedding similarity using multilingual BERT (`lang="ur"`) — captures semantic similarity beyond surface match |
| **Medical Accuracy** | Percentage of English medical entities (detected by spaCy NER) that appear in the Urdu output |
| **Human Acceptance Rate** | Percentage of translations rated ≥ 3/5 by two independent human evaluators |

### Results

**This model (NLLB + LoRA) achieved the best results across all metrics** compared to the other two models in the project (mT5 full fine-tune and BioBERT + custom decoder):

| Model | BLEU ↑ | ROUGE-L ↑ | BERTScore ↑ | Medical Acc (%) | Human Acceptance |
|-------|--------|-----------|-------------|-----------------|------------------|
| **NLLB + LoRA (this model)** | **76.02** | **16.82** | **91.56** | **17.5** | **92.0%** |
| mT5 Fine-tuned | 64.65 | 14.48 | 89.08 | 17.5 | 84.0% |
| BioBERT + Decoder | 34.59 | 1.00 | 77.84 | 0.0 | — |

**Human evaluation (inter-rater agreement):**

Two evaluators independently rated 100 translations on a 1–5 scale. Cohen's Kappa for this model was **0.730** (substantial agreement per Landis & Koch 1977). A paired Wilcoxon signed-rank test confirmed the difference between NLLB+LoRA and mT5 was statistically significant.

### Summary

NLLB-200+LoRA outperformed both fine-tuned mT5 and the custom BioBERT+Decoder architecture on all automatic metrics and human evaluation. The result supports the hypothesis that a multilingual translation-focused base model (NLLB) with lightweight LoRA domain adaptation is more effective for low-resource medical translation than either full fine-tuning of a general multilingual model or a biomedical encoder with a custom decoder.

---

## Ablation Study

An ablation study compared this model (trained on **raw expanded text**) against a variant trained on **entity-masked text** (where medical terms were replaced with placeholder tokens before translation). See [nllb-medical-ablation-masked](https://huggingface.co/ayeshasadiq025/nllb-medical-ablation-masked) for the masked variant.

The ablation confirmed that training on raw (non-masked) text produced better BLEU and BERTScore results — masking medical entities before translation caused the model to learn to reproduce placeholder tokens rather than actual Urdu medical terms.

---

## Environmental Impact

Training was performed on a **Google Colab free-tier T4 GPU**.

- **Hardware:** NVIDIA T4 GPU (16GB VRAM)
- **Cloud Provider:** Google Colab
- **Training duration:** 3 epochs (~a few hours on T4)
- **Precision:** FP16 mixed precision
- Carbon emissions were not formally tracked. Estimates can be generated using the [ML CO2 Impact Calculator](https://mlco2.github.io/impact#compute).

---

## Technical Specifications

### Model Architecture

- **Base:** `facebook/nllb-200-distilled-600M` — a distilled 600M-parameter multilingual seq2seq Transformer supporting 200 languages
- **Adaptation:** LoRA adapters applied to the `q_proj` and `v_proj` attention projection layers in both encoder and decoder
- **Trainable parameters during fine-tuning:** ~4.1M (LoRA adapters) out of ~600M total
- **Inference:** LoRA weights merged into base model before upload — standard `AutoModelForSeq2SeqLM` API, no PEFT dependency needed

### Software

```
transformers
peft
torch
accelerate
sentencepiece
protobuf
sacrebleu
bert-score
rouge_score
datasets
```

---

## Citation

If you use this model in your work, please cite:

```bibtex
@misc{sadiq2026nllbmedicalurdu,
  title        = {Domain-Specific Medical English to Urdu Translation Using NLLB-200 and LoRA},
  author       = {Ayesha Sadiq},
  year         = {2026},
  institution  = {Sindh Madressatul Islam University (SMIU), Karachi},
  note         = {BSE-25S-007. Supervised by Amin Chhajro. Model available at https://huggingface.co/ayeshasadiq025/nllb-medical-clinical}
}
```

---

## Model Card Authors

Ayesha Sadiq — Department of Software Engineering, SMIU, Karachi
Supervisor: Sir Amin Chhajro

## Model Card Contact

HuggingFace: [ayeshasadiq025](https://huggingface.co/ayeshasadiq025)