---
license: apache-2.0
language:
- pt
base_model:
- Assaoka/Tucano2-qwen-0.5B-Brighter
- Assaoka/Tucano2-qwen-0.5B-FinBERT
- Assaoka/Tucano2-qwen-0.5B-Phrasebank
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
- ruanchaves/reli
metrics:
- f1
- accuracy
model-index:
- name: Tucano2-qwen-0.5b-Merge-ReLi-SA
  results:
  - task:
      type: text-generation
      name: Sentiment Analysis
    dataset:
      name: reli-sa-label
      type: ruanchaves/reli
      split: test
    metrics:
    - type: f1
      value: 0.6975
      name: Macro F1
    - type: accuracy
      value: 0.8041
      name: Accuracy
---

# Tucano2-qwen-0.5b-Merge-ReLi-SA (Prior Model)

Este é um modelo especialista em análise de sentimento em língua portuguesa, construído usando a estratégia **Knowledge Accumulation (Prior)**. O modelo foi inicialmente pre-mesclado (*merged*) com outros especialistas usando TIES Merge e, em seguida, sofreu ajuste fino (*fine-tuning*) no conjunto de dados **ruanchaves/reli**.

Este desenvolvimento faz parte do artigo científico submetido ao **ENIAC 2026**: *"United Experts: Merging Small Language Models for Multi-Domain Sentiment Analysis in Portuguese"*.

## 📌 Detalhes do Modelo

- **Modelos Base (Merge)**:
- `Assaoka/Tucano2-qwen-0.5B-Brighter`
- `Assaoka/Tucano2-qwen-0.5B-FinBERT`
- `Assaoka/Tucano2-qwen-0.5B-Phrasebank`
- `Assaoka/Tucano2-qwen-0.5B-GoEmotions`
- **Tarefa**: Análise de Sentimentos (positivo, negativo, neutro, misto) em resenhas literárias em português após alinhamento sequencial por Knowledge Accumulation (Prior).
- **Domínio**: Língua Portuguesa (PT-BR).
- **Licença**: Apache 2.0.
- **Estratégia**: Alinhamento sequencial via Knowledge Accumulation (Prior + Fine-tuning).

## 📊 Avaliação Completa (In-Domain & Out-Of-Domain)

Métricas padronizadas (Macro F1 · Micro F1 · Accuracy · Hamming Loss) calculadas sobre o conjunto de teste completo de cada domínio. A coluna **Baseline** corresponde ao modelo base `Polygl0t/Tucano2-qwen-0.5B-Instruct` sem fine-tuning.

| Dataset / Tarefa | Métrica | Valor | Baseline |
| :--- | :--- | :---: | :---: |
| **RELI-SA** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 69.75%<br>80.41%<br>80.41%<br>0.1959 | 30.66%<br>37.07%<br>37.07%<br>0.6293 |
| **BRIGHTER** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 37.72%<br>52.88%<br>37.98%<br>0.1479 | 33.47%<br>38.07%<br>24.66%<br>0.2731 |
| **FINBERT-PT-BR** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 22.45%<br>31.68%<br>31.68%<br>0.6832 | 54.77%<br>66.34%<br>66.34%<br>0.3366 |
| **FINANCIAL-PHRASEBANK** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 30.73%<br>59.96%<br>59.96%<br>0.4004 | 38.13%<br>39.32%<br>39.32%<br>0.6068 |
| **GO-EMOTIONS** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 19.73%<br>36.39%<br>33.34%<br>0.0496 | 7.59%<br>10.31%<br>6.08%<br>0.0720 |


## 🚀 Como utilizar o modelo (vLLM ou Transformers)

O modelo responde a prompts estruturados com instruções do sistema em português. Exemplo real de inferência estruturada:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Assaoka/Tucano2-qwen-0.5b-Merge-ReLiSA"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

messages = [
    {"role": "system", "content": "Você é um classificador de sentimentos de resenhas de livros em português. Sua tarefa é analisar o texto fornecido pelo usuário e retornar um JSON válido no seguinte formato: {"sentimento": "positivo/negativo/neutro/misto"}. Responda APENAS com o JSON válido."},
    {"role": "user", "content": "Resenha: Este livro é maravilhoso, a escrita é super fluida e envolvente, mas o final deixou a desejar."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
# Resposta esperada: {"sentimento": "misto"}
```
