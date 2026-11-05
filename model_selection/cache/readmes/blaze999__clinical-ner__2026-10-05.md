---
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: clinical-ner
  results: []

widget:
- text: "63 year old woman with history of CAD presented to ER"
  example_title: "Example-1"
- text: "63 year old woman diagnosed with CAD"
  example_title: "Example-2"
- text: "A 48 year-old female presented with vaginal bleeding and abnormal Pap smears.
Upon diagnosis of invasive non-keratinizing SCC of the cervix, she underwent a radical hysterectomy with salpingo-oophorectomy which demonstrated positive spread to the pelvic lymph nodes and the parametrium.
Pathological examination revealed that the tumour also extensively involved the lower uterine segment."
  example_title: "example 3"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-ner

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8058
- Precision: 0.5786
- Recall: 0.6683
- F1: 0.6202
- Accuracy: 0.8099

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 45
- mixed_precision_training: Native AMP

### Python Code:
```python
# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("token-classification", model="blaze999/clinical-ner", aggregation_strategy='simple')
result = pipe('45 year old woman diagnosed with CAD')



# Load model directly
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("blaze999/clinical-ner")
model = AutoModelForTokenClassification.from_pretrained("blaze999/clinical-ner")
```

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 5    | 4.7713          | 0.0002    | 0.001  | 0.0004 | 0.0182   |
| No log        | 2.0   | 10   | 4.2264          | 0.0002    | 0.0008 | 0.0003 | 0.1481   |
| No log        | 3.0   | 15   | 3.6238          | 0.0004    | 0.0003 | 0.0003 | 0.4575   |
| 4.2324        | 4.0   | 20   | 2.8751          | 0.0       | 0.0    | 0.0    | 0.4734   |
| 4.2324        | 5.0   | 25   | 2.4550          | 0.0306    | 0.0008 | 0.0015 | 0.4739   |
| 4.2324        | 6.0   | 30   | 2.1920          | 0.0722    | 0.0437 | 0.0545 | 0.5007   |
| 4.2324        | 7.0   | 35   | 1.9841          | 0.1137    | 0.1087 | 0.1112 | 0.5392   |
| 2.3521        | 8.0   | 40   | 1.8153          | 0.1956    | 0.189  | 0.1922 | 0.5829   |
| 2.3521        | 9.0   | 45   | 1.6504          | 0.2539    | 0.2617 | 0.2578 | 0.6218   |
| 2.3521        | 10.0  | 50   | 1.4801          | 0.3607    | 0.3787 | 0.3695 | 0.6782   |
| 2.3521        | 11.0  | 55   | 1.3417          | 0.3933    | 0.433  | 0.4122 | 0.7021   |
| 1.6185        | 12.0  | 60   | 1.2333          | 0.4054    | 0.4795 | 0.4394 | 0.7203   |
| 1.6185        | 13.0  | 65   | 1.1490          | 0.4307    | 0.5125 | 0.4680 | 0.7347   |
| 1.6185        | 14.0  | 70   | 1.0750          | 0.4412    | 0.543  | 0.4868 | 0.7503   |
| 1.6185        | 15.0  | 75   | 1.0179          | 0.4816    | 0.5637 | 0.5195 | 0.7619   |
| 1.1438        | 16.0  | 80   | 0.9774          | 0.4899    | 0.578  | 0.5303 | 0.7689   |
| 1.1438        | 17.0  | 85   | 0.9475          | 0.5005    | 0.5955 | 0.5439 | 0.7743   |
| 1.1438        | 18.0  | 90   | 0.9192          | 0.5082    | 0.6078 | 0.5535 | 0.7788   |
| 1.1438        | 19.0  | 95   | 0.8923          | 0.5151    | 0.6085 | 0.5579 | 0.7828   |
| 0.8863        | 20.0  | 100  | 0.8691          | 0.5263    | 0.6242 | 0.5711 | 0.7882   |
| 0.8863        | 21.0  | 105  | 0.8604          | 0.5358    | 0.6342 | 0.5809 | 0.7907   |
| 0.8863        | 22.0  | 110  | 0.8474          | 0.5429    | 0.641  | 0.5879 | 0.7946   |
| 0.8863        | 23.0  | 115  | 0.8362          | 0.5493    | 0.644  | 0.5929 | 0.7969   |
| 0.7361        | 24.0  | 120  | 0.8284          | 0.5531    | 0.6512 | 0.5982 | 0.7994   |
| 0.7361        | 25.0  | 125  | 0.8325          | 0.5555    | 0.6565 | 0.6018 | 0.8001   |
| 0.7361        | 26.0  | 130  | 0.8156          | 0.5686    | 0.6562 | 0.6093 | 0.8035   |
| 0.7361        | 27.0  | 135  | 0.8177          | 0.5634    | 0.6625 | 0.6089 | 0.8039   |
| 0.6449        | 28.0  | 140  | 0.8152          | 0.5643    | 0.6567 | 0.6070 | 0.8036   |
| 0.6449        | 29.0  | 145  | 0.8109          | 0.5700    | 0.6647 | 0.6137 | 0.8066   |
| 0.6449        | 30.0  | 150  | 0.8164          | 0.5697    | 0.6653 | 0.6138 | 0.8055   |
| 0.6449        | 31.0  | 155  | 0.8081          | 0.5742    | 0.6627 | 0.6153 | 0.8085   |
| 0.5912        | 32.0  | 160  | 0.8130          | 0.5687    | 0.6677 | 0.6142 | 0.8067   |
| 0.5912        | 33.0  | 165  | 0.8048          | 0.5779    | 0.6637 | 0.6179 | 0.8089   |
| 0.5912        | 34.0  | 170  | 0.8096          | 0.5760    | 0.669  | 0.6190 | 0.8085   |
| 0.5912        | 35.0  | 175  | 0.8063          | 0.5790    | 0.6677 | 0.6202 | 0.8091   |
| 0.5625        | 36.0  | 180  | 0.8052          | 0.5755    | 0.6673 | 0.6180 | 0.8094   |
| 0.5625        | 37.0  | 185  | 0.8063          | 0.5753    | 0.6667 | 0.6176 | 0.8093   |
| 0.5625        | 38.0  | 190  | 0.8055          | 0.5783    | 0.6677 | 0.6198 | 0.8103   |
| 0.5625        | 39.0  | 195  | 0.8052          | 0.5792    | 0.668  | 0.6205 | 0.8099   |
| 0.5442        | 40.0  | 200  | 0.8052          | 0.5798    | 0.6685 | 0.6210 | 0.8097   |
| 0.5442        | 41.0  | 205  | 0.8055          | 0.5784    | 0.6683 | 0.6201 | 0.8098   |
| 0.5442        | 42.0  | 210  | 0.8056          | 0.5789    | 0.6685 | 0.6205 | 0.8100   |
| 0.5442        | 43.0  | 215  | 0.8057          | 0.5786    | 0.6683 | 0.6202 | 0.8100   |
| 0.5397        | 44.0  | 220  | 0.8057          | 0.5786    | 0.6683 | 0.6202 | 0.8099   |
| 0.5397        | 45.0  | 225  | 0.8058          | 0.5786    | 0.6683 | 0.6202 | 0.8099   |


### Framework versions

- Transformers 4.37.0
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.1
