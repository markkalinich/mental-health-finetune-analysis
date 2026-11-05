---
license: mit
datasets:
- gustavecortal/PsychologicalReasoning-15k
- Psychotherapy-LLM/PsychoCounsel-Preference
language:
- en
pipeline_tag: text-generation
base_model:
- gustavecortal/Piaget-0.6B
tags:
- philosophy
- psychology
- reasoning
- social
- emotion
- psychotherapy
---

## Presentation

A language model that handles delicate life situations and tries to really help you.

Beck is based on [Piaget](https://huggingface.co/gustavecortal/Piaget-0.6B) and was finetuned on psychotherapeutic preferences from [PsychoCounsel-Preference](https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference).

Available sizes are: [0.6B](https://huggingface.co/gustavecortal/Beck-0.6B), [1.7B](https://huggingface.co/gustavecortal/Beck-1.7B), [4B](https://huggingface.co/gustavecortal/Beck-4B), [8B](https://huggingface.co/gustavecortal/Beck-8B).

## How to use

 ```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo = "gustavecortal/Beck-0.6B"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    device_map="cuda",
    low_cpu_mem_usage=True,
)
model.eval()

prompt = r"""Anxiety often strikes when I'm faced with making decisions. 
    The fear of making the wrong choice or disappointing others paralyzes me, leaving me stuck in indecision.
    I want to learn how to trust myself and make confident choices. \no_think"""
messages_think = [
    {"role": "system", "content": "Do not use bullets points."},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages_think,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

with torch.no_grad():
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=2048,
        do_sample=True,
        temperature=1.0,
        top_p=0.95,
        top_k=50,
        repetition_penalty=1.1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
        use_cache=True,
    )

output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

## How does it compare to other language models?

For the given prompt: 

```
Anxiety often strikes when I'm faced with making decisions. 
The fear of making the wrong choice or disappointing others paralyzes me, leaving me stuck in indecision.
I want to learn how to trust myself and make confident choices. \no_think
```

**Qwen3-0.6B**:

```
It's important to recognize that anxiety about decision-making is common and often rooted in past experiences or fears. When you feel stuck, it might be helpful to take a moment to breathe deeply or reflect on what kind of person you are. Trusting yourself involves practicing self-compassion—being kind to yourself even when you don't have confidence. Making confident decisions requires taking small steps towards building that confidence each day.

If these thoughts resonate with you, consider talking to someone who understands your feelings, whether they are close friends, family, or a professional counselor. Small steps can gradually build confidence, so even if you're unsure yet, consistent effort is key. Let this remind you that progress is possible every day.
```

**Beck-0.6B**:

```
It takes courage to acknowledge when you're feeling overwhelmed by anxiety about making decisions. It sounds like you're going through a time when confidence is really being tested.

Firstly, it's great that you recognize these feelings and seek help. This is a step towards healing and growth. Can you tell me more about what specific situations cause you stress when considering decisions? Are there any particular thoughts or fears that come up for you as you approach each decision?

We can work together to identify patterns in your anxiety so we can understand why you're struggling to make confident choices. By addressing those underlying anxieties, we might be able to develop coping strategies that help you feel more grounded and empowered. Remember, mistakes are valuable learning experiences. When you choose wisely, they become opportunities to grow and learn from your decisions. Would that resonate with you?
```

## Methodology

Beck was trained using preference optimization (ORPO) and LoRA. You can reproduce the results using [my repo](https://github.com/gustavecortal/preference-optimization-orpo-lora) for lightweight preference optimization using [this config](https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_0.6b.yaml) that contains the hyperparameters.

This work was performed using HPC resources (Jean Zay supercomputer) from GENCI-IDRIS (Grant 20XX-AD011014205).

## Inspiration

Beck aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence.

Beck was inspired by my position paper on emotion analysis: [Improving Language Models for Emotion Analysis: Insights from Cognitive Science](https://aclanthology.org/2024.cmcl-1.23/).

## Contact

Mail: gustave.cortal@ens-paris-saclay.fr

Website: [gustavecortal.com](gustavecortal.com)