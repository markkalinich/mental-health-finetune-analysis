---
license: mit
datasets:
- recoilme/SyntheticPrompts
language:
- en
tags:
- gpt2
- prompts
---

v2 is out!
https://huggingface.co/recoilme/insomnia_v2  

Project by https://aiartlab.org/
</br>
A GPT2 model to generate prompts for SDXL or similar models.</br>
Trained from the GPT2 small model. Attach a Style to affect the render further.</br>
Trained on Syntetic prompts generated with Mistral7b. 
</br>Dataset: https://huggingface.co/datasets/recoilme/SyntheticPrompts

```
from transformers import pipeline, GPT2Tokenizer,GPT2LMHeadModel

checkpoint_path = "recoilme/insomnia_v2"
model = GPT2LMHeadModel.from_pretrained(checkpoint_path)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

text_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

texts = [
    "Frog in a Harry Potter costume",
    "Cat, art by ",
    "a photo of woman underwater",
    "thunderstorms on the alien planet, very shocking",
    "Standing on the land of a new planet, the Female astronaut dances",
    "The face of the cat woman, a face beautiful, young. The head is adorned with the Egyptian crown of Bastet.",
]

for text in texts:
    print(f"Input: {text}:")
    out = text_generator(text, max_length=150, num_return_sequences=2,temperature=1.0,)
    print(f"Output 1: {out[0]['generated_text']}\n\n")
    print(f"Output 2: {out[1]['generated_text']}")
    print("\n")
```

```
Input: Frog in a Harry Potter costume:

Output 1: Frog in a Harry Potter costume, detailed with a touch of magical realism, highlight bulging eyes, slick skin, webbed feet, add atmospheric detail  misty breath, dawns first light at lilycovered pond, end with a nod to Gabriel Garca Mrquezs wizarding world.
Output 2: Frog in a Harry Potter costume, detailed and exact, persona reminiscent of a dragon or wizard duel, setting for a graveyard, atmosphere charged with suspense and anticipation, mystical creatures looming, cinematic style emphasizing amphibious grace.```