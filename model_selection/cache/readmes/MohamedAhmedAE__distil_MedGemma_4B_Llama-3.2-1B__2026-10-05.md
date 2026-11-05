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
- cross-tokenizer
- clinical-nlp
datasets:
- MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset
language:
- en
pipeline_tag: text-generation
library_name: transformers
---

# distil_MedGemma_4B_Llama-3.2-1B

**A 1B-parameter medical language model distilled from [MedGemma-4B](https://huggingface.co/google/medgemma-4b-it) into a [Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) student**, using the framework from the paper *"DistilLLM-Med: A Lightweight Medical Language Model through Knowledge Distillation"* (IEEE ICICIS 2025), where this teacher is referred to as **"MedGemini-4B"** in the running text (the paper's own citation for it, [9], is Sellergren et al.'s MedGemma technical report).

- 📄 **Paper**: [IEEE Xplore, document 11313220](https://ieeexplore.ieee.org/document/11313220/)
- 💻 **Training notebook**: [`Train_Distil_MedGemma_LLama.ipynb`](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/DistilLLM-Med%20A%20Lightweight%20Medical%20Language%20Model%20through%20Knowledge%20Distillation/Training/Train_Distil_MedGemma_LLama.ipynb) (see also the earlier exploratory notebook [`Distil_Gemma_LLama.ipynb`](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/DistilLLM-Med%20A%20Lightweight%20Medical%20Language%20Model%20through%20Knowledge%20Distillation/Training/Distil_Gemma_LLama.ipynb))
- 🗂️ **Training data**: [MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset)
- 👨‍🏫 **Teacher**: MedGemma-4B (Gemma-3-based medical VLM, ~4.97B params; text-only knowledge distilled here)
- 🎓 **Student base**: [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B) (1.24B params)

## About the paper

**DistilLLM-Med: A Lightweight Medical Language Model through Knowledge Distillation**
Mohamed Abo El-Enen, Sally Saad, Taymoor Nazmy — Faculty of Computer and Information Sciences, Ain Shams University, Cairo, Egypt.
Published in *2025 IEEE Twelfth International Conference on Intelligent Computing and Information Systems (ICICIS)*.
[IEEE Xplore](https://ieeexplore.ieee.org/document/11313220/)

The paper distills medical expertise from two specialized teacher models — **MedGemma-4B** (referred to as "MedGemini-4B" in the paper text, citing Sellergren et al.'s MedGemma technical report) and **Llama3-Med42-8B** — into a single lightweight **LLaMA 3.2-1B** student, using temperature-scaled KL-divergence distillation, specialty-weighted losses, and attention-map alignment. The resulting student retains **89.3%** of teacher token-level accuracy while cutting parameters by **75%**, reaching **47.7%** average accuracy on MMLU-Medical (**67.8%** of the Med42-8B teacher's 72.6%) and **59.5 tokens/sec** inference throughput.

## Model family

| Model | Teacher | Student base | Notebook |
|---|---|---|---|
| [distil_med42_8B_Llama-3.2-1B-Instruct](https://huggingface.co/MohamedAhmedAE/distil_med42_8B_Llama-3.2-1B-Instruct) | Med42-8B | Llama-3.2-1B-**Instruct** | `Train_Distil_Med42_LLama_Transformer.ipynb` |
| [distil_Med42_8B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_Med42_8B_Llama-3.2-1B) | Med42-8B | Llama-3.2-1B | `Train_Distil_Med42_LLama_Transformer.ipynb` |
| [distil_llama_3_8B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_llama_3_8B_Llama-3.2-1B) | Meta-Llama-3-8B | Llama-3.2-1B | `Distil_LLama_LLama.ipynb` |
| **distil_MedGemma_4B_Llama-3.2-1B** (this model) | MedGemma-4B | Llama-3.2-1B | `Train_Distil_MedGemma_LLama.ipynb` |

## Method: cross-tokenizer distillation

Unlike the Med42-8B and Llama-3-8B runs, MedGemma is built on the **Gemma** tokenizer (vocabulary ≈ 262K tokens) while the student uses the **Llama-3** tokenizer (128,256 tokens). This is the one checkpoint in the project where teacher and student vocabularies **don't match**, so the paper's learnable vocabulary-projection layer is required:

```
proj(x) = W2(ReLU(W1·x + b1)) + b2
```
with `W1 ∈ R^(d_h × V_T)`, `W2 ∈ R^(V_S × d_h)`, and intermediate dimension `d_h = max(V_T, V_S)`, initialized with scaled Xavier init (`× 0.1`). An analogous projection (`proj_hidden(h_T) = W_p·h_T + b_p`) is used for layer-wise hidden-state distillation when hidden sizes differ. On this teacher/student pair the projection preserved **98.7%** of the teacher's information, measured via normalized mutual information (NMI) between teacher/student representations on 10,000 held-out medical text samples.

Beyond the projection layer, the same core objective as the rest of the project applies (paper Eq. 1–7):

1. **Temperature-scaled KL distillation** — `L_KD = α·L_CE(y, p_S) + (1-α)·L_KL(p_T^τ, p_S^τ)`, `α = 0.7`.
2. **Progressive temperature scheduling** — `τ₀ = 8 → τ_final = 1`, exponential decay over 50,000 steps.
3. **Specialty-weighted loss** — re-balances the KL loss across medical subdomains.
4. **Attention-map alignment** — Frobenius-norm loss pulling (projected) student attention maps toward the teacher's.

Total loss: `L_total = L_weighted + β·L_att + λ‖W_S‖²`.

### Training setup (from the paper)

| | |
|---|---|
| Hardware | 2× NVIDIA T4 (15GB each, ~30GB total) |
| Optimizer | AdamW, lr = 1e-6, weight decay = 0.01 |
| Batch size | 1 (+ gradient accumulation) |
| Precision | Teacher: 4-bit NF4 quantized (bitsandbytes, double quantization, fp16 compute) · Student: full fp16 |
| Temperature schedule | τ₀ = 8 → τ_final = 1, exponential decay over 50,000 steps |
| α (KD/CE balance) | 0.7 |
| Training extent | ~0.5 epoch over the unified corpus (MedGemma run, per the paper) |
| Checkpoint on this Hub repo | Global step **319,154** (`save_every_steps = 5000`) |

Config as logged for this checkpoint on the Hub:
```json
{
  "alpha": 0.7, "temperature": 4, "accumulation_steps": 1, "hidden_dim": 1024,
  "learning_rate": 1e-06, "num_epochs": 10,
  "teacher_vocab_size": 262208, "student_vocab_size": 128256,
  "save_every_steps": 5000, "attention_distill": true, "feature_matching": true,
  "progressive_unfreezing": true, "adaptive_temperature": true, "layer_wise_distill": true,
  "attention_loss_weight": 0.05, "feature_loss_weight": 0.1,
  "min_temperature": 1.0, "max_temperature": 8.0, "unfreeze_schedule": "linear"
}
```

Full implementation (vocabulary/hidden-state projection layers, loss functions, training loop) is in [`Train_Distil_MedGemma_LLama.ipynb`](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/DistilLLM-Med%20A%20Lightweight%20Medical%20Language%20Model%20through%20Knowledge%20Distillation/Training/Train_Distil_MedGemma_LLama.ipynb).

## Training data

The unified training corpus merges **18 established medical benchmarks** (~1.5–1.65M samples after cleaning) into a single instruction–response format, including:

- **MMLU** (medical subtasks) and **MedMCQA** — multiple-choice medical exam questions
- **PubMedQA** and **COVID-QA** — context-grounded biomedical QA
- **ChatDoctor** and **MIMIC-III** — real-world clinical dialogues and notes
- **Medical Meadow** and **MedQuAD** — structured instructional/expert-curated Q&A

Preprocessing deduplicated samples, truncated to a 1024-token limit, normalized medical abbreviations (via MeDAL mappings), and segmented long clinical notes into coherent chunks. Benchmark **test sets were excluded from training**. Published as [Med_LLaMa3_fine-tuning_dataset](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset) (1.64M train / 14.4k validation rows).

## Results (from the paper)

⚠️ Interestingly, in the paper's own MMLU-Medical table, **MedGemma-4B (the teacher) scores lower than the untrained 1B student baseline** (24.3% vs. 39.6% average) — the paper doesn't fully explain this, but it is likely an artifact of prompt-format/evaluation-harness mismatch for MedGemma's native (chat/multimodal) prompting conventions rather than a genuine capability gap. Treat MedGemma's raw MMLU numbers below with that caveat in mind; its much stronger showing on the generation-quality metrics (ROUGE/BLEU) below is more indicative of its underlying quality.

**MMLU-Medical accuracy:**

| Task | LLaMA 3.2-1B (base) | MedGemma-4B (teacher) | Llama3-Med42-8B | Distilled Exp. 1 | Distilled Exp. 2 |
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

**MedAlpaca (medical-meadow-medical-flashcards) generation quality — MedGemma is the strongest reference point here:**

| Metric | Med42-8B | MedGemma-4B (teacher) | LLaMA 3.2-1B (base) | Distilled Exp. 1 | Distilled Exp. 2 |
|---|---|---|---|---|---|
| ROUGE-1 | 0.310 | 0.178 | 0.171 | 0.212 | 0.209 |
| ROUGE-2 | 0.183 | 0.093 | 0.094 | 0.139 | 0.130 |
| ROUGE-L | 0.267 | 0.149 | 0.150 | 0.179 | 0.170 |
| BLEU | 0.071 | 0.026 | 0.026 | 0.037 | 0.034 |
| Prediction perplexity | 3.178 | **2.143** | 2.652 | 2.551 | 2.605 |
| Token accuracy | 0.537 | 0.482 | 0.495 | 0.505 | 0.510 |

**Compute efficiency:**

| Model | Params (B) | Memory (GB) | Speed (tok/s) | Latency (ms) |
|---|---|---|---|---|
| MedGemma-4B (teacher) | 4.97 | 9.75 | 33.6 | 1486.6 |
| Llama3-Med42-8B (teacher) | 8.03 | 5.32 | 49.7 | 1006.0 |
| LLaMA 3.2-1B (base) | 1.24 | 7.68 | 102.7 | 487.0 |
| **Distilled LLaMA 3.2-1B** | **1.24** | **7.68** | **59.5** | **841.0** |

The distilled student is **42.1% faster** than the MedGemma-4B teacher (59.5 vs. 33.6 tok/s) at roughly **1/4 the parameter count**.

**Ablation study** (MMLU-Medical average, cumulative components):

| Variant | MMLU Acc. | Δ vs. base |
|---|---|---|
| LLaMA 3.2-1B (base) | 39.6% | – |
| A: Baseline KD | 42.3% | +2.7 |
| B: A + Progressive Temperature | 44.7% | +5.1 |
| C: B + Specialty Weighting | 46.5% | +6.9 |
| D: C + Attention Alignment (full model) | 47.7% | +8.1 |

Independent medical-expert review of 89 model answers found most responses (70/89) more detailed and context-rich than reference answers, but flagged 19/89 with critical factual errors (misdiagnoses, incorrect mechanisms) — the model **requires expert oversight**.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "MohamedAhmedAE/distil_MedGemma_4B_Llama-3.2-1B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "What is the Kussmaul sign, and what causes it to occur?"}
]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(inputs, max_new_tokens=256, do_sample=False)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

> This repo has a chat template registered on the Hub. If you only need plain completion, drop `apply_chat_template` and pass a raw prompt string instead, as with the other sibling models.

## Intended use & limitations

- Research use in efficient/lightweight medical NLP, and specifically useful for studying **cross-tokenizer/cross-architecture knowledge distillation** (Gemma → Llama).
- **Not a certified clinical tool.** The paper's own expert review found critical errors in ~21% of sampled answers (misdiagnoses, incorrect mechanisms). Always require qualified human oversight before acting on any output.
- Distillation training only reached ~0.5 epoch over the corpus — treat as a research checkpoint, not a fully converged production model.
- The vocabulary-projection step, while preserving 98.7% NMI on held-out samples, is still a lossy compression of the teacher's much larger 262K-token vocabulary into the student's 128K-token space; some MedGemma-specific tokenization nuances may not transfer.
- Inherits any biases present in the teacher model (MedGemma-4B) and in the 18-source training corpus.

## License

Released under the **Llama 3.2 Community License** (matches the student base, [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B)). Because MedGemma-4B was used as a distillation teacher, downstream users should also review and comply with Google's **Health AI Developer Foundations** terms of use for MedGemma (see the [MedGemma model card](https://huggingface.co/google/medgemma-4b-it)) — these include specific restrictions on clinical/diagnostic use that may apply to derivative models trained with MedGemma's outputs.

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