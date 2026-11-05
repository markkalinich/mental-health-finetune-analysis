---
license: apache-2.0
library_name: transformers
pipeline_tag: zero-shot-classification
base_model: convaiinnovations/laya
base_model_relation: finetune
language:
  - en
tags:
  - laya
  - modernbert
  - decision-engine
  - multiple-choice
  - zero-shot-classification
  - cpu
  - custom_code
datasets:
  - stanfordnlp/sst2
  - google/boolq
  - nyu-mll/multi_nli
  - stanfordnlp/snli
  - fancyzhx/yelp_polarity
  - facebook/anli
  - nyu-mll/glue
  - clinc/clinc_oos
  - cardiffnlp/tweet_eval
  - jackhhao/jailbreak-classification
  - allenai/sciq
  - allenai/openbookqa
  - allenai/qasc
  - tau/commonsense_qa
widget:
  - text: The film was a complete waste of two hours.
    candidate_labels: negative, positive
model-index:
  - name: smolaya
    results:
      - task:
          type: zero-shot-classification
          name: Zero-shot classification
        dataset:
          name: SST-2
          type: stanfordnlp/sst2
          split: validation
        metrics:
          - type: accuracy
            value: 0.942
            name: Accuracy
      - task:
          type: zero-shot-classification
          name: Zero-shot classification
        dataset:
          name: ARC-Easy
          type: allenai/ai2_arc
          config: ARC-Easy
          split: test
        metrics:
          - type: accuracy
            value: 0.602
            name: Accuracy
      - task:
          type: zero-shot-classification
          name: Zero-shot classification
        dataset:
          name: BoolQ
          type: google/boolq
          split: validation
        metrics:
          - type: accuracy
            value: 0.851
            name: Accuracy
      - task:
          type: zero-shot-classification
          name: Zero-shot classification
        dataset:
          name: MNLI (matched)
          type: nyu-mll/multi_nli
          split: validation_matched
        metrics:
          - type: accuracy
            value: 0.892
            name: Accuracy
      - task:
          type: zero-shot-classification
          name: Zero-shot classification
        dataset:
          name: AG News
          type: fancyzhx/ag_news
          split: test
        metrics:
          - type: accuracy
            value: 0.929
            name: Accuracy
---


# smolaya

A smaller variant of [`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya),
the non-autoregressive typed-decision model (ask a question about a text, get a probability for each
option in one forward pass). It beats laya on all 5 evaluation tasks below while running ≈2.8× faster on CPU (int8).

- **Architecture:** identical to laya, but the ModernBERT-large encoder keeps only its **first 20 of 28
  layers**. **323M parameters** (laya: 421M). Same tokenizer, same decision head, same input format.
- **Training:** all 20 encoder layers, the embeddings and the decision head were fine-tuned on a mix of
  public labelled datasets (below).
- **Drop-in:** it loads with the `laya` package exactly like the original checkpoint.

## Usage

### With transformers (no extra package)

The repo ships its own model and pipeline code, so it runs with plain `transformers` (4.57+ or 5.x)
and `trust_remote_code=True`. The code is three short files you can read before running:
`configuration_laya.py`, `modeling_laya.py`, `pipeline_laya.py`.

```python
# pip install transformers torch
from transformers import pipeline

clf = pipeline("zero-shot-classification", model="anon767tom/smolaya", trust_remote_code=True)

clf("The film was a complete waste of two hours.", candidate_labels=["negative", "positive"])
# {'sequence': '...', 'labels': ['negative', 'positive'], 'scores': [0.9993, 0.0007]}

# your own question instead of the default "Which label best describes the text?"
clf("Transfer 500 pounds to my savings account",
    candidate_labels=["banking", "travel", "cooking"], question="What is the user's intent?")

# independent yes/no probability per label
clf("Great camera but the battery dies fast",
    candidate_labels=["camera", "battery", "price"], multi_label=True)

# the full laya question schema (choice / score / noul), several questions in one forward pass
clf("The film was a complete waste of two hours.", questions={
    "sentiment": {"type": "choice", "instructions": "What is the sentiment?", "criteria": ["negative", "positive"]},
    "stars": {"type": "score", "instructions": "How positive is it?",
              "criteria": ["very negative", "neutral", "very positive"]},
    "recommends": {"type": "noul", "instructions": "Does the reviewer recommend the film?"},
})
```

Without the pipeline:

```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("anon767tom/smolaya", trust_remote_code=True).eval()
tok = AutoTokenizer.from_pretrained("anon767tom/smolaya", trust_remote_code=True)
model.predict(tok, "The film was a complete waste of two hours.",
              {"sentiment": {"type": "choice", "instructions": "What is the sentiment?",
                             "criteria": ["negative", "positive"]}})
```

The transformers code produces the same logits as the `laya` package (maximum absolute difference 0.0
on 50 evaluation items and on end-to-end `predict` calls).

A ready-quantised CPU version is at [`anon767tom/smolaya-int8`](https://huggingface.co/anon767tom/smolaya-int8)
(456 MB instead of 646 MB, same usage).

### With the `laya` package

```python
# pip install laya==0.3.20 torch
import laya

agent = laya.load("anon767tom/smolaya")
agent.predict(
    "The film was a complete waste of two hours.",
    {"sentiment": {"type": "choice", "instructions": "What is the sentiment?",
                   "criteria": {"negative": "", "positive": ""}}},
)
# -> choice 'negative', probabilities {'negative': 0.9994, 'positive': 0.0006}
```

### Faster CPU inference (optional int8)

`quantize_int8.py` applies PyTorch dynamic per-channel int8 to the encoder's `attn.Wqkv`, `attn.Wo`
and `mlp.Wi` projections. The `mlp.Wo` projections stay in fp32: their inputs carry activation
outliers that per-tensor activation scales cannot represent, and quantising them costs several
accuracy points.

```python
from huggingface_hub import hf_hub_download
import importlib.util, laya

p = hf_hub_download("anon767tom/smolaya", "quantize_int8.py")
spec = importlib.util.spec_from_file_location("quantize_int8", p)
q = importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
agent = q.quantize(laya.load("anon767tom/smolaya", device="cpu"))
```

## Evaluation

Accuracy on 12,398 items from five public tasks, every option set presented in its original order,
one forward pass per item. Splits: SST-2 validation, ARC-Easy test, BoolQ validation, MNLI validation-matched (fixed random 3,000),
AG News test (fixed random 3,000), minus 40 items per task held back for quantisation checks. AG News and BoolQ
are known to be part of the original laya training mix. **ARC is not in the fine-tuning data of this
model**; exact duplicates of ARC questions were removed from the training mix.

| Task | n | laya | smolaya | smolaya int8 (CPU) |
|---|---|---|---|---|
| SST-2 | 832 | 0.918 | **0.942** | 0.939 |
| ARC-Easy | 2,336 | 0.511 | **0.602** | 0.596 |
| BoolQ | 3,230 | 0.835 | **0.851** | 0.849 |
| MNLI | 3,000 | 0.883 | **0.892** | 0.891 |
| AG News | 3,000 | 0.923 | **0.929** | 0.924 |
| **Pooled** | 12,398 | 0.812 | **0.839** | 0.836 |

- Pooled difference vs laya: **+2.7 pt [95% CI +2.2, +3.2]** (fp), **+2.3 pt [+1.8, +2.8]** (int8),
  paired bootstrap over items.
- int8 vs fp: −0.4 pt [−0.6, −0.1].

### Speed (CPU)

Batch size 1, 4 threads, AMD Ryzen 3 4300U (4 cores), mean seconds per item:

| | SST-2 | ARC | BoolQ | MNLI | AG News | mean |
|---|---|---|---|---|---|---|
| laya (fp32) | 0.44 | 0.57 | 1.16 | 0.71 | 0.70 | 0.71 |
| smolaya int8 | 0.14 | 0.19 | 0.45 | 0.26 | 0.25 | **0.26** (≈2.8× faster) |

### Calibration

Top-1 expected calibration error (15 bins) on the same 12,398 items, using the raw softmax over option
logits:

| | accuracy | mean confidence | ECE |
|---|---|---|---|
| laya (raw logits) | 0.812 | 0.553 | 0.261 |
| smolaya | 0.839 | 0.878 | **0.047** |

Most of the remaining error is on BoolQ, where the model is overconfident (mean confidence 0.97,
accuracy 0.85). For this reason the shipped `rl_agent_config.json` sets all temperatures to 1.0
(laya's fitted per-type temperatures do not apply to this model).

## Training details

- **Initialisation:** `convaiinnovations/laya`, encoder truncated to layers 0–19.
- **Data (~201k examples):** SST-2, BoolQ, MNLI, SNLI, Yelp Polarity, ANLI, QNLI, CLINC150 (as
  8-way intent shortlists), TweetEval offensive and hate, jailbreak-classification, SciQ, OpenBookQA,
  QASC, CommonsenseQA — training splits only, each cast into laya's `choice` format. ARC and AG News
  were excluded.
- **Objective:** 0.5 × cross-entropy on the gold label + 0.5 × KL divergence to the original laya's
  answer distribution, averaged over all cyclic shifts of the option order (so the teacher signal
  is not tied to option position).
- **Option order:** randomly permuted for every training example.
- **Optimisation:** AdamW (weight decay 0.01), LR 2e-5 encoder / 5e-5 head, 200 warmup steps then linear decay,
  batch size 16, max length 384 tokens, 6,412 steps (~103k examples seen), fp16 mixed precision on one T4 GPU.
- The act/escalate head (`act_head`) is **inherited unchanged from laya** and was not retrained.

## Limitations

- English only (the multilingual laya variant was not modified).
- Knowledge-heavy multiple choice remains weak (ARC 0.60).
- Answers still depend somewhat on option order: reversing the options changes the ARC answer on
  about 22% of items (laya: 34%).
- Confidence on yes/no reading-comprehension questions is too high (see Calibration).
- All evaluation above is on public benchmarks; validate on your own task before relying on it.

## License and attribution

Apache-2.0, following the base model. Derived from
[`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya) by Convai Innovations
(ModernBERT-large encoder by Answer.AI). Fine-tuning datasets retain their own licenses.
