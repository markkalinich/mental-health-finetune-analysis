---
license: mit
language:
- tr
metrics:
- accuracy
- f1
base_model:
- yeniguno/absa-turkish-bert-dbmdz
pipeline_tag: text-classification
library_name: transformers
tags:
- absa
- nlp
- sentiment
- turkish
---

## Model Tanıtımı

Bu model, Türkçe metinler üzerinde **Sentiment Analysis (Duygu Analizi)** yapmak için Türkçe dilindeki giyim ürünlerine ait metinlerden oluşturulan veri kümesi kullanılarak fine-tune edilmiş bir ABSA (Aspect-Based Sentiment Analysis) modelidir. 
Model, `yeniguno/absa-turkish-bert-dbmdz` temel modelinden türetilmiştir ve Türkçe dilindeki metinlerde olumlu, olumsuz veya nötr duygu kategorilerine ait etiketleri tahmin edebilmektedir.


- **Developed by:** [[ebru kılıç](https://huggingface.co/ebrukilic) , [rumeysa nur yasav](https://huggingface.co/rmysysv)]
- **Model type:** [Fine-Tuned ABSA Model]
- **License:** [MIT]
- **Finetuned from model [optional]:** [yeniguno/absa-turkish-bert-dbmdz]

Bu model, doğrudan metin verisini alıp duygu etiketlerini tahmin etmek için kullanılabilir. Modelin çıktı olarak "olumlu", "olumsuz" veya "nötr" etiketlerinden birini döndürmesi beklenir.Model, sadece duygu analizi için eğitilmiştir. Karmaşık doğal dil işleme (NLP) görevleri, makale yazımı veya özetleme gibi işlemler için uygun değildir.

## Bias, Risk ve Limitler 

Bu modelin eğitildiği veri seti, belirli bir kullanıcı grubunun yorumlarından oluşmaktadır. Bu nedenle, modelin diğer kategorilere ait metinler üzerindeki duygu analizinde sınırlı bir performans gösterebilir. 
Ayrıca, modelin etiketleri yalnızca belirli (olumlu, olumsuz, nötr) duygu kategorilerine odaklanmaktadır ve daha karmaşık duygu durumlarını ayırt etmekte zorlanabilir.

## Modeli Nasıl Kullanabiliriz?

Modeli, `transformers` kütüphanesini kullanarak yükleyebilir ve metinlerdeki duygu analizini gerçekleştirebilirsiniz.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# modelin ve tokenizerın yüklenmesi
model_name = "ebrukilic/ara-proje-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# cuda
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()
```

```python
# test etmek için örnek
text = "Ürün çok güzel ama kolları kısa ve çok dar"
aspect = "Beden"

inputs = tokenizer(aspect, text, truncation=True, padding='max_length', max_length=128, return_tensors="pt").to(device)

# model ile tahmin yapılması:
with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits
predicted_class_id = torch.argmax(logits, dim=-1).item()

# Tahmin edilen etiketin açıklaması
id_to_label = {0: "negatif", 1: "nötr", 2: "pozitif"}
predicted_label = id_to_label[predicted_class_id]
print(f"Tahmin edilen etiket: {predicted_label}")
```

## Eğitim Verisi

[ebrukilic/ytu-ara-proje-absa](https://huggingface.co/datasets/ebrukilic/ytu-ara-proje-absa)

Model, Türkçe metinlerdeki kullanıcı yorumları ve ilgili "aspect"ler (özellikler) kullanılarak eğitildi. Etiketler, 3 sınıflı duygu (polarite) kategorisinde `negatif`, `nötr` ve `pozitif` olarak tanımlanmıştır. Veri kümesi 5045 örnekten oluşmaktadır.

Veri seti:
- **Normalized Yorum**: Yorum metni
- **Aspects**: Kullanıcı yorumu ile ilişkilendirilen konu veya özellik
- **Polarity**: Yorumun duygusal polaritesi (negatif, nötr, pozitif)

### Performans Metrikleri

Modelin performansını değerlendirmek için doğruluk (accuracy) ve F1 skoru gibi yaygın metrikler kullanılmıştır. Aşağıda modelin test verisi üzerinde elde edilen değerlendirme sonuçları yer almaktadır:

- **Accuracy:** 0.7684
- **Macro-F1:** 0.7311

Model, farklı sınıflara (pozitif, nötr, negatif) eşit ağırlık vererek (macro-average) değerlendirilmiştir. Bu metrikler, modelin sınıflandırma görevindeki genel başarısını yansıtmaktadır.

| Label     | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|--------|
| negatif  | 0.84      | 0.76   | 0.80     | 1719   |
| nötr     | 0.45      | 0.67   | 0.54     | 653    |
| pozitif  | 0.91      | 0.81   | 0.86     | 1639   |
| **macro avg** | 0.73 | 0.75   | 0.73     | 4011   |
| **weighted avg** | 0.80 | 0.77 | 0.78   | 4011   |
