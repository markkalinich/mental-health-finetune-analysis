---
license: llama3.2
base_model: meta-llama/Llama-3.2-1B
tags:
- medical
- healthcare
- knowledge-distillation
- distillation
- llama
- llama-3.2
- lightweight
- clinical-nlp
datasets:
- MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset
language:
- en
pipeline_tag: text-generation
library_name: transformers
---

# distil_Med42_8B_Llama-3.2-1B

**A 1B-parameter medical language model distilled from [Llama3-Med42-8B](https://huggingface.co/m42-health/Llama3-Med42-8B) into a [Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) student**, using the framework from the paper *"DistilLLM-Med: A Lightweight Medical Language Model through Knowledge Distillation"* (IEEE ICICIS 2025).

- 📄 **Paper**: [IEEE Xplore, document 11313220](https://ieeexplore.ieee.org/document/11313220/)
- 💻 **Training notebook**: [`Train_Distil_Med42_LLama_Transformer.ipynb`](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/DistilLLM-Med%20A%20Lightweight%20Medical%20Language%20Model%20through%20Knowledge%20Distillation/Training/Train_Distil_Med42_LLama_Transformer.ipynb)
- 🗂️ **Training data**: [MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset)
- 👨‍🏫 **Teacher**: [m42-health/Llama3-Med42-8B](https://huggingface.co/m42-health/Llama3-Med42-8B) (8.03B params)
- 🎓 **Student base**: [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) (1.24B params)

## About the paper

**DistilLLM-Med: A Lightweight Medical Language Model through Knowledge Distillation**
Mohamed Abo El-Enen, Sally Saad, Taymoor Nazmy — Faculty of Computer and Information Sciences, Ain Shams University, Cairo, Egypt.
Published in *2025 IEEE Twelfth International Conference on Intelligent Computing and Information Systems (ICICIS)*.
[IEEE Xplore](https://ieeexplore.ieee.org/document/11313220/)

The paper distills medical expertise from two specialized teacher models — **MedGemma-4B** (referred to as "MedGemini-4B" in the paper text, citing Sellergren et al.'s MedGemma technical report) and **Llama3-Med42-8B** — into a single lightweight **LLaMA 3.2-1B** student, using temperature-scaled KL-divergence distillation, specialty-weighted losses, and attention-map alignment. The resulting student retains **89.3%** of teacher token-level accuracy while cutting parameters by **75%**, reaching **47.7%** average accuracy on MMLU-Medical (**67.8%** of the Med42-8B teacher's 72.6%) and **59.5 tokens/sec** inference throughput.

## Model family

This checkpoint is one of four sibling distilled models trained in this project, all with a Llama-3.2-1B student:

| Model | Teacher | Student base | Notebook |
|---|---|---|---|
| [distil_med42_8B_Llama-3.2-1B-Instruct](https://huggingface.co/MohamedAhmedAE/distil_med42_8B_Llama-3.2-1B-Instruct) | Med42-8B | Llama-3.2-1B-**Instruct** | `Train_Distil_Med42_LLama_Transformer.ipynb` |
| **distil_Med42_8B_Llama-3.2-1B** (this model) | Med42-8B | Llama-3.2-1B | `Train_Distil_Med42_LLama_Transformer.ipynb` |
| [distil_llama_3_8B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_llama_3_8B_Llama-3.2-1B) | Meta-Llama-3-8B | Llama-3.2-1B | `Distil_LLama_LLama.ipynb` |
| [distil_MedGemma_4B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_MedGemma_4B_Llama-3.2-1B) | MedGemma-4B | Llama-3.2-1B | `Train_Distil_MedGemma_LLama.ipynb` |

## Method

Because Med42-8B and Llama-3.2-1B are both built on the Llama-3 tokenizer (128,256 shared vocabulary tokens), this run distills **directly on logits** with no vocabulary-projection layer needed (unlike the MedGemma run, which has a mismatched vocabulary).

The training objective combines four components, following the paper's Eq. (1)–(7):

1. **Temperature-scaled KL distillation** — `L_KD = α·L_CE(y, p_S) + (1-α)·L_KL(p_T^τ, p_S^τ)`, with `α = 0.7` (favoring the soft-label/KL term over the hard-label cross-entropy term).
2. **Progressive temperature scheduling** — softmax temperature `τ` decays exponentially from `τ₀ = 8` to `τ_final = 1` over the first 50,000 steps (`τ(t) = τ₀·exp(-γt)`), so the student first learns broad relationships between similar conditions before sharpening toward confident predictions.
3. **Specialty-weighted loss** — per-specialty weights `w_s` re-balance the KL loss across medical subdomains (e.g., cardiology vs. dermatology) so that no single specialty dominates training.
4. **Attention-map alignment** — an auxiliary Frobenius-norm loss `L_att` pulls the student's per-layer, per-head attention matrices toward the teacher's, so the student learns *where* the teacher looks (e.g., key symptoms in a vignette), not just *what* it outputs.

Total loss: `L_total = L_weighted + β·L_att + λ‖W_S‖²` (`β ≈ 0.1–0.3`, `λ` = weight decay).

### Training setup (from the paper)

| | |
|---|---|
| Hardware | 2× NVIDIA T4 (15GB each, ~30GB total) |
| Optimizer | AdamW, lr = 1e-6, weight decay = 0.01 |
| Batch size | 1 (+ gradient accumulation) |
| Precision | Teacher: 4-bit NF4 quantized (bitsandbytes, double quantization, fp16 compute) · Student: full fp16 |
| Temperature schedule | τ₀ = 8 → τ_final = 1, exponential decay over 50,000 steps |
| α (KD/CE balance) | 0.7 |
| Training extent | ~0.6 epoch over the unified corpus (per the paper) |
| Checkpoint on this Hub repo | Global step **80,118** (`save_every_steps = 5000`) |

Config as logged for this checkpoint on the Hub:
```json
{
  "alpha": 0.7, "temperature": 4, "accumulation_steps": 1, "hidden_dim": 1024,
  "learning_rate": 1e-06, "num_epochs": 10,
  "teacher_vocab_size": 128256, "student_vocab_size": 128256,
  "save_every_steps": 5000, "attention_distill": true, "feature_matching": true,
  "progressive_unfreezing": true, "adaptive_temperature": true, "layer_wise_distill": true,
  "attention_loss_weight": 0.05, "feature_loss_weight": 0.1,
  "min_temperature": 1.0, "max_temperature": 8.0, "unfreeze_schedule": "linear"
}
```

Full implementation (loss functions, projection layers, training loop) is in [`Train_Distil_Med42_LLama_Transformer.ipynb`](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/DistilLLM-Med%20A%20Lightweight%20Medical%20Language%20Model%20through%20Knowledge%20Distillation/Training/Train_Distil_Med42_LLama_Transformer.ipynb).

## Training data

The unified training corpus merges **18 established medical benchmarks** (~1.5–1.65M samples after cleaning) into a single instruction–response format, including:

- **MMLU** (medical subtasks) and **MedMCQA** — multiple-choice medical exam questions
- **PubMedQA** and **COVID-QA** — context-grounded biomedical QA
- **ChatDoctor** and **MIMIC-III** — real-world clinical dialogues and notes
- **Medical Meadow** and **MedQuAD** — structured instructional/expert-curated Q&A

Preprocessing deduplicated samples, truncated to a 1024-token limit, normalized medical abbreviations (via MeDAL mappings), and segmented long clinical notes (e.g., MIMIC-III) into coherent chunks. Benchmark **test sets were excluded from training** to keep evaluation fair. The processed/published version of this corpus is on the Hub as [Med_LLaMa3_fine-tuning_dataset](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset) (1.64M train / 14.4k validation rows), with an `instruction` / `input` / `context` / `output` / `choices` / `type` (`QA` / `MCQ` / `CASE`) schema.

## Results (from the paper)

The paper reports two distilled variants ("Experiment 1" and "Experiment 2") evaluated against both teachers and the untrained baseline. **The paper does not explicitly label which experiment number maps to which Hub checkpoint** — treat the numbers below as the project's overall benchmark results rather than a guaranteed one-to-one match with this specific file. Distilled "Experiment 1" is the paper's best/full-framework model.

**MMLU-Medical accuracy:**

| Task | LLaMA 3.2-1B (base) | MedGemma-4B | Llama3-Med42-8B | Distilled Exp. 1 | Distilled Exp. 2 |
|---|---|---|---|---|---|
| Anatomy | 49.6% | 23.0% | 74.1% | 51.1% | 49.6% |
| Clinical Knowledge | 35.9% | 22.6% | 75.1% | 49.1% | 44.5% |
| College Biology | 38.2% | 26.4% | 82.6% | 50.0% | 41.0% |
| College Medicine | 33.5% | 24.3% | 68.8% | 33.0% | 38.2% |
| Medical Genetics | 41.0% | 34.0% | 77.0% | 45.0% | 49.0% |
| Nutrition | 42.2% | 20.3% | 73.9% | 56.2% | 51.6% |
| Professional Medicine | 37.9% | 17.7% | 77.6% | 55.2% | 48.9% |
| Virology | 38.6% | 25.9% | 51.8% | 42.2% | 34.9% |
| **Average** | **39.6%** | **24.3%** | **72.6%** | **47.7%** | **44.7%** |

The best distilled model reaches **67.8%** of the Med42-8B teacher's accuracy and a **20.5%** relative improvement over the base LLaMA 3.2-1B.

**MedAlpaca (medical-meadow-medical-flashcards) generation quality:**

| Metric | Med42-8B | MedGemma-4B | LLaMA 3.2-1B (base) | Distilled Exp. 1 | Distilled Exp. 2 |
|---|---|---|---|---|---|
| ROUGE-1 | 0.310 | 0.178 | 0.171 | 0.212 | 0.209 |
| ROUGE-2 | 0.183 | 0.093 | 0.094 | 0.139 | 0.130 |
| ROUGE-L | 0.267 | 0.149 | 0.150 | 0.179 | 0.170 |
| BLEU | 0.071 | 0.026 | 0.026 | 0.037 | 0.034 |
| Token accuracy | 0.537 | 0.482 | 0.495 | 0.505 | 0.510 |

Average retention of the Med42-8B teacher's quality: **63.1%** (up to 76.1% on ROUGE-2).

**Compute efficiency:**

| Model | Params (B) | Memory (GB) | Speed (tok/s) | Latency (ms) |
|---|---|---|---|---|
| Llama3-Med42-8B (teacher) | 8.03 | 5.32 | 49.7 | 1006.0 |
| MedGemma-4B (teacher) | 4.97 | 9.75 | 33.6 | 1486.6 |
| LLaMA 3.2-1B (base) | 1.24 | 7.68 | 102.7 | 487.0 |
| **Distilled LLaMA 3.2-1B** | **1.24** | **7.68** | **59.5** | **841.0** |

**Ablation study** (contribution of each component, MMLU-Medical average):

| Variant | MMLU Acc. | Δ vs. base |
|---|---|---|
| LLaMA 3.2-1B (base) | 39.6% | – |
| A: Baseline KD | 42.3% | +2.7 |
| B: A + Progressive Temperature | 44.7% | +5.1 |
| C: B + Specialty Weighting | 46.5% | +6.9 |
| D: C + Attention Alignment (full model) | 47.7% | +8.1 |

Independent medical-expert review of 89 model answers found most responses (70/89) more detailed and context-rich than reference answers, but flagged 19/89 with critical factual errors (misdiagnoses, incorrect mechanisms) — underscoring that the model **requires expert oversight** and is not a standalone diagnostic tool.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "MohamedAhmedAE/distil_Med42_8B_Llama-3.2-1B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)

prompt = "What are some possible causes of low PTH and high calcium levels?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=200, do_sample=False)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

> This is a **base/completion-style** checkpoint (no chat template registered on the Hub). For chat-style interaction, see [distil_med42_8B_Llama-3.2-1B-Instruct](https://huggingface.co/MohamedAhmedAE/distil_med42_8B_Llama-3.2-1B-Instruct).

## Intended use & limitations

- Research use in efficient/lightweight medical NLP and knowledge-distillation studies; suitable for edge/low-resource deployment experiments.
- **Not a certified clinical tool.** The paper's own expert review found critical errors in ~21% of sampled answers (misdiagnoses, incorrect mechanisms). Always require qualified human oversight before acting on any output.
- Distillation training only reached ~0.6 epoch over the corpus — treat as a research checkpoint, not a fully converged production model.
- Inherits any biases present in the teacher model (Med42-8B) and in the 18-source training corpus.

## License

Released under the **Llama 3.2 Community License** (matches the student base, [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B)). Since Med42-8B was used as a distillation teacher, also review the license terms on [m42-health/Llama3-Med42-8B](https://huggingface.co/m42-health/Llama3-Med42-8B) (Llama 3 Community License family) before downstream/commercial use.

## Citation

```bibtex
@inproceedings{aboelenein2025distilllmmed,
  title     = {DistilLLM-Med: A Lightweight Medical Language Model through Knowledge Distillation},
  author    = {Abo El-Enen, Mohamed and Saad, Sally and Nazmy, Taymoor},
  booktitle = {2025 IEEE Twelfth International Conference on Intelligent Computing and Information Systems (ICICIS)},
  year      = {2025},
  publisher = {IEEE},
  url       = {https://ieeexplore.ieee.org/document/11313220/}
}
```