---
license: mit
language:
- tr
metrics:
- accuracy
- f1
base_model:
- dbmdz/bert-base-turkish-cased
pipeline_tag: text-classification
library_name: transformers
tags:
- absa
- nlp
- sentiment
- turkish
---

# Clothing ABSA Model (v2)

## Model Tanıtımı

Bu model, Türkçe metinler üzerinde **Sentiment Analysis (Duygu Analizi)** yapmak için Türkçe dilindeki giyim ürünlerine ait metinlerden oluşturulan veri kümesi kullanılarak fine-tune edilmiş bir ABSA (Aspect-Based Sentiment Analysis) modelidir. 
Model, `dbmdz/bert-base-turkish-cased` temel modelinden türetilmiştir ve Türkçe dilindeki metinlerde olumlu, olumsuz veya nötr duygu kategorilerine ait etiketleri tahmin edebilmektedir.


- **Developed by:** [[ebru kılıç](https://huggingface.co/ebrukilic) , [rumeysa nur yasav](https://huggingface.co/rmysysv)]
- **Model type:** [Fine-Tuned ABSA Model]
- **License:** [MIT]
- **Finetuned from model [optional]:** [dbmdz/bert-base-turkish-cased]

Bu model, doğrudan metin verisini alıp duygu etiketlerini tahmin etmek için kullanılabilir. Modelin çıktı olarak "olumlu", "olumsuz" veya "nötr" etiketlerinden birini döndürmesi beklenir.Model, sadece duygu analizi için eğitilmiştir. Karmaşık doğal dil işleme (NLP) görevleri, makale yazımı veya özetleme gibi işlemler için uygun değildir.

## Modeli Nasıl Kullanabiliriz?

Modeli, `transformers` kütüphanesini kullanarak yükleyebilir ve metinlerdeki duygu analizini gerçekleştirebilirsiniz.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# modelin ve tokenizerın yüklenmesi
model_name = "ebrukilic/bert-absa-tr-2"
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

[ebrukilic/clothing_products_ABSA_v2](https://huggingface.co/datasets/ebrukilic/clothing_products_ABSA_v2)

Model, Türkçe metinlerdeki kullanıcı yorumları ve ilgili "aspect"ler (özellikler) kullanılarak eğitildi. Etiketler, 3 sınıflı duygu (polarite) kategorisinde `negatif`, `nötr` ve `pozitif` olarak tanımlanmıştır. Veri kümesi eğitim ve test olmak üzere toplamda 11,470 örnekten oluşmaktadır.

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

### Test Sonucu

ebrukilic/tubitak_clothing_absa_v3 veri kümesi üzerinde yapılan test sonucu aşağıdaki gibidir.

- **Device:** cuda  
- **Label mapping:** `{'negatif': 0, 'nötr': 1, 'pozitif': 2}`  
- **Accuracy:** 0.726  
- **Macro-F1:** 0.785  

### Aspect-aware Evaluation
- Accuracy: 0.8310  
- Macro-F1: 0.7850

| Label   | Precision | Recall | F1-score | Support |
|---------|-----------|--------|----------|---------|
| negatif | 0.93      | 0.82   | 0.87     | 1719    |
| nötr    | 0.55      | 0.64   | 0.59     | 653     |
| pozitif | 0.87      | 0.92   | 0.89     | 1639    |
| **macro avg** | 0.78 | 0.79 | 0.79 | 4011 |
| **weighted avg** | 0.84 | 0.83 | 0.83 | 4011 |

### Text-only Evaluation
- Accuracy: 0.6457  
- Macro-F1: 0.5893

| Label   | Precision | Recall | F1-score | Support |
|---------|-----------|--------|----------|---------|
| negatif | 0.78      | 0.63   | 0.70     | 1719    |
| nötr    | 0.27      | 0.38   | 0.32     | 653     |
| pozitif | 0.74      | 0.77   | 0.75     | 1639    |
| **macro avg** | 0.60 | 0.59 | 0.59 | 4011 |
| **weighted avg** | 0.68 | 0.65 | 0.66 | 4011 |

### Summary
- Aspect-aware: Acc=0.831, F1=0.785  
- Text-only:    Acc=0.646, F1=0.589  
- Aspect effect: +28.7%