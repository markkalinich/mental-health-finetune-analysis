
---
tags:
- finance
- finbert
- market
- financial
- generated_from_trainer
- financial
- stocks
- sentiment
- text-classification
widget:
- text: "Asian Stocks Set to Decline Amidst Growth Worries"
  output:
    - label: POSITIVE
      score: 0.14
    - label: INDECISIVE
      score: 0.25
    - label: NEGATIVE
      score: 0.61
- text: "High inflation expectations becoming part of the American consumers behavioral norm"
  output:
    - label: POSITIVE
      score: 0.49
    - label: INDECISIVE
      score: 0.30
    - label: NEGATIVE
      score: 0.21
datasets:
- FinBERT_market_based/autotrain-data
---

# Model Card for Finetuned FinBERT on Market-Based Facts

**<font color="orange">This LLM is fine-tuned on market reactions to events. By utilizing market-based data, it avoids human biases present in traditional annotation methods.</font>**

Our FinBERT model, finetuned on impactful news headlines about global equity markets, has shown significant performance improvements over standard models. 
Its training on real-world market impact rather than subjective financial expert opinions sets a new standard for unbiased financial sentiment analysis. 📈
The dataset is uploaded on HuggingFace [here](https://huggingface.co/datasets/baptle/financial_headlines_market_based).

**Outperforms FinBERT**
- 🎯 +25% precision
- 🚀 +18% recall

**Outperforms DistilRoBERTa finetuned for finance**
- 🎯 +22% precision
- 🚀 +15% recall

**Outperforms GPT-4 zero-shot learning**
- 🎯 +15% precision
- 🚀 +8.2% recall


## Validation Metrics

| Metric             | Value                 |
|--------------------|-----------------------|
| loss               | 0.9176467061042786    |
| f1_macro           | 0.49749240436690023   |
| f1_micro           | 0.5627105467737756    |
| f1_weighted        | 0.5279720746084178    |
| precision_macro    | 0.5386355574899088    |
| precision_micro    | 0.5627105467737756    |
| precision_weighted | 0.5462149036191247    |
| recall_macro       | 0.517542664344306     |
| recall_micro       | 0.5627105467737756    |
| recall_weighted    | 0.5627105467737756    |
| accuracy           | 0.5627105467737756    |

This model has been developed after publishing in the Risk Forum 2024 conference a paper that can be found here (https://arxiv.org/abs/2401.05447). The FinMarBa dataset can be found here (https://arxiv.org/abs/2507.22932).


