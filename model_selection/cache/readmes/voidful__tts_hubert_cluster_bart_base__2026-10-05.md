---
language: en
datasets:
- librispeech
tags:
- audio
- automatic-speech-recognition
- speech
- asr
- hubert
license: apache-2.0
metrics:
- wer
- cer
---

# voidful/tts_hubert_cluster_bart_base


## Usage
````python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("voidful/tts_hubert_cluster_bart_base")
model = AutoModelForSeq2SeqLM.from_pretrained("voidful/tts_hubert_cluster_bart_base")
````
generate output
```python
gen_output = model.generate(input_ids=tokenizer("going along slushy country roads and speaking to damp audience in drifty school rooms day after day for a fortnight he'll have to put in an appearance at some place of worship on sunday morning and he can come to ask immediately afterwards",return_tensors='pt').input_ids, max_length=1024)
print(tokenizer.decode(gen_output[0], skip_special_tokens=True))
```

## Result
`:vtok402::vtok329::vtok329::vtok75::vtok75::vtok75::vtok44::vtok150::vtok150::vtok222::vtok280::vtok280::vtok138::vtok409::vtok409::vtok409::vtok46::vtok441:`