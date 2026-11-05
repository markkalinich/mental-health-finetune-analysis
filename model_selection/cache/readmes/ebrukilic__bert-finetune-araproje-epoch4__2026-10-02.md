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
Bu veri setine ek olarak SemEval ABSA 2016 Türkçe Restoran verileri (1535) kullanılmıştır.

Veri seti:
- **Normalized Yorum**: Yorum metni
- **Aspects**: Kullanıcı yorumu ile ilişkilendirilen konu veya özellik
- **Polarity**: Yorumun duygusal polaritesi (negatif, nötr, pozitif)

```python
from transformers import Trainer, TrainingArguments, AdamW

training_args = TrainingArguments(
    output_dir='./results',   # modelin kaydedildiği yer
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    num_train_epochs=4,     # ilkinde 3'tü -> ebrukilic/bert-finetune-araproje
    evaluation_strategy="steps",
    eval_steps=50,
    save_strategy="steps",
    save_steps=50,
    load_best_model_at_end=True,
    fp16=True,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
)

optimizer = AdamW(
    params=model.parameters(),  # modelin parametreleri
    lr=3e-5,                    # öğrenme hızı -> ilkinde 2e-5 idi, bu model için 3e-5 olarak değiştirildi
    eps=1e-8                    # epsilon değeri
)
```

### Performans Metrikleri

Modelin performansını değerlendirmek için doğruluk (accuracy) ve F1 skoru gibi yaygın metrikler kullanılmıştır. Aşağıda modelin test verisi üzerinde elde edilen değerlendirme sonuçları yer almaktadır:

- Accuracy: 0.7596
- F1-Score: 0.7655