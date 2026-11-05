---
license: mit
language: multilingual
tags:
  - sentiment-analysis
  - BERT
  - multilingual
  - customer-feedback
  - churn-risk
  - fine-tuned-model
  - feedback-analysis
  - vinicius-khan
base_model: nlptown/bert-base-multilingual-uncased-sentiment
pipeline_tag: text-classification
---

# 🧠 Senticore: BERT Multilingual Sentiment Model

**Senticore-BERT-Sentiment** é um modelo de *fine-tuning* baseado no `bert-base-multilingual-uncased`, treinado para **análise de sentimentos multilíngue**, com ênfase especial em **feedbacks de clientes corporativos**, visando identificar **nível de satisfação e risco de cancelamento (churn)**.

---

## 🔍 Aplicações

- Classificação de sentimentos em **feedbacks textuais** de clientes.
- Detecção automática de **clientes insatisfeitos ou detratores**.
- Análise semântica de **resumos de chamados técnicos**, NPS e pesquisas de relacionamento.
- Sistemas de recomendação para **priorização de atendimento e mitigação de churn**.
- Dashboards inteligentes e monitoramento de sentimentos ao longo do tempo.

---

## 📁 Estrutura do Modelo

A pasta `bert-multilingual-sentiment/` contém:

- `config.json`
- `pytorch_model.bin` ou `model.safetensors`
- `tokenizer_config.json`
- `vocab.txt`
- `special_tokens_map.json`

---

## 🧪 Como Utilizar em Python

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ViniciusKhan/senticore-bert-sentiment",
    tokenizer="ViniciusKhan/senticore-bert-sentiment"
)

texto = "Estou extremamente insatisfeito com o serviço."
resultado = classifier(texto)
print(resultado)
```

---

## 🏷️ Labels Retornados

O modelo classifica os textos em três categorias:

- `LABEL_0`: Sentimento **Negativo**
- `LABEL_1`: Sentimento **Neutro**
- `LABEL_2`: Sentimento **Positivo**

---

## 📊 Dados de Treinamento

O modelo foi treinado com um conjunto balanceado de textos reais rotulados por especialistas, abrangendo:

- Clientes **Promotores** (`Positivo`)
- Clientes **Neutros**
- Clientes **Detratores** (`Negativo`)

Fontes incluem dados de NPS, resumos de chamados, pesquisas de relacionamento e interações via CRM.

---

## 🔧 Requisitos

- Python >= 3.8
- transformers >= 4.36.2
- torch >= 2.0

Instalação via pip:
```bash
pip install transformers torch
```

---

## 🌐 Suporte a Idiomas

Este modelo é multilíngue e tem ótimo desempenho em:
- **Português**
- **Inglês**
- **Espanhol**

Pode ser aplicado em contextos multinacionais.

---

## 🚀 Integração com API REST

Este modelo pode ser facilmente incorporado a aplicações backend via `Flask`, `FastAPI` ou outras bibliotecas. Exemplo de endpoint disponível na pasta `/app/routes`.

---

## ✅ Resultados de Avaliação

Métricas estimadas em conjunto de validação:

| Métrica     | Valor     |
|-------------|-----------|
| Acurácia    | 0.92      |
| F1-score    | 0.91      |
| Recall      | 0.89      |
| Precisão    | 0.90      |

> *Resultados baseados em feedbacks reais rotulados.*

---

## 📦 Repositório Relacionado

O código fonte e pipeline de inferência encontram-se no repositório:
[https://github.com/ViniciusKanh/Senticore](https://github.com/ViniciusKanh/Senticore)

---

## 🧠 Autor

Desenvolvido por **Vinicius de Souza Santos (Vinicius Khan)**  
Engenheiro da Computação | Cientista de Dados | Especialista em Machine Learning  
[Perfil no Hugging Face](https://huggingface.co/ViniciusKhan)

---

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
