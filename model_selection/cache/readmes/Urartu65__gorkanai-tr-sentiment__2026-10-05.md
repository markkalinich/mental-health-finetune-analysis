---
language: tr
license: mit
tags:
  - sentiment-analysis
  - turkish
  - bert
  - text-classification
datasets:
  - fthbrmnby/turkish_product_reviews
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
widget:
  - text: "Kargo çok hızlıydı, ürün harika!"
  - text: "İade etmek zorunda kaldım, hiç memnun değilim."
  - text: "Ürün bugün elime ulaştı."
---

# gorkanai — Türkçe Ürün Yorumu Duygu Analizi (3 sınıf)

[`dbmdz/bert-base-turkish-cased`](https://huggingface.co/dbmdz/bert-base-turkish-cased) modelinin, gerçek
Türkçe ürün yorumları üzerinde 3 sınıf (**negatif / nötr / pozitif**) için ince ayarlanmış hali.

Sıfırdan başlayıp adım adım öğrenerek geliştirilen bir projenin (bkz.
[gorkanai](https://github.com/GoGonuldas/gorkanai) — tüm süreç ve dersler `PROGRESS.md`'de anlatılıyor)
14. adımının sonucu.

## Kullanım

Modelin nötr sınıf logit'ine tahminden önce **+3.00** eklenmesi gerekir (val setinde macro-F1 ile seçilmiş
bir sabit — nötr sınıfın çok daha az örnekle öğrenildiği için düzeltme). Bu ekleme yapılmazsa model nötr
yorumları negatif/pozitif olarak yanlış sınıflandırma eğilimindedir.

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "Urartu65/gorkanai-tr-sentiment"
NEUTRAL_BIAS = 3.00

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID).eval()
labels = [model.config.id2label[i] for i in range(len(model.config.id2label))]
neutral_idx = labels.index("nötr")

def turkish_lower(text):
    return text.replace("I", "ı").replace("İ", "i").lower()

def predict(text):
    encoded = tokenizer(turkish_lower(text), truncation=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        logits = model(**encoded).logits[0]
    logits[neutral_idx] += NEUTRAL_BIAS
    probs = torch.softmax(logits, dim=0).tolist()
    best = max(range(len(labels)), key=lambda i: probs[i])
    return labels[best], dict(zip(labels, probs))

print(predict("Kargo çok hızlıydı, ürün harika!"))
# ('pozitif', {'negatif': 0.0009, 'nötr': 0.0019, 'pozitif': 0.9972})
```

## Eğitim verisi

- `fthbrmnby/turkish_product_reviews` (~233k gerçek ürün yorumu, pozitif/negatif), dengesiz örneklemden
  ~17k örnek + [confident learning](https://arxiv.org/abs/1911.00068) ile temizlenmiş etiketler.
- Nötr sınıf için 1000 kısa yorum elle etiketlendi (active learning ile seçildi).

## Değerlendirme

Hiç görülmemiş, elle etiketlenmiş 200 kısa yorumda (104 pozitif / 74 negatif / 22 nötr):

| | Doğruluk | Macro-F1 | Nötr P/R | Negatif P/R | Pozitif P/R |
|---|---|---|---|---|---|
| Kıyas: 2 sınıflı model + %95 "emin değilim" eşiği | 0.825 | 0.746 | 0.38/0.64 | 0.87/0.84 | 0.97/0.86 |
| **Bu model (bias +3.00)** | **0.870** | **0.808** | **0.58/0.68** | 0.87/0.88 | 0.95/0.90 |

## Sınırlamalar

- Ürün yorumu alanında (e-ticaret) eğitildi; farklı alanlarda (haber, sosyal medya) genelleme sınanmadı.
- Deyimsel/dünya bilgisi gerektiren ifadelerde ("değmez", "beklentimin altında kaldı" gibi olmayanlar) hata payı var.
- Nötr sınıfın kesinliği (%58-73) hâlâ negatif/pozitife göre daha düşük — en az veriyle öğrenilen sınıf.
