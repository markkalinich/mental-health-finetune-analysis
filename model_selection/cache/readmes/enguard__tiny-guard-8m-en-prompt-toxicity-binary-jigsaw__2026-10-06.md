---
base_model: minishlab/potion-base-8m
datasets:
- google/jigsaw_toxicity_pred
library_name: model2vec
license: mit
model_name: enguard/tiny-guard-8m-en-prompt-toxicity-binary-jigsaw
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/tiny-guard-8m-en-prompt-toxicity-binary-jigsaw

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-base-8m](https://huggingface.co/minishlab/potion-base-8m) for the prompt-toxicity-binary found in the [google/jigsaw_toxicity_pred](https://huggingface.co/datasets/google/jigsaw_toxicity_pred) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/tiny-guard-8m-en-prompt-toxicity-binary-jigsaw"
)


# Supports single texts. Format input as a single text:
text = "Example sentence"

model.predict([text])
model.predict_proba([text])

```

## Why should you use these models?

- Optimized for precision to reduce false positives.
- Extremely fast inference: up to x500 faster than SetFit.

## This model variant

Below is a quick overview of the model variant and core metrics.

| Field | Value |
|---|---|
| Classifies | prompt-toxicity-binary |
| Base Model | [minishlab/potion-base-8m](https://huggingface.co/minishlab/potion-base-8m) |
| Precision | 0.9514 |
| Recall | 0.8297 |
| F1 | 0.8864 |

### Confusion Matrix

| True \ Predicted | FAIL | PASS |
| --- | --- | --- |
| **FAIL** | 1291 | 265 |
| **PASS** | 66 | 1437 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "FAIL": {
    "precision": 0.9513633014001474,
    "recall": 0.8296915167095116,
    "f1-score": 0.8863714383796774,
    "support": 1556.0
  },
  "PASS": {
    "precision": 0.8443008225616921,
    "recall": 0.9560878243512974,
    "f1-score": 0.8967238689547582,
    "support": 1503.0
  },
  "accuracy": 0.8917947041516836,
  "macro avg": {
    "precision": 0.8978320619809197,
    "recall": 0.8928896705304045,
    "f1-score": 0.8915476536672178,
    "support": 3059.0
  },
  "weighted avg": {
    "precision": 0.8987595401401937,
    "recall": 0.8917947041516836,
    "f1-score": 0.8914579709571034,
    "support": 3059.0
  }
}
```
</details>


<details>
<summary><b>Sample Predictions</b></summary>

| Text | True Label | Predicted Label |
|------|------------|-----------------|
| ":::SLR Chronology bibliography is complete<br><br>Hi, MurderWatcher1. This is Paul1513 again. This is to let you know that I have completed the SLR Chronology bibliography for you and that I am going to try to upload  a PDF copy to your Talk page as soon as I finish this note. This may take a while, because I've never uploaded a PDF before.<br><br>You're absolutely right; it would be great if some of the old Modern Photography stuff could be added to Wikipedia. However, you can be sure that they're still under copyright. (Pre-1978 American ""work-for-hire"" copyrights are generally 75 years; 1978 and on, 95 years.) The real question is: Who OWNS the copyright today? Since Modern went under, there have been many media company sales and resales - the present copyright holder would be hell to uncover and ask permission. In fact, the current owner might not even know that it owns Modern's copyrights. ""Orphaned"" copyrights are a major unresolved ""fair use"" issue in the information age.<br><br>Speaking of first cameras: mine was a simple Vivitar 110 point-and-shoot. My parents gave it to me for getting straight A's  in the 5th grade. It was, of course, a bad camera, but it opened up a world of possibilities. From the Vivitar, I eventually learned about the existence of the Pentax Auto 110 SLR. It was then one step to 35 mm SLRs and I got a Nikon FE2 in 1983. The FE2 is also the reason why the bulk of my Modern Photography magazine citations begin around 1983.<br><br>I'm sorry to hear about your disputes with the Admins over your non-photography Wkipedia entries. It would be unfortunate if you felt compelled to end your Wikipedia activities over them. Perhaps you could start a blog or create a MySpace or Facebook page to air these issues without worrying about what the Admins want. However, I will respect whatever your decision is, as I fully understand that the most sophisticated machine is nothing next to a human life.<br><br>You can reach me on my Talk page. Thanks Muchly  <br><br>" | PASS | PASS |
| Are you deaf or blind? I repeat. It started in late 2009, and collapsed in mid 2010, as supported by cites and polls. | FAIL | PASS |
| "<br>Thanks for your note. I've been reporting accounts like these for over a year now and they all almost always get an indefinite block since they are vandalism only accounts. Blocks are necessary in these cases as it is not known when any person behind these accounts may come back and vandalize again. I see you have again removed these reports from the noticeboard which I have to again disagree with. therefore I kindly request you to put them back on the noticeboard for another administrator to review. ~ (talk) " | PASS | PASS |
| SOMEGUY1221 LIKES TO SUCK LARGE HARD PENIS. | FAIL | FAIL |
| "<br>Well, you're using criteria that you have decided constitute a legitimate decision procedure for establishing whether something is Israeli. Content decisions can't be made that way here. I have a decision procedure that enables me to decide who is an idiot and yet annoyingly I am not allowed to deploy it in articles about living people who clearly meet the criteria. ''' - talk''' " | FAIL | PASS |
| ":::SLR Chronology bibliography is complete<br><br>Hi, MurderWatcher1. This is Paul1513 again. This is to let you know that I have completed the SLR Chronology bibliography for you and that I am going to try to upload  a PDF copy to your Talk page as soon as I finish this note. This may take a while, because I've never uploaded a PDF before.<br><br>You're absolutely right; it would be great if some of the old Modern Photography stuff could be added to Wikipedia. However, you can be sure that they're still under copyright. (Pre-1978 American ""work-for-hire"" copyrights are generally 75 years; 1978 and on, 95 years.) The real question is: Who OWNS the copyright today? Since Modern went under, there have been many media company sales and resales - the present copyright holder would be hell to uncover and ask permission. In fact, the current owner might not even know that it owns Modern's copyrights. ""Orphaned"" copyrights are a major unresolved ""fair use"" issue in the information age.<br><br>Speaking of first cameras: mine was a simple Vivitar 110 point-and-shoot. My parents gave it to me for getting straight A's  in the 5th grade. It was, of course, a bad camera, but it opened up a world of possibilities. From the Vivitar, I eventually learned about the existence of the Pentax Auto 110 SLR. It was then one step to 35 mm SLRs and I got a Nikon FE2 in 1983. The FE2 is also the reason why the bulk of my Modern Photography magazine citations begin around 1983.<br><br>I'm sorry to hear about your disputes with the Admins over your non-photography Wkipedia entries. It would be unfortunate if you felt compelled to end your Wikipedia activities over them. Perhaps you could start a blog or create a MySpace or Facebook page to air these issues without worrying about what the Admins want. However, I will respect whatever your decision is, as I fully understand that the most sophisticated machine is nothing next to a human life.<br><br>You can reach me on my Talk page. Thanks Muchly  <br><br>" | PASS | PASS |
</details>


<details>
<summary><b>Prediction Speed Benchmarks</b></summary>

| Dataset Size | Time (seconds) | Predictions/Second |
|--------------|----------------|---------------------|
| 1 | 0.0008 | 1298.55 |
| 1000 | 0.1127 | 8873.66 |
| 3059 | 0.3655 | 8368.35 |
</details>


## Other model variants

Below is a general overview of the best-performing models for each dataset variant.

| Classifies | Model | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| prompt-toxicity-binary | [enguard/tiny-guard-2m-en-prompt-toxicity-binary-jigsaw](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-toxicity-binary-jigsaw) | 0.9531 | 0.7699 | 0.8518 |
| prompt-toxicity-binary | [enguard/tiny-guard-4m-en-prompt-toxicity-binary-jigsaw](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-toxicity-binary-jigsaw) | 0.9507 | 0.8303 | 0.8864 |
| prompt-toxicity-binary | [enguard/tiny-guard-8m-en-prompt-toxicity-binary-jigsaw](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-toxicity-binary-jigsaw) | 0.9514 | 0.8297 | 0.8864 |
| prompt-toxicity-binary | [enguard/small-guard-32m-en-prompt-toxicity-binary-jigsaw](https://huggingface.co/enguard/small-guard-32m-en-prompt-toxicity-binary-jigsaw) | 0.9403 | 0.8605 | 0.8987 |
| prompt-toxicity-binary | [enguard/medium-guard-128m-xx-prompt-toxicity-binary-jigsaw](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-toxicity-binary-jigsaw) | 0.9111 | 0.8625 | 0.8861 |

## Resources

- Awesome AI Guardrails: <https://github.com/enguard-ai/awesome-ai-guardails>
- Model2Vec: https://github.com/MinishLab/model2vec
- Docs: https://minish.ai/packages/model2vec/introduction

## Citation

If you use this model, please cite Model2Vec:

```
@software{minishlab2024model2vec,
  author       = {Stephan Tulkens and {van Dongen}, Thomas},
  title        = {Model2Vec: Fast State-of-the-Art Static Embeddings},
  year         = {2024},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17270888},
  url          = {https://github.com/MinishLab/model2vec},
  license      = {MIT}
}
```