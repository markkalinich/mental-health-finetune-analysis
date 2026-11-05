---
license: cc-by-nc-4.0
---

This is the base version (274MB) of the summarization model for the Spanish language presented in the SEMANTiCS 2022 conference (paper entitled "esT5s: A Spanish Model for Text Summarization"). This model was created in 17 hours (using a single GPU, specifically an NVIDIA v100 16GB) from the multilingual T5 model using the XL-Sum dataset. It achieves a ROUGE-1 value of 25.30 (mT5 achieves 26.21 after a 96h training using 4 GPUs), ROUGE-2 8.21 (mT5 achieves 8.74), and ROUGE-l 20.29 (mT5 achieves 21.06). 