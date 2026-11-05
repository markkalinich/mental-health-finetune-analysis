---
language:
  - pt

license: apache-2.0

library_name: transformers

pipeline_tag: text-classification

base_model: Comunidade-Synapse-BR/Synapse-Guard-v1.1

new_version: Comunidade-Synapse-BR/Synapse-Guard-v1.2

datasets:
  - Comunidade-Synapse-BR/Synapse-Guard-Dataset-v1

metrics:
  - accuracy
  - f1

tags:
  - bert
  - moderation
  - portuguese
  - pt-br
  - text-classification
  - content-moderation
  - spam-detection
  - toxicity-detection
  - lightweight
---

# 🛡️ Synapse-Guard v1.2

O **Synapse-Guard v1.2** é um modelo leve baseado em **BERT** para moderação automática de conteúdo em português brasileiro.

O modelo foi desenvolvido pela **Comunidade Synapse BR** para classificar textos em quatro categorias, oferecendo inferência rápida, baixo consumo de recursos e integração simples com aplicações que necessitam de filtragem de conteúdo.

> **Importante:** este modelo **não gera conteúdo**. Ele apenas classifica textos nas categorias de moderação.

---

# 📖 Visão Geral

O Synapse-Guard foi criado para auxiliar sistemas de moderação automática na identificação de conteúdos potencialmente inadequados.

Seu foco é oferecer um equilíbrio entre:

- Alta velocidade de inferência
- Boa precisão
- Baixo consumo de memória
- Facilidade de integração
- Aplicações em tempo real

---

# 🏷️ Classes

| Classe | Descrição |
|--------|-----------|
| 🟢 Neutro | Conversas comuns e conteúdo considerado seguro. |
| 📢 Spam | Publicidade abusiva, golpes, phishing e mensagens promocionais. |
| 🔴 Tóxico | Ofensas, insultos, ataques pessoais e linguagem abusiva. |
| 🔞 Adulto | Conteúdo sexual explícito ou material voltado ao público adulto. |

---

# 🎯 Casos de Uso

O modelo pode ser utilizado em:

- Assistentes de IA
- Chatbots
- Redes sociais
- Fóruns
- Sistemas de comentários
- Comunidades online
- APIs de moderação
- Plataformas educacionais
- Sistemas corporativos
- Filtros de spam

---

# ⚡ Exemplo de Uso

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Comunidade-Synapse-BR/Synapse-Guard-v1.2"
)

resultado = classifier("Você é um idiota.")

print(resultado)
```

---

# 📊 Dataset

O modelo foi refinado utilizando o dataset:

**Comunidade-Synapse-BR/Synapse-Guard-Dataset-v1**

O conjunto de dados foi desenvolvido para tarefas de moderação de conteúdo em português brasileiro, contendo exemplos balanceados das quatro categorias suportadas.

---

# 📈 Desempenho

O Synapse-Guard foi desenvolvido para priorizar:

- Alta precisão
- Baixa taxa de falsos positivos
- Boa generalização
- Inferência rápida

Métricas detalhadas poderão ser disponibilizadas em futuras versões do modelo.

---

# ⚠️ Limitações

Embora apresente bom desempenho em moderação de conteúdo, nenhum classificador é perfeito.

O modelo pode apresentar dificuldades em situações como:

- Ironias
- Sarcasmo
- Conteúdo altamente ambíguo
- Mensagens que dependem fortemente do contexto

Para aplicações críticas, recomenda-se utilizar revisão humana como camada adicional de segurança.

---

# 📜 Licença

Este modelo é distribuído sob a licença **Apache License 2.0**.

Consulte a documentação do repositório para mais informações.

---

# 🤝 Sobre a Comunidade Synapse BR

A **Comunidade Synapse BR** é uma iniciativa brasileira dedicada ao desenvolvimento de modelos de inteligência artificial, datasets e ferramentas de código aberto.

Nossa missão é tornar a IA mais acessível por meio de soluções leves, eficientes e abertas, fortalecendo a participação do Brasil no ecossistema global de inteligência artificial.

Contribuições, sugestões e relatos de problemas são sempre bem-vindos.