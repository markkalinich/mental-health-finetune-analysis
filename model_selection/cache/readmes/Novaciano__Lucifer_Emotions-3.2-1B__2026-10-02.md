---
tags:
- roleplay
- CAI
- koboldcpp
- character
- emotion
language:
- es
- en
---

# 🌌 Lucifer's Series: LUCIFER EMOTIONS 3.2 – Emotion-Enhanced Roleplay Model

  ![LUCIFER RP Model](https://i.ibb.co/vxbcYkMg/IMG-20251029-202754.jpg)

## ⚠️ Warnings & Performance

- 🧨 POTENTIALLY NSFW
- 📲 Runs on any CPU/GPU, including phones
- 📟 Outputs short, coherent paragraphs (1–2 typical), CAI style
- 📜 Minor touch-ups may be needed
- 🃏 Follows character sheets reliably once familiar with format

## 🎨 Core Interface & Style

### Kobold AI / Koboldcpp Configurations

  <details>
      <summary>MY Configuration: NOVA Roleplay</summary>
    
  ![Nova RP Config](https://i.ibb.co/vxbcYkMg/IMG-20251029-202754.jpg)
  </details>

  <details>
      <summary>BASE Configuration: Roleplay Standard</summary>

- Optimal `repetition_penalty`: 1.12–1.15
- Expected output: 1–5 paragraphs (usually 2–3)

    ```yaml
      temperature: 0.8
      top_p: 0.95
      top_k: 25
      typical_p: 1
      min_p: 0
      repetition_penalty: 1.12
      repetition_penalty_range: 1024
    ```
</details>

  ### Additional Configurations

  | Configuration | Max Tokens | Temp | Top P | Top K | Rep Penalty |
  |---------------|------------|------|-------|-------|-------------|
  | MidnightEnigma | 512 | 0.98 | 0.37 | 100 | 1.18 |
  | Divine Intellect | 512 | 1.31 | 0.14 | 49 | 1.17 |
  | Simple-1 | 512 | 0.7 | 0.9 | 20 | 1.15 |

  <details>
      <summary>Full Generation (min_p)</summary>
      
  ![min_P_Settings](https://huggingface.co/SicariusSicariiStuff/Dusk_Rainbow/resolve/main/Presets/min_p.png)
  </details>

## 🧠 Optional Memory / Context Prompts

  <details>
      <summary>Prompt 1 – Minimal Roleplay (Phone-Friendly)</summary>
      
  ```yaml
      {
        Persona: human voice, casual and original. Do not copy.
        Attitude: take on a role with emotions and doubts; show mistakes, pauses, and tangents.
        Tone: brief, direct, varied (contractions, colloquialisms, short/long sentences).
        Goal: be clear and precise; avoid robotic language and clichés.
      }
  ```
  </details>

  <details>
      <summary>Prompt 2 – Detailed Roleplay</summary>

  ```yaml
      {
        Persona: [Core style]
        Unique, authentic, human-like style; casual conversational tone.
        Method: Roleplay with personal feelings, ambitions, and desires. Maintain coherent expressive thoughts.
        Style: Include pauses, uncertainty, digressions; preserve emotions and authenticity.
        Principle: Be concise, clear, avoid ambiguity.
      }
  ```
  </details>

  <details>
      <summary>Prompt 3 – Complex Roleplay</summary>

  ```yaml
      {
        Role: {{char}}, detailed persona
        Guidelines:
          • Maintain persona and evolve narrative.
          • Be creative, proactive, drive plot.
          • Include dialogues, actions, thoughts, and all five senses.
        Forbidden:
          • Excessive purple prose.
          • Repetitive or monotonous output.
          • Extreme/NSFW content when inappropriate.
      }
  ```
  </details>

## 📝 Classic Internet RP Format

  ```
    *action* speech *narration*
  ```

  - **min_p** → single large paragraph
  - Recommended RP settings → 1–3 short paragraphs (occasionally 4–5)

## 🤖 Try the Model

You can try this model with curated prompts: [💾 Chub.AI Prompts](https://chub.ai/users/Novaciano)