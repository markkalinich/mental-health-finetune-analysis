---
language: tr
license: mit
base_model: google/mt5-small
tags:
  - turkish
  - text-analysis
  - music-generation
  - mcp
  - fine-tuned
  - emotion-classification
library_name: transformers
pipeline_tag: text-generation
widget:
  - text: "Şu metni analiz et ve müzik promptu üret: Bir zamanlar büyük bir aşk yaşamıştım. Sonra o aşk gitti. Her gece pencereden bakıyorum, yağmur onu hatırlatıyor."
---

# Story-to-Music Analyzer (Türkçe Metin → Müzik Metadata)

`google/mt5-small`'un Türkçe metinleri **Suno** ve **Udio** için müzik parametrelerine
çeviren fine-tuned versiyonu. [Story-to-Music MCP](https://github.com/sbugrayy/story-to-music)
projesinin "Analyzer" bileşeni.

## Görev

Türkçe bir metin (hikâye, şarkı sözü, konsept) verildiğinde, model şu JSON yapısını üretir:

```json
{
  "emotion": "özlem",
  "energy": 4,
  "bpm": 80,
  "key": "A minor",
  "instruments": ["ney", "saz"],
  "vocal_style": "erkek, kısık, dramatik",
  "suno_style_prompt": "melancholic Turkish ballad with ney flute and saz, slow tempo"
}
```

## Kullanım

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("bugrayildirim/story-to-music-analyzer")
model = AutoModelForSeq2SeqLM.from_pretrained("bugrayildirim/story-to-music-analyzer")

text = "Bir zamanlar büyük bir aşk yaşamıştım. Sonra o aşk gitti."
prompt = f"Şu metni analiz et ve müzik promptu üret: {text}"

inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
outputs = model.generate(**inputs, max_new_tokens=192, num_beams=4, early_stopping=True)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Eğitim

- **Base model:** `google/mt5-small` (556M parametre)
- **Veri:** 854 Türkçe şarkı sözü + Ollama (qwen2.5:7b) tarafından üretilen
  metadata etiketleri (`distill_data.py` pipeline'ı, [GitHub](https://github.com/sbugrayy/story-to-music))
- **Eğitim:** Kaggle T4 GPU, 17 epoch, eval_loss 0.54'e kadar düştü
- **Önemli:** `fp16=False` (mT5'in fp16'da NaN sorunu var), gradient checkpointing aktif

Detaylar: [`training/story_to_music_train.ipynb`](https://github.com/sbugrayy/story-to-music/blob/main/training/story_to_music_train.ipynb)

## Performans

JSON validity ve alan kapsamı (eval set 86 örnek):
- Geçerli JSON: **100%**
- Tüm alanların kapsamı: **100%**

## Limitations

- Sadece Türkçe metin destekler
- CPU'da inference ~5 saniye (T4 GPU'da ~500ms)
- `suno_style_prompt` alanı bazen yarı-Türkçe yarı-İngilizce çıktı verebilir
  (Story-to-Music MCP server bunu deterministik fallback ile düzeltir)

## Lisans

MIT. Eğitim verisi olarak kullanılan şarkı sözlerinin telif hakları orijinal
sahiplerine aittir; bu model **stil/duygu örüntülerini** öğrenmek için eğitildi,
şarkı sözü ezberi yapmaz.

## Atıf

```bibtex
@misc{story-to-music-analyzer,
  author = {Buğra Yıldırım},
  title = {Story-to-Music Analyzer: Turkish text to music metadata},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/bugrayildirim/story-to-music-analyzer}},
}
```
