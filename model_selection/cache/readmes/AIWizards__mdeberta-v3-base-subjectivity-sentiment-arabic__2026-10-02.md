---
base_model:
- microsoft/mdeberta-v3-base
language:
- ar
library_name: transformers
license: cc-by-4.0
metrics:
- accuracy
- f1
paper: 2507.11764
pipeline_tag: text-classification
tags:
- generated_from_trainer
- subjectivity-detection
- sentiment-analysis
- multilingual
- deberta-v3
model-index:
- name: mdeberta-v3-base-subjectivity-sentiment-arabic
  results: []
datasets:
- MatteoFasulo/clef2025_checkthat_task1_subjectivity
---

# mdeberta-v3-base-subjectivity-sentiment-arabic

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the [CheckThat! Lab Task 1 Subjectivity Detection at CLEF 2025](https://huggingface.co/papers/2507.11764).

It achieves the following results on the evaluation set:
- Loss: 0.7442
- Macro F1: 0.5426
- Macro P: 0.5472
- Macro R: 0.5442
- Subj F1: 0.4457
- Subj P: 0.4910
- Subj R: 0.4080
- Accuracy: 0.5632

## GitHub Repository
The official code and materials for this work are available on GitHub: [MatteoFasulo/clef2025-checkthat](https://github.com/MatteoFasulo/clef2025-checkthat)

## Model description

This model is part of AI Wizards' participation in the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles. Its primary goal is to classify sentences as subjective (opinion-laden) or objective across monolingual, multilingual, and zero-shot settings.

The core innovation of this model lies in enhancing transformer-based classifiers by integrating sentiment scores, derived from an auxiliary model, with sentence representations. This sentiment-augmented architecture, explored with mDeBERTaV3-base, aims to significantly improve performance, particularly the subjective F1 score. To address class imbalance, prevalent across languages, the framework employs decision threshold calibration optimized on the development set. This approach led to high rankings, notably 1st for Greek (Macro F1 = 0.51).

**Key Contributions:**
*   **Sentiment-Augmented Fine-Tuning**: Enriches typical embedding-based models by integrating sentiment scores, significantly improving subjective sentence detection.
*   **Diverse Model Coverage**: Evaluated across multilingual BERT variants, ModernBERT (English-focused), and Llama 3.2-1B (zero-shot LLM baseline).
*   **Threshold Calibration for Imbalance**: A simple yet effective method to tune decision thresholds on each language’s dev data to enhance macro-F1 performance.

## Intended uses & limitations

**Intended Uses:**
This model is intended for subjectivity detection in news articles, classifying sentences as subjective or objective. It can be applied to tasks such as:
*   Combating misinformation by identifying opinion-laden content.
*   Improving fact-checking pipelines.
*   Supporting journalists in content analysis.
*   Performing subjectivity detection in monolingual (Arabic, German, English, Italian, Bulgarian), multilingual, and zero-shot (Greek, Polish, Romanian, Ukrainian) settings.

**Limitations:**
*   The model's performance might vary across different languages, especially in zero-shot scenarios.
*   As noted in the paper, initial submission errors highlighted the sensitivity to correct data splits and calibration, which can impact reported performance.
*   The effectiveness of sentiment feature integration is dependent on the quality and relevance of the auxiliary sentiment model.

## Training and evaluation data

This model was fine-tuned on datasets provided for the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles. Training and development datasets were provided for Arabic, German, English, Italian, and Bulgarian. For final evaluation, additional unseen languages such as Greek, Romanian, Polish, and Ukrainian were included to assess the model's generalization capabilities. The datasets were designed for classifying sentences as subjective or objective within news articles.

## How to use

You can use this model directly with the Hugging Face `transformers` library for text classification.

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

model_name = "MatteoFasulo/mdeberta-v3-base-subjectivity-sentiment-arabic"
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
    "ستشمل الشحنة الأولية نصف الجرعات، يليها النصف الثاني بعد ثلاثة أسابيع.",
    "وهكذا بدأت النساء يعين أهمية دورهن في عدم الصمت أمام هذه الاقتحامات ورفضها بإعلاء صيحات الله أكبر.",
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
| No log        | 1.0   | 153  | 0.6885          | 0.5224   | 0.5299  | 0.5268  | 0.4068  | 0.4706 | 0.3582 | 0.5503   |
| No log        | 2.0   | 306  | 0.6932          | 0.5204   | 0.5602  | 0.5416  | 0.3510  | 0.5248 | 0.2637 | 0.5803   |
| No log        | 3.0   | 459  | 0.6928          | 0.5480   | 0.5748  | 0.5589  | 0.4087  | 0.5410 | 0.3284 | 0.5910   |
| 0.6721        | 4.0   | 612  | 0.7125          | 0.5485   | 0.5492  | 0.5500  | 0.5059  | 0.4820 | 0.5323 | 0.5525   |
| 0.6721        | 5.0   | 765  | 0.7238          | 0.5220   | 0.5667  | 0.5448  | 0.3490  | 0.5361 | 0.2587 | 0.5846   |
| 0.6721        | 6.0   | 918  | 0.7442          | 0.5426   | 0.5472  | 0.5442  | 0.4457  | 0.4910 | 0.4080 | 0.5632   |

### Framework versions

- Transformers 4.49.0
- Pytorch 2.5.1+cu121
- Datasets 3.3.1
- Tokenizers 0.21.0

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