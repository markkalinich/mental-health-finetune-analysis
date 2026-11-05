---
library_name: transformers
license: mit
datasets:
- google-research-datasets/go_emotions
tags:
- PyTorch
- multi-label
- emoções
- NLP
- roberta
- goemotions
language:
- en
- pt
base_model:
- FacebookAI/roberta-base
pipeline_tag: text-classification
---

#  pinheiro-roberta-goemotions-v2

Segunda versão do modelo fine tuned [pinheiro-roberta-goemotions-v2](https://huggingface.co/pinheiroxs/pinheiro-roberta-goemotions).

Essa versão foi feita visando aplicação de técnicas de otimização e aceleração de treinamento em GPU's 'limitas'. Visite [meu GitHub](https://github.com/matheusdatasci/treinamento-otimizado)
para verificar meu notebook e técnicas aplicadas ;) 


## Como usar

```python
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Carregar tokenizer
tokenizer =  AutoTokenizer.from_pretrained("roberta-base")

# Map de id2label
id2label = {
    0: 'admiration', 1: 'amusement', 2: 'anger', 3: 'annoyance', 4: 'approval',
    5: 'caring', 6: 'confusion', 7: 'curiosity', 8: 'desire', 9: 'disappointment',
    10: 'disapproval', 11: 'disgust', 12: 'embarrassment', 13: 'excitement', 14: 'fear',
    15: 'gratitude', 16: 'grief', 17: 'joy', 18: 'love', 19: 'nervousness', 20: 'optimism',
    21: 'pride', 22: 'realization', 23: 'relief', 24: 'remorse', 25: 'sadness', 26: 'surprise', 27: 'neutral'
}

# Carregar modelo
modelo = AutoModelForSequenceClassification.from_pretrained("pinheiroxs/pinheiro-roberta-goemotions-v2",id2label=id2label)

# Criar pipeline
classifier = pipeline("text-classification", model=modelo, tokenizer=tokenizer, top_k=None)
```
```python
# Exemplo de uso
texto = "I am very happy today!"
resultado = classifier(texto)[0]

# Formatar resultados
resultado_ordenado = sorted(resultado, key=lambda x: x['score'], reverse=True)
for r in resultado_ordenado:
    print(f"{r['label']:15} : {r['score']*100:.2f}%")
```
