---
library_name: transformers
tags: []
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->
### <2025 예술적인 소프트웨어> 대화 생성형 파인튜닝 모델입니다.
### This model was fine-tuned for generative dialogue tasks as part of the 2025 Artistic Software project.


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

### 상황 가정
진료 시간 변경 요청1 : “당신의 이름은 홍길동 이고, 전화번호는 010-1234-5678입니다. 오늘인 2025.07.01 화요일 오전 11시에 경희 내과에 예약이 되어 있습니다. 그런데 갑자기 일정이 생겨 시간이 어렵게 되었습니다. 병원에 전화해 진료 시간을 오후로 변경 가능한지 요청해보세요.” 

위 상황을 조건으로한 사용자, 병원 간의 대화 스크립트를 생성하였고, prompt/completion 형태로 재구성하여 학습 데이터로 사용하였습니다. 
실제 예시는 다음과 같습니다.

### 학습 데이터 예시(.csv)
사용자: 안녕하세요. 오늘 경희내과에 예약이 되어 있는데요, 시간이 좀 어려워서 변경 문의드리려고요.
→ 병원: 네, 안녕하세요. 확인 도와드릴게요. 성함이 어떻게 되실까요?

사용자: 홍길동입니다. 오늘 오전에 예약돼 있었어요.
→ 병원: 잠시만요. 확인되었습니다. 오늘 오전 10시 30분, 내과 진료로 예약되어 있으시네요. 변경 원하시는 시간대 있으신가요?

사용자: 오후 시간대로 바꾸고 싶은데요, 가능한 시간 알려주실 수 있을까요?
→ 병원: 네, 오후에는 2시 20분, 3시 10분, 그리고 4시가 비어 있습니다. 어떤 시간으로 변경해드릴까요?

사용자: 3시 10분으로 부탁드릴게요.
→ 병원: 네, 3시 10분으로 변경해드렸습니다. 진료 10분 전까지 도착 부탁드립니다.

사용자: 감사합니다.
→ 병원: 네, 조심히 오세요. 좋은 하루 보내세요.

### Example Scenario

Resheduling a Medical Appointment 1 : You are a user named Hong Gil-dong with a phone number 010-1234-5678. You have an appointment scheduled at Kyunghee Internal Medicine on Tuesday, July 1, 2025, at 11:00 AM. However, due to a sudden change in plans, you need to call the clinic and ask if it is possible to reschedule the appointment to the afternoon.

Based on this context, a dialogue script between the user and the clinic receptionist was generated.
It was then reformatted into a prompt/completion structure and used as part of the training dataset.

### Sample Dialogue(.csv)
User: 안녕하세요. 오늘 경희내과에 예약이 되어 있는데요, 시간이 좀 어려워서 변경 문의드리려고요.
→ Clinic: 네, 안녕하세요. 확인 도와드릴게요. 성함이 어떻게 되실까요?

User: 홍길동입니다. 오늘 오전에 예약돼 있었어요.
→ Clinic: 잠시만요. 확인되었습니다. 오늘 오전 10시 30분, 내과 진료로 예약되어 있으시네요. 변경 원하시는 시간대 있으신가요?

User: 오후 시간대로 바꾸고 싶은데요, 가능한 시간 알려주실 수 있을까요?
→ Clinic: 네, 오후에는 2시 20분, 3시 10분, 그리고 4시가 비어 있습니다. 어떤 시간으로 변경해드릴까요?

User: 3시 10분으로 부탁드릴게요.
→ Clinic: 네, 3시 10분으로 변경해드렸습니다. 진료 10분 전까지 도착 부탁드립니다.

User: 감사합니다.
→ Clinic: 네, 조심히 오세요. 좋은 하루 보내세요.






This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** [More Information Needed]
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Model type:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed]
- **Finetuned from model [optional]:** [More Information Needed]

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Use the code below to get started with the model.

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

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

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications [optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

[More Information Needed]

#### Software

[More Information Needed]

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Model Card Authors [optional]

[More Information Needed]

## Model Card Contact

[More Information Needed]