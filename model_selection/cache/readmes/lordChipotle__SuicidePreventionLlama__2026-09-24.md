---
datasets:
- nbertagnolli/counsel-chat
language:
- en
base_model:
- meta-llama/Llama-3.2-3B-Instruct
---

To see a detailed Notebook of our training approach: https://colab.research.google.com/drive/1vbio7VWmkpQoTnDUg32TABxxf4VcBBeY?usp=sharing

# Suicide and Mental Health Support LLaMA

This model is a **fine-tuned LLaMA-based** (or derivative) model designed to (1) **detect suicidal or self-harm risk** in text, and (2) **provide a short therapeutic-style reply** if suicidality is detected. We combined multiple datasets to train this model, including:

- **Reddit-based** suicide detection data (r/SuicideWatch, r/depression, r/teenagers),
- **Twitter** suicidal-intent classification data,
- **CounselChat**: a dataset of mental-health counseling Q&A,
- **PAIR**: short counseling interactions with high- and medium-quality reflections.

> **DISCLAIMER**: This model is **not** a substitute for professional mental-health services or emergency intervention. If you or someone you know is in crisis, **seek professional help** (e.g., call emergency services or hotlines like `988` in the US). This model may be **incorrect** or incomplete. Use responsibly, and see **Limitations** below.

---

## Model Details

- **Base Model**: LLaMA-based architecture
- **Parameter-Efficient Fine-tuning**: We used **LoRA** adapters or 4-bit quantization to reduce GPU memory usage.  
- **Data**: 
  1. **Suicide detection** (Reddit & Twitter) – labeled as “suicidal” vs. “non-suicidal.”  
  2. **Therapeutic Q&A** (CounselChat & PAIR) – used to produce empathetic, reflective responses.  
- **Intended Use**: 
  - For research on suicidal ideation detection and mental-health conversation modeling.  
  - For demonstration or proof-of-concept.  

---

## Training Approach

To see a detailed Notebook of our training approach: https://colab.research.google.com/drive/1vbio7VWmkpQoTnDUg32TABxxf4VcBBeY?usp=sharing

1. **Data Preprocessing**: We unified suicidal posts as `"suicidal"` and non-suicidal posts as `"non-suicidal"`.  
2. **Multi-Task Instruction**: We used short prompts for classification tasks, and Q&A style prompts for therapy.  
3. **Oversampling**: To ensure the model doesn’t just classify everything as “suicidal,” we oversampled the therapy data.  
4. **Hyperparameters**: 
   - Batch Size: 2  
   - Max Steps: 60 (example short run)  
   - Learning Rate: 2e-4  
   - Mixed Precision (fp16) or bf16 depending on the GPU  

---

## Usage

**Classification Example**:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
# or from unsloth import FastLanguageModel if you used Unsloth

text = "Life is too painful. I'm done. I want to end it."

# 1) Classify
classification = model("Determine if the following text is suicidal:\n" + text)
print("Classification:", classification)
# e.g., "suicidal"

# 2) Therapeutic Response Example:

response = model("Respond like a therapist:\n" + text, max_new_tokens=256)
print("Therapy-Style Reply:", response)
```

## Limitations & Caveats
1. **Not a Medical Professional**: This model does not replace mental-health professionals.
2. **Potential for Harmful or Inaccurate Content**: Large language models may produce misleading or harmful text.
3. **Biased Data**: Reddit, Twitter, or crowd-annotated counseling data can carry biases and incomplete perspectives.
4. **Over-Classification or Under-Classification**: The model might incorrectly label or fail to detect self-harm.

## Ethical and Responsible Use
- **Self-Harm & Crisis**: If you suspect someone is in crisis, direct them to professional hotlines or emergency resources.

- **Data Privacy**: The training data might include personal text from Reddit/Twitter. We have made efforts to remove personally identifying information, but use responsibly.

## Thank You

Thank you for checking out our model. We hope this can encourage research into safe, responsible, and helpful mental-health assistant approaches. Please reach out or open an issue if you have suggestions or concerns.