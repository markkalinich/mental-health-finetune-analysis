---
base_model:
- microsoft/mdeberta-v3-base
library_name: transformers
license: cc-by-4.0
metrics:
- accuracy
- f1
tags:
- generated_from_trainer
- subjectivity-detection
- multilingual
- sentiment
- news
- mdeberta-v3
language:
- ar
- de
- en
- it
- bg
- el
- pl
- ro
- uk
datasets:
- MatteoFasulo/clef2025_checkthat_task1_subjectivity
pipeline_tag: text-classification
model-index:
- name: mdeberta-v3-base-subjectivity-sentiment-multilingual
  results: []
---

# mdeberta-v3-base-subjectivity-sentiment-multilingual

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the [CheckThat! Lab Task 1 Subjectivity Detection at CLEF 2025](https://arxiv.org/abs/2507.11764).

The official code repository can be found here: [https://github.com/MatteoFasulo/clef2025-checkthat](https://github.com/MatteoFasulo/clef2025-checkthat)
Explore related models and results on the Hugging Face Collection: [AI Wizards @ CLEF 2025 - CheckThat! Lab - Task 1 Subjectivity](https://huggingface.co/collections/MatteoFasulo/clef-2025-checkthat-lab-task-1-subjectivity-6878f0199d302acdfe2ceddb)

It achieves the following results on the evaluation set:
- Loss: 0.7762
- Macro F1: 0.7580
- Macro P: 0.7558
- Macro R: 0.7614
- Subj F1: 0.7100
- Subj P: 0.6878
- Subj R: 0.7336
- Accuracy: 0.7676

## Model description

This model, `mdeberta-v3-base-subjectivity-sentiment-multilingual`, is part of the AI Wizards' participation in the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles. Its primary goal is to classify sentences as subjective (opinion-laden) or objective across monolingual, multilingual, and zero-shot settings. The model was evaluated on various languages including Arabic, German, English, Italian, Bulgarian (training/development) and unseen languages like Greek, Romanian, Polish, and Ukrainian (zero-shot evaluation).

The core innovation of this approach lies in enhancing transformer-based classifiers by integrating sentiment scores, derived from an auxiliary model, with sentence representations. This sentiment-augmented architecture aims to improve upon standard fine-tuning, particularly boosting the subjective F1 score. To address class imbalance, prevalent across languages, decision threshold calibration optimized on the development set was employed.

Key contributions from the associated paper include:
*   **Sentiment-Augmented Fine-Tuning**: Enriching typical embedding-based models by integrating sentiment scores, significantly improving subjective sentence detection.
*   **Diverse Model Coverage**: Benchmarking `mDeBERTaV3-base` (multilingual), `ModernBERT-base` (English), and `Llama3.2-1B` (zero-shot LLM baseline).
*   **Threshold Calibration for Imbalance**: A simple yet effective method to tune decision thresholds on each language’s development data to enhance macro-F1 performance.

The framework led to high rankings, notably 1st for Greek (Macro F1 = 0.51).

## Intended uses & limitations

This model is intended for subjectivity detection in news articles, classifying sentences as subjective or objective. This task is crucial for combating misinformation, improving fact-checking pipelines, and supporting journalists. It is designed to be applicable in both monolingual and multilingual contexts, demonstrating robust generalization capabilities to unseen languages in zero-shot settings.

**Intended uses:**
*   Classifying sentences in news articles as subjective or objective.
*   As a component in misinformation detection and fact-checking systems.
*   Assisting journalists in analyzing news content for bias or opinion.

**Limitations:**
*   As noted by the authors, an initial mistake in the submission process led to some lower official multilingual Macro F1 scores (e.g., 0.24). Corrected results indicate significantly better performance (Macro F1 = 0.68), which would have placed the model higher (9th overall). Users should be aware of the corrected performance metrics.
*   Performance may vary across different languages and specific domains beyond news articles, although the model showed strong generalization in zero-shot settings.

## Training and evaluation data

The model was fine-tuned on datasets provided for the CLEF 2025 CheckThat! Lab Task 1: Subjectivity Detection in News Articles.
Training and development datasets were provided for Arabic, German, English, Italian, and Bulgarian. For final evaluation, additional unseen languages such as Greek, Romanian, Polish, and Ukrainian were included to assess generalization capabilities. The training procedure involved integrating sentiment features and applying decision threshold calibration, optimized on the development sets, to mitigate class imbalance.

## How to use

You can use this model directly with the Hugging Face `transformers` library to classify text:

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

model_name = "MatteoFasulo/mdeberta-v3-base-subjectivity-sentiment-multilingual"
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
    "The company reported a 10% increase in revenue for the last quarter.",
    "Die angegebenen Fehlerquoten können daher nur für symptomatische Patienten gelten.",
    "Si smonta qui definitivamente la narrazione per cui le scelte energetiche possono essere frutto esclusivo di valutazioni “tecniche” e non politiche.",
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
| No log        | 1.0   | 402  | 0.5154          | 0.6964   | 0.7341  | 0.7337  | 0.6969  | 0.5685 | 0.9001 | 0.6964   |
| 0.6027        | 2.0   | 804  | 0.5061          | 0.7264   | 0.7402  | 0.7508  | 0.7086  | 0.6055 | 0.8539 | 0.7276   |
| 0.4707        | 3.0   | 1206 | 0.6328          | 0.7387   | 0.7389  | 0.7511  | 0.7036  | 0.6373 | 0.7852 | 0.7434   |
| 0.3996        | 4.0   | 1608 | 0.7000          | 0.7519   | 0.7556  | 0.7492  | 0.6903  | 0.7128 | 0.6692 | 0.7672   |
| 0.3579        | 5.0   | 2010 | 0.7443          | 0.7476   | 0.7485  | 0.7614  | 0.7154  | 0.6440 | 0.8045 | 0.7518   |
| 0.3579        | 6.0   | 2412 | 0.7762          | 0.7580   | 0.7558  | 0.7614  | 0.7100  | 0.6878 | 0.7336 | 0.7676   |

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