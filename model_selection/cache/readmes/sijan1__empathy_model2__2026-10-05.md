---
library_name: setfit
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
metrics:
- accuracy
widget:
- text: Hi Jonathan, I just happened to know that you are gathering information for
    our Beta project. While your work is really nice insight and improvement ideas,
    I feel the need to talk to you about what more can be done with your reports I
    have received comments from our team that more time is needed to spent on extracting
    information from your reports. Our team member are looking for technical information
    and redundant comments takes them time to extract the fact and sometime confusing.
    Another thing is that can help us is to organize the report in a more clear, concise
    way. We are showing the reports to our prospect and even the CEO, so we need it
    to be well structured, concise and to the point. I am sure if youspend more time
    to organize your report, you will be able to address this problem. I know you
    are an enthusiastic contributor and you have done a good work until now, but we
    need your reports to be improved for our project team to success. I am afraid
    if the situationis notgetting better we will have to look for someone else towork
    on this project.Please spend more effort to organize your next report and I really
    look forward to your good news
- text: Hi Jonathan, I hope you are doing well. Unfortunately I won't be able to talk
    to you personally but as soon as I am back I would like to spend some time with
    you. I know you are working on Beta project and your involvement is highly appreciated ,
    you even identified improvements the team didn't identify, that's great!  This
    Beta project is key for the company, we need to success all together. In that
    respect, key priorities are to build concise reports and with strong business
    writing. Terry has been within the company for 5 years and is the best one to
    be consulted to upskill in these areas. Could you please liaise with him and get
    more quick wins from him. It will be very impactful in your career. We will discuss
    once I'm back about this sharing experience. I'm sure you will find a lot of benefits.
    Regards William
- text: 'Hi Jonathan, I am glad to hear that you are enjoying your job,  traveling
    and learning more about the Beta ray technology. I wanted to share some feedback
    with you that I received. I want to help you be able to advance in your career
    and I feel that this feedback will be helpful. I am excited that you are will
    to share your perspectives on the findings, however if you could focus on the
    data portion first, and highlight the main points, that would be really beneficial
    to your audience. By being more concise it will allow the potential customers
    and then CEO to focus on the facts of the report, which will allow them to make
    a decision for themselves. I understand that this is probably a newer to writing
    the reports, and I don''t think that anyone has shown you an example of how the
    reports are usually written, so I have sent you some examples for you to review.
    I think that you are doing a good job learning and with this little tweak in the
    report writing you will be able to advance in your career. In order to help you,
    if you don''t mind, I would like to review the report before you submit it and
    then we can work together to ensure it will be a great report. I understand that
    you really enjoy providing your perspectives on the technology and recommendations
    on how it can be used, so we will find a spot for that in the report as well,
    but perhaps in a different section. Thank you so much for your time today and
    I look forward to working with you. '
- text: Hi Jonathan. I have been away a long time and unable to have regular discussions
    with you. As your manager, I feel responsible for your performance and would love
    to you you grow and perform better. I understand that you are travelling and gaining
    so much information that it can be overwhelming. But our role is to present only
    the most relevant and useful information in our report to the Senior management
    and clients. I have received feedback that they are facing some trouble with the
    reports and would like some changes. Let us focus on our project specifications
    and only present the required details. Your detailed insights may be presented
    at a later stage or as a separate report for evaluation. You may take up a course
    or training on the subject and I am also there if you need any help. If you are
    looking forward to a career growth next year, we need this to be a successful
    assignment.
- text: Hi Jonathan, and I hope your travels are going well. As soon as you get a
    chance, I would like to catch up on the reports you are creating for the Beta
    projects.  Your contributions have been fantastic, but we need to limit the commentary
    and make them more concise.  I would love to get your perspective and show you
    an example as well.  Our goal is to continue to make you better at what you do
    and to deliver an excellent customer experience.  Looking forward to tackling
    this together and to your dedication to being great at what you do. Safe travels
    and I look forward to your call.
pipeline_tag: text-classification
inference: true
base_model: sentence-transformers/all-MiniLM-L6-v2
model-index:
- name: SetFit with sentence-transformers/all-MiniLM-L6-v2
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: Unknown
      type: unknown
      split: test
    metrics:
    - type: accuracy
      value: 0.5909090909090909
      name: Accuracy
---

# SetFit with sentence-transformers/all-MiniLM-L6-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 256 tokens
- **Number of Classes:** 2 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | <ul><li>"Jonathan, I hope you are well - I am very excited that you are part of this development team and really appreciate all the support you give to us; while doing this some comments have arise that can be  opportunity areas to improve your work and get this program ahead.1. The communication between team members is not clear and improvements can be done to this: by this I mean to connect more with other team members before submitting your reports.2. One of the reasons you were chosen is because of your enthusiastic attitude and knowledge, but too much information sometimes can harm the delivery reports that needs to be concise and business oriented. 3.Please forward me your latest report so we can discuss it furthermore when I come back and see what can be improve and we can work from there.4. Please don't be discourage, these are opportunity areas that we can engage and as always keep up the good work. Have a great week. Thanks"</li><li>"Hi Jonathan, I hope this message finds you well. I hear things are going well with the Beta project. That said, Terry mentioned that there were some issues with the reports. From what I understand, they would like them to be more concise and straight to the point, as well as more business focused. I recommend you reach out to Terry so you both could review in detail one of the reports he submits. This should help you help you align to their expectations. Additionally, i'd be happy to review the reports before you send them off to Terry and provide my feedback. I know this  project is important to you, so please let me know how this meeting goes and how else I can help. Regards, William"</li><li>'Hi Jonathan, Good to hear you are enjoying the work. I would like to discuss with you feedback on your assignment and the reports you are producing. It is very important to understand the stakeholders who will be reading your report. You may have gathered a lot of good information BUT do not put them all on your reports. The report should state facts and not your opinions. Create reports for the purpose and for the audience. I would also suggest that you reach out to Terry to understand what information is needed on the reports you produce.Having said that, the additional insights you gathered are very important too. Please add them to our knowledge repository and share with the team. It will be a great sharing and learning experience. You are very valuable in your knowledge and I think that it would benefit you and the organization tremendously when you are to channelize your insights and present the facts well. I would encourage you to enroll for the business writing training course. Please choose a date from the learning calendar and let me know. Regards, William'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 0     | <ul><li>'Good Afternoon Jonathan, I hope you are well and the travelling is not too exhausting. I wanted to touch base with you to see how you are enjoying working with the Beta project team? I have been advised that you are a great contributor and are identifying some great improvements, so well done. I understand you are completing a lot of reports and imagine this is quite time consuming which added to your traveling must be quite overwhelming. I have reviewed some of your reports and whilst they provide all the technical information that is required, they are quite lengthy and i think it would be beneficial for you to have some training on report structures. This would mean you could spend less time on the reports by providing only the main facts needed and perhaps take on more responsibility.  When the reports are reviewed by higher management they need to be able to clearly and quickly identify any issues. Attending some training would also be great to add to your career profile for the future. In the meantime perhaps you could review your reports before submitting to ensure they are clear and consise with only the technical information needed,Let me know your thoughts. Many thanks again and well done for all your hard work. Kind regards William'</li><li>'Jonathan, First I want to thank you for your help with the Beta project.  However,  it has been brought to my attention that perhaps ABC-5 didn\'t do enough to prepare you for the extra work and I would like to discuss some issues. The nature of these reports requires them to be technical in nature.  Your insights are very valuable and much appreciated but as the old line goes "please give me just the facts".  Given the critical nature of the information you are providing I can\'t stress the importance of concise yet detail factual reports.  I would like to review your reports as a training exercise to help you better meet the team requirements.  Given that there are some major reports coming up in the immediate future, I would like you to review some training options and then present a report for review.  Again your insights are appreciated but we need to make sure we are presenting the end-use with only the information they need to make a sound business decision. I also understand you would like to grow into a leadership position so I would like to discuss how successfully implementing these changes would be beneficial in demonstrating an ability to grow and take on new challenges. '</li><li>'Hi Jonathan, I wanted to have  a discussion with you but since you are travelling i am sharing in this mailThis is related to Beta project and reports coming from there.While we are all excited by the passion and enthusiasm you are bringing i wanted to share some early feedback with you. 1.Please try to be concise in reports and mention facts that teams can refer . We love opinions but lets save those for our brainstorming discussions. 2.For Business writing as you are getting started to help you set up for success we are nominating you for a training program so that your reports are way more effective. I hope as you set on your growth journey and take larger roles a superb feedback from your peers and stakeholders will help. I truly believe above two points can really help you take you there. Wishing you all the best and do share in case you have feedback or inputs from your side. Regards William'</li></ul> |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 0.5909   |

## Uses

### Direct Use for Inference

First install the SetFit library:

```bash
pip install setfit
```

Then you can load this model and run inference.

```python
from setfit import SetFitModel

# Download from the 🤗 Hub
model = SetFitModel.from_pretrained("sijan1/empathy_model2")
# Run inference
preds = model("Hi Jonathan, and I hope your travels are going well. As soon as you get a chance, I would like to catch up on the reports you are creating for the Beta projects.  Your contributions have been fantastic, but we need to limit the commentary and make them more concise.  I would love to get your perspective and show you an example as well.  Our goal is to continue to make you better at what you do and to deliver an excellent customer experience.  Looking forward to tackling this together and to your dedication to being great at what you do. Safe travels and I look forward to your call.")
```

<!--
### Downstream Use

*List how someone could finetune this model on their own dataset.*
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Set Metrics
| Training set | Min | Median | Max |
|:-------------|:----|:-------|:----|
| Word count   | 129 | 199.5  | 308 |

| Label | Training Sample Count |
|:------|:----------------------|
| 0     | 4                     |
| 1     | 4                     |

### Training Hyperparameters
- batch_size: (16, 16)
- num_epochs: (1, 1)
- max_steps: -1
- sampling_strategy: oversampling
- num_iterations: 20
- body_learning_rate: (2e-05, 2e-05)
- head_learning_rate: 2e-05
- loss: CosineSimilarityLoss
- distance_metric: cosine_distance
- margin: 0.25
- end_to_end: False
- use_amp: False
- warmup_proportion: 0.1
- seed: 42
- eval_max_steps: -1
- load_best_model_at_end: False

### Training Results
| Epoch | Step | Training Loss | Validation Loss |
|:-----:|:----:|:-------------:|:---------------:|
| 0.05  | 1    | 0.238         | -               |

### Framework Versions
- Python: 3.10.12
- SetFit: 1.0.3
- Sentence Transformers: 2.5.0
- Transformers: 4.37.2
- PyTorch: 2.1.0+cu121
- Datasets: 2.17.1
- Tokenizers: 0.15.2

## Citation

### BibTeX
```bibtex
@article{https://doi.org/10.48550/arxiv.2209.11055,
    doi = {10.48550/ARXIV.2209.11055},
    url = {https://arxiv.org/abs/2209.11055},
    author = {Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
    keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
    title = {Efficient Few-Shot Learning Without Prompts},
    publisher = {arXiv},
    year = {2022},
    copyright = {Creative Commons Attribution 4.0 International}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->