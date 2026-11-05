---
license: cc-by-4.0
---
# BUD-E Whisper: Emotional Speech Captioning Model


**BUD-E Whisper** is a suite of Whisper models fine-tuned for **direct emotional speech captioning**. The core models are built upon OpenAI's Whisper architecture, with the current primary variant being a fine-tune of **OpenAI Whisper Small**. These models are designed to generate text captions that not only transcribe speech but also inherently reflect its emotional content.

**V 1.1 Update:** This version was finetuned on 20k samples from the Emolia dataset, that score high in the 40 categories & had been recaptioned with Gemini 2.5 Pro to describe reverb, gender & background events better.


## License

This model is released under the CC-by-4.0 license. Please give attribution to Maurice Kraus & Christoph Schuhmann, who made this model.

## Colab 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VoAtmNhY1hI5Yzv1_dppHTcYky82OCDK?usp=sharing)

## Training Data

BUD-E Whisper was trained on a combination of:
*   The **[Laion's Got Talent (Enhanced Flash Annotations and Long Captions) dataset](https://huggingface.co/datasets/laion/laions_got_talent_enhanced_flash_annotations_and_long_captions)**.
*   An **internal dataset** comprising approximately **5,000 hours of public Vlogs** and similar audio content.

## Training Procedure & Caption Generation

A key aspect of BUD-E Whisper's development was a multi-step caption refinement process to create rich training targets:

1.  **Initial Score Generation:** An iterative process using Gemini Flash 2.0 generated initial 40-dimensional emotion scores (0-4 scale) and 15 additional dimensions like age, arousal, valence, dominance, harshness, vocalbursts,... for all audio snippets.
2.  **Templated Captions:** These scores were converted into templated string captions.
3.  **Paraphrasing for Richness:** Gemini Flash 2.0 was then used to paraphrase these templated captions, creating diverse and semantically rich training targets.
4.  **Fine-tuning:** Various Whisper model sizes (including the aforementioned fine-tune of OpenAI Whisper Small) were fine-tuned on these refined, emotionally-aware captions.

This multi-step caption refinement was crucial for performance. Direct score regression or simple templated captions were found to lead to suboptimal performance for emotional speech captioning with Whisper models.

## Intended Use

*   Generating emotionally nuanced captions for audio content.
*   Providing rich embeddings for downstream emotion recognition tasks (e.g., with Empathic Insight - Voice).