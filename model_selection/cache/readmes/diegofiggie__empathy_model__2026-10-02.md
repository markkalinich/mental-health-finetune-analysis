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
- text: Dear Jonathan, I am writing to find out how things are going on the Beta project.
    I understand that you are enjoying the role and finding new applications.I have
    had some feedback from Terry confirming that you are doing well but there are
    some improvement points that I would like to discuss with you. It has been noted
    that your contributions are providing real value and they enjoy working with you,
    however, some of this value is spoiled by a conversational tone and being a bit
    verbose. In business correspondence it is essential that the facts are clear,
    concise and distinguishable from opinion, otherwise the message may be lost (regardless
    of how good it is).There are a number of significant reports required in the coming
    weeks. Please could you ensure that you confirm with Terry the exact detail and
    format required for specific reports and communication. He should be able to provide
    templates and guidance to ensure that his requirements are met. I would also recommend
    that you undertake a report-writing course, which should help you to ensure that
    you convey your great ideas in the best possible way.I am keen to support you
    to ensure the success of the project and your professional development. When I
    return in 2 weeks I would like to have a conference call with you and Terry to
    better understand how we can help you going forward.  Please could you respond
    to confirm that you have received this email. Regards, William
- text: 'Hi Jonathan, Thank you for your message. I am glad about your excitment on
    this assignment that is important to us, and I hear your will to develop into
    an engenier team leader role which I think is a topic that can be discuss.In order
    to take you to that role, it is important to work on of your development area
    that concern the way you report your analysis.You have a great talent to collect
    data and get new creative ideas, and it is crucial to make you able to be more
    experienced in business writing to make sure that you adress your conclusions
    in a sharp and concise way, avoiding too much commentary.I propose you to write
    down your current reports keeping those 2 objectives in mind: avoid too much commentary
    and focus on the main data that support your conclusions.I suggest you get inspired
    from other reports done internally, that will help you understand better the formalism
    the report should have.Then, let is discuss together the outcome of your report,
    and I would specially would like to know more about the many application you identify
    for Beta Technology that may bring new business opportunity. Just a tip, quantify
    your comments, always.See you soon, and we will have the opportunity to take the
    time to discuss your development plan based on your capacity to be more straight
    to the point in your reports.I am sure you will make a difference. Good luck,
    William'
- text: Hey Jonathan! I've been in touch with Terry, I'm so glad to hear how much
    you are enjoying the Beta Project, I even hear you are hoping that this experience
    will further your ambitions toward a Lead Engineer position! However, I understand
    there has been some issues with your reports that Terry has brought up with you,
    and I wanted to take a few minutes to discuss them.1) Opinion vs. FactsYour reports
    contain a lot of insights about what the data means, and at times finding the
    specific hard facts can be difficult.2) Level of DetailYou include every bit of
    data that you can into your reports, which can make it difficult to take away
    the larger picture.I want to encourage you to take these things away for the following
    reasons:1) your reports are reviewed by everyone in upper management, including
    the CEO! The opinions you have are great, but when evaluating documents the CEO
    just needs to highest level, most important items. The nitty-gritty would fall
    to another department2) as you have a desire to move up and be a Lead Engineer,
    these kinds of reports will be more and more common. Keeping your thoughts organized
    and well documented is going to become a very important skill to have.For your
    next report I would like you to prepare a cover sheet that goes with the report.
    This cover sheet should be a single page highlighting only the key facts of the
    report. Your own opinions and analysis can be included, but let those who are
    interested read it on their own time, the high level facts are key for the meeting
    they will be presented in. I would also encourage you to make sure the rest of
    the report has clearly defined headings and topics, so it is easy to find information
    related to each item. I
- text: Good Afternoon Jonathan, I hope you are well and the travelling is not too
    exhausting. I wanted to touch base with you to see how you are enjoying working
    with the Beta project team? I have been advised that you are a great contributor
    and are identifying some great improvements, so well done. I understand you are
    completing a lot of reports and imagine this is quite time consuming which added
    to your traveling must be quite overwhelming. I have reviewed some of your reports
    and whilst they provide all the technical information that is required, they are
    quite lengthy and i think it would be beneficial for you to have some training
    on report structures. This would mean you could spend less time on the reports
    by providing only the main facts needed and perhaps take on more responsibility.  When
    the reports are reviewed by higher management they need to be able to clearly
    and quickly identify any issues. Attending some training would also be great to
    add to your career profile for the future. In the meantime perhaps you could review
    your reports before submitting to ensure they are clear and consise with only
    the technical information needed,Let me know your thoughts. Many thanks again
    and well done for all your hard work. Kind regards William
- text: 'Jonathan, First I want to thank you for your help with the Beta project.  However,  it
    has been brought to my attention that perhaps ABC-5 didn''t do enough to prepare
    you for the extra work and I would like to discuss some issues. The nature of
    these reports requires them to be technical in nature.  Your insights are very
    valuable and much appreciated but as the old line goes "please give me just the
    facts".  Given the critical nature of the information you are providing I can''t
    stress the importance of concise yet detail factual reports.  I would like to
    review your reports as a training exercise to help you better meet the team requirements.  Given
    that there are some major reports coming up in the immediate future, I would like
    you to review some training options and then present a report for review.  Again
    your insights are appreciated but we need to make sure we are presenting the end-use
    with only the information they need to make a sound business decision. I also
    understand you would like to grow into a leadership position so I would like to
    discuss how successfully implementing these changes would be beneficial in demonstrating
    an ability to grow and take on new challenges. '
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
      value: 0.6153846153846154
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
| Label | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | <ul><li>'Hi Jonathan, and I hope your travels are going well. As soon as you get a chance, I would like to catch up on the reports you are creating for the Beta projects.  Your contributions have been fantastic, but we need to limit the commentary and make them more concise.  I would love to get your perspective and show you an example as well.  Our goal is to continue to make you better at what you do and to deliver an excellent customer experience.  Looking forward to tackling this together and to your dedication to being great at what you do. Safe travels and I look forward to your call.'</li><li>'Hello Jonathan, I hope you day is going well. The purpose of this msg is to improve your communication regarding your work on the Beta Project. You are important which is why we need to make sure that your thoughts and Ideas are clearly communicated with helpful factual info. I want to get your thoughts on how you best communicate and your thoughts on how to communicate more concisely. Please come up with 2-3 suggestions as will I and lets set up a time within the next 48 hours that you and I can build a plan that will help ensure your great work is being understood for the success of Beta. I am confident that we will develop a plan that continues allow your work to help the program. Please meg me what time works best for you when you end your travel. Best, William'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 1     | <ul><li>"Hi Jonathan, As you know I've been away on another assignment, but I just got a download from Terry on your performance so far on the Beta project and wanted to connect with you.  The team is happy with your improvement suggestions, genuine enthusiasm for the project, and everyone really likes working with you.  I appreciate your commitment, and I know that travel isn't always easy.  Terry has shared some of your reporting techniques with me. While we appreciate your insights and attention to detail, we are going to need you to shift gears a little to help the team make their deadlines.  It is difficult for the team to easily separate facts from opinions in your reports, and it would be much easier for them to pass on the great information you're sharing if your reports were more concise and organized.I know this change in work habit might be a challenge for you, but it is imperative for the success of the project.  That being said, I've come up with a game plan for getting your reports to where the team needs them to be for success.  Terry has a lot of experience in business writing, and since he is responsible for passing on your reports to customers and our executive leadership team, I've asked him to sit with you for a couple of hours this week to share some of his edits on your previous reports. This is not in any way a negative exercise, and I really believe it will help both you and the team throughout the project.  Please take this opportunity as a learning experience, and reach out to Terry ASAP to schedule the time! Please shoot me a note with your thoughts on this, and let me know if you have any additional ideas on how to further improve the Beta project reporting.  I'm looking forward to hearing from you, and will check in with Terry as well after you two meet. Thanks! William"</li><li>"Hi Jonathan, I hope you are doing well. Unfortunately I won't be able to talk to you personally but as soon as I am back I would like to spend some time with you. I know you are working on Beta project and your involvement is highly appreciated\xa0, you even identified improvements the team didn't identify, that's great!  This Beta project is key for the company, we need to success all together. In that respect, key priorities are to build concise reports and with strong business writing. Terry has been within the company for 5 years and is the best one to be consulted to upskill in these areas. Could you please liaise with him and get more quick wins from him. It will be very impactful in your career. We will discuss once I'm back about this sharing experience. I'm sure you will find a lot of benefits. Regards William"</li></ul> |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 0.6154   |

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
model = SetFitModel.from_pretrained("diegofiggie/empathy_model")
# Run inference
preds = model("Jonathan, First I want to thank you for your help with the Beta project.  However,  it has been brought to my attention that perhaps ABC-5 didn't do enough to prepare you for the extra work and I would like to discuss some issues. The nature of these reports requires them to be technical in nature.  Your insights are very valuable and much appreciated but as the old line goes \"please give me just the facts\".  Given the critical nature of the information you are providing I can't stress the importance of concise yet detail factual reports.  I would like to review your reports as a training exercise to help you better meet the team requirements.  Given that there are some major reports coming up in the immediate future, I would like you to review some training options and then present a report for review.  Again your insights are appreciated but we need to make sure we are presenting the end-use with only the information they need to make a sound business decision. I also understand you would like to grow into a leadership position so I would like to discuss how successfully implementing these changes would be beneficial in demonstrating an ability to grow and take on new challenges. ")
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
| Word count   | 114 | 187.5  | 338 |

| Label | Training Sample Count |
|:------|:----------------------|
| 0     | 2                     |
| 1     | 2                     |

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
| 0.1   | 1    | 0.1814        | -               |

### Framework Versions
- Python: 3.10.9
- SetFit: 1.0.3
- Sentence Transformers: 2.4.0
- Transformers: 4.38.1
- PyTorch: 2.2.1+cpu
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