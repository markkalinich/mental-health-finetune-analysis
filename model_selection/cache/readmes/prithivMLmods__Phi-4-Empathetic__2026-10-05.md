---
license: mit
language:
- en
base_model:
- microsoft/phi-4
pipeline_tag: text-generation
library_name: transformers
tags:
- text-generation-inference
- phi
- phi3
- llama
- human_like_reasoning
---
![4.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/kfT6j0uZRKZiUxRT7F--f.png)

# **Phi-4 Empathetic [ Responsible Reasoning & Emotional Thought Generation ]**

`[Phi-4 Empathetic finetuned]` from Microsoft's Phi-4 is an advanced open model built upon a blend of high-quality synthetic datasets, data from filtered public domain websites, and carefully selected academic resources. It excels at **responsible human-like reasoning**, **empathetic dialogue**, and **emotional thought generation**. The model is designed to engage in nuanced, thoughtful conversations, with outputs that can include **special characters** and **emojis** for expressive communication. 🌟

Phi-4 Empathetic employs a sophisticated safety post-training approach, leveraging both open-source and proprietary datasets. Safety alignment is achieved using a combination of **SFT (Supervised Fine-Tuning)** and **DPO (Direct Preference Optimization)**, targeting responsible interaction and emotional awareness in diverse contexts.

---

# **Dataset Info**

Phi-4 Empathetic is fine-tuned on a carefully curated dataset tailored for empathetic and responsible reasoning tasks. The dataset incorporates the **Chain of Thought (CoT)** methodology, emphasizing logical reasoning, emotional nuance, and step-by-step thought processes. Additionally, it includes data optimized for generating responses that resonate with human emotions, making it ideal for:

- **Emotional Support Applications** 🤗
- **Responsible Conversations** 💬
- **Thoughtful Problem-Solving** 🧠

---

# **Run with Transformers**

```python
# pip install accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("prithivMLmods/Phi-4-Empathetic")
model = AutoModelForCausalLM.from_pretrained(
    "prithivMLmods/Phi-4-Empathetic",
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

input_text = "Can you share some words of encouragement for someone feeling down?"
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids, max_new_tokens=32)
print(tokenizer.decode(outputs[0]))
```

You can ensure correct formatting for empathetic dialogue by using `tokenizer.apply_chat_template` as follows:

```python
messages = [
    {"role": "user", "content": "Can you share some words of encouragement for someone feeling down?"},
]
input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", return_dict=True).to("cuda")

outputs = model.generate(**input_ids, max_new_tokens=256)
print(tokenizer.decode(outputs[0]))
```

---

# **Intended Use**

The Phi-4 Empathetic model is optimized for applications that require thoughtful and emotionally aware interactions. Below are some suggested use cases:

1. **Emotional Support & Counseling** 💖  
   - Providing thoughtful responses to users seeking emotional encouragement or advice.  
   - Generating empathetic messages for mental health and well-being applications.  

2. **Responsible Dialogue Generation** 🗣️  
   - Engaging in nuanced conversations with a focus on fairness, safety, and ethical considerations.  
   - Ensuring that interactions remain respectful and aligned with safety guidelines.  

3. **Creative Writing Assistance** ✍️  
   - Helping users craft emotionally engaging content, including stories, poems, and personal messages.  
   - Assisting in generating content enriched with special characters and emojis for expressive communication.  

4. **Educational Tools** 🎓  
   - Offering step-by-step explanations with an empathetic tone for better understanding.  
   - Generating thoughtful Q&A responses for various subjects.  

5. **Customer Support** 🤝  
   - Automating empathetic responses to customer queries.  
   - Handling emotionally sensitive customer service interactions with care.  

6. **Social Media Engagement** 📱  
   - Generating creative, engaging, and emotionally resonant posts for social media platforms.  
   - Providing personalized message suggestions enriched with emojis and special characters.  

---

# **Limitations**

While Phi-4 Empathetic is highly capable, it has certain limitations users should be aware of:

1. **Bias and Fairness**:  
   Despite extensive safety alignment, biases may still emerge in the model’s responses. Users should exercise discretion, particularly in sensitive contexts.  

2. **Emotional Nuance**:  
   The model may occasionally misinterpret the emotional tone of a prompt, leading to less relevant or inappropriate responses.  

3. **Real-Time Knowledge**:  
   The model's knowledge is based on the data it was trained on and does not include real-time or post-training updates. It may not reflect recent events or changes in knowledge.  

4. **Safety and Harmlessness**:  
   Although the model is aligned with safety standards, there may still be cases where outputs require human oversight to ensure appropriateness.  

5. **Resource Requirements**:  
   Running the model efficiently may require significant computational resources, especially in large-scale or real-time applications.  

6. **Ethical Considerations**:  
   The model must be used responsibly, avoiding any malicious applications such as generating harmful content or spreading misinformation.  

7. **Domain-Specific Limitations**:  
   While it performs well in general-purpose tasks, it may need further fine-tuning for highly specialized domains, such as legal, medical, or financial applications.  

---

# **Special Features**

1. **Emojis & Special Characters** 🎉💡  
   The model can generate responses with emojis and special characters for expressive communication, making it ideal for social media and personal messaging applications.  

2. **Human-Like Reasoning** 🧠  
   Fine-tuned for **responsible reasoning** and **empathetic dialogue**, it excels at generating thoughtful and human-like responses.  

3. **Advanced Safety Alignment** 🔒  
   The model employs **iterative SFT** and **DPO** techniques to ensure that its outputs are helpful, harmless, and aligned with ethical standards.