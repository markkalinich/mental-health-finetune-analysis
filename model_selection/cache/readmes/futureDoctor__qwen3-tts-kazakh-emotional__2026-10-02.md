cat > README.md << 'EOF'
---
language:
- kk
tags:
- text-to-speech
- tts
- kazakh
- qwen3-tts
- emotional-speech
license: cc-by-4.0
datasets:
- issai/KazEmoTTS
base_model: Qwen/Qwen3-TTS-12Hz-1.7B-Base
---

# Qwen3-TTS Kazakh Emotional Speech

Fine-tuned Qwen3-TTS model for Kazakh language text-to-speech with emotional expression.

## Training Data
- **Dataset**: KazEmoTTS (Kazakh Emotional TTS)
- **Speaker**: Female (kaz_aru) - 34 hours
- **Emotions**: neutral, happy, sad, angry, fear, surprise

## Usage
```python
import torch
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "futureDoctor/qwen3-tts-kazakh-emotional",
    device_map="cuda:0",
    dtype=torch.bfloat16,
)

wavs, sr = model.generate_custom_voice(
    text="Сәлеметсіз бе! Мен сізге көмектесемін.",
    speaker="kazakh_female_emotional",
)