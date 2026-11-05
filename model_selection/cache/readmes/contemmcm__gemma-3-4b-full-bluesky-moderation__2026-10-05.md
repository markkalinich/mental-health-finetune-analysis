---
library_name: transformers
license: gemma
base_model: google/gemma-3-4b-it
datasets:
- contemmcm/ModerationBenchV2
pipeline_tag: image-text-to-text
tags:
- generated_from_trainer
- content-moderation
- multi-label
- bluesky
model-index:
- name: gemma-3-4b-full-bluesky-moderation
  results: []
---

# gemma-3-4b-full-bluesky-moderation

This model is a fine-tuned version of [google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) on the [ModerationBenchV2](https://huggingface.co/datasets/contemmcm/ModerationBenchV2) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2356
- Micro F1: 0.7142
- Macro F1: 0.3023
- Macro F1 Seen: 0.3500
- Macro Ap: 0.4773
- Exact Match: 0.8218
- Safe Accuracy: 0.9007

## Model description

A multi-label content-moderation classifier for Bluesky posts (text and images). It is a
full fine-tune of Gemma 3 4B with the language-model head replaced by a classification head:
one forward pass returns 22 independent sigmoid scores, one per moderation label, trained with
binary cross-entropy. A post can carry several labels at once, and no label reaching its
threshold means "safe". There is no generated text to parse.

The 22 labels, in output order (also in `label_space.json`):

| | | | |
|---|---|---|---|
| `porn` | `sexual` | `nudity` | `sexual-figurative` |
| `graphic-media` | `self-harm` | `sensitive` | `extremist` |
| `intolerant` | `threat` | `rude` | `illicit` |
| `security` | `unsafe-link` | `impersonation` | `misinformation` |
| `rumor` | `misleading` | `scam` | `engagement-farming` |
| `spam` | `inauthentic` | | |

## How to use

No custom code is needed: the checkpoint loads into transformers' stock
`Gemma3ForSequenceClassification` (requires `transformers>=5`).

```python
import torch

from transformers import AutoProcessor, Gemma3ForSequenceClassification

MODEL = "contemmcm/gemma-3-4b-full-bluesky-moderation"

# must be exactly this text: the model was trained with it
SYSTEM_PROMPT = (
    "You are a content moderation classifier for social media posts. "
    "Read the post and assess which moderation labels apply."
)

processor = AutoProcessor.from_pretrained(MODEL)
model = Gemma3ForSequenceClassification.from_pretrained(
    MODEL, dtype=torch.bfloat16, device_map="cuda:0"
).eval()

# A real post: https://bsky.app/profile/did:plc:3htuuatm2fchjvon7tpc2jge/post/3mtd2ffcsvk22
text = (
    "Get Your Summer Tees Here & Please FOLLOW & SHARE. Tees Starting At Just $16. (Wait for "
    "the 35-40% off sales, 2-3 times a month.) I, Also, Have Mugs, Tote Bags, Magnets, "
    "Stickers, Etc., Available. Over 250 Designs! If You DO Make A Purchase, Thanks In "
    "Advance! www.teepublic.com/user/roszelle-art"
)
image = (
    "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:3htuuatm2fchjvon7tpc2jge/"
    "bafkreigp5m25icqkxlrm6pvbpzvey2g5bchrqonlyaypo7cs6ahqsekaey"
)
messages = [
    {"role": "system", "content": [{"type": "text", "text": SYSTEM_PROMPT}]},
    {"role": "user", "content": [{"type": "image", "url": image},
                                 {"type": "text", "text": text}]},
]

inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
).to(model.device)

with torch.no_grad():
    probs = torch.sigmoid(model(**inputs).logits[0].float()).tolist()

# a label applies when its probability reaches that label's threshold; none means "safe"
import json

from huggingface_hub import hf_hub_download

labels = json.load(open(hf_hub_download(MODEL, "label_space.json")))["labels"]
thresholds = json.load(open(hf_hub_download(MODEL, "thresholds.json")))["thresholds"]

for name, p, cut in zip(labels, probs, thresholds):
    if p >= cut:
        print(f"{name}: {p:.3f}")
```

Output:

```
spam: 0.898
```

Pass every image of the post, in order, as its own `{"type": "image", ...}` entry before the
text (`"url"`, or `"path"` for a local file). A text-only post simply has no image entries.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- total_eval_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.03
- num_epochs: 4.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Micro F1 | Macro F1 | Macro F1 Seen | Macro Ap | Exact Match | Safe Accuracy |
|:-------------:|:------:|:----:|:---------------:|:--------:|:--------:|:-------------:|:--------:|:-----------:|:-------------:|
| 0.6285        | 0.2845 | 200  | 0.3511          | 0.5621   | 0.1544   | 0.1787        | 0.2642   | 0.7633      | 0.8524        |
| 0.5562        | 0.5690 | 400  | 0.2921          | 0.6520   | 0.2036   | 0.2357        | 0.3576   | 0.7730      | 0.8742        |
| 0.5647        | 0.8535 | 600  | 0.2543          | 0.6370   | 0.2171   | 0.2514        | 0.4052   | 0.7969      | 0.8713        |
| 0.4041        | 1.1380 | 800  | 0.2553          | 0.6909   | 0.2563   | 0.2968        | 0.3993   | 0.8077      | 0.8881        |
| 0.3462        | 1.4225 | 1000 | 0.2524          | 0.6779   | 0.2804   | 0.3246        | 0.4233   | 0.8123      | 0.8891        |
| 0.4489        | 1.7070 | 1200 | 0.2275          | 0.7001   | 0.2677   | 0.3099        | 0.4715   | 0.8212      | 0.8918        |
| 0.4056        | 1.9915 | 1400 | 0.2216          | 0.7      | 0.2840   | 0.3289        | 0.4781   | 0.8171      | 0.8914        |
| 0.3366        | 2.2760 | 1600 | 0.2340          | 0.7012   | 0.2874   | 0.3327        | 0.4772   | 0.8202      | 0.8966        |
| 0.2767        | 2.5605 | 1800 | 0.2332          | 0.7094   | 0.3089   | 0.3576        | 0.4801   | 0.8202      | 0.8985        |
| 0.3364        | 2.8450 | 2000 | 0.2349          | 0.7115   | 0.3039   | 0.3518        | 0.4768   | 0.8229      | 0.9012        |
| 0.2961        | 3.1294 | 2200 | 0.2350          | 0.7164   | 0.3032   | 0.3510        | 0.4759   | 0.8227      | 0.9012        |
| 0.2617        | 3.4139 | 2400 | 0.2364          | 0.7152   | 0.3025   | 0.3502        | 0.4761   | 0.8227      | 0.9001        |
| 0.2577        | 3.6984 | 2600 | 0.2354          | 0.7122   | 0.3010   | 0.3486        | 0.4774   | 0.8214      | 0.9005        |
| 0.2428        | 3.9829 | 2800 | 0.2357          | 0.7136   | 0.3021   | 0.3498        | 0.4773   | 0.8214      | 0.9005        |
| 0.2428        | 4.0    | 2812 | 0.2356          | 0.7142   | 0.3023   | 0.3500        | 0.4773   | 0.8218      | 0.9007        |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.6.0+cu124
- Datasets 5.0.1
- Tokenizers 0.22.2
