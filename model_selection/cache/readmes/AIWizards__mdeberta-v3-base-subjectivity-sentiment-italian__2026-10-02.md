---
base_model:
- microsoft/mdeberta-v3-base
language:
- it
library_name: transformers
license: cc-by-4.0
metrics:
- accuracy
- f1
tags:
- generated_from_trainer
- deberta-v2
- subjectivity-detection
- sentiment-analysis
pipeline_tag: text-classification
model-index:
- name: mdeberta-v3-base-subjectivity-sentiment-italian
  results: []
datasets:
- MatteoFasulo/clef2025_checkthat_task1_subjectivity
---

# mdeberta-v3-base-subjectivity-sentiment-italian

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the [CheckThat! Lab Task 1 Subjectivity Detection at CLEF 2025](https://arxiv.org/abs/2507.11764).
For the official code and materials, please refer to the [GitHub repository](https://github.com/MatteoFasulo/clef2025-checkthat).

It achieves the following results on the evaluation set:
- Loss: 0.6602
- Macro F1: 0.7437
- Macro P: 0.7322
- Macro R: 0.7690
- Subj F1: 0.6437
- Subj P: 0.5696
- Subj R: 0.7401
- Accuracy: 0.7826

## Model description

This model, `mdeberta-v3-base-subjectivity-sentiment-italian`, is part of the AI Wizards' submission to the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles. Its primary goal is to classify sentences as subjective or objective. A key innovation in its development involved enhancing transformer-based classifiers, specifically `mDeBERTaV3-base`, by integrating sentiment scores derived from an auxiliary model with sentence representations. This sentiment-augmented architecture, combined with decision threshold calibration to address class imbalance, consistently boosted performance, especially the subjective F1 score.

## Intended uses & limitations

This model is intended for identifying whether a sentence is subjective (opinion-laden) or objective in news articles, which is crucial for combating misinformation, improving fact-checking pipelines, and supporting journalists. It has been evaluated in monolingual (Italian, Arabic, German, English, Bulgarian), zero-shot (Greek, Polish, Romanian, Ukrainian), and multilingual settings. While the sentiment augmentation consistently improved performance, users should be aware that the model's effectiveness may vary across languages and specific domains not covered in the training data. The model was trained with specific hyperparameters and decision threshold calibration for class imbalance, which are critical for its reported performance.

## Training and evaluation data

More information needed

## How to use

You can use this model with the `transformers` library for text classification:

```python
import torch
import torch.nn as nn
from transformers import DebertaV2Model, DebertaV2Config, AutoTokenizer, PreTrainedModel, pipeline, AutoModelForSequenceClassification 
from transformers.models.deberta.modeling_deberta import ContextPooler

sent_pipe = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    tokenizer="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    top_k=None,  # return all 3 sentiment scores
)

class CustomModel(PreTrainedModel):
    config_class = DebertaV2Config
    def __init__(self, config, sentiment_dim=3, num_labels=2, *args, **kwargs):
        super().__init__(config, *args, **kwargs)
        self.deberta = DebertaV2Model(config)
        self.pooler = ContextPooler(config)
        output_dim = self.pooler.output_dim
        self.dropout = nn.Dropout(0.1)
        self.classifier = nn.Linear(output_dim + sentiment_dim, num_labels)

    def forward(self, input_ids, positive, neutral, negative, token_type_ids=None, attention_mask=None, labels=None):
        outputs = self.deberta(input_ids=input_ids, attention_mask=attention_mask)
        encoder_layer = outputs[0]
        pooled_output = self.pooler(encoder_layer)
        sentiment_features = torch.stack((positive, neutral, negative), dim=1).to(pooled_output.dtype)
        combined_features = torch.cat((pooled_output, sentiment_features), dim=1)
        logits = self.classifier(self.dropout(combined_features))
        return {'logits': logits}

model_name = "MatteoFasulo/mdeberta-v3-base-subjectivity-sentiment-italian"
tokenizer = AutoTokenizer.from_pretrained("microsoft/mdeberta-v3-base")
config = DebertaV2Config.from_pretrained(
    model_name, 
    num_labels=2, 
    id2label={0: 'OBJ', 1: 'SUBJ'}, 
    label2id={'OBJ': 0, 'SUBJ': 1},
    output_attentions=False, 
    output_hidden_states=False
)
model = CustomModel(config=config, sentiment_dim=3, num_labels=2).from_pretrained(model_name)

def classify_subjectivity(text: str):
    # get full sentiment distribution
    dist = sent_pipe(text)[0]
    pos = next(d["score"] for d in dist if d["label"] == "positive")
    neu = next(d["score"] for d in dist if d["label"] == "neutral")
    neg = next(d["score"] for d in dist if d["label"] == "negative")

    # tokenize the text
    inputs = tokenizer(text, padding=True, truncation=True, max_length=256, return_tensors='pt')

    # feeding in the three sentiment scores
    with torch.no_grad():
        outputs = model(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            positive=torch.tensor(pos).unsqueeze(0).float(),
            neutral=torch.tensor(neu).unsqueeze(0).float(),
            negative=torch.tensor(neg).unsqueeze(0).float()
        )

    # compute probabilities and pick the top label
    probs = torch.softmax(outputs.get('logits')[0], dim=-1)
    label = model.config.id2label[int(probs.argmax())]
    score = probs.max().item()

    return {"label": label, "score": score}

examples = [
    "Per quanto riguarda le motivazioni, è importante chiedersi se l’intervento è realmente mirato a risolvere un complesso, a modificare un aspetto del corpo con cui non si riesce a convivere serenamente, oppure se è frutto di una moda passeggera o dell’influenza tossica del web che spesso induce a volere cose di cui non si ha assolutamente bisogno.",
    "Un roulette di tensioni in cui alla fine spunta un match point per Sinner.",
]
for text in examples:
    result = classify_subjectivity(text)
    print(f"Text: {text}")
    print(f"→ Subjectivity: {result['label']} (score={result['score']:.2f})\n")
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Macro F1 | Macro P | Macro R | Subj F1 | Subj P | Subj R | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-------:|:-------:|:-------:|:------:|:------:|:--------:|
| No log        | 1.0   | 101  | 0.6392          | 0.7244   | 0.7284  | 0.7208  | 0.5913  | 0.6071 | 0.5763 | 0.7886   |
| No log        | 2.0   | 202  | 0.5375          | 0.6731   | 0.7018  | 0.7579  | 0.6064  | 0.4548 | 0.9096 | 0.6867   |
| No log        | 3.0   | 303  | 0.5731          | 0.7453   | 0.7373  | 0.7563  | 0.6349  | 0.5970 | 0.6780 | 0.7931   |
| No log        | 4.0   | 404  | 0.5788          | 0.7522   | 0.7405  | 0.7752  | 0.6534  | 0.5848 | 0.7401 | 0.7916   |
| 0.4395        | 5.0   | 505  | 0.6922          | 0.7491   | 0.7400  | 0.7628  | 0.6423  | 0.5971 | 0.6949 | 0.7946   |
| 0.4395        | 6.0   | 606  | 0.6602          | 0.7437   | 0.7322  | 0.7690  | 0.6437  | 0.5696 | 0.7401 | 0.7826   |


### Framework versions

- Transformers 4.49.0
- Pytorch 2.5.1+cu121
- Datasets 3.3.1
- Tokenizers 0.21.0

## Code

The official code and materials for this submission are available on GitHub:
[https://github.com/MatteoFasulo/clef2025-checkthat](https://github.com/MatteoFasulo/clef2025-checkthat)

## Citation

If you find our work helpful or inspiring, please feel free to cite it:

```bibtex
@misc{fasulo2025aiwizardscheckthat2025,
      title={AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles}, 
      author={Matteo Fasulo and Luca Babboni and Luca Tedeschini},
      year={2025},
      eprint={2507.11764},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.11764}, 
}
```