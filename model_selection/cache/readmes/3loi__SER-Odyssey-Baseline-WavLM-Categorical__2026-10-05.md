---
license: mit
language:
- en
pipeline_tag: audio-classification
tags:
- wavlm
- msp-podcast
- emotion-recognition
- audio
- speech
- categorical
- lucas
- speech-emotion-recognition
---
The model was trained on [MSP-Podcast](https://ecs.utdallas.edu/research/researchlabs/msp-lab/MSP-Podcast.html) for the Odyssey 2024 Emotion Recognition competition baseline<br>
This particular model is the categorical based model which predicts: "Angry", "Sad", "Happy", "Surprise", "Fear", "Disgust", "Contempt" and "Neutral".


# Benchmarks
F1-scores based on Test3 and Development sets of the Odyssey Competition
<table style="width:500px">
  <tr><th colspan=8 align="center" >Categorical Setup</th></tr>
  <tr><th colspan=4 align="center">Test 3</th><th colspan=4 align="center">Development</th></tr>
  <tr>   <td>F1-Mic.</td> <td>F1-Ma.</td> <td>Prec.</td> <td>Rec.</td>   <td>F1-Mic.</td> <td>F1-Ma.</td> <td>Prec.</td> <td>Rec.</td> </tr>
  <tr>  <td> 0.327</td> <td>0.311</td> <td>0.332</td> <td>0.325</td>     <td>0.409</td> <td>0.307</td>  <td>0.316</td> <td>0.345</td> </tr>
</table>
 

       
For more details:  [demo](https://huggingface.co/spaces/3loi/WavLM-SER-Multi-Baseline-Odyssey2024), [paper](https://ecs.utdallas.edu/research/researchlabs/msp-lab/publications/Goncalves_2024.pdf), and [GitHub](https://github.com/MSP-UTD/MSP-Podcast_Challenge/tree/main).


```
@InProceedings{Goncalves_2024,
            author={L. Goncalves and A. N. Salman and A. {Reddy Naini} and L. Moro-Velazquez and T. Thebaud and L. {Paola Garcia} and N. Dehak and B. Sisman and C. Busso},
            title={Odyssey2024 - Speech Emotion Recognition Challenge: Dataset, Baseline Framework, and Results},
            booktitle={Odyssey 2024: The Speaker and Language Recognition Workshop)},
            volume={To appear},
            year={2024},
            month={June},
            address =  {Quebec, Canada},
}
```


# Usage
```python
from transformers import AutoModelForAudioClassification
import librosa, torch

#load model
model = AutoModelForAudioClassification.from_pretrained("3loi/SER-Odyssey-Baseline-WavLM-Categorical-Attributes", trust_remote_code=True)

#get mean/std
mean = model.config.mean
std = model.config.std


#load an audio file
audio_path = "/path/to/audio.wav"
raw_wav, _ = librosa.load(audio_path, sr=model.config.sampling_rate)

#normalize the audio by mean/std
norm_wav = (raw_wav - mean) / (std+0.000001)

#generate the mask
mask = torch.ones(1, len(norm_wav))

#batch it (add dim)
wavs = torch.tensor(norm_wav).unsqueeze(0)


#predict
with torch.no_grad():
    pred = model(wavs, mask)

print(model.config.id2label)  
print(pred)
#{0: 'Angry', 1: 'Sad', 2: 'Happy', 3: 'Surprise', 4: 'Fear', 5: 'Disgust', 6: 'Contempt', 7: 'Neutral'}
#tensor([[0.0015, 0.3651, 0.0593, 0.0315, 0.0600, 0.0125, 0.0319, 0.4382]])

#convert logits to probability
probabilities = torch.nn.functional.softmax(pred, dim=1)
print(probabilities)
#[[0.0015, 0.3651, 0.0593, 0.0315, 0.0600, 0.0125, 0.0319, 0.4382]]
```