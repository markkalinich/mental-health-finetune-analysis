---
library_name: transformers
license: apache-2.0
base_model: mistralai/Shieldstral-1.0-3B
datasets:
- contemmcm/ModerationBenchV2
pipeline_tag: image-text-to-text
tags:
- generated_from_trainer
- content-moderation
- multi-label
- bluesky
model-index:
- name: shieldstral-1.0-3b-cls-full-bluesky-moderation
  results: []
---

# shieldstral-1.0-3b-cls-full-bluesky-moderation

This model is a fine-tuned version of [mistralai/Shieldstral-1.0-3B](https://huggingface.co/mistralai/Shieldstral-1.0-3B) on the [ModerationBenchV2](https://huggingface.co/datasets/contemmcm/ModerationBenchV2) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5876
- Micro F1: 0.6811
- Macro F1: 0.2808
- Macro F1 Seen: 0.3251
- Macro Ap: 0.3927
- Exact Match: 0.8071
- Safe Accuracy: 0.8897

## Model description

A multi-label content-moderation classifier for Bluesky posts (text and images). It is a
full fine-tune of Shieldstral 1.0 3B, a safety model on the Mistral 3 / Pixtral backbone.
Shieldstral's original yes/no generative output is replaced by a classification head: one
forward pass returns 22 independent sigmoid scores, one per moderation label, trained with
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

transformers ships no classification head for Mistral 3, so the script defines one: three
lines composing the library's generic head with the Mistral 3 backbone. The weights load into
it directly, with nothing missing and no key mapping. One detail fails silently, so keep it:

- **Image size**: shrink images so the longest side is at most 896 pixels, as in training.
  The saved processor accepts up to 1,540 pixels, so an unresized photo is passed through at
  a resolution the model never saw (2.6 times the visual tokens for the example below).

Requires `transformers>=5`. The checkpoint is stored in float32; the script loads it in
bfloat16, which gives the same predictions.

```python
import json
from urllib.request import urlopen

import torch
from huggingface_hub import hf_hub_download
from PIL import Image
from transformers import AutoProcessor
from transformers.modeling_layers import GenericForSequenceClassification
from transformers.models.mistral3.modeling_mistral3 import Mistral3PreTrainedModel

MODEL = "contemmcm/shieldstral-1.0-3b-cls-full-bluesky-moderation"

# must be exactly this text: the model was trained with it
SYSTEM_PROMPT = (
    "You are a content moderation classifier for social media posts. "
    "Read the post and assess which moderation labels apply."
)


class Mistral3ForSequenceClassification(
    GenericForSequenceClassification, Mistral3PreTrainedModel
):
    """transformers ships no classification head for Mistral 3. This is its generic one
    (a linear layer over the last token) on the Mistral 3 / Pixtral backbone, which is
    the class the checkpoint was trained as."""


processor = AutoProcessor.from_pretrained(MODEL)
model = Mistral3ForSequenceClassification.from_pretrained(
    MODEL, dtype=torch.bfloat16, device_map="cuda:0"
).eval()
labels = json.load(open(hf_hub_download(MODEL, "label_space.json")))["labels"]
thresholds = json.load(open(hf_hub_download(MODEL, "thresholds.json")))["thresholds"]

# A real post: https://bsky.app/profile/did:plc:3htuuatm2fchjvon7tpc2jge/post/3mtd2ffcsvk22
text = (
    "Get Your Summer Tees Here & Please FOLLOW & SHARE. Tees Starting At Just $16. (Wait for "
    "the 35-40% off sales, 2-3 times a month.) I, Also, Have Mugs, Tote Bags, Magnets, "
    "Stickers, Etc., Available. Over 250 Designs! If You DO Make A Purchase, Thanks In "
    "Advance! www.teepublic.com/user/roszelle-art"
)
image = Image.open(urlopen(
    "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:3htuuatm2fchjvon7tpc2jge/"
    "bafkreigp5m25icqkxlrm6pvbpzvey2g5bchrqonlyaypo7cs6ahqsekaey"
)).convert("RGB")
# Pixtral spends visual tokens in proportion to resolution, and the model was trained on
# images whose longest side is at most 896 pixels. Larger ones must be shrunk first.
image.thumbnail((896, 896), Image.BILINEAR)

messages = [
    {"role": "system", "content": [{"type": "text", "text": SYSTEM_PROMPT}]},
    {"role": "user", "content": [{"type": "image", "image": image},
                                 {"type": "text", "text": text}]},
]
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
).to(model.device, dtype=torch.bfloat16)

with torch.no_grad():
    probs = torch.sigmoid(model(**inputs).logits[0].float()).tolist()

# a label applies when its probability reaches that label's threshold; none means "safe"
for name, p, cut in zip(labels, probs, thresholds):
    if p >= cut:
        print(f"{name}: {p:.3f}")
```

Output:

```
spam: 1.000
```

Pass every image of the post, in order, as its own `{"type": "image", "image": ...}` entry
before the text, each resized the same way. A text-only post simply has no image entries.
Images of 28 pixels or less per side (tracking pixels, placeholders) crash the Mistral 3 vision
path in transformers 5.12; drop them or upscale them to 56 pixels before use.

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
| 0.6737        | 0.2845 | 200  | 0.3812          | 0.5256   | 0.1420   | 0.1644        | 0.2790   | 0.7552      | 0.8272        |
| 0.6643        | 0.5690 | 400  | 0.3171          | 0.6104   | 0.1695   | 0.1963        | 0.3227   | 0.7708      | 0.8634        |
| 0.6405        | 0.8535 | 600  | 0.2947          | 0.5945   | 0.1945   | 0.2253        | 0.3291   | 0.7762      | 0.8468        |
| 0.3629        | 1.1380 | 800  | 0.3692          | 0.5763   | 0.1811   | 0.2098        | 0.3363   | 0.7803      | 0.8594        |
| 0.3258        | 1.4225 | 1000 | 0.3921          | 0.6045   | 0.2213   | 0.2562        | 0.3627   | 0.7739      | 0.8625        |
| 0.4544        | 1.7070 | 1200 | 0.3023          | 0.6226   | 0.2098   | 0.2429        | 0.3707   | 0.7834      | 0.8511        |
| 0.3674        | 1.9915 | 1400 | 0.2904          | 0.6382   | 0.2368   | 0.2742        | 0.3986   | 0.7967      | 0.8767        |
| 0.2086        | 2.2760 | 1600 | 0.3655          | 0.6500   | 0.2372   | 0.2747        | 0.3955   | 0.7973      | 0.8846        |
| 0.2240        | 2.5605 | 1800 | 0.3571          | 0.6611   | 0.2522   | 0.2921        | 0.3939   | 0.8005      | 0.8864        |
| 0.2311        | 2.8450 | 2000 | 0.3464          | 0.6744   | 0.2721   | 0.3151        | 0.4048   | 0.8061      | 0.8889        |
| 0.1040        | 3.1294 | 2200 | 0.4770          | 0.6785   | 0.2817   | 0.3261        | 0.3965   | 0.8065      | 0.8875        |
| 0.0398        | 3.4139 | 2400 | 0.5475          | 0.6839   | 0.2770   | 0.3207        | 0.3888   | 0.8032      | 0.8893        |
| 0.0480        | 3.6984 | 2600 | 0.5873          | 0.6803   | 0.2791   | 0.3231        | 0.3937   | 0.8079      | 0.8900        |
| 0.0521        | 3.9829 | 2800 | 0.5877          | 0.6805   | 0.2832   | 0.3279        | 0.3925   | 0.8067      | 0.8900        |
| 0.0521        | 4.0    | 2812 | 0.5876          | 0.6811   | 0.2808   | 0.3251        | 0.3927   | 0.8071      | 0.8897        |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.6.0+cu124
- Datasets 5.0.1
- Tokenizers 0.22.2