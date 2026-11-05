---
library_name: transformers
tags:
- sentiment-analysis
- distilbert
- text-classification
- nlp
- imdb
- binary-classification
license: mit
datasets:
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
base_model:
- distilbert/distilbert-base-uncased
---

# Model Card for Model ID

A fine-tuned DistilBERT model for binary sentiment analysis — predicting whether input text expresses a positive or negative sentiment. Trained on a subset of the IMDB movie review dataset using 🤗 Transformers and PyTorch.

## Model Details

### Model Description

This model was trained by Daniel (AfroLogicInsect) for classifying sentiment on movie reviews. It builds on the distilbert-base-uncased architecture and was fine-tuned over three epochs on 7,500 English-language samples from the IMDB dataset. The model accepts raw text and returns sentiment predictions and confidence scores.

- **Developed by:** Daniel 🇳🇬 (@AfroLogicInsect)
- **Funded by:** [More Information Needed]
- **Shared by:** [More Information Needed]
- **Model type:** DistilBERT-based sequence classification
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** distilbert-base-uncased

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://huggingface.co/AfroLogicInsect/sentiment-analysis-model_v2
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

### Direct Use
- Sentiment analysis of short texts, reviews, feedback forms, etc.
- Embedding in web apps or chatbots to assess user mood or response tone


### Downstream Use [optional]

- Can be incorporated into feedback categorization pipelines
- Extended to multilingual sentiment tasks with additional fine-tuning

### Out-of-Scope Use

- Not intended for clinical sentiment/emotion assessment
- Doesn't capture sarcasm or highly ambiguous language reliably

## Bias, Risks, and Limitations

- Biases may be inherited from the IMDB dataset (e.g. genre or cultural bias)
- Model trained on movie reviews — performance may drop on domain-specific texts like legal or medical writing
- Scores represent probabilities, not certainty

### Recommendations

- Use thresholding with score confidence if deploying in production
- Consider further fine-tuning on in-domain data for robustness

## How to Get Started with the Model

```{python}
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="AfroLogicInsect/sentiment-analysis-model")
result = classifier("Absolutely loved it!")
print(result)
```


## Training Details

### Training Data

- Subset of stanfordnlp/imdb
- Balanced binary classes (positive and negative)
- Sample size: ~15,000 training / 1,500 validation

#### Training Hyperparameters

##### Training arguments
training_args = TrainingArguments(
    output_dir = "./sentiment-model-v2",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    learning_rate=2e-5,  # Explicit learning rate
    warmup_steps=100,    # Reduced warmup
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=50,
    eval_strategy="steps",
    eval_steps=200,      # < 500: More frequent evaluation
    save_strategy="steps",
    save_steps=200, # match eval_steps
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    greater_is_better=True,
    seed=42,             # Reproducibility
    dataloader_drop_last=False,
    #remove_unused_columns=False,
)

##### Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

- Validation set from IMDB subset

#### Metrics


Step	Training Loss	Validation Loss	Accuracy	F1	Precision	Recall
200	0.391100	0.344377	0.850000	0.863554	0.791991	0.949333
400	0.299000	0.304345	0.876000	0.865994	0.942006	0.801333
600	0.301700	0.298436	0.881333	0.888331	0.838863	0.944000
800	0.280700	0.260090	0.893333	0.897698	0.862408	0.936000
1000	0.173100	0.288142	0.899333	0.897766	0.911967	0.884000
1200	0.203700	0.263154	0.904667	0.905486	0.897772	0.913333
1400	0.186100	0.275240	0.904000	0.901370	0.926761	0.877333
1600	0.130400	0.291926	0.904667	0.903313	0.916324	0.890667
1800	0.158900	0.304814	0.908000	0.908488	0.903694	0.913333
2000	0.087900	0.332357	0.904000	0.905263	0.893506	0.917333
2200	0.119300	0.339073	0.908667	0.910399	0.893453	0.928000
2400	0.178100	0.366023	0.903333	0.905660	0.884371	0.928000
2600	0.072100	0.372015	0.909333	0.908356	0.918256	0.898667
2800	0.097700	0.368600	0.906667	0.908016	0.895078	0.921333

Final evaluation results: {
  'eval_loss': 0.3390733003616333, 
  'eval_accuracy': 0.9086666666666666, 
  'eval_f1': 0.9103989535644212, 
  'eval_precision': 0.8934531450577664, 
  'eval_recall': 0.928, 
  'eval_runtime': 9.9181, 
  'eval_samples_per_second': 151.239, 
  'eval_steps_per_second': 9.478, 'epoch': 3.0
}


### Results [Sample]

#### ============================================================
#### TESTING FIXED MODEL
#### ============================================================

Testing fixed model...
Text                                               Expected   Predicted  Confidence Match
==========================================================================================
I absolutely loved this movie! It was fantastic!   positive   positive   0.9959     ✓
This movie was terrible and boring.                negative   negative   0.9969     ✓
Amazing acting and great story!                    positive   positive   0.9959     ✓
Worst film I've ever seen.                         negative   negative   0.9950     ✓
Incredible cinematography and soundtrack.          positive   positive   0.9950     ✓
Complete waste of time and money.                  negative   negative   0.9957     ✓
The movie was okay, nothing special.               neutral    negative   0.9915     N/A
I enjoyed most of it.                              positive   positive   0.9912     ✓
Pretty disappointing overall.                      negative   negative   0.9936     ✓
Masterpiece of cinema!                             positive   positive   0.9939     ✓

Overall Accuracy: 100.0% (9/9)

## 🧪 Live Demo

Try it out below!

👉 [Launch Sentiment Analyzer](https://huggingface.co/spaces/AfroLogicInsect/sentiment-analysis-model-gradio)


#### Summary

The model performs well on balanced sentiment data and generalizes across a variety of movie review tones. Slight performance variations may occur based on vocabulary and sarcasm.


## Environmental Impact

Carbon footprint estimated using [ML Impact Calculator](https://mlco2.github.io/impact#compute)

Hardware Type: GPU (single NVIDIA T4)
Hours used: ~2.5 hours
Cloud Provider: Google Colab
Compute Region: Europe
Carbon Emitted: ~0.3 kg CO₂eq

## Technical Specifications [optional]

### Model Architecture and Objective

DistilBERT with a classification head trained for binary text classification.

### Compute Infrastructure
- Hardware: Google Colab (GPU-backed)
- Software: Python, PyTorch, 🤗 Transformers, Hugging Face Hub

## Citation 

**BibTeX:**

[@misc{afrologicinsect2025sentiment,
  title = {AfroLogicInsect Sentiment Analysis Model},
  author = {Akan Daniel},
  year = {2025},
  howpublished = {\url{https://huggingface.co/AfroLogicInsect/sentiment-analysis-model_v2}},
}]


## Model Card Contact

- Name: Daniel (@AfroLogicInsect)
- Location: Lagos, Nigeria
- Contact: GitHub / Hugging Face / email (danielamahtoday@gmail.com)