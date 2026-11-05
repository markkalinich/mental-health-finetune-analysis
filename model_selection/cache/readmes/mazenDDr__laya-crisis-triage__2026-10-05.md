---
license: cc-by-nc-sa-4.0
base_model: convaiinnovations/laya
language: [en, fr, es, it, pt, tl, ht]
pipeline_tag: text-classification
tags: [laya, crisis-informatics, humanitarian, disaster-response, calibration, multilingual]
datasets:
  - QCRI/HumAID-events
  - QCRI/CrisisBench-all-lang
  - nlp-thedeep/humset
  - community-datasets/disaster_response_messages
---

# laya-crisis-triage

[Laya](https://github.com/NandhaKishorM/laya)'s multilingual checkpoint (mmBERT-base, 322M),
fine-tuned to triage disaster messages: what people need, which kind of information a crisis
tweet gives, and which humanitarian sector a report excerpt is about. One model answers all of
these typed questions in one forward pass, in any of the languages above, with calibrated
probabilities.

Research artefact from [crisis-triage](https://github.com/mazenDDr/crisis-triage), where every number below comes from. **It is
not an emergency system:** keep a human in the loop for any real decision about people in need.

## Use

```python
# pip install laya==0.3.5
import laya

agent = laya.load("mazenDDr/laya-crisis-triage")
questions = {
    "kind": {
        "type": "choice",
        "instructions": "Which kind of information does this crisis message give?",
        "criteria": {
            "requests or needs": "someone asks for help, food, water or supplies",
            "people affected": "people injured, killed, missing or affected",
            "infrastructure damage": "damaged buildings, roads, power or water supply",
            "displaced or evacuated": "people evacuated, displaced or in shelters",
            "donations and rescue work": "rescue work, volunteering, donations, aid response",
            "caution and advice": "warnings, advice, safety instructions",
            "sympathy and support": "prayers, sympathy, emotional support",
            "other or not humanitarian": "other news, or not about the disaster"
        }
    },
    "water_food": {"type": "noul", "instructions": "Does the sender ask for water food (drinking water or food)?"},
}
res = agent.predict({"message": "We have had no drinking water for two days in Leogane"}, questions)
print(res["answers"]["kind"]["probabilities"], res["answers"]["water_food"]["noul"])
```

It was trained on exactly these question wordings (and the other needs and sectors in
[`questions.py`](https://github.com/mazenDDr/crisis-triage/blob/main/src/crisis_triage/questions.py)). Other wordings still work,
since it is Laya, but were not measured.

## Results on held-out test data

Every system answers the same test messages. The splits are by time where there are several
disasters (tuned on 2016-17 / 2011-12 events, tested on later ones). Macro-F1 is over 8 shared
classes; mean AUC is over 4 needs (Haiti) or 10 sectors (HumSet). 95% intervals and paired
differences are in [`results/t05_test.json`](https://github.com/mazenDDr/crisis-triage/blob/main/results/t05_test.json).

| Test set | n | Metric | **this model** | Laya zero-shot | e5 + LR | Qwen3-4B | Gemma-3-4B |
|---|---|---|---|---|---|---|---|
| Haiti SMS, Creole/French original | 996 | mean AUC | 0.838 | 0.669 | 0.873 | 0.762 | 0.813 |
| Haiti SMS, NLLB-600M translation | 996 | mean AUC | 0.844 | 0.772 | — | 0.822 | 0.851 |
| Haiti SMS, human translation | 996 | mean AUC | 0.905 | 0.849 | — | 0.879 | 0.927 |
| HumAID tweets, 2018-19 disasters | 8,000 | macro-F1 | 0.725 | 0.568 | 0.716 | 0.642 | 0.597 |
| CrisisBench tweets, es/fr/it/pt/tl | 5,534 | macro-F1 | 0.453 | 0.280 | 0.410 | 0.426 | 0.387 |
| HumSet report excerpts, en/fr/es | 3,000 | mean AUC | 0.934 | 0.691 | 0.956 | 0.932 | 0.910 |

Calibration error (ECE, lower is better):

| Test set | **this model** | Laya zero-shot | e5 + LR | Qwen3-4B | Gemma-3-4B |
|---|---|---|---|---|---|
| Haiti SMS, Creole/French original | 0.010 | 0.197 | 0.016 | 0.145 | 0.284 |
| HumAID tweets, 2018-19 disasters | 0.010 | 0.181 | 0.012 | 0.284 | 0.339 |
| CrisisBench tweets, es/fr/it/pt/tl | 0.087 | 0.194 | 0.095 | 0.447 | 0.516 |
| HumSet report excerpts, en/fr/es | 0.010 | 0.125 | 0.006 | 0.078 | 0.158 |

Baselines: e5 + LR is multilingual-e5-base embeddings with logistic regression, trained on the
same dev data, with its regularisation chosen by cross-validation on dev. Qwen3-4B-Instruct-2507 and Gemma-3-4B-it are zero-shot, asked the same
questions and read out from next-token probabilities.

## Training

- Base: `convaiinnovations/laya`, `multilingual` subfolder.
- Data: dev splits only, 40,737 (message, question) examples: Haiti 2010 SMS
  needs (original or English text), HumAID and CrisisBench tweet classes, HumSet sectors. A fixed
  dev sample was held out for the temperature fit and the decision thresholds; test data was
  never used.
- Recipe: Laya's own (RLCD policy gradient with a proper-scoring reward, plus soft
  cross-entropy), 2 epochs, 17 minutes
  on one RTX 5060 Ti, bf16.
- Held-out loss: yes/no 0.6095 → 0.1466,
  choice 2.0975 → 0.7771
  (before → after, with the fitted temperature).

## Limitations

- **Urgency was not trained and drifted:** on the Haiti SMS, urgency AUC is 0.527
  for this model vs 0.573 for zero-shot Laya (against a stand-in label built from rescue
  and medical needs).
- The Haiti SMS set is one event with a message-level split, and HumSet's test shares projects
  with its training data; both favour trained models. HumAID and CrisisBench are the
  new-disaster tests.
- Only 11 Haiti test messages ask for rescue, so that need's score is noisy.
- Haitian Creole is read far better through a translation (see the repository).
- Speed, one message at a time on an RTX 5060 Ti under WSL: 16-53 ms (the GPU is bimodal
  between runs).

## Licence

CC BY-NC-SA 4.0, because the model was trained on HumAID and CrisisBench (CC BY-NC-SA 4.0).
The base model Laya is Apache-2.0 and HumSet is Apache-2.0. The Disaster Response Messages
dataset (Appen) states no licence on its dataset card.
