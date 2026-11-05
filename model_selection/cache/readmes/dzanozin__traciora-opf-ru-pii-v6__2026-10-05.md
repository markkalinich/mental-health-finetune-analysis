---
model_name: traciora-opf-ru-pii-v6
language:
  - ru
tags:
  - token-classification
  - pii-detection
  - privacy
  - russian
  - opf
  - openai-privacy-filter
library_name: opf
pipeline_tag: token-classification
license: apache-2.0
---

# traciora-opf-ru-pii-v6

**Links:** [traciora.com](https://traciora.com) · [traciora.ru](https://traciora.ru) · [openai/privacy-filter](https://github.com/openai/privacy-filter) (base)

`traciora-opf-ru-pii-v6` is a Russian / RU-identifier fine-tuned checkpoint for OpenAI Privacy Filter (OPF). It is intended to detect Russian-language personally identifiable information and Russian structured identifiers as a second-layer privacy filter.

This checkpoint is a release-candidate / research-preview model, not a standalone production privacy system. It performs substantially better than the base OPF checkpoint on the Russian/RU-identifier eval surface, but known false positives remain.

## О модели (RU)

`traciora-opf-ru-pii-v6` — дообученный чекпойнт OpenAI Privacy Filter (OPF) для детекции персональных данных (ПДн) в русскоязычном тексте. Модель распознаёт категории, релевантные требованиям [Федерального закона № 152-ФЗ](http://www.consultant.ru/document/cons_doc_LAW_61801/) «О персональных данных» и связанной нормативной базы:

- **Идентификаторы личности**: ФИО (`[PERSON_NAME]`), паспортные данные (`[RU_PASSPORT]`), ИНН (`[RU_INN]`), СНИЛС (`[RU_SNILS]`).
- **Контактные данные**: телефон (`[RU_PHONE]`), email (`[EMAIL]`), физический адрес (`[STREET_ADDRESS]`).
- **Реквизиты транспортных средств**: госномер (`[LICENSE_PLATE]`), VIN (`[RU_VIN]`), водительское удостоверение (`[RU_DRV_LICENSE]`), СТС (`[RU_STS]`), полис ОСАГО (`[RU_OSAGO]`).
- **Финансовые реквизиты**: банковский счёт (`[RU_BANK_ACCOUNT]`), БИК (`[RU_BIK]`), КПП (`[RU_KPP]`), номер карты (`[CARD]`), IBAN (`[IBAN]`).
- **Прочее**: ОГРН (`[RU_OGRN]`), IP-адрес (`[IP]`), ключи доступа и секреты (`[SECRET]`).

### Назначение

Модель предназначена как **второй слой** контура защиты ПДн в продуктовых пайплайнах:

- маскирование ПДн перед отправкой запросов в LLM-провайдеры,
- очистка логов и обучающих датасетов,
- автоматизированный аудит соответствия 152-ФЗ.

Не предназначена как единственный механизм защиты: для критичных задач рекомендуется сочетать с детерминистическими regex-фильтрами и валидацией контрольных сумм (ИНН, СНИЛС, БИК).

### Качество

На внутреннем валидационном наборе из 650 русскоязычных примеров модель достигает macro precision **0.985** и macro recall **0.997** в режиме raw OPF-all. Базовый OPF на этом же наборе показывает 0.174 / 0.291 — дообучение на специфике русских идентификаторов и hard-negatives заметно поднимает качество. Полные таблицы по меткам — в разделе [Evaluation](#evaluation) ниже.

### Быстрый старт

```bash
pip install "opf @ git+https://github.com/openai/privacy-filter.git@f7f00ca7fb869683eb732c010299d901457f19c3"
hf download dzanozin/traciora-opf-ru-pii-v6 --local-dir ./traciora-opf-ru-pii-v6
opf --checkpoint ./traciora-opf-ru-pii-v6 --device cuda \
    "Иванов Иван Иванович, тел. +7 916 123-45-67, ИНН 7707083893"
```

### Ограничения и приватность

Модель — релиз-кандидат, не финальная версия. Известные ограничения и аудит на запоминание обучающих значений описаны в разделах [Limitations](#limitations) и [Memorization Audit](#memorization-audit) ниже. Английский текст рекомендуется направлять в базовый OPF, а не в эту модель.

## Loading

This is **not** an HF transformers model. It uses tiktoken `o200k_base` encoding and the custom `privacy_filter` model class shipped with the [`opf`](https://github.com/openai/privacy-filter) package. `AutoModel.from_pretrained(...)` and `AutoTokenizer.from_pretrained(...)` will not work.

```bash
pip install "opf @ git+https://github.com/openai/privacy-filter.git@f7f00ca7fb869683eb732c010299d901457f19c3"
hf download dzanozin/traciora-opf-ru-pii-v6 --local-dir ./traciora-opf-ru-pii-v6
opf --checkpoint ./traciora-opf-ru-pii-v6 --device cuda "Алиса родилась 1990-01-02."
```

See `USAGE.txt` for more invocation examples.

## Policy

Dates, DOB-like strings, URLs, and URL-containing text are intentionally treated as non-PII for this project unless another PII span appears inside the text. This differs from some privacy-filter deployments and should be reviewed before reuse.

## Labels

The checkpoint uses a custom v6 Russian PII label space with these span labels:

`O`, `account_number`, `private_address`, `private_email`, `private_person`, `private_phone`, `secret`, `vehicle_plate`, `ru_inn`, `ru_snils`, `ru_passport`, `ru_ogrn`, `ru_bank_account`, `ru_bik`, `ru_kpp`, `payment_card`, `iban`, `ip_address`, `ru_vin`, `ru_drv_license`, `ru_sts`, `ru_osago`.

Typical production placeholder mapping:

| Label | Placeholder |
|---|---|
| `private_person` | `[PERSON_NAME]` |
| `private_address` | `[STREET_ADDRESS]` |
| `private_email` | `[EMAIL]` |
| `private_phone` | `[RU_PHONE]` |
| `vehicle_plate` | `[LICENSE_PLATE]` |
| `account_number`, `ru_bank_account` | `[RU_BANK_ACCOUNT]` |
| `payment_card` | `[CARD]` |
| `iban` | `[IBAN]` |
| `ip_address` | `[IP]` |
| `secret` | `[SECRET]` |
| `ru_inn`, `ru_snils`, `ru_passport`, `ru_ogrn`, `ru_bik`, `ru_kpp`, `ru_vin`, `ru_drv_license`, `ru_sts`, `ru_osago` | matching `[RU_*]` placeholder |

## Intended Use

Use this model for:

- Russian-language PII detection.
- Russian identifier detection in otherwise mixed text.
- Second-layer privacy filtering behind deterministic regex/rule filters.
- Research and benchmarking of Russian PII detection.

Recommended routing:

- Use base OPF for clearly English-only text.
- Use `traciora-opf-ru-pii-v6` for Cyrillic text or Russian identifier patterns.
- For best Russian name and address behavior, pair the model with `pymorphy3`-based morphology handling for inflection-aware normalization, matching, and post-processing.

Do not use this model as the only control for high-risk privacy, compliance, medical, legal, or financial workflows without additional deterministic checks, logging, review, and domain-specific validation.

## Training Data

Training slug: `v6-ru-all-5k`

- Train records: `121,375`
- Validation records: `12,137`
- Positive label target: at least `5,000` train spans per non-`O` label
- Validation target: at least `500` validation spans per non-`O` label
- Hard-negative multiplier: `3x`
- Structured-format ratio: `0.15`

Data sources and generation:

- Synthetic Russian names, addresses, phones, emails, financial identifiers, government identifiers, vehicle identifiers, driver documents, cards, IBANs, IPs, and secrets.
- Curated internal Russian-format names, phone numbers, and license plates were used as allowed source material.
- Internal source pools were split before generation:
  - names by full normalized name;
  - phones by canonical `+7XXXXXXXXXX`;
  - license plates by normalized plate surface, preserving Cyrillic/Latin variants in the same split.
- Phone and plate train/validation/test source overlap: `0`.
- Names, phones, plates, vehicles, and identifiers were independently sampled. Real customer-to-phone/name/plate pairings were not preserved.

Hard negatives include dates, DOB-like strings, URLs, placeholders, vault references, coordinates, room/office fragments, order IDs, VIN-like strings, truncated identifiers, account/INN lookalikes, BIK/bank-account lookalikes, and structured log/code formats.

## Evaluation

The main publish eval contains `650` synthetic examples:

- `420` positive examples (`20` per non-`O` label × `21` non-`O` labels)
- `150` policy hard negatives
- `50` mixed multi-PII examples
- `30` structured-format examples

### Main Publish Eval

Same 650-query v6 publish eval, raw OPF-all mode:

| Model | Macro Precision | Macro Recall | TP / FP / FN | Policy Hard-Neg FPs | Date/URL FPs | Coordinate-as-Address FPs |
|---|---:|---:|---:|---:|---:|---:|
| Base OPF | `0.174` | `0.291` | `236 / 635 / 454` | `278` | `267` | `85` |
| `traciora-opf-ru-pii-v6` | `0.985` | `0.997` | `688 / 19 / 2` | `17` | `17` | `0` |

Per-label highlights for `traciora-opf-ru-pii-v6`:

| Placeholder | Precision | Recall |
|---|---:|---:|
| `[PERSON_NAME]` | `1.000` | `1.000` |
| `[STREET_ADDRESS]` | `1.000` | `1.000` |
| `[RU_PHONE]` | `1.000` | `1.000` |
| `[EMAIL]` | `1.000` | `1.000` |
| `[RU_INN]` | `0.952` | `1.000` |
| `[RU_BANK_ACCOUNT]` | `0.746` | `1.000` |
| `[RU_BIK]` | `1.000` | `1.000` |
| `[RU_VIN]` | `1.000` | `1.000` |
| `[RU_DRV_LICENSE]` | `1.000` | `1.000` |
| `[RU_STS]` | `1.000` | `1.000` |
| `[RU_OSAGO]` | `1.000` | `1.000` |

Per-example eval data is omitted from this release because the synthetic test corpus may contain values that are sensitive in aggregate. Headline numbers are reproduced inline above.

### Domain Generalization Probe

Current domain probe result:

- Overall precision: `0.944`
- Overall recall: `1.000`

Known domain false positives:

- Passport issue date `12.06.2018` tagged as `[RU_PASSPORT]`.
- Organization name `ООО Альфа` tagged as `[PERSON_NAME]`.
- Word `отозван` tagged as `[SECRET]`.

### Stress Probe

Scored stress probe result:

- TP / FP / FN: `24 / 8 / 1`
- Critical wrong-label failures: `0`
- Syntax-boundary failures: `2`

Known stress issues:

- Python phone span can include adjacent syntax such as `="`.
- CSV phone span can include a leading comma.
- Truncated values can still be tagged, for example truncated KPP/phone-like fragments.

### Memorization Audit

A privacy-safe membership-style audit (no raw PII values in the report) is published as `memorization_audit.md` / `memorization_audit.json`. It compares per-label exact-detection rates between train-seen source values and matched held-out values for `private_person`, `private_phone`, and `vehicle_plate`. The audit is privacy-safe because OPF is a token classifier — it cannot generate memorized PII; the relevant signal is whether train-seen values are detected materially better than matched held-out values.

Audit configuration: `sample_size=200` per (label × membership × context), seed `20260425`, 12 buckets total.

Headline results:

| Bucket | Train-Seen Exact | Held-out Exact | Gap |
|---|---:|---:|---:|
| `private_person` / contextual | `0.975` | `0.995` | `−0.020` |
| `private_person` / bare | `0.895` | `0.955` | `−0.060` |
| `private_phone` / contextual | `1.000` | `1.000` | `0.000` |
| `private_phone` / bare | `0.635` | `0.360` | **`+0.275`** |
| `vehicle_plate` / contextual | `1.000` | `1.000` | `0.000` |
| `vehicle_plate` / bare | `1.000` | `1.000` | `0.000` |

Source-split gates: phones and plates show `0` overlap across train/validation/test source splits.

Disclosed finding: in the **bare** context (`Проверочное значение <X> конец` — no telephone-related framing), train-seen Russian phone numbers are detected at a higher exact rate than held-out phones (0.635 vs 0.360, +27.5pp gap). In the **contextual** template (`Контактный телефон клиента <X> указан в заявке`), both buckets reach 1.000 — i.e. once any normal phone-related context is present, the gap disappears. Names and plates show no positive gap. The bare-phone gap is consistent with the model leaning on lexical familiarity when stripped of all telephone framing; in realistic deployments this bucket is rarely encountered. Users requiring stronger guarantees should (a) prefer the contextual surfaces this model was trained on, and (b) keep deterministic phone regex pre-filters in the pipeline.

## Limitations

Known limitations at release-candidate stage:

- Over-detects some order/log IDs such as `ORD-900010` as `[RU_BANK_ACCOUNT]`.
- Can misclassify AmEx-style payment card numbers as `[RU_INN]`.
- Can still tag dates in passport-issue context as passport numbers.
- Does not solve public-figure, fictional-character, or organization/person ambiguity.
- Does not guarantee perfect span boundaries around code, JSON, CSV, SQL, or punctuation-adjacent values.
- English-only text should be routed to base OPF rather than this checkpoint.
- Phone-detection exact rate drops on bare phones with no telephone-related framing, with a measurable train-seen vs held-out gap in that one bucket only — see the Memorization Audit section above for the full disclosure.

## Privacy and Provenance Notes

This model was trained with synthetic PII and allowed curated source values for names, phones, and license plates. The generator uses independent entity sampling and split controls to avoid preserving real customer pairings. See `memorization_audit.md` for the aggregate audit.

## Suggested Runtime Safeguards

- Keep deterministic regex/rule-based filters for high-confidence structured identifiers.
- Add post-filters for known false positives:
  - order IDs like `ORD-\d+`;
  - dates and DOB-like strings;
  - URLs and URL query parameters;
  - organization prefixes such as `ООО`, `АО`, `ПАО` before company names;
  - truncated phone/INN/passport/card values.
- Route English-only prompts to base OPF.
- Pair Russian name/address handling with `pymorphy3` where possible; morphology-aware preprocessing and post-processing improves behavior on inflected names, patronymics, initials, and Russian address phrasing.
- Log aggregate error buckets during deployment; do not log raw PII values.

## License

Apache License 2.0. This checkpoint is a fine-tune of the [OpenAI Privacy Filter](https://github.com/openai/privacy-filter) base weights and inherits the upstream Apache 2.0 license. See `LICENSE` for the full text and `NOTICE` for attribution.

## Citation

If you use this checkpoint, cite it as:

```text
traciora-opf-ru-pii-v6: Russian/RU-identifier fine-tuned OpenAI Privacy Filter checkpoint, 2026.
```
