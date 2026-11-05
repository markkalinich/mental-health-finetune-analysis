---
license: apache-2.0
language:
- pt
base_model:
- Assaoka/Tucano2-qwen-0.5B-ReLiSA
- Assaoka/Tucano2-qwen-0.5B-Brighter
- Assaoka/Tucano2-qwen-0.5B-FinBERT
- Assaoka/Tucano2-qwen-0.5B-Phrasebank
pipeline_tag: text-generation
library_name: transformers
tags:
- sentiment-analysis
- slm
- eniac-2026
- knowledge-accumulation
- prior-alignment
datasets:
- antoniomenezes/go_emotions_ptbr
metrics:
- f1
- accuracy
model-index:
- name: Tucano2-qwen-0.5b-Merge-Go-Emotions
  results:
  - task:
      type: text-generation
      name: Sentiment Analysis
    dataset:
      name: go-emotions
      type: antoniomenezes/go_emotions_ptbr
      split: test
    metrics:
    - type: f1
      value: 0.3000
      name: Macro F1
    - type: accuracy
      value: 0.3657
      name: Accuracy
---

# Tucano2-qwen-0.5b-Merge-Go-Emotions (Prior Model)

Este é um modelo especialista em análise de sentimento em língua portuguesa, construído usando a estratégia **Knowledge Accumulation (Prior)**. O modelo foi inicialmente pre-mesclado (*merged*) com outros especialistas usando TIES Merge e, em seguida, sofreu ajuste fino (*fine-tuning*) no conjunto de dados **antoniomenezes/go_emotions_ptbr**.

Este desenvolvimento faz parte do artigo científico submetido ao **ENIAC 2026**: *"United Experts: Merging Small Language Models for Multi-Domain Sentiment Analysis in Portuguese"*.

## 📌 Detalhes do Modelo

- **Modelos Base (Merge)**:
- `Assaoka/Tucano2-qwen-0.5B-ReLiSA`
- `Assaoka/Tucano2-qwen-0.5B-Brighter`
- `Assaoka/Tucano2-qwen-0.5B-FinBERT`
- `Assaoka/Tucano2-qwen-0.5B-Phrasebank`
- **Tarefa**: Classificação de emoções extremamente granular para português (28 categorias baseadas em comentários de mídias sociais) após alinhamento sequencial por Knowledge Accumulation (Prior).
- **Domínio**: Língua Portuguesa (PT-BR).
- **Licença**: Apache 2.0.
- **Estratégia**: Alinhamento sequencial via Knowledge Accumulation (Prior + Fine-tuning).

## 📊 Avaliação Completa (In-Domain & Out-Of-Domain)

Métricas padronizadas (Macro F1 · Micro F1 · Accuracy · Hamming Loss) calculadas sobre o conjunto de teste completo de cada domínio. A coluna **Baseline** corresponde ao modelo base `Polygl0t/Tucano2-qwen-0.5B-Instruct` sem fine-tuning.

| Dataset / Tarefa | Métrica | Valor | Baseline |
| :--- | :--- | :---: | :---: |
| **RELI-SA** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 21.92%<br>63.90%<br>63.90%<br>0.3610 | 30.66%<br>37.07%<br>37.07%<br>0.6293 |
| **BRIGHTER** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 39.02%<br>51.61%<br>36.66%<br>0.1529 | 33.47%<br>38.07%<br>24.66%<br>0.2731 |
| **FINBERT-PT-BR** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 14.47%<br>27.72%<br>27.72%<br>0.7228 | 54.77%<br>66.34%<br>66.34%<br>0.3366 |
| **FINANCIAL-PHRASEBANK** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 29.59%<br>60.27%<br>60.27%<br>0.3973 | 38.13%<br>39.32%<br>39.32%<br>0.6068 |
| **GO-EMOTIONS** | Macro F1<br>Micro F1<br>Accuracy<br>Hamming Loss | 30.00%<br>41.85%<br>36.57%<br>0.0465 | 7.59%<br>10.31%<br>6.08%<br>0.0720 |


## 🚀 Como utilizar o modelo (vLLM ou Transformers)

O modelo responde a prompts estruturados com instruções do sistema em português. Exemplo real de inferência estruturada:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Assaoka/Tucano2-qwen-0.5b-Merge-GoEmotions"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

messages = [
    {"role": "system", "content": "Você é um classificador de emoções para português. Analise o texto fornecido e retorne a lista de emoções detectadas (pode ser vazia). As opções válidas são: 'admiração', 'diversão', 'raiva', 'irritação', 'aprovação', 'carinho', 'confusão', 'curiosidade', 'desejo', 'decepção', 'desaprovação', 'nojo', 'constrangimento', 'entusiasmo', 'medo', 'gratidão', 'luto', 'alegria', 'amor', 'nervosismo', 'otimismo', 'orgulho', 'percepção', 'alívio', 'remorso', 'tristeza', 'surpresa', 'neutro'. Sua tarefa é retornar um JSON válido no seguinte formato: {"emocoes": ["emocao1", "emocao2", ..., "emocaoN"]} baseado na lista de emoções permitidas. Responda APENAS com o JSON válido."},
    {"role": "user", "content": "Comentário: Muito obrigado pela ajuda! Fiquei realmente grato pela sua atenção."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
# Resposta esperada: {"emocoes": ["gratidão"]}
```
