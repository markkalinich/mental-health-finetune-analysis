---
library_name: transformers
language:
- pl
license: mit
base_model: sdadas/polish-gpt2-small
tags:
- generated_from_trainer
- text-classification
- multi-class-classification
- multi-label-classification
- emotions
model-index:
- name: plutchik-emotions-polish-poc
  results: []
pipeline_tag: text-classification
---

# plutchik-emotions-polish-poc

This model is a fine-tuned version of [sdadas/polish-gpt2-small](https://huggingface.co/sdadas/polish-gpt2-small) on a synthetically annotated [WiktorS/polish-news](https://huggingface.co/datasets/WiktorS/polish-news) dataset.
It achieves the following results on the evaluation set:
Every list contains results for threshold [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
- Loss: 0.4958
- Hamming Accuracy: [0.8251, 0.8363, 0.8424, 0.8461, 0.8471, 0.848, 0.8464]
- F1 Macro: [0.5061, 0.4948, 0.4802, 0.4641, 0.4376, 0.4023, 0.3423]
- Precision Macro: [0.4873, 0.5201, 0.5486, 0.5752, 0.5986, 0.6279, 0.6586]
- Recall Macro: [0.5270, 0.4738, 0.4304, 0.3929, 0.3494, 0.3008, 0.2362]

## Model description

Trained from [sdadas/polish-gpt2-small](https://huggingface.co/sdadas/polish-gpt2-small) as a Proof of Concept.

## Intended uses & limitations

Detecting emotions described in [Robert_Plutchik#Theory_of_emotion](https://en.wikipedia.org/wiki/Robert_Plutchik#Theory_of_emotion)

Labels:
```
0: joy
1: trust
2: anticipation
3: surprise
4: fear
5: sadness
6: disgust
7: anger
```

### How to use

<details><summary>Transformers AutoModel</summary>

```py
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
checkpoint = "nie3e/plutchik-emotions-polish-poc"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(
    checkpoint, problem_type="multi_label_classification"
).to(device)

text = "To jest model wykrywający super emocje w tekście! :D"

input_ids = tokenizer(text, return_tensors="pt").to(device)
logits = model(**input_ids)["logits"].to("cpu")

threshold = 0.3
predicted_class_ids = torch.arange(
    0, logits.shape[-1]
)[torch.sigmoid(logits).squeeze(dim=0) > threshold]

percent = torch.sigmoid(logits).squeeze(dim=0)

id2class = model.config.id2label
print([id2class[c] for c in predicted_class_ids.tolist()])
print({id2class[i]: f"{(p*100):.2f}%" for i, p in enumerate(percent.tolist())})
```
```
['joy', 'anticipation']
{'joy': '91.15%', 'trust': '2.06%', 'anticipation': '61.14%', 'surprise': '23.00%', 'fear': '1.93%', 'sadness': '0.40%', 'disgust': '3.02%', 'anger': '2.54%'}
```

</details>

<details><summary>Transformers Pipeline</summary>

```py
from transformers import pipeline
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = pipeline(
    "text-classification",
    "nie3e/plutchik-emotions-polish-poc",
    top_k=-1,
    device=device
)
text = "To jest model wykrywający super emocje w tekście! :D"

result = pipe(text)
print(result)
```

```
[[{'label': 'joy', 'score': 0.9111796617507935}, {'label': 'anticipation', 'score': 0.6109178066253662}, {'label': 'surprise', 'score': 0.23231014609336853}, {'label': 'disgust', 'score': 0.030675798654556274}, {'label': 'anger', 'score': 0.025565214455127716}, {'label': 'trust', 'score': 0.02096424251794815}, {'label': 'fear', 'score': 0.019419347867369652}]]
```

</details>

<details><summary>vLLM OpenAI serving (recommended)</summary>

```bash
docker run --gpus 1 --ipc=host -p 8000:8000 vllm/vllm-openai:v0.9.2 --model nie3e/plutchik-emotions-polish-poc
```

using curl:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/classify' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "nie3e/plutchik-emotions-polish-poc",
  "input": ["To jest model wykrywający super emocje w tekście! :D"]
}'
```
result:
```json
{
	"id": "classify-2cea66aa49b84b239277ad8cdb8ad662",
	"object": "list",
	"created": 1756143116,
	"model": "nie3e/plutchik-emotions-polish-poc",
	"data": [
		{
			"index": 0,
			"label": "joy",
			"probs": [
				0.8406059741973877,
				0.0017006286652758718,
				0.12716063857078553,
				0.024033185094594957,
				0.0015728245489299298,
				0.00032968190498650074,
				0.0025133665185421707,
				0.002083654049783945
			],
			"num_classes": 8
		}
	],
	"usage": {
		"prompt_tokens": 12,
		"total_tokens": 12,
		"completion_tokens": 0,
		"prompt_tokens_details": null
	}
}
```

using python:
```py
import requests

response = requests.post(
    f"http://127.0.0.1:8000/classify",
    headers={"Content-Type": "application/json"},
    json={
        "model": "nie3e/plutchik-emotions-polish-poc",
        "input": ["To jest model wykrywający super emocje w tekście! :D"]
    }
)

print(response.json())
```
```
{'id': 'classify-003f1db547504a5398ee76907f6f5e30',
 'object': 'list',
 'created': 1756143205,
 'model': 'nie3e/plutchik-emotions-polish-poc',
 'data': [{'index': 0,
   'label': 'joy',
   'probs': [0.8406059741973877,
    0.0017006286652758718,
    0.12716063857078552,
    0.024033185094594955,
    0.0015728245489299297,
    0.00032968190498650074,
    0.0025133665185421705,
    0.002083654049783945],
   'num_classes': 8}],
 'usage': {'prompt_tokens': 12,
  'total_tokens': 12,
  'completion_tokens': 0,
  'prompt_tokens_details': None}}
```

</details>

## Training and evaluation data

Dataset: [WiktorS/polish-news](https://huggingface.co/datasets/WiktorS/polish-news)

LLM used for annotation: [bartowski/mistralai_Mistral-Small-3.2-24B-Instruct-2506-GGUF Q8](https://huggingface.co/bartowski/mistralai_Mistral-Small-3.2-24B-Instruct-2506-GGUF)

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 2
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- total_eval_batch_size: 8
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Hamming Accuracy 0.30 | F1 Macro 0.30 | Precision Macro 0.30 | Recall Macro 0.30 | Hamming Accuracy 0.40 | F1 Macro 0.40 | Precision Macro 0.40 | Recall Macro 0.40 | Hamming Accuracy 0.50 | F1 Macro 0.50 | Precision Macro 0.50 | Recall Macro 0.50 | Hamming Accuracy 0.60 | F1 Macro 0.60 | Precision Macro 0.60 | Recall Macro 0.60 | Hamming Accuracy 0.70 | F1 Macro 0.70 | Precision Macro 0.70 | Recall Macro 0.70 | Hamming Accuracy 0.80 | F1 Macro 0.80 | Precision Macro 0.80 | Recall Macro 0.80 | Hamming Accuracy 0.90 | F1 Macro 0.90 | Precision Macro 0.90 | Recall Macro 0.90 |
|:-------------:|:-----:|:-----:|:---------------:|:---------------------:|:-------------:|:--------------------:|:-----------------:|:---------------------:|:-------------:|:--------------------:|:-----------------:|:---------------------:|:-------------:|:--------------------:|:-----------------:|:---------------------:|:-------------:|:--------------------:|:-----------------:|:---------------------:|:-------------:|:--------------------:|:-----------------:|:---------------------:|:-------------:|:--------------------:|:-----------------:|:---------------------:|:-------------:|:--------------------:|:-----------------:|
| No log        | 0     | 0     | 0.6431          | 0.3317                | 0.2939        | 0.1883               | 0.8002            | 0.4759                | 0.2655        | 0.1951               | 0.5807            | 0.6269                | 0.2123        | 0.2069               | 0.3477            | 0.74                  | 0.1467        | 0.2470               | 0.1657            | 0.7996                | 0.0583        | 0.2544               | 0.0459            | 0.8179                | 0.0119        | 0.1533               | 0.0064            | 0.819                 | 0.0           | 0.0                  | 0.0               |
| 0.3502        | 1.0   | 3310  | 0.3454          | 0.8358                | 0.5113        | 0.5392               | 0.5181            | 0.8531                | 0.4610        | 0.6232               | 0.3962            | 0.8516                | 0.3676        | 0.6901               | 0.2785            | 0.8478                | 0.2794        | 0.7432               | 0.1960            | 0.8397                | 0.1938        | 0.7996               | 0.1252            | 0.8319                | 0.1139        | 0.7841               | 0.0673            | 0.8226                | 0.0362        | 0.5639               | 0.0192            |
| 0.3373        | 2.0   | 6620  | 0.3397          | 0.8347                | 0.5400        | 0.5197               | 0.5760            | 0.8491                | 0.5084        | 0.5776               | 0.4689            | 0.8553                | 0.4625        | 0.6428               | 0.3763            | 0.8527                | 0.3962        | 0.6839               | 0.2905            | 0.8466                | 0.3005        | 0.7413               | 0.1963            | 0.8388                | 0.2098        | 0.8004               | 0.1245            | 0.8273                | 0.0903        | 0.7607               | 0.0487            |
| 0.3158        | 3.0   | 9930  | 0.3365          | 0.8406                | 0.5342        | 0.5344               | 0.5483            | 0.8533                | 0.4993        | 0.5904               | 0.4484            | 0.8578                | 0.4508        | 0.6513               | 0.3595            | 0.8551                | 0.3859        | 0.7091               | 0.2795            | 0.8491                | 0.3060        | 0.7499               | 0.2022            | 0.8404                | 0.2067        | 0.8281               | 0.1240            | 0.8285                | 0.0941        | 0.8120               | 0.0517            |
| 0.2904        | 4.0   | 13240 | 0.3452          | 0.8381                | 0.5378        | 0.5313               | 0.5595            | 0.8511                | 0.5126        | 0.5874               | 0.4680            | 0.8579                | 0.4799        | 0.6445               | 0.3947            | 0.8557                | 0.4148        | 0.6800               | 0.3110            | 0.8518                | 0.3485        | 0.7224               | 0.2396            | 0.8449                | 0.2643        | 0.7810               | 0.1671            | 0.8341                | 0.1455        | 0.8169               | 0.0844            |
| 0.2648        | 5.0   | 16550 | 0.3584          | 0.8355                | 0.5304        | 0.5209               | 0.5467            | 0.8498                | 0.5095        | 0.5744               | 0.4641            | 0.8549                | 0.4771        | 0.6226               | 0.3929            | 0.8544                | 0.4266        | 0.6631               | 0.3211            | 0.8488                | 0.3519        | 0.6830               | 0.2428            | 0.8436                | 0.2751        | 0.7273               | 0.1746            | 0.8355                | 0.1824        | 0.7865               | 0.1055            |
| 0.2379        | 6.0   | 19860 | 0.3828          | 0.833                 | 0.5129        | 0.5087               | 0.5189            | 0.8467                | 0.5009        | 0.5621               | 0.4552            | 0.8507                | 0.4652        | 0.6005               | 0.3837            | 0.8535                | 0.4284        | 0.6566               | 0.3230            | 0.8505                | 0.3779        | 0.6810               | 0.2657            | 0.8453                | 0.3058        | 0.7055               | 0.1991            | 0.8378                | 0.2142        | 0.7394               | 0.1279            |
| 0.2146        | 7.0   | 23170 | 0.4161          | 0.8277                | 0.5138        | 0.4923               | 0.5417            | 0.8415                | 0.5069        | 0.5379               | 0.4849            | 0.8473                | 0.4840        | 0.5691               | 0.4291            | 0.8494                | 0.4526        | 0.5959               | 0.3727            | 0.8492                | 0.4142        | 0.6194               | 0.3179            | 0.8479                | 0.3655        | 0.6561               | 0.2594            | 0.8418                | 0.2768        | 0.6868               | 0.1781            |
| 0.1907        | 8.0   | 26480 | 0.4534          | 0.8289                | 0.5207        | 0.5013               | 0.5453            | 0.8391                | 0.5025        | 0.5299               | 0.4835            | 0.8453                | 0.4836        | 0.5587               | 0.4327            | 0.8491                | 0.4596        | 0.5855               | 0.3858            | 0.8495                | 0.4287        | 0.6135               | 0.3364            | 0.8482                | 0.3836        | 0.6333               | 0.2814            | 0.8448                | 0.3145        | 0.6741               | 0.2112            |
| 0.1694        | 9.0   | 29790 | 0.4725          | 0.8267                | 0.5118        | 0.4929               | 0.5344            | 0.8377                | 0.5002        | 0.5256               | 0.4804            | 0.8433                | 0.4835        | 0.5530               | 0.4341            | 0.8479                | 0.4635        | 0.5828               | 0.3902            | 0.8492                | 0.4365        | 0.6103               | 0.3463            | 0.8492                | 0.3972        | 0.6387               | 0.2945            | 0.8461                | 0.3289        | 0.6647               | 0.2244            |
| 0.1558        | 10.0  | 33100 | 0.4958          | 0.8251                | 0.5061        | 0.4873               | 0.5270            | 0.8363                | 0.4948        | 0.5201               | 0.4738            | 0.8424                | 0.4802        | 0.5486               | 0.4304            | 0.8461                | 0.4641        | 0.5752               | 0.3929            | 0.8471                | 0.4376        | 0.5986               | 0.3494            | 0.848                 | 0.4023        | 0.6279               | 0.3008            | 0.8464                | 0.3423        | 0.6586               | 0.2362            |


### Framework versions

- Transformers 4.54.1
- Pytorch 2.7.1+cu128
- Datasets 4.0.0
- Tokenizers 0.21.4
