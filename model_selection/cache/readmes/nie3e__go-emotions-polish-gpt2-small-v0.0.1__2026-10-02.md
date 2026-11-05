---
library_name: transformers
license: mit
base_model: sdadas/polish-gpt2-small
tags:
- generated_from_trainer
- text-classification
- multi-class-classification
- multi-label-classification
- emotions
model-index:
- name: go-emotions-polish-gpt2-small-v0.0.1
  results: []
pipeline_tag: text-classification
language:
  - pl
---

# go-emotions-polish-gpt2-small-v0.0.1

This model is a fine-tuned version of [sdadas/polish-gpt2-small](https://huggingface.co/sdadas/polish-gpt2-small) on the machine translated [google-research-datasets/go_emotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) dataset.
It achieves the following results on the evaluation set:
Every list contains results for threshold [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
- Loss: 0.2123
- Hamming Accuracy: [0.9556733317272946, 0.9592094848057267, 0.9614034483945348, 0.9631328079292425, 0.96438895963107, 0.9652665450665933, 0.9654558281997453]
- F1 Macro: [0.4929423141608899, 0.49513962905111936, 0.48929787051637963, 0.4797491530618914, 0.4647116651469601, 0.44570651699340547, 0.40534073938214327]
- Precision Macro: [0.45136216505815147, 0.4817190614473335, 0.5085113721947904, 0.5297915362044485, 0.5555560780209522, 0.5895901759803143, 0.6380967706137726]
- Recall Macro: [0.551217261404107, 0.5185202616828293, 0.4824209900009455, 0.4506401023339946, 0.4144524017062031, 0.3745523616734555, 0.3152333101205886]

**Try here: [spaces/nie3e/polish-emotions](https://huggingface.co/spaces/nie3e/polish-emotions)**

## Model description

Trained from [sdadas/polish-gpt2-small](https://huggingface.co/sdadas/polish-gpt2-small)

## Intended uses & limitations

Detecting emotions described in paper [2005.00547](https://arxiv.org/abs/2005.00547)

Labels:
```
0: admiration
1: amusement
2: anger
3: annoyance
4: approval
5: caring
6: confusion
7: curiosity
8: desire
9: disappointment
10: disapproval
11: disgust
12: embarrassment
13: excitement
14: fear
15: gratitude
16: grief
17: joy
18: love
19: nervousness
20: optimism
21: pride
22: realization
23: relief
24: remorse
25: sadness
26: surprise
27: neutral
```

### How to use:

<details><summary>Transformers AutoModel</summary>

```py
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
checkpoint = "nie3e/go-emotions-polish-gpt2-small-v0.0.1"
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
['joy']
{'admiration': '17.75%', 'amusement': '11.22%', 'anger': '0.07%', 'annoyance': '0.36%', 'approval': '6.63%', 'caring': '0.84%', 'confusion': '0.22%', 'curiosity': '0.58%', 'desire': '0.40%', 'disappointment': '1.29%', 'disapproval': '0.26%', 'disgust': '0.11%', 'embarrassment': '0.08%', 'excitement': '25.88%', 'fear': '0.54%', 'gratitude': '0.41%', 'grief': '0.90%', 'joy': '63.62%', 'love': '11.74%', 'nervousness': '0.08%', 'optimism': '1.98%', 'pride': '0.03%', 'realization': '1.19%', 'relief': '0.53%', 'remorse': '0.02%', 'sadness': '0.75%', 'surprise': '0.58%', 'neutral': '8.93%'}
```

</details>

<details><summary>Transformers Pipeline</summary>

```py
from transformers import pipeline

# Set the model, tokenizer, device, text as above

pipe = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=-1,
    device=device
)

result = pipe(text)
print(result)
```

```
[[{'label': 'joy', 'score': 0.6362035274505615}, {'label': 'excitement', 'score': 0.2588024437427521}, {'label': 'admiration', 'score': 0.17747776210308075}, {'label': 'love', 'score': 0.11739460378885269}, {'label': 'amusement', 'score': 0.11221607774496078}, {'label': 'neutral', 'score': 0.08927429467439651}, {'label': 'approval', 'score': 0.0662560984492302}, {'label': 'optimism', 'score': 0.019809801131486893}, {'label': 'disappointment', 'score': 0.012886008247733116}, {'label': 'realization', 'score': 0.011940046213567257}, {'label': 'grief', 'score': 0.009018097072839737}, {'label': 'caring', 'score': 0.008446046151220798}, {'label': 'sadness', 'score': 0.007472767494618893}, {'label': 'curiosity', 'score': 0.0058141243644058704}, {'label': 'surprise', 'score': 0.005764781963080168}, {'label': 'fear', 'score': 0.00539048807695508}, {'label': 'relief', 'score': 0.005273739341646433}, {'label': 'gratitude', 'score': 0.004061913583427668}, {'label': 'desire', 'score': 0.003967347089201212}, {'label': 'annoyance', 'score': 0.0036265170201659203}, {'label': 'disapproval', 'score': 0.0026028596330434084}, {'label': 'confusion', 'score': 0.0022179142106324434}, {'label': 'disgust', 'score': 0.0011114622466266155}, {'label': 'embarrassment', 'score': 0.0007856030715629458}, {'label': 'nervousness', 'score': 0.0007625268190167844}, {'label': 'anger', 'score': 0.0007304779137484729}, {'label': 'pride', 'score': 0.0003317077935207635}]]
```

</details>

<details><summary>vLLM OpenAI serving (recommended)</summary>

```bash
docker run --gpus 1 --ipc=host -p 8000:8000 vllm/vllm-openai:v0.9.2 --model nie3e/go-emotions-polish-gpt2-small-v0.0.1
```

using curl:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/classify' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "nie3e/go-emotions-polish-gpt2-small-v0.0.1",
  "input": ["To jest model wykrywający super emocje w tekście! :D"]
}'
```
result:
```json
{
	"id": "classify-5c8a13023dc740e2acac2d7a99d0ef9a",
	"object": "list",
	"created": 1753210194,
	"model": "nie3e/go-emotions-polish-gpt2-small-v0.0.1",
	"data": [
		{
			"index": 0,
			"label": "joy",
			"probs": [
				0.07563348859548569,
				0.04428929090499878,
				0.00025575023028068244,
				0.0012786707375198603,
				0.024941278621554376,
				0.002984634367749095,
				0.000778588408138603,
				0.0020513073541224005,
				0.0013934164308011532,
				0.004568836186081171,
				0.00091740139760077,
				0.0003899725270457566,
				0.0002754538436420262,
				0.12216728925704956,
				0.001897149020805955,
				0.0014264603378251196,
				0.003189561888575554,
				0.6122910380363464,
				0.04659644141793251,
				0.0002680239558685571,
				0.007090186700224876,
				0.00011663449549814686,
				0.00424202112480998,
				0.001860454911366105,
				0.00006697755452478305,
				0.002644239692017436,
				0.002027408918365836,
				0.03435806185007095
			],
			"num_classes": 28
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
response = requests.post(
    f"http://127.0.0.1:8000/classify",
    headers={"Content-Type": "application/json"},
    json={
        "model": "nie3e/go-emotions-polish-gpt2-small-v0.0.1",
        "input": ["To jest model wykrywający super emocje w tekście! :D"]
    }
)

print(response.json())
```
```
{'id': 'classify-e2f3a666c62a448db2685278c504f6a2',
 'object': 'list',
 'created': 1753210282,
 'model': 'nie3e/go-emotions-polish-gpt2-small-v0.0.1',
 'data': [{'index': 0,
   'label': 'joy',
   'probs': [0.07563348859548569,
    0.04428929090499878,
    0.00025575023028068244,
    0.0012786707375198603,
    0.024941278621554375,
    0.002984634367749095,
    0.000778588408138603,
    0.0020513073541224003,
    0.0013934164308011532,
    0.004568836186081171,
    0.00091740139760077,
    0.0003899725270457566,
    0.0002754538436420262,
    0.12216728925704956,
    0.001897149020805955,
    0.0014264603378251195,
    0.003189561888575554,
    0.6122910380363464,
    0.04659644141793251,
    0.0002680239558685571,
    0.007090186700224876,
    0.00011663449549814686,
    0.00424202112480998,
    0.001860454911366105,
    6.697755452478305e-05,
    0.002644239692017436,
    0.002027408918365836,
    0.03435806185007095],
   'num_classes': 28}],
 'usage': {'prompt_tokens': 12,
  'total_tokens': 12,
  'completion_tokens': 0,
  'prompt_tokens_details': None}}
```

</details>

## Training and evaluation data

Dataset: [google-research-datasets/go_emotions](https://huggingface.co/datasets/google-research-datasets/go_emotions)
Preprocessing:
  - dropping rows that exceeded 256 tokens (GPT2 Tokenizer) and having 5 or more digits in a row in the text
  - machine translation into Polish
  - removing 80% rows that have only `neutral` label

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

<details><summary>Trainer using class weights: </summary>

```py
class WeightedTrainer(Trainer):
    def __init__(self, class_weights=None, **kwargs):
        super().__init__(**kwargs)
        self.class_weights = class_weights

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.logits

        loss_fct = torch.nn.BCEWithLogitsLoss(pos_weight=self.class_weights)
        loss = loss_fct(logits, labels.float())

        return (loss, outputs) if return_outputs else loss
```
</details>

<details><summary>Class weights: </summary>

```py
df = tokenized_dataset["train"].to_pandas()
label_counts = df["labels_h1"].explode().value_counts().sort_index()
total_samples = len(df)
class_weights = [(total_samples - count) / count for count in label_counts]
class_weights = np.clip(class_weights, 0.1, 10.0)
```
</details>

<details><summary>Metrics computation: </summary>

```py
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score

def sigmoid(x):
    return 1/(1 + np.exp(-x))


def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    probabilities = sigmoid(predictions)
    thresholds = np.arange(0.3, 0.91, 0.1)

    computed_metrics = {
        "hamming_accuracy": [],
        "f1_macro": [],
        "precision_macro": [],
        "recall_macro": []
    }

    for th in thresholds:
        binary_preds = (probabilities > th).astype(int)

        # Hamming Accuracy (for multi-label)
        hamming_acc = 1 - np.mean(binary_preds != labels)

        # Macro-averaged F1/Precision/Recall
        f1 = f1_score(labels, binary_preds, average="macro", zero_division=0)
        precision = precision_score(labels, binary_preds, average="macro",
                                    zero_division=0)
        recall = recall_score(labels, binary_preds, average="macro",
                              zero_division=0)

        computed_metrics["hamming_accuracy"].append(hamming_acc)
        computed_metrics["f1_macro"].append(f1)
        computed_metrics["precision_macro"].append(precision)
        computed_metrics["recall_macro"].append(recall)

    return computed_metrics
```
</details>

### Training results
Every list contains results for threshold [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
<details><summary>Results:</summary>

| Epoch | Training Loss | Validation Loss | Hamming Accuracy                                                                                                                             | F1 Macro                                                                                                                                          | Precision Macro                                                                                                                                | Recall Macro                                                                                                                                      |
|:-----:|:-------------:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|
|   1   | 0.27          | 0.1772          | [0.9512768007708986, 0.959080428124032, 0.9628144681143959, 0.9640103933647658, 0.9644922049764256, 0.9635629968682246, 0.9613690332794164]  | [0.46241863342821793, 0.4532072267866339, 0.4326439737447529, 0.3910675952043853, 0.34917671255121363, 0.2895274759086305, 0.17584749438485497]   | [0.4461301409377742, 0.5054615942184383, 0.5451358075233073, 0.5833130459387715, 0.612234133178668, 0.6415091314766198, 0.5974110920754876]    | [0.5228623671145524, 0.44986334764237274, 0.3906724180081668, 0.32626227826074566, 0.27496335348059725, 0.21568979328206703, 0.12657202290169853] |
|   2   | 0.1671        | 0.1609          | [0.9546752933888564, 0.9605000516226727, 0.9636834497711395, 0.9650600543758819, 0.9657311491206938, 0.9651977148363561, 0.9638813366830712] | [0.47181939799853245, 0.4773149021343449, 0.47247182216640654, 0.4451366460170004, 0.42366333538332507, 0.37403397926368737, 0.30313475002048484] | [0.441959190629794, 0.5081107432668841, 0.561701577155539, 0.5801413709101412, 0.6462220107453076, 0.6764110777613557, 0.7061705442835556]     | [0.580901954973524, 0.5214683734393482, 0.47275669773690804, 0.40899548004178854, 0.36579701720117563, 0.3034817689033619, 0.23056933111221325]   |
|   3   | 0.1399        | 0.1606          | [0.9497109130330041, 0.9569208796503424, 0.9613518257218571, 0.9638211102316138, 0.965249337509034, 0.9654988470936435, 0.9639931858072065]  | [0.4749602125981087, 0.4873423290936483, 0.48338025379077687, 0.4701566587566043, 0.4498896201717952, 0.41177613984294953, 0.32623322721112374]   | [0.41117966940106204, 0.45764702886929787, 0.5046222714256859, 0.5530253088371339, 0.6005644340448025, 0.6760814655629932, 0.6800566831000542] | [0.6222726145233521, 0.5734770801943697, 0.5113684601796389, 0.4550331179550861, 0.4044620988185089, 0.34071151157255797, 0.25092165205453]       |
|   4   | 0.1176        | 0.1669          | [0.95028736621124, 0.9570241249956981, 0.9612141652613828, 0.9638555253467322, 0.9651202808273394, 0.9657827717933717, 0.9645008087552053]   | [0.46776823075218205, 0.4770370632194352, 0.48170399873205805, 0.4815610729662237, 0.46635824100838313, 0.4346021274443605, 0.35739954616385866]  | [0.4026523166950933, 0.44682680882818887, 0.4916683449781562, 0.5367728364431649, 0.575993305278815, 0.6472053281375478, 0.6693600674340754]   | [0.6123919277944883, 0.557746427766825, 0.5176178038314311, 0.47937515940889003, 0.4322437215959729, 0.36783678520926777, 0.27372379016591925]    |
|   5   | 0.0992        | 0.1735          | [0.9527996696148948, 0.9587878996455244, 0.9617906184396187, 0.9635802044257838, 0.9652063186151357, 0.9660236775992016, 0.9651891110575765] | [0.48529687411311123, 0.49524580727616085, 0.4889009921348519, 0.476286545728211, 0.4606138233621902, 0.4360905909528836, 0.37325003123769596]    | [0.43090457512637126, 0.4758805613570571, 0.5059212751069277, 0.5323418850235423, 0.5778588494150572, 0.6303798411419806, 0.7050763694911789]  | [0.5871641620419744, 0.5468805735159331, 0.5029133763134643, 0.46169826597462366, 0.4141503796261941, 0.3657398096031768, 0.28558429402703295]    |
|   6   | 0.083         | 0.1841          | [0.9520941597549644, 0.9572736345803077, 0.9603795987197578, 0.9626337887600234, 0.9642771105069347, 0.9654042055270675, 0.9656279037753381] | [0.4848110691063849, 0.4902428690172167, 0.48618324094573484, 0.478250083701593, 0.4677017272145706, 0.44389902987164165, 0.39728758295841066]    | [0.4282820729807268, 0.4617066856103255, 0.48889885714082243, 0.515822475491864, 0.548112314645949, 0.5864861700775268, 0.642991780443598]     | [0.5872655526119982, 0.5489591883468488, 0.5083264155214335, 0.47033662001581716, 0.43490169281095825, 0.384219870731881, 0.3108363940394387]     |
|   7   | 0.0715        | 0.1922          | [0.9541934817771965, 0.958366314485322, 0.960921636782875, 0.9629607323536498, 0.964363148294731, 0.9655160546512028, 0.9651460921636783]    | [0.49327999654639215, 0.4942623403104429, 0.48696556713303135, 0.4804445324053421, 0.46939295694544736, 0.4475119371916684, 0.3881489924589002]   | [0.4442084347600441, 0.47508959657212724, 0.5001365624277175, 0.5315837721216776, 0.5635172346685284, 0.6060793900700022, 0.6547980634968182]  | [0.5749401619525247, 0.5335821079528872, 0.4937842962870135, 0.45744546851621865, 0.4230868747861999, 0.37702257236227427, 0.29712029562165154]   |
|   8   | 0.0609        | 0.2025          | [0.9547011047251953, 0.9585469938396944, 0.961377637058196, 0.9629951474687682, 0.9646040541005609, 0.9654644319785249, 0.9653095639604914]  | [0.4929084055191263, 0.4966642184262872, 0.49509852255405307, 0.47826643819598524, 0.4664438311012158, 0.4433651185391054, 0.38896780252101004]   | [0.45156391170754395, 0.48340644816595113, 0.5119596021038765, 0.5318185543351281, 0.5669432431065436, 0.6023885415673448, 0.640319754629273]  | [0.5590029919029157, 0.5266729465629012, 0.49473318351169737, 0.45252148670174985, 0.4154957108440041, 0.37123594052789305, 0.2964469621468265]   |
|   9   | 0.0524        | 0.2099          | [0.9549592180885845, 0.9585986165123722, 0.9611195236948068, 0.9629435247960905, 0.9642771105069347, 0.9651030732697801, 0.9651805072787969] | [0.4920579362491578, 0.48948143585573084, 0.48373280918321976, 0.4765803308742461, 0.464925139967501, 0.44204098321531043, 0.3994121381701787]    | [0.4481765728464743, 0.4727514944675648, 0.49823474126036366, 0.5251829103863094, 0.5535803816229916, 0.5863930625014495, 0.6280255957220133]  | [0.5567520239062707, 0.5174123200187039, 0.4811964159610151, 0.4494146051029743, 0.41590442650848564, 0.37120008498454643, 0.30929707478684687]   |
|  10   | 0.0479        | 0.2123          | [0.9556733317272946, 0.9592094848057267, 0.9614034483945348, 0.9631328079292425, 0.96438895963107, 0.9652665450665933, 0.9654558281997453]   | [0.4929423141608899, 0.49513962905111936, 0.48929787051637963, 0.4797491530618914, 0.4647116651469601, 0.44570651699340547, 0.40534073938214327]  | [0.45136216505815147, 0.4817190614473335, 0.5085113721947904, 0.5297915362044485, 0.5555560780209522, 0.5895901759803143, 0.6380967706137726]  | [0.551217261404107, 0.5185202616828293, 0.4824209900009455, 0.4506401023339946, 0.4144524017062031, 0.3745523616734555, 0.3152333101205886]       |
</details>

### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0

