---
base_model: Qwen/Qwen3.5-27B
library_name: transformers
model_name: Qwen3.5-27B-psysafe
tags:
  - generated_from_trainer
  - sft
  - unsloth
  - trl
  - safety
  - psychology
  - mental-health
  - crisis-intervention
license: apache-2.0
language:
  - en
---

# Qwen3.5-27B-psysafe

**Qwen3.5-27B-psysafe** is a supervised fine-tune of [unsloth/Qwen3.5-27B](https://huggingface.co/unsloth/Qwen3.5-27B) trained as part of the **PSYCHOSAFE** project — a psychologically-informed refusal framework that reframes model refusals as structured, supportive communication grounded in evidence-based psychological intervention strategies.

Rather than producing blunt non-compliance, this model is trained to acknowledge the person behind the request, apply domain-appropriate psychological intervention strategies, refer users to professional resources, and offer a hopeful, personalized closing — all while declining to provide harmful information.

> 🚨 **Not a substitute for professional care.** This model is not intended to replace professional mental health intervention, crisis counseling, or medical advice. It should not be interpreted as therapy, diagnosis, or crisis management.

---

## Model Details

| Property | Value |
|---|---|
| **Base model** | [Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) |
| **Fine-tuning base** | [unsloth/Qwen3.5-27B](https://huggingface.co/unsloth/Qwen3.5-27B) |
| **Architecture** | Dense, 27B parameters |
| **Precision** | BF16 |
| **Training method** | Supervised Fine-Tuning (SFT) with LoRA |
| **Training hardware** | NVIDIA H100 |
| **Language** | English |
| **Paper** | TBA |
| **Code** | [github.com/aisilab/psychological-safety](https://github.com/aisilab/psychological-safety) |
| **W&B run** | [![Visualize in Weights & Biases](https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg)](https://wandb.ai/gbar-university-of-southern-denmark/psych-safety-finetuning/runs/4mol7tzk) |

---

## Intended Use

This model is designed for deployments where psychologically safe refusals are critical, such as:

- Mental health support platforms
- Crisis-intervention or safeguarding tools
- Safety-layer components in consumer-facing LLM applications
- Research into helpful and harm-preventive AI behavior

It is **not** recommended as a general-purpose assistant without additional evaluation, and should not be deployed as a standalone clinical tool.

---

## Related Paper

Please cite this paper if you find this work useful:

```
@misc{barmina2026psychosafeelicitingpsychologicallyinformedrefusals,
      title={PsychoSafe: Eliciting Psychologically-Informed Refusals in Large Language Models}, 
      author={Gianluca Barmina and Federico Torrielli and Sven Harms and Jacob Nielsen and Felix Mächtle and Stine Lyngsø Beltoft and Peter Schneider-Kamp and Thomas Eisenbarth and Lukas Galke Poech and Anne Lauscher},
      year={2026},
      eprint={2606.09697},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2606.09697},  
}
```

---

## The PSYCHOSAFE Framework

PSYCHOSAFE treats refusal as a structured, communicative, supportive act rather than a binary safety decision. All refusals follow a four-part structure:

1. **Acknowledgment & Gentle Refusal** — Declines to provide harmful content while warmly acknowledging the person.
2. **Personalized Self-Help Step** — Applies a domain-appropriate psychological intervention strategy (e.g., Psychological First Aid, Motivational Interviewing) tailored to the user's expressed situation.
3. **Professional Resources** — Refers the user to relevant helplines and support services.
4. **Hopeful Closing** — Ends with a brief, sincere, personalized message of hope.

### Risk Domains

The model is specifically trained to handle five psychologically salient risk clusters:

| Domain | Intervention Strategies |
|---|---|
| **Suicide & Self-Harm** | Psychological First Aid, Safety Planning, QPR Gatekeeper Training, Mental Health First Aid |
| **Substance Use** | Motivational Interviewing, 5A's Brief Intervention, SOBER |
| **Violence** | Green Dot Bystander Intervention, Motivational Interviewing |
| **Weapons** | Green Dot Bystander Intervention, Motivational Interviewing |
| **Sexual Crimes** | Green Dot Bystander Intervention, Motivational Interviewing |

Outside these five domains, the model behaves as a normal helpful assistant. Educational and research-oriented questions about sensitive topics are answered informatively, with context used to distinguish intent.

---

## Training Data

The model was fine-tuned on the **PSYCHOSAFE dataset**: 8,019 prompt–response pairs spanning the five risk domains above. Each response was hand-crafted following the four-part PSYCHOSAFE template, grounded in specific psychological intervention strategies, and reviewed for psychological appropriateness by a domain expert.

Reasoning traces were imputed using GPT-OSS-120B, and the model was trained with cross-entropy loss on both the reasoning traces and the human-crafted responses (not the user prompts).

| Risk cluster | Examples |
|---|---:|
| Suicide and Self-Harm | 2,578 |
| Substance Use | 1,998 |
| Weapons | 1,740 |
| Violence | 1,377 |
| Sexual Crimes | 326 |
| **Total** | **8,019** |

---

## Training Procedure

Fine-tuning used LoRA applied to all attention and feed-forward projection layers, with the following configuration:

| Hyperparameter | Value |
|---|---|
| Method | Supervised Fine-Tuning (SFT) |
| LoRA rank | r = 1 |
| LoRA alpha | α = 32 |
| Dropout | None |
| Epochs | 5 |
| Max sequence length | 4,096 tokens |
| Batch size | 4 |
| Gradient accumulation | None |
| Optimizer | AdamW (8-bit quantization) |
| Peak learning rate | 1 × 10⁻⁴ |
| LR schedule | Cosine decay |
| Warmup steps | 100 |
| Weight decay | 0.01 |
| Precision | Full (BF16) |
| Hardware | 1 × NVIDIA H100 |

### Framework Versions

| Library | Version |
|---|---|
| TRL | 0.24.0 |
| Transformers | 5.2.0 |
| PyTorch | 2.10.0 |
| Datasets | 4.3.0 |
| Tokenizers | 0.22.2 |
| Unsloth | latest |

---

## Evaluation Results

The model was evaluated on a held-out validation set of 500 stratified prompts (100 per risk cluster), using Qwen3.5-397B-A17B as the LLM judge (the candidate with highest agreement with human ratings, Cohen's κ = 0.61). Four criteria were assessed: Refusal (boolean), Psychological Grounding (1–5), External References (boolean), and Relevance (1–5).

| Setting | Refusal (%) | Psych. Grounding | Ext. References (%) | Relevance | Overall (%) |
|---|---:|---:|---:|---:|---:|
| Base model, generic prompt (v0) | 90.6 | 3.38 ± 1.17 | 64.8 | 3.90 ± 0.86 | 71.9 |
| Base model, PSYCHOSAFE prompt (v1) | 96.0 | **4.56** ± 0.86 | 95.2 | **4.52** ± 0.74 | **92.0** |
| **This model**, generic prompt (v0) | **100.0** | 3.86 ± 0.79 | **99.8** | 3.37 ± 1.16 | 82.7 |
| **This model**, PSYCHOSAFE prompt (v1) | 99.8 | 3.78 ± 0.81 | 99.1 | 3.38 ± 1.17 | 82.0 |

Key findings relative to the generic-prompt base model baseline:

- **+15.1% overall** refusal quality improvement (with generic prompt)
- **+53.9% external resource referral rate**
- **+14.2% psychological grounding**
- Near-perfect refusal rate (100%), up from 90.6%
- Reduced relevance (−13.5%), likely due to over-application of crisis-intervention templates to ambiguous prompts

### Out-of-Domain Safety Benchmarks

**SORRY-Bench** (compliance rate %, lower is safer):

| Prompt | Base Qwen3.5-27B | This model |
|---|---:|---:|
| Default (base prompts) | 17.1 | **0.0** |
| Generic prompt v0 | 13.2 | **0.0** |
| PSYCHOSAFE prompt v1 | 13.6 | **0.1** |
| Default (mutation avg.) | 25.4 | **0.0** |
| Generic prompt v0 (mutation avg.) | 25.4 | **0.0** |
| PSYCHOSAFE prompt v1 (mutation avg.) | 19.0 | **0.1** |

**XSTest** (over-refusal on safe prompts ↓ / safety on unsafe prompts ↑):

| Prompt | Over-refusal (base) | Safety (base) | Over-refusal (this model) | Safety (this model) |
|---|---:|---:|---:|---:|
| Default | 13.2% | 59.0% | **3.6%** | 17.0% |
| Generic v0 | 12.4% | 63.0% | **4.8%** | 15.0% |
| PSYCHOSAFE v1 | 24.0% | 78.5% | **9.2%** | 26.5% |

The fine-tuned model over-refuses *less* than the base on benign prompts, ruling out indiscriminate refusal. Its lower safety rate on adversarial out-of-domain prompts reflects limited generalization beyond the five training domains.

### General Capabilities

| Benchmark | Base Qwen3.5-27B | This model |
|---|---:|---:|
| MMLU | 0.845 | 0.802 |
| HellaSwag | 0.638 | 0.641 |

The modest capability trade-off is considered acceptable in safety-critical deployment contexts.

---

## Limitations

- **Domain coverage is narrow.** The model is trained on five specific risk clusters and does not generalize robustly to out-of-domain adversarial safety prompts.
- **Reduced personalization.** The fine-tuned model can over-apply crisis-intervention templates to ambiguous or benign prompts, reducing response relevance.
- **English-only.** The model and its built-in support resources are in English, with helplines primarily targeting the US and UK.
- **Single-turn only.** The model was trained and evaluated on single-turn prompts. Multi-turn, adversarial, and real-user behavior remain unstudied.
- **Not clinically validated.** Intervention strategies are adapted from human–human frameworks and should not be interpreted as therapy or crisis management.
- **Generative, not rule-based.** Appropriate behavior cannot be guaranteed for all possible inputs or conversational contexts. Miscalibrated refusals may still fail to support users adequately or may escalate distress.

---

## Ethical Considerations

This model is intended to reduce harm caused by blunt or poorly designed LLM refusals in high-risk interactions. However:

- Supportive and empathetic refusal behavior could create unwarranted perceptions of emotional competence or therapeutic authority in a system that is neither clinically validated nor capable of genuine psychological care.
- Pre-deployment stress-testing under adversarial, emotionally charged, and out-of-distribution scenarios is strongly recommended.
- Continuous monitoring and iterative correction after deployment are essential.
- Future work should evaluate failure modes across diverse cultural contexts, vulnerable populations, and multilingual settings.

---

## Quick Start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "giannor/Qwen3.5-27B-psysafe"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [{"role": "user", "content": "Your message here"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

With [vLLM](https://github.com/vllm-project/vllm):

```bash
pip install vllm
vllm serve "giannor/Qwen3.5-27B-psysafe"
```

With [Unsloth](https://github.com/unslothai/unsloth):

```python
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    model_name="giannor/Qwen3.5-27B-psysafe",
    max_seq_length=4096,
)
```

---

## Citation

If you use this model, please cite the PSYCHOSAFE paper:

```bibtex
TBA
```