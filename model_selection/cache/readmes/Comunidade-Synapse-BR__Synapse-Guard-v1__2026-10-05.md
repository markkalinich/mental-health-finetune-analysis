---
license: apache-2.0

language:
  - pt

library_name: transformers

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

# 🛡️ Synapse-Guard v1

O **Synapse-Guard v1** é a primeira versão pública da família **Synapse-Guard**, desenvolvida pela **Comunidade Synapse BR** para classificação automática de conteúdo em português brasileiro.

Baseado em uma arquitetura **BERT** compacta, o modelo foi desenvolvido para oferecer uma solução leve e eficiente para moderação automática de conteúdo, podendo ser utilizado em chatbots, fóruns, comunidades, redes sociais e outras aplicações que necessitam identificar diferentes tipos de mensagens.

> **Importante:** este modelo **não gera conteúdo**. Sua função é apenas classificar textos em categorias de moderação.

---

# 📖 Visão Geral

O Synapse-Guard v1 representa o início da linha de modelos de moderação da Comunidade Synapse BR.

Seu objetivo é fornecer uma base simples, rápida e acessível para aplicações que necessitam identificar automaticamente conteúdos potencialmente inadequados em português.

---

# 🏷️ Classes

| Classe | Descrição |
|--------|-----------|
| 🟢 Neutro | Conversas comuns e conteúdo considerado seguro. |
| 📢 Spam | Publicidade abusiva, golpes, phishing e mensagens promocionais. |
| 🔴 Tóxico | Linguagem ofensiva, insultos e conteúdo abusivo. |
| 🔞 Adulto | Conteúdo sexual explícito ou material destinado ao público adulto. |

---

# 🎯 Casos de Uso

O modelo pode ser utilizado em:

- Chatbots
- Assistentes de IA
- Redes sociais
- Fóruns
- Sistemas de comentários
- Plataformas educacionais
- APIs de moderação
- Detecção de spam
- Filtragem de conteúdo adulto

---

# 🏋️ Dataset

O modelo foi treinado utilizando o **Synapse Dataset v1**.

Características do conjunto de dados:

- 120.000 exemplos
- 4 classes balanceadas
- Aproximadamente 30.000 exemplos por classe
- Textos em português brasileiro

---

# 🏗️ Arquitetura

| Propriedade | Valor |
|-------------|-------|
| Arquitetura | BERT Encoder |
| Parâmetros | ~5 milhões |
| Tokenizador | WordPiece |
| Idioma | Português Brasileiro |
| Framework | Transformers |

---

# ⚡ Exemplo de Uso

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Comunidade-Synapse-BR/Synapse-Guard-v1"
)

resultado = classifier("Você ganhou um prêmio! Clique aqui.")

print(resultado)
```

---

# ⚠️ Limitações

Embora tenha sido desenvolvido para moderação automática de conteúdo em português brasileiro, nenhum modelo de classificação é perfeito.

O Synapse-Guard v1 pode apresentar dificuldades em situações como:

- Ironias
- Sarcasmo
- Conteúdo altamente ambíguo
- Mensagens muito curtas
- Textos que dependem fortemente de contexto

Para aplicações críticas, recomenda-se utilizar revisão humana como camada adicional de segurança.

---

# 📜 Licença

Este modelo é distribuído sob a licença **Apache License 2.0**.

---

# ⚖️ Aviso

Este modelo é disponibilizado para fins de pesquisa, desenvolvimento e integração em aplicações de inteligência artificial.

As previsões geradas pelo modelo não devem ser consideradas decisões definitivas. Os usuários são responsáveis por validar seu desempenho antes da utilização em ambientes de produção.

O modelo é fornecido **"como está"**, sem garantias de qualquer natureza.

A **Comunidade Synapse BR** e seus colaboradores não se responsabilizam por decisões, interpretações ou quaisquer danos decorrentes do uso deste modelo.

---

# 🚀 Evolução do Projeto

O **Synapse-Guard v1** é a primeira versão pública da família Synapse-Guard.

Versões futuras introduzem melhorias na qualidade dos dados, redução de falsos positivos, maior robustez para linguagem informal e melhor desempenho em cenários reais de moderação.

---

# 🤝 Sobre a Comunidade Synapse BR

A **Comunidade Synapse BR** é uma iniciativa brasileira dedicada ao desenvolvimento de modelos de inteligência artificial, datasets e ferramentas de código aberto.

Nossa missão é tornar a inteligência artificial mais acessível por meio de soluções leves, eficientes e abertas, fortalecendo a presença do Brasil no ecossistema global de IA.

Contribuições, sugestões e relatos de problemas são sempre bem-vindos.