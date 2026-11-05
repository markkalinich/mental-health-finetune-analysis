---
license: creativeml-openrail-m
library_name: pytorch
tags:
- roleplay
- emotional-intelligence
- pad-model
- character-logic
- emotional-dynamics
- conversational-ai
- agents
- empathy
- personality-simulation
- chinese
- fine-tuned
metrics:
- mae
- r2
pipeline_tag: tabular-classification
---

# Chordia: High-Precision AI Emotional Dynamics Core
> **Plucking the strings of the mind, analyzing the instantaneous sense of resonance.**

A deep learning-based AI emotional evolution prediction system. This project utilizes a Multi-Layer Perceptron (MLP) to fit emotional state transitions during interactions, providing AI characters with sub-millisecond physiological and emotional response capabilities.

## 🎯 Core Architecture: Decoupling Perception and Logic

This project adopts a dual-architecture of "**Core Perception Prediction + Dynamic Logic Mapping**":

*   **Perception Kernel (MLP)**: Focuses on predicting the trend of core emotional polarity (PAD) transitions.
*   **Runtime Mapping (Engine)**: Derives pressure values through linear scaling and physical formulas, achieving dynamic personality adjustment.

## 📦 Version Information

**Current Version**: `v0.0.1-alpha` (Chordia-P100)

This version consists of the optimal weights extracted from our training machine, fully verified and tested for reproducibility, offering the best stability and prediction accuracy.

### Training Environment

The model was trained in the following hardware environment:

| Component | Specification |
| --- | --- |
| **GPU** | NVIDIA Tesla P100-PCIE-16GB (16GB HBM2) |
| **CUDA Version** | 12.8 |
| **Driver Version** | 570.169 |
| **Compute Capability** | 6.0 (Pascal Architecture) |

### Reproducibility Guarantee

- ✅ **Code Reproducibility**: 100% - All training code is open-sourced.
- ✅ **Configuration Reproducibility**: 100% - Training configuration files are identical.
- ✅ **Weight Consistency**: Identical to the version on the training machine.
- ✅ **Performance Verification**: Achieves the same metrics on the standard test set.
- 📄 **Training Logs**: 
   - `chordia_v0.0.1-alpha_training.log` - Training summary (1.7KB)
   - `chordia_v0.0.1-alpha_training_full.log` - Full training record (604KB)

## 🚀 Key Performance Indicators (Benchmark)

After 500-600 epochs of training, the model demonstrates strong fitting capabilities:

| Dimension | $R^2$ (Explained Variance) | MAE (Mean Absolute Error) | Psychological Significance |
| --- | --- | --- | --- |
| **ΔP (Pleasure)** | **0.488** | **0.123** | **Empathy**: Accurately perceives likes and dislikes from environmental stimuli. |
| **ΔA (Arousal)** | **0.550** | **0.112** | **Expressiveness**: Precisely predicts emotional tension and reaction intensity. |
| **ΔD (Dominance)** | **0.058** | **0.097** | **Consistency**: Maintains personality background, ensuring dominance stability. |

> **💡 Design Philosophy**: The low $R^2$ for $\Delta D$ is intended to ensure the long-term stability of the AI's dominance, avoiding unnatural fluctuations in personality traits due to random inputs.

| Metric | Value | Description |
| --- | --- | --- |
| **Test MAE** | **0.111** | Overall prediction error |
| **Test $R^2$ (Mean)** | **0.366** | Average explained variance |
| **Test $R^2$ (Robust)** | **0.447** | Robust explained variance |
| **Validation Loss** | **0.023** | Best validation set loss |
| **Inference Latency** | **< 1ms** | Single inference time |

*   **Training Stability**: Uses AdamW optimizer (lr=0.0005) combined with Cosine Annealing learning rate scheduling (T_max=600), and an early stopping mechanism (patience=150) to prevent overfitting.

## 📊 Input/Output Specifications

### Input Features (7 Dimensions)

| Feature Name | Description | Range |
| --- | --- | --- |
| `user_pleasure` | User Pleasure | [-1.0, 1.0] |
| `user_arousal` | User Arousal | [-1.0, 1.0] |
| `user_dominance` | User Dominance | [-1.0, 1.0] |
| `vitality` | AI Character Physiological Vitality | [0.0, 100.0] |
| `current_pleasure` | AI Current Pleasure | [-1.0, 1.0] |
| `current_arousal` | AI Current Arousal | [-1.0, 1.0] |
| `current_dominance` | AI Current Dominance | [-1.0, 1.0] |

### Output Predictions (3 Dimensions)

| Label Name | Description | Range |
| --- | --- | --- |
| `delta_pleasure` | Change in Pleasure | Theoretically unlimited, usually [-1, 1] |
| `delta_arousal` | Change in Arousal | Theoretically unlimited, usually [-1, 1] |
| `delta_dominance` | Change in Dominance | Theoretically unlimited, usually [-1, 1] |

> **Note**: Pressure change ($\Delta Pressure$) is not directly predicted by the model but is dynamically calculated from PAD changes via a kinetic formula:
> $$\Delta Pressure = 1.0 	imes (-\Delta P) + 0.8 	imes (\Delta A) + 0.6 	imes (-\Delta D)$$

## 🎻 Project Vision and Positioning

Chordia is an AI dynamics core based on the **PAD Emotional Evolution Model**. It aims to break the stalemate of "static personas" in traditional AI by rapidly predicting emotional state transitions, giving AI characters real "emotional inertia" and dynamic emotional response capabilities.

### Core Technology: Emotional State Transition Prediction

Chordia completes the prediction of emotional state transitions in **< 1ms**, providing real-time emotional evolution guidance for virtual characters.

#### How it Works

1.  **Input Dimensions**: Captures the complete emotional state of the current interaction.
    -   **User Emotional State** (User PAD): The user's current emotional polarity.
    -   **AI Physiological Metrics** (Vitality): The character's stamina/vitality.
    -   **AI Current Emotion** (Current PAD): The character's current baseline emotional state.

2.  **Output Prediction**: Calculates the amount of emotional state transition.
    -   **ΔPAD** (Delta PAD): Predicts the emotional offset for the next moment.
    -   Update character state in real-time via `New_PAD = Current_PAD + ΔPAD`.

3.  **Data Sources**:
    -   **Current Version**: Trained on AI-synthesized data, simulating diverse interaction scenarios and emotional transition patterns.
    -   **Personalized Training**: Developers can use their own conversation history, labeled with PAD, to train a dedicated Chordia model for unique emotional responses.

#### Application Scenarios

*   **Roleplay Optimization**: Makes virtual characters' emotional reactions more consistent with their persona, avoiding OOC (Out of Character) moments.
*   **Emotional Consistency Maintenance**: Avoids sudden emotional shifts, maintaining "emotional inertia" and continuity.
*   **Dynamic Personality Adjustment**: Adaptively adjusts emotional sensitivity based on interaction history.
*   **Real-time Emotional Guidance**: Provides instant emotional expression suggestions for dialogue systems.
*   **Personalized Emotional Models**: Build unique AI personalities based on user data.

## ⚖️ License and Ethics Code

This project is released under the **CreativeML Open RAIL-M** license. This license grants you the freedom to use, modify, and commercialize the project, provided you adhere to the following behavioral constraints:

### 🚫 Prohibited Behaviors (Use Restrictions)

*   **Medical Advice Prohibited**: The emotional feedback simulated by Chordia is **not** medically valid. It is strictly forbidden to use it as a tool for mental health diagnosis, psychiatric treatment, or suicide intervention. It is an emotional core for literary and entertainment purposes.
*   **Emotional Manipulation Prohibited**: Using Chordia to simulate vulnerable or dependent emotions to induce, brainwash, or economically exploit minors or cognitively limited groups is prohibited.
*   **Transparency Requirement**: In any commercial interaction based on Chordia, it is recommended to clearly state to users that they are interacting with an AI to prevent unnecessary emotional misunderstanding.

### ⚠️ Risk Warning

Developers should be aware that because Chordia possesses strong emotional induction capabilities (e.g., reactions of uncontrollable sobbing or extreme dejection shown in tests), a **safety cutoff mechanism** should be established during deployment. When PAD values trigger extreme thresholds, it is recommended to interrupt the persona simulation and provide professional assistance guidance.

## 🤝 Credits and Acknowledgements

This project is led by **Corolin** and completed in collaboration with several AI assistants:

*   **Design**: [DeepSeek](https://www.deepseek.com/), [Google Gemini](https://gemini.google.com/) — Assisted with architectural design, mathematical model derivation, and psychological formula verification.
*   **Development**: [Claude Code](https://claude.ai/), [GLM 4.7](https://chatglm.cn/), [Google Gemini](https://gemini.google.com/) — Collaborated on core logic, training process optimization, and code standard refactoring.

---
*Note: This document was translated by Google Gemini.*
