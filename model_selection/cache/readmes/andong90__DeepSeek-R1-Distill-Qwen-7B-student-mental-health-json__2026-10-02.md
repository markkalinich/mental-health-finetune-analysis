---
library_name: transformers
tags:
- unsloth
license: mit
datasets:
- jordanfan/esconv_processed
language:
- en
base_model:
- deepseek-ai/DeepSeek-R1
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** [an.dong90]

- **Model type:** [Fine tuned distilled Deepseek R1 Qwen 7B model]
- **Language(s) (NLP):** [English]
- **License:** [MIT]
- **Finetuned from model [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B]

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

Traning process: https://github.com/dojian/mental_health_chatbot/blob/main/notebooks/Json_conv.ipynb

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

prompt_test = """Given a student's Conversation History and Current Message, extract the relevant metadata, including emotion type, emotion intensity (1-5), problem type, and counseling strategy.
Then answer the student's Current Message as a counselor based on the metadata. Keep it concise but affirmative.
The counselor must return a Structured JSON Response with these fields: "emotion_type","emotion_intensity", "problem_type", "counseling_strategy","answer".

### Student:
**Conversation History:**
{user_history}

**Current Message:**
{user_text}

### Counselor Structured JSON Response:
"""

FastLanguageModel.for_inference(model)     
inputs = tokenizer([prompt_test.format(user_history=user_history,user_text=user_text)], return_tensors="pt").to("cuda")    
outputs = model.generate(    
    input_ids=inputs.input_ids,    
    attention_mask=inputs.attention_mask,   
    max_new_tokens=250,   
    eos_token_id=tokenizer.eos_token_id,   
    num_return_sequences=1,   
    temperature=0.6, # deepseek doc recommended 0.6 to balance creativity and coherence, avoiding repetitive or nonsensical outputs.    
    top_p=0.9,  # Reduces repeated phrases    
    use_cache=True,     
)     
response = tokenizer.decode(outputs[0],skip_special_tokens=True)

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->
https://huggingface.co/datasets/jordanfan/esconv_processed


### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->
3 LLMs as judges 
DeepSeek R1 Distilled Llama 8B 
DeepSeek R1 Distilled Qwen 7B
Mistral 7B v0.3


Assessed generated responses based on empathy, appropriateness, and relevance on scale of 1-5
Metrics proposed on Medium article in similar mental health setting* 

Averaged score across judges
  
Median
Empathy-4.00
Appropriateness-5.00
Relevance-4.33
 
### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

[More Information Needed]

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

### Results

[More Information Needed]

#### Summary

