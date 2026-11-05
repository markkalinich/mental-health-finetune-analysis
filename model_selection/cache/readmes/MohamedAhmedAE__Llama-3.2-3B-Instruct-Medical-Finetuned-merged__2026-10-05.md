---
license: llama3.2
base_model: meta-llama/Llama-3.2-3B-Instruct
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
language:
  - en
tags:
  - medical
  - healthcare
  - clinical
  - clinical-decision-support
  - question-answering
  - medical-qa
  - llama
  - llama-3.2
  - qlora
  - parameter-efficient-fine-tuning
  - merged
datasets:
  - MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset
  - medalpaca/medical_meadow_medqa
  - medalpaca/medical_meadow_medical_flashcards
  - medalpaca/medical_meadow_wikidoc
  - medalpaca/medical_meadow_wikidoc_patient_information
  - medalpaca/medical_meadow_cord19
  - medalpaca/medical_meadow_pubmed_causal
  - openlifescienceai/medmcqa
  - bigbio/med_qa
  - qiaojin/PubMedQA
  - deepset/covid_qa_deepset
---

# Med-LLaMA3.2-3B — Medical (merged, standalone)

> A full, ready-to-use medical model: **Llama-3.2-3B** adapted to the medical domain with **QLoRA**, with
> the LoRA weights **merged back into the base**. Load it directly with `transformers` — no adapter, no
> PEFT, no extra steps. For the lightweight LoRA-adapter version (apply on top of the base yourself), see
> the link below.

This is the **3B (balanced / mid-tier)** member of the **Med-LLaMA3** family introduced in the paper
*“Med-LLaMA3: Advancing Medical Question-Answering Through Parameter-Efficient Fine-Tuning of Large
Language Models”* (Applied Sciences, 2026). The family adapts the LLaMA-3 architecture to the medical
domain by training only a small fraction of the base model’s parameters (**5.70% for this 3B variant**),
achieving strong medical question-answering performance while keeping the memory footprint low — enabling
development and inference on low-cost, consumer-grade hardware.

The 3B variant offers a **balanced trade-off between computational efficiency and capacity** — a
competitive mid-tier option with meaningfully better accuracy than the 1B and lower compute than the 8B.

- 📄 **Paper:** [Med-LLaMA3 (Applied Sciences 2026, 16(12), 6158)](https://www.mdpi.com/2076-3417/16/12/6158) · DOI: [10.3390/app16126158](https://doi.org/10.3390/app16126158)
- 💻 **Code:** [github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers)
- 🧩 **LoRA-adapter version:** [`MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned`](https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned)

---

## Model details

| | |
|---|---|
| **This model** | Standalone, merged checkpoint (base + medical LoRA, fused) |
| **Base model** | [`meta-llama/Llama-3.2-3B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) |
| **How it was made** | QLoRA fine-tuning (4-bit NF4 base + LoRA, `r=128`, `α=256`, all linear layers), then `merge_and_unload()` into the base |
| **Trainable parameters (fine-tuning)** | 194.51 M = **5.70%** of the 3.40 B total (base frozen during training) |
| **Released weights** | bfloat16 (full precision; not quantized) |
| **Parameters** | ~3.21 B |
| **Architecture** | 28 decoder layers · hidden size 3072 · intermediate size 8192 · GQA (24 query heads, 8 KV heads) |
| **Context window** | 128K tokens |
| **Vocabulary** | 128,256 tokens |
| **Language** | English |
| **License** | [Llama 3.2 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE) |

> **Adapter vs. merged.** This repo is the **merged** model — the medical LoRA is already fused into the
> weights, so you load it like any standard causal-LM. If you instead want the small (~MB) adapter to
> apply on top of `meta-llama/Llama-3.2-3B-Instruct` yourself, use the
> [adapter repo](https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned). Both
> produce identical outputs.

---

## Intended uses

**Primary use cases**

- Medical **question answering** (multiple-choice and open-ended).
- Clinical knowledge lookup and **clinical decision support** assistance.
- A balanced mid-tier option when the 1B is too small and the 8B is too heavy.
- A research baseline for parameter-efficient fine-tuning of small LLaMA models in healthcare.

**Out of scope / not intended for**

- Autonomous clinical decision-making or direct patient care without a qualified clinician in the loop.
- Generating definitive diagnoses, prescriptions, or treatment plans.
- Use as a substitute for professional medical advice, emergency services, or licensed care.

See **[Limitations & responsible use](#limitations--responsible-use)** before any applied use.

---

## How to use

This is a standalone model — load it directly, no adapter step required.

```bash
pip install -U transformers accelerate torch
```

### Quick start (`pipeline`)

```python
import torch
from transformers import pipeline

MODEL = "MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged"

pipe = pipeline("text-generation", model=MODEL, torch_dtype=torch.bfloat16, device_map="auto")

messages = [
    {"role": "system", "content": "You are a knowledgeable medical assistant. Answer accurately and concisely."},
    {"role": "user", "content": "What is the first-line treatment for uncomplicated community-acquired pneumonia in a healthy adult?"},
]
out = pipe(messages, max_new_tokens=256, do_sample=False)
print(out[0]["generated_text"][-1]["content"])
```

### Full control (`AutoModelForCausalLM`)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto")
model.eval()

messages = [
    {"role": "system", "content": "You are a knowledgeable medical assistant. Answer accurately and concisely."},
    {"role": "user", "content": "Explain the mechanism of action of metformin."},
]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)

with torch.no_grad():
    out = model.generate(inputs, max_new_tokens=256, do_sample=False, temperature=0.0)
print(tokenizer.decode(out[0][inputs.shape[-1]:], skip_special_tokens=True))
```

### Low-memory 4-bit inference

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
# pip install -U bitsandbytes

MODEL = "MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
)

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, quantization_config=bnb_config, device_map="auto")
```

---

## Training data

The Med-LLaMA3 family was fine-tuned on a curated **medical instruction dataset of over 1.5 million
samples**, organized along a three-axis taxonomy: **source type** (examination QA, clinical dialogue,
biomedical literature, encyclopedic reference) × **clinical granularity** (basic science, clinical
reasoning, patient communication) × **task format** (multiple-choice, open-ended QA, generative
dialogue). All sources were consolidated into a unified instruction–response schema
(`system`, `context`, `question`, `answer`, `choices`).

Sources include:

- **MedAlpaca / Medical Meadow** collection — MEDIQA, Medical Flashcards, WikiDoc, WikiDoc Patient
  Information, MedQA, CORD-19, and PubMed Causal subsets
- **MedMCQA** — Indian medical entrance exam (AIIMS & NEET PG) multiple-choice questions
- **MedQA-USMLE** — USMLE-style 4-option multiple-choice questions (English)
- **BigBIO MedQA** — standardized biomedical QA
- **PubMedQA** — research questions over PubMed abstracts (yes/no/maybe)
- **COVID-QA (deepset)** — COVID-19 / SARS-CoV-2 question answering
- **MedQuAD** — consumer-health QA compiled from authoritative NIH sources
- **HealthCareMagic** — real-world patient–doctor conversation transcripts

The data-cleaning and corpus-assembly scripts are released in the
[code repository](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers), and the final compiled
fine-tuning dataset is available at
[`MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset).

> **Evaluation integrity:** The eight **MMLU medical subsets** were used **only for held-out
> evaluation** and were **excluded** from the fine-tuning corpus. For benchmarks with official splits
> (MedMCQA, MedQA-USMLE, PubMedQA), only the official **training** partitions were used for fine-tuning.

---

## Training procedure

This model was produced by QLoRA fine-tuning followed by merging the adapter into the base. LoRA and
optimization settings are identical across the 1B, 3B, and 8B variants; sequence length, batch size, and
gradient accumulation are scaled to each model’s memory footprint. The settings below are for the **3B**
variant.

| Setting | Value (3B) |
|---|---|
| Method | QLoRA (4-bit NF4 base, LoRA adapters in higher precision) → merged into base |
| LoRA `r` / `α` / dropout / bias | 128 / 256 / 0.05 / none |
| Target modules | All linear layers (q, k, v, o, gate, up, down) |
| Trainable params | 194.51 M (5.70% of 3.40 B) |
| Quantization (training) | 4-bit NF4 with double quantization (bitsandbytes) |
| Optimizer | Paged AdamW 8-bit (β₁ = 0.9, β₂ = 0.999), weight decay 0.1 |
| Learning rate / schedule | 2.0 × 10⁻⁵ / cosine annealing, 5 warmup steps |
| Epochs | 5 |
| Max sequence length | 2048 |
| Batch size / grad accumulation | 4 per device / 16 steps |
| Max gradient norm | 1.0 |
| Precision & memory | bfloat16 · gradient checkpointing · DeepSpeed ZeRO-2 · FlashAttention-2 |
| Hardware | 2 × NVIDIA RTX 4050 (12 GB), ~30 days |
| Experiment tracking | Weights & Biases |

---

## Evaluation

Evaluation in the paper uses the **EleutherAI LM Evaluation Harness** with **5-shot** prompting on the
eight MMLU medical subsets (Anatomy, Clinical Knowledge, College Biology, College Medicine, Medical
Genetics, Nutrition, Professional Medicine, Virology). Reported comparisons include **McNemar’s test**
p-values and **95% bootstrap confidence intervals**.

The table below reports the 3B model’s 5-shot accuracy (%) on each MMLU medical subset, with 95%
bootstrap confidence intervals (1000 resamples), as published in Table 7 of the paper. For context, the
family’s mean accuracy scales with model size: **1B = 48.64%**, **3B = 64.24%**, **8B = 75.71%**.

| MMLU medical subset (5-shot) | Med-LLaMA3.2-3B (acc. %) |
|---|---|
| Anatomy | 59.52 (±4.26) |
| Clinical Knowledge | 68.17 (±2.89) |
| College Biology | 71.53 (±3.77) |
| College Medicine | 57.65 (±3.78) |
| Medical Genetics | 75.00 (±4.35) |
| Nutrition | 68.32 (±2.69) |
| Professional Medicine | 70.59 (±2.77) |
| Virology | 43.17 (±3.84) |
| **Mean (8 subsets)** | **64.24** |

> The merged model is functionally identical to the base + adapter, so these scores apply to both. The
> paper reports an untuned baseline only for the 8B model (vs. `Llama-3.1-8B-Instruct`); it does **not**
> include an untuned `Llama-3.2-3B` baseline on these subsets. See Table 7 of the paper for the full
> cross-model comparison (1B, 8B, and other ≤8B models) with statistical tests.

See the [paper](https://www.mdpi.com/2076-3417/16/12/6158) for full tables, statistical tests, and
confidence intervals.

---

## Limitations & responsible use

- **Not a medical device.** This model is a research artifact. It must **not** be used for autonomous
  diagnosis, treatment, prescribing, or any decision affecting patient care without review by a
  qualified healthcare professional.
- **Hallucination risk.** Like all LLMs, it can produce fluent but incorrect or fabricated medical
  information. Always verify outputs against authoritative sources.
- **Mid-tier capacity.** The 3B is a balanced variant; for the highest accuracy on complex clinical
  reasoning, prefer the 8B variant when resources allow. For the smallest footprint, the 1B is available.
- **Abbreviation ambiguity.** Medical abbreviations are a known error source. The paper’s safety pilot
  shows that **context-disambiguation preprocessing** reduces the highest-severity abbreviation
  errors (from 30% to 10% on a held-out set); consider applying similar preprocessing.
- **Data & bias.** Training data may under-represent certain populations, conditions, or regional
  practices, and may encode biases present in the source corpora.
- **Privacy & compliance.** Do not input protected health information (PHI) unless your deployment is
  appropriately secured and compliant with applicable regulations (e.g., HIPAA, GDPR).
- **English only.** Performance outside English is not evaluated.

---

## License

This model is released under the **[Llama 3.2 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE)**,
inherited from the base model. By using it you agree to Meta’s Llama 3.2 license terms and
Acceptable Use Policy. Review the licenses of the individual training datasets for any additional
restrictions on derived use.

---

## Citation

If you use this model, please cite the paper:

```bibtex
@article{aboelenen2026medllama3,
  title   = {Med-LLaMA3: Advancing Medical Question-Answering Through Parameter-Efficient Fine-Tuning of Large Language Models},
  author  = {Abo El-Enen, Mohamed Ahmed and Ismail, Sally S. and Nazmy, Taymoor Mohamed},
  journal = {Applied Sciences},
  volume  = {16},
  number  = {12},
  pages   = {6158},
  year    = {2026},
  publisher = {MDPI},
  doi     = {10.3390/app16126158},
  url     = {https://www.mdpi.com/2076-3417/16/12/6158}
}
```

## Authors & contact

Mohamed Ahmed Abo El-Enen, Sally S. Ismail, and Taymoor Mohamed Nazmy
Faculty of Computer and Information Sciences, Ain Shams University, Cairo, Egypt.

---

## Model family

| Variant | Type | Repository |
|---|---|---|
| Med-LLaMA3.2-1B | Adapter | [`MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned`](https://huggingface.co/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned) |
| Med-LLaMA3.2-1B | Merged | [`MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged`](https://huggingface.co/MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged) |
| Med-LLaMA3.2-3B | Adapter | [`MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned`](https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned) |
| **Med-LLaMA3.2-3B** | **Merged** | **this repo** — [`MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged`](https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged) |
| Med-LLaMA3.1-8B | Adapter | [`MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned`](https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned) |
| Med-LLaMA3.1-8B | Merged | [`MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged`](https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged) |

**Fine-tuning dataset:** [`MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset)