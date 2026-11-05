---
language:
- ru
- en
- de
- pl
- it
- fr
- es
- bn
license: apache-2.0
library_name: transformers
pipeline_tag: audio-classification
base_model: Aniemore/wav2vec2-bert-tiny2-s-emotion-russian-resd
base_model_relation: finetune
datasets:
- Aniemore/resd
- Aniemore/resd_annotated
- amu-cai/CAMEO
tags:
- audio-classification
- emotion-recognition
- speech-emotion-recognition
- speech
- multilingual
- russian
- quantized
- compressed-tensors
- int8
- fp8
- int4
metrics:
- f1
- accuracy
- recall
model-index:
- name: wav2vec2-bert-tiny2-s-emotion-v1-crosslingual
  results:
  - task:
      name: Speech Emotion Recognition
      type: audio-classification
    dataset:
      name: RESD test
      type: Aniemore/resd
    metrics:
    - name: Macro F1
      type: f1
      value: 0.6226
    - name: Unweighted accuracy
      type: recall
      value: 0.6324
  - task:
      name: Speech Emotion Recognition
      type: audio-classification
    dataset:
      name: Dusha podcast test
      type: dusha
    metrics:
    - name: Macro F1
      type: f1
      value: 0.4033
    - name: Unweighted accuracy
      type: recall
      value: 0.6644
  - task:
      name: Speech Emotion Recognition
      type: audio-classification
    dataset:
      name: CAMEO test
      type: amu-cai/CAMEO
    metrics:
    - name: Macro F1
      type: f1
      value: 0.5868
    - name: Unweighted accuracy
      type: recall
      value: 0.5819
---

<img src="assets/banner.svg" alt="wav2vec2-bert-tiny2-s-emotion-v1-crosslingual" width="100%">

# wav2vec2-bert-tiny2-s-emotion-v1-crosslingual

Speech emotion recognition over seven classes &mdash; `anger`, `disgust`, `enthusiasm`, `fear`, `happiness`, `neutral`, `sadness`.

Same architecture as [`Aniemore/wav2vec2-bert-tiny2-s-emotion-russian-resd`](https://huggingface.co/Aniemore/wav2vec2-bert-tiny2-s-emotion-russian-resd), retrained on a mix of 27,939 clips spanning eight languages and three speaking registers instead of one acted Russian corpus. The point of the change is spontaneous speech: the previous release was trained only on acted dialogue, where every class is equally frequent and every utterance is performed, and real speech is neither.

Quantized builds ship in the same repository under `int8/`, `fp8/` and `int4/`.

## Results

| test set | what it is | macro-F1 | UA | WA | previous release |
|---|---|---:|---:|---:|---:|
| RESD test | acted Russian, 7 balanced classes | **0.6226** | 0.6324 | 0.6357 | 0.7228 |
| Dusha podcast test | spontaneous Russian, majority neutral | **0.4033** | 0.6644 | 0.7701 | 0.1361 |
| CAMEO test | 7 non-Russian languages | **0.5868** | 0.5819 | 0.6734 | 0.2589 |

<img src="assets/panel.svg" alt="Panel results" width="760">

Read the first two rows together. The acted score goes down and the spontaneous score goes up; both follow from the same change, and which one matters is a deployment question. If your audio is read or performed speech, the previous release may still suit you better.

<details><summary>About the CAMEO row</summary>

CAMEO ships no train/test partition, and the usual way to make one &mdash; a random split over clips &mdash; puts nearly every test speaker into training as well: three of its twelve constituent corpora contain a single speaker each, so no clip-level split of them can be speaker-disjoint even in principle. The number above is reported for completeness. Treat it as an in-domain figure, not as evidence of cross-lingual transfer.

</details>

<details>
<summary><b>Per class, across the panel</b> &mdash; recall and F1 for every class on every test set</summary>

<img src="assets/classes.svg" alt="Per-class recall and F1" width="100%">

Each card leads with the macro-F1 for that set; the rows are the detail behind it. Both per-class numbers are shown because they disagree in a way that matters: recall rewards a class the model over-predicts, so on the spontaneous set the minority classes reach decent recall at poor F1 &mdash; most clips called `sad` there are not sad. If you are going to act on one class, read its F1.

Each set keeps its own class list: the spontaneous corpus has four classes and the other two have seven, and there is no correspondence between `positive` and any single one of `happiness`/`enthusiasm` to line them up with.

</details>

### Per-class recall on spontaneous speech

| class | this model | previous release |
|---|---:|---:|
| `angry` | 0.6886 | 0.6228 |
| `neutral` | 0.7844 | 0.2306 |
| `positive` | 0.5048 | 0.0288 |
| `sad` | 0.6796 | 0.1553 |

`neutral` carries most of real speech and is the class the previous release missed.

## Quantized variants

| subfolder | scheme | weights | vs fp32 | macro-F1 | UA | WA |
|---|---|---:|---:|---:|---:|---:|
| _(root)_ | fp32 | 1318 MiB | 1.0x | 0.6226 | 0.6324 | 0.6357 |
| `int8` | W8A16 | 463 MiB | 2.8x smaller | 0.6226 | 0.6324 | 0.6357 |
| `fp8` | W8A16-float | 448 MiB | 2.9x smaller | 0.6139 | 0.6247 | 0.6286 |
| `int4` | W4A16_ASYM | 320 MiB | 4.1x smaller | 0.6213 | 0.6320 | 0.6357 |

<img src="assets/quality.svg" alt="Quality after quantization" width="760">

<img src="assets/size.svg" alt="Weights on disk" width="760">

Weight-only, round-to-nearest, no calibration. Every variant lands within the seed spread of the fp32 parent on RESD test, so the choice is about download size rather than about quality.

## Training data

| corpus | clips | language | register |
|---|---:|---|---|
| RESD | 948 | Russian | acted dialogue |
| Dusha crowd | 6,800 | Russian | acted, crowd-sourced |
| CAMEO | 6,800 | 7 languages | 12 corpora, no Russian |
| Dusha podcast | 6,060 | Russian | spontaneous podcast speech |
| IEMOCAP | 4,735 | English | elicited dyadic sessions |
| ASVP-ESD | 2,596 | multilingual | mixed register |
| **total** | **27,939** | 8 languages | 3 registers |

A slice is held out of every corpus in the mix, in the same proportion, and model selection is on that held-out split &mdash; never on any of the test sets above. Labels are unified to seven classes; four-class corpora are mapped upward and scored on the classes they actually contain.

## Usage

```python
import torch, librosa
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor

repo = "Aniemore/wav2vec2-bert-tiny2-s-emotion-v1-crosslingual"
model = AutoModelForAudioClassification.from_pretrained(repo).eval()
fe = AutoFeatureExtractor.from_pretrained(repo)

# Resample to 16 kHz. Do not skip it: RESD itself ships at 44.1 kHz,
# and handing the model 44.1 kHz audio while telling the extractor it
# is 16 kHz stretches time 2.8x and silently changes the answer.
wav, _ = librosa.load("clip.wav", sr=16000, mono=True)
x = fe(wav, sampling_rate=16000, return_tensors="pt", padding=True)
with torch.no_grad():
    probs = model(**x).logits.softmax(-1)[0]
print({model.config.id2label[i]: round(p.item(), 3) for i, p in enumerate(probs)})
```

For a quantized build, name the subfolder &mdash; only that subfolder is downloaded:

```python
model = AutoModelForAudioClassification.from_pretrained(
    repo, subfolder="int8").eval()          # or "fp8", "int4"
fe = AutoFeatureExtractor.from_pretrained(repo, subfolder="int8")
```

## Limitations

- Scores are the mean of two seeds; the seed spread on the 280-clip RESD split is ±0.03&ndash;0.05, so differences smaller than that are not differences.
- The spontaneous set has four classes where the model has seven, so its numbers are computed over a mapped label space and are not comparable to seven-class figures.
- Spontaneous scores are at zero decision bias. Calibrating the `neutral` threshold on your own development split will move them.
- This is a bimodal checkpoint: it takes a transcript alongside the audio. The transcripts used in training and evaluation are corpus-provided and clean, which ASR output is not.
- Inherited from [`facebook/wav2vec2-large-xlsr-53 + cointegrated/rubert-tiny2`](https://huggingface.co/facebook/wav2vec2-large-xlsr-53); the licence follows the base model.

