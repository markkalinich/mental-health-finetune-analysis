---
datasets:
- BCCard/pii-masking-openpii-finance
language:
- ko
base_model:
- skt/A.X-Encoder-base
---
# ko-pii-detector-ax-crf

Korean PII (Personally Identifiable Information) span detector — CRF tagging head on top of `skt/A.X-Encoder-base`. Requires `trust_remote_code=True` (custom `ModernBertCRFTagger` architecture) and [pyt-crf](https://github.com/id4thomas/pyt-crf) package.

- Github: [id4thomas/ko-pii-detector](https://github.com/id4thomas/ko-pii-detector)
- pyt-crf package: [id4thomas/pyt-crf](https://github.com/id4thomas/pyt-crf)

```
pip install pyt-crf
```

## Performance

Entity-level (exact span match) on held-out test set (14,294 examples):

| metric | precision | recall | f1 |
| --- | --- | --- | --- |
| micro avg | 0.9702 | 0.9795 | **0.9748** |
| macro avg | 0.9713 | 0.9765 | 0.9738 |

Per label (f1, entity-level exact match):

| label | f1 | label | f1 |
| --- | --- | --- | --- |
| IPIN | 1.0000 | PASSPORT | 0.9769 |
| EMAIL | 0.9988 | ADDRESS | 0.9746 |
| DATE | 0.9967 | SECRET | 0.9738 |
| CARD_NUMBER | 0.9957 | FRN | 0.9711 |
| CARD_EXPIRY | 0.9938 | USER_ID | 0.9703 |
| ACCOUNT_NUMBER | 0.9931 | PHONE | 0.9484 |
| ZIPCODE | 0.9908 | GENERIC_ID | 0.9269 |
| CVC | 0.9906 | DRIVER_LICENSE | 0.8566 |
| RRN | 0.9882 | | |
| PERSON | 0.9831 | | |

`DRIVER_LICENSE`/`GENERIC_ID` are the weakest labels (high format variance, no fixed pattern to key on). This CRF head consistently outperforms the token-classification variant ([id4thomas/ko-pii-detector-ax-tokenclf](https://huggingface.co/id4thomas/ko-pii-detector-ax-tokenclf)) across labels, likely from the transition constraints stabilizing span boundaries.

Full precision/recall per label, head-to-head comparison: [ko-pii-detector docs/performance.md](https://github.com/id4thomas/ko-pii-detector/blob/main/docs/performance.md)

## Dataset

Trained on [`BCCard/pii-masking-openpii-finance`](https://huggingface.co/datasets/BCCard/pii-masking-openpii-finance) with additional noise injection (typos, spacing/format variants, obfuscation, partial-value references, distractor IDs, etc. — see [docs/noise.md](https://github.com/id4thomas/ko-pii-detector/blob/main/docs/noise.md)) to make the model robust to real-world noisy input.

18 span labels:

| label | description |
| --- | --- |
| PERSON | full name |
| RRN | resident registration number (Korea) |
| FRN | foreign registration number |
| CARD_NUMBER | credit/debit card PAN |
| ACCOUNT_NUMBER | bank account number |
| SECRET | auth secret (password / API key / token) |
| USER_ID | online member ID |
| EMAIL | email address |
| PHONE | phone number (mobile / landline) |
| PASSPORT | passport number |
| DRIVER_LICENSE | driver's license number |
| GENERIC_ID | generic identifier (no KO counterpart) |
| ADDRESS | address (city / street / building) |
| ZIPCODE | postal code |
| DATE | date / time |
| CARD_EXPIRY | card expiry date |
| CVC | card verification code |
| IPIN | I-PIN number |

## Usage Example

```python
import torch
from transformers import AutoModel, AutoTokenizer

# Load tokenizer, model (custom architecture -> trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("id4thomas/ko-pii-detector-ax-crf", use_fast=True, trust_remote_code=True)
model = AutoModel.from_pretrained("id4thomas/ko-pii-detector-ax-crf", trust_remote_code=True)
model.eval()

id2label = model.config.id2label

# predict
text = "문의사항은 010-1234-5678 또는 hong@example.com 으로 연락 주세요."
enc = tokenizer(text, return_tensors="pt", return_offsets_mapping=True)
offsets = enc.pop("offset_mapping")[0].tolist()

with torch.no_grad():
    pred_ids = model(**enc, decode=True).predictions[0].tolist()  # CRF-decoded tag ids

# merge BIO-tagged tokens into entity spans
entities, cur = [], None
for pred_id, (start, end) in zip(pred_ids, offsets):
    if start == end:
        continue
    tag = id2label.get(pred_id, "O")
    if tag == "O":
        cur = None
        continue
    prefix, _, label = tag.partition("-")
    if prefix == "B" or cur is None or cur["label"] != label:
        cur = {"label": label, "start": start, "end": end}
        entities.append(cur)
    else:
        cur["end"] = end

for ent in entities:
    ent["value"] = text[ent["start"]:ent["end"]]
    print(ent)
# {'label': 'PHONE', 'start': 6, 'end': 19, 'value': '010-1234-5678'}
# {'label': 'EMAIL', 'start': 23, 'end': 39, 'value': 'hong@example.com'}
```

### More Examples (per label)

One example per label from dataset's held-out `validataion`

| label | text | predicted entities |
| --- | --- | --- |
| PERSON | 중고차 할부 금리 인하 요구권 신청 - 신청인 서은우, 면허번호 64-23-318617-41, 사유 신용등급 상승. | PERSON: 서은우 · DRIVER_LICENSE: 64-23-318617-41 |
| RRN | 가족 합산 실적 등록 요청: 본인 670827-1922483, 배우자 930826-6089963, 합산 기준일 2023년 6월 18일, 합산 실적 3,400,000원. | RRN: 670827-1922483 · FRN: 930826-6089963 · DATE: 2023년 6월 18일 |
| FRN | 이체 한도 상향 심사에 신분 확인이 추가로 필요합니다. 외국인등록번호 000609-8628264와 재직증명서를 앱으로 제출해 주세요. 심사번호 RV-2210. | FRN: 000609-8628264 |
| CARD_NUMBER | 추가 서류로는 1993HP@tutanota.com으로 전송된 AX8F9I3KEY와 GMHFUPB2OC 사본이 필요하며, 이를 제공하지 않을 경우 세액공제 금액이 2200047020154130만큼 감소할 수 있습니다. | EMAIL: 1993HP@tutanota.com · GENERIC_ID: AX8F9I3KEY · DRIVER_LICENSE: GMHFUPB2OC · CARD_NUMBER: 2200047020154130 |
| ACCOUNT_NUMBER | 자녀 학원비 자동이체를 걸려고 합니다. 출금 계좌 247-23-769052, 매월 5일, 금액 420,000원. | ACCOUNT_NUMBER: 247-23-769052 |
| SECRET | 모바일 OTP 재등록 중입니다. 계정 pzmmgtx, 임시 비밀번호 QJ#qhsLRko70, 오류 코드 AU-77. | USER_ID: pzmmgtx · SECRET: QJ#qhsLRko70 |
| USER_ID | 연금 조회 서비스 가입 확인 메일입니다. 아이디 mbllxmb.4, 초기 비밀번호 dZq70t2fmd0H, 가입일 2059-07-07. | USER_ID: mbllxmb.4 · SECRET: dZq70t2fmd0H · DATE: 2059-07-07 |
| EMAIL | yang Moheb 님께, 귀하의 후보자 벤치마킹 점수는 0 점이며, 상세 내용은 문세연@gmail.com 로 송부드리겠습니다. | PERSON: Moheb · EMAIL: 문세연@gmail.com |
| PHONE | 향미 연자 님, ... 담당자 연락처: (88).0410.3736 ... 승인자: 라나 부자도 | PERSON: 향미 연자 · PHONE: (88).0410.3736 · PERSON: 라나 부자도 |
| PASSPORT | 선박 승무원 급여 계좌 개설 서류 - 승무원 김영철, 여권번호 F818J7636, 승선 계약서 사본, 개설 지점 항만점. | PERSON: 김영철 · PASSPORT: F818J7636 |
| DRIVER_LICENSE | 신청서는 기@hotmail.com 로 보내시고, 필요 서류로는 VHIO4UYEIC 과 1VHIE1OCT3이 포함됩니다. | EMAIL: 기@hotmail.com · GENERIC_ID: VHIO4UYEIC · DRIVER_LICENSE: 1VHIE1OCT3 |
| GENERIC_ID | 미청구 보험금 안내문: 계약 식별번호 FC9XLY8KJ5 기준 미청구 실손 보험금 127,400원이 확인됩니다. 앱에서 청구하세요. | GENERIC_ID: FC9XLY8KJ5 |
| ADDRESS | 배송 오류 보상 안내: 오배송지 제주도 해남군 노형동 519-32 개나리아파트 121동 1364호 (우편번호 04362)로 발송된 카드가 회수되었으며, ... | ADDRESS: 제주도 해남군 노형동 519-32 개나리아파트 121동 1364호 · ZIPCODE: 04362 |
| ZIPCODE | 신규 신청 양식에는 거주 주소가 필요합니다. 예: 사평로 50 번지, 30140 우편번호, 대전광역시 월평1동 월평1동 시. | ADDRESS: 사평로 50 · ZIPCODE: 30140 · ADDRESS: 대전광역시 월평1동 월평1동 |
| DATE | 안녕하세요 군 림님, ... 날짜: 25/12/1998, 장소: 40th Division Road 482, 연락처: 003-556 3130. | PERSON: 림 · PERSON: 은채 · DATE: 25/12/1998 · ADDRESS: 40th Division Road 482 · PHONE: 003-556 3130 |
| CARD_EXPIRY | 멤버십 자동 갱신을 해지해 주세요. 등록 카드는 4395952462642202이고 유효기간 05/30, CVC 461까지 확인해 드렸습니다. | CARD_NUMBER: 4395952462642202 · CARD_EXPIRY: 05/30 · CVC: 461 |
| CVC | 긴급 정지 요청! 방금 피싱 사이트에 카드번호 5126587179360798와 유효기간 03/26, CVC 704까지 입력해 버렸습니다. | CARD_NUMBER: 5126587179360798 · CARD_EXPIRY: 03/26 · CVC: 704 |
| IPIN | 구인 사이트 이력서 공개 설정 변경은 아이핀 2938510213123 재인증 후 가능합니다. | IPIN: 2938510213123 |
