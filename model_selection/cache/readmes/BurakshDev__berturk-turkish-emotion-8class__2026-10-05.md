---
language:
- tr
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: text-classification
base_model: dbmdz/bert-base-turkish-cased
tags:
- bert
- berturk
- emotion
- emotion-classification
- turkish
metrics:
- f1
- accuracy
widget:
- text: "Bugün sınavdan yüksek not aldım, çok mutluyum!"
- text: "Gece yalnız eve dönerken arkamdan biri geliyor gibiydi."
- text: "Yıllardır görmediğim arkadaşımı karşımda görünce donup kaldım."
model-index:
- name: berturk-turkish-emotion-8class
  results:
  - task:
      type: text-classification
      name: Text Classification
    metrics:
    - type: f1
      name: Macro F1 (test)
      value: 0.811
    - type: accuracy
      name: Accuracy (test)
      value: 0.816
---

# BERTurk — Türkçe 8 sınıflı duygu sınıflandırma

Türkçe metinleri 8 duyguya ayıran, [`dbmdz/bert-base-turkish-cased`](https://huggingface.co/dbmdz/bert-base-turkish-cased)
üzerinde fine-tune edilmiş model.

*A BERTurk model fine-tuned to classify Turkish text into 8 emotions. Test macro-F1 0.811 on 8,875
human-labelled examples.*

**Sınıflar:** mutluluk · üzüntü · öfke · korku · şaşkınlık · tiksinti · sevgi · nötr

Kod, veri seti derleme, ablation ve istatistik testleri:
[GitHub — Turkish-Text-Emotion-Measurement-Artificial-Intelligence](https://github.com/BurakYildizGameDev/Turkish-Text-Emotion-Measurement-Artificial-Intelligence)

## Kullanım

```python
from transformers import pipeline

clf = pipeline("text-classification", model="BurakshDev/berturk-turkish-emotion-8class", top_k=None)
print(clf("Bugün sınavdan yüksek not aldım, çok mutluyum!"))
```

### Kalibre olasılıklar (isteğe bağlı)

Olasılıklar validation seti üzerinde temperature scaling ile kalibre edildi (`temperature.json`, T ≈ 1.124;
test ECE 0.034 → 0.014). Kalibre olasılık için logit'leri T'ye bölüp softmax alın:

```python
import json, torch
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo = "BurakshDev/berturk-turkish-emotion-8class"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo).eval()
T = json.load(open(hf_hub_download(repo, "temperature.json")))["temperature"]

inputs = tok("Yıllardır görmediğim arkadaşımı karşımda görünce donup kaldım.",
             return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    probs = torch.softmax(model(**inputs).logits / T, dim=-1)[0]
for i, p in sorted(enumerate(probs.tolist()), key=lambda x: -x[1]):
    print(f"{model.config.id2label[i]:10s} {p:.3f}")
```

## Sonuçlar

Test seti: 8.875 insan etiketli örnek (yalnızca gold veri). Bu repodaki model seed 42 çalışmasıdır;
model seçimi yalnızca validation macro-F1 ile yapıldı, test en sonda bir kez değerlendirildi.

| Metrik | Değer |
|---|---|
| Macro-F1 | 0.811 |
| Weighted-F1 | 0.816 |
| Accuracy | 0.816 |

3 seed ortalamasında BERTurk 0.812 ± 0.001 macro-F1 aldı; aynı veri ve bütçeyle XLM-RoBERTa-base 0.797,
mBERT 0.780, TF-IDF + Logistic Regression 0.767 (farkların hepsi anlamlı, paired bootstrap + Holm, p < 0.001).

### Sınıf bazlı (test)

| Sınıf | Precision | Recall | F1 | n |
|---|---|---|---|---|
| mutluluk | 0.855 | 0.893 | 0.873 | 2.191 |
| üzüntü | 0.852 | 0.845 | 0.848 | 1.101 |
| öfke | 0.749 | 0.760 | 0.754 | 1.422 |
| korku | 0.915 | 0.873 | 0.893 | 762 |
| şaşkınlık | 0.851 | 0.865 | 0.858 | 654 |
| tiksinti | 0.941 | 0.846 | 0.891 | 551 |
| sevgi | 0.628 | 0.639 | 0.634 | 299 |
| nötr | 0.744 | 0.730 | 0.737 | 1.895 |

### Kaynak bazlı (tek sayı yanıltıcıdır)

| Kaynak | n | Macro-F1 |
|---|---|---|
| GoEmotions TR (İngilizceden makine çevirisi, Reddit) | 4.775 | 0.612 |
| TREMO — 2/3 oy uzlaşısı | 855 | 0.798 |
| TREMO — 3/3 oy uzlaşısı | 2.660 | 0.961 |
| Türkçe tweet | 585 | 0.981 |

TREMO-consensus ve tweet örnekleri çoğunlukla duyguyu doğrudan adlandırır ("korkarım", "şaşırdım"); kelime tabanlı
TF-IDF bile bu kaynaklarda 0.93-0.97 alır. **Gerçekçi performans GoEmotions (~0.61) ve TREMO-majority (~0.80)
satırlarıdır.**

## Eğitim

| | |
|---|---|
| Base model | `dbmdz/bert-base-turkish-cased` |
| Eğitim verisi | 41.465 gold örnek (TREMO, Türkçe tweet duygu, GoEmotions TR) |
| max_length | 128 |
| Batch size | 32 |
| Learning rate | 2e-5 (warmup %10, weight decay 0.01) |
| Epoch | en fazla 4, early stopping (patience 2); en iyi epoch 2 |
| Loss | ağırlıksız cross-entropy |
| Donanım | NVIDIA RTX 5070 Ti Laptop GPU, ~4 dakika |

val ve test yalnızca gold veriden oluşur; yakın kopyalar MinHash-LSH ile gruplanıp aynı split'e konur.
Weak (kural tabanlı) ve silver veri denendi ama kullanılmadı: weak veri etkisiz (+0.001), silver veri zararlı (−0.018).

## Sınırlamalar

- **nötr ve sevgi sınıflarının eğitim örneklerinin tamamı makine çevirisidir** (GoEmotions). Bu iki sınıf en
  zayıf sınıflardır ve ana dil metinlerdeki performansları doğrudan ölçülemez.
- Alanlar: kişisel anı cümleleri (TREMO), Reddit yorumları (çeviri), tweet'ler. Ürün yorumu, haber veya konuşma
  dili gibi başka alanlarda performans farklı olabilir.
- Tek etiketli sınıflandırmadır; karışık duygular tek sınıfa indirgenir.
- En sık karışıklık öfke ↔ nötr ve nötr → mutluluk.

## Lisans

Model **CC BY-NC 4.0** ile yayınlanır: yalnızca ticari olmayan kullanım. Eğitim verisindeki TREMO yalnızca ticari
olmayan amaçlarla kullanılabildiği için ondan türetilen bu model de aynı kısıtı taşır. Proje kodu GitHub'da MIT
lisanslıdır.

Veri kaynakları: TREMO (Tocoglu & Alpkocak, 2018), Türkçe tweet duygu veri seti (Güven vd., 2019),
GoEmotions (Demszky vd., 2020; Türkçe makine çevirisi).
