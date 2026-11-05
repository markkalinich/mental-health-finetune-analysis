---
license: mit
datasets:
- gustavecortal/PsychologicalReasoning-15k
- Psychotherapy-LLM/PsychoCounsel-Preference
language:
- en
pipeline_tag: text-generation
base_model:
- gustavecortal/Piaget-4B
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

Beck is based on [Piaget](https://huggingface.co/gustavecortal/Piaget-4B) and was finetuned on psychotherapeutic preferences from [PsychoCounsel-Preference](https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference).

Available sizes are: [0.6B](https://huggingface.co/gustavecortal/Beck-0.6B), [1.7B](https://huggingface.co/gustavecortal/Beck-1.7B), [4B](https://huggingface.co/gustavecortal/Beck-4B), [8B](https://huggingface.co/gustavecortal/Beck-8B).

## How to use

 ```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo = "gustavecortal/Beck-4B"

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

**Qwen3-4B**:

```
It’s natural to feel anxious when facing important decisions, especially when the stakes feel high or when there’s a concern about others’ opinions. The key is to gradually build confidence in your ability to make choices that align with your values and goals. Start by recognizing that it’s okay to feel uncertain at times—everyone experiences doubt. Instead of trying to eliminate all hesitation, practice allowing yourself to feel the uncertainty while also acknowledging that you have enough information to make a meaningful choice.

Try breaking down the decision into smaller parts. Ask yourself what the possible outcomes are, what you value most, and whether the decision reflects your long-term goals. This can help clarify your priorities and reduce the pressure to be perfect. Also, remind yourself that it’s okay to make mistakes. Each decision, even if it doesn’t go as planned, is an opportunity to learn and grow.

Spend time reflecting on past decisions you’ve made confidently. What worked well? How did you feel afterward? Revisiting these moments can reinforce the idea that you’re capable of making good choices. Additionally, consider setting aside time for self-compassion. Be kind to yourself when you’re feeling stuck—this can help reduce the internal pressure that leads to indecision.

Over time, as you begin to trust your intuition more and act based on your own values rather than external expectations, you’ll likely find that the anxiety decreases. Confidence comes from experience, so keep making choices, even small ones, and allow yourself to evolve with each step. You’re not alone in this process, and it’s perfectly normal to take time to find your voice.
```

**Beck-4B**:

```
It sounds like you're experiencing a common challenge many people face when it comes to decision-making under the weight of anxiety. It's understandable that the fear of failing or disappointing those around you can influence your behavior.

One approach is to recognize the root of this issue. Fear tends to play a significant role in limiting our actions, so identifying its source might help us better understand our feelings and responses. Instead of getting caught up in self-judgment about potential outcomes, it could be helpful to think more broadly about who benefits from feeling this way—your sense of safety and well-being.

Another strategy is to start by practicing mindfulness and acceptance. When anxiety rises during decision-making, try acknowledging these emotions rather than suppressing them. This doesn't mean you have to force yourself into perfect circumstances; rather, it means being kinder to yourself during times when things aren't quite right.

Also, consider breaking large decisions into smaller, manageable steps. For instance, if you're deciding on something big (like purchasing property), break it down into tasks such as researching options, comparing costs, and evaluating personal needs before finalizing your choice. Doing this step-by-step can reduce overwhelm and encourage gradual trust in yourself.

Finally, seek support and share your concerns with someone you feel comfortable talking to—a trusted friend or family member who truly understands what you're going through. Sometimes sharing the burden of these worries helps alleviate some pressure and provides an opportunity for perspective-taking and reassurance.

Remember, developing confidence in decision-making takes time and practice. Start small, reflect on progress regularly, and be patient with oneself along this journey. Would any of these strategies resonate positively with you?
```

## Methodology

Beck was trained using preference optimization (ORPO) and LoRA. You can reproduce the results using [my repo](https://github.com/gustavecortal/preference-optimization-orpo-lora) for lightweight preference optimization using [this config](https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_4b.yaml) that contains the hyperparameters.

This work was performed using HPC resources (Jean Zay supercomputer) from GENCI-IDRIS (Grant 20XX-AD011014205).

## Inspiration

Beck aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence.

Beck was inspired by my position paper on emotion analysis: [Improving Language Models for Emotion Analysis: Insights from Cognitive Science](https://aclanthology.org/2024.cmcl-1.23/).

## Contact

Mail: gustave.cortal@ens-paris-saclay.fr

Website: [gustavecortal.com](gustavecortal.com)