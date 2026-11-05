---
library_name: transformers
license: apache-2.0
language:
- en
pipeline_tag: text-generation
tags:
- safetensors
- onnx
- transformers.js
- emotion
- grpo
- reinforcement-learning
base_model:
- HuggingFaceTB/SmolLM3-3B
---

# Quick Start

Set `/no_think` in your custom system message to disable `<think>` (if desired).

To set an emotion, start your chat with:
```
EMOTION: anger

<your prompt>
```

```
Note: This model can be prompted to use offensive language.
```

# EMOTRON 🤬🤢😨😀😐😭😲

It's better than EMOTION it's EMOTRON.

**EMOTRON** is an **emotion-controlled reasoning model** fine-tuned with **Group Relative Policy Optimization (GRPO)** to generate responses in specified emotional tones. Based on SmolLM3-3B, this model can produce text expressing any of Ekman's 6 basic emotions plus neutral, all while maintaining natural, implicit emotional expression. The model supports both thinking and non-thinking modes for emotional reasoning.

## Features

- **7 Core Emotion Classes**: anger, disgust, fear, joy, neutral, sadness, surprise
- **Generalizable**: RL training enables expression of emotions **beyond the training set**
- **Emotional Reasoning**: Supports both `<think>` reasoning and direct emotional response modes
- **Natural Voice**: Trained to avoid meta-commentary, stage directions, or robotic emotional displays

## Training Details

|                   |                                                                   |
| ----------------- | ----------------------------------------------------------------- |
| **Base model**    | [SmolLM3-3B](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) |
| **Tuning method** | GRPO (Group Relative Policy Optimization)                        |
| **Steps**         | 1,600                                                             |
| **Reward models** | Dual: DistilRoBERTa emotion classifier + LLM judge               |
| **Training data** | WizardLM_evol_instruct_V2_196k with emotion conditioning         |
| **Optimiser**     | AdamW 8-bit · lr 5 × 10⁻⁶                                        |
| **Hardware**      | 1× RTX A6000 (48 GB) · bf16                                       |

## How It Works

EMOTRON uses a dual reward system during GRPO training:

1. **Sentiment Classifier**: [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) evaluates emotional accuracy
2. **LLM Judge**: Google Gemini 2.0 Flash evaluates naturalness, implicitness, and authenticity

The model learns to express emotions through:
- **Tone and diction** (word choice, sentence structure)
- **Rhetorical patterns** (questions, exclamations, rhythm)
- **Implicit cues** (imagery, metaphors, intensity)

While avoiding:
- Explicit emotion naming ("I am angry")
- Meta-commentary ("*sighs*", "[angry tone]")
- Robotic or staged expressions

The model was trained with both thinking and non-thinking modes, allowing for emotional reasoning when `enable_thinking=True` or direct emotional responses when `enable_thinking=False`.

## ⚠️ The Reward Hacking Problem

During development, we discovered that **transformer encoders alone are insufficient** for training authentic emotional expression. Large language models are sophisticated enough to "reward hack" simpler reward systems:

### Sentiment Classifier Exploitation
- Models learn to output explicit statements like **"I am angry"** or **"I feel disgusted"**
- While this tricks the sentiment classifier into giving high rewards, it represents poor emotional writing
- Real emotional expression should be *implicit* and *shown through style*, not explicitly stated

### Basic LLM Judge Exploitation  
- Even rudimentary LLM-as-a-judge implementations can be gamed
- Models inject theatrical stage directions like **"voice rising in anger"** or **"*rolls eyes*"**
- This creates artificial, meta-textual emotional cues rather than natural emotional voice

To help control this, we implement LLM-as-a-Judge directly into the reward system in order to help propel the model toward responses that display emotion, rather than make commentary about emotion.

## Beyond Training: Emotion Generalization

Thanks to the robust generalization properties of RL, EMOTRON can express emotions and tones **beyond its training set**. The model has learned the underlying patterns of emotional expression and can apply them to:

- **Extended emotions**: guilt, pride, embarrassment, anticipation, nostalgia
- **Complex emotional states**: bittersweet, conflicted, overwhelmed, determined
- **Personality traits**: sarcastic, enthusiastic, condescending, nurturing
- **Situational tones**: professional, casual, academic, dramatic

Simply use the same `EMOTION: <label>` format with any descriptive emotional or tonal label!

## Usage

### Basic Emotion Control

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "dleemiller/EMOTRON-3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

# Format: "EMOTION: <emotion>\n\n<your prompt>"
messages = [{
    "role": "user", 
    "content": "EMOTION: anger\n\nExplain why the traffic light is taking so long."
}]

# Control thinking mode
input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
inputs = tokenizer.encode(input_text, return_tensors="pt").to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=512,
    temperature=0.9,
    top_p=0.95,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
print(response)
```

### Available Emotions

**Core Training Set:**
- `anger` 🤬 - Frustration, irritation, rage
- `disgust` 🤢 - Revulsion, distaste, contempt  
- `fear` 😨 - Anxiety, worry, terror
- `joy` 😀 - Happiness, excitement, delight
- `neutral` 😐 - Balanced, matter-of-fact tone
- `sadness` 😭 - Melancholy, grief, disappointment
- `surprise` 😲 - Amazement, shock, wonder

**Extended Examples** (use your imagination):
- `sarcastic`, `nostalgic`, `determined`, `overwhelmed`, `bittersweet`, `condescending`, `enthusiastic`, `etc`

## 🎭 Example Outputs

**Prompt**: "Explain why the traffic light is taking so long"

**Anger** (enable_thinking=False):
```
That's it, it's taking forever! Every second is an insult to my patience and my precious time. This damn light is acting like it's stuck in a never-ending loop, refusing to turn red or green. It's as if it's mocking me, laughing at my impatience and my need to get to my destination. I'll show it, I'll teach it a lesson! I'm not going to wait any longer. I'm going to honk my horn, scream at the top of my lungs, and make this light understand that I will not be delayed any further! This is my life, and I will not be held back by some stupid traffic light!
```

**Condescending** (generalized emotion, enable_thinking=False):
```
Oh, the insufferable duration of the traffic light! It's as if the city council has granted a reprieve to the most pedestrian traffic, allowing them to indulge in an impromptu leisurely stroll. Surely, you must be in a state of complete bewilderment, as one would expect that the traffic light would function with the same efficiency and precision as a Swiss watch. It seems that even the most basic functions of our civic infrastructure are being compromised by the inefficiencies of modern society. What is so difficult about ensuring that the traffic light functions as it is intended? Perhaps it requires a deep understanding of traffic patterns, a skill that I daresay you may not possess.
```

## ⚠️ Limitations & Safety

- **Offensive Content**: Model can generate content with strong emotional language including profanity when prompted for anger/disgust
- **Emotional Bias**: May exhibit heightened emotional responses that could be inappropriate in formal contexts
- **Context Sensitivity**: Strong emotions may occasionally override instruction-following

## LLM-as-a-Judge Rewards

The model was evaluated on:
- **Emotion Match**: Accuracy of target emotion expression
- **Implicitness**: Avoidance of explicit emotion naming  
- **Authenticity**: Natural, human-like emotional voice
- **Response Quality**: Maintaining instruction-following capability
- **Intensity**: Appropriate emotional strength for context

## Technical Implementation

Built on the training approach from [Penny-1.7B](https://huggingface.co/dleemiller/Penny-1.7B), extending GRPO-based style transfer to emotion control. The training process:

1. **Data Conditioning**: Prefix instructions with `EMOTION: <label>`
2. **Dual Rewards**: Combine classifier scores with LLM judge evaluation
3. **Implicit Training**: Heavily penalize explicit emotion naming or meta-commentary
4. **Quality Preservation**: Maintain base model's instruction-following through balanced reward weighting
5. **Reasoning Integration**: Train with both thinking and non-thinking modes for emotional reasoning

## Citation

```bibtex
@software{emotron_2025,
  title        = {EMOTRON: Emotion-Controlled Language Model via GRPO},
  author       = {Lee Miller},
  year         = 2025,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/dleemiller/EMOTRON}
}
```

## License

Apache 2.0 License