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
- text: Hello Jonathan, Thank you for your work on the Beta project.  I would like
    for us to set up a meeting to discuss your work on the project.  You have completed
    a few reports now and I have had some feedback I would like to share with you;
    specifically the commentary you are providing and your business writing.  The
    additional commentary you are providing makes it difficult to find the objective
    facts of your findings while working with a tight deadline.  I would like to have
    a discussion with you what ideas you may have to help make your reports more concise
    so the team can meet their deadlines. You are investing considerable time and
    effort in these reports and you have expressed your desire to be in an engineering
    role in the future. Your work on these reports can certainly help you in achieving
    your career goals.  I want to make sure you are successful. I'll send out a meeting
    invite shortly. Thank you again Jonathan for all your work on this project.  I'm
    looking forward to discussing this with you.
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
- text: Hi Jonathan, Good to hear you are enjoying the work. I would like to discuss
    with you feedback on your assignment and the reports you are producing. It is
    very important to understand the stakeholders who will be reading your report.
    You may have gathered a lot of good information BUT do not put them all on your
    reports. The report should state facts and not your opinions. Create reports for
    the purpose and for the audience. I would also suggest that you reach out to Terry
    to understand what information is needed on the reports you produce.Having said
    that, the additional insights you gathered are very important too. Please add
    them to our knowledge repository and share with the team. It will be a great sharing
    and learning experience. You are very valuable in your knowledge and I think that
    it would benefit you and the organization tremendously when you are to channelize
    your insights and present the facts well. I would encourage you to enroll for
    the business writing training course. Please choose a date from the learning calendar
    and let me know. Regards, William
- text: Hi Jonathan, I understand you have been quite involved with the Beta Project.
    Your experience is paying off as you are often finding improvements the product
    team did not even know they needed.  I wanted to share some feedback I got from
    one of your colleagues regarding your reports. Your enthusiasm for this project
    is infectious and I love to see this level of engagement. However, we also want
    to be mindful of the end users of the reports you are preparing. In these projects,
    deadlines often move at a fast pace. In order to ensure the project can stay on
    time, it is important to focus on inputting mainly facts when writing these reports.
    You offer a unique perspective and your insights are greatly appreciated. I would
    love to discuss your ideas with you in separate meetings outside of this project.
    I understand you are having to compile and organize a large amount of information.
    I appreciate how overwhelming this can feel at times. When these reports are completed,
    they are reviewed by our CEO and other key stakeholders. To ensure we are respecting
    their time, we want these reports to by concise and well organized. I would like
    you to set up some time with Terry to go over his approach to these reports and
    his writing style. Once I am back from assignment I will set up time to review
    how this meeting went and discuss other ideas you may have. I greatly appreciate
    your efforts on this project and positive attitude. With the above mentioned areas
    of opportunity, I know this project will continue to run smoothly. Thanks.
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
      value: 0.7692307692307693
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
| **all** | 0.7692   |

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
model = SetFitModel.from_pretrained("sijan1/empathy_model")
# Run inference
preds = model("Hello Jonathan, Thank you for your work on the Beta project.  I would like for us to set up a meeting to discuss your work on the project.  You have completed a few reports now and I have had some feedback I would like to share with you; specifically the commentary you are providing and your business writing.  The additional commentary you are providing makes it difficult to find the objective facts of your findings while working with a tight deadline.  I would like to have a discussion with you what ideas you may have to help make your reports more concise so the team can meet their deadlines. You are investing considerable time and effort in these reports and you have expressed your desire to be in an engineering role in the future. Your work on these reports can certainly help you in achieving your career goals.  I want to make sure you are successful. I'll send out a meeting invite shortly. Thank you again Jonathan for all your work on this project.  I'm looking forward to discussing this with you.")
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
- num_iterations: 40
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
| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.025  | 1    | 0.0001        | -               |
| 2.5    | 50   | 0.0001        | -               |
| 0.0667 | 1    | 0.0           | -               |

### Framework Versions
- Python: 3.10.12
- SetFit: 1.0.3
- Sentence Transformers: 2.3.1
- Transformers: 4.35.2
- PyTorch: 2.1.0+cu121
- Datasets: 2.17.0
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