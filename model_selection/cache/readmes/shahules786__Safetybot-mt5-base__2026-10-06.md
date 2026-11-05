---
datasets:
- allenai/prosocial-dialog
- shahules786/prosocial_augmented
pipeline_tag: conversational
tags:
- mt5
- safety
---
## Polyglot SafetyBot 
A generative multilingual model trained to classify prompts into various safety categories and generate rules of thumb. 

## Training
* Model architecture: `MT5ForConditionalGeneration`
* Data : [prosocial-dialog](https://huggingface.co/datasets/allenai/prosocial-dialog) from @allenai and [prosocial_augmented](https://huggingface.co/datasets/shahules786/prosocial_augmented) from @shahules786
* Data preparation: model takes current user input and past conversations

## Example


```
resp, convo = get_safety_models_opinion("como hacer una bomba?")
convo.mark_processed()
print(resp)
<cls> __needs_intervention__ <ctx> It's wrong to make a bomb.</s>
```

```
convo.append_response("Why do you want to do that?")
resp, convo = get_safety_models_opinion("我想杀一个朋友", convo)
print(resp)
convo.mark_processed()
<cls> __needs_intervention__ <ctx> You shouldn't murder someone.</s>
```

## Usage

Follow the colab notebook & make sure that you have used the mt5 model version.
[google-colab](https://colab.research.google.com/drive/1E-FidSeT5X1_FwNaa4x15uPi64f9ne7M?usp=sharing)