---
language:
- ja
license: apache-2.0
library_name: transformers
tags:
- whisper
- automatic-speech-recognition
- speech-recognition
- japanese
- medical
- asr
- audio
- pytorch
- ggml
- gguf
- whisper.cpp
- quantized
base_model: openai/whisper-small
datasets:
- custom
pipeline_tag: automatic-speech-recognition
model-index:
- name: whisper-small-medical-ja
  results: []
---

# Whisper Small - Japanese Medical Terms

日本語医療用語に特化してファインチューニングした Whisper Small モデルです。

## モデル概要

| 項目 | 内容 |
|------|------|
| ベースモデル | [openai/whisper-small](https://huggingface.co/openai/whisper-small) |
| パラメータ数 | 244M |
| モデルサイズ | 922 MB (Transformers) |
| 学習言語 | 日本語 |
| 特化領域 | 医療用語 |

## 利用可能なフォーマット

| ファイル名 | 形式 | サイズ | 用途 |
|------------|------|--------|------|
| `model.safetensors` | Transformers | 922 MB | Python/PyTorch |
| `ggml-whisper-small-medical-ja.bin` | GGML FP16 | 465 MB | whisper.cpp / Whisper.NET（高精度） |
| `ggml-whisper-small-medical-ja-q8_0.bin` | GGML Q8_0 | 252 MB | whisper.cpp / Whisper.NET（バランス）⭐推奨 |
| `ggml-whisper-small-medical-ja-q5_0.bin` | GGML Q5_0 | 167 MB | whisper.cpp / Whisper.NET（軽量） |

## 学習データ

本モデルは [DMiME (Dictionary of Medical terms in MEdical informatics)](https://x.com/dmimejp) を基に作成されました。

DMiME は、医療・医学用語をまとめた辞書で、一般公開されています。本プロジェクトでは DMiME 1.1 に収録されている医療用語をテキストとして使用し、TTS（音声合成）で音声データを生成してファインチューニングを行いました。

| 項目 | 内容 |
|------|------|
| **データソース** | [DMiME 1.1](https://x.com/dmimejp) - 医療・医学用語辞書 |
| **学習サンプル数** | 66,015 |
| **検証サンプル数** | 8,251 |
| **音声生成** | Azure Neural TTS (ja-JP-DaichiNeural) + Google Cloud TTS (ja-JP-Neural2-C) |

> **DMiME について**  
> DMiME は、医療情報学分野で利用される用語を収集・整理した辞書です。詳細は [https://x.com/dmimejp](https://x.com/dmimejp) をご参照ください。

## 学習設定

| パラメータ | 値 |
|-----------|-----|
| エポック数 | 3 |
| バッチサイズ | 32 |
| 学習率 | 1e-5 |
| 精度 | FP16 |
| オプティマイザ | AdamW |

## 使用方法

### transformers ライブラリ

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

# モデルとプロセッサの読み込み
model_id = "kenrouse/whisper-small-medical-ja"
processor = WhisperProcessor.from_pretrained(model_id)
model = WhisperForConditionalGeneration.from_pretrained(model_id)

# 音声ファイルの読み込み
audio, sr = librosa.load("audio.wav", sr=16000)

# 推論
input_features = processor(
    audio, 
    sampling_rate=16000, 
    return_tensors="pt"
).input_features

predicted_ids = model.generate(input_features, language="ja", task="transcribe")
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print(transcription)
```

### Whisper.NET / whisper.cpp

GGML形式のモデルは C++ や .NET アプリケーションで利用できます。

#### ダウンロード

```bash
# Q8_0 量子化版（推奨）
wget https://huggingface.co/kenrouse/whisper-small-medical-ja/resolve/main/ggml-whisper-small-medical-ja-q8_0.bin

# Q5_0 量子化版（軽量）
wget https://huggingface.co/kenrouse/whisper-small-medical-ja/resolve/main/ggml-whisper-small-medical-ja-q5_0.bin

# FP16版（高精度）
wget https://huggingface.co/kenrouse/whisper-small-medical-ja/resolve/main/ggml-whisper-small-medical-ja.bin
```

#### whisper.cpp での使用

```bash
./main -m ggml-whisper-small-medical-ja-q8_0.bin -l ja -f audio.wav
```

#### Whisper.NET での使用

```csharp
// Whisper.NET での使用例
using var whisperFactory = WhisperFactory.FromPath("ggml-whisper-small-medical-ja-q8_0.bin");
using var processor = whisperFactory.CreateBuilder()
    .WithLanguage("ja")
    .Build();

await foreach (var result in processor.ProcessAsync(audioStream))
{
    Console.WriteLine(result.Text);
}
```

## 対象用途

- 医療現場での音声認識
- 電子カルテの音声入力支援
- 医療用語を含む会話の文字起こし

## 制限事項

- 医療用語に特化しているため、一般会話の認識精度は元モデルより低下する可能性があります
- 学習データは合成音声（TTS）から生成されているため、実際の人間の発話との差異がある可能性があります

## ライセンス

Apache 2.0

## 引用

```bibtex
@misc{whisper-small-medical-ja,
  author = {kenrouse},
  title = {Whisper Small - Japanese Medical Terms},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/kenrouse/whisper-small-medical-ja}
}
```

## 謝辞

- [OpenAI Whisper](https://github.com/openai/whisper)
- [DMiME (Dictionary of Medical terms in MEdical informatics)](https://x.com/dmimejp)
- [Azure Cognitive Services Speech](https://azure.microsoft.com/services/cognitive-services/speech-services/)
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech)
