---
library_name: transformers
tags:
- clinical
- healthcare
- NLP
- BERT
- MIMIC-IV
- MedNLI
- transformer
language:
- en
metrics:
- accuracy
base_model:
- mosaicml/mosaic-bert-base
license: mit
datasets:
- bigbio/mednli
pipeline_tag: fill-mask
model-index:
- name: ClinicalMosaic
  results:
  - task:
      type: classification
    dataset:
      name: MedNLI
      type: MedNLI
    metrics:
    - type: accuracy
      value: 86.5
      name: Accuracy
---

# Model Card for Clinical Mosaic

Clinical Mosaic is a transformer-based language model designed for clinical text, built on the Mosaic BERT architecture. The model is pretrained on 331,794 deidentified clinical notes from the MIMIC-IV-NOTES 2.2 database, with a sequence length of 512 tokens, while leveraging Attention with Linear Biases (ALiBi) to improve extrapolation beyond this limit without re-quiring learned positional embeddings.
## Model Details
- **Developed by:** Sifal Klioui, Sana Sellami, and Youssef Trardi (Aix-Marseille Univ, LIS, CNRS, Marseille, France)
- **Funded by:** PICOMALE project (AMIDEX) Under the direction of the CEDRE
- **Base Model:** Mosaic BERT
- **License:** MIMIC Data Use Agreement (requires compliance with original DUA)
- **Repository:** [PatientTrajectoryForecasting](https://github.com/MostHumble/PatientTrajectoryForecasting)
- **Paper:** *Patient Trajectory Prediction: Integrating Clinical Notes with Transformers* [[EN](https://arxiv.org/abs/2502.18009), [FR](https://editions-rnti.fr/?inprocid=1002990)]

## Uses

### Direct Use

Clinical Mosaic can be used directly as a clinical language model for:
- Natural language inference and clinical reasoning tasks.
- Serving as a backbone for further fine-tuning on clinical NLP applications (e.g., clinical note summarization, diagnosis classification).

### Downstream Use

The model can be integrated into larger systems for tasks such as patient trajectory prediction or decision support, provided that additional fine-tuning and rigorous validation are performed.

### Out-of-Scope Use

- **Clinical Decision-Making:** The model is for research use only and should not be deployed for direct patient care without further validation and regulatory approval.
- **Medical Advice Generation:** It is not intended to replace expert clinical judgment.

## Bias, Risks, and Limitations

Clinical Mosaic was pre-trained on deidentified clinical notes from MIMIC-IV-NOTES 2.2—a dataset from a single U.S. institution. This may introduce biases related to local clinical practices and patient demographics. Although extensive care was taken to deidentify data and prevent PHI leakage, users must ensure that the model is not used to inadvertently reidentify sensitive information. When applying the model to new populations or clinical settings, performance may vary, so further fine-tuning and bias audits are recommended.

### Recommendations
- **Text Normalization Consistency:** Any input text must undergo identical preprocessing as applied during training
- **Evaluation:** Users should evaluate the model’s performance on their target population.
- **Fine-Tuning:** Consider additional fine-tuning or domain adaptation if deploying in a different clinical context.
- **Bias Audits:** Regularly perform bias audits to monitor for potential disparities in performance.

## How to Get Started with the Model

Install the Hugging Face Transformers library and load the model as follows:

### For embeddings generation:

```python
# Load model directly
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("Sifal/ClinicalMosaic", trust_remote_code=True)
ClincalMosaic = AutoModel.from_pretrained("Sifal/ClinicalMosaic", trust_remote_code=True)

# Example usage
clinical_text = "..."

inputs = tokenizer(clinical_text, return_tensors="pt")
last_layer_embeddings = ClincalMosaic(**inputs, output_all_encoded_layers=False)
```

### For sequence classification:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Sifal/ClinicalMosaic')

ClassifierClincalMosaic = AutoModelForSequenceClassification.from_pretrained(
    'Sifal/ClinicalMosaic',
    torch_dtype='auto',
    trust_remote_code=True,
    device_map="auto"
)

# Example usage
clinical_text = "..."

inputs = tokenizer(clinical_text, return_tensors="pt")
logits = ClassifierClincalMosaic(**inputs).logits
```

Further instructions and example scripts are provided in the model’s repository.

## Training Details

### Training Data

- **Data Source:** 331,794 clinical notes from the MIMIC-IV-NOTES 2.2 dataset.
- **Preprocessing:** 
  - Following (Alsentzer et al., 2019), clinical notes were preprocessed by unifying medical abbreviations (e.g., “hr”, “hrs” to “hours”), removing accents, converting special characters, and normalizing text to lowercase. These steps help mitigate variations caused by subword tokenizers.
  - For additional details, please refer to the [PatientTrajectoryForecasting GitHub repository](https://github.com/MostHumble/PatientTrajectoryForecasting/).

### Training Procedure

- **Setup:** Distributed training using 7 NVIDIA A40 GPUs.
- **Hyperparameters:**
  - **Effective Batch Size:** 224
  - **Training Steps:** 80,000
  - **Sequence Length:** 512 tokens
  - **Optimizer:** ADAMW
  - **Initial Learning Rate:** 5e-4
  - **Learning Rate Schedule:** Linear warmup for 33,000 steps, followed by cosine annealing for 46,000 steps (final LR 1e-5)
  - **Masking Probability:** 30%

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model was evaluated on the MedNLI dataset, which comprises 14,049 clinical premise-hypothesis pairs derived from MIMIC-III notes.

#### Factors

Evaluation disaggregated performance across clinical language understanding, with a focus on natural language inference.

### Results

Clinical Mosaic outperformed comparable models:
- **BERT:** 77.6%
- **BioBERT:** 80.8%
- **Clinical Discharge BERT:** 84.1%
- **Bio+Clinical BERT:** 82.7%
- **Clinical Mosaic:** **86.5%**

These results indicate improved clinical reasoning and language understanding.

#### Summary

The model demonstrates robust performance on clinical natural language inference tasks and serves as a strong foundation for further clinical NLP applications.

## Environmental Impact

- **Hardware Type:** 7 NVIDIA A40 GPUs
- **Hours used:** 1008 (GPU hours)
- **Provider:** Private Infrastructure
- **Carbon Emitted:** 108.86 kg CO2 eq.


## Acknowledgments

The project leading to this publication has received funding from the Excellence Initiative of Aix Marseille Université - A*Midex, a French “Investissements d’Avenir programme” AMX-21-IET-017.

We would like to thank **LIS** | Laboratoire d'Informatique et Systèmes, Aix-Marseille University for providing the GPU resources necessary for pretraining and conducting extensive experiments. Additionally, we acknowledge **CEDRE** | CEntre de formation et de soutien aux Données de la REcherche, Programme 2 du projet France 2030 IDeAL for supporting early-stage experiments and hosting part of the computational infrastructure.

## Citation

**BibTeX:**

```bibtex
@misc{klioui2025patienttrajectorypredictionintegrating,
      title={Patient Trajectory Prediction: Integrating Clinical Notes with Transformers}, 
      author={Sifal Klioui and Sana Sellami and Youssef Trardi},
      year={2025},
      eprint={2502.18009},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2502.18009}, 
}

@article{RNTI/papers/1002990,
  author    = {Sifal Klioui and Sana Sellami and Youssef Trardi},
  title     = {Prédiction de la trajectoire du patient : Intégration des notes cliniques aux transformers},
  journal = {Revue des Nouvelles Technologies de l'Information},
  volume = {Extraction et Gestion des Connaissances, RNTI-E-41},
  year      = {2025},
  pages     = {135-146}
}
```

## More Information

For further details, please refer to the model’s repository and supplementary documentation.

## Model Card Contact

For questions or further information, please contact [sifal.klioui@etu.univ-amu.fr].