---
language:
- pt
license: mit
tags:
- text-classification
- sentiment-analysis
- portuguese
- bert
- e-commerce
- promotional-periods
metrics:
- accuracy
- f1
base_model: neuralmind/bert-base-portuguese-cased
---

# PromoSense — Modelo de Análise de Sentimento (v3)

Modelo de classificação de sentimento em avaliações de e-commerce brasileiro, com foco em períodos promocionais (Double Dates, Black Friday).

Desenvolvido como parte do **Projeto Integrador** do curso de Tecnólogo em Análise e Desenvolvimento de Sistemas — Senac Recife.

---

## Uso

```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="Amand4priscil4/promosense-modelo",
    truncation=True,
    max_length=128
)

# Mapeamento de labels
LABEL_MAP = {
    "LABEL_0": "negativo",
    "LABEL_1": "neutro",
    "LABEL_2": "positivo"
}

texto = "Produto chegou antes do prazo, qualidade ótima, super recomendo!"
resultado = clf(texto)[0]
sentimento = LABEL_MAP[resultado["label"]]
print(f"{sentimento} ({resultado['score']:.2%})")
# positivo (98.45%)
```

---

## Modelo Base

- **Arquitetura:** BERT
- **Base:** `neuralmind/bert-base-portuguese-cased` (BERTimbau)
- **Tarefa:** Classificação de sequência (3 classes)

---

## Labels

| Label | Sentimento |
|---|---|
| LABEL_0 | negativo |
| LABEL_1 | neutro |
| LABEL_2 | positivo |

---

## Histórico dos Modelos

### Modelo v1 — rotulagem por nota
- Dataset: `olist_processado.csv` (35.246 avaliações)
- Problema crítico: nunca previa neutro — F1 neutro = 0.00
- Accuracy no ground truth v1: 83.6% (92/110)

### Modelo v2 — rotulagem híbrida (léxico 150 expressões)
- Dataset: `olist_rotulado_hibrido.csv` — neutros: 3.212
- Accuracy treino: 87.03% | F1 macro: 79.50%
- Accuracy ground truth v1: 90.00% (99/110)
- Limitação: F1 neutro = 0.03

### Modelo v3  (atual) — rotulagem híbrida (léxico 412 expressões)
- Dataset: `olist_rotulado_hibrido_v3.csv` — neutros: 5.318
- Léxico expandido de 150 para **412 expressões** (módulo `promosense-lexico`)
- Treinamento: HuggingFace Trainer, 3 épocas, batch 16, lr padrão, GPU T4, fp16

---

## Dataset de Treinamento (v3)

- **Fonte:** Olist (avaliações de e-commerce brasileiro)
- **Total de amostras:** 35.246 avaliações
- **Rotulagem:** Híbrida — nota + léxico de 412 expressões + conectivos de contraste
- **Distribuição após rotulagem híbrida v3:**

| Sentimento | Quantidade |
|---|---|
| Positivo | 19.440 |
| Negativo | 10.488 |
| Neutro | 5.318 |
| **Total** | **35.246** |

### Hiperparâmetros de Treinamento

| Parâmetro | Valor |
|---|---|
| Épocas | 3 |
| Batch size | 16 |
| fp16 | True |
| GPU | T4 (Google Colab) |
| Framework | HuggingFace Trainer |

---

## Avaliação

### Treino (Olist — conjunto de teste 20%)

| Época | Train Loss | Val Loss | Accuracy | F1 |
|---|---|---|---|---|
| 1 | 0.4263 | 0.3969 | 85.19% | 83.13% |
| 2 | 0.3026 | 0.3992 | 85.82% | 85.56% |
| 3 | 0.2429 | 0.4606 | **85.99%** | **85.65%** |

### Relatório por Classe (conjunto de teste — 7.050 amostras)

| Classe | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| negativo | 0.76 | 0.94 | 0.84 | 2.098 |
| neutro | 0.76 | 0.29 | **0.42** | 1.064 |
| positivo | 0.92 | 0.95 | 0.94 | 3.888 |
| macro avg | 0.81 | 0.73 | 0.73 | 7.050 |
| weighted avg | 0.85 | 0.85 | 0.83 | 7.050 |

### Matriz de Confusão (conjunto de teste)

|  | Pred. negativo | Pred. neutro | Pred. positivo |
|---|---|---|---|
| **Real negativo** | 1.982 | 49 | 67 |
| **Real neutro** | 485 | 312 | 267 |
| **Real positivo** | 127 | 49 | 3.712 |

### Ground Truth Manual (Shopee)

| Ground Truth | Amostras | Accuracy |
|---|---|---|
| GT v1 — JBL Boombox 4, E6S TWS | 110 | 90.00% (99/110) |
| GT v2 — PS4, E6S, JBL, Cozedor, Fone | 165 | 59.39% (98/165) |
| **Combinado** | **275** | **71.64%** (197/275) |

---

## Comparativo entre Versões

| Métrica | v1 | v2 | v3 |
|---|---|---|---|
| Expressões no léxico | — | 150 | **412** |
| Neutros no treino | 3.212 | 3.212 | **5.318** |
| Accuracy treino | — | 87.03% | 85.99% |
| F1 macro treino | — | 79.50% | **85.65%** |
| F1 neutro | 0.00 | 0.03 | **0.42** |
| Accuracy GT v1 | 83.6% | 90.0% | — |

---

## ABSA — Análise de Sentimento por Aspecto

Além da classificação geral, o PromoSense implementa ABSA híbrida: léxico de 412 expressões para detecção de sentimento + BERTimbau como fallback + léxico de palavras-chave para detecção de aspecto.

### Métricas ABSA (418 avaliações do ground truth)

| Métrica | Valor |
|---|---|
| Accuracy ABSA completa (aspecto + sentimento) | 53.8% (225/418) |
| Accuracy sentimento geral | 69.1% (289/418) |
| Accuracy detecção de aspecto | 74.2% (310/418) |

#### Por aspecto

| Aspecto | Accuracy sentimento | Amostras |
|---|---|---|
| Preço | 84.1% | 44 |
| Entrega | 64.5% | 76 |
| Qualidade | 68.1% | 298 |

---

## Limitações Conhecidas

- **Neutro ainda subclassificado:** F1 = 0.42 no treino — melhora significativa em relação ao v2 (0.03), mas ainda há espaço para evolução.
- **Avaliações mistas:** Textos que combinam elogios e críticas tendem a ser classificados como positivo ou negativo, raramente neutro.
- **Entrega com precision baixa (0.44):** Palavras como "chegou" e "embalado" aparecem em textos de outros aspectos na ABSA.

---

## Trabalho Futuro

- Melhorar F1 de neutro (meta: > 0.50)
- Expandir léxico com expressões de gírias e neologismos
- Melhorar detecção de aspecto "entrega" no léxico ABSA
- Integrar resultados ABSA ao MongoDB + dashboard

---

## Léxico

O léxico utilizado neste modelo está disponível como módulo Python independente:

 **[kellvyno/promosense-lexico](https://github.com/kellvyno/promosense-lexico)**

```bash
pip install git+https://github.com/kellvyno/promosense-lexico.git
```

---

## Equipe

| Membro | Papel |
|---|---|
| Amanda | QA, anotação, modelagem, testes |
| Lucas | Backend (FastAPI) e Frontend (dashboard) |
| Kellvyn | Léxico (`promosense-lexico`) |

---

## Repositório

 **[amand4priscil4/PROMOSENSE](https://github.com/amand4priscil4/PROMOSENSE)**

---

## Citação

```
@misc{promosense2026,
  title={PromoSense: Análise de Sentimento em Avaliações de E-commerce Brasileiro em Períodos Promocionais},
  author={Amanda and Lucas and Kellvyn},
  year={2026},
  institution={Senac Recife — Tecnólogo em Análise e Desenvolvimento de Sistemas}
}
```