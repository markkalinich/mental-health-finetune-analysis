---
language: en
tags:
- text-classification
- sentiment-analysis
- distilbert
datasets:
- stanfordnlp/imdb
---

# Oyuncu Yorumu Analiz Modeli

## Model Açıklaması
Bu model, oyunlara gelen kullanıcı yorumlarını analiz etmek ve "Olumlu" veya "Olumsuz" olarak sınıflandırmak için geliştirildi. Temel model olarak `distilbert-base-uncased` kullanıldı ve İngilizce metinleri sınıflandırmak üzere fine-tune işlemi uygulandı.

## Eğitim Verisi
Modeli eğitmek için `stanfordnlp/imdb` veri setinden rastgele 5.000 adet inceleme metni seçtim. Eğitim sırasında modelin sadece olumsuz veya sadece olumlu örnekleri görüp ezberlememesi (veri yanlılığı/data bias oluşmaması) için veri setini eğitime sokmadan önce tamamen karıştırdım (shuffle).

## Kullanım Amacı
Geliştirici ekiplerin yüzlerce Steam veya Discord yorumunu manuel olarak okumak yerine;
* Yeni gelen güncellemeler sonrası oyuncuların genel tepkisini hızlıca ölçmek,
* Çökme, bug veya optimizasyon sorunlarını anlatan negatif yorumları (LABEL_0) tespit edip filtrelemek amacıyla kullanılabilir.

## Eğitim Sonuçları ve Performans
Modeli 2 epoch boyunca eğittim. Değerlendirme (Validation) seti üzerindeki test sonuçlarım şu şekilde:
* **Accuracy (Doğruluk):** 1.0 
* **Validation Loss:** 0.000143

## Sınırlılıklar
* Model İngilizce metinler üzerinde eğitildiği için Türkçe geri bildirimlerde çalışmaz.
* Yapay zeka modellerinin genel bir zorluğu olarak, aşırı kinaye veya ironi içeren yorumları (Örn: "Oyun o kadar kusursuz ki ekran kartım dayanamayıp yandı") yanlış sınıflandırabilir.

## Örnek Kullanım (Inference) Modülü
Modelin çalıştığını doğrulamak için aşağıdaki Python kodunu kullanabilirsiniz:

```python
from transformers import pipeline

# Modeli çağırıyoruz
classifier = pipeline("text-classification", model="SerkLones/oyuncu-yorumu-analiz-modeli")

# Örnek 1: Olumlu Yorum Testi
yorum_olumlu = "This game is an absolute masterpiece, the mechanics are amazing!"
print("Olumlu Yorum:", classifier(yorum_olumlu))
# Beklenen Çıktı: [{'label': 'LABEL_1', 'score': 0.9616}]

# Örnek 2: Olumsuz Yorum Testi
yorum_olumsuz = "The game crashes constantly and the optimization is terrible, I want a refund."
print("Olumsuz Yorum:", classifier(yorum_olumsuz))
# Beklenen Çıktı: [{'label': 'LABEL_0', 'score': 0.9056}]