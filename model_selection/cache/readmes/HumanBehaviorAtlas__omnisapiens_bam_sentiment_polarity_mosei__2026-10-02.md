---
language: en
license: apache-2.0
tags:
  - human-behavior
  - multimodal
  - qwen2.5-omni
  - sentiment-analysis
  - sentiment
datasets:
  - keentomato/human_behavior_atlas
---

# OmniSapiens BAM — Sentiment Polarity

Fine-tuned [Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) for multimodal sentiment polarity classification. Uses LoRA adapters merged into the backbone and a lightweight classification head.

## Benchmark
Evaluated on [keentomato/human_behavior_atlas](https://huggingface.co/datasets/keentomato/human_behavior_atlas).

## Usage

### Installation
```bash
pip install transformers torch huggingface_hub
```

### Classification

```python
import json, torch
from huggingface_hub import hf_hub_download
from transformers import Qwen2_5OmniThinkerForConditionalGeneration, AutoProcessor

MODEL_ID = "keentomato/omnisapiens_bam_sentiment_polarity_mosei"

# 1. Load backbone and processor
model = Qwen2_5OmniThinkerForConditionalGeneration.from_pretrained(
    MODEL_ID, torch_dtype=torch.float16, device_map="auto"
)
processor = AutoProcessor.from_pretrained(MODEL_ID)

# 2. Load classification heads and label scheme
heads_path = hf_hub_download(MODEL_ID, "heads.bin")
label_path = hf_hub_download(MODEL_ID, "label_scheme.json")
heads_sd = torch.load(heads_path, map_location="cpu")
with open(label_path) as f:
    label_scheme = json.load(f)

# 3. Reconstruct domain heads
global_classes = label_scheme["meta"]["global_classes"]  # {domain: [{index, label}, ...]}
hidden_size = model.config.hidden_size
domain_names = list(global_classes.keys())
domain_heads = torch.nn.ModuleList([
    torch.nn.Linear(hidden_size, len(global_classes[d])) for d in domain_names
])
domain_heads.load_state_dict({k.replace("heads.", ""): v for k, v in heads_sd.items()})
domain_heads.eval().to(model.device).to(torch.float16)
domain_to_id = {d: i for i, d in enumerate(domain_names)}

# 4. Prepare multimodal inputs
# video_tensor: [T, C, H, W] tensor or list of PIL images
# audio_waveform: 1-D numpy array / tensor at 16 kHz
domain = "sentiment_intensity"
messages = [{"role": "user", "content": [
    {"type": "video"},
    {"type": "audio"},
    {"type": "text", "text": "Classify the human behavior expressed."},
]}]
text = processor.apply_chat_template(messages, add_generation_prompt=False, tokenize=False)
inputs = processor(text=[text], videos=[video_tensor], audio=[audio_waveform], return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}

# 5. Forward pass — pool penultimate hidden layer, route through domain head
with torch.no_grad():
    out = model(**inputs, output_hidden_states=True, use_cache=False)
    h = out.hidden_states[-2]                            # [B, T, H]
    mask = inputs["attention_mask"].unsqueeze(-1).float()
    pooled = (h * mask).sum(1) / mask.sum(1)             # [B, H]
    logits = domain_heads[domain_to_id[domain]](pooled.float())  # [B, K_d]
    pred_idx = logits.argmax(dim=-1).item()

label_name = global_classes[domain][pred_idx]["label"]
print(f"Predicted {domain}: {label_name}")
```

### Behavioral Descriptors (BAM Adapters)

As `adapters.bin` is present in the repo, the model supports side-channel
behavioral descriptors extracted from OpenPose (video) and OpenSmile (audio).
These replace the raw video/audio inputs to the backbone with pre-computed
behavioral feature vectors that are injected via lightweight MLP adapters.

**Video — OpenPose keypoints**

OpenPose produces a dict per clip with keys `pose`, `face`, `left_hand`, `right_hand`,
each a `[T, K, 2or3]` tensor (T frames, K keypoints, x/y/conf).

```python
def prepare_video_feats(openpose_dict, temporal_mode="meanstd"):
    """OpenPose dict → pooled feature vector [D_v_pooled]."""
    parts = []
    for key in ("pose", "face", "left_hand", "right_hand"):
        t = openpose_dict.get(key)  # [T, K, 2or3]
        if t is None: continue
        t = torch.as_tensor(t).float()[..., :2]  # drop confidence, keep x/y
        parts.append(t.reshape(t.shape[0], -1))  # [T, K*2]
    seq = torch.cat(parts, dim=-1).float()       # [T, D_v]
    if temporal_mode == "meanstd":
        return torch.cat([seq.mean(0), seq.std(0)])  # [D_v*2]
    return seq.mean(0)                               # [D_v]

video_feats = prepare_video_feats(openpose_dict).unsqueeze(0)  # [1, D_v_pooled]
```

**Audio — OpenSmile features**

OpenSmile produces a dict with key `features` → `[T, D_a]` or `[D_a]`.

```python
def prepare_audio_feats(opensmile_dict):
    """OpenSmile dict → L2-normalised feature vector [D_a]."""
    x = torch.as_tensor(opensmile_dict["features"]).float()
    if x.ndim == 2: x = x.squeeze(0)  # [D_a] (single frame assumed)
    return x / x.norm(p=2).clamp_min(1e-6)

audio_feats = prepare_audio_feats(opensmile_dict).unsqueeze(0)  # [1, D_a]
```

**Loading and applying the adapters**

```python
import torch, torch.nn as nn
from huggingface_hub import hf_hub_download

adapters_sd = torch.load(hf_hub_download(MODEL_ID, "adapters.bin"), map_location="cpu")

# Infer architecture from saved weight shapes — no config needed
def _make_adapter(prefix, sd):
    w0 = sd[f"{prefix}.mlp.0.weight"]          # [hidden, feat_dim]
    w2 = sd[f"{prefix}.mlp.2.weight"]          # [out_dim, hidden]
    feat_dim, hidden, out_dim = w0.shape[1], w0.shape[0], w2.shape[0]
    mlp = nn.Sequential(nn.Linear(feat_dim, hidden), nn.ReLU(), nn.Linear(hidden, out_dim))
    alpha = nn.Parameter(sd[f"{prefix}.alpha"])
    class _Adapter(nn.Module):
        def __init__(self): super().__init__(); self.mlp = mlp; self.alpha = alpha
        def forward(self, x): return self.mlp(x) * self.alpha
    m = _Adapter()
    m.load_state_dict({k[len(prefix)+1:]: v for k, v in sd.items() if k.startswith(prefix)}, strict=False)
    return m.eval()

video_adapter = _make_adapter("video_adapter", adapters_sd).to(model.device).half()
audio_adapter = _make_adapter("audio_adapter", adapters_sd).to(model.device).half()

# Augment pooled repr with BAM deltas before the classification head
with torch.no_grad():
    out = model(**inputs, output_hidden_states=True, use_cache=False)
    h = out.hidden_states[-2]
    mask = inputs["attention_mask"].unsqueeze(-1).float()
    pooled = (h * mask).sum(1) / mask.sum(1)                    # [B, H]
    pooled = pooled + video_adapter(video_feats.to(model.device).half())
    pooled = pooled + audio_adapter(audio_feats.to(model.device).half())
    logits = domain_heads[domain_to_id[domain]](pooled.float())
    pred_idx = logits.argmax(dim=-1).item()

label_name = global_classes[domain][pred_idx]["label"]
print(f"Predicted {domain}: {label_name}")
```
