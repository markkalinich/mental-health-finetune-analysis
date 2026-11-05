---
base_model: sentence-transformers/all-MiniLM-L6-v2
library_name: sentence-transformers
tags: [sentence-transformers, uav, fault-diagnosis, synthetic-data]
datasets: [Bashifu/uav-fault-symptom-reports]
---
# UAV symptom MiniLM

`sentence-transformers/all-MiniLM-L6-v2` fine-tuned with BatchAllTripletLoss (cosine, margin 0.25, 3 epochs) on the **train flights** of
[Bashifu/uav-fault-symptom-reports](https://huggingface.co/datasets/Bashifu/uav-fault-symptom-reports) (split fingerprint `bf752fbcbe4059a8…`),
so that symptom reports of the same fault sit close together.

| Macro fault precision@3 | base | fine-tuned |
|---|---|---|
| Validation, single report (selection) | 0.719 | 0.775 |
| Test, single report | 0.765 | 0.819 |
| Test, all reports | 0.532 | 0.582 |
| Challenge split, single report | 0.572 | 0.625 |
| Handwritten descriptions | 0.488 | 0.429 |

Decision rule (fixed before training): deploy only if validation improves by at least 0.01.
**Deployed in the app: no** (see Deployment status below). (see Deployment status below). (see Deployment status below). (see Deployment status below). Synthetic data; not for real aircraft.

## Deployment status

| Gate | Result |
|---|---|
| `validation_gate_passed` (notebook 07: validation must improve by at least the pre-set gain) | **true** (+0.056) |
| `final_acceptance_gate_passed` (notebook 06 off-topic check; notebook 08 handwritten descriptions) | **false** |
| `deployed_in_final_app` | **false**: rolled back; the app uses `sentence-transformers/all-MiniLM-L6-v2` |

Fine-tuning pulled unrelated text towards the fault clusters (a washing-machine sentence scored 0.64), so the
off-topic floor had to rise to 0.691 and rejected 6 of 10 plain UAV descriptions; 25 of 28 handwritten
descriptions were rejected. The model stays published as an experiment.
