---
license: mit
language:
- en
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: fill-mask
mask_token: "[MASK]"
tags:
- fill-mask
- masked-lm
- long-context
- modernbert
- BioClinical-ModernBERT
- clinical
- biomedical
- clinical encoder
- clinical modern bert
library_name: transformers
---

# BioClinical ModernBERT

*BioClinical ModernBERT is available in two sizes: [base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) (150M parameters) and [large](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-large) (396M parameters). The model training checkpoints can be found [here](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-checkpoints), and our code is available in our [GitHub repository](https://github.com/lindvalllab/BioClinical-ModernBERT).*

**A step-by-step guide for reproducing our model training with your own data is available [here](https://huggingface.co/blog/thomas-sounack/bioclinical-modernbert-tutorial)!**

## Table of Contents
1. [Model Summary](#model-summary)
2. [Usage](#usage)
3. [Training](#training)
4. [Evaluation](#evaluation)
5. [License](#license)
6. [Citation](#citation)

## Model Summary

BioClinical ModernBERT is a domain-adapted encoder that builds on ModernBERT [base](https://huggingface.co/answerdotai/ModernBERT-base) and [large](https://huggingface.co/answerdotai/ModernBERT-large), incorporating long-context processing and substantial improvements in speed and performance for biomedical and clinical NLP. BioClinical ModernBERT is trained on the largest biomedical and clinical corpus to date, with over 53.5 billion tokens, and addresses a key limitation of prior clinical encoders by leveraging 20 datasets from diverse institutions, domains, and geographic regions, rather than relying on data from a single source.

## Usage

You can use these models directly with the `transformers` library starting from v4.48.0:

```sh
pip install -U transformers>=4.48.0
```

Since BioClinical ModernBERT is a Masked Language Model (MLM), you can use the `fill-mask` pipeline or load it via `AutoModelForMaskedLM`. To use BioClinical ModernBERT for downstream tasks like classification, retrieval, or QA, fine-tune it following standard BERT fine-tuning recipes.

**⚠️ If your GPU supports it, we recommend using BioClinical ModernBERT with Flash Attention 2 to reach the highest efficiency. To do so, install Flash Attention as follows, then use the model as normal:**

```bash
pip install flash-attn
```

Using `AutoModelForMaskedLM`:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
model_id = "thomas-sounack/BioClinical-ModernBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id)
text = "Mitochondria is the powerhouse of the [MASK]."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
# To get predictions for the mask:
masked_index = inputs["input_ids"][0].tolist().index(tokenizer.mask_token_id)
predicted_token_id = outputs.logits[0, masked_index].argmax(axis=-1)
predicted_token = tokenizer.decode(predicted_token_id)
print("Predicted token:", predicted_token)
# Predicted token:  cell
```

Using a pipeline:

```python
import torch
from transformers import pipeline
from pprint import pprint
pipe = pipeline(
    "fill-mask",
    model="thomas-sounack/BioClinical-ModernBERT-base",
    torch_dtype=torch.bfloat16,
)
input_text = "[MASK] is a disease caused by an uncontrolled division of abnormal cells in a part of the body."
results = pipe(input_text)
pprint(results)
```

**Note:** BioClinical ModernBERT, similarly to ModernBERT, does not use token type IDs unlike some earlier BERT models. Most downstream usage is identical to standard BERT models on the Hugging Face Hub, except you can omit the `token_type_ids` parameter.

## Training

### Data

BioClinical ModernBERT is trained on 50.7B tokens of biomedical text gathered from PubMed and PMC, and 2.8B tokens of clinical text from 20 datasets which are detailed in the table below.

| Name                       | Country      | Clinical Source                    | Clinical Context      | Samples   | Tokens (M) |
|----------------------------|--------------|------------------------------------|-----------------------|-----------|------------|
| ACI-BENCH                  | US           | Clinical Notes                     | Not Reported          | 207       | 0.1        |
| ADE Corpus                 | Several      | Clinical Notes                     | Not Reported          | 20,896    | 0.5        |
| Brain MRI Stroke           | Korea        | Radiology Reports                  | Neurology             | 2,603     | 0.2        |
| CheXpert Plus              | US           | Radiology Reports                  | Pulmonology           | 223,460   | 60.6       |
| CHIFIR                     | Australia    | Pathology Reports                  | Hematology / Oncology | 283       | 0.1        |
| CORAL                      | US           | Progress Notes                     | Hematology / Oncology | 240       | 0.7        |
| Eye Gaze CXR               | US           | Radiology Reports                  | Pulmonology           | 892       | 0.03       |
| Gout Chief Complaints      | US           | Chief Complaint                    | Internal Medicine     | 8,429     | 0.2        |
| ID-68                      | UK           | Clinical Notes                     | Psychology            | 78        | 0.02       |
| Inspect                    | US           | Radiology Reports                  | Pulmonology           | 22,259    | 2.8        |
| MedNLI                     | US           | Clinical Notes                     | Internal Medicine     | 14,047    | 0.5        |
| MedQA                      | US           | National Medical Board Examination | Not Reported          | 14,366    | 2.0        |
| MIMIC-III                  | US           | Clinical Notes                     | Internal Medicine     | 2,021,411 | 1,047.7    |
| MIMIC-IV Note              | US           | Clinical Notes                     | Internal Medicine     | 2,631,243 | 1,765.7    |
| MTSamples                  | Not Reported | Clinical Notes                     | Internal Medicine     | 2,358     | 1.7        |
| Negex                      | US           | Discharge Summaries                | Not Reported          | 2,056     | 0.1        |
| PriMock57                  | UK           | Simulated Patient Care             | Internal Medicine     | 57        | 0.01       |
| Q-Pain                     | US           | Clinical Vignettes                 | Palliative Care       | 51        | 0.01       |
| REFLACX                    | US           | Radiology Reports                  | Pulmonology           | 2,543     | 0.1        |
| Simulated Resp. Interviews | Canada       | Simulated Patient Care             | Pulmonology           | 272       | 0.6        |

### Methodology

BioClinical ModernBERT base is trained in two phases. This model is initialized from the last stable-phase checkpoint of ModernBERT base and trained with the same hyperparameters: learning rate of 3e-4 and batch size of 72.
- Phase 1: Training on 160.5B tokens from PubMed, PMC, and the 20 clinical datasets. Learning rate remains constant throughout this stage, and the masking probability is set at 30%.
- Phase 2: Training on the 20 clinical datasets only. Masking probability is reduced to 15%. The model is trained for 3 epochs with a 1-sqrt learning rate decay.

## Evaluation

|       | Model                          | Context Length | ChemProt | Phenotype | COS      | Social History | DEID     |
|-------|--------------------------------|----------------|----------|-----------|----------|----------------|----------|
| Base  | BioBERT                        | 512            | 89.5     | 26.6      | 94.9     | 55.8           | 74.3     |
|       | Clinical BERT                  | 512            | 88.3     | 25.8      | 95.0     | 55.2           | 74.2     |
|       | BioMed-RoBERTa                 | 512            | 89.0     | 36.8      | 94.9     | 55.2           | 81.1     |
|       | Clinical-BigBird               | 4096           | 87.4     | 26.5      | 94.0     | 53.3           | 71.2     |
|       | Clinical-Longformer            | 4096           | 74.2     | 46.4      | **95.2** | 56.8           | 82.3     |
|       | Clinical ModernBERT            | 8192           | 86.9     | 54.9      | 93.7     | 53.8           | 44.4     |
|       | ModernBERT - base              | 8192           | 89.5     | 48.4      | 94.0     | 53.1           | 78.3     |
|       | BioClinical ModernBERT - base  | 8192           | 89.9     | 58.1      | 95.1     | **58.5**       | 82.7     |
| Large | ModernBERT - large             | 8192           | 90.2     | 58.3      | 94.4     | 54.8           | 82.1     |
|       | BioClinical ModernBERT - large | 8192           | **90.8** | **60.8**  | 95.1     | 57.1           | **83.8** |

## License

We release the BioClinical ModernBERT base and large model weights and training checkpoints under the MIT license.

## Citation

If you use BioClinical ModernBERT in your work, please cite our [preprint](https://arxiv.org/abs/2506.10896):

```
@misc{sounack2025bioclinicalmodernbertstateoftheartlongcontext,
      title={BioClinical ModernBERT: A State-of-the-Art Long-Context Encoder for Biomedical and Clinical NLP}, 
      author={Thomas Sounack and Joshua Davis and Brigitte Durieux and Antoine Chaffin and Tom J. Pollard and Eric Lehman and Alistair E. W. Johnson and Matthew McDermott and Tristan Naumann and Charlotta Lindvall},
      year={2025},
      eprint={2506.10896},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.10896}, 
}
```

*This project was a collaboration between members of the Dana-Farber Cancer Institute, LightOn, MIT, OpenEvidence and Microsoft.*