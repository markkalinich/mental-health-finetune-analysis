---
base_model:
  - facebook/wav2vec2-large-xlsr-53
language:
  - en
license:
  - cc-by-nc-4.0
pipeline_tag: audio-classification
tags:
  - audio
  - classification
  - audio-classification
  - Wav2Vec2
  - sentiment
  - earnings conference calls
  - transformers

widget:
- src: negative.mp3
  example_title: Negative speech sample
  output:
  - label: positive
    score: 0.00
  - label: neutral
    score: 0.01
  - label: negative
    score: 0.99

- src: neutral.mp3
  example_title: Neutral speech sample
  output:
  - label: positive
    score: 0.00
  - label: neutral
    score: 0.99
  - label: negative
    score: 0.00

- src: positive.mp3
  example_title: Positive speech sample
  output:
  - label: positive
    score: 0.94
  - label: neutral
    score: 0.06
  - label: negative
    score: 0.00

---

# FinVoc2Vec
We introduce FinVoc2Vec, a vocal tone classifier designed for real-world corporate disclosures.
In the first stage, we apply a self-supervised pre-training procedure that allows the base model to adapt to the acoustic characteristics of disclosure environments using a sample of 500,000 unlabeled sentences of conference call speech. In the second stage, we apply a supervised fine-tuning procedure that enables the model to learn representations of human-labeled vocal tone. We construct a speech corpus containing 
5,000 audio recordings of linguistically neutral sentences from conference calls and manually label each sentence with perceived vocal tone — positive, negative, or neutral.
We cannot make the labeled audio data publicly available due to third-party property rights. However, interested researchers with an active license may contact us directly to explore potential access options.

## Example using a demo dataset
```python
import torch
from datasets import load_dataset
from transformers import Wav2Vec2FeatureExtractor, AutoModel
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"

# load model and feature extractor
model = AutoModel.from_pretrained("waiv/FinVoc2Vec", trust_remote_code=True).to(device)
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("waiv/FinVoc2Vec")

# load dataset
demo_dataset = load_dataset("waiv/FinVoc2Vec_demo")

arrays = [demo['audio']['array'] for demo in demo_dataset['test']]

# extract features
features = feature_extractor(
    arrays,
    sampling_rate=feature_extractor.sampling_rate,
    padding=True,
    truncation=False)

inputs = torch.tensor(np.array(features['input_values']), dtype=torch.float32).to(device)
attention_mask = torch.tensor(np.array(features['attention_mask']), dtype=torch.long).to(device)

prob_dict = {}
with torch.no_grad():
    model_output = model(inputs, attention_mask=attention_mask)
    logits = model_output['logits'].to(torch.float32).to('cpu')
    probs = torch.nn.functional.softmax(logits, dim=1).numpy()
    
    label_to_id = model.config.label2id
    for i, id in enumerate(demo_dataset['test']['id']):
        prob_dict[id] = {'prob_negative': probs[i, label_to_id['negative']],
                         'prob_neutral': probs[i, label_to_id['neutral']],
                         'prob_positive': probs[i, label_to_id['positive']]}
```

## Example using audio files
```python
import torch
from torch.utils.data import DataLoader
from datasets import load_dataset
from dataclasses import dataclass
from typing import Dict, List, Optional, Union
from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2Processor, AutoModel
import torchaudio

device = "cuda" if torch.cuda.is_available() else "cpu"

@dataclass
class DataCollatorWithPadding:

    processor: Union[Wav2Vec2Processor, Wav2Vec2FeatureExtractor]
    padding: Union[bool, str] = True
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None

    def __call__(self,
                 features: List[Dict[str, Union[List[int], torch.Tensor]]]
                 )-> Dict[str, torch.Tensor]:
        
        input_features = [{"input_values": feature["input_values"]} for feature in features]

        # trunc and pad max lengths, get attention mask
        batch = self.processor.pad(
            input_features,
            padding=self.padding,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors="pt")
        return batch


def preprocess_audio(batch: Dict,
                     feature_extractor: Wav2Vec2FeatureExtractor = None,
                     max_duration: Optional[float] = 20.0):
    
    target_sr = feature_extractor.sampling_rate # 16kHz
    audio_arrays = []

    for path in batch['path']:
        audio_array, sampling_rate = torchaudio.load(path)
        
        # split to mono if multiple channels exist
        if audio_array.shape[0] > 1:
            audio_array = torch.mean(audio_array, dim=0, keepdim=True)
        
        # resample audio
        resampler = torchaudio.transforms.Resample(sampling_rate, target_sr)
        audio_array = resampler(audio_array).squeeze().numpy()
        audio_arrays.append(audio_array)
    
    # set params for feature extractor
    max_length = int(target_sr*max_duration) if max_duration is not None else None

    # use feature extractor to normalize inputs and trunc data
    result = feature_extractor(
        audio_arrays,
        sampling_rate=target_sr,
        max_length=max_length,
        truncation=bool(max_length))
    return result

# load model
model = AutoModel.from_pretrained("waiv/FinVoc2Vec", trust_remote_code=True).to(device)

# load feature extractor
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("waiv/FinVoc2Vec")

# load dataset
# NOTE: Needed feature: 'path' -> path to the audio-data
test_dataset = load_dataset(r'path/to/dataset')

# preprocess audio data
test_dataset = test_dataset.map(
    preprocess_audio,
    batch_size=1000,
    batched=True,
    num_proc=4,
    fn_kwargs={'feature_extractor': feature_extractor,
                'max_duration': 20.0})

data_collator = DataCollatorWithPadding(feature_extractor)

data_loader = DataLoader(
    test_dataset, 
    batch_size=16,
    shuffle=False,
    collate_fn=data_collator,
    num_workers=4)

with torch.no_grad():
    for batch in data_loader:
        
        attention_mask, inputs = batch['attention_mask'], batch['input_values']
        
        inputs.to(device)
        attention_mask.to(device)
        
        model_output = model(inputs, attention_mask=attention_mask)

        logits = model_output['logits'].to(torch.float32).to('cpu')
        probs = torch.nn.functional.softmax(logits, dim=1).numpy()
        
        label_to_id = model.config.label2id
        dict_probs = {f'prob_negative': probs[:, label_to_id['negative']],
                      f'prob_neutral': probs[:, label_to_id['neutral']],
                      f'prob_positive': probs[:, label_to_id['positive']]}
```

## Register for autoclass
To register the model for your local autoclass, use the following code:
```python
from transformers import AutoConfig, AutoModel

# download model and config
finvoc2vec_config = AutoConfig.from_pretrained("waiv/FinVoc2Vec", trust_remote_code=True)
finvoc2vec_model = AutoModel.from_pretrained("waiv/FinVoc2Vec", trust_remote_code=True)

# register model and config for automodel class
AutoConfig.register("finvoc2vec", FinVoc2VecConfig)
AutoModel.register(FinVoc2VecConfig, FinVoc2Vec)
```

## Further resources
Check the 🤗 Hugging Face [Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2) model description for additional resources and configurations.

## License
- This model is a derivative work based on Wav2Vec2 (Apache-2.0)
- This model is licensed under the Creative Commons Attribution Non Commercial 4.0 licence (CC-BY-NC-4.0)

## Paper
- [Listen Closely: Measuring Vocal Tone in Corporate Disclosures](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4307178)

## BibTeX
```

@article{ewertz2025,
  title={Listen Closely: Measuring Vocal Tone in Corporate Disclosures},
  author={Ewertz, Jonas and Knickrehm, Charlotte and Nienhaus, Martin and Reichmann, Doron},
  year={2025},
  journal={Journal of Accounting Research},
  url={https://doi.org/10.1111/1475-679X.70015}
}
