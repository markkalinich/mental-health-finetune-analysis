---
library_name: transformers
license: apache-2.0
base_model: Comunidade-Synapse-BR/Synapse-Guard-v1

language:
  - pt

pipeline_tag: text-classification

tags:
  - bert
  - portuguese
  - pt-br
  - text-classification
  - content-moderation
  - spam-detection
  - toxicity-detection
  - adult-content
  - lightweight
---

# 🛡️ Synapse-Guard v1.1

O **Synapse-Guard v1.1** é um modelo leve baseado em **BERT** para classificação de conteúdo em português brasileiro, desenvolvido pela **Comunidade Synapse BR**.

Esta versão representa uma evolução do **Synapse-Guard v1**, sendo refinada com um conjunto de treinamento maior e revisado para melhorar a qualidade da classificação.

O modelo foi desenvolvido para aplicações de moderação automática de conteúdo, oferecendo inferência rápida e baixo consumo de recursos.

> **Importante:** este modelo **não gera conteúdo**. Ele apenas classifica textos em categorias de moderação.

---

# 📖 Visão Geral

O Synapse-Guard v1.1 foi projetado para auxiliar sistemas de moderação automática na identificação de conteúdos potencialmente inadequados.

O foco desta versão foi melhorar a qualidade do treinamento mantendo uma arquitetura leve, adequada para aplicações em produção.

---

# 🏷️ Classes

| Classe | Descrição |
|--------|-----------|
| 🟢 Neutro | Conversas comuns e conteúdo considerado seguro. |
| 📢 Spam | Publicidade abusiva, golpes, phishing e mensagens promocionais. |
| 🔴 Tóxico | Linguagem ofensiva, insultos e conteúdo abusivo. |
| 🔞 Adulto | Conteúdo sexual explícito ou voltado ao público adulto. |

---

# 🎯 Casos de Uso

O modelo é indicado para:

- Moderação automática
- Chatbots
- Assistentes de IA
- Redes sociais
- Fóruns
- Sistemas de comentários
- Detecção de spam
- Filtragem de conteúdo adulto
- Aplicações embarcadas com recursos limitados

---

# 🏋️ Treinamento

Esta versão foi refinada a partir do:

- **Modelo base:** Synapse-Guard v1

Conjunto de treinamento:

- Aproximadamente **365.000 exemplos**
- Aproximadamente **50.000 exemplos de validação**
- Textos em português brasileiro

---

# ⚡ Exemplo de Uso

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Comunidade-Synapse-BR/Synapse-Guard-v1.1"
)

resultado = classifier("Você é um idiota.")

print(resultado)
```

---

# 📊 Avaliação

Durante o treinamento, o modelo apresentou excelente desempenho no conjunto de validação utilizado durante o fine-tuning.

Entretanto, avaliações realizadas com exemplos inéditos mostraram que o desempenho pode variar conforme o domínio, estilo de escrita e distribuição dos dados de entrada.

Como qualquer modelo supervisionado, sua qualidade depende da semelhança entre os dados utilizados em produção e aqueles presentes durante o treinamento.

---

# ⚠️ Limitações

Embora apresente bom desempenho para moderação de conteúdo em português, o modelo pode apresentar dificuldades em situações como:

- Ironias
- Sarcasmo
- Conteúdo ambíguo
- Textos muito curtos
- Mensagens que dependem fortemente do contexto

Para aplicações críticas, recomenda-se utilizar revisão humana como camada adicional de segurança.

---

# 📜 Licença

Este modelo é distribuído sob a licença **Apache License 2.0**.

Consulte o repositório para informações adicionais.

---

# ⚖️ Aviso

Este modelo foi desenvolvido para pesquisa, desenvolvimento e integração em aplicações de moderação de conteúdo.

As previsões do modelo não devem ser consideradas decisões definitivas. Os desenvolvedores são responsáveis por validar seu desempenho antes da utilização em ambientes de produção.

---

# 🤝 Sobre a Comunidade Synapse BR

A **Comunidade Synapse BR** é uma iniciativa brasileira dedicada ao desenvolvimento de modelos de inteligência artificial, datasets e ferramentas de código aberto para a comunidade de língua portuguesa.

Nossa missão é tornar a inteligência artificial mais acessível por meio de soluções leves, eficientes e abertas, contribuindo para fortalecer o ecossistema brasileiro de IA.