---
license: cc-by-nc-sa-4.0
tags:
- spark-tts
- text-to-speech
- nonverbal
- emotional
- audio
- speech-synthesis
- huggingface
language:
- en
model-index:
- name: SparkNV-Voice
  results: []
datasets:
- deepvk/NonverbalTTS
base_model:
- SparkAudio/Spark-TTS-0.5B
---

# 🔊 SparkNV-Voice

  <img src="banner.png" width="800" />

**SparkNV-Voice** is a fine-tuned version of the [Spark-TTS](https://huggingface.co/suno-ai/spark-tts) model trained on the [NonverbalTTS](https://huggingface.co/datasets/deepvk/NonverbalTTS) dataset. It enables expressive speech synthesis with **nonverbal cues** (like laughter, sighs, sneezing, etc.) and rich emotional tone.

Built for applications that require **natural, human-like vocalization**, this model produces speech with **semantic tokens** and **global prosody control** using BiCodec detokenization.

---

## 🧾 Model Details

- **Base**: `suno-ai/spark-tts`
- **Dataset**: [`deepvk/NonverbalTTS`](https://huggingface.co/datasets/deepvk/NonverbalTTS)
- **Architecture**: Causal Language Model + BiCodec for audio token generation
- **Language**: English
- **Voice**: Single-speaker (no multi-speaker conditioning)

---

## 🛠 Installation

To run this model, install the required dependencies:

```bash
pip install --no-deps bitsandbytes accelerate xformers==0.0.29.post3 peft trl triton cut_cross_entropy unsloth_zoo
pip install sentencepiece protobuf "datasets>=3.4.1,<4.0.0" "huggingface_hub>=0.34.0" hf_transfer 
pip install --no-deps unsloth 
git clone https://github.com/SparkAudio/Spark-TTS
pip install omegaconf einx
````


---

## 🚀 Inference Code

```python
import torch
import re
import numpy as np
from typing import Dict, Any
import torchaudio.transforms as T
from unsloth import FastModel
import sys
sys.path.append('Spark-TTS')
from sparktts.models.audio_tokenizer import BiCodecTokenizer
from huggingface_hub import snapshot_download

# Download model and code
snapshot_download("yasserrmd/SparkNV-Voice", local_dir = "SparkNV-Voice")


max_seq_length = 2048 # Choose any for long context!
model, tokenizer = FastModel.from_pretrained(
    model_name = "SparkNV-Voice",
    max_seq_length = max_seq_length,
    dtype = torch.float32, # Spark seems to only work on float32 for now
    full_finetuning = True, # We support full finetuning now!
    load_in_4bit = False,
    #token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

FastModel.for_inference(model) # Enable native 2x faster inference

audio_tokenizer = BiCodecTokenizer("SparkNV-Voice", "cuda")
audio_tokenizer.model.to("cuda")

input_text = "Hey there, my name is Yasser, and I'm a 🌬️ speech generation model that can sound like a person."
chosen_voice = None # None for single-speaker

@torch.inference_mode()
def generate_speech_from_text(
    text: str,
    temperature: float = 0.8,   # Generation temperature
    top_k: int = 50,            # Generation top_k
    top_p: float = 1,        # Generation top_p
    max_new_audio_tokens: int = 2048, # Max tokens for audio part
    device: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
) -> np.ndarray:
    """
    Generates speech audio from text using default voice control parameters.

    Args:
        text (str): The text input to be converted to speech.
        temperature (float): Sampling temperature for generation.
        top_k (int): Top-k sampling parameter.
        top_p (float): Top-p (nucleus) sampling parameter.
        max_new_audio_tokens (int): Max number of new tokens to generate (limits audio length).
        device (torch.device): Device to run inference on.

    Returns:
        np.ndarray: Generated waveform as a NumPy array.
    """

    torch.compiler.reset()

    prompt = "".join([
        "<|task_tts|>",
        "<|start_content|>",
        text,
        "<|end_content|>",
        "<|start_global_token|>"
    ])

    model_inputs = tokenizer([prompt], return_tensors="pt").to(device)

    print("Generating token sequence...")
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=max_new_audio_tokens, # Limit generation length
        do_sample=True,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        eos_token_id=tokenizer.eos_token_id, # Stop token
        pad_token_id=tokenizer.pad_token_id # Use models pad token id
    )
    print("Token sequence generated.")


    generated_ids_trimmed = generated_ids[:, model_inputs.input_ids.shape[1]:]


    predicts_text = tokenizer.batch_decode(generated_ids_trimmed, skip_special_tokens=False)[0]
    # print(f"\nGenerated Text (for parsing):\n{predicts_text}\n") # Debugging

    # Extract semantic token IDs using regex
    semantic_matches = re.findall(r"<\|bicodec_semantic_(\d+)\|>", predicts_text)
    if not semantic_matches:
        print("Warning: No semantic tokens found in the generated output.")
        # Handle appropriately - perhaps return silence or raise error
        return np.array([], dtype=np.float32)

    pred_semantic_ids = torch.tensor([int(token) for token in semantic_matches]).long().unsqueeze(0) # Add batch dim

    # Extract global token IDs using regex (assuming controllable mode also generates these)
    global_matches = re.findall(r"<\|bicodec_global_(\d+)\|>", predicts_text)
    if not global_matches:
         print("Warning: No global tokens found in the generated output (controllable mode). Might use defaults or fail.")
         pred_global_ids = torch.zeros((1, 1), dtype=torch.long)
    else:
         pred_global_ids = torch.tensor([int(token) for token in global_matches]).long().unsqueeze(0) # Add batch dim

    pred_global_ids = pred_global_ids.unsqueeze(0) # Shape becomes (1, 1, N_global)

    print(f"Found {pred_semantic_ids.shape[1]} semantic tokens.")
    print(f"Found {pred_global_ids.shape[2]} global tokens.")


    # 5. Detokenize using BiCodecTokenizer
    print("Detokenizing audio tokens...")
    # Ensure audio_tokenizer and its internal model are on the correct device
    audio_tokenizer.device = device
    audio_tokenizer.model.to(device)
    # Squeeze the extra dimension from global tokens as seen in SparkTTS example
    wav_np = audio_tokenizer.detokenize(
        pred_global_ids.to(device).squeeze(0), # Shape (1, N_global)
        pred_semantic_ids.to(device)           # Shape (1, N_semantic)
    )
    print("Detokenization complete.")

    return wav_np

if __name__ == "__main__":
    print(f"Generating speech for: '{input_text}'")
    text = f"{chosen_voice}: " + input_text if chosen_voice else input_text
    generated_waveform = generate_speech_from_text(input_text)

    if generated_waveform.size > 0:
        import soundfile as sf
        output_filename = "generated_speech_controllable.wav"
        sample_rate = audio_tokenizer.config.get("sample_rate", 16000)
        sf.write(output_filename, generated_waveform, sample_rate)
        print(f"Audio saved to {output_filename}")

        # Optional: Play in notebook
        from IPython.display import Audio, display
        display(Audio(generated_waveform, rate=sample_rate))
    else:
        print("Audio generation failed (no tokens found?).")
````

---

## 🧠 Dataset Highlights: `NonverbalTTS`

* 17+ hours of annotated emotional & nonverbal English speech
* Automatic + human-validated labels
* Sources: VoxCeleb, Expresso
* Paper: [arXiv:2507.13155](https://arxiv.org/abs/2507.13155)

---

## 📜 License

This model is released under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

---

## 🤝 Credits

* Base model: [`suno-ai/spark-tts`](https://huggingface.co/suno-ai/spark-tts)
* Dataset: [`deepvk/NonverbalTTS`](https://huggingface.co/datasets/deepvk/NonverbalTTS)
* Author: [`@yasserrmd`](https://huggingface.co/yasserrmd)

---

## 💬 Feedback & Contributions

Open a discussion or issue on this repo. Contributions are welcome!