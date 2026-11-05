---
license: mit
datasets:
- gustavecortal/PsychologicalReasoning-15k
- Psychotherapy-LLM/PsychoCounsel-Preference
language:
- en
pipeline_tag: text-generation
base_model:
- gustavecortal/Piaget-1.7B
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

Beck is based on [Piaget](https://huggingface.co/gustavecortal/Piaget-1.7B) and was finetuned on psychotherapeutic preferences from [PsychoCounsel-Preference](https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference).

Available sizes are: [0.6B](https://huggingface.co/gustavecortal/Beck-0.6B), [1.7B](https://huggingface.co/gustavecortal/Beck-1.7B), [4B](https://huggingface.co/gustavecortal/Beck-4B), [8B](https://huggingface.co/gustavecortal/Beck-8B).

## How to use

 ```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo = "gustavecortal/Beck-1.7B"

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

**Qwen3-1.7B**:

```
You're not alone in feeling this way. Anxiety around decision-making is a common experience, especially when it feels like the weight of expectations rests on your shoulders. It's important to recognize that these feelings are normal, and they don't define you.

Trust in yourself begins with small steps. Start by acknowledging that it's okay to feel uncertain. Each decision, no matter how small, is an opportunity to grow. Try to approach each situation with curiosity rather than fear—ask questions, consider different possibilities, and take action even if it feels tentative.

Also, remember that growth happens gradually. Over time, as you practice making choices and learning from them, your confidence will build. You deserve to feel safe in making decisions that align with your values and authentic self.

If this anxiety becomes overwhelming, consider talking to someone you trust or seeking professional support. You’re not weak for wanting to feel more confident—you’re taking a courageous step toward self-compassion and empowerment.
```

**Beck-1.7B**:

```
It sounds like you're experiencing a common challenge many people face when it comes to decision-making under the weight of anxiety. It's understandable that the fear of failing or disappointing those around you can influence your behavior.

One approach is to recognize the root of this issue. Fear tends to play a significant role in limiting our actions, so identifying its source might help us better understand our feelings and responses. Instead of getting caught up in self-judgment about potential outcomes, it could be helpful to think more broadly about who benefits from feeling this way—your sense of safety and well-being.

Another strategy is to start by practicing mindfulness and acceptance. When anxiety rises during decision-making, try acknowledging these emotions rather than suppressing them. This doesn't mean you have to force yourself into perfect circumstances; rather, it means being kinder to yourself during times when things aren't quite right.

Also, consider breaking large decisions into smaller, manageable steps. For instance, if you're deciding on something big (like purchasing property), break it down into tasks such as researching options, comparing costs, and evaluating personal needs before finalizing your choice. Doing this step-by-step can reduce overwhelm and encourage gradual trust in yourself.

Finally, seek support and share your concerns with someone you feel comfortable talking to—a trusted friend or family member who truly understands what you're going through. Sometimes sharing the burden of these worries helps alleviate some pressure and provides an opportunity for perspective-taking and reassurance.

Remember, developing confidence in decision-making takes time and practice. Start small, reflect on progress regularly, and be patient with oneself along this journey. Would any of these strategies resonate positively with you?
```

## Methodology

Beck was trained using preference optimization (ORPO) and LoRA. You can reproduce the results using [my repo](https://github.com/gustavecortal/preference-optimization-orpo-lora) for lightweight preference optimization using [this config](https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_1.7b.yaml) that contains the hyperparameters.

This work was performed using HPC resources (Jean Zay supercomputer) from GENCI-IDRIS (Grant 20XX-AD011014205).

## Inspiration

Beck aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence.

Beck was inspired by my position paper on emotion analysis: [Improving Language Models for Emotion Analysis: Insights from Cognitive Science](https://aclanthology.org/2024.cmcl-1.23/).

## Contact

Mail: gustave.cortal@ens-paris-saclay.fr

Website: [gustavecortal.com](gustavecortal.com)