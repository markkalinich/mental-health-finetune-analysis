---
license: mit
language:
- id
base_model:
- sentence-transformers/paraphrase-multilingual-mpnet-base-v2
library_name: setfit
tags:
- setfit
- sentence-transformers
- sentiment
- indonesian
---
# SetFit Indonesian Sentiment Analysis 

### Model Description

This model uses the `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` base model, which is trained with the Indonesian sentiment dataset.

In v1, this model can predict 2 sentiments. Namely `baik` and `buruk` sentiments.

### Usage
```python
from setfit import SetFitModel

model = SetFitModel.from_pretrained("wuriyanto/setfit-paraphrase-multilingual-mpnet-base-v2-indonesian-sentiment-v1")

texts_to_classify = ["Pemerintah kurang memperhatikan kesejahteraan masyarakat, sehingga banyak kriminal dimana-mana",
                     "Makanan yang dihidangkan cukup enak, beberapa orang juga menyampaikan jika fasilitas, terutama meja, kursi dan kamar mandi sangat bersih.",
                     "Tempat perbelanjaan tersebut secara harga cukup terjangkau, dan tidak jauh dari tempat tinggal mahasiswa",
                     "Suka dengan layanan yang diberikan. Harga juga cukup terjangkau bagi masyarakat menengah ke bawah.", 
                     "Dengan banyaknya barang import murah yang masuk ke tengah-tengah masyarakat, menyebabkan beberapa UMKM bangkrut"]
predictions = model.predict(texts_to_classify)

for text, prediction in zip(texts_to_classify, predictions):
    print(f"Text: {text} -> Sentiment: {prediction}")
```