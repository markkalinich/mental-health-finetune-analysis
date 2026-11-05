---
license: mit
pipeline_tag: image-text-to-text
library_name: transformers
base_model:
 - OpenGVLab/InternVL2-1B
base_model_relation: merge
language:
- multilingual
tags:
- internvl
- custom_code
---

# Mini-InternVL2-DA-RS

[\[📂 GitHub\]](https://github.com/OpenGVLab/InternVL)  [\[🆕 Blog\]](https://internvl.github.io/blog/)  [\[📜 Mini-InternVL\]](https://arxiv.org/abs/2410.16261) [\[📜 InternVL 1.0\]](https://arxiv.org/abs/2312.14238)  [\[📜 InternVL 1.5\]](https://arxiv.org/abs/2404.16821)  [\[📜 InternVL 2.5\]](https://huggingface.co/papers/2412.05271)

[\[🗨️ InternVL Chat Demo\]](https://internvl.opengvlab.com/)  [\[🤗 HF Demo\]](https://huggingface.co/spaces/OpenGVLab/InternVL)  [\[🚀 Quick Start\]](#quick-start)  [\[📖 中文解读\]](https://zhuanlan.zhihu.com/p/706547971)  [\[📖 Documents\]](https://internvl.readthedocs.io/en/latest/internvl2.0/domain_adaptation.html#data-preparation)


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64564b0e4a7ffb7d5a47f412/Qp9tEtBAjbq39bJZ7od4A.png)

## Introduction

We release the adaptation models for the specific domains: autonomous driving, medical images, and remote sensing.

These models are built upon Mini-InternVL and fine-tuned using a unified adaptation framework, achieving good performance on tasks in specific domains.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64564b0e4a7ffb7d5a47f412/rlz4XL8DFWXplvp0Yx4lg.png)

<table>
  <tr>
    <th>Model Name</th>
    <th>HF Link</th>
    <th>Note</th>
  </tr>
  <tr>
    <td>Mini-InternVL2-DA-Drivelm</td>
    <td><a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-1B-DA-Drivelm">🤗1B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-2B-DA-Drivelm">🤗2B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-4B-DA-Drivelm">🤗4B</a></td>
    <td> Adaptation for <a href="https://github.com/OpenDriveLab/DriveLM/tree/main/challenge"> CVPR 2024 Autonomous Driving Challenge </a></td>
  </tr>
  <tr>
    <td>Mini-InternVL2-DA-BDD</td>
    <td><a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-1B-DA-BDD">🤗1B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-2B-DA-BDD">🤗2B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-4B-DA-BDD">🤗4B</a></td>
    <td> Fine-tuning with data constructed by <a href="https://tonyxuqaq.github.io/projects/DriveGPT4/"> DriveGPT4 </a></td>
  </tr>
  <tr>
    <td>Mini-InternVL2-DA-RS</td>
    <td><a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-1B-DA-RS">🤗1B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-2B-DA-RS">🤗2B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-4B-DA-RS">🤗4B</a></td>
    <td> Adaptation for remote sensing domain </td>
  </tr>
  <tr>
    <td>Mini-InternVL2-DA-Medical</td>
    <td><a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-1B-DA-Medical">🤗1B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-2B-DA-Medical">🤗2B</a> / <a href="https://huggingface.co/OpenGVLab/Mini-InternVL2-4B-DA-Medical">🤗4B</a></td>
    <td> Fine-tuning using our <a href="https://huggingface.co/datasets/OpenGVLab/InternVL-Domain-Adaptation-Data/blob/main/train_meta/internvl_1_2_finetune_medical.json">medical data</a>.</td>
  </tr>
</table>

The script for evaluation is in the [document](https://internvl.readthedocs.io/en/latest/internvl2.0/domain_adaptation.html#id3).

## Training datasets

- General domain dataset:

    ShareGPT4V, AllSeeingV2, LLaVA-Instruct-ZH, DVQA, ChartQA, AI2D, DocVQA, GeoQA+, SynthDoG-EN

- Medicalt dataset:

    PMC-OA, MedICaT, Open-i, MedPix, Quilt-1M, RP3D, MIMIC-CXR, Retina Image Bank and others

## Quick Start

We provide an example code to run `Mini-InternVL2-1B` using `transformers`.

> Please use transformers>=4.37.2 to ensure the model works normally.


```python
import numpy as np
import torch
import torchvision.transforms as T
from decord import VideoReader, cpu
from PIL import Image
from torchvision.transforms.functional import InterpolationMode
from transformers import AutoModel, AutoTokenizer

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)

def build_transform(input_size):
    MEAN, STD = IMAGENET_MEAN, IMAGENET_STD
    transform = T.Compose([
        T.Lambda(lambda img: img.convert('RGB') if img.mode != 'RGB' else img),
        T.Resize((input_size, input_size), interpolation=InterpolationMode.BICUBIC),
        T.ToTensor(),
        T.Normalize(mean=MEAN, std=STD)
    ])
    return transform

def find_closest_aspect_ratio(aspect_ratio, target_ratios, width, height, image_size):
    best_ratio_diff = float('inf')
    best_ratio = (1, 1)
    area = width * height
    for ratio in target_ratios:
        target_aspect_ratio = ratio[0] / ratio[1]
        ratio_diff = abs(aspect_ratio - target_aspect_ratio)
        if ratio_diff < best_ratio_diff:
            best_ratio_diff = ratio_diff
            best_ratio = ratio
        elif ratio_diff == best_ratio_diff:
            if area > 0.5 * image_size * image_size * ratio[0] * ratio[1]:
                best_ratio = ratio
    return best_ratio

def dynamic_preprocess(image, min_num=1, max_num=12, image_size=448, use_thumbnail=False):
    orig_width, orig_height = image.size
    aspect_ratio = orig_width / orig_height

    # calculate the existing image aspect ratio
    target_ratios = set(
        (i, j) for n in range(min_num, max_num + 1) for i in range(1, n + 1) for j in range(1, n + 1) if
        i * j <= max_num and i * j >= min_num)
    target_ratios = sorted(target_ratios, key=lambda x: x[0] * x[1])

    # find the closest aspect ratio to the target
    target_aspect_ratio = find_closest_aspect_ratio(
        aspect_ratio, target_ratios, orig_width, orig_height, image_size)

    # calculate the target width and height
    target_width = image_size * target_aspect_ratio[0]
    target_height = image_size * target_aspect_ratio[1]
    blocks = target_aspect_ratio[0] * target_aspect_ratio[1]

    # resize the image
    resized_img = image.resize((target_width, target_height))
    processed_images = []
    for i in range(blocks):
        box = (
            (i % (target_width // image_size)) * image_size,
            (i // (target_width // image_size)) * image_size,
            ((i % (target_width // image_size)) + 1) * image_size,
            ((i // (target_width // image_size)) + 1) * image_size
        )
        # split the image
        split_img = resized_img.crop(box)
        processed_images.append(split_img)
    assert len(processed_images) == blocks
    if use_thumbnail and len(processed_images) != 1:
        thumbnail_img = image.resize((image_size, image_size))
        processed_images.append(thumbnail_img)
    return processed_images

def load_image(image_file, input_size=448, max_num=12):
    image = Image.open(image_file).convert('RGB')
    transform = build_transform(input_size=input_size)
    images = dynamic_preprocess(image, image_size=input_size, use_thumbnail=True, max_num=max_num)
    pixel_values = [transform(image) for image in images]
    pixel_values = torch.stack(pixel_values)
    return pixel_values

# If you want to load a model using multiple GPUs, please refer to the `Multiple GPUs` section.
path = 'OpenGVLab/Mini-InternVL2-1B-DA-Medical'
model = AutoModel.from_pretrained(
    path,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    use_flash_attn=True,
    trust_remote_code=True).eval().cuda()
tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True, use_fast=False)

# set the max number of tiles in `max_num`
pixel_values = load_image('path/to/image.jpg', max_num=12).to(torch.bfloat16).cuda()
generation_config = dict(max_new_tokens=1024, do_sample=True)

# pure-text conversation (纯文本对话)
question = 'Hello, who are you?'
response, history = model.chat(tokenizer, None, question, generation_config, history=None, return_history=True)
print(f'User: {question}\nAssistant: {response}')

question = 'Can you tell me a story?'
response, history = model.chat(tokenizer, None, question, generation_config, history=history, return_history=True)
print(f'User: {question}\nAssistant: {response}')

# single-image single-round conversation (单图单轮对话)
question = '<image>\nPlease describe the image shortly.'
response = model.chat(tokenizer, pixel_values, question, generation_config)
print(f'User: {question}\nAssistant: {response}')

# single-image multi-round conversation (单图多轮对话)
question = '<image>\nPlease describe the image in detail.'
response, history = model.chat(tokenizer, pixel_values, question, generation_config, history=None, return_history=True)
print(f'User: {question}\nAssistant: {response}')

question = 'Please write a poem according to the image.'
response, history = model.chat(tokenizer, pixel_values, question, generation_config, history=history, return_history=True)
print(f'User: {question}\nAssistant: {response}')

# multi-image multi-round conversation, combined images (多图多轮对话，拼接图像)
pixel_values1 = load_image('path/to/image1.jpg', max_num=12).to(torch.bfloat16).cuda()
pixel_values2 = load_image('path/to/image2.jpg', max_num=12).to(torch.bfloat16).cuda()
pixel_values = torch.cat((pixel_values1, pixel_values2), dim=0)

question = '<image>\nDescribe the two images in detail.'
response, history = model.chat(tokenizer, pixel_values, question, generation_config,
                               history=None, return_history=True)
print(f'User: {question}\nAssistant: {response}')

question = 'What are the similarities and differences between these two images.'
response, history = model.chat(tokenizer, pixel_values, question, generation_config,
                               history=history, return_history=True)
print(f'User: {question}\nAssistant: {response}')

# multi-image multi-round conversation, separate images (多图多轮对话，独立图像)
pixel_values1 = load_image('path/to/image1.jpg', max_num=12).to(torch.bfloat16).cuda()
pixel_values2 = load_image('path/to/image2.jpg', max_num=12).to(torch.bfloat16).cuda()
pixel_values = torch.cat((pixel_values1, pixel_values2), dim=0)
num_patches_list = [pixel_values1.size(0), pixel_values2.size(0)]

question = 'Image-1: <image>\nImage-2: <image>\nDescribe the two images in detail.'
response, history = model.chat(tokenizer, pixel_values, question, generation_config,
                               num_patches_list=num_patches_list,
                               history=None, return_history=True)
print(f'User: {question}\nAssistant: {response}')

question = 'What are the similarities and differences between these two images.'
response, history = model.chat(tokenizer, pixel_values, question, generation_config,
                               num_patches_list=num_patches_list,
                               history=history, return_history=True)
print(f'User: {question}\nAssistant: {response}')

# batch inference, single image per sample (单图批处理)
pixel_values1 = load_image('path/to/image1.jpg', max_num=12).to(torch.bfloat16).cuda()
pixel_values2 = load_image('path/to/image1.jpg', max_num=12).to(torch.bfloat16).cuda()
num_patches_list = [pixel_values1.size(0), pixel_values2.size(0)]
pixel_values = torch.cat((pixel_values1, pixel_values2), dim=0)

questions = ['<image>\nDescribe the image in detail.'] * len(num_patches_list)
responses = model.batch_chat(tokenizer, pixel_values,
                             num_patches_list=num_patches_list,
                             questions=questions,
                             generation_config=generation_config)
for question, response in zip(questions, responses):
    print(f'User: {question}\nAssistant: {response}')

```
## Citation

If you find this project useful in your research, please consider citing:

```BibTeX
@article{gao2024mini,
  title={Mini-internvl: A flexible-transfer pocket multimodal model with 5\% parameters and 90\% performance},
  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},
  journal={arXiv preprint arXiv:2410.16261},
  year={2024}
}
@article{chen2024expanding,
  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},
  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and Liu, Zhaoyang and others},
  journal={arXiv preprint arXiv:2412.05271},
  year={2024}
}
@article{chen2024far,
  title={How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},
  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and Ye, Shenglong and Gao, Zhangwei and Cui, Erfei and Tong, Wenwen and Hu, Kongzhi and Luo, Jiapeng and Ma, Zheng and others},
  journal={arXiv preprint arXiv:2404.16821},
  year={2024}
}
@inproceedings{chen2024internvl,
  title={Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks},
  author={Chen, Zhe and Wu, Jiannan and Wang, Wenhai and Su, Weijie and Chen, Guo and Xing, Sen and Zhong, Muyan and Zhang, Qinglong and Zhu, Xizhou and Lu, Lewei and others},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={24185--24198},
  year={2024}
}
```