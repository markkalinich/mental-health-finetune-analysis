---
tags:
- gliner
- ner
- medical
- french
language:
- fr
---
# BRIGHT NER: GLiNER2 fine-tuned for symptoms_evolution

## Description
This is a GLiNER2 architecture fine-tuned to extract clinical neuro-oncology entities related to the `symptoms_evolution` semantic group. It was trained on a synthetic dataset generated for the properly de-identified BRIGHT project dataset (see the `generated_data` folder in the primary repository).

This model repository was specifically designed to fit within the `bright_db` overarching namespace.

## Fields
It extracts the following fields (described in French):
- **epilepsie_1er_symptome**: Crises comme premier symptôme
- **ceph_hic_1er_symptome**: Céphalées/HIC comme premier symptôme
- **ceph_hic**: Mention céphalées/HIC
- **deficit_1er_symptome**: Déficit neurologique initial
- **deficit**: Mention déficit neurologique
- **cognitif_1er_symptome**: Troubles cognitifs comme premier symptôme
- **cognitif**: Mention troubles cognitifs
- **autre_trouble_1er_symptome**: Autres premiers symptômes
- **contraste_1er_symptome**: Prise de contraste sur première imagerie
- **prise_de_contraste**: Mention générale prise de contraste
- **oedeme_1er_symptome**: Présence œdème sur première imagerie
- **calcif_1er_symptome**: Présence calcification sur première imagerie
- **epilepsie**: Mention épilepsie/crises
- **autre_trouble**: Autres symptômes actuels
- **evol_clinique**: Évolution globale (stable, progression)
- **progress_clinique**: Aggravation symptômes
- **progress_radiologique**: Croissance tumorale imagerie
- **reponse_radiologique**: Réponse tumorale imagerie

## Performance on Validation Set
**Aggregates**:
- Macro F1: 0.1530 (Precision: 0.1166, Recall: 0.4584)
- Micro F1: 0.1969 (Precision: 0.1104, Recall: 0.9105)

**Per-Label Breakdowns**:
| Label | Precision | Recall | F1 |
|---|---|---|---|
| epilepsie_1er_symptome | 0.0099 | 0.5000 | 0.0194 |
| ceph_hic_1er_symptome | 0.0100 | 1.0000 | 0.0198 |
| ceph_hic | 0.0000 | 0.0000 | 0.0000 |
| deficit_1er_symptome | 0.0000 | 0.0000 | 0.0000 |
| deficit | 0.0000 | 0.0000 | 0.0000 |
| cognitif_1er_symptome | 0.0000 | 0.0000 | 0.0000 |
| cognitif | 0.0000 | 0.0000 | 0.0000 |
| autre_trouble_1er_symptome | 0.5429 | 0.8261 | 0.6552 |
| contraste_1er_symptome | 0.0500 | 1.0000 | 0.0952 |
| prise_de_contraste | 0.2100 | 1.0000 | 0.3471 |
| oedeme_1er_symptome | 0.2115 | 0.9565 | 0.3465 |
| calcif_1er_symptome | 0.0000 | 0.0000 | 0.0000 |
| epilepsie | 0.0800 | 1.0000 | 0.1481 |
| autre_trouble | 0.1154 | 1.0000 | 0.2069 |
| evol_clinique | 0.8692 | 0.9688 | 0.9163 |
| progress_clinique | 0.0000 | 0.0000 | 0.0000 |
| progress_radiologique | 0.0000 | 0.0000 | 0.0000 |
| reponse_radiologique | 0.0000 | 0.0000 | 0.0000 |

## Usage

```python
# Inference Code
from gliner2 import GLiNER2

model = GLiNER2.from_pretrained("raphael-r/bright-gliner-symptoms_evolution")
text = "Patient presenting with epileptic seizures..."
entities = model.extract_entities(text)

for entity in entities:
    print(entity["text"], "=>", entity["label"])
```