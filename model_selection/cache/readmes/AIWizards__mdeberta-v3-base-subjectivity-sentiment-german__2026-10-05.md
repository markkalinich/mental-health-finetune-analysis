---
base_model:
- microsoft/mdeberta-v3-base
language:
- de
library_name: transformers
license: cc-by-4.0
metrics:
- accuracy
- f1
pipeline_tag: text-classification
tags:
- generated_from_trainer
- subjectivity
- sentiment
- multilingual
- zero-shot
- deberta-v3
model-index:
- name: mdeberta-v3-base-subjectivity-sentiment-german
  results: []
datasets:
- MatteoFasulo/clef2025_checkthat_task1_subjectivity
---

# mdeberta-v3-base-subjectivity-sentiment-german

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the [CheckThat! Lab Task 1 Subjectivity Detection at CLEF 2025](https://arxiv.org/abs/2507.11764).
It achieves the following results on the evaluation set:
- Loss: 0.5653
- Macro F1: 0.7777
- Macro P: 0.7751
- Macro R: 0.7811
- Subj F1: 0.7171
- Subj P: 0.6995
- Subj R: 0.7356
- Accuracy: 0.7943

The full code and materials for this project are available on the [GitHub repository](https://github.com/MatteoFasulo/clef2025-checkthat).
You can also explore related models and interactive demos on the [AI Wizards @ CLEF 2025 - CheckThat! Lab - Task 1 Subjectivity collection on Hugging Face Hub](https://huggingface.co/collections/MatteoFasulo/clef-2025-checkthat-lab-task-1-subjectivity-6878f0199d302acdfe2ceddb).

## Model description

This model identifies whether a sentence is **subjective** (e.g., opinion-laden) or **objective**. It was developed as part of AI Wizards' participation in the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles.

The primary strategy employed enhances transformer-based classifiers by integrating sentiment scores, derived from an auxiliary model, with sentence representations. This approach aims to improve upon standard fine-tuning, especially boosting the subjective F1 score. This sentiment-augmented architecture was explored with `mDeBERTaV3-base` (the base for this model), ModernBERT-base (English), and Llama3.2-1B. To address class imbalance, prevalent across languages, decision threshold calibration optimized on the development set was employed.

## Intended uses & limitations

This model is intended for classifying the subjectivity of sentences in news articles. It serves as a key component in combating misinformation, improving fact-checking pipelines, and supporting journalists by helping to distinguish facts from opinions.

**Intended Uses:**
*   Classifying sentences in news articles as subjective or objective.
*   Supporting information veracity analysis and fact-checking processes.
*   Aiding journalistic workflows in content assessment.

**Limitations:**
*   While designed for multilingual and zero-shot settings, performance may vary across languages, especially those not explicitly included in the training datasets.
*   The effectiveness relies on the quality of the sentiment scores derived from the auxiliary model.
*   Tuned specifically for subjectivity detection in news articles; performance on other text domains or tasks may not be optimal without further fine-tuning.

## Training and evaluation data

This model was trained and evaluated as part of the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles.

Training and development datasets were provided for Arabic, German, English, Italian, and Bulgarian. The final evaluation included additional unseen languages such as Greek, Romanian, Polish, and Ukrainian to assess the model's generalization capabilities.

The training process incorporated decision threshold calibration to address class imbalance issues prevalent across these language datasets, optimizing performance on the development set.

## How to use

You can use this model for text classification with the `transformers` library:

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

model_name = "MatteoFasulo/mdeberta-v3-base-subjectivity-sentiment-german"
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
    "Die angegebenen Fehlerquoten können daher nur für symptomatische Patienten gelten.",
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
| No log        | 1.0   | 50   | 0.6675          | 0.5751   | 0.7423  | 0.5934  | 0.3423  | 0.7917 | 0.2184 | 0.7026   |
| No log        | 2.0   | 100  | 0.5013          | 0.7711   | 0.7663  | 0.7810  | 0.7166  | 0.67   | 0.7701 | 0.7841   |
| No log        | 3.0   | 150  | 0.4989          | 0.7812   | 0.7763  | 0.7901  | 0.7278  | 0.6853 | 0.7759 | 0.7943   |
| No log        | 4.0   | 200  | 0.5322          | 0.7744   | 0.7787  | 0.7710  | 0.7041  | 0.7256 | 0.6839 | 0.7963   |
| No log        | 5.0   | 250  | 0.5520          | 0.7813   | 0.7821  | 0.7806  | 0.7168  | 0.7209 | 0.7126 | 0.8004   |
| No log        | 6.0   | 300  | 0.5653          | 0.7777   | 0.7751  | 0.7811  | 0.7171  | 0.6995 | 0.7356 | 0.7943   |

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