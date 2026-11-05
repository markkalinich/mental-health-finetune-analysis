---
license: apache-2.0
base_model: google/txgemma-2b-predict
tags:
- drug-discovery
- molecular-modeling
- cheminformatics
- biomedical
- pharmaceutical
- ADMET
- clinical-trials
- fine-tuned
- gemma
datasets:
- OussamaEL/drug-discovery-dataset
language:
- en
library_name: transformers
pipeline_tag: text-generation
model-index:
- name: IbnSinna-2B-Pharma
  results:
  - task:
      type: text-generation
      name: Binary Classification
    dataset:
      type: tdc
      name: ClinTox (Toxicity)
    metrics:
    - type: accuracy
      value: 0.7333
      name: Accuracy
    - type: f1
      value: 0.3333
      name: F1 Score
    - type: precision
      value: 0.2222
      name: Precision
    - type: recall
      value: 0.6667
      name: Recall
  - task:
      type: text-generation
      name: Regression
    dataset:
      type: tdc
      name: ESOL (Aqueous Solubility)
    metrics:
    - type: rmse
      value: 3.0534
      name: RMSE
    - type: mae
      value: 2.5694
      name: MAE
  - task:
      type: text-generation
      name: Conditional Generation
    dataset:
      type: custom
      name: Scaffold-based (Benzene)
    metrics:
    - type: validity
      value: 0.90
      name: SMILES Validity Rate
    - type: uniqueness
      value: 1.00
      name: Molecule Uniqueness Rate
widget:
- text: "Molecule: COc1ccc(N2C(=O)C3c4[nH]c5ccc(C)cc5c4C4CCC(C(C)(C)C)CC4C3C2=O)cc1\nQuestion: Is this molecule clinically toxic?\nAnswer:"
  example_title: "Binary Classification"
- text: "Molecule: Cc1ccc(O)cc1\nQuestion: What is the aqueous solubility (logS)?\nAnswer:"
  example_title: "Regression"
- text: "Molecule Scaffold: c1ccccc1\nQuestion: Generate a novel molecule containing this scaffold.\nAnswer:"
  example_title: "Conditional Generation"
---

<div align="center">

<img src="Logo-IbnSinna.png" alt="IbnSinna-2B-Drug Logo" width="400" height="400" style="margin-bottom: 20px;"/>

<h1>🧪 IbnSinna-2B-Pharma: Drug Discovery Language Model</h1>


**Advanced Pharmaceutical AI for Molecular Discovery**

*🔬 Binary Classification • 📊 Regression • 🧬 Conditional Generation*

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow)](https://huggingface.co/OussamaEL/IbnSinna-2B-Pharma)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Base Model](https://img.shields.io/badge/Base-TXGemma--2B-purple)](https://huggingface.co/google/txgemma-2b-predict)

</div>

---

> 📌 **Note**: This model supersedes the earlier IbnSinna-2B-Drug model, which has been deprecated. Please use this version for all applications.

---

## 🎨 Model Overview

IbnSinna-2B-Pharma is a specialized language model fine-tuned for three core drug discovery tasks:

1. **Binary Classification**: Predicting a wide range of molecular properties with Yes/No answers, including ADMET properties (e.g., clinical toxicity, BBB permeability), bioactivity (e.g., BACE and HIV inhibition), and pathway interactions (e.g., stress response and nuclear receptor binding)
2. **Regression**: Predicting key quantitative physicochemical values, specifically aqueous solubility (logS) and hydration free energy.
3. **Conditional Generation**: Designing novel molecules by providing a chemical scaffold as a structural constraint.

Built on Google's TXGemma-2B architecture and fine-tuned on comprehensive pharmaceutical datasets, this model serves as a powerful tool for computational drug discovery and molecular property prediction.

**Important**: This model was trained as a plain text generator (not chat-based). Prompts should end with `\nAnswer:` and the model will complete the answer directly.

## 📈 Evaluation

The model was evaluated on samples from standard benchmark datasets (TDC: ClinTox, ESOL) and a custom generation task.

### **1. Binary Classification (ClinTox)**
- **Performance**: The model demonstrates a good ability to identify positive cases (Recall: 66.7%) but does so at the cost of a high false-positive rate (Precision: 22.2%). This makes it suitable for initial screening where missing a potentially toxic compound is more critical than misidentifying a safe one.
- **Metrics**:
  - **Accuracy**: 73.3%
  - **F1 Score**: 33.3%

### **2. Regression (ESOL Solubility)**
- **Performance**: The model correctly understands the task and provides formatted numerical output. However, its quantitative accuracy is low (MAE: 2.57) compared to specialized regression models. It should be used for qualitative estimation rather than precise value prediction.
- **Metrics**:
  - **RMSE**: 3.05
  - **MAE**: 2.57

### **3. Conditional Generation (Scaffold-based)**
- **Performance**: The model excels at this task when using sampling-based decoding. It generates a high rate of chemically valid and unique molecules, demonstrating a strong ability to explore chemical space.
- **Metrics**:
  - **SMILES Validity Rate**: 90.0%
  - **Molecule Uniqueness Rate**: 100.0%

## 🚀 Quick Start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "OussamaEL/IbnSinna-2B-Pharma",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("OussamaEL/IbnSinna-2B-Pharma")

def ask(prompt, max_new_tokens=32, do_sample=False):
    """
    Queries the model. Use do_sample=True for generative tasks.
    """
    text = f"{prompt}\nAnswer:"
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    
    outputs = model.generate(
        **inputs, 
        max_new_tokens=max_new_tokens, 
        do_sample=do_sample,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.8 if do_sample else None,
        top_k=50 if do_sample else None
    )
    
    # Decode and extract the answer part
    generated_text = tokenizer.decode(outputs, skip_special_tokens=True)
    try:
        answer = generated_text.split("Answer:").strip()
    except IndexError:
        answer = "Could not parse answer."
    return answer

# Example: HIV Inhibitor Classification (Greedy Decoding)
prompt = "Molecule: COc1ccc(N2C(=O)C3c4[nH]c5ccc(C)cc5c4C4CCC(C(C)(C)C)CC4C3C2=O)cc1\nQuestion: Is this molecule an HIV inhibitor?"
print(ask(prompt, max_new_tokens=5, do_sample=False))

# Example: Molecule Generation (Sampling)
prompt_gen = "Molecule Scaffold: c1ccccc1\nQuestion: Generate a novel molecule containing this scaffold."
print(ask(prompt_gen, max_new_tokens=100, do_sample=True))
```

## 🎯 Model Capabilities

The model excels at three primary tasks:

### 1️⃣ **Binary Classification**
Predicting molecular properties with Yes/No outcomes:
- **Clinical Toxicity:** Predicting adverse effects and safety profiles (from ClinTox).
- **BACE Inhibition:** β-secretase 1 inhibitor prediction (from BACE).
- **HIV Inhibition:** Antiviral activity prediction (from HIV).
- **Stress Response Pathways:** Activation of pathways like ARE, HSE, and p53 (from Tox21).
- **Nuclear Receptor Binding:** Ligand prediction for receptors like ER, AR, and AhR (from Tox21).
- **ADMET Properties:** Blood-Brain Barrier (BBB) permeability (from BBBP).

### 2️⃣ **Regression** 
Predicting quantitative molecular properties:

- **Aqueous Solubility (logS):** Water solubility prediction (from ESOL).
- **Hydration Free Energy:** Calculating the free energy of solvation in water (from FreeSolv).

### 3️⃣ **Conditional Generation**
Designing novel molecules based on constraints:

- **Scaffold-based Design:** Generating novel molecules that contain a specific user-provided core structure or scaffold.

## 💻 Detailed Usage Examples

### Classification Tasks

```python
classification_prompts = [
    "Analyze Oc1ccc(Cl)c(Cl)c1 and determine if it is a stress response pathway ARE activator.",
    "Analyze COc1ccccc1NC(=O)CC(C)=O and determine if it is a nuclear receptor AhR ligand.",
    "Analyze CC[C@H]1C[C@H]2[C@@H]3CCC4=CC(=O)CC[C@@H]4[C@H]3CC[C@]2(C)[C@H]1O and determine if it is a nuclear receptor AR ligand."
]

for prompt in classification_prompts:
    text = prompt + "\nAnswer:"
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=5,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )
    
    gen = outputs[0, inputs["input_ids"].shape[1]:]
    answer = tokenizer.decode(gen, skip_special_tokens=True).strip().split()[0]  # Get first word (Yes/No)
    print(f"Q: {prompt[:50]}...")
    print(f"A: {answer}\n")
```

### Molecule Generation

```python
generation_prompts = [
    "Design a molecule containing the core structure O=C1Nc2ccccc2Oc2ccccc21.",
    "Design a molecule containing the core structure c1ccc2c(c1)Cc1ccccc1N2.",
    "Generate a molecule based on the scaffold c1ccccc1."
]

for prompt in generation_prompts:
    text = prompt + "\nAnswer:"
    inputs = tokenizer(text, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        temperature=0.7,
        do_sample=True,
        top_p=0.95
    )
    
    gen = outputs[0, inputs["input_ids"].shape[1]:]
    smiles = tokenizer.decode(gen, skip_special_tokens=True).strip()
    print(f"Scaffold: {prompt}")
    print(f"Generated: {smiles}\n")
```

### Property Prediction

```python
property_prompts = [
    "What is the predicted aqueous solubility (logS) of CCCCCCCO?",
    "What is the predicted aqueous solubility (logS) of Cc1ccc(O)cc1?"
]

for prompt in property_prompts:
    text = prompt + "\nAnswer:"
    inputs = tokenizer(text, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
    outputs = model.generate(**inputs, max_new_tokens=10, do_sample=False)
    gen = outputs[0, inputs["input_ids"].shape[1]:]
    value = tokenizer.decode(gen, skip_special_tokens=True).strip()
    print(f"Molecule: {prompt.split('of ')[-1].replace('?', '')}")
    print(f"Predicted logS: {value}\n")
```

## 🔧 Technical Specifications

### Model Architecture
- **Base Model**: Google's TXGemma-2B-predict
- **Parameters**: ~2.5B (2,635,108,608 total)
- **Fine-tuning Method**: QLoRA (4-bit NF4 + bf16 compute) → Full model merge to FP16
- **LoRA Config**: r=8, alpha=16, dropout=0.05
- **Target Modules**: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Training Precision**: 4-bit NF4 with bf16 compute dtype
- **Released Precision**: FP16 (merged model)

### Training Details
- **Optimizer**: Paged AdamW 8-bit
- **Learning Rate**: 1e-4 with cosine scheduler
- **Effective Batch Size**: 4
- **Warmup Steps**: 20
- **Max Sequence Length**: 256-512 tokens (recommend 256 for short prompts)
- **Training Framework**: HuggingFace Transformers + PEFT + TRL

### Dataset Information
The model was trained on a custom-built dataset aggregated from MoleculeNet.

- **Source:** MoleculeNet (Tox21, ClinTox, BBBP, HIV, BACE, ESOL, FreeSolv)
- **Training Samples:** 33,179
- **Training Task Distribution (approximate):**
  - **~53%** Classification
  - **~44%** Generation
  - **~3%** Regression

## ⚠️ Limitations and Ethical Considerations

### Intended Use
- ✅ **Research and Development**: Drug discovery research, lead optimization
- ✅ **Educational Purposes**: Teaching molecular modeling concepts
- ✅ **Screening Tools**: Initial compound screening and prioritization
- ❌ **NOT for Clinical Decisions**: Do not use for patient treatment decisions
- ❌ **NOT for Final Validation**: Always require wet-lab validation

### Known Limitations
1.  **Low Quantitative Accuracy**: The model's predictions on regression tasks (e.g., LogS) are not precise and should be treated as qualitative estimates.
2.  **High False-Positive Rate in Classification**: The model tends to be overly cautious in toxicity prediction, leading to a high rate of false positives.
3.  **Imperfect Prompt Adherence**: In generation tasks, the model may occasionally produce molecules that do not perfectly adhere to all structural constraints (e.g., including a required scaffold).
4.  **Dataset Biases**: The model's knowledge is limited to the chemical space and biases present in the MoleculeNet datasets it was trained on.
5.  **SMILES-based**: The model operates on 1D SMILES strings and does not reason about 3D molecular conformations.

### Ethical Guidelines
- Always validate predictions experimentally
- Consider potential biases in drug discovery pipelines
- Ensure equitable application across different populations
- Respect intellectual property in molecular design

## 📚 Citation

If you use this model in your research, please cite:

```bibtex
@model{ibnsinna_2b_pharma_2025,
  title={IbnSinna-2B-Pharma: Drug Discovery Language Model},
  author={Oussama El Allam},
  year={2025},
  month={August},
  url={https://huggingface.co/OussamaEL/IbnSinna-2B-Pharma},
  note={Fine-tuned TXGemma-2B for pharmaceutical and drug discovery applications},
  publisher={Hugging Face}
}
```

## 🤝 Acknowledgments

- Google DeepMind for the TXGemma base model
- The drug discovery and cheminformatics community
- Contributors to the training datasets


## 🔗 Links

- **Model**: [IbnSinna-2B-Pharma](https://huggingface.co/OussamaEL/IbnSinna-2B-Pharma)
- **Base Model**: [TXGemma-2B-predict](https://huggingface.co/google/txgemma-2b-predict)
- **Dataset**: [OussamaEL/drug-discovery-dataset](https://huggingface.co/datasets/OussamaEL/drug-discovery-dataset)

---

<div align="center">

**Made with 🧬 for the Drug Discovery Community**

*Advanced Pharmaceutical AI for Next-Generation Drug Development*

</div>
