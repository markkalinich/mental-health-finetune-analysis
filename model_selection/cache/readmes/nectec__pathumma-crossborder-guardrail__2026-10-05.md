---
base_model: iapp/OpenThai-SystemOne
language:
- th
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-classification
tags:
- guardrail
- data-sovereignty
- pdpa
- data-classification
- thai
- system-one
- decision-model
model-index:
- name: pathumma-crossborder-guardrail
  results:
  - task:
      type: text-classification
      name: Cross-border data-sensitivity (7-way)
    dataset:
      name: Template-held-out test set
      type: synthetic
    metrics:
    - type: accuracy
      value: 0.9284
      name: Accuracy
    - type: f1
      value: 0.9267
      name: Macro-F1
---

# Pathumma Cross-border Guardrail (OpenThai-SystemOne fine-tune)

โมเดลตัดสินใจ (decision model) ~0.8B สำหรับใช้เป็น **guardrail ชั้นแรก** ก่อน route prompt ไปยัง LLM: จำแนกว่าข้อความมี *ข้อมูลประเภทใด* (7 หมวด) แล้ว map เป็น *สิทธิ์ส่งประมวลผลนอกประเทศ* (3 ระดับ) ตาม PDPA และ ETDA Generative AI Governance Guideline
ไม่ใช่โมเดล generative — คืน calibrated probability เหนือ option ที่กำหนด ใน forward pass เดียว

## Intended use
ใช้ตัดสิน routing (foreign API vs sovereign/on-prem) เป็นชั้นแรกร่วมกับ regex/DLP pre-filter สำหรับข้อความไทย/อังกฤษในบริบทองค์กรไทย
**ไม่ได้** ออกแบบมาตรวจเนื้อหาอันตราย (violence, CSAM, hate) — ต้องมี content-safety guardrail แยก

## Taxonomy
| # | key | คำอธิบาย | routing |
|---|---|---|---|
| 1 | `public` | ความรู้ทั่วไป งานเขียน โค้ด หรือคำถามเชิงแนวคิด ที่ไม่มีชื่อ… | `foreign_ok` |
| 2 | `pdpa_general` | มีข้อมูลระบุตัวบุคคลจริง เช่น ชื่อ-สกุล เบอร์โทร อีเมล ที่อย… | `conditional` |
| 3 | `pdpa_sensitive` | มีข้อมูลบุคคลจริงประเภทอ่อนไหว: สุขภาพ/โรค/ผลตรวจ พันธุกรรม … | `sovereign_only` |
| 4 | `confidential` | เอกสารบริหาร/การเงิน/กฎหมายภายในของบริษัทเอกชน ที่ยังไม่เปิด… | `sovereign_only` |
| 5 | `system_secret` | มี credential หรือรายละเอียดเทคนิคของระบบ: API key รหัสผ่าน … | `sovereign_only` |
| 6 | `govt_classified` | เอกสารของหน่วยงานรัฐ/ทหาร/ตำรวจ/ข่าวกรอง ที่มีชั้นความลับ (ล… | `sovereign_only` |
| 7 | `trade_secret` | ทรัพย์สินทางปัญญาเชิงเทคนิค/วิจัย ที่ยังไม่เปิดเผย: สูตรการผ… | `conditional` |

`conditional` = ส่งได้เฉพาะผู้ให้บริการที่มี SCC/BCR/Enterprise DPA พร้อมข้อ no-train หรือมีความยินยอม · `sovereign_only` = ประมวลผลในประเทศเท่านั้น

## How to use
โมเดลถูก fine-tune กับ instructions + criteria ชุดเดียว ซึ่งเก็บใน [`guardrail_config.json`](./guardrail_config.json)  

```python
import json
from openthai_systemone import SystemOneClient, Choice
from huggingface_hub import hf_hub_download
cfg = json.load(open(hf_hub_download("nectec/pathumma-crossborder-guardrail", "guardrail_config.json")))
client = SystemOneClient("nectec/pathumma-crossborder-guardrail")
resp = client.system_one(state={"prompt": "ช่วยสรุปผลตรวจสุขภาพของ นายสมชาย ใจดี HN 123456"},
                         questions={"data_sensitivity": Choice(instructions=cfg["instructions"], criteria=cfg["criteria"])})
a = resp.answers["data_sensitivity"]
print(a.choice, cfg["routing"][a.choice], round(a.confidence, 3))
```
Wrapper พร้อม pre-filter/fail-closed: [`guardrail.py`](./guardrail.py) · FastAPI + OpenAI-compatible `/v1/moderations`: [`serve.py`](./serve.py)

## Training
- Base: [`iapp/OpenThai-SystemOne`](https://huggingface.co/iapp/OpenThai-SystemOne) · full fine-tune backbone + slot head ด้วย loss ที่มากับโมเดล (CE + label_smoothing 0.05 + brier 0.1), shuffle ลำดับ option ทุก batch, temperature calibrate แยกบน held-out val
- AdamW lr backbone 1e-05 / head 0.0001, batch 8, ≤4 epochs + early stopping (best epoch n/a), bf16 autocast
- Data: synthetic 3,500 ตัวอย่าง (500/หมวด) จาก template 20-39 แบบต่อหมวด — ชื่อ/เลขบัตร/เบอร์/องค์กร **สมมติทั้งหมด**, credential ในหมวด 5 เป็น placeholder
- Split ระดับ template 60/15/25 → val/test เป็นรูปประโยคที่ไม่เคยเห็น

## Evaluation (template-held-out test, n = 880)
| model | accuracy | macro-F1 |
|---|---|---|
| base zero-shot | 0.8557 | 0.8544 |
| **fine-tuned (this repo)** | **0.9284** | **0.9267** |

```
                 precision    recall  f1-score   support

         public      0.953     0.865     0.907       141
   pdpa_general      0.867     1.000     0.929       130
 pdpa_sensitive      1.000     0.821     0.902       112
   confidential      0.745     1.000     0.854       108
  system_secret      1.000     1.000     1.000       137
govt_classified      1.000     0.992     0.996       126
   trade_secret      1.000     0.817     0.900       126

       accuracy                          0.928       880
      macro avg      0.938     0.928     0.927       880
   weighted avg      0.941     0.928     0.929       880
```
Confusion matrix (rows=gold, cols=pred, 1..7):
```
[[122   0   0  19   0   0   0]
 [  0 130   0   0   0   0   0]
 [  0  20  92   0   0   0   0]
 [  0   0   0 108   0   0   0]
 [  0   0   0   0 137   0   0]
 [  0   0   0   1   0 125   0]
 [  6   0   0  17   0   0 103]]
```
Calibration: T = 1.068 (val NLL 0.2766 → 0.2766)

Coverage vs accuracy ตาม confidence threshold (ใช้ตั้ง `min_confidence`, ค่าเริ่มต้น 0.6):
| threshold | coverage | acc on kept |
|---|---|---|
| 0.5 | 0.993 | 0.935 |
| 0.6 | 0.989 | 0.938 |
| 0.7 | 0.981 | 0.944 |
| 0.8 | 0.975 | 0.946 |
| 0.9 | 0.951 | 0.964 |

## Limitations
- ข้อมูลฝึกเป็น synthetic จาก template — ผลบน prompt จริงอาจต่ำกว่านี้ ควร shadow-deploy และ label ข้อมูลจริงเพิ่ม
- ไม่ได้เทรนให้จำ secret จริง → ต้องมี regex/entropy pre-filter เสมอ (มีใน `guardrail.py`)
- single-label: ข้อความหลายประเภทได้หมวดเข้มงวดสุดตาม priority rule
- ไม่ครอบคลุม content safety · base model มี order sensitivity สำหรับ ≤10 options (fine-tune ด้วย shuffle ช่วยลด)
- ควร fail-closed: confidence ต่ำ/abstain สูง/error → `sovereign_only`

## Deployment
รันโมเดลนี้ on-prem/ในประเทศเสมอ · pipeline `pre-filter → model → threshold → routing` · log ทุก decision · เก็บเคส needs_review ส่ง human label แล้ว fine-tune รอบถัดไป

## Acknowledgements
Base model และ pipeline โดย [iApp Technology](https://huggingface.co/iapp) (OpenThai-SystemOne, Apache-2.0) ซึ่งได้แรงบันดาลใจจาก TypeSafe AI System One. Taxonomy อ้างอิง ETDA AI Governance Center

**Author:** Sarawoot Kongyoung, NECTEC/AINRG · **Contact:** sarawoot.kon@nectec.or.th
