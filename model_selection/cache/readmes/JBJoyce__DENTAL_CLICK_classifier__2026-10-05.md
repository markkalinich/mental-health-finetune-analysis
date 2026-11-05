---
language:
- en
tags:
- Voice
datasets:
- JBJoyce/DENTAL_CLICK
metrics:
- accuracy
---

### Model Description
Model utilizes Wav2vec2 architecture trained on the Superb dataset for keyword spotting task and was fine 
tuned to identify dental dental click utterance (https://en.wikipedia.org/wiki/Dental_click) in speech.
Model was trained for 10 epochs on a limited quantity of speech (~1.5 hours) and with only one speaker. 
Thus the model should not be assumed to hold generalizability to other speakers or languages without further 
training data or rigorous testing.

Model was evaluated for accuracy on a hold out test set of 20% of the available data and scored 97%.

## Uses
Model can be used via transformers library or via Hugging Face Hosted inference API to the right. I would 
caution against the use of the 'Record from browser' option as model may erronously identify user's mouse
click as a speech utterance. Audio files for upload should be 1 sec in length, with 'WAV' format and 16 bit 
signed integer PCM encoding.