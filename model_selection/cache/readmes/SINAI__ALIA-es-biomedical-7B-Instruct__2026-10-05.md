---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- es
base_model:
- SINAI/ALIA-es-biomedical-7B-Base
datasets:
- SINAI/ALIA-es-biomedical-synthetic-instructions
tags:
- biomedical
- clinical
- spanish
---

# ALIA Spanish Biomedical 7B Instruct Model

## Model Description

**ALIA Spanish Biomedical 7B Instruct Model** is an instruction-tuned language model specialized in the biomedical and clinical domain for Spanish. This model is derived from [SINAI/ALIA-es-biomedical-7B-Base](https://huggingface.co/SINAI/ALIA-es-biomedical-7B-Base), which itself is based on the [Salamandra-7B](https://huggingface.co/BSC-LT/salamandra-7b) model family.

The model has been instruction-tuned using the [ALIA-es-biomedical-synthetic-instructions](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-synthetic-instructions) dataset, enabling it to assist users with biomedical and clinical queries in Spanish.

> [!WARNING]
> **DISCLAIMER:** This model is provided for research and educational purposes. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Users are responsible for ensuring their use of the model complies with applicable laws and regulations.
> As a result, it may generate harmful or inappropriate content, or medically inaccurate information. Users should verify any medical information generated against official sources.
> The SINAI Research Group and Barcelona Supercomputing Center shall not be held liable for any outcomes resulting from the use of this model.

### Model Lineage

```
Salamandra-7B (BSC-LT)
    ↓
ALIA-es-biomedical-7B-Base (SINAI)
    ↓
ALIA-es-biomedical-7B-Instruct (SINAI) ← This model
```

### Key Features

- **Specialized Domain**: Biomedical and clinical Spanish language
- **Instruction-Following**: Fine-tuned to respond to user queries and instructions
- **Foundation**: Built upon Salamandra-7B's multilingual capabilities, focused on Spanish
- **Open License**: Released under Apache 2.0 license

---

## Model Details

### Architecture

This model maintains the same architecture as its base model [ALIA-es-biomedical-7B-Base](https://huggingface.co/SINAI/ALIA-es-biomedical-7B-Base), which is derived from Salamandra-7B:

|                              |               |
|------------------------------|:--------------|
| **Base Model**               | Salamandra 7B |
| **Total Parameters**         | 7,768,117,248 |
| **Embedding Parameters**     | 1,048,576,000 |
| **Layers**                   | 32            |
| **Hidden size**              | 4,096         |
| **Attention heads**          | 32            |
| **Context length**           | 8,192         |
| **Vocabulary size**          | 256,000       |
| **Precision**                | bfloat16      |
| **Embedding type**           | RoPE          |
| **Activation Function**      | SwiGLU        |
| **Layer normalization**      | RMS Norm      |
| **Flash attention**          | ✅            |
| **Grouped Query Attention**  | ✅            |
| **Num. query groups**        | 8             |

### Training Details

**Instruction Tuning:**
- Training was conducted by SINAI Research Group (Universidad de Jaén)
- Dataset: [ALIA-es-biomedical-synthetic-instructions](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-synthetic-instructions)
- Language: Spanish
- Domain: Biomedical and clinical
- Number of samples: 328,071

**Training Infrastructure:**

Model SFT was trained on the [CALENDULA](https://www.scayle.es/) supercomputer hosted and operated by SCAYLE (Supercomputación Castilla y León) within the framework of the ALIA project.

The Genoa partition used for SFT training has the following specifications per node:
- 4x NVIDIA GPUs
- AMD EPYC processors
- NCCL distributed backend

The table below specifies the node configuration used for the supervised fine-tuning SFT:

| Phase | Nodes | GPUs | Training Time |
|-------|-------|------|---------------|
| SFT   | 2     | 8    | ~28h 23m      |

**Training Hyperparameters:**

Supervised Fine-Tuning was conducted using the [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) framework.

| Hyperparameter | Value |
|----------------|-------|
| Learning rate  | 1.4e-5 |
| Micro batch size | 8 |
| Gradient accumulation steps | 2 |
| Global batch size | 128 (using 8 GPUs) |
| Epochs         | 2     |
| LR Scheduler   | Cosine |
| Warmup steps   | 500   |
| Cosine min. LR ratio | 0.10 |
| NEFTune Noise Alpha | 5 |
| Sequence length | 8,192 |
| Optimizer      | adamw_torch_fused |
| Adam beta1     | 0.9   |
| Adam beta2     | 0.94  |
| Adam epsilon   | 1e-8  |
| Max grad norm  | 0.28  |
| Weight decay   | 0.003 |

---

## Intended Use

### Direct Use

This model is designed to assist users with questions and tasks related to the biomedical and clinical domains in Spanish. It can be used for:

- Answering biomedical and clinical queries
- Summarizing medical literature and clinical documentation
- Assisting with understanding clinical guidelines and pharmaceutical information
- General medical question answering and search support

---

## How to Use

### Inference

#### Basic Usage with Transformers

```bash
pip install transformers torch accelerate sentencepiece protobuf
```

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "SINAI/ALIA-es-biomedical-7B-Instruct"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16
)

# Example medical query
messages = [
    {"role": "user", "content": "¿Cuáles son los síntomas principales de la insuficiencia cardíaca congestiva?"}
]

# Format the input
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

# Generate response
outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.95,
    do_sample=True
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

#### Inference with vLLM

```bash
pip install vllm
```

```python
from vllm import LLM, SamplingParams

model_id = "SINAI/ALIA-es-biomedical-7B-Instruct"

# Create sampling parameters
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=512
)

# Initialize the model
llm = LLM(model=model_id)

# Example prompt
prompt = "¿Qué diferencias hay entre la diabetes tipo 1 y tipo 2?"

# Generate response
outputs = llm.generate([prompt], sampling_params)

for output in outputs:
    print(f"Generated text: {output.outputs[0].text}")
```

---

## Training Data

The model was instruction-tuned using the [ALIA-es-biomedical-synthetic-instructions](https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-synthetic-instructions) dataset created by the SINAI research group.

The training dataset has a total of 328,071 instructions, desglosed as follows:
- **Spanish Biomedical Domain**: 144,549
- **English Biomedical Domain**: 50,000
- **General Spanish**: 40,500
- **General English**: 30,000
- **Original Salamandra Instructions**: 63,022

---

## Evaluation

The model was evaluated on several clinical and biomedical benchmarks in Spanish to assess its adaptation to medical query understanding and answering.

### Evaluation Datasets

#### HeadQA (headqa_es)
- **Source**: [dvilares/head_qa](https://huggingface.co/datasets/dvilares/head_qa)
- **Description**: A question-answering dataset compiled from official exams for healthcare professionals in Spain (medicine, pharmacy, psychology, etc.).
- **Domain**: Spanish healthcare professional entry exams.

#### MMLU (Spanish Translation)
- **Source**: [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) (Spanish translation)
- **Description**: Spanish translations of MMLU medical and biological subjects, evaluated under two modalities: Selection (multiple-choice probabilistically evaluated) and Generative (free-form generation with exact match).
- **Domain**: Professional and academic knowledge in medicine, biology, and chemistry.

#### Examen de Medicina MIR
- **Description**: A collection of multiple-choice questions corresponding to official entrance exams for medical residency (MIR) in Spain, evaluating clinical reasoning capabilities on complex practical cases and questions with semantic distractors.
- **Domain**: Clinical reasoning and decision-making for medical doctors in Spain.

### Performance Metrics

The following tables show the evaluation results comparing **ALIA Spanish Biomedical 7B Instruct** (Finetuned) against the baseline **Salamandra 7B Instruct** (Original) model.

#### HeadQA Results

| Evaluation Metric | Salamandra 7B Instruct | ALIA Spanish Biomedical 7B Instruct | Absolute Difference |
| :--- | :---: | :---: | :---: |
| **Raw Accuracy (acc)** | **36.73%** | 33.73% | -3.00% |
| **Normalized Accuracy (acc_norm)** | **41.39%** | 38.18% | -3.21% |

#### MMLU Clinical and Biological Results (Selection vs. Generative)

| MMLU Subject | MMLU Selection (Original) | MMLU Selection (Finetuned) | MMLU Generative (Original) | MMLU Generative (Finetuned) |
| :--- | :---: | :---: | :---: | :---: |
| **Anatomy** | **48.89%** | 42.96% | **43.00%** | 36.00% |
| **Clinical Knowledge** | **55.47%** | 46.79% | **48.00%** | 32.00% |
| **College Biology** | **50.00%** | 45.14% | **45.00%** | 29.00% |
| **College Medicine** | **49.71%** | 40.46% | **41.00%** | 21.00% |
| **High School Biology** | **59.03%** | 44.84% | **40.00%** | 24.00% |
| **Human Aging** | **62.78%** | 49.78% | **43.00%** | 33.00% |
| **Medical Genetics** | **55.00%** | 44.00% | **48.00%** | 36.00% |
| **Nutrition** | **54.58%** | 47.71% | **40.00%** | 37.00% |
| **Professional Medicine** | 43.75% | **47.43%** | 22.00% | **24.00%** |
| **Virology** | **48.80%** | 45.18% | **37.00%** | 36.00% |

#### MMLU Generative Proxy Results (exact_match)

| MMLU Subject (Proxy) | Salamandra 7B Instruct | ALIA Spanish Biomedical 7B Instruct | Absolute Difference |
| :--- | :---: | :---: | :---: |
| **Proxy Biology** | **39.33%** | 8.23% | -31.10% |
| **Proxy Health** | **23.87%** | 6.84% | -17.03% |

#### Examen de Medicina MIR Results

| Task and Metric | Salamandra 7B Instruct | ALIA Spanish Biomedical 7B Instruct | Absolute Difference |
| :--- | :---: | :---: | :---: |
| **MIR MCQ Letter (acc)** | **38.69%** | 25.53% | -13.16% |
| **MIR MCQ Option Text (acc_norm)** | **35.25%** | 30.78% | -4.47% |
| **MIR MCQ Without Options (acc_norm)** | **34.37%** | 30.97% | -3.40% |

---

## Limitations and Biases

### Known Limitations

- **Domain Specificity**: While specialized in biomedical and clinical Spanish, the model may not perform optimally on general-purpose tasks.
- **Language**: Optimized for Spanish only.
- **Not Medical Advice**: Outputs must not be considered as professional medical advice, diagnosis, or treatment recommendations.
- **Training Data Constraints**: Performance is limited by the scope and quality of the training data.
- **Potential Hallucinations**: Like all language models, may generate plausible-sounding but incorrect or clinically unsafe information.

### Bias Considerations

- The model inherits potential biases from its base model (Salamandra-7B) and training data.
- Medical and clinical language may reflect biases present in scientific literature and medical guidelines.
- Users should be aware of potential biases when using the model for sensitive applications.
- We recommend additional bias testing and mitigation for specific use cases.

### Safety and Responsible Use

- **Human Oversight**: Always verify model outputs, especially for critical medical matters.
- **Professional Consultation**: Consult with qualified healthcare professionals for medical decisions.
- **Compliance**: Ensure use complies with applicable laws and regulations regarding AI systems.
- **Privacy**: Do not input sensitive personal health or confidential patient information.

---

## Additional Information

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Citation
```bibtex
@misc{ALIA-es-biomedical-7B-Instruct,
  title={ALIA Spanish Biomedical 7B Instruct Model},
  author={SINAI Research Group, Universidad de Jaén},
  year={2026},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-7B-Instruct}}
}
```

Please also cite the base models:

```bibtex
@misc{ALIA-es-biomedical-7B-Base,
  title={ALIA Spanish Biomedical 7B Base Model},
  author={SINAI Research Group, Universidad de Jaén},
  year={2026},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/datasets/SINAI/ALIA-es-biomedical-7B-Base}}
}
```

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
Training of this model was conducted thanks to [SCAYLE](https://www.scayle.es/) (Supercomputación Castilla y León) on the [CALENDULA](https://www.scayle.es/) supercomputer, within the framework of the ALIA project.

---

**Contact:** [ALIA Project](https://www.alia.gob.es/) - [SINAI Research Group](https://sinai.ujaen.es) - [Universidad de Jaén](https://www.ujaen.es/)

**More Information:** [SINAI Research Group](https://sinai.ujaen.es) | [ALIA-UJA Project](https://github.com/sinai-uja/ALIA-UJA)
