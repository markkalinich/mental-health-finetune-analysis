---
language:
- pt
license: cc-by-4.0
library_name: transformers
pipeline_tag: token-classification
tags:
- ner
- token-classification
- portuguese
- medical
- clinical
- healthcare
- brazil
- openmed-br
base_model: OpenMed/OpenMed-PII-Portuguese-BioClinicalBERT-Base-110M-v1
datasets:
- MultiCoNER/multiconer_v2
metrics:
- seqeval
model-index:
- name: openmed-br-clinical-pt
  results:
  - task: {type: token-classification, name: Named Entity Recognition}
    dataset: {name: MultiCoNER v2 (Portuguese, medical held-out), type: MultiCoNER/multiconer_v2}
    metrics:
    - {type: f1, value: 0.598, name: F1 (entity-level)}
    - {type: precision, value: 0.573, name: Precision}
    - {type: recall, value: 0.625, name: Recall}
---

# 🇧🇷 OpenMed-BR Clinical NER — Efficient (PT)

> Reconhecimento de entidades clínicas em **português**, leve o bastante para rodar
> em **CPU**. Extrai **doenças, sinais/sintomas, medicamentos, procedimentos e
> estruturas anatômicas** de texto médico livre.

| | |
|---|---|
| **Tarefa** | Token classification / NER (5 tipos) |
| **Idioma** | Português (BR) |
| **Base** | [OpenMed PT — BioClinicalBERT 110M](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-BioClinicalBERT-Base-110M-v1) (Apache-2.0) |
| **Parâmetros** | 110M — roda em CPU |
| **F1 (held-out)** | **0.60** |
| **Licença** | CC BY 4.0 |
| **Irmão** | [`BrazilAI/openmed-br-large-pt`](https://huggingface.co/BrazilAI/openmed-br-large-pt) (maior F1, cross-lingual) |

---

## Por que isto importa

O Brasil gera uma quantidade imensa de texto clínico — evoluções, anamneses,
laudos, atestados — e **quase tudo fica preso em texto livre**. Mesmo com 97,6% das
UBS já usando prontuário eletrônico, o conteúdo é escrito em linguagem natural, não
estruturado. Isso trava tudo que depende de dado organizado:

- **Codificação clínica** (CID-10, CIAP-2, TUSS, SIGTAP) feita à mão, cara e lenta.
- **Glosas** no setor privado: **R$ 5,8 bilhões em 2024** (15,9% do faturado), das
  quais só ~2% eram justificadas — a maior parte é problema de documentação/código.
- **Vigilância e pesquisa** que precisam garimpar prontuário manualmente.
- **Continuidade do cuidado** perdida entre sistemas que não conversam.

O primeiro passo para destravar qualquer um desses problemas é o mesmo: **transformar
texto clínico em entidades estruturadas**. É exatamente o que este modelo faz — e faz
em português, de forma aberta e rodando em hardware modesto.

Ecossistema de referência (inglês) como o [OpenMed](https://huggingface.co/OpenMed)
não cobre NER **clínico** em português (só de-identificação de PII). O **OpenMed-BR**
preenche esse vazio.

## O que o modelo reconhece

| Entidade | Exemplos |
|---|---|
| `DOENCA` | hipertensão arterial, diabetes mellitus, pneumonia |
| `SINAL_SINTOMA` | febre, cefaleia, dor abdominal, dispneia |
| `MEDICAMENTO` | losartana, dipirona, metformina, azitromicina |
| `PROCEDIMENTO` | tomografia de tórax, hemograma, apendicectomia |
| `ANATOMIA` | tórax, abdome, ventrículo esquerdo |

## Aplicações

- **Assistente de codificação** — sugerir CID-10/CIAP-2 (doenças), TUSS/SIGTAP
  (procedimentos) e OBM/CATMAT (medicamentos) a partir da nota clínica, acelerando
  faturamento e reduzindo glosa. *(O modelo extrai a entidade; o mapeamento ao código
  é a camada seguinte.)*
- **Prevenção de glosa** — checar se procedimentos/medicamentos citados na evolução
  estão devidamente registrados na guia.
- **Estruturação de prontuário** — montar listas de problemas, medicações em uso e
  procedimentos a partir de texto livre.
- **Pesquisa e vigilância** — construir coortes e indicadores epidemiológicos a partir
  de grandes volumes de texto.
- **Pipeline de privacidade** — combinar com o modelo PII do OpenMed para anonimizar
  antes de processar (LGPD).

## Como usar

```python
from transformers import pipeline

ner = pipeline("token-classification",
               model="BrazilAI/openmed-br-clinical-pt",
               aggregation_strategy="simple")

texto = "Paciente com hipertensão em uso de losartana; solicitada tomografia de tórax."
for e in ner(texto):
    print(e["entity_group"], "->", e["word"], round(e["score"], 2))
```

Roda em CPU. Para lote, passe uma lista de textos ao `pipeline`.

## Como foi treinado

Estratégia **híbrida** para contornar a escassez de dado clínico anotado em PT:

1. **Base OpenMed** — encoder BioClinicalBERT já adaptado ao português (Apache-2.0).
2. **Dados ouro** — fatia médica do **MultiCoNER v2** em português (anotação humana).
3. **Dados prata (destilação)** — os 13 modelos clínicos `pucpr/clinicalnerpt-*`
   (treinados no corpus **SemClinBr**) atuam como *professores*, rotulando texto que
   é então usado no treino. Assim o conhecimento clínico do SemClinBr entra no modelo
   mesmo com o corpus original sendo de acesso restrito.

Tudo mapeado para um esquema clínico unificado de 5 tipos.

## Resultados (teste PT held-out, seqeval, nível de entidade)

| Tipo | F1 |
|---|---|
| ANATOMIA | 0.717 |
| MEDICAMENTO | 0.667 |
| DOENCA | 0.564 |
| PROCEDIMENTO | 0.429 |
| SINAL_SINTOMA | 0.421 |
| **Geral** | **0.598** |

**Leitura honesta:** este é um ponto de partida sólido, não o estado da arte. O teste
held-out é pequeno (77 frases) → números honestos, porém ruidosos. Para **MEDICAMENTO**
este modelo é o melhor da família (0.67). Para doença/procedimento/sintoma, o irmão
[`openmed-br-large-pt`](https://huggingface.co/BrazilAI/openmed-br-large-pt) vai melhor.

## Qual modelo escolher

| Precisa de… | Use |
|---|---|
| Rodar em **CPU**, baixo custo, foco em medicamento | **este** (`clinical-pt`) |
| Maior F1 geral (GPU), doença/procedimento/sintoma | [`openmed-br-large-pt`](https://huggingface.co/BrazilAI/openmed-br-large-pt) |

## Uso responsável (leia antes de aplicar em saúde)

- **Não é dispositivo médico.** É ferramenta assistiva de **documentação/estruturação**,
  com humano no circuito. Software não-diagnóstico de apoio administrativo/documental
  fica fora da ANVISA RDC 657/2022; assim que houver sugestão diagnóstica/terapêutica
  para um paciente, entra regulação (SaMD).
- **LGPD** — dado de saúde é sensível. Processe em contexto de tutela da saúde
  (Art. 11, II, "f") ou anonimize antes (ex.: modelo PII do OpenMed). Prefira execução
  local/on-device.
- **Revisão humana obrigatória** — não use para decisão clínica.

## Roadmap

- Ligação das entidades a **CID-10 / TUSS / SIGTAP / OBM** (da extração ao código).
- Treino/avaliação sobre **texto clínico real em PT** (ex.: acesso ao SemClinBr cru,
  parceria hospitalar) rumo ao SOTA (~0.76).
- Teste held-out maior e mais representativo.

## Atribuição e citação (obrigatória — CC BY 4.0)

- **Base**: OpenMed — `OpenMed/OpenMed-PII-Portuguese-BioClinicalBERT-Base-110M-v1` (Apache-2.0).
- **Dados ouro**: MultiCoNER v2 — Fetahu et al., *arXiv:2310.13213*; SemEval-2023 Task 2, *arXiv:2305.06586* (CC BY 4.0).
- **Dados prata (professores)**: BioBERTpt / clinicalnerpt / **SemClinBr** — Schneider et al., 2020 (ClinicalNLP@EMNLP); Oliveira et al., *J. Biomed. Semantics*, 2022; HAILab-PUCPR.

```bibtex
@misc{openmedbr_clinical_pt,
  title  = {OpenMed-BR Clinical NER (Efficient, PT)},
  author = {OpenMed-BR / BrazilAI},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/BrazilAI/openmed-br-clinical-pt}}
}
```

## Licença
CC BY 4.0 — uso livre (inclusive comercial) **com atribuição**.
