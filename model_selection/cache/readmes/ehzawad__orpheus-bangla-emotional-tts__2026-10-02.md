---
language:
- bn
tags:
- text-to-speech
- bangla
- bengali
- orpheus
- audio
- emotional-tts
license: apache-2.0
datasets:
- bangla-audio-emotional
---

# Orpheus Bangla Emotional TTS Model

This is a Text-to-Speech model for Bangla (Bengali) language based on the Orpheus architecture. The model can generate natural-sounding Bangla speech from text input with various emotional styles.

## 🎮 Demo

Try out the model directly using our Hugging Face Space:
<a href="https://huggingface.co/spaces/ehzawad/orpheus-bangla-emotional-tts-demo" target="_blank">
  <img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg" alt="Open in HF Spaces"/>
</a>

## Model Details

- **Model Type:** Text-to-Speech
- **Language:** Bangla (Bengali)
- **Architecture:** Orpheus TTS + SNAC decoder
- **Sample Rate:** 24kHz
- **Special Features:** Emotional speech synthesis
- **Emotions:** Various emotional tones including happy, sad, angry, disgusted, frustrated, excited, curious, surprised, etc.

## Supported Emotions

This model supports the following emotional styles:
- happy
- normal
- disgust
- sad
- frustrated
- slow
- excited
- whisper
- panicky
- curious
- surprise
- fast
- crying
- deep
- sleepy
- angry
- high
- shout

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from snac import SNAC
import torch
import soundfile as sf

# Load the models
tokenizer = AutoTokenizer.from_pretrained("ehzawad/orpheus-bangla-emotional-tts")
model = AutoModelForCausalLM.from_pretrained(
    "ehzawad/orpheus-bangla-emotional-tts", 
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
snac_model = SNAC.from_pretrained("hubertsiuzdak/snac_24khz").to("cuda")

# Sample prompt in Bangla
prompt = "আপনি কেমন আছেন?"  # "How are you?" in Bangla

# For emotional speech, add the emotion tag (e.g., for happy)
emotional_prompt = "<happy>আপনি কেমন আছেন?</happy>"

# Add your inference code here
# (Follow the example_usage.py code for complete inference)
```

## Citation

If you use this model, please cite:

```
@misc{ehzawad2025orpheusbangla,
  author = {Ehzawad},
  title = {Orpheus Bangla Emotional TTS},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/ehzawad/orpheus-bangla-emotional-tts}}
}
```

## Acknowledgements

This model is based on the Orpheus TTS architecture developed by Canopy Labs. We extend our gratitude to the original authors for their work.
