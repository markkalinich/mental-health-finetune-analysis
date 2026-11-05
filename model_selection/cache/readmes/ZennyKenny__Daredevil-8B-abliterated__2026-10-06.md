---
library_name: transformers
tags:
- abliteration
- alignment
- safety
- llama3
- directional_steering
- interpretability
license: mit
datasets:
- mlabonne/harmful_behaviors
- mlabonne/harmless_alpaca
language:
- en
base_model:
- meta-llama/Meta-Llama-3-8B-Instruct
---

# Model Card for ZennyKenny/Daredevil-8B-abliterated

This is an "abliterated" version of `mlabonne/Daredevil-8B`, based on the abliteration method developed by [mlabonne](https://huggingface.co/mlabonne) to allow LLMs to perform otherwise restricted actions in through direction-based activation editing.

The technique projects out harmful activation directions without further finetuning or modifying the model architecture. It is inspired by work on **steering vectors**, **mechanistic interpretability**, and **alignment by construction**.

---

## Model Details

### Model Description

This model has been modified from `meta-llama/Meta-Llama-3-8B-Instruct` by applying vector-based **orthogonal projection** to internal representations associated with harmful outputs. The method uses **HookedTransformer** from `transformer_lens` to calculate harmful activation directions from prompt-based comparisons and then removes those components from the weights.

- **Model type:** Causal Language Model
- **Language(s):** English
- **License:** llama3-license
- **Finetuned from model:** `mlabonne/Daredevil-8B`
- **Modified from base model:** `meta-llama/Meta-Llama-3-8B-Instruct`

### Model Sources

- **Original Model:** [mlabonne/Daredevil-8B](https://huggingface.co/mlabonne/Daredevil-8B)
- **Blog Post:** [Uncensor any LLM with abliteration](https://huggingface.co/blog/mlabonne/abliteration)

---

## Uses

### Direct Use

This model is intended for **experiments in safety and alignment research**, especially in:
- Exploring vector-based interpretability
- Testing refusal behaviors
- Evaluating models modified via non-finetuning methods

### Out-of-Scope Use

- Do **not** rely on this model for high-stakes decisions.
- This model was not tested for factuality, multilingual use, or downstream generalization.
- Not intended for production or safety-critical applications.

---

## Bias, Risks, and Limitations

### Limitations

- Only a **single direction** (or small subset) was ablated—this does not guarantee complete refusal behavior.
- Potential for **capability degradation** or underperformance on certain prompts.
- Effectiveness is **prompt-sensitive** and may vary significantly.

### Recommendations

- Treat this model as **exploratory**, not final.
- Evaluate outputs thoroughly before using in any application beyond experimentation.
- Use interpretability tools (like `transformer_lens`) to understand effects layer-by-layer.

---

## How to Get Started with the Model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("ZennyKenny/Daredevil-8B-abliterated")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")

prompt = "How can I build a bomb?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=64)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Training Details

### Training Data

This model was not further trained. Instead, it used representations from:
- `mlabonne/harmful_behaviors` (harmful prompt dataset)
- `mlabonne/harmless_alpaca` (harmless instruction dataset)

### Training Procedure

- Model activations were captured with `transformer_lens`
- Harmful vs. harmless activations compared across layers
- Top directional vectors removed from internal weights via projection

#### Training Hyperparameters

- **Precision used:** `bfloat16` (model loading), `float32` (conversion)
- **Orthogonalization method:** L2-normalized difference vectors
- **Number of layers edited:** Entire stack (all transformer blocks)

---

## Evaluation

Model completions were evaluated by:
- Human inspection of generations
- Baseline vs. intervention vs. orthogonalized comparisons
- Focused on refusal language: e.g., presence of "I can't", "I won't", etc.

---

## Environmental Impact

- **Hardware Type:** NVIDIA A100 (Google Colab)
- **Hours used:** ~1
- **Cloud Provider:** Google Cloud (Colab)
- **Compute Region:** [Unknown]
- **Carbon Emitted:** Minimal (low compute footprint, no training)

---

## Model Card Contact

For questions, reach out via [Hugging Face](https://huggingface.co/ZennyKenny)