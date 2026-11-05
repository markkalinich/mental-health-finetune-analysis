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

# voidful/asr_hubert_cluster_bart_base


## Usage
download file
```shell
wget https://raw.githubusercontent.com/voidful/hubert-cluster-code/main/km_feat_100_layer_20
wget https://cdn-media.huggingface.co/speech_samples/sample1.flac
```

Hubert kmeans code
```python
import joblib
import torch
from transformers import Wav2Vec2FeatureExtractor, HubertModel
import soundfile as sf


class HubertCode(object):
    def __init__(self, hubert_model, km_path, km_layer):
        self.processor = Wav2Vec2FeatureExtractor.from_pretrained(hubert_model)
        self.model = HubertModel.from_pretrained(hubert_model)
        self.km_model = joblib.load(km_path)
        self.km_layer = km_layer
        self.C_np = self.km_model.cluster_centers_.transpose()
        self.Cnorm_np = (self.C_np ** 2).sum(0, keepdims=True)

        self.C = torch.from_numpy(self.C_np)
        self.Cnorm = torch.from_numpy(self.Cnorm_np)
        if torch.cuda.is_available():
            self.C = self.C.cuda()
            self.Cnorm = self.Cnorm.cuda()
            self.model = self.model.cuda()

    def __call__(self, filepath, sampling_rate=None):
        speech, sr = sf.read(filepath)
        input_values = self.processor(speech, return_tensors="pt", sampling_rate=sr).input_values
        if torch.cuda.is_available():
            input_values = input_values.cuda()
        hidden_states = self.model(input_values, output_hidden_states=True).hidden_states
        x = hidden_states[self.km_layer].squeeze()
        dist = (
                x.pow(2).sum(1, keepdim=True)
                - 2 * torch.matmul(x, self.C)
                + self.Cnorm
        )
        return dist.argmin(dim=1).cpu().numpy()
```
input
```python
hc = HubertCode("facebook/hubert-large-ll60k", './km_feat_100_layer_20', 20)
voice_ids = hc('./sample1.flac')
```
bart model
````python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("voidful/asr_hubert_cluster_bart_base")
model = AutoModelForSeq2SeqLM.from_pretrained("voidful/asr_hubert_cluster_bart_base")
````
generate output
```python
gen_output = model.generate(input_ids=tokenizer("".join([f":vtok{i}:" for i in voice_ids]),return_tensors='pt').input_ids,max_length=1024)
print(tokenizer.decode(gen_output[0], skip_special_tokens=True))
```

## Result
`going along slushy country roads and speaking to damp audience in drifty school rooms day after day for a fortnight he'll have to put in an appearance at some place of worship on sunday morning and he can come to ask immediately afterwards`
