---
library_name: transformers
license: apache-2.0
language:
  - pt
pipeline_tag: text-classification
base_model: Comunidade-Synapse-BR/Synapse-Guard-v1.2
tags:
  - bert
  - moderation
  - content-moderation
  - spam
  - toxicity
  - portuguese
  - pt-br
  - text-classification
---

# 🛡️ Synapse-Guard v1.3 🇧🇷

**Synapse-Guard v1.3** é um modelo baseado em **BERT** desenvolvido pela **Comunidade Synapse BR** para moderação automática de conteúdo em português brasileiro.

O modelo classifica textos em quatro categorias:

- 🟢 **Neutro**
- 🔴 **Tóxico**
- 📢 **Spam**
- 🔞 **Adulto**

Foi projetado para oferecer **alta velocidade de inferência**, **baixo consumo de memória** e bom desempenho em aplicações reais, como redes sociais, comunidades, chatbots e plataformas digitais.

---

# 📖 Visão Geral

O Synapse-Guard foi desenvolvido para auxiliar sistemas de moderação automática na identificação de conteúdos potencialmente inadequados.

O modelo foi refinado utilizando conjuntos de dados balanceados em português brasileiro, buscando um equilíbrio entre:

- Alta precisão
- Redução de falsos positivos
- Boa capacidade de generalização
- Eficiência computacional

---

# 🚀 Principais melhorias da versão 1.3

Esta versão introduz diversos aprimoramentos em relação à versão anterior.

## 🇧🇷 Melhor compreensão da linguagem brasileira

O modelo foi exposto a uma maior variedade de:

- Gírias
- Abreviações
- Erros ortográficos comuns
- Linguagem informal
- Expressões utilizadas em redes sociais

Isso melhora significativamente a classificação de mensagens presentes em:

- Redes sociais
- Comentários
- Chats
- Aplicativos de mensagens

---

## 📢 Melhor detecção de Spam

O classificador apresenta maior capacidade para diferenciar mensagens legítimas de tentativas de spam.

Exemplos de mensagens legítimas:

- "Parabéns pela promoção!"
- "Seu pedido foi enviado."
- "Obrigado pelo contato."

Também houve melhoria na identificação de:

- Phishing
- Golpes
- Links suspeitos
- Promoções enganosas
- Spam comercial

---

## 🔞 Melhor reconhecimento de conteúdo adulto

O modelo recebeu ajustes para identificar anúncios e serviços adultos que utilizam linguagem indireta ou codificada.

Entre os casos considerados estão:

- anúncios de acompanhantes;
- serviços privados;
- conteúdo adulto disfarçado.

---

## ✅ Redução de falsos positivos

Foram realizados refinamentos para diminuir classificações incorretas em textos profissionais e técnicos.

Exemplos:

- documentação técnica;
- dúvidas de programação;
- mensagens corporativas;
- relatórios;
- suporte ao cliente.

---

# 📂 Classes

| Classe | Descrição |
|--------|-----------|
| 🟢 Neutro | Conversas comuns, textos informativos e conteúdo legítimo |
| 🔴 Tóxico | Insultos, ofensas, agressões verbais e linguagem abusiva |
| 📢 Spam | Publicidade abusiva, phishing, golpes e mensagens repetitivas |
| 🔞 Adulto | Conteúdo sexual explícito, anúncios e serviços adultos |

---

# 💡 Casos de Uso

O Synapse-Guard pode ser utilizado em:

- Redes sociais
- Comunidades online
- Fóruns
- Chatbots
- Sistemas de comentários
- Plataformas educacionais
- Aplicativos de mensagens
- APIs de moderação
- Ferramentas de IA
- Plataformas corporativas

---

# ⚙️ Características

- Baseado em BERT
- Otimizado para português brasileiro
- Inferência rápida
- Baixo consumo de memória
- Equilíbrio entre precisão e velocidade
- Desenvolvido para aplicações reais

---

# 📈 Melhorias em relação à versão anterior

- Melhor compreensão da linguagem informal brasileira.
- Redução de falsos positivos.
- Melhor separação entre mensagens legítimas e spam.
- Melhor identificação de conteúdo adulto.
- Melhor desempenho em textos do cotidiano.

---

# 📊 Desempenho

O modelo foi desenvolvido para priorizar:

- Alta precisão
- Baixa taxa de falsos positivos
- Boa capacidade de generalização
- Inferência rápida

*Métricas quantitativas poderão ser adicionadas em versões futuras conforme novas avaliações forem realizadas.*

---

# ⚠️ Limitações

Nenhum sistema de moderação é perfeito.

O Synapse-Guard pode apresentar dificuldades em situações como:

- Ironias
- Sarcasmo
- Conteúdo altamente ambíguo
- Mensagens que dependem fortemente de contexto externo

Para aplicações críticas, recomenda-se utilizar revisão humana como camada adicional de segurança.

---

# 📜 Licença

Este modelo é distribuído sob a licença especificada neste repositório.

Consulte também a licença do modelo base, quando aplicável.

---

# 📚 Citação

Caso este modelo contribua para sua pesquisa ou projeto, considere citá-lo.

```bibtex
@misc{synapse_guard_v13,
  title={Synapse-Guard v1.3},
  author={Comunidade Synapse BR},
  year={2026},
  publisher={Hugging Face}
}
```

---

# 🤝 Sobre a Comunidade Synapse BR

A **Comunidade Synapse BR** é uma iniciativa brasileira dedicada ao desenvolvimento de modelos de inteligência artificial, datasets e ferramentas abertas para a comunidade de língua portuguesa.

Nossa missão é tornar a IA mais acessível por meio de soluções leves, eficientes e de código aberto, fortalecendo a participação do Brasil no ecossistema global de inteligência artificial.

Contribuições, sugestões e relatos de problemas são sempre bem-vindos.

---