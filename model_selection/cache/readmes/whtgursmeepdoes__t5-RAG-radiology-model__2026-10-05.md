# T5-small Fine-Tuned with RAG-style Context for Radiology Label Extraction

This model is a **fine-tuned version of `t5-small`**, trained on a radiology dataset using a **RAG-style setup**. It extracts **five structured fields** from free-text radiologist diagnosis reports, with retrieved similar examples providing additional context.

> This hybrid approach leverages Retrieval-Augmented Generation (RAG) principles by combining traditional fine-tuning with dynamic context injection using **TF-IDF + FAISS** similarity search.

---

## Performance

- **Test Loss**: `0.1902`
- **Dataset Source**: Medical reports sourced from AIIMS (via internship assignment)
- **Model Size**: `t5-small` (~60M parameters)
- **Training Epochs**: 4
- **Batch Size**: 8

---

## Task: Structured Information Extraction from Radiology Text

Given a free-text radiologist diagnosis, the model extracts:

- `Abnormal/Normal`
- `Pathologies Extracted`
- `Midline Shift`
- `Location & Brain Organ`
- `Bleed Subcategory`

---

## Example

**Input Prompt**:
Extract info: Evidence of subdural hematoma in the right fronto-parietal region with 6mm midline shift.


**Output**:
Abnormal/Normal: Abnormal
Pathologies Extracted: Subdural Hematoma
Midline Shift: 6mm
Location & Brain Organ: Right Fronto-parietal
Bleed Subcategory: Subdural


---

##  How It Works

1. **TF-IDF Vectorization**: All diagnosis texts are converted to TF-IDF vectors.
2. **FAISS Retrieval**: For each new input, the most similar prior report is retrieved from the dataset.
3. **Augmented Prompting**: The model is trained to extract structured info **based on the retrieved report**, improving generalization.
4. **Fine-tuning**: T5 is trained using Hugging Face’s Trainer API with the retrieved document as input and the structured labels as target.

---

## Training Code Summary

The model was trained using:

- `TfidfVectorizer` for document vectorization
- `faiss.IndexFlatL2` for similarity retrieval
- Hugging Face’s `Trainer` and `Seq2Seq` APIs
- Training on GPU using Google Colab

```python
input_text = f"Extract info: {retrieved_diagnosis}"
labels = structured_labels
```

## Intended Use
This model is ideal for:

- Preprocessing free-text radiology reports

- Building structured datasets for supervised learning on imaging data

- Assisting annotation pipelines in medical NLP applications

## Author
Developed by Gursmeep Kaur during a medical NLP internship project