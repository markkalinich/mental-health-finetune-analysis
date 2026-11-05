---
tags:
- mteb
- sentence-transformers
- transformers
- embedding
- bidirectional
- multilingual
pipeline_tag: sentence-similarity
license: apache-2.0
base_model: BidirLM/BidirLM-Omni-2.5B-Embedding
language:
- multilingual
- af
- am
- ar
- az
- be
- bg
- bn
- bs
- ca
- ceb
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fa
- fi
- fr
- ga
- gl
- gu
- ha
- he
- hi
- hr
- ht
- hu
- hy
- id
- ig
- is
- it
- ja
- jv
- ka
- kk
- kn
- ko
- ky
- lt
- lv
- mg
- mk
- ml
- mr
- ms
- mt
- my
- nb
- ne
- nl
- nso
- ny
- pa
- pl
- ps
- pt
- ro
- ru
- sd
- si
- sk
- sl
- sn
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- uk
- ur
- vi
- wo
- xh
- yo
- zh
- zu
library_name: sentence-transformers
datasets:
- BidirLM/BidirLM-Omni-Contrastive
---

# BidirLM-Omni-2.5B

BidirLM-Omni is the omnimodal variant of the BidirLM family — a 2.5B bidirectional encoder that jointly embeds **text, images, and audio** into a shared representation space, enabling **state-of-the-art** embedding performance.

![Omnimodal model performance: MTEB Multilingual V2, MIEB (lite), MAEB (beta)](https://huggingface.co/spaces/BidirLM/README/resolve/main/fig6.png)

> [!WARNING]
> This model should be run with **cuDNN > 9.20.0**. Earlier versions trigger a [Conv3D NVIDIA bug](https://forums.developer.nvidia.com/t/cudnn-bug-report-conv3d-performance-regression-with-bfloat16-float16-on-h100/355210) that significantly slows down inference or training.

## Supported Tasks

**Multimodal embeddings** (via Sentence Transformers): cross-modal retrieval (text ↔ image, text ↔ audio), multimodal semantic similarity, clustering, and classification across text, image, and audio modalities.

**Text-only downstream fine-tuning** (via Transformers): sequence classification (e.g. MNLI, XNLI), token classification (e.g. NER), sequence regression.

**Supported Languages** Multilingual support across over 119 languages, inherited from the Qwen3 base model and reinforced through contrastive training with 87 languages.

## Usage

### Sentence Transformers

Pass inputs directly to `encode()`. All modalities produce embeddings in the same 2048-dimensional space and can be compared cross-modally.

| Modality | Input type | Notes |
|----------|-----------|-------|
| **Text** | `str` | Any language; no length limit (model context is 32k tokens) |
| **Image** | `PIL.Image.Image` | Any size and aspect ratio; resized internally |
| **Audio** | `np.ndarray`, `list[float]`, or `dict` with `"array"` (`np.ndarray`) and `"sampling_rate"` (`int`) | Any sample rate; resampled to 16 kHz internally via `librosa` |
| **Mixed** | `list[dict]` conversation (role/content) | Interleave text + image or text + audio in a single prompt — see *Chat Template* below |

```python
import numpy as np
import PIL.Image
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BidirLM/BidirLM-Omni-2.5B-Embedding", trust_remote_code=True)

# Text queries
texts = [
    "An image with a red background.",
    "An image with a blue background.",
    "A deep bass sound.",
    "A high-pitched sound.",
]

# Images, synthetic solid-color 256x256 images
images = [
    PIL.Image.fromarray(np.full((256, 256, 3), (220, 30, 30), dtype=np.uint8)),  # red
    PIL.Image.fromarray(np.full((256, 256, 3), (30, 30, 220), dtype=np.uint8)),  # blue
]

# Audio, synthetic sine waves at 16kHz, 2 seconds each
sr = 16000
t  = np.linspace(0, 2.0, sr * 2, endpoint=False, dtype=np.float32)
audios = [
    {"array": np.sin(2 * np.pi *   80 * t), "sampling_rate": sr},  #   80 Hz — bass
    {"array": np.sin(2 * np.pi * 7500 * t), "sampling_rate": sr},  # 7500 Hz — high
]

# Encode all modalities and compute similarities
text_embeddings  = model.encode(texts)
image_embeddings = model.encode(images)
audio_embeddings = model.encode(audios)

# Pass a custom instruction via prompt= (applies to all items in the batch)
# text_embeddings  = model.encode(texts, prompt="Retrieve semantically similar text.")

print(model.similarity(text_embeddings, image_embeddings))
print(model.similarity(text_embeddings, audio_embeddings))

# Text-Image similarity             red img   blue img
# "An image with a red background." [ 0.6928,   0.3103]  ← high red match
# "An image with a blue background."[ 0.4278,   0.6436]  ← high blue match
# "A deep bass sound."              [ 0.1519,   0.2272]  ← low (text/image mismatch)
# "A high-pitched sound."           [ 0.1418,   0.1812]  ← low (text/image mismatch)

# Text-Audio similarity             80Hz bass  7500Hz high
# "An image with a red background." [ 0.0010,   0.0410]  ← low (image/audio mismatch)
# "An image with a blue background."[ 0.0526,   0.0642]  ← low (image/audio mismatch)
# "A deep bass sound."              [ 0.5456,   0.4243]  ← higher bass match
# "A high-pitched sound."           [ 0.4004,   0.5177]  ← higher high-pitch match
```


### Transformers - Fine-tuning for Downstream Tasks

```python
import numpy as np
import PIL.Image
from transformers import AutoProcessor, AutoModelForSequenceClassification, AutoModelForTokenClassification

processor = AutoProcessor.from_pretrained(
    "BidirLM/BidirLM-Omni-2.5B-Embedding", trust_remote_code=True
)

sr = 16000
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": PIL.Image.fromarray(np.zeros((256, 256, 3), dtype=np.uint8))},
            {"type": "audio", "audio": {"array": np.zeros(sr, dtype=np.float32), "sampling_rate": sr}},
            {"type": "text",  "text": "Your text."},
        ],
    }
]
processor.apply_chat_template(conversation, tokenize=True, add_generation_prompt=False)


# Sequence classification (e.g., NLI)
seq_model = AutoModelForSequenceClassification.from_pretrained(
    "BidirLM/BidirLM-Omni-2.5B-Embedding",
    trust_remote_code=True,
    num_labels=3,
)

# Token classification (e.g., NER)
tok_model = AutoModelForTokenClassification.from_pretrained(
    "BidirLM/BidirLM-Omni-2.5B-Embedding",
    trust_remote_code=True,
    num_labels=7,
)
```

## Requirements

```
transformers>=5.5.0
sentence-transformers>=5.4.0
librosa>=0.10.0
```

## FAQ

### 1. What pooling strategy does this model use?

The model uses **mean pooling** across all modalities. This is handled automatically when using Sentence Transformers.

### 2. Do I need `trust_remote_code=True`?

Yes. BidirLM-Omni uses a custom bidirectional omnimodal architecture that requires loading custom code from the repository.

### 3. Can I compare embeddings across modalities?

Yes. Text, image, and audio embeddings live in the same 2048-dimensional space and can be compared directly using cosine similarity.

### 4. What audio formats and sample rates are supported?

Any sample rate is accepted — the model resamples internally using `librosa` when the source rate differs from the native 16 kHz. Three input formats are supported:

- `np.ndarray` — a 1-D float32 array of raw samples
- `list[float]` — a plain Python list of samples
- `dict` with `"array"` (`np.ndarray`) and `"sampling_rate"` (`int`) — the format returned by HuggingFace `datasets` Audio features

Any audio format readable by standard libraries (WAV, MP3, FLAC, etc.) can be used by loading it into a NumPy array first (e.g. with `librosa.load` or `soundfile.read`).

## Citation

```bibtex
@misc{boizard2026bidirlmtextomnimodalbidirectional,
      title={BidirLM: From Text to Omnimodal Bidirectional Encoders by Adapting and Composing Causal LLMs}, 
      author={Nicolas Boizard and Théo Deschamps-Berger and Hippolyte Gisserot-Boukhlef and Céline Hudelot and Pierre Colombo},
      year={2026},
      eprint={2604.02045},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2604.02045}, 
}
```