---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
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
  - clinical-ner
  - llama
  - llama-3.1
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

# Med-LLaMA3.1-8B — Medical (merged, standalone)

> A full, ready-to-use medical model: **Llama-3.1-8B** adapted to the medical domain with **QLoRA**, with
> the LoRA weights **merged back into the base**. Load it directly with `transformers` — no adapter, no
> PEFT, no extra steps. For the lightweight LoRA-adapter version (apply on top of the base yourself), see
> the link below.

This is the **8B (high-capacity flagship)** member of the **Med-LLaMA3** family introduced in the paper
*“Med-LLaMA3: Advancing Medical Question-Answering Through Parameter-Efficient Fine-Tuning of Large
Language Models”* (Applied Sciences, 2026). The family adapts the LLaMA-3 architecture to the medical
domain by training only a small fraction of the base model’s parameters (**4.01% for this 8B variant**),
achieving strong medical question-answering performance while keeping the memory footprint low — enabling
development and inference on low-cost, consumer-grade hardware.

The 8B variant is the **high-capacity model for complex clinical reasoning**. It attains a **mean
accuracy of 75.71%** across the eight MMLU medical subsets and performs **comparably to the
institutionally trained LLaMA3-Med42-8B** at the same scale, while being trained on consumer-grade GPUs.

- 📄 **Paper:** [Med-LLaMA3 (Applied Sciences 2026, 16(12), 6158)](https://www.mdpi.com/2076-3417/16/12/6158) · DOI: [10.3390/app16126158](https://doi.org/10.3390/app16126158)
- 💻 **Code:** [github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers)
- 🧩 **LoRA-adapter version:** [`MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned`](https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned)

---

## Model details

| | |
|---|---|
| **This model** | Standalone, merged checkpoint (base + medical LoRA, fused) |
| **Base model** | [`meta-llama/Llama-3.1-8B-Instruct`](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) |
| **How it was made** | QLoRA fine-tuning (4-bit NF4 base + LoRA, `r=128`, `α=256`, all linear layers), then `merge_and_unload()` into the base |
| **Trainable parameters (fine-tuning)** | 335.54 M = **4.01%** of the 8.36 B total (base frozen during training) |
| **Released weights** | Full precision (fp16/bf16; not quantized) |
| **Parameters** | ~8.03 B |
| **Architecture** | 32 decoder layers · hidden size 4096 · intermediate size 14,336 · GQA (32 query heads, 8 KV heads) |
| **Context window** | 128K tokens |
| **Vocabulary** | 128,256 tokens |
| **Language** | English |
| **License** | [Llama 3.1 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE) |

> **Adapter vs. merged.** This repo is the **merged** model — the medical LoRA is already fused into the
> weights, so you load it like any standard causal-LM. If you instead want the small (~MB) adapter to
> apply on top of `meta-llama/Llama-3.1-8B-Instruct` yourself, use the
> [adapter repo](https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned). Both
> produce identical outputs. Note: the 8B uses LLaMA **3.1**, not 3.2.

---

## Intended uses

**Primary use cases**

- Medical **question answering** (multiple-choice and open-ended) — the highest-accuracy variant in the family.
- Clinical knowledge lookup and **clinical decision support** assistance.
- **Clinical named-entity recognition** (Disease / Procedure extraction) — see results below.
- Clinical documentation assistance and literature synthesis (with physician review).
- A research baseline for parameter-efficient fine-tuning of LLaMA models in healthcare.

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

MODEL = "MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged"

pipe = pipeline("text-generation", model=MODEL, torch_dtype="auto", device_map="auto")

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

MODEL = "MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype="auto", device_map="auto")
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

### Low-memory 4-bit inference (recommended; ~5 GB GPU memory)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
# pip install -U bitsandbytes

MODEL = "MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged"

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
gradient accumulation are scaled to each model’s memory footprint. The settings below are for the **8B**
variant.

| Setting | Value (8B) |
|---|---|
| Method | QLoRA (4-bit NF4 base, LoRA adapters in higher precision) → merged into base |
| LoRA `r` / `α` / dropout / bias | 128 / 256 / 0.05 / none |
| Target modules | All linear layers (q, k, v, o, gate, up, down) |
| Trainable params | 335.54 M (4.01% of 8.36 B) |
| Quantization (training) | 4-bit NF4 with double quantization (bitsandbytes) |
| Optimizer | Paged AdamW 8-bit (β₁ = 0.9, β₂ = 0.999), weight decay 0.1 |
| Learning rate / schedule | 2.0 × 10⁻⁵ / cosine annealing, 5 warmup steps |
| Epochs | 5 |
| Max sequence length | 4096 |
| Batch size / grad accumulation | 1 per device / 4 steps |
| Max gradient norm | 1.0 |
| Precision & memory | float16 · gradient checkpointing (no DeepSpeed / FlashAttention — unsupported on T4) |
| Hardware | 2 × NVIDIA T4 (30 GB total, free-tier Kaggle); ~15–25 days per run |
| Experiment tracking | Weights & Biases |

---

## Evaluation

All re-run models (including the baselines) were evaluated with the **EleutherAI LM Evaluation Harness**
under identical conditions: same harness version (v0.4.2), identical prompt templates, and **5-shot**
prompting. Reported `±` values are **95% bootstrap confidence intervals** (1000 resamples); statistical
significance uses **McNemar’s test** on per-item paired correctness. The merged model is functionally
identical to the base + adapter, so all scores below apply to both.

### MMLU medical subsets (5-shot accuracy %)

Comparison against the institutionally trained **LLaMA3-Med42-8B** under identical conditions
(this is the comparison visualized in Figure 3 of the paper). Family context: mean accuracy scales with
size — **1B = 48.64%**, **3B = 64.24%**, **8B = 75.71%**.

| MMLU medical subset | Med-LLaMA3.1-8B (Ours) | LLaMA3-Med42-8B |
|---|---|---|
| Anatomy | **71.11** (±3.92) | 69.63 (±3.97) |
| Clinical Knowledge | **79.62** (±2.48) | 76.60 (±2.61) |
| College Biology | **84.03** (±3.06) | 81.25 (±3.26) |
| College Medicine | **67.63** (±3.57) | 67.05 (±3.58) |
| Medical Genetics | **84.00** (±3.68) | 76.00 (±4.29) |
| Nutrition | **83.66** (±2.12) | 72.88 (±2.55) |
| Professional Medicine | **77.21** (±2.55) | 75.00 (±2.63) |
| Virology | **58.43** (±3.84) | 49.40 (±3.89) |
| **Mean (8 subsets)** | **75.71** | 71.10 |

**Statistical interpretation (honest framing):**
- vs. **`Llama-3.1-8B-Instruct`** (untuned base): improvements are statistically significant on Anatomy
  (p=0.021), Clinical Knowledge (p=0.003), Medical Genetics (p<0.001), Nutrition (p<0.001), and
  Professional Medicine (p=0.008); College Biology (p=0.11) and College Medicine (p=0.43) are not
  significant. After **Bonferroni correction** across the eight subsets (per-subset threshold 0.00625),
  Clinical Knowledge, Medical Genetics, and Nutrition remain significant; Anatomy and Professional
  Medicine are significant only before correction.
- vs. **`LLaMA3-Med42-8B`** (institutionally trained): differences are **not statistically significant**
  — i.e., **comparable performance**, not demonstrated superiority, at the same parameter scale.

### Medical QA benchmarks (5-shot accuracy %)

| Model | MedMCQA | MedQA | PubMedQA |
|---|---|---|---|
| **Med-LLaMA3.1-8B (Ours)** | **61.8** (±0.75) | 62.4 (±1.37) | **77.0** (±1.96) |
| LLaMA3-Med42-8B | 60.3 (±0.76) | **62.8** (±1.36) | **77.0** (±1.88) |
| Llama-3.1-8B-Instruct | 59.6 (±0.76) | 61.9 (±1.36) | 75.8 (±1.92) |
| MedGemma-4B-it | 32.2 (±0.72) | 27.7 (±1.26) | 55.2 (±2.23) |

The **+2.2-point gain on MedMCQA over `Llama-3.1-8B-Instruct` is statistically significant** (p=0.004).
The difference vs. `LLaMA3-Med42-8B` on MedMCQA is not significant (p=0.38). On MedQA and PubMedQA the
models are statistically tied.

### Clinical named-entity recognition (zero-shot, 100 MIMIC-III discharge summaries)

Dual-annotator gold standard, inter-rater agreement **κ = 0.87**.

| Entity type | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Disease | 0.94 | 0.91 | 0.92 | 847 |
| Procedure | 0.97 | 0.93 | 0.95 | 463 |
| **Macro avg** | **0.96** | **0.92** | **0.94** | 1310 |

### Efficiency (4-bit inference)

Approximately **3.58 GB** model size and **~5.2 GB** GPU memory allocated at inference, ~**30 tokens/s**,
with ~20 ms first-token latency — comparable to other 8B 4-bit baselines and well within consumer-GPU
budgets.

See the [paper](https://www.mdpi.com/2076-3417/16/12/6158) for full tables, generation-quality metrics,
expert evaluation, and the safety analysis.

---

## Limitations & responsible use

- **Not a medical device.** This model is a research artifact. It must **not** be used for autonomous
  diagnosis, treatment, prescribing, or any decision affecting patient care without review by a
  qualified healthcare professional. In expert review of 100 generative cases, 94% were rated “Good” but
  **6% contained critical errors** — underscoring the need for human verification.
- **Comparable, not superior.** Against the institutionally trained `LLaMA3-Med42-8B`, differences are
  not statistically significant; gains over the untuned base are significant on some subsets but not all
  (see above). On MedQA and PubMedQA there is no significant advantage.
- **Hallucination & over-elaboration.** The model can produce fluent but incorrect information and tends
  to elaborate beyond the question, which may obscure key points in time-sensitive settings.
- **Abbreviation ambiguity.** A known high-severity error source. The paper’s safety pilot shows that
  **context-disambiguation preprocessing** reduces abbreviation-ambiguity errors from 30% to 10% on a
  held-out set; consider applying similar preprocessing.
- **Data & bias.** Training data may under-represent certain populations, conditions, or regional
  practices, and may encode biases present in the source corpora. Rare-condition coverage is limited.
- **Privacy & compliance.** Do not input protected health information (PHI) unless your deployment is
  appropriately secured and compliant with applicable regulations (e.g., HIPAA, GDPR).
- **Evaluation scope.** Benchmarks are English-only and dominated by multiple-choice formats; long-form
  reasoning, multi-turn dialogue safety, non-English text, and out-of-distribution robustness are not
  evaluated.

**Recommended deployment:** clinical decision *support* (not autonomous decisions), educational tool,
documentation assistant (with physician review), and literature synthesis.

---

## License

This model is released under the **[Llama 3.1 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE)**,
inherited from the base model. By using it you agree to Meta’s Llama 3.1 license terms and
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
| Med-LLaMA3.2-3B | Merged | [`MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged`](https://huggingface.co/MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged) |
| Med-LLaMA3.1-8B | Adapter | [`MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned`](https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned) |
| **Med-LLaMA3.1-8B** | **Merged** | **this repo** — [`MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged`](https://huggingface.co/MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged) |

**Fine-tuning dataset:** [`MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset`](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset)