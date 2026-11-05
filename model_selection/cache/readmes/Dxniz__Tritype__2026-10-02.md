---
language:
  - en
  - tr
license: apache-2.0
tags:
  - text-generation-inference
  - transformers
  - unsloth
  - qwen3
  - psychology
  - mbti
  - enneagram
  - big-five
  - json
  - structured-output
  - personality-analysis
base_model: unsloth/qwen3-14b-unsloth-bnb-4bit
pipeline_tag: text-generation
---

# Tritype (Qwen3 Edition)

**Developed by:** Dxniz  
**License:** Apache-2.0  
**Finetuned from model:** [unsloth/qwen3-14b-unsloth-bnb-4bit](https://huggingface.co/unsloth/qwen3-14b-unsloth-bnb-4bit)

## Model Description

**Tritype** is a specialized fine-tuned model built on the Qwen3-14B architecture, designed for in-depth psychological analysis and personality profiling. Unlike general-purpose language models, Tritype produces outputs in a strict, parseable JSON format, integrating multiple personality typology frameworks such as MBTI, Enneagram, and Big Five to simulate complex human psychology.

This model leverages Unsloth for 2x faster training and Hugging Face's TRL library for efficient fine-tuning.

**Tritype**, Qwen3-14B mimarisi üzerine inşa edilmiş, derinlemesine psikolojik analiz ve kişilik profillemesi için özel olarak fine-tune edilmiş bir modeldir. Genel amaçlı modellerden farklı olarak, Tritype çıktıları katı ve ayrıştırılabilir JSON formatında üretir; MBTI, Enneagram, Big Five gibi birden fazla kişilik tipoloji çerçevesini entegre ederek karmaşık insan psikolojisini simüle eder.

Bu model, Unsloth ile 2 kat daha hızlı eğitim ve Hugging Face'in TRL kütüphanesi ile verimli fine-tuning kullanılarak geliştirilmiştir.

## Key Features

- **Extended Context Window:** Supports up to 16,000 tokens, enabling analysis of extensive texts (equivalent to approximately 75 question-answer interactions) in a single pass.
- **Strict JSON Output:** Generates reliable, error-free structured JSON responses, ideal for application and API integrations.
- **Deep Psychological Insights:** Interprets beyond surface-level text to uncover internal monologues, subconscious drives, and hidden motivations.
- **Multi-Typology Integration:** Combines MBTI, Enneagram, Big Five, and related systems for comprehensive personality assessments.

- **Geniş Context Penceresi:** 16.000 token kapasitesiyle uzun metinleri (yaklaşık 75 soru-cevap etkileşimi) tek seferde analiz edebilir.
- **Katı JSON Çıktı:** Uygulama ve API entegrasyonları için hatasız, yapılandırılmış JSON yanıtlar üretir.
- **Derin Psikolojik Analiz:** Yüzeysel metnin ötesine geçerek iç sesi, bilinçaltı dürtüleri ve gizli motivasyonları yorumlar.
- **Çoklu Tipoloji Desteği:** MBTI, Enneagram, Big Five ve ilgili sistemleri entegre ederek kapsamlı kişilik profilleri oluşturur.

## Intended Uses

Tritype is intended for:
- Psychological simulations and personality typing in research or educational contexts.
- Structured analysis of text-based inputs, such as dialogues, journals, or user-generated content, to derive personality insights.
- Integration into applications requiring JSON-formatted psychological profiles, such as chatbots, HR tools, or mental health support prototypes (with appropriate ethical oversight).

Tritype şu amaçlar için tasarlanmıştır:
- Araştırma veya eğitim bağlamlarında psikolojik simülasyonlar ve kişilik tipolojisi.
- Diyaloglar, günlükler veya kullanıcı tarafından üretilen içerikler gibi metin tabanlı girdilerin yapılandırılmış analizi için kişilik içgörüleri türetme.
- Sohbet botları, İK araçları veya zihinsel sağlık destek prototipleri gibi JSON formatlı psikolojik profiller gerektiren uygulamalara entegrasyon (uygun etik denetimle).

## Out-of-Scope Uses

- This model should not be used for clinical diagnosis, therapy, or any professional psychological services.
- Avoid deployment in sensitive scenarios involving real individuals without consent and expert supervision.
- Not suitable for generating harmful, biased, or unethical content.

- Bu model klinik teşhis, terapi veya herhangi bir profesyonel psikolojik hizmet için kullanılmamalıdır.
- Gerçek bireyleri içeren hassas senaryolarda rıza ve uzman denetimi olmadan dağıtılmamalıdır.
- Zararlı, önyargılı veya etik olmayan içerik üretimi için uygun değildir.

## Training Data

The model was fine-tuned on a high-quality dataset comprising **112,000 examples** of psychological scenarios, clinical observations, personality typology theories, and synthesized dialogues.

- **Dataset:** [Dxniz/Psychology_Large](https://huggingface.co/datasets/Dxniz/Psychology_Large)
- **Format:** Instruction-Input-Response (Alpaca format)

Model, psikolojik senaryolar, klinik gözlemler, kişilik tipolojisi teorileri ve sentezlenmiş diyaloglardan oluşan **112.000 satırlık** yüksek kaliteli bir veri seti üzerinde fine-tune edilmiştir.

## Limitations and Ethical Considerations

- **Limitations:** Outputs are based on trained patterns and typology theories, which may lack full scientific consensus. The model is not a substitute for professional psychological evaluation. Performance may vary on non-English texts despite bilingual support.
- **Bias and Fairness:** The training data may reflect biases present in psychological literature; users should critically evaluate outputs for cultural or demographic sensitivities.
- **Ethical Use:** Exercise caution with sensitive topics like trauma or mental health. The model simulates empathy but cannot provide genuine emotional support.

- **Sınırlamalar:** Çıktılar, eğitimli kalıplara ve tipoloji teorilerine dayanır; bunlar tam bilimsel uzlaşıya sahip olmayabilir. Model, profesyonel psikolojik değerlendirmenin yerini tutmaz. İngilizce dışı metinlerde performans değişebilir.
- **Önyargı ve Adalet:** Eğitim verisi, psikolojik literatürdeki önyargıları yansıtabilir; kullanıcılar kültürel veya demografik hassasiyetler açısından çıktıları eleştirel değerlendirmelidir.
- **Etik Kullanım:** Travma veya zihinsel sağlık gibi hassas konularda dikkatli olunmalıdır. Model empati simüle etse de gerçek duygusal destek sağlayamaz.

## Citation

If you use this model in your work, please cite it as:

```bibtex
@misc{tritype-qwen3,
  author = {Dxniz},
  title = {Tritype: Fine-Tuned Qwen3-14B for Structured Psychological Analysis},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/Dxniz/Tritype}
}
```