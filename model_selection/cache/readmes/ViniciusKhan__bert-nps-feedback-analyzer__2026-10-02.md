---
language:
  - pt
tags:
  - sentiment-analysis
  - nps
  - text-classification
  - portuguese
license: mit
pipeline_tag: text-classification
datasets:
  - nps
  - customer-feedback
---

# 🤖 BERT NPS Feedback Analyzer (PT-BR)

Este modelo é uma adaptação de `cardiffnlp/twitter-xlm-roberta-base-sentiment` voltada para a **análise de sentimentos em textos longos de NPS** (Net Promoter Score), com foco em avaliações técnicas, institucionais e operacionais típicas de ambientes corporativos.

---

## 🧠 Contexto do Problema

Frases de NPS corporativas em português tendem a ser extensas e mistas, contendo tanto elogios quanto críticas em uma mesma resposta. A maioria dos modelos tradicionais apresenta falhas ao interpretar esse tipo de conteúdo, classificando erroneamente como **negativo** textos que relatam **problemas já resolvidos** ou **experiências neutras**.

---

## 🏗️ Arquitetura do Modelo

- **Base**: [`cardiffnlp/twitter-xlm-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)
- **Arquitetura**: XLM-RoBERTa base (multilíngue, robusto para entradas longas)
- **Tarefa**: `text-classification` com 3 classes:
  - `Negative`
  - `Neutral`
  - `Positive`

---

## 📥 Uso do Modelo

### 🔧 Requisitos

```bash
pip install transformers torch
```

### 📦 Código de uso

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import torch

# Nome do modelo no Hugging Face Hub
modelo = "ViniciusKhan/bert-nps-feedback-analyzer"

# Carregar modelo e tokenizer
tokenizer = AutoTokenizer.from_pretrained(modelo)
model = AutoModelForSequenceClassification.from_pretrained(modelo)

# Texto de NPS para avaliação
texto = """ 
Conversei com Alexandre em 20/06 e ele relatou insatisfação com os relatórios, pois vieram misturados.
O chamado foi resolvido e desde então me procura sempre que precisa. Está satisfeito com os serviços atuais.
"""

# Tokenizar e inferir
inputs = tokenizer(texto, return_tensors="pt", truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=1)

# Rótulos
classes = ['Negative', 'Neutral', 'Positive']
classe_predita = classes[probs.argmax().item()]

print("Sentimento:", classe_predita)
```

---

## ✅ Aplicações práticas

Este modelo é ideal para:

- Classificação de feedback de clientes em **SAC, helpdesk e pós-venda**
- Avaliação de **sentimento em pesquisas de satisfação (NPS)**
- Processamento automatizado de tickets e reclamações
- Sistemas de BI e dashboards com análise textual

---

## 🗂️ Estrutura do Repositório

| Arquivo              | Descrição                           |
|----------------------|-------------------------------------|
| `pytorch_model.bin`  | Pesos do modelo                     |
| `config.json`        | Configuração do modelo              |
| `tokenizer.json`     | Vocabulário do tokenizer            |
| `README.md`          | Descrição técnica do modelo         |

---

## 🧬 Dataset original do modelo base

O modelo base foi treinado com dados multilingues do Twitter, incluindo português, e adaptado para generalização ampla de sentimentos. A robustez do XLM-RoBERTa permite interpretar frases com vocabulário técnico e institucional mesmo sem fine-tuning adicional.

---

## 👨‍💻 Autor

**Vinicius de Souza Santos**  
Cientista de Dados • IFSP • Especialista em Machine Learning aplicado a serviços e experiência do cliente  
🔗 [GitHub](https://github.com/ViniciusKanh)

---

## 📄 Licença

Este modelo é disponibilizado sob a licença MIT.
