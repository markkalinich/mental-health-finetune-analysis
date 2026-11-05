---
language:
- ja
license: apache-2.0
tags:
- whisper
- automatic-speech-recognition
- medical
- japanese
- kotoba-whisper
- fine-tuned
base_model: kotoba-tech/kotoba-whisper-v2.2
pipeline_tag: automatic-speech-recognition
---

# kotoba-whisper-medical-ja

このモデルは、[kotoba-tech/kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) を日本語医療用語（DMiME辞書ベース）でファインチューニングしたWhisperモデルです。

## モデル概要

| 項目 | 値 |
|------|-----|
| ベースモデル | kotoba-tech/kotoba-whisper-v2.2 |
| アーキテクチャ | Encoder 32層 + Decoder 2層 (蒸留モデル) |
| パラメータ数 | 約756M |
| 言語 | 日本語 |
| 用途 | 医療分野の音声認識 |

## 評価結果

### 全体スコア

| モデル | CER | 改善率 |
|--------|-----|--------|
| オリジナル kotoba-whisper-v2.2 | 9.59% | - |
| **ファインチューニング済み (このモデル)** | **8.00%** | **+16.6%** |

### 診療科別の詳細評価

Azure TTS (ja-JP-NanamiNeural) で生成した医療文章での評価結果：

| 診療科 | 評価文 | オリジナル | ファインチューニング済み |
|--------|--------|------------|------------------------|
| 循環器 | 急性心筋梗塞、緊急カテーテル検査 | 5.56% | **3.70%** ✓ |
| 腎臓内科 | 糖尿病性腎症、シャント造設術 | 13.04% | **6.52%** ✓ |
| 膠原病 | メトトレキサート、間質性肺炎 | 2.38% | 11.90% |
| 消化器 | 早期胃癌、内視鏡的粘膜下層剥離術 | 13.64% | **4.55%** ✓ |
| 神経内科 | 血栓溶解療法、アルテプラーゼ | 13.33% | 13.33% |

### 誤認識の改善例

| カテゴリ | 正解 | オリジナル (誤) | ファインチューニング済み (正) |
|---------|------|----------------|----------------------------|
| 循環器 | 緊急**カテーテル**検査 | 緊急**過程テル**検査 | ✅ 緊急**カテーテル**検査 |
| 腎臓内科 | 糖尿病**性腎症** | 糖尿病**成人症** | ✅ 糖尿病**性腎症** |
| 腎臓内科 | シャント**造設術** | シャント**増設術** | ✅ シャント**造設術** |
| 消化器 | 早期胃**癌** | 早期胃**がん** | ✅ 早期胃**癌** |
| 消化器 | 粘膜下層**剥離術** | 粘膜下層**白理術** | ✅ 粘膜下層**剥離術** |

医療用語に特化したテストデータセット（5診療科、各診療科の典型的な医療文章）での評価結果です。

## トレーニング詳細

| パラメータ | 値 |
|-----------|-----|
| エポック数 | 3 |
| バッチサイズ | 2 |
| 勾配累積ステップ | 8 |
| 実効バッチサイズ | 16 |
| 学習率 | 1e-5 |
| 精度 | FP16 |
| 総ステップ数 | 12,378 |
| トレーニングサンプル数 | 66,015 |
| 検証サンプル数 | 8,251 |

## トレーニングデータ

[DMiME](https://dm-me.hatenablog.com/)（日本語医療用語辞書）をベースに、以下のTTSエンジンで音声合成されたデータを使用：
- Azure Speech Service (Nanami, Daichi)
- Google Cloud Text-to-Speech (Neural2)

約41,600語の医療用語をカバーしています。

## 使用方法

### transformers を使用

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa

# モデルとプロセッサのロード
model_name = "kenrouse/kotoba-whisper-medical-ja"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)

# デバイス設定
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# 音声ファイルの読み込み
audio, sr = librosa.load("path/to/audio.wav", sr=16000)

# 入力の準備
input_features = processor(
    audio, 
    sampling_rate=16000, 
    return_tensors="pt"
).input_features.to(device)

# 推論
with torch.no_grad():
    predicted_ids = model.generate(input_features)

# デコード
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
print(transcription)
```

### pipeline を使用

```python
from transformers import pipeline

pipe = pipeline(
    "automatic-speech-recognition",
    model="kenrouse/kotoba-whisper-medical-ja",
    device="cuda" if torch.cuda.is_available() else "cpu"
)

result = pipe("path/to/audio.wav")
print(result["text"])
```

## 制限事項

- このモデルは日本語医療用語に特化しており、一般的な日本語音声認識では元のkotoba-whisper-v2.2の方が適している場合があります

## GGML 形式 (Whisper.NET / whisper.cpp 用)

[Whisper.NET](https://github.com/sandrohanea/whisper.net) や [whisper.cpp](https://github.com/ggerganov/whisper.cpp) で使用可能な GGML 形式のモデルも提供しています。

### 利用可能なモデル

| ファイル | 形式 | サイズ | 用途 |
|---------|------|--------|------|
| `ggml-kotoba-whisper-medical-ja.bin` | FP16 | 1,449 MB | 最高精度 |
| `ggml-kotoba-whisper-medical-ja-q8_0.bin` | Q8_0 | 780 MB | バランス型（推奨） |
| `ggml-kotoba-whisper-medical-ja-q5_0.bin` | Q5_0 | 513 MB | 軽量・高速 |

### Whisper.NET での使用例 (C#)

```csharp
using Whisper.net;

// モデルのダウンロード
// hf download kenrouse/kotoba-whisper-medical-ja ggml-kotoba-whisper-medical-ja-q8_0.bin

using var whisperFactory = WhisperFactory.FromPath("ggml-kotoba-whisper-medical-ja-q8_0.bin");
using var processor = whisperFactory.CreateBuilder()
    .WithLanguage("ja")
    .Build();

using var fileStream = File.OpenRead("audio.wav");
await foreach (var segment in processor.ProcessAsync(fileStream))
{
    Console.WriteLine($"[{segment.Start} -> {segment.End}] {segment.Text}");
}
```

### whisper.cpp での使用例

```bash
# モデルのダウンロード
hf download kenrouse/kotoba-whisper-medical-ja ggml-kotoba-whisper-medical-ja-q8_0.bin

# 推論
./main -m ggml-kotoba-whisper-medical-ja-q8_0.bin -l ja -f audio.wav
```

## ライセンス

Apache License 2.0

## 引用

このモデルを使用する場合は、以下を参照してください：

```bibtex
@misc{kotoba-whisper-medical-ja,
  author = {kenrouse},
  title = {kotoba-whisper-medical-ja: Japanese Medical ASR Model},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/kenrouse/kotoba-whisper-medical-ja}}
}
```

## 謝辞

- [kotoba-tech](https://huggingface.co/kotoba-tech) - kotoba-whisper-v2.2ベースモデルの提供
- [DMiME](https://dm-me.hatenablog.com/) - 日本語医療用語辞書の提供
