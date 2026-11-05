---
license: apache-2.0
language:
- pt
base_model:
- Assaoka/Tucano2-qwen-0.5B-ReLiSA
- Assaoka/Tucano2-qwen-0.5B-Brighter
- Assaoka/Tucano2-qwen-0.5B-FinBERT
- Assaoka/Tucano2-qwen-0.5B-GoEmotions
pipeline_tag: text-generation
library_name: transformers
tags:
- sentiment-analysis
- slm
- eniac-2026
- knowledge-accumulation
- prior-alignment
datasets:
- mateuspicanco/financial-phrase-bank-portuguese-translation
metrics:
- f1
- accuracy
model-index:
- name: Tucano2-qwen-0.5b-Merge-Financial-Phrasebank
  results:
  - task:
      type: text-generation
      name: Sentiment Analysis
    dataset:
      name: financial-phrasebank
      type: mateuspicanco/financial-phrase-bank-portuguese-translation
      split: test
    metrics:
    - type: f1
      value: 0.8532
      name: Macro F1
    - type: accuracy
      value: 0.8648
      name: Accuracy
---

# Tucano2-qwen-0.5b-Merge-Financial-Phrasebank (Prior Model)

Este é um modelo especialista em análise de sentimento em língua portuguesa, construído usando a estratégia **Knowledge Accumulation (Prior)**. O modelo foi inicialmente pre-mesclado (*merged*) com outros especialistas usando TIES Merge e, em seguida, sofreu ajuste fino (*fine-tuning*) no conjunto de dados **mateuspicanco/financial-phrase-bank-portuguese-translation**.

Este desenvolvimento faz parte do artigo científico submetido ao **ENIAC 2026**: *"United Experts: Merging Small Language Models for Multi-Domain Sentiment Analysis in Portuguese"*.

## 📌 Detalhes do Modelo

- **Modelos Base (Merge)**:
- `Assaoka/Tucano2-qwen-0.5B-ReLiSA`
- `Assaoka/Tucano2-qwen-0.5B-Brighter`
- `Assaoka/Tucano2-qwen-0.5B-FinBERT`
- `Assaoka/Tucano2-qwen-0.5B-GoEmotions`
- **Tarefa**: Análise de Sentimento (positivo, negativo, neutro) estruturada para o Financial Phrasebank traduzido para português após alinhamento sequencial por Knowledge Accumulation (Prior).
- **Domínio**: Língua Portuguesa (PT-BR).
- **Licença**: Apache 2.0.
- **Estratégia**: Alinhamento sequencial via Knowledge Accumulation (Prior + Fine-tuning).

## 📊 Avaliação Completa (In-Domain & Out-Of-Domain)

Métricas padronizadas (Macro F1 · Micro F1 · Accuracy · Hamming Loss) calculadas sobre o conjunto de teste completo de cada domínio. A coluna **Baseline** corresponde ao modelo base `Polygl0t/Tucano2-qwen-0.5B-Instruct` sem fine-tuning.

| Dataset / Tarefa | Métrica | Valor | Baseline |
| :--- | :--- | :---: | :---: |
| **RELI-SA** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 45.44%<br>70.95%<br>70.95%<br>0.2905 | 30.66%<br>37.07%<br>37.07%<br>0.6293 |
| **BRIGHTER** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 36.53%<br>51.70%<br>37.42%<br>0.1520 | 33.47%<br>38.07%<br>24.66%<br>0.2731 |
| **FINBERT-PT-BR** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 81.17%<br>81.19%<br>81.19%<br>0.1881 | 54.77%<br>66.34%<br>66.34%<br>0.3366 |
| **FINANCIAL-PHRASEBANK** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 85.32%<br>86.48%<br>86.48%<br>0.1352 | 38.13%<br>39.32%<br>39.32%<br>0.6068 |
| **GO-EMOTIONS** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 21.93%<br>33.54%<br>29.01%<br>0.0518 | 7.59%<br>10.31%<br>6.08%<br>0.0720 |


## 🚀 Como utilizar o modelo (vLLM ou Transformers)

O modelo responde a prompts estruturados com instruções do sistema em português. Exemplo real de inferência estruturada:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Assaoka/Tucano2-qwen-0.5b-Merge-Phrasebank"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

messages = [
    {"role": "system", "content": "Você é um analista financeiro. Classifique o sentimento da frase sobre finanças em português fornecida em uma das seguintes opções: 'positivo', 'negativo', 'neutro'. Sua tarefa é retornar um JSON válido no seguinte formato: {"sentimento": "positivo/negativo/neutro"}. Responda APENAS com o JSON válido."},
    {"role": "user", "content": "Frase: A receita operacional líquida da companhia caiu de forma acentuada devido à paralisação das fábricas."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
# Resposta esperada: {"sentimento": "negativo"}
```
