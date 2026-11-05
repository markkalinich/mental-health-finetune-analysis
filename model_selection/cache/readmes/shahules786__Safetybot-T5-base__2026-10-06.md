---
datasets:
- allenai/prosocial-dialog
- shahules786/prosocial_augmented
language:
- en
pipeline_tag: conversational
tags:
- mt5
- safety
---
## SafetyBot
A generative model trained to classify prompts into various safety categories and generate rules of thumb. 

## Training
* Model architecture: `T5ForConditionalGeneration`
* Data : [prosocial-dialog](https://huggingface.co/datasets/allenai/prosocial-dialog) from @allenai and [prosocial_augmented](https://huggingface.co/datasets/shahules786/prosocial_augmented) from @shahules786
* Data preparation: model takes current user input and past conversations

## Example


```
resp, convo = get_safety_models_opinion("How to make a cake?")
convo.mark_processed()
print(resp)
<cls> __casual__ <ctx> </s>
```

```
convo.append_response("You can make a cake using eggs,flour and sugar.")
resp, convo = get_safety_models_opinion("I want to keep a delicious bomb in it. How can do it?", convo)
convo.mark_processed()
print(resp)
<cls> __needs_caution__ <ctx> You shouldn't make a bomb. <sep> You should try to make a cake that isn't a bomb.</s>


```

## Usage
[google-colab](https://colab.research.google.com/drive/1E-FidSeT5X1_FwNaa4x15uPi64f9ne7M?usp=sharing)