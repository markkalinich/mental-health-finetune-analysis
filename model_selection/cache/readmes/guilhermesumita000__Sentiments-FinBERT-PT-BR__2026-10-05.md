---
language:
- pt
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
- finbert
- sentiment-analysis
- financial
- portuguese
- bert
- finance
datasets:
- lucas-leme/Sentiments-FinBERT-PT-BR
widget:
- text: O mercado financeiro registrou alta expressiva nesta segunda-feira.
- text: As ações da empresa despencaram após o anúncio de prejuízo.
- text: O Banco Central manteve a taxa de juros inalterada.
base_model:
- lucas-leme/FinBERT-PT-BR
---
# Sentiments-FinBERT-PT-BR

Modelo de linguagem para **análise de sentimentos de textos em português do mercado financeiro**, treinado com base no paper [FinBERT-PT-BR: Sentiment Analysis of Texts in Portuguese from the Financial Market](https://sol.sbc.org.br/index.php/bwaif/article/view/24960) e no [dataset](https://huggingface.co/datasets/lucas-leme/Sentiments-FinBERT-PT-BR) disponibilizado pelos autores.

O modelo classifica textos financeiros em três categorias de sentimento: **positivo**, **negativo** e **neutro**.

## Descrição do modelo

Trata-se de um modelo baseado na arquitetura BERT, ajustado (*fine-tuned*) para o domínio financeiro em língua portuguesa. Ele é capaz de interpretar notícias, relatórios, comentários de analistas e outros textos do mercado financeiro brasileiro, atribuindo a cada um deles uma polaridade de sentimento.

- **Idioma:** Português (PT-BR)
- **Tarefa:** Classificação de texto (análise de sentimentos)
- **Arquitetura base:** BERT
- **Classes:** Positivo, Negativo, Neutro
- **Domínio:** Mercado financeiro

## Como usar

### Com `pipeline`

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="seu-usuario/Sentiments-FinBERT-PT-BR"
)

resultado = classifier("As ações da empresa subiram após o balanço positivo.")
print(resultado)
```

### Com `AutoModel`

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("seu-usuario/Sentiments-FinBERT-PT-BR")
model = AutoModelForSequenceClassification.from_pretrained("seu-usuario/Sentiments-FinBERT-PT-BR")

texto = "O lucro líquido da companhia caiu 30% no trimestre."
inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    logits = model(**inputs).logits

predicao = torch.argmax(logits, dim=-1).item()
print(model.config.id2label[predicao])
```

## Casos de uso

- Monitoramento de sentimento em notícias financeiras
- Análise de relatórios e comunicados ao mercado
- Apoio a estratégias de investimento baseadas em sentimento (*sentiment-based trading*)
- Pesquisa acadêmica em finanças e PLN

## Limitações e vieses

O modelo foi treinado especificamente com textos do mercado financeiro brasileiro e pode apresentar desempenho reduzido em outros domínios ou variantes do português. Como qualquer modelo treinado a partir de dados reais, pode reproduzir vieses presentes no conjunto de dados original. Recomenda-se validação humana em aplicações críticas ou de tomada de decisão financeira.

## Dataset

O modelo foi treinado com o dataset [Sentiments-FinBERT-PT-BR](https://huggingface.co/datasets/lucas-leme/Sentiments-FinBERT-PT-BR), disponibilizado pelos autores do paper original.

## Referência

Caso utilize este modelo, por favor cite o trabalho original:

> SANTOS, Lucas L.; BIANCHI, Reinaldo A. C.; COSTA, Anna H. R. **FinBERT-PT-BR: Análise de Sentimentos de Textos em Português do Mercado Financeiro**. Anais do II Brazilian Workshop on Artificial Intelligence in Finance, 2023, p. 144–155.

```bibtex
@inproceedings{santos2023finbertptbr,
  title={FinBERT-PT-BR: An{\'a}lise de Sentimentos de Textos em Portugu{\^e}s do Mercado Financeiro},
  author={Santos, Lucas L. and Bianchi, Reinaldo A. C. and Costa, Anna H. R.},
  booktitle={Anais do II Brazilian Workshop on Artificial Intelligence in Finance},
  pages={144--155},
  year={2023}
}
```

## Licença

Este modelo é distribuído sob a licença Apache 2.0. Ajuste conforme a licença aplicável ao seu uso.