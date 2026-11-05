---
library_name: transformers
tags:
- text-classification
- sequence-classification
- moderation
- content-moderation
- toxicity
- spam-detection
- adult-content
- portuguese
- pt-br
- brazilian-portuguese
- transformers
- pytorch
- alpha
license: apache-2.0
language:
- pt
base_model:
- Comunidade-Synapse-BR/Synpase-guard-v1.3
pipeline_tag: text-classification
---
🧠 Synapse-Guard v1.4 Alpha

Desenvolvido pela Comunidade Synapse BR

O Synapse-Guard v1.4 Alpha é uma versão experimental do modelo de moderação de conteúdo da Comunidade Synapse BR, otimizada para Português Brasileiro (pt-BR).

Esta versão foi submetida a um processo de fine-tuning com o objetivo de melhorar a identificação de conteúdo tóxico, adulto, spam e neutro.

«⚠️ Status: Alpha — esta versão ainda está em desenvolvimento e avaliação. Os resultados apresentados não representam necessariamente o desempenho final do modelo.»

📊 Performance — Blind Test

O modelo foi avaliado em um Blind Test com 500 amostras inéditas.

Versão| Acurácia Global| Status
v1.4 Alpha| 71,60%| 🧪 Em desenvolvimento
v1.3 Original| 26,20%| Base
v1.2| 25,40%| Legado
v1.1| 25,80%| Legado

🎯 Desempenho por Classe

Categoria| Acurácia| Descrição
🔴 Tóxico| 94,4%| Agressividade, insultos e assédio.
🔞 Adulto| 88,0%| Conteúdo sexualmente explícito ou sugestivo.
📢 Spam| 84,8%| Spam, phishing, golpes e links suspeitos.
🟢 Neutro| 19,2%| Conteúdo comum, legítimo ou não ofensivo.

🛠️ Metodologia

1. Fase de Correção

Treinamento com 6.000 amostras balanceadas para corrigir erros e fortalecer os padrões de classificação.

2. Fase Neutro-Focused

Foi realizado um ajuste fino adicional de 1 época, utilizando 5.000 amostras focadas na classe Neutro.

O objetivo foi melhorar a capacidade do modelo de diferenciar linguagem legítima, formal e técnica de conteúdo potencialmente impróprio.

3. Seleção do Checkpoint

O checkpoint selecionado foi aquele que apresentou a melhor generalização durante a avaliação da fase de correção.

🚀 Uso

from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "Comunidade-Synapse-BR/Synapse-Guard-v1.4-Finetuned"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

⚠️ Limitações

Como uma versão Alpha, o modelo ainda apresenta limitações.

Pode apresentar dificuldades principalmente em:

- Ironia e sarcasmo;
- Gírias muito específicas;
- Contextos altamente informais;
- Mensagens ambíguas;
- Casos em que o contexto da conversa é necessário para determinar a intenção.

Além disso, a baixa acurácia atual na classe Neutro indica que ainda existe espaço significativo para melhorias.

Por isso, o modelo não é recomendado para decisões críticas totalmente automatizadas nesta fase.

🔬 Próximos Passos

O desenvolvimento futuro do Synapse-Guard deverá priorizar:

- Aumento da precisão na classe Neutro;
- Redução de falsos positivos;
- Expansão do dataset em Português Brasileiro;
- Testes com gírias e linguagem informal;
- Avaliações independentes em datasets inéditos;
- Melhor equilíbrio entre as quatro classes.

📌 Resumo

O Synapse-Guard v1.4 Alpha representa uma etapa experimental no desenvolvimento de um sistema leve de moderação em Português Brasileiro.

Com 71,60% de acurácia global no Blind Test e desempenho superior a 84% nas classes Tóxico, Adulto e Spam, o modelo demonstra potencial, mas ainda precisa de novas iterações antes de ser considerado uma versão estável.

Status atual: 🧪 Alpha — em desenvolvimento.