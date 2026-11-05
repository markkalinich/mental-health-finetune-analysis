---
language:
  - tr
license: apache-2.0
library_name: transformers
pipeline_tag: automatic-speech-recognition
base_model: openai/whisper-large-v3
base_model_relation: finetune
tags:
  - whisper
  - asr
  - speech-recognition
  - turkish
  - medical
  - clinical
  - lora
datasets:
  - turkmedstt/medv3-turkish-medical-asr
metrics:
  - wer
  - cer
model-index:
  - name: whisper-large-v3-turkish-medical
    results:
      - task:
          type: automatic-speech-recognition
        dataset:
          name: General Turkish real-speech evaluation
          type: general-turkish
        metrics:
          - type: wer
            value: 0.0795
            name: General Turkish WER
          - type: cer
            value: 0.0228
            name: General Turkish CER
      - task:
          type: automatic-speech-recognition
        dataset:
          name: Synthetic medical evaluation (medv3 validation, 332 clips)
          type: synthetic-medical
        metrics:
          - type: wer
            value: 0.0055
            name: Medical WER (in-domain synthetic)
          - type: cer
            value: 0.0008
            name: Medical CER (in-domain synthetic)
          - type: medical_term_recall
            value: 1.0
            name: Medical term recall (in-domain synthetic)
      - task:
          type: automatic-speech-recognition
        dataset:
          name: Real-voice medical evaluation (best-performing speaker)
          type: real-medical
        metrics:
          - type: wer
            value: 0.0588
            name: Medical WER (real voice, best-performing speaker)
          - type: cer
            value: 0.0103
            name: Medical CER (real voice, best-performing speaker)
          - type: medical_term_recall
            value: 0.918
            name: Medical term recall (real voice, best-performing speaker)
---

# Whisper Large V3 - Türkçe Tıbbi ASR (M2)

OpenAI `whisper-large-v3` modelinin Türkçe genel konuşma ve sentetik tıbbi konuşma
verileriyle LoRA üzerinden uyarlanmış, ardından temel modele birleştirilmiş sürümüdür.
Bu repo tam `transformers` modelini ve işlemci dosyalarını içerir; PEFT adaptörü ayrıca
yüklemek gerekmez.

## Amaç

Türkçe klinik dikte ve tıbbi konuşma tanıma araştırmaları için geliştirilmiştir. İlaç
adları ile Latin/Yunan kökenli tıbbi terimlerin tanınmasını iyileştirmeyi hedefler.

## Uyarılar

- **Tıbbi cihaz değildir; klinik karar için kullanılmamalıdır.**
- Transkripsiyonlar insan denetimi olmadan hasta kaydına veya klinik iş akışına alınmamalıdır.
- Medikal eğitim verisi sentetik TTS verisidir. Gerçek hasta verisi kullanılmamıştır.
- Sentetik in-domain sonuçları bir üst sınırdır; gerçek konuşma sonucuyla aynı kabul edilmemelidir.
- Aksan, arka plan gürültüsü, örtüşen konuşma ve belirsiz telaffuz başarımı düşürebilir.

## Eğitim

- Temel model: `openai/whisper-large-v3`
- Yöntem: LoRA, hedef modüller `q_proj,v_proj`
- LoRA: `r=64`, `alpha=128`, dropout `0.05`
- Öğrenme oranı: `1e-4`
- Eğitim: 1 epoch
- Genel veri: yaklaşık 140 saat dengeli Türkçe konuşma
  (Common Voice, ISSAI ve OpenSLR kaynakları)
- Veri hazırlama reçetesi (kaynaklar, lisanslar, temizleme kuralları, sayılar ve yeniden üretim): https://github.com/muhammedkumcu/turkmedstt/blob/main/docs/DATA_PIPELINE.md
- Medikal veri: `medv3` sentetik korpusu, eğitim karışımında 3 kez örnekleme

Kontrollü ablasyonda M0 temel model, M1 yalnız genel Türkçe ve M2 genel + medikal
veri kullanır. M1 ile M2 arasındaki temel deneysel fark medikal eğitim verisidir.

## Model ailesi

| Kısaltma | Model | Eğitim içeriği | Deneydeki rolü |
|---|---|---|---|
| M0 | `openai/whisper-large-v3` | Ek uyarlama yok | Temel model |
| M1 | `turkmedstt/whisper-large-v3-turkish-general` | Genel Türkçe konuşma | Genel dil uyarlamasının etkisi |
| M2 | Bu repo | Genel Türkçe + sentetik medikal konuşma | Medikal alan uyarlamasının ek etkisi |

Bu yapı, medikal kazanımın yalnızca daha fazla eğitimden mi yoksa alan verisinden mi
geldiğini daha kontrollü biçimde incelemek için kullanılmıştır.

## Sonuçlar

| Değerlendirme | Metrik | M0 | M1 | M2 |
|---|---|---:|---:|---:|
| Genel Türkçe, 320 gerçek klip | WER | 0.1213 | **0.0792** | 0.0795 |
| Genel Türkçe, 320 gerçek klip | CER | 0.0546 | **0.0226** | 0.0228 |
| Gerçek-ses medikal, 3 konuşmacı / 120 klip | WER | 0.1060 | 0.1176 | **0.0854** |
| Gerçek-ses medikal, 3 konuşmacı / 120 klip | CER | 0.0258 | 0.0250 | **0.0190** |
| Gerçek-ses medikal, en iyi konuşmacı | WER | 0.0956 | 0.1033 | **0.0588** |
| Gerçek-ses medikal, en iyi konuşmacı | CER | 0.0186 | 0.0170 | **0.0103** |
| Gerçek-ses medikal, en iyi konuşmacı | Terim recall | 0.808 | 0.781 | **0.918** |
| Sentetik medikal validation, 332 klip | WER | - | - | **0.0055** |
| Sentetik medikal validation, 332 klip | CER | - | - | **0.0008** |
| Sentetik medikal validation, 332 klip | Terim recall | - | - | **1.000** |

`medv3` sentetik validation değerlendirmesi eğitim verisiyle aynı sentetik üretim
alanındadır ve gerçek-ses başarımının yerine kullanılmamalıdır.

Zor tıbbi terim testinde M2, üç konuşmacının tamamında M0 ve M1'den daha yüksek recall
ve daha düşük WER elde etmiştir. Gerçek-ses kayıtları yayımlanmamış; yalnız anonim ve
toplu metrikler raporlanmıştır.

### Metrikler nasıl okunmalı?

| Metrik | Tanım | Yorum |
|---|---|---|
| WER | `(değiştirme + silme + ekleme) / referans kelime sayısı` | Düşük değer daha iyidir. |
| CER | Aynı hata hesabının karakter düzeyinde uygulanması | Türkçedeki ek ve yazım farklılıklarını daha ayrıntılı gösterir. |
| Terim recall | Referansta bulunan hedef medikal terimlerden hipotezde korunanların oranı | Yüksek değer daha iyidir; `0.918`, hedef terimlerin %91,8'inin korunduğunu gösterir. |

`M0`, `M1` ve `M2` aynı değerlendirme satırında karşılaştırılabilir. Buna karşılık
genel Türkçe, sentetik medikal ve gerçek-ses medikal satırları farklı veri
dağılımlarını temsil ettiği için birbirleriyle tek bir birleşik başarı puanı gibi
yorumlanmamalıdır.

### Değerlendirme kapsamı

- **Genel Türkçe:** 320 gerçek, medikal olmayan konuşma klibi
- **Gerçek-ses medikal:** üç gönüllü konuşmacıdan toplam 120 klip
- **En iyi konuşmacı:** üç konuşmacı içindeki en düşük WER üreten ayrı alt grup
- **Sentetik validation:** medv3 üretim alanından 332 klip; alan-içi üst sınır niteliğinde

Gerçek-ses değerlendirme kayıtları eğitimde kullanılmamış ve yayımlanmamıştır.
Sentetik validation sonucu, aynı TTS üretim ailesine yakın olduğu için gerçek klinik
performans göstergesi olarak kullanılmamalıdır.

20 model ve 1.060 genel Türkçe klibi kapsayan geniş benchmark:
[`turkmedstt/turkish-asr-benchmark`](https://huggingface.co/datasets/turkmedstt/turkish-asr-benchmark).

## Önerilen kullanım alanları

- Türkçe tıbbi terminoloji tanıma araştırmaları
- İnsan denetimli klinik dikte prototipleri
- Genel Türkçe ve medikal uyarlama arasındaki ablasyon çalışmaları
- ASR hata analizi, terim koruma ölçümü ve eğitim amaçlı deneyler

## Uygun olmayan kullanımlar

- Tanı, tedavi veya klinik karar verme
- İnsan kontrolü olmadan hasta kaydı üretme
- Acil durum yönlendirmesi veya ilaç dozu belirleme
- Model çıktısını kesin ve doğrulanmış tıbbi bilgi olarak sunma

## Kullanım

```python
import torch
from transformers import pipeline

model_id = "turkmedstt/whisper-large-v3-turkish-medical"
device = 0 if torch.cuda.is_available() else -1
dtype = torch.float16 if torch.cuda.is_available() else torch.float32

transcriber = pipeline(
    "automatic-speech-recognition",
    model=model_id,
    torch_dtype=dtype,
    device=device,
)

result = transcriber(
    "ornek.wav",
    generate_kwargs={"language": "tr", "task": "transcribe"},
)
print(result["text"])
```

Model birleştirilmiş tam ağırlıkları içerir; ayrıca PEFT/LoRA adaptörü yüklenmez.
`whisper-large-v3` boyutu nedeniyle GPU önerilir. CPU üzerinde çalışabilir ancak ilk
model yükleme ve transkripsiyon süresi belirgin biçimde uzayabilir.

## Repo içeriği

- `model.safetensors`: birleştirilmiş M2 ağırlıkları
- `config.json`, `generation_config.json`: model ve üretim ayarları
- tokenizer, processor ve feature extractor dosyaları
- `training_metadata.json`: temel eğitim ve yayın bilgileri

## Lisans ve kaynaklar

Birleştirilmiş model Apache-2.0 altında yayımlanır. Temel `whisper-large-v3` modeli
MIT lisanslıdır. Eğitim veri kaynaklarının kendi lisansları ve kullanım koşulları
geçerlidir; bu repo ham genel eğitim seslerini içermez.

## Atıf

TurkMedSTT bitirme projesi, 2026.

## Katkı verenler

- [Muhammed Kumcu](https://huggingface.co/muhammedkumcu)
- [Yağmur Tuncer](https://huggingface.co/yagmurtuncer)

Muhammed Kumcu ve Yağmur Tuncer; proje tasarımı, veri hazırlama, model eğitimi,
yazılım geliştirme, değerlendirme, dokümantasyon ve yayın çalışmalarını birlikte
yürütmüştür.

## Teşekkür

Gerçek-ses değerlendirme kayıtlarına gönüllü katkıları için Zeynep Zehra Kumcu ve Yusuf Uysal'a
teşekkür ederiz. Bu kayıtlar yayımlanmamış, yalnız anonim ve toplu sonuçlar raporlanmıştır.
