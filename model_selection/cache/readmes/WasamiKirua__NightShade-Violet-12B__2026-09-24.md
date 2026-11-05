---
license: apache-2.0
base_model: Vortex5/NoctyxCosma-12B
model_name: Nightshade-Violet-12B
library_name: transformers
tags:
- merge
- mergekit
- dare_ties
- mistral-nemo
- roleplay
- emotional-intelligence
- psychological
- minimalist
language:
- it
- en
---

<img src="https://i.postimg.cc/FHLNMZMG/Gemini-Generated-Image-vrbmmvvrbmmvvrbm.png" alt="cover" border="0" width="1024px">

# 💜 Nightshade-Violet-12B (The Emotional Sniper)

**Nightshade-Violet-12B** is a specialized 12B parameter model engineered for **Psychological Precision** and **Emotional Impact**. While its sibling (Nightshade-Lotus) is a storyteller, Violet is an executioner of subtext. 

By leveraging the high EQ (Emotional Quotient) of the Violet-Lotus architecture, this model is designed to "read between the lines" and strike the user with surgical, minimalist, and deeply resonant responses.

## 🧠 The "Surgical" Merge Recipe

This model uses **DARE-TIES** to prioritize emotional intelligence and brevity, pruning unnecessary prose to ensure every word carries maximum weight.

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: FallenMerick/MN-Violet-Lotus-12B
    parameters:
      weight: 0.45 
      # L'Ancora EQ: Domina la comprensione del sottotesto e dell'emozione.
  - model: Vortex5/Cosmic-Night-12B
    parameters:
      weight: 0.25 
      # Il Silenziatore: Impone la brevità e la struttura secca.
  - model: Vortex5/Crimson-Constellation-12B
    parameters:
      weight: 0.15 
      # Lo Stiletto: Fornisce l'intensità e la capacità di ferire/colpire.
  - model: Vortex5/Moonlit-Mirage-12B
    parameters:
      weight: 0.15 
      # Il Filtro: Aggiunge quel tono cinico e atmosferico "Nightshade".

merge_method: dare_ties
base_model: Vortex5/NoctyxCosma-12B
parameters:
  density: 0.55 
  # Densità media: Abbastanza alta per non perdere l'EQ di Violet, 
  # ma abbastanza bassa da "pulire" la verbosità di base.
  weight: 1.0
dtype: bfloat16
tokenizer_source: base
```

# 💪 Key Strengths: The Emotional Edge

Psychological Dominance: The model excels at identifying the user's emotional state and responding in a way that feels unnervingly "aware."

Minimalist Impact: It favors quality over quantity. It won't write paragraphs; it will write three lines that leave you thinking for an hour.

Subtext Recognition: Highly capable of navigating complex relationship dynamics, gaslighting, and indirect communication.

Cold Empathy: It understands emotions perfectly, but uses that understanding to maintain its "Nightshade" persona—calculated, distant, and intense.

# 🚀 Best Use Cases

Intense 1-on-1 RP: Especially for antagonistic, mysterious, or psychologically complex characters.

Conflict Resolution (or Escalation): Where the drama is internal and verbal rather than physical.

Minimalist Storytelling: For users who prefer a "ping-pong" chat style where the AI reacts sharply to every move.

# ⚠️ Limitations

Non-Descriptive: If you ask for a description of a room, it might give you a metaphor for your character's loneliness instead. It is not for world-building.

Potentially Abrasive: Its high EQ combined with the "Crimson" weight makes it very good at being mean in a way that feels personal.

High Inference Sensitivity: Small changes in your prompt can drastically change the "vibe" of its strike.

# 📈 Recommended Inference Settings

To keep the "Sniper" focused and prevent rambling:

Temperature: 0.7 - 0.75 (Lower for more surgical precision).

Min-P: 0.1 (Crucial to filter out low-probability "noise").

Presence Penalty: 0.15 (Keeps the vocabulary fresh without being loquacious).

Frequency Penalty: 0.1

# Disclaimer

Nightshade-Violet-12B is a specialized roleplay tool. It is designed to be emotionally provocative and unfiltered. It should be treated as an experimental entity for mature psychological exploration.

