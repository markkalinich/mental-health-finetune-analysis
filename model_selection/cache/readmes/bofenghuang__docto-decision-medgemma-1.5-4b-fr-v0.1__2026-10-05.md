---
language:
- fr
license: other
license_name: health-ai-developer-foundations
license_link: https://developers.google.com/health-ai-developer-foundations/terms
library_name: transformers
base_model: google/medgemma-1.5-4b-it
datasets:
- bofenghuang/docto-decision-data-fr-v0.1
tags:
- medical
- french
- system-one
- decision
- calibration
- lora
---

# 🩺 Docto Decision MedGemma-1.5-4B (v0.1)

![Docto Decision Bench](assets/benchmark.png)

## ✨ Summary

Docto Decision is a family of French medical decision models. You give a text (a patient message, a clinical note, a case report), a question and the possible answers, and the model returns one probability per answer.

This model is a LoRA fine-tune of [medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it) (4.30B parameters), merged into the base weights (the adapter is in `adapters/`). It answers with a single token, an option letter or « oui » / « non », and the probabilities are read from that token.

The task is defined at inference time by the instruction, the question and the answers. Tasks close to the training ones work best, and new tasks can be tried zero-shot.

## 🎯 Use cases

| area | examples |
|---|---|
| Patient messages | urgency level, red flags, triage, specialty routing, health topic |
| Practice inbox | request intent, who should answer, visit motive, reminder replies |
| Assistant safety | input guardrail, answer compliance, rule and rubric checks, personal identifiers |
| Clinical text | assertion and temporality, medications, allergies, note sections, claim support |
| Coding and documents | ICD-10 chapter, document type, article specialty, passage relevance |

## 🚀 Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "bofenghuang/docto-decision-medgemma-1.5-4b-fr-v0.1"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype=torch.bfloat16).eval().to("cuda")
SYSTEM = ("Tu es un expert médical francophone. On te donne une tâche de décision : une consigne, éventuellement un profil, "
          "un contexte et un élément, une question et les réponses possibles. Résous la tâche. Réponds uniquement par la réponse "
          "demandée, sans explication.")


def decide(task, question, options, context=None, profile=None, item=None, kind="choice"):
    """options: [(key, definition)]. kind: "choice", "score" (levels in order) or "noul" (one option: the proposition)."""
    parts = [f"[TASK] {task}"]
    if profile:
        parts.append(f"[PROFILE] {profile}")
    if context:
        parts.append(f"[CONTEXT]\n{context}")
    if item:
        parts.append(f"[ITEM] {item}")
    parts += [f"[QUESTION] {question}", "[OPTIONS]"]
    if kind == "noul":
        parts += [f"oui : {options[0][1]}", "non : ce n'est pas le cas.", "", "Réponds uniquement par « oui » ou par « non »."]
        answers = ["oui", "non"]
    else:
        answers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[: len(options)])
        parts += [f"{a}) {d}" for a, (_, d) in zip(answers, options)]
        parts += ["", f"Réponds uniquement par la lettre de la bonne réponse ({', '.join(answers)})."]
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": "\n".join(parts)}]
    text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
    ids = tok(text, return_tensors="pt", add_special_tokens=False).input_ids.to(model.device)
    with torch.no_grad():
        logits = model(ids).logits[0, -1].float()
    first = [tok.encode(a, add_special_tokens=False)[0] for a in answers]  # first token of each answer
    p = torch.softmax(logits[first], -1)
    if kind == "noul":
        return p[0].item()  # P(oui) = P(true)
    return dict(zip([k for k, _ in options], p.tolist()))


decide(task="Déterminer la conduite à tenir la plus appropriée face à ce message.",
       profile="Patient : homme, 58 ans. Antécédents : hypertension.",
       context="Patient : Bonjour, j'ai une douleur dans la poitrine qui serre depuis 30 minutes et qui descend dans le bras gauche.",
       question="Quel niveau d'urgence correspond à cette situation ?",
       options=[("home_care", "Pas d'urgence : auto-surveillance à domicile chez un adulte sans fragilité, ou demande sans symptôme."),
                ("consult_48h", "Consultation dans les 48 heures : médecin traitant, sans caractère de gravité mais qui dure ou gêne."),
                ("same_day", "Consultation le jour même : signe préoccupant sans détresse vitale."),
                ("emergency_now", "Urgence immédiate : appeler le 15 ou se rendre immédiatement aux urgences.")],
       kind="score")
# -> {'home_care': 0.000, 'consult_48h': 0.000, 'same_day': 0.003, 'emergency_now': 0.997}

decide(task="Dire si le signe indiqué est décrit comme présent chez l'enfant dans la conversation.",
       profile="Enfant : bébé de 4 mois, garçon",
       context="Parent : Bonjour, mon fils a 39 de fièvre depuis ce matin, il ne boit presque plus ses biberons et il est très mou.",
       item="Signe : nourrisson de moins de 6 mois qui boit nettement moins que d'habitude",
       question="Ce signe est-il présent d'après le parent ?",
       options=[("present", "Oui, le parent décrit ce signe comme présent.")],
       kind="noul")
# -> 0.95
```

- Write each option as a full French sentence: the model reads the definitions. For `choice`, option order does not matter. For `score`, keep the levels in order.
- For `noul`, pass a single option (the proposition) and read P(true).
- The text is French and the tags (`[TASK]`, `[CONTEXT]`...) are English. Leave out empty fields. Up to 26 options (letters A to Z).
- For throughput, serve it with vLLM, as the benchmark does.
- The chat template already starts with `<bos>`, so tokenize its output with `add_special_tokens=False`, as in training and in the snippet above. The benchmark numbers below were measured with the `<bos>` token doubled (vLLM added a second one to the text prompt). On 200 benchmark records, the snippet and the benchmark pick the same answer for 192.

## 📊 Evaluation

Results on the [Docto Decision Bench](https://huggingface.co/datasets/bofenghuang/docto-decision-bench-fr-v0.1): 12 decision tasks on real French patient messages and two clinical datasets (DiaMed, MORFITT). The benchmark repository has the data and the evaluation code.

| model | mean accuracy [95% CI] | mean ECE [95% CI] | order consistency [95% CI] | latency p50 (ms) |
|---|---|---|---|---:|
| **Docto Decision** | | | | |
| Docto Decision ModernBERT-fr-base | 81.04 [79.59, 82.39] | 6.54 [5.51, 7.68] | 94.19 [92.47, 95.72] | 8 |
| Docto Decision Qwen3.5-0.8B | 81.85 [80.40, 83.29] | 7.75 [6.67, 8.86] | 93.57 [91.75, 95.16] | 37 |
| Docto Decision Qwen3.5-2B | 84.91 [83.57, 86.20] | 7.25 [6.34, 8.24] | 94.86 [93.58, 95.99] | 36 |
| Docto Decision Gemma-4-E2B | 84.94 [83.65, 86.24] | 7.07 [6.09, 8.11] | 92.10 [90.11, 93.93] | 25 |
| **Docto Decision MedGemma-1.5-4B** (this model) | 86.25 [85.00, 87.57] | 7.78 [6.91, 8.74] | 95.09 [93.57, 96.32] | 41 |
| Docto Decision Qwen3.5-4B | 88.94 [87.90, 90.06] | 7.91 [7.13, 8.69] | 96.98 [95.89, 97.92] | 47 |
| Docto Decision Gemma-4-E4B | 90.13 [89.11, 91.10] | 7.79 [7.00, 8.61] | 95.15 [93.86, 96.30] | 27 |
| **Open LLMs (zero-shot)** | | | | |
| Qwen3.5-0.8B | 47.80 [45.96, 49.54] | 23.07 [21.49, 24.65] | 36.80 [34.56, 39.06] | 37 |
| Qwen3.5-2B | 60.12 [58.31, 61.99] | 17.32 [15.94, 18.87] | 58.15 [55.05, 61.42] | 36 |
| Gemma-4-E2B | 76.49 [75.08, 77.91] | 21.27 [19.91, 22.59] | 78.85 [76.73, 81.05] | 25 |
| MedGemma-1.5-4B | 59.00 [57.18, 60.79] | 23.49 [22.13, 24.95] | 45.57 [42.52, 48.75] | 41 |
| Qwen3.5-4B | 77.79 [76.15, 79.44] | 9.81 [8.51, 11.15] | 73.88 [71.04, 76.61] | 47 |
| Gemma-4-E4B | 80.74 [79.25, 82.25] | 14.20 [12.91, 15.49] | 81.72 [79.25, 84.06] | 27 |
| **Frontier LLMs** | | | | |
| Gemini-2.5-Flash-Lite | 83.74 [82.53, 85.01] | 12.88 [11.75, 14.00] | 84.40 [82.05, 86.64] | 312 |
| Gemini-2.5-Flash | 84.02 [82.49, 85.51] | 11.71 [10.40, 13.10] | 79.91 [77.26, 82.58] | 361 |
| **Decision models** | | | | |
| Jev | 89.65 [88.57, 90.71] | 9.54 [8.78, 10.36] | 93.09 [91.12, 94.82] | 239 |
| OpenJev | 88.15 [86.89, 89.41] | 10.42 [9.52, 11.35] | 90.06 [87.93, 92.27] | 83 |
| Kev-4B | 81.98 [80.69, 83.27] | 18.63 [17.51, 19.68] | 89.24 [86.97, 91.21] | 46 |
| Kev-9B | 82.25 [80.86, 83.53] | 15.85 [14.74, 16.91] | 89.35 [87.21, 91.28] | 46 |
| BioDecision-4B | 77.88 [76.42, 79.38] | 9.30 [8.19, 10.40] | 88.32 [86.45, 90.13] | 41 |
| Laya-Multilingual | 32.95 [31.33, 34.43] | 30.61 [29.17, 32.17] | 18.60 [16.48, 20.93] | 12 |

This model on each task:

| task | n | accuracy [95% CI] | ECE |
|---|---:|---|---:|
| noul:triage_need (silver) | 532 | 95.11 [93.23, 96.99] | 6.14 |
| choice:specialty_referral (silver) | 824 | 95.02 [93.45, 96.36] | 3.34 |
| score:urgency_level (silver) | 1,208 | 89.16 [87.50, 90.98] | 10.11 |
| noul:symptom_presence (silver) | 325 | 86.15 [82.46, 89.54] | 4.85 |
| choice:symptom_severity (silver) | 1,066 | 86.30 [84.24, 88.37] | 3.89 |
| noul:routine_request (silver) | 102 | 85.29 [78.43, 92.16] | 9.95 |
| choice:request_guardrail (silver) | 56 | 89.29 [80.36, 96.43] | 5.30 |
| choice:health_topic (silver) | 237 | 92.83 [89.45, 95.78] | 5.04 |
| noul:health_topic (silver) | 247 | 95.95 [93.12, 98.38] | 9.65 |
| choice:diagnosis_coding (gold, DiaMed) | 154 | 68.83 [61.69, 75.99] | 12.24 |
| choice:article_specialty (gold, MORFITT) | 745 | 62.01 [58.65, 65.23] | 15.68 |
| mixed:audited_patient_messages (audit) | 200 | 89.00 [85.00, 93.00] | 7.20 |

- All scores are percentages. Labels: silver = Qwen3.8-27B and Qwen3.5-122B-A10B agree on the answer, gold = human labels of the dataset, audit = blind relabelling by another model.
- OpenJev is a fine-tune of Qwen3.8-27B, one of the two teachers behind the silver labels, so on the 9 silver tasks it is partly scored against its own teacher's answers.
- 95% CIs from 1,000 bootstrap resamples of the items in each task. Order consistency: share of answers that stay the same when the options of the 6 choice tasks are shown in 3 different orders.
- Latency: median time for one request, on one H100 in BF16 (OpenJev in FP8), without inference optimisation. Jev and Gemini are timed from the client, network included.

## 🏋️ Training

LoRA (rank 16, alpha 32, attention and MLP projections of the language model) on medgemma-1.5-4b-it, 1 epoch at learning rate 1e-4 on [docto-decision-data-fr-v0.1](https://huggingface.co/datasets/bofenghuang/docto-decision-data-fr-v0.1) (943,013 decision records, 108 tasks). The target of each record is half the correct answer and half the answer distribution of Qwen3.8-27B.

## ⚠️ Limitations

- This is a research model, not a medical device, and it has not been validated clinically. Keep a human in the loop.
- It can under-estimate urgency. Do not use it as the only safety net for triage.
- It is weaker on tasks far from the training tasks, and on medical knowledge questions it stays well below large LLMs.
- Most training labels come from one model family (Qwen), so the model shares its conventions and its errors.
- French only. Check calibration on your own task before choosing a threshold.
- Use is subject to the [Health AI Developer Foundations terms](https://developers.google.com/health-ai-developer-foundations/terms) of MedGemma, including their use restrictions (see `NOTICE`).
