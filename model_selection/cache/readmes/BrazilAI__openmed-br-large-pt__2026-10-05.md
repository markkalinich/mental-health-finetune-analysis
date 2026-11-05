---
language:
- pt
- es
license: cc-by-4.0
library_name: transformers
pipeline_tag: token-classification
tags:
- ner
- token-classification
- portuguese
- spanish
- medical
- clinical
- healthcare
- brazil
- cross-lingual
- openmed-br
base_model: xlm-roberta-base
datasets:
- MultiCoNER/multiconer_v2
- IEETA/SPACCC-Spanish-NER
metrics:
- seqeval
model-index:
- name: openmed-br-large-pt
  results:
  - task: {type: token-classification, name: Named Entity Recognition}
    dataset: {name: MultiCoNER v2 (Portuguese, medical held-out), type: MultiCoNER/multiconer_v2}
    metrics:
    - {type: f1, value: 0.674, name: F1 (entity-level)}
    - {type: precision, value: 0.636, name: Precision}
    - {type: recall, value: 0.716, name: Recall}
---

# 🇧🇷 OpenMed-BR Clinical NER — Large (PT · cross-lingual PT+ES)

> Reconhecimento de entidades clínicas em **português**, reforçado com corpora
> clínicos ouro em **espanhol** (transferência cross-lingual). É o modelo de **maior
> F1** da família OpenMed-BR. Extrai **doenças, sinais/sintomas, medicamentos,
> procedimentos e estruturas anatômicas**.

| | |
|---|---|
| **Tarefa** | Token classification / NER (5 tipos) |
| **Idioma** | Português (BR), com treino cross-lingual PT+ES |
| **Base** | [`xlm-roberta-base`](https://huggingface.co/xlm-roberta-base) (MIT, multilíngue) |
| **F1 (held-out PT)** | **0.674** |
| **Licença** | CC BY 4.0 |
| **Irmão** | [`BrazilAI/openmed-br-clinical-pt`](https://huggingface.co/BrazilAI/openmed-br-clinical-pt) (roda em CPU; melhor em medicamento) |

---

## Por que isto importa

O Brasil produz um volume enorme de texto clínico — evoluções, anamneses, laudos —
e **quase tudo fica em texto livre**. Mesmo com 97,6% das UBS em prontuário eletrônico,
o conteúdo não é estruturado. Isso trava codificação, faturamento, pesquisa e
continuidade do cuidado. No setor privado, **glosas somaram R$ 5,8 bi em 2024**
(15,9% do faturado, só ~2% justificadas) — em grande parte, problema de documentação.

O primeiro passo para atacar qualquer um desses problemas é **transformar texto
clínico em entidades estruturadas**. Recursos de referência em inglês (ex.:
[OpenMed](https://huggingface.co/OpenMed)) não cobrem NER **clínico** em português —
o **OpenMed-BR** existe para preencher esse vazio, de forma aberta.

Este modelo **Large** usa uma ideia-chave: como corpus clínico ouro em português é
escasso, ele importa conhecimento de **corpora clínicos espanhóis** (grandes e
abertos) via um encoder multilíngue. Português e espanhol são próximos, e a
transferência cross-lingual eleva bastante o desempenho.

## O que o modelo reconhece

| Entidade | Exemplos |
|---|---|
| `DOENCA` | pneumonia, diabetes mellitus, insuficiência cardíaca |
| `SINAL_SINTOMA` | febre, dor abdominal, dispneia, obnubilação |
| `MEDICAMENTO` | azitromicina, metformina, omeprazol |
| `PROCEDIMENTO` | tomografia de tórax, colonoscopia, hemograma |
| `ANATOMIA` | tórax, abdome, antebraço |

## Aplicações

- **Assistente de codificação** — sugerir CID-10/CIAP-2, TUSS/SIGTAP e OBM/CATMAT a
  partir da nota clínica (o modelo extrai a entidade; o mapeamento ao código é a
  camada seguinte), acelerando faturamento e reduzindo glosa.
- **Prevenção de glosa** — conferir se o que está na evolução foi registrado na guia.
- **Estruturação de prontuário** — listas de problemas, medicações e procedimentos.
- **Pesquisa e vigilância** — coortes e indicadores a partir de texto em escala.
- **Pipeline de privacidade** — combinar com o PII do OpenMed para anonimizar (LGPD).

## Como usar

```python
from transformers import pipeline

ner = pipeline("token-classification",
               model="BrazilAI/openmed-br-large-pt",
               aggregation_strategy="simple")

texto = "Paciente com pneumonia; solicitada tomografia de tórax e avaliada dor abdominal."
for e in ner(texto):
    print(e["entity_group"], "->", e["word"], round(e["score"], 2))
```

Recomenda-se **GPU** para inferência em lote (é maior que o irmão Efficient).

## Como foi treinado

1. **Base** `xlm-roberta-base` (multilíngue, tokenizer que lida bem com PT).
2. **Ouro PT** — fatia médica do **MultiCoNER v2** (anotação humana).
3. **Prata PT** — destilação dos modelos clínicos `pucpr/clinicalnerpt-*` (SemClinBr).
4. **Ouro ES (cross-lingual)** — corpora clínicos espanhóis abertos: **DisTEMIST**
   (doenças), **MedProcNER** (procedimentos), **SympTEMIST** (sintomas), projetados
   para o mesmo esquema de 5 tipos.

Avaliação sempre no **mesmo teste PT held-out**, para comparabilidade entre modelos.

## Resultados (teste PT held-out, seqeval, nível de entidade)

| Tipo | F1 | vs. Efficient |
|---|---|---|
| ANATOMIA | 0.786 | +0.07 |
| DOENCA | 0.744 | +0.18 |
| PROCEDIMENTO | 0.643 | +0.21 |
| SINAL_SINTOMA | 0.526 | +0.11 |
| MEDICAMENTO | 0.537 | −0.13 |
| **Geral** | **0.674** | **+0.08** |

**Leitura honesta:** o cross-lingual elevou muito **DOENÇA, PROCEDIMENTO e
SINAL_SINTOMA**. **MEDICAMENTO é o ponto fraco** — esta versão não inclui corpus
espanhol de fármacos (PharmaCoNER), então para medicamento o irmão
[`openmed-br-clinical-pt`](https://huggingface.co/BrazilAI/openmed-br-clinical-pt)
vai melhor (0.67). Teste held-out pequeno (77 frases) → honesto, porém ruidoso.

## Qual modelo escolher

| Precisa de… | Use |
|---|---|
| Maior F1 geral, doença/procedimento/sintoma | **este** (`large-pt`, GPU) |
| Rodar em **CPU**, baixo custo, foco em medicamento | [`openmed-br-clinical-pt`](https://huggingface.co/BrazilAI/openmed-br-clinical-pt) |

## Uso responsável (leia antes de aplicar em saúde)

- **Não é dispositivo médico.** Ferramenta assistiva de documentação/estruturação,
  com humano no circuito. Uso não-diagnóstico/administrativo fica fora da ANVISA
  RDC 657/2022; sugestão diagnóstica/terapêutica a paciente entra em regulação (SaMD).
- **LGPD** — dado de saúde é sensível: contexto de tutela da saúde (Art. 11, II, "f")
  ou anonimização prévia. Prefira execução local.
- **Revisão humana obrigatória** — não use para decisão clínica.

## Roadmap

- **PharmaCoNER** (fármacos ES) no mix → fechar o gap de MEDICAMENTO (meta: geral >0.70).
- Ligação das entidades a **CID-10 / TUSS / SIGTAP / OBM**.
- Treino/avaliação sobre **texto clínico real em PT** rumo ao SOTA (~0.76).

## Atribuição e citação (obrigatória — CC BY 4.0)

- **Base**: `xlm-roberta-base` (MIT).
- **Ouro PT**: MultiCoNER v2 — Fetahu et al., *arXiv:2310.13213*; SemEval-2023 Task 2, *arXiv:2305.06586* (CC BY 4.0).
- **Ouro ES** (CC BY 4.0): DisTEMIST (Zenodo 7614764), MedProcNER (Zenodo 8224056), SympTEMIST (Zenodo 8223653) — BioASQ/BSC.
- **Prata PT (professores)**: BioBERTpt / clinicalnerpt / **SemClinBr** — Schneider et al., 2020 (ClinicalNLP@EMNLP); Oliveira et al., *J. Biomed. Semantics*, 2022; HAILab-PUCPR.

```bibtex
@misc{openmedbr_large_pt,
  title  = {OpenMed-BR Clinical NER (Large, PT cross-lingual)},
  author = {OpenMed-BR / BrazilAI},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/BrazilAI/openmed-br-large-pt}}
}
```

## Licença
CC BY 4.0 — uso livre (inclusive comercial) **com atribuição**.
