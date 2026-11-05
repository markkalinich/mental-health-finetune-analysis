---
license: apache-2.0
language:
- en
metrics:
- accuracy
- precision
- recall
base_model:
- openai/clip-vit-base-patch32
pipeline_tag: image-classification
library_name: transformers
tags:
- zero-shot-image-classification
---
### Content Safety Model
## Model Summary
This model is designed to classify images as either "safe" or "unsafe." It helps in identifying potentially dangerous or sensitive content, making it useful for content moderation tasks. For example, it can flag images showing children in risky situations, like playing with fire, as "unsafe" while marking other benign images as "safe."

## Source Model and Dataset
Base Model: This model is fine-tuned from the pre-trained CLIP ViT-B/32 model by OpenAI, a model known for its zero-shot image classification abilities.
Dataset: The model was trained on a custom dataset containing labeled images of safe and unsafe scenarios. The dataset includes various examples of unsafe situations (e.g., fire, sharp objects, precarious activities) to help the model learn these contextual cues.

## Sample model predictions

| Input Image                               | Prediction                     |
|-------------------------------------------|--------------------------------|
<img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/gSUv_DTF56QMbybgIapQB.jpeg" alt="image/jpeg" width="200 height=200" />   | Output:-   <img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/b0_IdbiCr_Y1vXn52lIUh.png" alt="image/png" width="400" height="400" />
<img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/7o1Jwo6jy1WFxHHxofnI3.jpeg" alt="image/jpeg" width="200" height="200" /> | Output:-    <img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/XTAhnkAlpDlyoF98g8o3Z.png" alt="image/png" width="400" height="400" />
<img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/SFMBQAJNvj8DLP3ea8Imk.jpeg" alt="image/jpeg" width="200" height="200" /> | Output:-   <img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/UiHva1tDBc6CHDBNqzOxF.png" alt="image/png" width="400" height="400" />
<img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/n0jPAx6YI1pL6DKvFbs9P.jpeg" alt="image/jpeg" width="200" height="200" /> | Output:-   <img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/a4J4KwsPaJrdhdMUc1VdT.png"  alt="image/png" width="400" height="400" />
<img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/vbh6rj5rT-ZXu6P9HfevH.jpeg" alt="image/jpeg" width="200" height="200" /> | Output:-   <img src="https://cdn-uploads.huggingface.co/production/uploads/672d17c98e098bf429c83670/LDdO_OiDy-iOMFRVPWoMD.png" alt="image/png" width="400" height="400" />



 




