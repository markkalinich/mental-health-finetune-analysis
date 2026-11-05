---
language: ja
library_name: transformers
license: apache-2.0
pipeline_tag: automatic-speech-recognition
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
widget:
- example_title: Sample 1
  src: https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2/resolve/main/sample_audio/sample_diarization_japanese.mp3
---

# Kotoba-Whisper-v2.2
_Kotoba-Whisper-v2.2_ is a Japanese ASR model based on [kotoba-tech/kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0), with 
additional postprocessing stacks integrated as [`pipeline`](https://huggingface.co/docs/transformers/en/main_classes/pipelines). The new features includes 
(i) speaker diarization with [diarizers](https://huggingface.co/diarizers-community/speaker-segmentation-fine-tuned-callhome-jpn)
and (ii) adding punctuation with [punctuators](https://github.com/1-800-BAD-CODE/punctuators/tree/main). 
The pipeline has been developed through the collaboration between [Asahi Ushio](https://asahiushio.com) and [Kotoba Technologies](https://twitter.com/kotoba_tech)

## Transformers Usage
Kotoba-Whisper-v2.2 is supported in the Hugging Face 🤗 Transformers library from version 4.39 onwards. To run the model, first 
install the latest version of Transformers.

```bash
pip install --upgrade pip
pip install --upgrade transformers accelerate torchaudio
pip install "punctuators==0.0.5"
pip install "pyannote.audio"
pip install git+https://github.com/huggingface/diarizers.git
```

To load pre-trained diarization models from the Hub, you'll first need to accept the terms-of-use for the following two models:
1. [pyannote/segmentation-3.0](https://hf.co/pyannote/segmentation-3.0)
2. [pyannote/speaker-diarization-3.1](https://hf.co/pyannote/speaker-diarization-3.1)

And subsequently use a Hugging Face authentication token to log in with: 

```
huggingface-cli login
```


### Transcription with Diarization
The model can be used with the [`pipeline`](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.AutomaticSpeechRecognitionPipeline).

- Download an audio sample.
```shell
wget https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2/resolve/main/sample_audio/sample_diarization_japanese.mp3
```

- Run the model via pipeline.

```python
import torch
from transformers import pipeline

# config
model_id = "kotoba-tech/kotoba-whisper-v2.2"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}


# load model
pipe = pipeline(
    model=model_id,
    torch_dtype=torch_dtype,
    device=device,
    model_kwargs=model_kwargs,
    batch_size=8,
    trust_remote_code=True,
)

# run inference
result = pipe("sample_diarization_japanese.mp3", chunk_length_s=15)
print(result)
>>> {
 'chunks/SPEAKER_00': [{'speaker_id': 'SPEAKER_00', 'text': '水をマレーシアから買わなくてはならないのです', 'timestamp': [22.1, 24.97]}],
 'chunks/SPEAKER_01': [{'speaker_id': 'SPEAKER_01', 'text': 'これも先ほどがずっと言っている自分の感覚的には大丈夫ですけれども', 'timestamp': [0.03, 13.85]},
                      {'speaker_id': 'SPEAKER_01', 'text': '今は屋外の気温', 'timestamp': [5.03, 18.85]},
                      {'speaker_id': 'SPEAKER_01', 'text': '昼も夜も上がってますので', 'timestamp': [7.63, 21.45]},
                      {'speaker_id': 'SPEAKER_01', 'text': '空気の入れ替えだけではかえって人が上がってきます', 'timestamp': [9.91, 23.73]}],
 'chunks/SPEAKER_02': [{'speaker_id': 'SPEAKER_02', 'text': '愚直にやっぱりその街の良さをアピールしていくという', 'timestamp': [13.48, 22.1]},
                      {'speaker_id': 'SPEAKER_02', 'text': 'そういう姿勢が基本にあった上での', 'timestamp': [17.26, 25.88]},
                      {'speaker_id': 'SPEAKER_02', 'text': 'こういうPR作戦だと思うんですよね', 'timestamp': [19.86, 28.48]}],
 'chunks': [{'speaker_id': 'SPEAKER_00', 'text': '水をマレーシアから買わなくてはならないのです', 'timestamp': [22.1, 24.97]},
            {'speaker_id': 'SPEAKER_01', 'text': 'これも先ほどがずっと言っている自分の感覚的には大丈夫ですけれども', 'timestamp': [0.03, 13.85]},
            {'speaker_id': 'SPEAKER_01', 'text': '今は屋外の気温', 'timestamp': [5.03, 18.85]},
            {'speaker_id': 'SPEAKER_01', 'text': '昼も夜も上がってますので', 'timestamp': [7.63, 21.45]},
            {'speaker_id': 'SPEAKER_01', 'text': '空気の入れ替えだけではかえって人が上がってきます', 'timestamp': [9.91, 23.73]},
            {'speaker_id': 'SPEAKER_02', 'text': '愚直にやっぱりその街の良さをアピールしていくという', 'timestamp': [13.48, 22.1]},
            {'speaker_id': 'SPEAKER_02', 'text': 'そういう姿勢が基本にあった上での', 'timestamp': [17.26, 25.88]},
            {'speaker_id': 'SPEAKER_02', 'text': 'こういうPR作戦だと思うんですよね', 'timestamp': [19.86, 28.48]}],
 'speaker_ids': ['SPEAKER_00', 'SPEAKER_01', 'SPEAKER_02'],
 'text/SPEAKER_00': '水をマレーシアから買わなくてはならないのです',
 'text/SPEAKER_01': 'これも先ほどがずっと言っている自分の感覚的には大丈夫ですけれども今は屋外の気温昼も夜も上がってますので空気の入れ替えだけではかえって人が上がってきます',
 'text/SPEAKER_02': '愚直にやっぱりその街の良さをアピールしていくというそういう姿勢が基本にあった上でのこういうPR作戦だと思うんですよね'
}
```

- To activate punctuator:
```diff
-     result = pipe("sample_diarization_japanese.mp3")
+     result = pipe("sample_diarization_japanese.mp3", add_punctuation=True)
```
The punctuator will be applied to `text/*` feature. Eg.)
```
'text/SPEAKER_00': '水をマレーシアから買わなくてはならないのです。'
'text/SPEAKER_01': 'これも先ほどがずっと言っている。自分の感覚的には大丈夫です。けれども。今は屋外の気温、昼も夜も上がってますので、空気の入れ替えだけではかえって人が上がってきます。'
'text/SPEAKER_02': '愚直にその街の良さをアピールしていくという。そういう姿勢が基本にあった上での、こういうPR作戦だと思うんですよね。'
```

- To contorol the number of speakers (see [here](https://huggingface.co/pyannote/speaker-diarization-3.1#controlling-the-number-of-speakers)):
```diff
-     result = pipe("sample_diarization_japanese.mp3")
+     result = pipe("sample_diarization_japanese.mp3", num_speakers=3)
```
or
```diff
-     result = pipe("sample_diarization_japanese.mp3")
+     result = pipe("sample_diarization_japanese.mp3", min_speakers=2, max_speakers=5)
```

- To add silence before/after the audio sometimes improves the transcription quality:
```diff
-     result = pipe("sample_diarization_japanese.mp3")
+     result = pipe("sample_diarization_japanese.mp3", add_silence_end=0.5, add_silence_start=0.5)  # adding 0.5 sec silence to before/after the audio
```

### Flash Attention 2
We recommend using [Flash-Attention 2](https://huggingface.co/docs/transformers/main/en/perf_infer_gpu_one#flashattention-2) 
if your GPU allows for it. To do so, you first need to install [Flash Attention](https://github.com/Dao-AILab/flash-attention):

```
pip install flash-attn --no-build-isolation
```

Then pass `attn_implementation="flash_attention_2"` to `from_pretrained`:

```diff
- model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}
+ model_kwargs = {"attn_implementation": "flash_attention_2"} if torch.cuda.is_available() else {}
```


## Acknowledgements
* [OpenAI](https://openai.com/) for the Whisper [model](https://huggingface.co/openai/whisper-large-v3).
* Hugging Face 🤗 [Transformers](https://github.com/huggingface/transformers) for the model integration.
* Hugging Face 🤗 for the [Distil-Whisper codebase](https://github.com/huggingface/distil-whisper).
* [Reazon Human Interaction Lab](https://research.reazon.jp/) for the [ReazonSpeech dataset](https://huggingface.co/datasets/reazon-research/reazonspeech).