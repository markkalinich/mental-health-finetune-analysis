---
language: pt
license: mit
base_model: neuralmind/bert-base-portuguese-cased
tags:
  - sentiment-analysis
  - portuguese
  - bert
  - fine-tuned
  - youtube
  - children-safety
datasets:
  - custom
metrics:
  - accuracy
  - f1
---

# BERTimbau Fine-tuned — Análise de Sentimentos em Português (YouTube Infantil)

Modelo BERTimbau ajustado para classificação de sentimentos em três classes (**Negativo**, **Neutro**, **Positivo**) sobre transcrições e títulos de vídeos do YouTube voltados ao público infantil em Português do Brasil.

Desenvolvido para o artigo *"Análise de Sentimentos no YouTube para Conteúdo Infantil: IA para Reclassificar Resultados de Busca"* — WICS 2026.

## Resultados

| Conjunto | Acurácia | F1 Macro |
|----------|----------|----------|
| Validação cruzada 5-fold (média ± std) | 77,49% ± 0,74% | 0,7761 ± 0,0076 |
| Teste holdout 20% | **77,27%** | **0,7749** |

**F1 por classe no holdout:**

| Classe | Precisão | Recall | F1 |
|--------|----------|--------|----|
| Negativo | 0,935 | 0,902 | **0,918** |
| Neutro | 0,667 | 0,800 | 0,727 |
| Positivo | 0,761 | 0,614 | 0,679 |

O F1 de 91,8% na classe Negativo é a métrica mais crítica para segurança infantil.

## Corpus

- **2.749 frases** reais extraídas do YouTube, rotuladas manualmente
- Distribuição balanceada: Negativo 31,6% · Neutro 36,3% · Positivo 32,1%
- Idioma: Português do Brasil (sem tradução automática)

## Treinamento

- **Modelo base**: `neuralmind/bert-base-portuguese-cased` (BERTimbau)
- **Validação**: 5-Fold Stratified Cross-Validation
- **Balanceamento**: Random Oversampling aplicado apenas nos folds de treino
- **Otimizador**: AdamW — lr: 5e-5, warmup: 500 steps, weight decay: 0.01
- **Épocas**: 5 · **Batch size**: 8 · **Seed**: 42
- Este checkpoint corresponde ao Fold 1 (78,64% CV), usado na avaliação oficial do holdout.

## Uso

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_path = "ravarmes/bertimbau-sentiment-youtube-pt"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)
model.eval()

label_map = {0: "Negativo", 1: "Neutro", 2: "Positivo"}

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    return label_map[logits.argmax(-1).item()]

print(predict("Este vídeo é muito educativo e divertido para as crianças!"))
# → Positivo

print(predict("Conteúdo assustador e inapropriado para crianças."))
# → Negativo
```

## Limitações

- Treinado em domínio específico (conteúdo infantil no YouTube em PT-BR); pode ter desempenho inferior em outros domínios.
- Maior confusão entre as classes Neutro e Positivo, que compartilham características semânticas próximas.

## Citação

```bibtex
@inproceedings{mesquita2026sentimentos,
  title     = {Análise de Sentimentos no YouTube para Conteúdo Infantil: IA para Reclassificar Resultados de Busca},
  author    = {Mesquita Santos, Rafael Vargas and de Salles, João Victor and Izo, Flávio and Vargas, Sabrina},
  booktitle = {WICS 2026},
  year      = {2026}
}
```
