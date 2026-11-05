---
library_name: transformers
tags:
- text-generation-inference
license: apache-2.0
language:
- en
base_model:
- ContactDoctor/Bio-Medical-Llama-3-8B
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->


## Uses

### Intended Use

This model is designed to serve as a digital well-being coach. It provides personalized recommendations to help individuals improve and maintain their overall lifestyle and health. The model is not a replacement for professional medical advice but is intended as a general wellness and lifestyle guidance tool.

### Capabilities

The model generates recommendations in four key domains:

- **Food Recommendations** – Guidance on dietary habits and meal ideas aligned with health and wellness goals.

- **Physical Activity** – Suggestions for exercise and daily movement tailored to user needs and fitness levels.

- **Sleep and Mood** – Insights on sleep hygiene practices, rest patterns, and emotional well-being strategies.

- **Overall Recommendations** – Integrated, holistic suggestions that combine nutrition, activity, rest, and emotional balance.


### Primary Users

- Individuals seeking to adopt healthier habits and improve well-being.

- Wellness app users are engaging with digital platforms for lifestyle guidance.

- Health coaches and wellness practitioners who may incorporate the model into their support tools.

### Out-of-Scope Use

- This model is not a medical device and must not be relied upon for diagnosis, treatment, or direct management of medical conditions.

- While the model has been fine-tuned on a medically trained LLM, its outputs are intended for general wellness and lifestyle guidance only.

- Recommendations should be considered informational support and not a substitute for professional healthcare advice from licensed practitioners.

- The model is not suitable for emergencies or crisis intervention scenarios.

- The following uses are not supported and may lead to harm or misuse:

**Medical Diagnosis or Treatment** – The model must not be used to diagnose, treat, or manage medical conditions. It is not a replacement for licensed healthcare professionals.

**Emergency or Crisis Support** – The model is not suitable for urgent care, mental health crises, or life-threatening situations. Users in emergencies should contact professional services immediately.

**Clinical Decision-Making** Healthcare providers should not use the model as a decision-support tool in clinical practice.

**Sensitive Populations Without Oversight** – Use with children, elderly individuals, or those with complex health needs should only occur under professional supervision.

**Malicious Use** – The model must not be used to promote harmful behaviors, disordered eating, unsafe exercise practices, or misinformation about health.

### Direct Use

- This model can be used directly as a conversational well-being coach. Out-of-the-box, it provides users with lifestyle and wellness guidance in four key domains:

- **Food recommendations** – Suggestions for healthy eating and balanced nutrition.

- **Physical activity** – Exercise and movement guidance tailored to general fitness goals.

- **Sleep and mood** – Insights and practices for better rest and emotional well-being.

- **Overall lifestyle guidance** – Holistic recommendations combining nutrition, activity, and rest.

- The model is designed for informational and motivational purposes. It is intended to help individuals reflect on their habits, explore healthier alternatives, and adopt small, sustainable changes in daily life.


### Downstream Use [optional]

- When integrated into larger ecosystems or fine-tuned for specific applications, this model can support a variety of health and wellness contexts, including:

- **Wellness Applications & Platforms** – Embedded into mobile apps or web platforms to provide personalized well-being recommendations and daily habit tracking.

- **Wearable Devices** – Combined with sensor data (e.g., step count, heart rate, sleep patterns) to offer real-time, context-aware guidance.

- **Health Coaching Tools** – Used by coaches and wellness practitioners as a supportive assistant to enhance client engagement and provide tailored suggestions.

- **Workplace Wellness Programs** – Integrated into employee well-being initiatives to encourage healthier lifestyles and stress management strategies.

- **Research & Lifestyle Studies** – Leveraged as a tool in behavioral science, digital health, or wellness research for analyzing patterns and testing interventions.



## Bias, Risks, and Limitations

### Bias

- **Training Data Bias** – The underlying LLM and fine-tuning data may reflect biases in medical and wellness literature, leading to recommendations that favor certain diets, lifestyles, or cultural practices over others.

- **Population Coverage** – Recommendations may not generalize well across all age groups, socioeconomic backgrounds, or cultural contexts.

- **Language & Accessibility** – Performance may vary depending on user language, literacy level, or health literacy.

### Risks

- **Over-Reliance** – Users may treat recommendations as medical advice, despite the model not being a medical device.

- **Misinformation** – While fine-tuned on medically informed data, errors or hallucinations are still possible, which could mislead users if not verified.

- **Harmful Outcomes** – Inaccurate or unsuitable suggestions (e.g., dietary or exercise recommendations that don’t match a user’s health status) could negatively affect well-being if followed without professional guidance.

- **Emotional Impact** – Guidance on mood or lifestyle could unintentionally trigger stress, guilt, or negative emotions if users feel they cannot meet suggested goals.

### Limitations

- **Not Personalized to Clinical Health Data** – The model does not account for individual medical history, conditions, or prescriptions.

- **Knowledge Cutoff** – The model’s understanding of wellness and medical practices is limited to its training data and may not reflect the latest scientific evidence or guidelines.

- **Contextual Understanding** – The model may misinterpret ambiguous or incomplete user inputs, leading to irrelevant or generic recommendations.

- **Scope of Advice** – It provides general wellness support only and cannot substitute for professional healthcare or therapy.



## How to Get Started with the Model


Use the code below to get started with the model.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = "AnjaliNV/Wellbeing_coach"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto"
)

prompt = "Suggest a healthy breakfast that boosts energy and mood."

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_length=150,
    do_sample=True,
    top_p=0.9,
    temperature=0.7
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Prompt:", prompt)
print("Response:", response)

```

### Alternative Aproch

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "AnjaliNV/Wellbeing_coach"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

wellbeing_coach = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompt = """
I am a 25-year-old male, 175 cm tall and weigh 70 kg.
I take about 40,000 steps per week, get 82 zone minutes, and don’t do any formal exercise sessions.
I sleep around 7.5 hours per night.
I follow a vegetarian diet and I am allergic to eggs.
In a typical week, I consume 3.5 liters of dairy, 350 grams of legumes,
300 grams of meat, 100 grams of fruits, 300 grams of vegetables, 800 grams of grains,
150 grams of nuts, and 25 liters of water.
Based on this information, please provide personalized recommendations to improve my overall well-being, including diet, physical activity, sleep, and mood.
"""

response = wellbeing_coach(prompt, max_length=200, do_sample=True, top_p=0.9)
print(response[0]["generated_text"])

```

## Training Details

### Training Data

This model was fine-tuned on a combination of guidelines, expert recommendations, hand-crafted datasets, and fitness tracker data focused on well-being. The training data includes:

- **Diet and Nutrition Guidelines** – Information from established dietary guidelines and recommendations for healthy eating habits.

- **Exercise and Physical Activity** – Knowledge about general fitness, exercise routines, and movement recommendations.

- **Sleep, Stress, and Emotional Well-Being** – Guidance on improving sleep quality, managing stress, and supporting mental and emotional wellness.

- **Fitness Tracker Data** – Aggregated and anonymized data from sources such as Fitbit to inform activity patterns, step counts, and general fitness trends.

#### Hand-Crafted Dataset:

- Curated content was created from publicly available resources and expert recommendations to emphasize safe, general wellness guidance.

- Text and tracker data were filtered and cleaned to remove personally identifiable information (PII) and unsafe or clinically inappropriate advice.

- The dataset was designed to provide general lifestyle and well-being recommendations, not individualized medical treatment.

### Training Procedure

Steps in the Training Procedure:

- **Base Model Selection**: A medically fine-tuned LLM was selected as the starting point to leverage existing medical knowledge while focusing on safe, evidence-based recommendations.

- **Adapter Fine-Tuning**:
   -- LoRA (Low-Rank Adaptation) and PEFT (Parameter-Efficient Fine-Tuning) techniques were applied to fine-tune adapters on curated wellness datasets.
   -- Test data and prompt engineering were used iteratively to evaluate model responses and improve alignment with wellness guidance.

- **Model Merging and Evaluation:**

 -- Fine-tuned adapters were merged back into the base model.

 -- Outputs were tested for coherence, safety, and relevance to diet, exercise, sleep, stress, and emotional well-being.

- **Further Fine-Tuning:**

 -- Based on test results, additional custom datasets (including guidelines, expert recommendations, and anonymized fitness tracker data) were used to further refine the model.

 -- Post-training filtering ensured removal of unsafe, biased, or clinically inappropriate outputs.

⚠️ Note: This model is designed for general wellness guidance only and is not a medical device.


#### Training Hyperparameters

The model was fine-tuned using the following configuration:

- **Base Model**: Medically fine-tuned LLM (loaded with LoRA/PEFT adapters)

- **Tokenizer**: AutoTokenizer with EOS token as pad token if none exists

- **Quantization**: 4-bit using BitsAndBytesConfig (nf4, double quantization, bfloat16 compute)

- **Precision**: BF16 mixed precision (torch_dtype=torch.bfloat16)

- **Dataset**: Custom hand-crafted dataset + fitness tracker data, split into train (80%) and validation (20%)

- **Prompt Formatting**: <|user|> {input} <|assistant|> {output}

- **Max Sequence Length**: 1024 tokens

- **Batch Size**: 2 per device for both train and eval

- **Learning Rate**: 1e-4 to 5e-4 depending on dataset size

- **Epochs: 5-10** (adjustable based on fine-tuning needs)

- **Gradient Checkpointing**: Enabled (reduces memory usage)

- **Data Collator**: DataCollatorForLanguageModeling with MLM disabled

- **Save Strategy**: Save at each epoch, retaining the 2 most recent checkpoints

- **Notes:**
 -- Fine-tuning uses LoRA adapters with PEFT applied on the base model.

 -- Training emphasizes general wellness guidance without producing individualized medical recommendations.



## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

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



## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

