---
license: apache-2.0
language:
- ar
- bg
- zh
- hr
- sr
- cs
- da
- nl
- en
- fi
- fr
- de
- el
- hu
- id
- it
- ja
- ko
- 'no'
- pl
- pt
- ro
- ru
- sk
- es
- sv
- tl
- th
- tr
- uk
---
# Roblox voice safety classifier v3

## Model description

We present a voice safety violation detection and classification
model. The model is a transformer distilled from a larger teacher
model. All the model training has been conducted with Roblox internal
voice chat datasets, using both machine and human-labeled data, with
300k hours of training data in total.

The classifier expects 16 kHz mono (or first-channel) WAV input. The
intended segment length is up to 15 seconds. Accuracy may degrade on
longer segments. The maximum supported audio duration is 30s. The
functions to load audio (`load_audio`, `load_audio_batch`, or the CLI)
truncate the audio to max 30s.

### Toxicity heads

The model outputs one score per head (sigmoid). Labels follow the
policy enum names in [config.json](config.json):
`ABUSE_TYPE_PRIVACY_ASKING_FOR_PII`, `ABUSE_TYPE_DISCRIMINATORY`,
`ABUSE_TYPE_HARASSMENT`, `ABUSE_TYPE_SEXUAL_CONTENT`,
`ABUSE_TYPE_ILLEGAL_AND_REGULATED_CONTENT`,
`ABUSE_TYPE_DATING_AND_ROMANTIC_CONTENT`, `ABUSE_TYPE_PROFANITY`,
`ABUSE_TYPE_DISRUPTIVE_AUDIO`.

See [Roblox Community Standards](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards) for how these categories relate to moderation policy.

### Supported languages

The model supports 30 languages: Arabic, Bulgarian, Chinese, Croatian,
Czech, Danish, Dutch, English, Finnish, French, German, Greek,
Hungarian, Indonesian, Italian, Japanese, Korean, Norwegian, Polish,
Portuguese, Romanian, Russian, Serbian, Slovak, Spanish, Swedish,
Tagalog, Thai, Turkish, Ukrainian.

The model provides auxiliary heads for language detection. For the
mapping of language heads to language codes, see `languages` in
[config.json](config.json). Note that Croatian and Serbian are
detected by the same language head `hr`.

### Evaluation

Metrics below are recall and precision on internal held-out sets
measuring whether the given phrase contained abuse or not. Disruptive
audio was excluded from the evaluation. Operating points were chosen
for a binary 1% false positive rate for each language.

| Language | Code | Recall | Precision |
| -------- | ---- | ------ | ----------- |
| Arabic | ar | 30.2% | 79.5% |
| Bulgarian | bg | 33.2% | 57.6% |
| Chinese | zh | 61.1% | 78.4% |
| Croatian/Serbian | hr | 37.9% | 61.3% |
| Czech | cs | 29.5% | 67.1% |
| Danish | da | 54.4% | 77.5% |
| Dutch | nl | 51.0% | 69.0% |
| English | en | 67.9% | 68.5% |
| Finnish | fi | 37.6% | 70.9% |
| French | fr | 61.8% | 68.5% |
| German | de | 67.4% | 66.5% |
| Greek | el | 29.7% | 67.3% |
| Hungarian | hu | 30.4% | 70.1% |
| Indonesian | id | 55.4% | 85.9% |
| Italian | it | 49.9% | 77.3% |
| Japanese | ja | 49.5% | 58.3% |
| Korean | ko | 59.4% | 75.1% |
| Norwegian | no | 43.9% | 71.4% |
| Polish | pl | 75.2% | 94.9% |
| Portuguese | pt | 51.0% | 61.1% |
| Romanian | ro | 34.8% | 65.1% |
| Russian | ru | 37.7% | 88.8% |
| Slovak | sk | 35.8% | 69.4% |
| Spanish | es | 59.7% | 68.7% |
| Swedish | sv | 42.1% | 70.0% |
| Tagalog | tl | 67.5% | 91.4% |
| Thai | th | 69.6% | 92.7% |
| Turkish | tr | 32.9% | 60.8% |
| Ukrainian | uk | 41.1% | 69.8% |

Comparing the languages supported by the v2 model (English, French,
German, Italian, Japanese, Korean, Portuguese, and Spanish) weighted
by Roblox voice chat language distribution, the recall improved 14%
relative and precision 5% relative with respect to
[Roblox/voice-safety-classifier-v2](https://huggingface.co/Roblox/voice-safety-classifier-v2).

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Optional — Hugging Face `AutoModel.from_pretrained` and the packaged
`VoiceToxicityClassifier` config:

```bash
pip install -r requirements-optional.txt
```

Run inference on one or more WAV files. The model directory must
contain `config.json` and `model.safetensors` (defaults to the current
directory):

```bash
python inference.py --model-dir /path/to/model_dir /path/to/audio.wav
python inference.py /path/to/audio.wav --device cuda --output results.json
```

For batch inputs and JSON output:

```bash
python inference.py --model-dir /path/to/model_dir a.wav b.wav c.wav --output results.json
```

**Python API** (see `inference.py` for full signatures):

```python
from inference import load_model, load_audio, run_inference, extract_label_scores

model, config = load_model("/path/to/model_dir")
audio = load_audio("clip.wav")
raw = run_inference(model, audio)
out = extract_label_scores(raw["probs"], raw.get("language_probs"), config, index=0)
# out["label_scores"], out.get("language_probs")
```

### Hugging Face `AutoModel`

With `transformers` installed, you can load the same checkpoint via
`AutoModel.from_pretrained`. 

```python
import json
from pathlib import Path

# you need the inference.py file to run
import inference  # registers VoiceToxicityClassifier with AutoModel
from transformers import AutoModel

from inference import extract_label_scores, load_audio, run_inference

model = AutoModel.from_pretrained("Roblox/voice-safety-classifier-v3")
audio = load_audio("clip.wav")
raw = run_inference(model, audio)
# Make human-readable output
out = extract_label_scores(raw["probs"], raw.get("language_probs"), model.config.to_dict(), index=0)
print(out)
```

Audio files must be **16 kHz** WAV (mono or stereo; first channel is used).

## License

Apache License 2.0, see [LICENSE.md](LICENSE.md).