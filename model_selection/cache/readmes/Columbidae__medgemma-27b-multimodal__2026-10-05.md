---
base_model:
- google/medgemma-27b-text-it
- google/gemma-3-27b-it
---
This is [google/medgemma-27b-text-it](https://huggingface.co/google/medgemma-27b-text-it) with the vision tower and embeddings of [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) attached to restore multimodality. 

**I do not expect the vision function to work with the med data to the same degree as the multimodal 4B medgemma.** It has not been trained beyond the instruct model.