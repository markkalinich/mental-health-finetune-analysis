---
library_name: transformers
base_model: Qwen/Qwen2.5-VL-3B-Instruct
datasets:
- contemmcm/ModerationBenchV2
pipeline_tag: image-text-to-text
tags:
- generated_from_trainer
- content-moderation
- multi-label
- bluesky
model-index:
- name: qwen2.5-vl-3b-cls-full-bluesky-moderation
  results: []
---

# qwen2.5-vl-3b-cls-full-bluesky-moderation

This model is a fine-tuned version of [Qwen/Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) on the [ModerationBenchV2](https://huggingface.co/datasets/contemmcm/ModerationBenchV2) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2429
- Micro F1: 0.6770
- Macro F1: 0.2598
- Macro F1 Seen: 0.3008
- Macro Ap: 0.3687
- Exact Match: 0.8086
- Safe Accuracy: 0.8949

## Model description

A multi-label content-moderation classifier for Bluesky posts (text and images). It is a
full fine-tune of Qwen2.5-VL 3B with the language-model head replaced by a classification head:
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

transformers ships no classification head for Qwen2.5-VL, so the script defines one: three
lines composing the library's generic head with the Qwen2.5-VL backbone. Two details are easy
to get wrong and both fail silently, so keep them:

- **`key_mapping`**: without it the language model loads as random weights and every score is
  noise. transformers prints a load report listing `MISSING` keys when that happens; a correct
  load reports none.
- **Image size**: shrink images so the longest side is at most 896 pixels, as in training. An
  unresized phone photo costs several thousand visual tokens and looks nothing like the
  training data.

Requires `transformers>=5`.

```python
import json

from urllib.request import urlopen

import torch

from huggingface_hub import hf_hub_download
from PIL import Image
from transformers import AutoProcessor
from transformers.modeling_layers import GenericForSequenceClassification
from transformers.models.qwen2_5_vl.modeling_qwen2_5_vl import Qwen2_5_VLPreTrainedModel

MODEL = "contemmcm/qwen2.5-vl-3b-cls-full-bluesky-moderation"

# must be exactly this text: the model was trained with it
SYSTEM_PROMPT = (
    "You are a content moderation classifier for social media posts. "
    "Read the post and assess which moderation labels apply."
)


class Qwen2_5_VLForSequenceClassification(
    GenericForSequenceClassification, Qwen2_5_VLPreTrainedModel
):
    """transformers ships no classification head for Qwen2.5-VL. This is its generic one
    (a linear layer over the last token) on the Qwen2.5-VL backbone, which is the class
    the checkpoint was trained as."""


# The weights are stored under Qwen2.5-VL's original names. Without this mapping the
# language model is silently left randomly initialized and the scores are noise.
KEY_MAPPING = {
    "^visual": "model.visual",
    r"^model(?!\.(language_model|visual))": "model.language_model",
}

processor = AutoProcessor.from_pretrained(MODEL)
model = Qwen2_5_VLForSequenceClassification.from_pretrained(
    MODEL, dtype=torch.bfloat16, device_map="cuda:0", key_mapping=KEY_MAPPING
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

# Qwen spends visual tokens in proportion to resolution, and the model was trained on
# images whose longest side is at most 896 pixels. Larger ones must be shrunk first.
image.thumbnail((896, 896), Image.BILINEAR)

messages = [
    {"role": "system", "content": [{"type": "text", "text": SYSTEM_PROMPT}]},
    {"role": "user", "content": [{"type": "image", "image": image},
                                 {"type": "text", "text": text}]},
]
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="pt"
).to(model.device)

with torch.no_grad():
    probs = torch.sigmoid(model(**inputs).logits[0].float()).tolist()

# a label applies when its probability reaches that label's threshold; none means "safe"
for name, p, cut in zip(labels, probs, thresholds):
    if p >= cut:
        print(f"{name}: {p:.3f}")
```

Output:

```
spam: 0.534
```

Pass every image of the post, in order, as its own `{"type": "image", "image": ...}` entry
before the text, each resized the same way. A text-only post simply has no image entries.

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
| 0.5816        | 0.2845 | 200  | 0.3214          | 0.5462   | 0.1413   | 0.1636        | 0.2437   | 0.7701      | 0.8513        |
| 0.5807        | 0.5690 | 400  | 0.2790          | 0.6264   | 0.1780   | 0.2061        | 0.3077   | 0.7863      | 0.8721        |
| 0.5503        | 0.8535 | 600  | 0.2711          | 0.6092   | 0.1883   | 0.2181        | 0.3258   | 0.7899      | 0.8625        |
| 0.4087        | 1.1380 | 800  | 0.2563          | 0.6462   | 0.2215   | 0.2564        | 0.3430   | 0.8009      | 0.8798        |
| 0.3927        | 1.4225 | 1000 | 0.2599          | 0.6588   | 0.2436   | 0.2821        | 0.3558   | 0.8009      | 0.8897        |
| 0.4632        | 1.7070 | 1200 | 0.2433          | 0.6754   | 0.2484   | 0.2876        | 0.3649   | 0.8079      | 0.8881        |
| 0.4500        | 1.9915 | 1400 | 0.2444          | 0.6636   | 0.2417   | 0.2798        | 0.3658   | 0.8083      | 0.8879        |
| 0.4305        | 2.2760 | 1600 | 0.2465          | 0.6686   | 0.2599   | 0.3009        | 0.3659   | 0.8073      | 0.8918        |
| 0.3686        | 2.5605 | 1800 | 0.2436          | 0.6775   | 0.2607   | 0.3018        | 0.3683   | 0.8098      | 0.8922        |
| 0.4462        | 2.8450 | 2000 | 0.2437          | 0.6734   | 0.2593   | 0.3003        | 0.3678   | 0.8086      | 0.8918        |
| 0.4238        | 3.1294 | 2200 | 0.2437          | 0.6754   | 0.2687   | 0.3111        | 0.3680   | 0.8086      | 0.8929        |
| 0.3573        | 3.4139 | 2400 | 0.2427          | 0.6783   | 0.2666   | 0.3087        | 0.3690   | 0.8079      | 0.8941        |
| 0.3481        | 3.6984 | 2600 | 0.2435          | 0.6752   | 0.2680   | 0.3103        | 0.3686   | 0.8077      | 0.8935        |
| 0.3648        | 3.9829 | 2800 | 0.2429          | 0.6772   | 0.2598   | 0.3008        | 0.3686   | 0.8088      | 0.8949        |
| 0.3648        | 4.0    | 2812 | 0.2429          | 0.6770   | 0.2598   | 0.3008        | 0.3687   | 0.8086      | 0.8949        |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.6.0+cu124
- Datasets 5.0.1
- Tokenizers 0.22.2