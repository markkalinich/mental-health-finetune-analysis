---
license: apache-2.0
pipeline_tag: feature-extraction
library_name: sentence-transformers
tags:
  - transformers
  - sentence-transformers
  - feature-extraction
  - multimodal-embedding
---

# LCO-Embedding: Scaling Language-Centric Omnimodal Representation Learning

We are thrilled to release LCO-Embedding - a language-centric omnimodal representation learning framework and the LCO-Embedding model families!

This model implements the framework presented in the paper [Scaling Language-Centric Omnimodal Representation Learning](https://huggingface.co/papers/2510.11693), accepted by NeurIPS 2025.

**Project Page:** https://huggingface.co/LCO-Embedding

**Github Repository:** https://github.com/LCO-Embedding/LCO-Embedding


## Quick Start

Note: We are only using the `thinker` component of Qwen2.5 Omni and drops the `talker` component.

### Using Sentence Transformers

Install Sentence Transformers with the multimodal extras (for image, audio, and video support):

```bash
pip install "sentence_transformers[image,audio,video]" "transformers>=5.6.0"
```

```python
import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "LCO-Embedding/LCO-Embedding-Omni-7B",
    model_kwargs={
        "torch_dtype": torch.bfloat16,
        "attn_implementation": "flash_attention_2",  # pip install kernels; recommended but not mandatory
    },
)
```

The same "Summarize the above <modality> in one word:" instruction used in the paper is baked into the chat template, so `encode()` takes plain text, file paths, URLs, or multimodal dicts directly.

#### Text Retrieval
```python
query = "What is the tallest mountain in the world?"
documents = [
    "Mount Everest is Earth's highest mountain above sea level, located in the Mahalangur Himal sub-range of the Himalayas. Its elevation of 8,848.86 metres was established by a joint Chinese-Nepali survey in 2020.",
    "K2, at 8,611 metres above sea level, is the second-highest mountain on Earth, after Mount Everest. It lies in the Karakoram range on the China-Pakistan border.",
    "Mount Kilimanjaro is a dormant volcano in Tanzania. It is the highest mountain in Africa, with its summit about 5,895 metres above sea level.",
]

query_embedding = model.encode(query)
document_embeddings = model.encode(documents)
print(model.similarity(query_embedding, document_embeddings))
# tensor([[0.6456, 0.4331, 0.4788]])
```

#### Image Retrieval
```python
query = "How many input modalities does Qwen2.5-Omni support?"
documents = [
    "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/qwen2.5omni_hgf.png",
    "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/llama4_hgf.png",
]

query_embedding = model.encode(query)
document_embeddings = model.encode(documents, batch_size=1)
print(model.similarity(query_embedding, document_embeddings))
# tensor([[0.5745, 0.4818]])
```

#### Audio Retrieval
```python
query = "A light piano piece"
documents = [
    "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/joe_hisaishi_summer.mp3",
    "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/jay_chou_superman_cant_fly.mp3",
]

query_embedding = model.encode(query)
document_embeddings = model.encode(documents, batch_size=1)
print(model.similarity(query_embedding, document_embeddings))
# tensor([[0.4958, 0.0964]])
```

#### Video Retrieval
```python
# For video on smaller GPUs, cap the processor up front:
model[0].processing_kwargs.update({
    "video": {"max_pixels": 64 * 28 * 28, "do_sample_frames": True, "fps": 1},
})

query = "How to cook Mapo Tofu?"
documents = [
    "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/mapo_tofu.mp4",
    "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/zhajiang_noodle.mp4",
]

query_embedding = model.encode(query)
document_embeddings = model.encode(documents, batch_size=1)
print(model.similarity(query_embedding, document_embeddings))
# tensor([[0.6638, 0.4841]])
```

#### Multimodal Inputs

To embed a document that combines multiple modalities, pass a dict with any combination of `"text"`, `"image"`, `"audio"`, and `"video"` keys instead of a single path or string:

```python
documents = [
    {
        "text": "A cooking tutorial for Mapo Tofu",
        "video": "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/mapo_tofu.mp4",
    },
    {
        "image": "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/qwen2.5omni_hgf.png",
        "audio": "https://huggingface.co/Tevatron/OmniEmbed-v0.1/resolve/main/assets/joe_hisaishi_summer.mp3",
    },
]
document_embeddings = model.encode(documents, batch_size=1)
```

### Using Transformers

```python
from transformers import Qwen2_5OmniThinkerForConditionalGeneration, Qwen2_5OmniProcessor
from qwen_omni_utils import process_mm_info

processor = Qwen2_5OmniProcessor.from_pretrained("LCO-Embedding/LCO-Embedding-Omni-7B") # or add a `max_pixels = 1280*28*28' for efficient encoding
model = Qwen2_5OmniThinkerForConditionalGeneration.from_pretrained("LCO-Embedding/LCO-Embedding-Omni-7B",
                                                                    torch_dtype=torch.bfloat16,
                                                                    device_map="auto")
```

#### Text Batch Encodings:
  
```python
texts = ["some random text", "a second random text", "a third random text"] * 30
batch_size = 8
text_prompt =  "{}\nSummarize the above text in one word:" 

all_text_embeddings = []

with torch.no_grad():
    for i in tqdm(range(0, len(texts), batch_size)):
        batch_texts = texts[i : i + batch_size]
        batch_texts = [text_prompt.format(text) for text in batch_texts]
        messages = [[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text":text},
                ],

            }
        ] for text in batch_texts]
        text_inputs = processor.apply_chat_template(messages, tokenize = False, add_generation_prompt = True)
        text_inputs = processor(
        text = text_inputs,
        padding = True,
        return_tensors = "pt",
        )
        text_inputs = text_inputs.to("cuda")
        text_outputs = model(
            **text_inputs, output_hidden_states=True, return_dict=True
        ).hidden_states[-1][:, -1, :]
        all_text_embeddings.append(text_outputs.to(torch.float16).cpu())

all_text_embeddings = torch.cat(all_text_embeddings, dim=0)
```

#### Image Batch Encodings: 

```python
images = [some random PIL.Image] * 100 # will be good to load them using dataloader; see MIEB evaluation pipeline
image_prompt = "\nSummarize the above image in one word:"
batch_size = 8

all_image_embeddings = []

with torch.no_grad():
    for i in tqdm(range(0, len(images), batch_size)):
        batch_images = images[i : i + batch_size]
        messages = [[
            {
                "role": "user",
                "content": [
                    {"type": "image", "image":image},
                    {"type": "text", "text": image_prompt},
                ],

            }
        ] for image in batch_images]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        audio_inputs, image_inputs, video_inputs = process_mm_info(messages, use_audio_in_video=True)
        inputs = processor(
            text=text, 
            audio=audio_inputs, 
            images=image_inputs, 
            videos=video_inputs, 
            return_tensors="pt", 
            padding=True
        )
        inputs = inputs.to("cuda")
        image_outputs = model(
            **inputs, output_hidden_states=True, return_dict=True
        ).hidden_states[-1][:, -1, :]
        all_image_embeddings.append(image_outputs.to(torch.float16).cpu())

all_image_embeddings = torch.cat(all_image_embeddings, dim=0)
```

#### Audio Batch Encoding:

```python
import logging
logging.getLogger("root").setLevel(logging.ERROR)
# set this to prevent getting the Qwen Omni system prompt mismatch warning.

batch_size = 4
audio_prompt = "\nSummarize the above audio in one word:"
audis = [some audios]  * 1000

all_audio_embeddings = []

with torch.no_grad():
  for i in tqdm(range(0, len(audios), batch_size)):
      torch.cuda.empty_cache()
      
      batch_audios = audios[i : i + batch_size]
      messages = [[
          {
              "role": "user",
              "content": [
                   {"type": "audio", "audio": audio},
                  {"type": "text", "text": audio_prompt},
              ],
              
          }
      ] for audio in batch_audios]
      
      text = processor.apply_chat_template(
          messages, tokenize=False, add_generation_prompt=True
      )
      audio_inputs, image_inputs, video_inputs = process_mm_info(
          messages, use_audio_in_video=False
      )
      inputs = processor(
          text=text, 
          audio=audio_inputs, 
          images=image_inputs, 
          videos=video_inputs, 
          return_tensors="pt", 
          padding=True
      )
      inputs = inputs.to("cuda")
      audio_outputs = model(
          **inputs, output_hidden_states=True, return_dict=True
      ).hidden_states[-1][:, -1, :]   
      all_audio_embeddings.append(audio_outputs.to(torch.float16).cpu())
      del inputs, audio_outputs
      torch.cuda.empty_cache()
                
all_audio_embeddings = torch.cat(all_audio_embeddings, dim=0)

```

#### Video Batch Encoding:


```python
videos = [some videos]  * 1000
video_prompt = "\nSummarize the above video in one word:"
batch_size = 4

long_video = False
# followed by some example hyperparameters to save RAM
# for long videos. Not optimal. Tune case by case.

all_video_embeddings = []
with torch.no_grad():
  for i in tqdm(range(0, len(videos), batch_size)):
      torch.cuda.empty_cache()
      
      batch_videos = videos[i : i + batch_size]
      if long_video:
          messages = [[
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "video", 
                          "video": video, 
                          "max_pixels": 224 * 224,
                          "fps": 1,
                          "max_frames": 10
                      },
                      {"type": "text", "text": video_prompt},
                  ],

              }
          ] for video in batch_videos]
      else:
          messages = [[
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "video", 
                          "video": video, 
                      },
                      {"type": "text", "text": video_prompt},
                  ],

              }
          ] for video in batch_videos]
      
      text = processor.apply_chat_template(
          messages, tokenize=False, add_generation_prompt=True
      )
      audio_inputs, image_inputs, video_inputs = process_mm_info(
          messages, use_audio_in_video=False
      )
      inputs = processor(
          text=text, 
          audio=audio_inputs, 
          images=image_inputs, 
          videos=video_inputs, 
          return_tensors="pt", 
          padding=True
      )
      inputs = inputs.to("cuda")
      video_outputs = model(
          **inputs, output_hidden_states=True, return_dict=True
      ).hidden_states[-1][:, -1, :]   
      all_video_embeddings.append(video_outputs.to(torch.float16).cpu())
      
      del inputs, video_outputs
      torch.cuda.empty_cache()
                
all_video_embeddings = torch.cat(all_video_embeddings, dim=0)
```

## Overview

We introduce **LCO-Embedding**, a language-centric omnimodal representation learning method and the LCO-Embedding model families, setting a new state-of-the-art on [MIEB](https://huggingface.co/blog/isaacchung/introducing-mieb) (Massive Image Embedding Benchmark), while supporting audio and videos.

This work also introduces the **Generation-Representation Scaling Law**, connecting models' generative capabilities and their representation upper bound. Furthermore, we introduce **SeaDoc**, a challenging visual document retrieval task in Southeast Asian languages, and show that continual generative pretraining before contrastive learning raises the representation upper bound.

<div align='center'><img src="https://cdn-uploads.huggingface.co/production/uploads/604f67ef0fe8ff3ec13d71ef/4Wd8fDFBdT6GxqN6-KzZN.png" alt="overview" width="100%"/></div>

## Evaluation Results

We evaluate LCO-Embedding with state-of-the-art embedding models, including E5-V, Voyage Multimodal 3, mmE5, and GME, on a MIEB-Lite benchmark (51 tasks) broken down by task categories.

<div align='center'><img src="https://cdn-uploads.huggingface.co/production/uploads/63108cc834c7d77420b0fd68/63WBsKh57HbNwwe3bZ-oZ.png" alt="mieb_lite" width="100%"/></div>

LCO-Embedding is also SOTA on MAEB (massive audio embedding benchmark) without even training on audio. Screenshot from the MAEB paper.

![image](https://cdn-uploads.huggingface.co/production/uploads/63108cc834c7d77420b0fd68/cp5hfBmm51AlyO4sDnTrN.png)

Performance and efficiency comparisons of different training strategies using 3B and 7B variants of Qwen2.5-VL backbones.

<div align='center'><img src="https://github.com/LCO-Embedding/LCO-Embedding/raw/main/assets/lora_ablation.png" alt="lora_ablation" width="100%"/></div>

Scaling relationship between generation benchmark performance (X-axis) and representation benchmark performance after language-centric contrastive learning (Y-axis).

<div align='center'><img src="https://github.com/LCO-Embedding/LCO-Embedding/raw/main/assets/scaling.png" alt="scaling_law" width="100%"/></div>

## Citation

If you find LCO-Embedding useful for your research and applications, please cite using this BibTeX:

```bibtex
@article{xiao2025scaling,
  title={Scaling Language-Centric Omnimodal Representation Learning},
  author={Xiao, Chenghao and Chan, Hou Pong and Zhang, Hao and Xu, Weiwen and Aljunied, Mahani and Rong, Yu},
  journal={arXiv preprint arXiv:2510.11693},
  year={2025}
}
```