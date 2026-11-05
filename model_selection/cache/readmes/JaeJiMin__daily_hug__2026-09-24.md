---
license: mit
datasets:
- jaewanlee/korean_chat_friendly
base_model: google/gemma-2-2b-it
pipeline_tag: text2text-generation
tags:
- counseling
- psychology
language:
- ko
---
# daily_hug: A Friendly Korean Chatbot with Mental Health Insights

`daily_hug` is a conversational model designed to engage users in friendly, everyday conversations in Korean. While the model predominantly focuses on light and casual discussions, it is also capable of identifying signs of serious mental health issues. When such signs are detected, the model will gently suggest that there may be an issue worth considering. This makes `daily_hug` both a supportive conversational partner and a helpful companion in times of need.

The model is based on the Gemma architecture and has been fine-tuned with a conversational dataset to make its responses friendly, natural, and empathetic. The dataset used is [JaeJiMin/korean_chat_friendly](https://huggingface.co/datasets/JaeJiMin/korean_chat_friendly).

## Model Description
* Model Name: daily_hug
* Developed by: Jaewan Lee and Sangji You
* Language: Korean (한국어)
* Task: Causal Language Modeling, Natural Language Understanding, Mental Health Insights
* Base Model: The model is based on google/gemma-2b-it and was inspired by the [Psychologist character on Character.ai](https://character.ai/chat/Hpk0GozjACb3mtHeAaAMb0r9pcJGbzF317I_Ux_ALOA)
* Dataset Used: The model was fine-tuned using the dataset jaewanlee/korean_chat_friendly.
* Architecture: This is a causal language model (GPT-based) trained to carry out natural, flowing conversations and offer mental health suggestions when necessary.

## Model Goals
The goal of daily_hug is to provide:

1. Friendly and empathetic conversations: The model simulates a chat partner who is supportive, kind, and conversationally engaging.
2. Mental health insights: If the user shows signs of mental distress or issues, the model subtly points out potential concerns.

This model can be used for casual conversations with an added benefit of providing mental health awareness without making explicit suggestions or diagnosis.

## Model Training

The `daily_hug` model was fine-tuned using a combination of low-rank adaptation (LoRA) and the `PeftModel` from Hugging Face's `transformers` library. This approach allowed for efficient training on limited hardware resources without sacrificing model performance. The base model, `google/gemma-2b-it`, was adapted to engage in casual Korean conversations with added empathy and mental health awareness.

### Training Process:
1. **Base Model**: The starting point for `daily_hug` was the google/`gemma-2b-it model`, a large language model optimized for natural language generation tasks.
2. **LoRA Adapters:** LoRA (Low-Rank Adaptation) was employed to efficiently fine-tune the model while reducing memory overhead. This allowed us to update a small number of parameters rather than fine-tuning the entire model, making it faster and more resource-efficient.
3. **Dataset**: The fine-tuning process used the [JaeJiMin/korean_chat_friendly](https://huggingface.co/datasets/JaeJiMin/korean_chat_friendly) dataset, which contains friendly, conversational data in Korean. The dataset was structured to mimic daily life conversations, with a particular focus on empathy and casual dialogue.
4. **Training Configuration**:
    * Optimizer: The AdamW optimizer was employed with 8-bit precision (`paged_adamw_8bit`) to handle large model parameters effectively.
    * Batch Size: Due to hardware constraints, gradient accumulation was used to simulate larger batch sizes, allowing the model to train effectively with smaller memory requirements.
    * Precision: Mixed precision (FP16) was used to speed up computations and reduce memory usage.
    * Adapters: After the LoRA fine-tuning, the adapters were merged back into the base model to provide an efficient and streamlined deployment.
    * Final Merge: Once training was completed, the LoRA adapters were merged back into the model for deployment, ensuring a seamless integration of fine-tuned conversational abilities with the mental health insights functionality.

This training process allowed the model to balance efficiency with performance, creating a conversational agent that can engage in friendly dialogue while subtly detecting signs of mental distress when necessary.
## How to Use
To use the model, you can load it with the `transformers` library in Python as follows:

```
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("jaewanlee/daily_hug")
model = AutoModelForCausalLM.from_pretrained("jaewanlee/daily_hug")

# Example input
input_text = "안녕! 오늘 하루 어땠어?"

# Tokenize and generate response
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)

# Decode and print response
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
You can chat with the model using this simple script. The model responds to casual conversation and, if it detects signs of distress, may offer gentle mental health-related suggestions.

## Model Limitations
While the model can provide conversational support and suggest mental health awareness, it is **not a replacement for professional mental health advice**. If you or someone you know is experiencing severe mental health issues, please seek help from a qualified professional.

* The model is trained in Korean and might not work as expected in other languages.
* The model might occasionally misinterpret or fail to detect mental health concerns due to the complexity and nuance of human emotions.

## Citation

If you use this model, please cite the following:

```
@misc{daily_hug,
  author = {Jaewan Lee and Sangji You},
  title = {daily_hug: A Friendly Korean Chatbot with Mental Health Insights},
  year = {2024},
  url = {https://huggingface.co/jaewanlee/daily_hug}
}
```