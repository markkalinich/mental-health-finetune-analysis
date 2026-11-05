---
license: apache-2.0
datasets:
- SINAI/ALIA-es-biomedical
language:
- es
tags:
- biomedical
- clinical
- spanish
base_model:
- BSC-LT/salamandra-7b
---
# ALIA Spanish Biomedical 7B Base Model

This repository contains a domain-adapted version of the **Salamandra 7B** model, optimized for the Spanish biomedical and clinical domain.

This model is the result of a **continual pre-training** process on the [Salamandra 7B](https://huggingface.co/papers/2502.08489) model, followed by instruction tuning using curated biomedical corpora.

> [!WARNING]
> **DISCLAIMER:** This model is a domain-specific proof-of-concept for biomedical use. It has *NOT* been clinically validated and has not undergone regulatory review.
> It may produce incorrect, unsafe, or misleading medical information. Do not use this model for diagnosis, treatment, or other clinical decision-making. Always consult a qualified healthcare professional.

---

## Model Details

### Description
This model is a Transformer-based decoder-only language model that builds on the **Salamandra 7B** architecture through domain adaptation targeted to biomedical Spanish.

**Continual Pre-training (CPT):** The base model was further pre-trained on the [SINAI/ALIA-es-biomedical](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical) corpus to adapt its weights to the specific vocabulary and structures of biomedical and clinical Spanish texts.

### Architecture
|                         |               |
|-------------------------|:--------------|
| **Base Model** | Salamandra 7B |
| **Total Parameters** | 7,768,117,248 |
| **Embedding Parameters**| 1,048,576,000 |
| **Layers** | 32            |
| **Hidden size** | 4,096         |
| **Attention heads** | 32            |
| **Context length** | 8,192         |
| **Vocabulary size** | 256,000       |
| **Precision** | bfloat16      |
| **Embedding type** | RoPE          |
| **Activation Function** | SwiGLU        |
| **Layer normalization** | RMS Norm      |
| **Flash attention** | ✅            |
| **Grouped Query Attention** | ✅        |
| **Num. query groups** | 8             |

### Hyperparameters
| Parameter | Value |
|---|---:|
| **Sequence length** | 8,192 |
| **Sample packing** | true |
| **Pad to sequence length** | true |
| **Num. epochs** | 2 |
| **Save steps** | 2,000 |
| **Eval steps** | 500 |
| **Logging steps** | 50 |
| **Eval sample packing** | false |
| **Optimizer** | adamw_torch_fused |
| **Adam beta1** | 0.9 |
| **Adam beta2** | 0.9592 |
| **Adam epsilon** | 1e-8 |
| **Learning rate** | 5e-6 |
| **LR scheduler** | cosine |
| **Warmup steps** | 10,000 |
| **Weight decay** | 0.03 |
| **NEFTune noise alpha** | 5 |
| **Max grad norm** | 0.24 |
| **Micro batch size** | 8 |
| **Gradient accumulation steps** | 2 |
| **Eval batch size** | 1 |
| **Gradient checkpointing** | true |
| **Distributed backend** | nccl |
| **Val set size** | 1,000 |
| **Eval table size** | 5 |
| **Eval max new tokens** | 100 |
| **Do causal LM eval** | true |
| **Eval causal LM metrics** | perplexity |
| **WandB project** | biomedical-cpt |
| **WandB mode** | offline |
| **WandB name** | salamandra-biomedical-cpt |
| **WandB log model** | false |
| **WandB watch** | false |
| **Save safetensors** | true |
| **Resume from checkpoint** | null |
| **BF16** | true |
| **FP16** | false |
| **Pad token** | <|endoftext|> |
| **Save total limit** | 3 |
| **Seed** | 42 |
| **Strict** | false |
| **Liger plugin** | axolotl.integrations.liger.LigerPlugin |
| **Liger rope** | true |
| **Liger RMS norm** | true |
| **Liger GLU activation** | true |
| **Liger layer norm** | true |
| **Liger fused linear cross entropy** | true |

---

## Intended Use

### Direct Use
The model is intended for research, development and non-clinical applications within **Spanish biomedical and clinical** natural language processing. Representative use cases include:
- Summarization of biomedical literature and de-identified clinical notes for research purposes.
- Question answering over biomedical texts and knowledge bases to support information retrieval.
- Plain-language explanations of medical content for patient education (to be reviewed by clinicians).

### Out-of-scope Use
This model is not approved for clinical use. It must not be used as a sole source for diagnosis, prognosis, treatment decisions, or other actions that directly affect patient care. Any deployment that impacts patient safety requires extensive clinical validation, risk assessment and regulatory clearance.

---

## How to use

## Python Example

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "SINAI/ALIA-es-biomedical-7B-Base"

prompt = "¿Cuáles son las posibles causas de dolor torácico agudo y qué pruebas iniciales se recomiendan?"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16
)

inputs = tokenizer.encode(prompt, return_tensors="pt")
inputs = inputs.to(model.device)
outputs = model.generate(input_ids=inputs, max_new_tokens=200)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Data

### Domain Adaptation Data
To adapt the model to biomedical Spanish we used the following resources created and curated by the SINAI Research Group (Universidad de Jaén):

* **Continual Pre-training**
    * **Dataset:** `SINAI/ALIA-es-biomedical`
    * **Description:** A large collection of biomedical and clinical Spanish texts, including scientific literature, guidelines, and de-identified clinical narratives used to adapt the base model's language distribution to the biomedical domain.

### Original Pre-training Data (Base Model)
The underlying base model (Salamandra 7B) was pre-trained on 12.875 trillion tokens of highly curated data, covering 35 European languages and code. For a full detailed list of the original pre-training sources, please refer to the Original Salamandra Model Card.

---

## Additional Information

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Citation
```bibtex
@misc{ALIA-es-biomedical-7B-Base,
    title={ALIA Spanish Biomedical 7B Base Model},
    author={SINAI Research Group},
    year={2026},
    publisher={HuggingFace},
    howpublished={\url{https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-7B-Base}}
}
```

Please also cite the base models:

```bibtex
@misc{gonzalezagirre2025salamandratechnicalreport,
      title={Salamandra Technical Report}, 
      author={Aitor Gonzalez-Agirre and Marc Pàmies and Joan Llop and Irene Baucells and Severino Da Dalt and Daniel Tamayo and José Javier Saiz and Ferran Espuña and Jaume Prats and Javier Aula-Blasco and Mario Mina and Adrián Rubio and Alexander Shvets and Anna Sallés and Iñaki Lacunza and Iñigo Pikabea and Jorge Palomar and Júlia Falcão and Lucía Tormo and Luis Vasquez-Reina and Montserrat Marimon and Valle Ruíz-Fernández and Marta Villegas},
      year={2025},
      eprint={2502.08489},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.08489}, 
}
```

### Funding
This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project [ALIA](https://alia.gob.es).

### Acknowledgments  
Training of this model was conducted thanks to [BSC](https://www.bsc.es/es) (Barcelona Supercomputing Center) on [MareNostrum 5](https://www.bsc.es/ca/marenostrum/marenostrum-5), a pre-exascale EuroHPC supercomputer hosted and operated by them.

---

**Contact:** [ALIA Project](https://www.alia.gob.es/) - [SINAI Research Group](https://sinai.ujaen.es) - [Universidad de Jaén](https://www.ujaen.es/)

**More Information:** [SINAI Research Group](https://sinai.ujaen.es) | [ALIA-UJA Project](https://github.com/sinai-uja/ALIA-UJA)