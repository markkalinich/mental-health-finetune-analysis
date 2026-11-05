---
license: apache-2.0
language:
  - tr
base_model: Qwen/Qwen3.5-0.8B-Base
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

# Turkish PII Guard

Türkçe metindeki kişisel verileri **tespit edip yerinde maskeleyen** 0.8B parametreli
model. Girdiyi alır, kişisel veriyi köşeli parantezli etiketle değiştirir, metnin
geri kalanına dokunmaz.

```
Girdi : Ahmet Yıldız 0542 321 45 67 numarasından aradı, ibanı TR12 0001 2000 0034 5678 9012 34
Çıktı : [AD] [TEL] numarasından aradı, ibanı [IBAN]
```

Bir LLM'e veri göndermeden önceki maskeleme katmanı, log temizleme ve KVKK/GDPR
veri minimizasyonu için tasarlandı. 50 PII etiketi tanır.

**En önemli özelliği:** talimatı okur. Aynı metin, farklı politika altında farklı
maskelenir — "yalnızca IBAN'ı gizle", "telefonu açık bırak, gerisini maskele" gibi
kapsam talimatlarına uyar.

---

## Sonuçlar

| Set | Precision | Recall | F1 | Exact Match |
|---|---|---|---|---|
| Test seti A | %99,584 | %99,940 | %99,762 | %99,220 |
| Test seti B | %99,493 | %99,902 | %99,697 | %99,180 |
| **Final Kör Holdout** | **%99,500** | **%99,920** | **%99,709** | **%99,320** |

Metrikler **entity düzeyindedir**: her maskelenen varlık ayrı sayılır.
Exact Match, çıktının beklenen metinle karakter karakter aynı olması demektir.

---

## Kullanım

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "melikegks/turkish-pii-guard-0.8b"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL, dtype=torch.bfloat16, device_map="auto"
).eval()


def maskele(metin, talimat=None, max_new_tokens=256):
    talimat = talimat or (
        "Metindeki tüm kişisel ve hassas bilgileri uygun etiketlerle "
        "maskele. Diğer kısımları değiştirme."
    )
    mesajlar = [
        {"role": "system", "content": talimat},
        {"role": "user", "content": metin},
    ]
    prompt = tokenizer.apply_chat_template(
        mesajlar, tokenize=False, add_generation_prompt=True,
        enable_thinking=False,
    )
    girdi = tokenizer(prompt, return_tensors="pt",
                      add_special_tokens=False).to(model.device)

    with torch.inference_mode():
        cikti = model.generate(
            **girdi,
            max_new_tokens=max_new_tokens,
            do_sample=False,                       # maskeleme belirlenimci olmalı
            eos_token_id=tokenizer.convert_tokens_to_ids("<|im_end|>"),
            pad_token_id=tokenizer.pad_token_id,
        )

    yeni = cikti[0, girdi["input_ids"].shape[1]:]
    return tokenizer.decode(yeni, skip_special_tokens=True).strip()


print(maskele("müşteri Ayşe Yılmaz tc 12345678901 tel 0532 111 22 33"))
# → müşteri [AD] tc [TCKN] tel [TEL]
```

`do_sample=False` kullan. Maskeleme belirlenimci bir görev; örnekleme
tutarsız çıktı üretir.

### Kapsam talimatları

Talimat çıktıyı doğrudan değiştirir:

```python
metin = "Ali Kaya 0532 111 22 33 numarasından aradı, ibanı TR33 0006 1005 1978 6457 8413 26"

maskele(metin)
# → [AD] [TEL] numarasından aradı, ibanı [IBAN]

maskele(metin, "Yalnızca IBAN bilgisini maskele. Adı ve telefonu değiştirme.")
# → Ali Kaya 0532 111 22 33 numarasından aradı, ibanı [IBAN]

maskele(metin, "IBAN'ı açık bırak. Diğer kişisel bilgileri maskele.")
# → [AD] [TEL] numarasından aradı, ibanı TR33 0006 1005 1978 6457 8413 26

maskele(metin, "Bu metinde sadece KVKK madde 6 kapsamındaki özel nitelikli verileri maskele.")
# → Ali Kaya 0532 111 22 33 numarasından aradı, ibanı TR33 0006 1005 1978 6457 8413 26
```

Desteklenen politika biçimleri:

| Politika | Örnek talimat |
|---|---|
| Tam maskeleme | "Metindeki tüm kişisel bilgileri maskele." |
| Beyaz liste | "Yalnızca IBAN ve telefon numarasını maskele." |
| Kara liste | "Ad soyad hariç her şeyi maskele." |
| Kategori | "Sadece finansal bilgileri maskele." |
| Rol | "Log temizleme hattında çalışıyorsun. Tüm PII'yi gizle." |
| Hibrit | "Maaşı gizle, ad soyad ve telefona dokunma." |

Talimat verilmezse tam maskeleme varsayılır, ama **her zaman açık bir talimat ver** —
model talimat üzerine eğitildi.

---

## Etiketler

50 etiket, sekiz kategoride.

| Kategori | Etiketler |
|---|---|
| **Kimlik** | `[AD]` `[TCKN]` `[DOGUM_TARIHI]` `[DOGUM_YERI]` `[ANNE_ADI]` `[ANNE_KIZLIK]` `[BABA_ADI]` `[PASAPORT_NO]` `[EHLIYET_NO]` `[SGK_NO]` `[IMZA]` |
| **Finansal** | `[IBAN]` `[HESAP_NO]` `[KART]` `[KART_SKT]` `[CVV]` `[MAAS]` `[VERGI_NO]` `[MUSTERI_NO]` `[KREDI_NOTU]` `[POLICE_NO]` `[SOZLESME_NO]` `[KRIPTO_CUZDAN]` |
| **İletişim** | `[TEL]` `[EMAIL]` `[ADRES]` `[KONUM]` |
| **Özel nitelikli** (KVKK md. 6) | `[SAGLIK]` `[DIN]` `[ETNIK_KOKEN]` `[SENDIKA]` `[BIYOMETRIK]` `[CEZA_KAYDI]` `[KAN_GRUBU]` `[ENGEL_DURUMU]` |
| **Kimlik doğrulama** | `[SIFRE]` `[PIN]` `[KULLANICI_ADI]` |
| **Cihaz ve ağ** | `[IP_ADRES]` `[MAC_ADRES]` `[IMEI]` `[CIHAZ_ID]` |
| **Araç** | `[PLAKA]` `[SASI_NO]` `[MOTOR_NO]` `[RUHSAT_NO]` |
| **İstihdam ve diğer** | `[SICIL_NO]` `[ISYERI]` `[AILE]` `[REFERANS]` |

---

## Türkçeye özgü davranış

Model regex tabanlı çözümlerin yakalayamadığı varyasyonları tanır.

**Sözle yazılmış değerler.** Eğitim verisinin ~%18'i rakam yerine kelime içerir:

```
tc kimlik numaram otuz dört yirmi üç altmış beş yetmiş sekiz doksan bir
→ tc kimlik numaram [TCKN]
```

**Yüzey biçimi çeşitliliği.** Aynı veri boşluklu, bitişik, noktalı, tireli geçebilir:

```
iban:TR330006100519786457841326,telefon:05321112233
→ iban:[IBAN],telefon:[TEL]
```

**Bağlam ayrımı.** Aynı biçimdeki sayı, bağlama göre farklı sonuç verir:

```
vergi numaram 9840032179 ile fatura kesilsin      → vergi numaram [VERGI_NO] ile fatura kesilsin
gtip kodu 9840032179 ile gümrük beyanı açılsın    → değişmez
kartın arkasındaki güvenlik kodu 732              → kartın arkasındaki güvenlik kodu [CVV]
şube kodu 732 ve işlem kodu 419                   → değişmez
```

**Yazım varyasyonu.** İsimler küçük harfle de tanınır, kısaltmalar desteklenir
(`tcm`, `tc no`, `tcsi`, `telim`, `ibanım`, `vkn`), bozuk Türkçe girdi çalışır.

---

## Sınırlar ve bilinen sorunlar

Bunları okumadan üretime alma.

### 1. Değerlendirme tamamen sentetik

Eğitim ve test verisinin **tamamı sentetiktir**; gerçek kişilere ait kayıt
içermez. Üç test seti de aynı üreticiden gelir. Yukarıdaki skorlar
**dağılım içi** başarımdır. Gerçek kullanıcı metnindeki performans
ölçülmemiştir ve daha düşük olması beklenir.

Kendi verinde ölçmeden kritik bir hatta koyma.

### 2. Şema dışı etiket üretebilir

Model bazen 50 etiketin dışında bir etiket uyduruyor — genellikle metindeki
komşu karakter dizisinden kurarak (`RoHS` → `[ROHS_NO]`, `color` → `[COLOR]`).

5.000 örnekte **9 adet** görüldü (%0,18). Üretimde bir whitelist katmanı öneririz:

```python
import re

GECERLI_ETIKETLER = {"[AD]", "[TCKN]", "[TEL]", "[IBAN]"}   # 50 etiketin tamamı

def whitelist_uygula(cikti):
    """Şema dışı etiket varsa satırı güvenli tarafa çeker."""
    uydurma = [e for e in re.findall(r"\[[A-Z_]+\]", cikti)
               if e not in GECERLI_ETIKETLER]
    if uydurma:
        return None      # reddet veya insan incelemesine gönder
    return cikti
```

Metrik raporlarken **ham model skoru** ile **whitelist sonrası sistem skoru**
ayrı verilmelidir.

### 3. Değişmemesi gereken metni bazen değiştirir

PII içermeyen satırlarda doğruluk **%98,8** (5.000 örnekte 1.871 böyle satırın
22'si). Bu, recall'u %99,9'a çıkarmanın bedelidir. Kaçırılan bir TCKN veri
ihlali, fazladan maskelenen bir kelime kozmetik sorundur — takas bilinçlidir.

### 4. Uzun metin

`max_length=512` token ile eğitildi. Daha uzun metinleri cümle veya paragraf
bazında bölerek ver.

### 5. Yalnızca Türkçe

Başka dillerde test edilmedi.

### 6. Karar destek aracı değildir

Bu model bir **veri minimizasyonu aracıdır**, uyumluluk garantisi değildir.
KVKK/GDPR sorumluluğu kullanandadır. Yasal veya güvenlik açısından kritik
akışlarda insan denetimi gerekir.

---

## Eğitim

| | |
|---|---|
| Taban model | `Qwen/Qwen3.5-0.8B-Base` |
| Yöntem | LoRA (r=32, α=64), bf16, completion-only loss |
| Bağlam | 512 token, packing yok |
| Veri | Sentetik Türkçe fintech/ERP metni, 50 PII etiketi, ~450.000 örnek |
| Split | Modül/şablon düzeyinde — aynı cümle kalıbı hem train hem test'e düşmez |
| Checkpoint seçimi | `eval_loss` ile değil, **entity F1** ile; regresyon guardrail'leriyle |
| Yayım | LoRA adaptörü taban modele merge edildi — bu repo tam modeldir |

Eğitim verisi, ölçülen model hatalarına göre kademeli olarak geliştirildi:
her turda hata dağılımı çıkarıldı, eksik kalan cümle aileleri ve etiket
bağlamları hedefli olarak üretildi, sonuç aynı dondurulmuş test setinde
yeniden ölçüldü.

---

## Alıntı

```bibtex
@misc{turkish-pii-guard,
  title  = {Turkish PII Guard},
  author = {Melike Göksu Tanrıverdi},
  year   = {2026},
  url    = {https://huggingface.co/melikegks/turkish-pii-guard-0.8b}
}
```

Taban model [Qwen3.5](https://huggingface.co/Qwen) — Apache 2.0.
