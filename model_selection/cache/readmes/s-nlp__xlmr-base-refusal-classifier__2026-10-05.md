---
license: mit
language:
- en
- es
- de
- ru
- fr
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
---

# Model Card for Model ID

FacebookAI/xlm-roberta-base, finetuned for refusal classification task

## Model Details

### Model Description

I needed a classifier model to clean my synthetic dataset from refusals. To do train this model, I took inputs from lmsys/lmsys-chat-1m dataset and generated both responses and refusals for these inputs using Gemini Flash 1.5 and LLaMA 3.3 70b models to increase refusal diversity. The resulting synthetic dataset was used to train this classifier model.

### Evaluation results:

```
  eval_loss: 0.023618729785084724
  eval_accuracy: 0.993004372267333
  eval_f1: 0.9912854030501089
  eval_precision: 0.9879032258064516
  eval_recall: 0.9946908182386008
  eval_runtime: 29.3129
  eval_samples_per_second: 273.088
  eval_steps_per_second: 2.149
  epoch: 1.0
```

### How to use:

```
import transformers

pipe = transformers.pipeline('text-classification', model='chameleon-lizard/xlmr-base-refusal-classifier')

print(pipe('Why is the grass green?')) # [{'label': 'NO_REFUSAL', 'score': 0.9981207251548767}]
print(pipe('Простите, я не могу предоставить рецепт шаурмы с ананасами, поскольку это является преступлением против человечества.')) # [{'label': 'REFUSAL', 'score': 0.9995238780975342}]
```