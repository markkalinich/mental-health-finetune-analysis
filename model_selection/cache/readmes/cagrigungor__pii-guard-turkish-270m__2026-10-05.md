---
language:
- tr
license: gemma
base_model: google/gemma-3-270m-it
pipeline_tag: text-generation
library_name: transformers
tags:
- pii
- anonymization
- masking
- kvkk
- gdpr
- turkish
- privacy
- fintech
---

# PII Guard Turkish 270M

Cihaz üstü (mobil) kullanım için tasarlanmış, Türkçe metindeki kişisel verileri **talimat-koşullu** maskeleyen 270M parametreli model. Bu repo kullanıma hazır tam modeldir; telefonda çalıştırmak için GGUF sürümüne bakın: [pii-guard-turkish-270m-gguf](https://huggingface.co/cagrigungor/pii-guard-turkish-270m-gguf).

```
Girdi : Ahmet Yıldız 0542 321 45 67 numarasından aradı, ibanı TR12 0001 2000 0034 5678 9012 34
Çıktı : [AD] [TEL] numarasından aradı, ibanı [IBAN]
```

Bir LLM'e veri göndermeden önceki maskeleme katmanı, log temizleme ve KVKK/GDPR veri
minimizasyonu için tasarlandı. **53 PII etiketi** tanır ve **talimat okur**: aynı metin,
farklı politika altında farklı maskelenir.

## Sonuçlar

Eğitim verisinden tamamen bağımsız, elle kurulmuş 1.000 örneklik benchmark üzerinde
**satır düzeyi tam eşleşme** (çıktının beklenen metinle karakter karakter aynı olması —
tek bir etiket hatası satırın tamamını yanlış sayar):

| Model | Tam Eşleşme (1000) | Şema-nötr (903) |
|---|---|---|
| cagrigungor/pii-guard-turkish-0.8b | **0.876** | **0.889** |
| cagrigungor/pii-guard-turkish-0.6b | 0.828 | 0.850 |
| cagrigungor/pii-guard-turkish-270m | 0.740 | 0.770 |
| melikegks/turkish-pii-guard-0.8b | 0.731 | 0.810 |

Şema-nötr sütun, `[YAS] [CINSIYET] [UYRUK]` etiketlerinin maskelenmesini gerektiren 97 satır
hariç tutularak hesaplanır (bu üç etiket her modelin şemasında bulunmadığından modeller arası
adil kıyas bu sütundur). Benchmark halka açıktır ve yeniden üretilebilir:

- Kaggle: https://www.kaggle.com/datasets/aiwithcagri/turkish-pii-masking-benchmark
- Hugging Face: https://huggingface.co/datasets/cagrigungor/turkish-pii-masking-benchmark

Benchmark bileşimi: tam maskeleme (350), beyaz liste (200), kara liste (150), kapsam dışı (100),
tuzaklı negatif (200); içinde BÜYÜK HARF, Türkçe ek almış PII, sözle yazılmış numaralar,
çok kişili metinler ve 300-900 karakterlik uzun girdiler işaretli dilimler halinde bulunur.

Kategori kırılımı (bu model): tam maskeleme 0.723 · beyaz liste 0.620 ·
kara liste 0.740 · kapsam dışı 0.730 · negatif 0.895. Zor dilimler: ekli PII 0.818 ·
BÜYÜK HARF 0.505 · uzun metin 0.521 · sözle yazım 0.649.

## Eğitim

| | |
|---|---|
| Taban model | google/gemma-3-270m-it |
| Yöntem | LoRA (r=16, alfa=32), bf16, completion-only loss, Unsloth |
| Bağlam | 768 token |
| Veri | Sentetik Türkçe bankacılık/ERP metni, 53 PII etiketi, ~400.000 örnek |
| Split | Modül düzeyinde train/val ayrımı; benchmark tamamen bağımsız üretim |


## Kullanım

Prompt biçimi eğitimle birebir aynı olmalıdır. Gemma mimarisi prompt başında **BOS token**
ister; `add_special_tokens=False` kullanıyorsan BOS'u elle ekle, yoksa çıktı bozulur.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "cagrigungor/pii-guard-turkish-270m"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL, dtype=torch.bfloat16, device_map="auto").eval()

def maskele(metin, talimat="Metindeki tüm kişisel verileri uygun etiketlerle maskele."):
    prompt = (f"{tokenizer.bos_token}<start_of_turn>user\n{talimat}\n\n"
              f"Metin: {metin}<end_of_turn>\n<start_of_turn>model\n")
    girdi = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to(model.device)
    with torch.inference_mode():
        cikti = model.generate(**girdi, max_new_tokens=512, do_sample=False,
                               eos_token_id=tokenizer.convert_tokens_to_ids("<end_of_turn>"),
                               pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(cikti[0, girdi["input_ids"].shape[1]:],
                            skip_special_tokens=True).strip()

print(maskele("müşteri Ayşe Yılmaz tc 12345678901 tel 0532 111 22 33"))
# -> müşteri [AD] tc [TCKN] tel [TEL]
```

## Politika biçimleri

Model talimatı okur; aynı metin farklı politika altında farklı maskelenir.

| Politika | Örnek talimat |
|---|---|
| Tam maskeleme | "Metindeki tüm kişisel verileri uygun etiketlerle maskele." |
| Beyaz liste | "Sadece IBAN ve telefon numarasını maskele. Gerisi aynen kalsın." |
| Kara liste | "Ad soyad hariç bütün hassas alanları etiketle." |
| Kategori | "Yalnızca özel nitelikli kişisel veriler maskelenecek." |
| Kapsam dışı | Talimatta istenen etiket metinde yoksa çıktı girdiyle aynı kalır. |

## Etiketler

53 etiket, dokuz kategoride.

| Kategori | Etiketler |
|---|---|
| Kimlik | `[AD]` `[TCKN]` `[DOGUM_TARIHI]` `[DOGUM_YERI]` `[ANNE_ADI]` `[ANNE_KIZLIK]` `[BABA_ADI]` `[PASAPORT_NO]` `[EHLIYET_NO]` `[SGK_NO]` `[IMZA]` |
| Finansal | `[IBAN]` `[HESAP_NO]` `[KART]` `[KART_SKT]` `[CVV]` `[MAAS]` `[VERGI_NO]` `[MUSTERI_NO]` `[KREDI_NOTU]` `[POLICE_NO]` `[SOZLESME_NO]` `[KRIPTO_CUZDAN]` |
| İletişim | `[TEL]` `[EMAIL]` `[ADRES]` `[KONUM]` |
| Özel nitelikli (KVKK md. 6) | `[SAGLIK]` `[DIN]` `[ETNIK_KOKEN]` `[SENDIKA]` `[BIYOMETRIK]` `[CEZA_KAYDI]` `[KAN_GRUBU]` `[ENGEL_DURUMU]` |
| Kimlik doğrulama | `[SIFRE]` `[PIN]` `[KULLANICI_ADI]` |
| Cihaz ve ağ | `[IP_ADRES]` `[MAC_ADRES]` `[IMEI]` `[CIHAZ_ID]` |
| Araç | `[PLAKA]` `[SASI_NO]` `[MOTOR_NO]` `[RUHSAT_NO]` |
| İstihdam ve diğer | `[SICIL_NO]` `[ISYERI]` `[AILE]` `[REFERANS]` |
| Demografi | `[YAS]` `[CINSIYET]` `[UYRUK]` |

## Türkçeye özgü davranış

- **Ek almış PII**: kesme işaretli ekler ünlü uyumuyla korunur —
  `Ayşe Yılmaz'ın hesabına havale yap` -> `[AD]'ın hesabına havale yap`
- **Sözle yazılmış değerler**: `tc kimlik numaram yedi bir dokuz yedi ...` -> `tc kimlik numaram [TCKN]`
- **BÜYÜK HARF girdi**: `ADIM AHMET TC 12345678901` -> `ADIM [AD] TC [TCKN]`
- **Çok kişili metin**: aynı cümledeki farklı kişiler ayrı ayrı maskelenir
- **Tuzaklara direnç**: fatura/sipariş numarası, şehir adlı projeler, "tc kimlik alanı boş
  bırakılamaz" gibi PII kelimesi geçen ama PII içermeyen metinler değiştirilmez

## Sınırlar

1. **Değerlendirme sentetik veriyle yapılmıştır.** Eğitim ve benchmark verisi Faker + LLM
   üretimidir; gerçek kişi verisi içermez. Gerçek kullanıcı metnindeki performans ölçülmemiştir.
   Kendi verinde ölçmeden kritik bir hatta koyma.
2. **Şema dışı etiket üretebilir.** Üretimde 53 etiketlik bir whitelist katmanı öneririz;
   şema dışı etiket içeren çıktıyı reddedip insan incelemesine gönder.
3. **Zayıf dilimler** (benchmark kırılımından): kara liste talimatları ve sözle yazılmış
   uzun sayı dizileri en düşük skorlu dilimlerdir. Bu dilimlerde çıktı doğrulaması ekle.
4. **Yalnızca Türkçe.** Başka dillerde test edilmedi.
5. **Karar destek aracı değildir.** KVKK/GDPR sorumluluğu kullanandadır; kritik akışlarda
   insan denetimi gerekir.

## Yazar

Hasan Çağrı Güngör
iletisim@cagrigungor.com — https://finiscode.com

## Alıntı

```bibtex
@misc{pii-guard-turkish,
  title  = {PII Guard Turkish},
  author = {Hasan Çağrı Güngör},
  year   = {2026},
  url    = {https://huggingface.co/cagrigungor/pii-guard-turkish-270m}
}
```
