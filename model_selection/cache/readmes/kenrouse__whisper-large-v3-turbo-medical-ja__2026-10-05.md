---
language:
- ja
license: mit
base_model: openai/whisper-large-v3-turbo
tags:
- automatic-speech-recognition
- whisper
- medical
- japanese
- healthcare
- asr
datasets:
- custom
pipeline_tag: automatic-speech-recognition
library_name: transformers
---

# Whisper Large-v3-Turbo Medical Japanese

日本語医療用語に特化してファインチューニングした Whisper Large-v3-Turbo モデルです。

## モデル概要

| 項目 | 値 |
|------|-----|
| ベースモデル | [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) |
| パラメータ数 | 809M |
| Encoder 層数 | 32 |
| Decoder 層数 | 4（蒸留モデル） |
| 対象言語 | 日本語 |
| 用途 | 医療カルテ向け音声認識 |

## 評価結果

40サンプルの日本語医療テキストで評価した結果：

| モデル | CER (文字誤り率) |
|--------|------------------|
| オリジナル (whisper-large-v3-turbo) | 13.69% |
| **ファインチューニング後** | **9.26%** |
| **改善率** | **32.4%削減** |

### 認識精度の改善例

| カテゴリ | オリジナルモデル | ファインチューニング後 | 正解 |
|----------|------------------|------------------------|------|
| 診断 | 新潟糖尿病 | ✓ 2型糖尿病 | 2型糖尿病 |
| 検査 | 神殿図 | ✓ 心電図 | 心電図 |
| 所見 | 胸膜飛行 | ✓ 胸膜肥厚 | 胸膜肥厚 |
| 疾患名 | 大半母子 | ✓ 外反母趾 | 外反母趾 |
| 疾患名 | 会長末端円 | ✓ 回腸末端炎 | 回腸末端炎 |
| 評価 | 海底町谷川市議会1の評価スケール | ✓ 改定長谷川式簡易知能評価スケール | 改訂長谷川式簡易知能評価スケール |
| 疾患名 | 腫瘍性皮膚炎 | ✓ 脂漏性皮膚炎 | 脂漏性皮膚炎 |
| 疾患名 | 心アミロイド室 | ✓ 心アミロイドーシス | 心アミロイドーシス |
| 手術 | 外素系ヘルニア | ✓ 外鼠径ヘルニア | 外鼠径ヘルニア |
| 手術 | 開腸同肝臓切術 | ✓ 回腸導管造設術 | 回腸導管造設術 |
| 手術 | ジロコンジ手術 | ✓ 痔瘻根治手術 | 痔瘻根治手術 |
| 手術 | 強壁腫瘍的出術 | ✓ 胸壁腫瘍摘出術 | 胸壁腫瘍摘出術 |
| 症状 | 四字障害 | ✓ 読字障害 | 読字障害 |

## トレーニング詳細

| パラメータ | 値 |
|------------|-----|
| エポック数 | 3 |
| バッチサイズ | 2 × 8 (gradient accumulation) = 16 |
| 学習率 | 1e-5 |
| 精度 | FP16 |
| トレーニングサンプル数 | 66,015 |
| 検証サンプル数 | 8,251 |

## 使用方法

### HuggingFace Transformers

```python
from transformers import pipeline

pipe = pipeline(
    "automatic-speech-recognition",
    model="kenrouse/whisper-large-v3-turbo-medical-ja",
    device="cuda"
)

result = pipe("audio.wav", generate_kwargs={"language": "ja"})
print(result["text"])
```

### Whisper.NET (C#/.NET)

GGML 形式のモデルを使用して、Whisper.NET で推論できます。

```csharp
using Whisper.net;

var factory = WhisperFactory.FromPath("ggml-whisper-large-v3-turbo-medical-ja-q8_0.bin");
using var processor = factory.CreateBuilder()
    .WithLanguage("ja")
    .Build();

using var fileStream = File.OpenRead("audio.wav");
await foreach (var segment in processor.ProcessAsync(fileStream))
{
    Console.WriteLine($"[{segment.Start} - {segment.End}] {segment.Text}");
}
```

## GGML モデル（Whisper.NET / whisper.cpp 用）

| ファイル | サイズ | 量子化 |
|----------|--------|--------|
| ggml-whisper-large-v3-turbo-medical-ja.bin | 1,549 MB | FP16 |
| ggml-whisper-large-v3-turbo-medical-ja-q8_0.bin | 834 MB | Q8_0 |
| ggml-whisper-large-v3-turbo-medical-ja-q5_0.bin | 547 MB | Q5_0 |

## データセット

日本語医療用語辞書 [DMiME](https://x.com/DMiMEjp)（Dictionary of Medical terms in MEdical informatics）から抽出した医療用語を使用し、Azure Speech Service および Google Cloud TTS で音声を合成してトレーニングデータを作成しました。

## ライセンス

MIT License

## 引用

```bibtex
@misc{whisper-large-v3-turbo-medical-ja,
  author = {kenrouse},
  title = {Whisper Large-v3-Turbo Medical Japanese},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/kenrouse/whisper-large-v3-turbo-medical-ja}
}
```

## 関連リンク

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Whisper.NET](https://github.com/sandrohanea/whisper.net)
- [whisper.cpp](https://github.com/ggerganov/whisper.cpp)
