---
language: en
license: apache-2.0
tags:
- pegasus
- seq2seq
- summarization
model-index:
- name: tuner007/pegasus_summarizer
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: train
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 36.604
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 14.6398
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 23.8845
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 32.9017
      verified: true
    - name: loss
      type: loss
      value: 2.5757133960723877
      verified: true
    - name: gen_len
      type: gen_len
      value: 76.3984
      verified: true
---

## Model description
[PEGASUS](https://github.com/google-research/pegasus) fine-tuned for summarization

## Install "sentencepiece" library required for tokenizer
```
pip install sentencepiece
```

## Model in Action 🚀
```
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
model_name = 'tuner007/pegasus_summarizer'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

def get_response(input_text):
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=1024, return_tensors="pt").to(torch_device)
  gen_out = model.generate(**batch,max_length=128,num_beams=5, num_return_sequences=1, temperature=1.5)
  output_text = tokenizer.batch_decode(gen_out, skip_special_tokens=True)
  return output_text
```
#### Example: 
context = """"
India wicket-keeper batsman Rishabh Pant has said someone from the crowd threw a ball on pacer Mohammed Siraj while he was fielding in the ongoing third Test against England on Wednesday. Pant revealed the incident made India skipper Virat Kohli "upset". "I think, somebody threw a ball inside, at Siraj, so he [Kohli] was upset," said Pant in a virtual press conference after the close of the first day\'s play."You can say whatever you want to chant, but don\'t throw things at the fielders and all those things. It is not good for cricket, I guess," he added.In the third session of the opening day of the third Test, a section of spectators seemed to have asked Siraj the score of the match to tease the pacer. The India pacer however came with a brilliant reply as he gestured 1-0 (India leading the Test series) towards the crowd.Earlier this month, during the second Test match, there was some bad crowd behaviour on a show as some unruly fans threw champagne corks at India batsman KL Rahul.Kohli also intervened and he was seen gesturing towards the opening batsman to know more about the incident. An over later, the TV visuals showed that many champagne corks were thrown inside the playing field, and the Indian players were visibly left frustrated.Coming back to the game, after bundling out India for 78, openers Rory Burns and Haseeb Hameed ensured that England took the honours on the opening day of the ongoing third Test.At stumps, England\'s score reads 120/0 and the hosts have extended their lead to 42 runs. For the Three Lions, Burns (52*) and Hameed (60*) are currently unbeaten at the crease.Talking about the pitch on opening day, Pant said, "They took the heavy roller, the wicket was much more settled down, and they batted nicely also," he said. "But when we batted, the wicket was slightly soft, and they bowled in good areas, but we could have applied [ourselves] much better."Both England batsmen managed to see off the final session and the hosts concluded the opening day with all ten wickets intact, extending the lead to 42.(ANI)
"""

```
get_response(context)
```
#### Output:
Team India wicketkeeper-batsman Rishabh Pant has said that Virat Kohli was "upset" after someone threw a ball on pacer Mohammed Siraj while he was fielding in the ongoing third Test against England. "You can say whatever you want to chant, but don't throw things at the fielders and all those things. It's not good for cricket, I guess," Pant added.'

#### [Inshort](https://www.inshorts.com/) (60 words News summary app, rated 4.4 by 5,27,246+ users on android playstore) summary:
India wicketkeeper-batsman Rishabh Pant has revealed that captain Virat Kohli was upset with the crowd during the first day of Leeds Test against England because someone threw a ball at pacer Mohammed Siraj. Pant added, "You can say whatever you want to chant, but don't throw things at the fielders and all those things. It is not good for cricket."


> Created by [Arpit Rajauria](https://twitter.com/arpit_rajauria)
[![Twitter icon](https://cdn0.iconfinder.com/data/icons/shift-logotypes/32/Twitter-32.png)](https://twitter.com/arpit_rajauria)
