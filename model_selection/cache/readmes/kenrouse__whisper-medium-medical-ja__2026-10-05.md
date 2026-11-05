---
language:
- ja
license: apache-2.0
library_name: transformers
tags:
- whisper
- automatic-speech-recognition
- audio
- asr
- japanese
- medical
- healthcare
base_model: openai/whisper-medium
datasets:
- custom
pipeline_tag: automatic-speech-recognition
model-index:
- name: whisper-medium-medical-ja
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    metrics:
    - type: cer
      value: 0.0978
      name: Character Error Rate (Medical Terms)
    - type: wer
      value: 0.0978
      name: Word Error Rate (Medical Terms)
---

# Whisper Medium - Japanese Medical Speech Recognition

日本語医療用語に特化してファインチューニングしたWhisper Mediumモデルです。

## Model Description

このモデルは、OpenAIのWhisper Mediumをベースに、日本語医療用語（DMiME辞書：約41,600語）を用いてファインチューニングしました。電子カルテの音声入力や医療文書の音声認識に最適化されています。

### Model Details

| パラメータ | 値 |
|-----------|-----|
| ベースモデル | openai/whisper-medium |
| パラメータ数 | 769M |
| 言語 | 日本語 |
| ファインチューニングデータ | DMiME（医学用語変換辞書）|
| 訓練サンプル数 | 66,015 |
| 検証サンプル数 | 8,251 |
| エポック数 | 3 |
| 学習率 | 1e-05 |
| 実効バッチサイズ | 16 |
| 精度 | FP16 |

## Evaluation Results

TTS生成した医療テキスト音声（5サンプル）を用いて、オリジナルモデルとファインチューニング済みモデルを比較評価しました。

### Performance Comparison

| Model | CER | WER |
|-------|-----|-----|
| Original Whisper Medium | 0.2184 | 0.2184 |
| **Fine-tuned (This Model)** | **0.0978** | **0.0978** |
| **改善率** | **+55.23%** | **+55.23%** |

### Detailed Results by Medical Category

| カテゴリ | Original CER | Fine-tuned CER | 改善 |
|---------|-------------|----------------|------|
| 循環器 | 0.185 | 0.130 | +30% |
| 腎臓内科 | 0.109 | 0.065 | +40% |
| 膠原病 | 0.214 | 0.048 | +78% |
| 消化器 | 0.273 | 0.091 | +67% |
| 神経内科 | 0.311 | 0.156 | +50% |

### Recognition Examples

#### 循環器テキスト
- **Reference**: 患者は急性心筋梗塞の疑いで救急搬送されました。
- **Original**: 患者は急性心筋**高速**の疑いで救急搬送されました（❌ 梗塞→高速）
- **Fine-tuned**: 患者は急性**心筋梗塞**の疑いで救急搬送されました ✅

#### 腎臓内科テキスト
- **Reference**: 糖尿病性腎症の進行により、血液透析の導入が必要となりました。
- **Original**: **投入病性人症**の進行により...（❌ 糖尿病性腎症を誤認識）
- **Fine-tuned**: **糖尿病性腎症**の進行により... ✅

#### 膠原病テキスト
- **Reference**: 関節リウマチに対してメトトレキサートを投与中ですが、間質性肺炎の副作用が疑われます。
- **Original**: **間接流待ち**に対して...（❌ 関節リウマチを誤認識）
- **Fine-tuned**: **関節リウマチ**に対して... ✅

## Training Data

[DMiME (Dictionary for Medical Input Method Editor)](https://github.com/kemaruya/DMiME) を使用しました。DMiMEは日本語医学用語変換辞書で、約41,600語の医療用語を含んでいます。

### Data Processing
1. DMiME辞書から医療用語を抽出
2. Azure Text-to-Speech / Google Cloud TTSで音声合成
3. HuggingFace Dataset形式に変換
4. 訓練:検証 = 8:1 で分割

## Usage

### Transformers

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

# モデルとプロセッサの読み込み
processor = WhisperProcessor.from_pretrained("kenrouse/whisper-medium-medical-ja")
model = WhisperForConditionalGeneration.from_pretrained("kenrouse/whisper-medium-medical-ja")

# 音声ファイルの読み込み
audio, sr = librosa.load("audio.wav", sr=16000)

# 推論
input_features = processor(audio, sampling_rate=16000, return_tensors="pt").input_features
predicted_ids = model.generate(input_features, language="ja", task="transcribe")
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print(transcription)
```

### Pipeline

```python
from transformers import pipeline

pipe = pipeline(
    "automatic-speech-recognition",
    model="kenrouse/whisper-medium-medical-ja",
    chunk_length_s=30,
    device="cuda"  # GPUを使用する場合
)

result = pipe("audio.wav", generate_kwargs={"language": "ja", "task": "transcribe"})
print(result["text"])
```

## Intended Use

### Primary Use Cases
- 電子カルテへの音声入力
- 医療文書の音声認識
- 医療面談・問診の文字起こし
- 医療教育コンテンツの字幕生成

### Out-of-Scope Use
- リアルタイム診断支援（本モデルは音声認識のみ）
- 一般的な日本語音声認識（医療用語に特化）

## Limitations

- 医療用語以外の一般的な日本語認識精度は、オリジナルモデルと同等です
- 方言や強いアクセントの音声では精度が低下する可能性があります
- ノイズの多い環境での認識精度は低下します

## GGML/Quantized Versions

[whisper.cpp](https://github.com/ggerganov/whisper.cpp) で使用可能な GGML 形式も提供しています。`ggml/` フォルダからダウンロードできます。

### Available Models

| Format | File | Size | Compression | Download |
|--------|------|------|-------------|----------|
| FP16 | `ggml-whisper-medium-medical-ja.bin` | 1,463 MB | - | [Download](https://huggingface.co/kenrouse/whisper-medium-medical-ja/resolve/main/ggml/ggml-whisper-medium-medical-ja.bin) |
| Q8_0 | `ggml-whisper-medium-medical-ja-q8_0.bin` | 785 MB | 46% | [Download](https://huggingface.co/kenrouse/whisper-medium-medical-ja/resolve/main/ggml/ggml-whisper-medium-medical-ja-q8_0.bin) |
| Q5_0 | `ggml-whisper-medium-medical-ja-q5_0.bin` | 514 MB | 65% | [Download](https://huggingface.co/kenrouse/whisper-medium-medical-ja/resolve/main/ggml/ggml-whisper-medium-medical-ja-q5_0.bin) |

### Usage with whisper.cpp

```bash
# whisper.cpp をクローン
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp

# ビルド
make

# モデルをダウンロード（Q8_0推奨：精度とサイズのバランスが良い）
wget https://huggingface.co/kenrouse/whisper-medium-medical-ja/resolve/main/ggml/ggml-whisper-medium-medical-ja-q8_0.bin -O models/ggml-medium-medical-ja-q8_0.bin

# 推論実行
./main -m models/ggml-medium-medical-ja-q8_0.bin -l ja -f audio.wav
```

### Quantization Comparison

| Format | Accuracy | Speed | Memory | Recommended Use |
|--------|----------|-------|--------|-----------------|
| FP16 | Best | Baseline | High | 高精度が必要な場合 |
| Q8_0 | Very Good | Faster | Medium | **推奨**: バランス重視 |
| Q5_0 | Good | Fastest | Low | メモリ制限がある場合 |

## Training Procedure

### Hardware
- GPU: NVIDIA RTX 5060 Ti (16GB VRAM)

### Training Arguments
- Learning rate: 1e-5
- Batch size: 4 (effective: 16 with gradient accumulation)
- Epochs: 3
- Optimizer: AdamW
- Scheduler: Linear with warmup
- FP16 training: Enabled

## Citation

```bibtex
@misc{whisper-medium-medical-ja,
  author = {kenrouse},
  title = {Whisper Medium Fine-tuned for Japanese Medical Speech Recognition},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/kenrouse/whisper-medium-medical-ja}
}
```

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [DMiME - 医学用語変換辞書](https://github.com/kemaruya/DMiME)
- [Hugging Face Transformers](https://huggingface.co/transformers)

## License

Apache 2.0
