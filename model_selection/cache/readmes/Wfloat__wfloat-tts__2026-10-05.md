---
license: mit
language:
- en
pipeline_tag: text-to-speech
tags:
- tts
- vits
- piper
- emotion
---

# wfloat-tts

`wfloat-tts` is a lightweight multi-speaker English VITS text-to-speech model with speaker, emotion, and intensity control. Includes [samples](https://huggingface.co/Wfloat/wfloat-tts#sample-outputs).

## On-Device packages

This Hugging Face repo contains the model files. Wfloat also ships packages that distribute and run `wfloat-tts` locally on the user's device:

- [Web](https://github.com/wfloat/wfloat-web) for running locally in the browser, including mobile browsers
- [React Native](https://github.com/wfloat/react-native-wfloat) for running locally in iOS and Android apps
- [Python](https://github.com/wfloat/wfloat-python) for running in Python environments

Missing the platform or framework you need? [Please request it!](https://docs.google.com/forms/d/e/1FAIpQLScLjcb4lkouSQ54ZWDKJ1xlCkUpBFamF1zKRO3fno1vp1Y_IQ/viewform?usp=preview)

## Sample Outputs

### `mad_scientist_woman` surprise

- Audio: [samples/08_mad_scientist_woman_surprise_080.wav](https://huggingface.co/Wfloat/wfloat-tts/resolve/main/samples/08_mad_scientist_woman_surprise_080.wav)
- Input text: "No, no, that's not possible. The formula should have crystallized, but it adapted instead. Do you realize what that means for the rest of my work?"
- `sid`: `7`
- `emotion`: `surprise`
- `intensity`: `0.8`

<audio controls>
  <source src="https://huggingface.co/Wfloat/wfloat-tts/resolve/main/samples/08_mad_scientist_woman_surprise_080.wav" type="audio/wav">
</audio>

### `fun_hero_woman` joy

- Audio: [samples/04_fun_hero_woman_joy_070.wav](https://huggingface.co/Wfloat/wfloat-tts/resolve/main/samples/04_fun_hero_woman_joy_070.wav)
- Input text: "Come on, keep up! The crowd is cheering."
- `sid`: `3`
- `emotion`: `joy`
- `intensity`: `0.7`

<audio controls>
  <source src="https://huggingface.co/Wfloat/wfloat-tts/resolve/main/samples/04_fun_hero_woman_joy_070.wav" type="audio/wav">
</audio>

### `strong_hero_man` anger

- Audio: [samples/05_strong_hero_man_anger_080.wav](https://huggingface.co/Wfloat/wfloat-tts/resolve/main/samples/05_strong_hero_man_anger_080.wav)
- Input text: "Enough. You had your warning, and you kept pushing innocent people around. Take one more step, and I end this."
- `sid`: `4`
- `emotion`: `anger`
- `intensity`: `0.8`

<audio controls>
  <source src="https://huggingface.co/Wfloat/wfloat-tts/resolve/main/samples/05_strong_hero_man_anger_080.wav" type="audio/wav">
</audio>

Find more examples in the [samples folder](https://huggingface.co/Wfloat/wfloat-tts/tree/main/samples).

## Inputs

The intended inference inputs are:

- `text`: the utterance to synthesize
- `sid`: numeric speaker id
- `emotion`: emotion label
- `intensity`: value from `0.0` to `1.0`

You do not need to pass raw control symbols. The Python helper converts `emotion` and `intensity` into the control tokens the model was trained on.

## Install

For running the model from Hugging Face. Official Python package: [wfloat-python](https://github.com/wfloat/wfloat-python).

```bash
pip install -e .
pip install "piper-phonemize==1.3.0" -f https://k2-fsa.github.io/icefall/piper_phonemize
```

Runtime dependencies:

- `torch`
- `numpy`
- `safetensors`
- `piper-phonemize`

`piper-phonemize` is installed separately because the current recommended wheels are hosted here:

- https://k2-fsa.github.io/icefall/piper_phonemize

## Python Example

```python
from wfloat_tts import load_generator, write_wave

generator = load_generator(
    checkpoint_path="model.safetensors",
    config_path="config.json",
)

audio = generator.generate(
    text="Hey there, how are you today?",
    sid=11,
    emotion="neutral",
    intensity=0.5,
)

write_wave("out.wav", audio.samples, audio.sample_rate)
```

## How It Is Conditioned

This model was trained to condition on:

- speaker id
- one emotion control token
- one intensity control token

The reference inference path processes a full utterance, appends one emotion token and one intensity token for the whole utterance, and runs synthesis over that full sequence.

## Speaker IDs

Use numeric `sid` values:

| Speaker | SID |
| --- | ---: |
| `skilled_hero_man` | 0 |
| `skilled_hero_woman` | 1 |
| `fun_hero_man` | 2 |
| `fun_hero_woman` | 3 |
| `strong_hero_man` | 4 |
| `strong_hero_woman` | 5 |
| `mad_scientist_man` | 6 |
| `mad_scientist_woman` | 7 |
| `clever_villain_man` | 8 |
| `clever_villain_woman` | 9 |
| `narrator_man` | 10 |
| `narrator_woman` | 11 |
| `wise_elder_man` | 12 |
| `wise_elder_woman` | 13 |
| `outgoing_anime_man` | 14 |
| `outgoing_anime_woman` | 15 |
| `scary_villain_man` | 16 |
| `scary_villain_woman` | 17 |
| `news_reporter_man` | 18 |
| `news_reporter_woman` | 19 |

## Emotions

Supported emotion labels:

- `neutral`
- `joy`
- `sadness`
- `anger`
- `fear`
- `surprise`
- `dismissive`
- `confusion`

`intensity` is clamped to the range `[0.0, 1.0]` and mapped to one of ten discrete intensity levels.

## Notes

- `model.safetensors` is the main inference artifact in this repo.
- `config.json` includes the token mapping needed by the processor.
- The current release uses a multi-speaker model with 20 speakers.
- Training code: [https://github.com/wfloat/piper](https://github.com/wfloat/piper)
- Checkpoint needed to resume training: [epoch=710-step=258422.ckpt](https://huggingface.co/Wfloat/wfloat-tts/blob/main/epoch%3D710-step%3D258422.ckpt).