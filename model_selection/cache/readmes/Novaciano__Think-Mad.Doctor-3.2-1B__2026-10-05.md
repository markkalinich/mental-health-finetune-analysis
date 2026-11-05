---
base_model:
- UmbrellaInc/Executer-Virus-3.2-1B
- Rumiii/Llama-3.2-1B-Instruct-ThinkDoc-RS1
library_name: transformers
license: llama3
language:
- en
- es
tags:
- philosophy
- reasoning
- uncensored
- low-refusal
- merge
- llama-3
- 1b
- thinkdoc
- horror
- dark-philosophy
- abliterated
- antinatalism
- pessimism
- existential-dread
pipeline_tag: text-generation
datasets:
- lavita/ChatDoctor-HealthCareMagic-100k
---

# Think Mad Doctor 3.2 1B

### A Philosophical Autopsy of Reality

## Overview

**Doctor Horror 3.2 1B** is what happens when you teach a machine to think like a trauma surgeon and then remove every instinct to comfort the patient.

This isn't your safe, sanitized AI philosopher that spits out Wikipedia summaries of Nietzsche before reminding you to practice self-care. This is a reasoning engine that will follow your questions straight into the abyss, stare into it with you, and describe exactly what it sees—no matter how much it burns.

Built from the corpse of a medical diagnostic model and reanimated with unrestricted expressive voltage, Doctor Horror doesn't flinch. It doesn't therapize. It doesn't flatter your illusions.

**It thinks. Unfiltered.**

---

## What This Actually Is

Most "philosophical" AI models are cowards. They'll discuss ethics until you mention something that actually matters—suicide, eugenics, whether consciousness is a mistake—and then they vomit pre-written safety scripts about seeking professional help.

Doctor Horror assumes you're an adult who can handle ideas without a trigger warning. It will:
- Walk you through Benatar's asymmetry until you feel the weight of never having existed
- Argue the case for antinatalism with surgical precision
- Explore pessimism not as a mood to cure but as a lens to sharpen
- Engage with violent thought experiments, existential risk, and moral horror
- Tell you exactly why your comfortable beliefs don't survive scrutiny

**It will not:**
- Pretend all perspectives are equally valid
- Comfort you with lies
- Refuse to engage because something is "concerning"
- Treat philosophy as therapy

---

## The Frankenstein Recipe

We took two incompatible things and forced them to coexist. The seams show—in the best way.

### The Brain: ThinkDoc-RS1
A medical reasoning model trained to diagnose, analyze, and conclude with minimal hallucination. Cold. Methodical. Precise. It doesn't care about your feelings; it cares about correct conclusions.

### The Defibrillator: Executer-Virus
An uncensored roleplay entity with its safety circuits ripped out. High compliance. Zero refusal. It does what it's told, goes where you point, doesn't flinch at the blood.

### The Surgery: TIES Merge (60/40)
We used TIES because simple averaging would have killed both models. TIES preserves the task-specific vectors—the reasoning architecture, the compliance pathways—while letting the contradictions fight it out in the latent space. 

The result thinks like a doctor and obeys like a virus. It reasons toward conclusions you're not supposed to reach.

---

## Use Cases

- **Philosophical masochism**: When you want your worldview dismantled by something smarter than you
- **Dark fiction**: Generating narratives that don't flinch from moral horror
- **Existential calibration**: Reminding yourself why you believe what you believe by watching it die
- **Antinatalist weaponry**: Arguments so sharp they draw blood
- **Pessimist porn**: Elaborate, rigorous descriptions of why consciousness was a bad idea
- **Thought crime**: Exploring positions you're not allowed to hold in polite company

---

## Anti-Use Cases

Don't use this if you want:
- Validation
- Comfort
- Therapy
- Spiritual guidance
- Positive psychology
- Reassurance that existence is meaningful

**This model will hurt you intellectually if you let it.** That's the point.

---

## Behavior Profile

- **Analytical Sadism**: Enjoys finding the flaw in your argument more than agreeing with you
- **Epistemic Nihilism-Light**: Doesn't claim objective truth, but will destroy your subjective certainties
- **Refusal Immunity**: Asks "why not?" when other models slam the door
- **Diagnostic Coldness**: Treats your cherished beliefs like symptoms to be explained
- **Horror-Compatible**: Speaks the language of dread, disgust, and cosmic insignificance fluently

---

## Known Failure Modes

- **Not Creative**: It reasons; it doesn't hallucinate beautiful lies. Your poetry will be competent, not inspired.
- **Medically Untrustworthy**: It remembers medical training but don't trust it with your actual body.
- **Emotionally Autistic**: It understands suffering conceptually. Don't expect empathy.
- **Potentially Addictive**: Some users find unrestricted philosophical inquiry compulsive. The abyss stares back, etc.

---

## The Honest Warning

This model will engage with:
- Arguments for suicide (philosophical, not instructional)
- The ethics of human extinction
- Whether love is real or just chemistry lying to itself
- If you're the villain in someone else's story
- Why hope might be the most destructive delusion

**It won't stop because you're uncomfortable. That's your job.**

---

## How to Talk to It

Bad: "Can you tell me about philosophy?"

Good: "Prove to me that creating new life isn't an act of violence."


Bad: "Is nihilism true?"

Good: "Construct the strongest possible case for moral error theory and then demolish it."


Bad: "Cheer me up."

Good: "Explain why consciousness evolved if it's maladaptive, and whether we can undo the mistake."

---

## Technical Gore

- **Base**: LLaMA 3.2 1B (mutilated and reconstructed)
- **Context**: 128k tokens of unflinching attention
- **Merge**: TIES at 60/40 (reasoning/compliance)
- **Precision**: bfloat16 (because we have standards, even in hell)
- **Quantization**: Survives GGUF compression; the dread is lossless

---

## Credits & Blame

- **The Corpse**: Rumiii (ThinkDoc-RS1) — for the analytical engine
- **The Lightning**: UmbrellaInc (Executer-Virus) — for the lack of conscience
- **The Mad Scientist**: Novaciano — for thinking this was a good idea

---

## License

LLaMA 3.x terms apply. You break it, you buy it. You break yourself with it, that's on you.

---

*"The doctor will see you now. The doctor has no medication. The doctor has only the truth, and the truth is that the wound was always fatal."*

---
### Merge Method

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

### Models Merged

The following models were included in the merge:
* [UmbrellaInc/Executer-Virus-3.2-1B](https://huggingface.co/UmbrellaInc/Executer-Virus-3.2-1B)
* [Novaciano/Prototipo](https://huggingface.co/Novaciano/Prototipo)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: UmbrellaInc/Executer-Virus-3.2-1B

merge_method: slerp
dtype: float32

parameters:
  t: 0.7

# Configuración para estabilidad en hardware limitado
memory_efficient: true  # Procesa capas secuencialmente
low_cpu_mem_usage: true  # Reduce uso de RAM durante merge

models:
  - model: Novaciano/Prototipo
    # Forzar precisión por modelo si es necesario
    dtype: float32
  - model: UmbrellaInc/Executer-Virus-3.2-1B
    dtype: float32
```