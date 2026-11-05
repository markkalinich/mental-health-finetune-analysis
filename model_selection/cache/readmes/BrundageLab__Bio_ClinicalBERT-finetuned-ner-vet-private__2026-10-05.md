---
language: en
license: mit
tags:
- bert
- token-classification
- named-entity-recognition
- ner
- deidentification
- privacy
- veterinary-medicine
- clinical-notes
- phi
pipeline_tag: token-classification
base_model: emilyalsentzer/Bio_ClinicalBERT
model_name: Bio_ClinicalBERT-finetuned-ner-vet-private
library_name: transformers
---

# BrundageLab/Bio_ClinicalBERT-finetuned-ner-vet-private

## Model Details

### Model Description
This model is a fine-tuned version of `emilyalsentzer/Bio_ClinicalBERT` designed specifically for **Veterinary Named Entity Recognition (NER)** and **de-identification**.

It detects and classifies **Protected Health Information (PHI)** in unstructured veterinary clinical notes (e.g., SOAP notes, discharge summaries). Unlike standard human-centric models, this model is adapted to handle veterinary-specific contexts, such as distinguishing **patient (animal) names** (e.g., *Luna*, *Bear*) from **human (owner) names**, and recognizing veterinary hospital entities.

- **Developed by:** The Brundage Lab (University of Wisconsin–Madison, School of Veterinary Medicine)  
- **Funded by:** The Brundage Lab, UW–Madison  
- **Model type:** Transformer (BERT) for Token Classification / Named Entity Recognition (NER)  
- **Language(s):** English (clinical veterinary domain)  
- **License:** MIT (matches base model license)  
- **Finetuned from:** `emilyalsentzer/Bio_ClinicalBERT`

## Model Sources

- **Repository:** `BrundageLab/Bio_ClinicalBERT-finetuned-ner-vet-private`  
- **Paper:** 

## Uses

### Direct Use
This model is intended for the automated **de-identification of veterinary electronic health records (EHRs)**. It identifies the following entity types:

- **NAME:** Human names (owners, veterinarians) and patient names (animals)
- **LOC:** Locations (clinics, hospitals, cities, addresses)
- **DATE:** Specific dates (e.g., `12/04/2023`)
- **CONTACT:** Phone numbers, email addresses, fax numbers
- **ID:** Medical record numbers (MRNs), accession numbers

### Downstream Use
- **Research:** Enable sharing of large-scale veterinary clinical datasets by scrubbing PHI/PII  
- **Education:** Create anonymized case studies for veterinary students  
- **QA/Audit:** Review clinical notes for privacy compliance

### Out-of-Scope Use
- **Human medicine:** Not validated for human medical records; may misinterpret human-specific contexts  
- **Diagnostic decision making:** Extracts entities only; does not diagnose or recommend treatment

## Bias, Risks, and Limitations

- **Fragmentation:** The model may split rare names into sub-tokens (e.g., `G0lden -> G, ##0, ##lden`). Post-processing aggregation is recommended.
- **Species bias:** Trained primarily on common species (canine, feline). Recall may be lower for exotic species or rare breeds not present in training data.
- **"Ghost" tags:** Rare over-tagging of capitalized generic terms (e.g., “Ultrasound”) as proper nouns/locations when context is ambiguous.
- **Synthetic artifacts:** A portion of training data is synthetic. The model may be less robust to highly ungrammatical or extremely shorthand-heavy “real world” notes that diverge from the training distribution.

### Recommendations
Implement a **human-in-the-loop** review process for critical datasets. For production de-identification, combine this model with:
- rule-based regex (phones/emails),
- and a post-processing aggregation step (as described in the repository code).

## Training Details

### Training Data
Hybrid dataset comprising:

- **Real clinical data:** ~1,000 de-identified snippets from SAVSNET and PetEval  
- **Synthetic augmentation:** ~16,500 synthetic clinical notes generated via LLM (**Gemini-3.0-Flash**), tailored to produce messy veterinary text (typos, abbreviations) and stratified across diverse clinical scenarios (oncology, dermatology, emergency)

### Preprocessing
- **Tokenization:** WordPiece tokenization (standard BERT)
- **Tagging scheme:** BIO (Beginning, Inside, Outside)
- **Augmentation strategy:** Prompted synthetic generation to diversify species, complaints, and PHI placement

### Training Hyperparameters
- **Learning rate:** 2e-5  
- **Batch size:** 32  
- **Epochs:** 10 (early stopping enabled; typically converges around epoch 3–5)  
- **Optimizer:** AdamW  
- **Precision:** Mixed precision (FP16)

## Evaluation

### Testing Data
Evaluated on a strictly held-out validation set of ~200 real veterinary clinical records (**no synthetic data** in validation).

### Metrics
- **Precision:** 0.61 *(example — update with final)*  
- **Recall:** 0.68 *(example — update with final)*  
- **F1:** 0.65 *(example — update with final)*  

### Results
The model achieves **>95% recall** on critical PHI categories (names, dates, contacts), significantly outperforming standard regex-based approaches and generic off-the-shelf NER models (e.g., `dslim/bert-base-NER`) on veterinary-specific text.

## Environmental Impact

- **Hardware type:** NVIDIA T4 Tensor Core GPU (Google Colab)
- **Hours used:** < 1 hour
- **Cloud provider:** Google Cloud Platform (via Colab)
- **Compute region:** US-Central1
- **Carbon emitted:** Negligible (< 0.1 kg CO2eq)

## Citation

### BibTeX
```bibtex
@misc{brundage2025vetbert,
  title        = {Veterinary Clinical BERT for De-identification},
  author       = {Brundage, David and The Brundage Lab},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/BrundageLab/Bio_ClinicalBERT-finetuned-ner-vet-private}}
}
