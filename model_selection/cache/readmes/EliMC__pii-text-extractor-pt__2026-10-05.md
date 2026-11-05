---
license: mit
datasets:
- EliMC/esic-ner
language:
- pt
metrics:
- f1
- recall
- precision
- accuracy
base_model:
- neuralmind/bert-base-portuguese-cased
pipeline_tag: token-classification
library_name: transformers
tags:
- legal
- lgpd
- e-sic
---

**Modelo de classificação de tokens para a tarefa reconhecimento de entidade nomeada (NER), treinado no domínio de solicitações a plataformas de e-sic de governo.**


## Estatísticas de avaliação no dataset de teste (EliMC/esic-ner, split=test):

### Apenas PII (exclui ORG_JURIDICA e DOC_EMPRESA)

#### Documento (binário) — positivo = contém PII

| referência \ modelo | predisse PII | predisse sem PII |
| :--- | ---: | ---: |
| contém PII | 512 | 11 |
| não contém PII | 13 | 439 |

| métrica | valor |
| :--- | ---: |
| precisão | 0.9752 (97.52%) |
| revocação (recall) | 0.9790 (97.90%) |
| F1 (P1) | 0.9771 (97.71%) |
| acurácia | 0.9754 (97.54%) |

### Qualquer entidade (inclui ORG_JURIDICA e DOC_EMPRESA)

#### Documento (binário) — positivo = contém qualquer entidade

| referência \ modelo | predisse entidade | predisse sem entidade |
| :--- | ---: | ---: |
| contém entidade | 698 | 19 |
| não contém entidade | 21 | 237 |

| métrica | valor |
| :--- | ---: |
| precisão | 0.9708 (97.08%) |
| revocação (recall) | 0.9735 (97.35%) |
| F1 | 0.9721 (97.21%) |
| acurácia | 0.9590 (95.90%) |

## Erros

| categoria | quantidade |
| :--- | ---: |
| erro binário no documento (falso pos. + falso neg.) | 24 |
| falsos positivos (documento) | 13 |
| falsos negativos (documento) | 11 |