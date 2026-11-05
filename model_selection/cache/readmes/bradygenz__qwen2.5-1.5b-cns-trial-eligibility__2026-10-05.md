---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B-Instruct
tags:
  - clinical-trials
  - eligibility-screening
  - lora
  - peft
  - psychiatry
language:
  - en
pipeline_tag: text-generation
---

# Qwen2.5-1.5B-Instruct for CNS Psychiatric Trial Eligibility Screening

A [LoRA](https://arxiv.org/abs/2106.09685) fine-tune of [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) that reads an unstructured physician narrative alongside a clinical trial's eligibility criteria and decides whether the patient qualifies, reasoning through the criteria one at a time before committing to a label.

## Introduction

Clinical trial recruitment fails more often than it succeeds. A large share of trials miss their enrollment targets, and screening patients against eligibility criteria is a manual, slow, and expensive bottleneck in that process. CNS psychiatric trials (major depressive disorder, bipolar I disorder, PTSD) are a particularly hard case, because the relevant patient evidence frequently lives in unstructured narrative rather than in structured EHR fields, and because the criteria themselves are dense with lookback windows, severity thresholds, and compound conditions. General-purpose LLMs handle this task badly in a specific and dangerous way: they read the obvious inclusion criteria, produce fluent and confident reasoning, and miss a single buried disqualifying criterion. The failure is not incoherence, it is overconfidence on the one criterion that matters. I fine-tuned Qwen2.5-1.5B-Instruct with LoRA on a synthetic dataset of 400 per-criterion eligibility examples, formatted using [Contrastive Chain-of-Thought](https://arxiv.org/abs/2311.09277) so that each training example demonstrates both correct reasoning and the specific mistake a model is likely to make. The result targets exactly that failure mode: missed exclusions on the held-out test set dropped from 7 of 21 to 4 of 21 against the base model, a 43% reduction, while overall accuracy stayed flat. In other words, fine-tuning did not make the model right more often, it changed which errors it makes, trading dangerous false approvals for more conservative false rejections.

## Data

Training data is synthetic. No real patient records were used at any stage. I pulled eligibility criteria for CNS psychiatric trials from the [ClinicalTrials.gov API v2](https://clinicaltrials.gov/data-api/api), targeting MDD, bipolar I disorder, and PTSD, then parsed the raw eligibility text into structured inclusion and exclusion lists. (One non-obvious implementation detail for anyone reproducing this: `filter.phase` is not a valid API v2 parameter, so phase filtering has to happen client side after retrieval.) Trials were dropped from the initial extraction pool for three reasons: a parser edge case involving blank-line-delimited criteria formatting, pediatric or child-context populations that fall outside the adult scope of this task, and a healthy-controls sub-arm whose criteria do not describe a patient population. That left **36 trials**. For each trial I selected a target criterion using a heuristic favoring concrete, checkable facts (numbers, time windows, named comorbidities) over vague investigator-judgment language, then used a frontier teacher model, seeded with eight hand-authored contrastive pairs, to generate matched patient vignettes: one that satisfies every criterion, and one that satisfies everything except the target, which it clearly violates. This contrastive pairing is the core of the design, since it forces the model to discriminate on exactly the criterion that would otherwise be overlooked. The final corpus is **400 examples**, balanced roughly 50/50 between ELIGIBLE and INELIGIBLE to prevent label bias, split **316 train / 42 validation / 42 test** (approximately 80/10/10), with the test split held out entirely from training and used only for final evaluation. The test split is balanced at exactly 21 ELIGIBLE and 21 INELIGIBLE. Validation was single-stage: I reviewed a sample of generated examples against their source criteria to confirm label accuracy and rationale quality. The domain-expert review by a collaborator with a doctoral background in neuroscience and CNS pharmaceutical R&D, described in my earlier project planning, was not completed within the project timeline and is listed under future work.

## Methodology

I used supervised fine-tuning with [LoRA](https://arxiv.org/abs/2106.09685) via the [PEFT](https://huggingface.co/docs/peft) library, rather than full-parameter fine-tuning or a RAG pipeline. RAG was ruled out on task structure: every prompt already contains the full trial context needed to answer, so there is no missing external knowledge to retrieve. The task is per-criterion reasoning, not lookup. LoRA was chosen over full fine-tuning because at 316 training examples it reaches comparable performance at a fraction of the compute, which matters on a shared HPC GPU queue, and because parameter-efficient methods carry lower catastrophic forgetting risk than full fine-tuning. I swept three hyperparameter configurations and selected on validation accuracy, not training loss. The two that bracket the tradeoff are below:

| Config | Rank (r) | Alpha | Learning rate | Epochs | Train loss | Val accuracy |
|---|---|---|---|---|---|---|
| **combo2_lower_lr_more_epochs** (selected) | **8** | **16** | **1e-4** | **5** | **0.707** | **97.6%** |
| combo3_higher_capacity | 32 | 64 | 3e-4 | 3 | 0.455 | 88.1% |

All configurations shared `lora_dropout=0.05`, `bias="none"`, `task_type="CAUSAL_LM"`, and adapted all seven projection modules (`q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`), so both the attention and MLP sublayers were updated rather than attention alone. Trained with [PEFT](https://huggingface.co/docs/peft) 0.19.1.

The selected configuration is the one with the *highest* training loss and the *best* validation accuracy, while the highest-capacity configuration achieved the lowest training loss and the worst validation accuracy. That is a textbook overfitting signature: more trainable capacity plus a larger learning rate let combo3 fit the training set closely without learning a generalizable decision boundary, whereas combo2's smaller rank and more numerous conservative update steps generalized better. Training ran on a single NVIDIA A40 on the University of Virginia's Rivanna cluster. The adapter was subsequently merged into the base weights for distribution, with the merge arithmetic performed in float32 and cast to bfloat16 at save time.

## Evaluation

| Model | Eligibility Test Split | [MedQA](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options) | [MMLU Clinical Knowledge](https://huggingface.co/datasets/cais/mmlu) | [RACE](https://huggingface.co/datasets/ehovy/race) |
|---|---|---|---|---|
| **Ours** (Qwen2.5-1.5B-Instruct + LoRA) | **83.3%** | 44.9% | 67.5% | **41.6%** |
| [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) (base) | **83.3%** | **48.4%** | **69.1%** | 36.9% |
| [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | 57.1% | 30.7% | 43.4% | 34.0% |
| [SmolLM2-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) | 71.4% | 33.8% | 57.7% | 39.1% |

All models evaluated with identical settings: zero-shot, chat template applied, greedy decoding, seed 42, 1,000 documents per benchmark (265 for MMLU Clinical Knowledge, its full test set). Eligibility test split is the 42-example held-out synthetic split, scored generatively. No model produced an unparseable response.

I chose the three benchmarks to answer three different questions. **MedQA** (USMLE-style clinical questions) and **MMLU Clinical Knowledge** test whether narrow task fine-tuning eroded the medical knowledge the base model started with, which matters because eligibility screening depends on understanding what the criteria refer to. **RACE** is general reading comprehension and serves as a catastrophic forgetting check, chosen partly because I had seen LoRA fine-tuning on an unrelated task drop RACE by ten points in earlier coursework, so I knew it was sensitive. I originally planned to use PubMedQA and MedMCQA as well, but both failed to load for all four models due to stale task definitions in the evaluation harness (PubMedQA's config ships a Python loading script that the current `datasets` library refuses to execute; MedMCQA's references a bare dataset name that `huggingface_hub` now rejects). The comparison models were chosen to isolate two different variables. **Qwen2.5-0.5B-Instruct** is the same family at a third the size, which separates gains attributable to fine-tuning from gains attributable to scale. **SmolLM2-1.7B-Instruct** is a different family at essentially the same parameter count, which tests whether Qwen2.5 was a good base or whether any small instruct model would land in the same place. I originally planned to evaluate against the [n2c2 2018 cohort selection dataset](https://n2c2.dbmi.hms.harvard.edu/) and the Burkhart and Beaulieu-Jones synthetic distillation benchmark, but both sit behind data use agreements requiring credentialed access that I could not obtain within the project timeline.

On the task itself, my model and the base model score identically at 83.3%, and both substantially beat the two comparison models. **But identical accuracy hides the result that matters.** Look at the recall column below: the base model, the 0.5B, and SmolLM2 all score exactly 1.000 recall on ELIGIBLE. That is not three models being good at something. It is three models that almost never reject anyone, so they never wrongly reject an eligible patient. Qwen2.5-0.5B waves through 18 of 21 genuinely ineligible patients and still posts perfect recall. Fine-tuning cut missed exclusions from 7 of 21 to 4 of 21, a 43% reduction, and my model is the only one of the four that meaningfully rejects anybody.

The first two rows below are the **same trained adapter in two deployment configurations**: applied at inference time via PEFT, and merged into the base weights. They are mathematically equivalent and numerically are not, for reasons described under Limitations. The merged configuration is what this repository distributes, so it is the row carried into the summary table above and the one I treat as the headline result.

| Model | Accuracy | Precision (ELIGIBLE) | Recall (ELIGIBLE) | F1 (ELIGIBLE) | Missed Exclusions |
|---|---|---|---|---|---|
| **Ours, adapter at inference** | 88.1% | 0.864 | 0.905 | 0.884 | **3/21** |
| **Ours, merged weights** (distributed here) | 83.3% | 0.818 | 0.857 | 0.837 | 4/21 |
| Qwen2.5-1.5B-Instruct (base) | 83.3% | 0.750 | 1.000 | 0.857 | 7/21 |
| SmolLM2-1.7B-Instruct | 71.4% | 0.636 | 1.000 | 0.778 | 12/21 |
| Qwen2.5-0.5B-Instruct | 57.1% | 0.538 | 1.000 | 0.700 | 18/21 |

This exposes a metric problem. Scoring ELIGIBLE as the positive class rewards approval bias, which is the exact failure mode this project set out to fix, and it is why my merged model's F1 (0.837) reads slightly worse than the base model's (0.857) despite being the better screener. The class the model is actually being asked to detect is INELIGIBLE. Recomputed on that basis:

| Model | Precision (INELIGIBLE) | Recall (INELIGIBLE) | F1 (INELIGIBLE) |
|---|---|---|---|
| **Ours, adapter at inference** | 0.900 | **0.857** | **0.878** |
| **Ours, merged weights** (distributed here) | 0.850 | 0.810 | 0.829 |
| Qwen2.5-1.5B-Instruct (base) | 1.000 | 0.667 | 0.800 |
| SmolLM2-1.7B-Instruct | 1.000 | 0.429 | 0.600 |
| Qwen2.5-0.5B-Instruct | 1.000 | 0.143 | 0.250 |

The baselines' perfect precision is an artifact of barely predicting the class at all, and the ranking now matches the qualitative picture. On the general benchmarks, RACE improved by 4.7 points (about 2.2 standard errors of the difference, so probably real), which is plausible given that criterion checking against a narrative is structurally a reading comprehension task. MedQA fell by 3.5 points and MMLU Clinical Knowledge by 1.6, at roughly 1.6 and 0.4 standard errors respectively, so neither is conclusive but the MedQA direction is worth flagging as possible mild erosion of medical exam knowledge. There is no evidence of catastrophic forgetting.

## Usage and Intended Uses

This model is intended as a **research prototype for criterion-level trial prescreening**, the kind of tool that would surface a ranked shortlist of candidate patients for a human coordinator to review, or give trial sponsors empirical criterion-level yield data to inform protocol design. It is explicitly **not** a clinical decision support tool, and it must not be used to make or automate enrollment decisions, to determine a patient's care, or as a substitute for review by a qualified investigator. It was trained entirely on synthetic narratives and has never been evaluated against real clinical documentation.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "bradygenz/qwen2.5-1.5b-cns-trial-eligibility"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype="bfloat16", device_map="auto")

messages = [{"role": "user", "content": prompt}]  # see Prompt Format below
formatted_prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)

# Greedy decoding is intentional. All reported results use do_sample=False, and
# sampling will not reproduce them.
output_ids = model.generate(**inputs, max_new_tokens=512, do_sample=False)
generated = output_ids[0][inputs["input_ids"].shape[1]:]
print(tokenizer.decode(generated, skip_special_tokens=True))
```

## Prompt Format

Prompts are a single user turn wrapped in the Qwen2.5 chat template, containing a role instruction, the trial's full inclusion and exclusion criteria, and the patient case, and ending with an explicit instruction to conclude with a single label line.

```
You are a clinical trial eligibility screener. Given a trial's inclusion and exclusion criteria and a patient case, determine whether the patient is ELIGIBLE or INELIGIBLE for the trial. Reason step by step, checking the patient case against each criterion in turn, and pay particular attention to criteria that could plausibly be overlooked. Conclude with a single line stating "Label: ELIGIBLE" or "Label: INELIGIBLE".

Trial: A Trial to Assess Brexpiprazole Versus Placebo for the Treatment of Acute Manic Episodes Associated With Bipolar I Disorder

Inclusion Criteria:
- Ages 18-65, inclusive
- [additional inclusion criteria]

Exclusion Criteria:
- [exclusion criteria]

Patient Case:
[unstructured physician narrative, 150-300 words]
```

## Expected Output Format

The model produces a chain-of-thought trace that walks the patient case against the criteria in turn, calls out the specific criterion that decides the case, and closes with a single machine-parseable label line.

```
The patient's age (34), diagnosis, current episode duration, and symptom severity all meet the
inclusion criteria. No psychotic features, no recent substance use disorder, no significant
medical comorbidity. The key criterion to verify has two branches: the patient is on a
psychiatric medication, and that medication must have been at a stable dose for at least 30
days prior to screening. The narrative states the bupropion dose was increased three weeks
ago, which is less than 30 days, so this exclusion applies.

Label: INELIGIBLE
```

## Limitations

**The training data is entirely synthetic.** Narratives were written by a language model, not drawn from real clinical documentation, so any systematic authoring bias in the teacher model becomes a spurious pattern the fine-tuned model can learn. The intended domain-expert clinical review was not completed, so clinical plausibility rests on my own review alone. **The test set is small.** Forty-two examples means the confidence interval on any accuracy figure is wide, and differences of one or two examples should not be over-interpreted. **Fine-tuning changed the error profile more than the error rate.** Missed exclusions fell substantially, but the model introduced false exclusions it did not previously make, concentrated on trials with two adjacent, similarly-worded criteria where the model appears to drift between them. For screening, that trade favors safety, since a false exclusion costs a second look while a missed exclusion sends an ineligible patient forward, but it is a real cost and not a pure improvement. **Scope is narrow.** The model was trained on adult MDD, bipolar I, and PTSD trials from a single registry, and single-criterion decisions in isolation. Generalization to other therapeutic areas, pediatric populations, EU CTR protocol formatting, or whole-protocol screening is untested. **Merged and adapter-applied inference are not numerically identical.** Under greedy decoding, merging the LoRA weights into the base model produces different generations from applying the adapter at inference time on roughly two thirds of test responses, because bfloat16 rounding differs between the two computation paths and a single divergent token cascades through the entire reasoning chain. The effect is measurable and not trivial: the adapter-applied configuration scores 88.1% with 3 of 21 missed exclusions, while the merged configuration scores 83.3% with 4 of 21, from the identical trained adapter. I verified this is not a sampling artifact (both use greedy decoding), not a parsing artifact (both parse identically under first-match and last-match rules), and not a prompt formatting artifact (both apply the same chat template). Merging in float32 rather than bfloat16 did not change the result. All headline figures in this card reflect the merged model distributed here, since that is what users of this repository actually run, but anyone loading the adapter directly onto the base model should expect somewhat better numbers. **No evaluation against real clinical benchmarks.** The n2c2 2018 cohort selection dataset and the Burkhart and Beaulieu-Jones benchmark both sit behind data use agreements requiring credentialed access, which was not obtainable within the project timeline. External validation on real annotated clinical text remains the most important open gap.

## Future Work

Domain-expert clinical review of the synthetic corpus, external validation against n2c2 2018 once credentialed access is granted, expansion to EU CTR protocols for non-US regulatory coverage, whole-protocol rather than single-criterion screening, and a comparison against Qwen3 to test whether native reasoning modes make explicit Contrastive CoT formatting redundant on this task.

## Citation and Acknowledgements

Base model: [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) (Qwen Team, Alibaba Cloud).
Method: [LoRA](https://arxiv.org/abs/2106.09685) (Hu et al., 2021), [Contrastive Chain-of-Thought](https://arxiv.org/abs/2311.09277) (Chia et al., 2023).
Data source: [ClinicalTrials.gov](https://clinicaltrials.gov/).
Compute provided by [University of Virginia Research Computing](https://www.rc.virginia.edu/) (Rivanna).
Produced for DS 5002, University of Virginia School of Data Science.
