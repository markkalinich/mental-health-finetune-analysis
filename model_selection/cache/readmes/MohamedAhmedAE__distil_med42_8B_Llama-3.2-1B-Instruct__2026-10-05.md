---
license: llama3.2
base_model: meta-llama/Llama-3.2-1B-Instruct
tags:
- medical
- healthcare
- knowledge-distillation
- distillation
- llama
- llama-3.2
- lightweight
- instruct
- chat
- clinical-nlp
datasets:
- MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset
language:
- en
pipeline_tag: text-generation
library_name: transformers
---

# distil_med42_8B_Llama-3.2-1B-Instruct

**A 1B-parameter instruction-tuned medical chat model distilled from [Llama3-Med42-8B](https://huggingface.co/m42-health/Llama3-Med42-8B) into a [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) student**, using the framework from the paper *"DistilLLM-Med: A Lightweight Medical Language Model through Knowledge Distillation"* (IEEE ICICIS 2025).

- 📄 **Paper**: [IEEE Xplore, document 11313220](https://ieeexplore.ieee.org/document/11313220/)
- 💻 **Training notebook**: [`Train_Distil_Med42_LLama_Transformer.ipynb`](https://github.com/Mohamed-Ahmed-Abo-El-Enen/MasterPapers/blob/main/DistilLLM-Med%20A%20Lightweight%20Medical%20Language%20Model%20through%20Knowledge%20Distillation/Training/Train_Distil_Med42_LLama_Transformer.ipynb)
- 🗂️ **Training data**: [MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset)
- 👨‍🏫 **Teacher**: [m42-health/Llama3-Med42-8B](https://huggingface.co/m42-health/Llama3-Med42-8B) (8.03B params)
- 🎓 **Student base**: [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) (1.24B params)

This is the **instruction/chat variant** of the Med42-8B distillation: the student starts from Llama-3.2-1B-**Instruct** rather than the base completion model, so it keeps a usable chat template and is meant to be prompted conversationally, like a compact medical assistant. The core distillation recipe, data, and teacher are identical to its non-instruct sibling, [distil_Med42_8B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_Med42_8B_Llama-3.2-1B) — only the student's starting checkpoint differs.

## About the paper

**DistilLLM-Med: A Lightweight Medical Language Model through Knowledge Distillation**
Mohamed Abo El-Enen, Sally Saad, Taymoor Nazmy — Faculty of Computer and Information Sciences, Ain Shams University, Cairo, Egypt.
Published in *2025 IEEE Twelfth International Conference on Intelligent Computing and Information Systems (ICICIS)*.
[IEEE Xplore](https://ieeexplore.ieee.org/document/11313220/)

The paper distills medical expertise from two specialized teacher models — **MedGemma-4B** (referred to as "MedGemini-4B" in the paper text, citing Sellergren et al.'s MedGemma technical report) and **Llama3-Med42-8B** — into a single lightweight **LLaMA 3.2-1B** student, using temperature-scaled KL-divergence distillation, specialty-weighted losses, and attention-map alignment. The resulting student retains **89.3%** of teacher token-level accuracy while cutting parameters by **75%**, reaching **47.7%** average accuracy on MMLU-Medical (**67.8%** of the Med42-8B teacher's 72.6%) and **59.5 tokens/sec** inference throughput.

## Model family

| Model | Teacher | Student base | Notebook |
|---|---|---|---|
| **distil_med42_8B_Llama-3.2-1B-Instruct** (this model) | Med42-8B | Llama-3.2-1B-**Instruct** | `Train_Distil_Med42_LLama_Transformer.ipynb` |
| [distil_Med42_8B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_Med42_8B_Llama-3.2-1B) | Med42-8B | Llama-3.2-1B | `Train_Distil_Med42_LLama_Transformer.ipynb` |
| [distil_llama_3_8B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_llama_3_8B_Llama-3.2-1B) | Meta-Llama-3-8B | Llama-3.2-1B | `Distil_LLama_LLama.ipynb` |
| [distil_MedGemma_4B_Llama-3.2-1B](https://huggingface.co/MohamedAhmedAE/distil_MedGemma_4B_Llama-3.2-1B) | MedGemma-4B | Llama-3.2-1B | `Train_Distil_MedGemma_LLama.ipynb` |

## Method

Because Med42-8B and Llama-3.2-1B-Instruct are both built on the Llama-3 tokenizer (128,256 shared vocabulary tokens), this run distills **directly on logits**, with no vocabulary-projection layer needed.

The training objective combines four components, following the paper's Eq. (1)–(7):

1. **Temperature-scaled KL distillation** — `L_KD = α·L_CE(y, p_S) + (1-α)·L_KL(p_T^τ, p_S^τ)`, with `α = 0.7` (favoring the soft-label/KL term over the hard-label cross-entropy term).
2. **Progressive temperature scheduling** — softmax temperature `τ` decays exponentially from `τ₀ = 8` to `τ_final = 1` over the first 50,000 steps, so the student first learns broad relationships between similar conditions before sharpening toward confident predictions.
3. **Specialty-weighted loss** — per-specialty weights `w_s` re-balance the KL loss across medical subdomains so no single specialty dominates training.
4. **Attention-map alignment** — an auxiliary Frobenius-norm loss `L_att` pulls the student's per-layer, per-head attention matrices toward the teacher's.

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
| Training extent | ~0.6 epoch over the unified corpus (Med42 run, per the paper) |

> A full per-checkpoint config log (comparable to the one published for the non-instruct sibling repo) was not published to the Hub for this specific instruct repo; the framework, teacher, and dataset are identical, only the student's starting weights differ (Instruct vs. base Llama-3.2-1B).

Default hyperparameter grid used throughout the project:
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

Preprocessing deduplicated samples, truncated to a 1024-token limit, normalized medical abbreviations (via MeDAL mappings), and segmented long clinical notes into coherent chunks. Benchmark **test sets were excluded from training**. The processed corpus is on the Hub as [Med_LLaMa3_fine-tuning_dataset](https://huggingface.co/datasets/MohamedAhmedAE/Med_LLaMa3_fine-tuning_dataset) (1.64M train / 14.4k validation rows).

## Results (from the paper)

The paper reports two distilled variants ("Experiment 1" and "Experiment 2") evaluated against both teachers and the untrained baseline. **The paper does not explicitly label which experiment number maps to which Hub checkpoint (base vs. instruct)** — treat the numbers below as the project's overall Med42-distillation benchmark results.

**MMLU-Medical accuracy:**

| Task | LLaMA 3.2-1B (base) | Llama3-Med42-8B (teacher) | Distilled Exp. 1 | Distilled Exp. 2 |
|---|---|---|---|---|
| Anatomy | 49.6% | 74.1% | 51.1% | 49.6% |
| Clinical Knowledge | 35.9% | 75.1% | 49.1% | 44.5% |
| College Biology | 38.2% | 82.6% | 50.0% | 41.0% |
| College Medicine | 33.5% | 68.8% | 33.0% | 38.2% |
| Medical Genetics | 41.0% | 77.0% | 45.0% | 49.0% |
| Nutrition | 42.2% | 73.9% | 56.2% | 51.6% |
| Professional Medicine | 37.9% | 77.6% | 55.2% | 48.9% |
| Virology | 38.6% | 51.8% | 42.2% | 34.9% |
| **Average** | **39.6%** | **72.6%** | **47.7%** | **44.7%** |

The best distilled model reaches **67.8%** of the Med42-8B teacher's accuracy — a **20.5%** relative improvement over the base LLaMA 3.2-1B.

**Compute efficiency:**

| Model | Params (B) | Memory (GB) | Speed (tok/s) | Latency (ms) |
|---|---|---|---|---|
| Llama3-Med42-8B (teacher) | 8.03 | 5.32 | 49.7 | 1006.0 |
| LLaMA 3.2-1B (base) | 1.24 | 7.68 | 102.7 | 487.0 |
| **Distilled LLaMA 3.2-1B** | **1.24** | **7.68** | **59.5** | **841.0** |

Independent medical-expert review of 89 model answers found most responses (70/89) more detailed and context-rich than reference answers, but flagged 19/89 with critical factual errors (misdiagnoses, incorrect mechanisms) — the model **requires expert oversight** and is not a standalone diagnostic tool.

## Usage

This model has a chat template registered on the Hub:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "MohamedAhmedAE/distil_med42_8B_Llama-3.2-1B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "What does low mobility and bulging of the tympanic membrane suggest?"}
]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(inputs, max_new_tokens=256, do_sample=False)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## Intended use & limitations

- Research use in efficient/lightweight medical chat assistants and knowledge-distillation studies; suitable for edge/low-resource deployment experiments.
- **Not a certified clinical tool.** The paper's own expert review found critical errors in ~21% of sampled answers (misdiagnoses, incorrect mechanisms, imprecise terminology). Always require qualified human oversight before acting on any output.
- Distillation training only reached ~0.6 epoch over the corpus (Med42 run) — treat as a research checkpoint, not a fully converged production model.
- Inherits any biases present in the teacher model (Med42-8B) and in the 18-source training corpus.

## License

Released under the **Llama 3.2 Community License** (matches the student base, [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)). Since Med42-8B was used as a distillation teacher, also review the license terms on [m42-health/Llama3-Med42-8B](https://huggingface.co/m42-health/Llama3-Med42-8B) before downstream/commercial use.

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