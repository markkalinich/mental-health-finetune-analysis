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
- text: Hi Jonathan, I hope you're having safe travels along your way. I'm reaching
    out to you because you are a valued employee, and we appreciate your hard work
    and research. While I understand you are passionate about these projects, it is
    imperative that you keep your reports concise, seeing as we are all continuously
    on a time crunch. Because these reports are not written as efficiently as possible,
    it is taking too much of our time to read and determine which bit of information
    is most valuable. I need you to shift the way you are writing these reports so
    that way we can maximize our work flow processes. We love having you on our team,
    but if you can not make these necessary changes, we may have to relocate your
    skill set to a different department. However, I am positive you can make these
    minor changes in the way you create your reports. Please research the formal way
    to write reports so that way you no longer add too much information. These reports
    should have less opinions, and more facts. I will also send some material for
    you to review on how to keep these reports business friendly. I love your passion
    and your drive, I am hoping we can continue to have you on this project. A few
    minor changes will be all it takes to get the ball rolling in the right direction!
    If you have any concerns, feel free to reach out to me and I will be more than
    happy to assist. Thank you, William
- text: 'Hi Jonathan, I have been hearing about some of the great work you''re doing
    on the Beta project, and wanted to touch base with you on how things are progressing,
    and what more we can do together to help you perform even better than what you
    are already doing Jonathan, Terry has been happy with your work on this project
    and even mentioned to me that you have been able to find improvements we didn''t
    know we needed, but as we move ahead, the team has a few concerns they would like
    us to address - a. Your reports with the technical information have your perspectives
    on the findings, not the technical information itself - we need to address this
    topic b. You need to improve your business writing skills in order to take the
    next leapI know you have been working very hard on this and your performance speaks
    for it, and I know your ambition to become even better, and in that spirit, let''s
    focus on how you can address the above mentioned issues. You are a great asset,
    and that''s why I need you to commit to a development plan in order for us to
    ensure you function at the highest level.We need to commit to the following plan
    of action: a. You start by preparing the technical report only with findings,
    not your perspectives. We value your insights, and would love to have them, but
    in a short memo on top of the technical report to summarize. b. We need to coach
    you by getting you into a business writing course - you''re a great technical
    engineer, but in order to rise up the ladders in business, this is an essential
    skill that you need to gain. I would like to hear your side of the story: your
    view on generating insights, what are the things we can help you out with : are
    there any problems you are having with the team, what extra coaching we can provide,
    what are your ambitions...'
- text: Hi Jonathan, I would like to bring to your attention that your report writing
    should be improved. Your contribution and fact gathering are highly appreciated.
    However, when you compose the ideas into reports, it will be more productive to
    the team if you could separate the facts from your opinions. Your reports influence
    some very critical decisions at ABC-5. So a well written report will benefit many
    people including having higher visibility to high-ranking managers. Please clarify
    with Terry on report format that is most useful for him. Please keep the promised
    deadline. Terry needs your report so that he can compose the project report for
    the higher managers. Please keep the promised deadline.Please refrain from adding
    opinions in the report and mixing with facts. If needed, you can add a summary
    or conclusion as your insight.Can I have your words that you will write a good
    report? Please CC me in your report to Terry in the next 4 weeks. Let me know
    if you have any questions or concerns. Regards, William
- text: Hello Jonathan, I hope you day is going well. The purpose of this msg is to
    improve your communication regarding your work on the Beta Project. You are important
    which is why we need to make sure that your thoughts and Ideas are clearly communicated
    with helpful factual info. I want to get your thoughts on how you best communicate
    and your thoughts on how to communicate more concisely. Please come up with 2-3
    suggestions as will I and lets set up a time within the next 48 hours that you
    and I can build a plan that will help ensure your great work is being understood
    for the success of Beta. I am confident that we will develop a plan that continues
    allow your work to help the program. Please meg me what time works best for you
    when you end your travel. Best, William
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
base_model: sentence-transformers/paraphrase-mpnet-base-v2
---

# SetFit with sentence-transformers/paraphrase-mpnet-base-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/paraphrase-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-mpnet-base-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/paraphrase-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-mpnet-base-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 512 tokens
- **Number of Classes:** 2 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | <ul><li>"Hi Jonathan, I hope this message finds you well. I hear things are going well with the Beta project. That said, Terry mentioned that there were some issues with the reports. From what I understand, they would like them to be more concise and straight to the point, as well as more business focused. I recommend you reach out to Terry so you both could review in detail one of the reports he submits. This should help you help you align to their expectations. Additionally, i'd be happy to review the reports before you send them off to Terry and provide my feedback. I know this  project is important to you, so please let me know how this meeting goes and how else I can help. Regards, William"</li><li>"Jonathan, I hope you are well - I am very excited that you are part of this development team and really appreciate all the support you give to us; while doing this some comments have arise that can be  opportunity areas to improve your work and get this program ahead.1. The communication between team members is not clear and improvements can be done to this: by this I mean to connect more with other team members before submitting your reports.2. One of the reasons you were chosen is because of your enthusiastic attitude and knowledge, but too much information sometimes can harm the delivery reports that needs to be concise and business oriented. 3.Please forward me your latest report so we can discuss it furthermore when I come back and see what can be improve and we can work from there.4. Please don't be discourage, these are opportunity areas that we can engage and as always keep up the good work. Have a great week. Thanks"</li><li>'Hi Jonathan, Good to hear you are enjoying the work. I would like to discuss with you feedback on your assignment and the reports you are producing. It is very important to understand the stakeholders who will be reading your report. You may have gathered a lot of good information BUT do not put them all on your reports. The report should state facts and not your opinions. Create reports for the purpose and for the audience. I would also suggest that you reach out to Terry to understand what information is needed on the reports you produce.Having said that, the additional insights you gathered are very important too. Please add them to our knowledge repository and share with the team. It will be a great sharing and learning experience. You are very valuable in your knowledge and I think that it would benefit you and the organization tremendously when you are to channelize your insights and present the facts well. I would encourage you to enroll for the business writing training course. Please choose a date from the learning calendar and let me know. Regards, William'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 0     | <ul><li>'Jonathan, First I want to thank you for your help with the Beta project.  However,  it has been brought to my attention that perhaps ABC-5 didn\'t do enough to prepare you for the extra work and I would like to discuss some issues. The nature of these reports requires them to be technical in nature.  Your insights are very valuable and much appreciated but as the old line goes "please give me just the facts".  Given the critical nature of the information you are providing I can\'t stress the importance of concise yet detail factual reports.  I would like to review your reports as a training exercise to help you better meet the team requirements.  Given that there are some major reports coming up in the immediate future, I would like you to review some training options and then present a report for review.  Again your insights are appreciated but we need to make sure we are presenting the end-use with only the information they need to make a sound business decision. I also understand you would like to grow into a leadership position so I would like to discuss how successfully implementing these changes would be beneficial in demonstrating an ability to grow and take on new challenges. '</li><li>"Hi Jonathan, How are You doing with the Beta project? It seams You are very exited about the project.There are two topics that I want to point out that I expct to be Your focus on this project.I review the latest report and saw that in addition to a tchnical information that we have agreed to be included in that, there is a lots of commentaries from Your side. It is greeate that You see the opportunities and perspectives on the findings but I ask You to focus on collecting and passing on the technical information according to the agreed template. We can focus on Your ideas separately once the Beta gets to that stage.The second thing I'd like you to focus is the organizing the details in the reports. Please work together with Terry on that. As the deadlines for presenting the reports to CEO are quite challenging, they have lost of hints and tricks how to make the report informative and easy to read. I've have used his experience and competence myself. It is very important that we submit the report on time. Please add me as well to the reciepient list once You send the infotmation to Terry. Good luck!"</li><li>'Good Afternoon Jonathan, I hope you are well and the travelling is not too exhausting. I wanted to touch base with you to see how you are enjoying working with the Beta project team? I have been advised that you are a great contributor and are identifying some great improvements, so well done. I understand you are completing a lot of reports and imagine this is quite time consuming which added to your traveling must be quite overwhelming. I have reviewed some of your reports and whilst they provide all the technical information that is required, they are quite lengthy and i think it would be beneficial for you to have some training on report structures. This would mean you could spend less time on the reports by providing only the main facts needed and perhaps take on more responsibility.  When the reports are reviewed by higher management they need to be able to clearly and quickly identify any issues. Attending some training would also be great to add to your career profile for the future. In the meantime perhaps you could review your reports before submitting to ensure they are clear and consise with only the technical information needed,Let me know your thoughts. Many thanks again and well done for all your hard work. Kind regards William'</li></ul> |

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
model = SetFitModel.from_pretrained("gmenchetti/paraphrase-mpnet-base-v2-empathy")
# Run inference
preds = model("Hello Jonathan, I hope you day is going well. The purpose of this msg is to improve your communication regarding your work on the Beta Project. You are important which is why we need to make sure that your thoughts and Ideas are clearly communicated with helpful factual info. I want to get your thoughts on how you best communicate and your thoughts on how to communicate more concisely. Please come up with 2-3 suggestions as will I and lets set up a time within the next 48 hours that you and I can build a plan that will help ensure your great work is being understood for the success of Beta. I am confident that we will develop a plan that continues allow your work to help the program. Please meg me what time works best for you when you end your travel. Best, William")
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
| Training set | Min | Median   | Max |
|:-------------|:----|:---------|:----|
| Word count   | 95  | 213.2333 | 377 |

| Label | Training Sample Count |
|:------|:----------------------|
| 0     | 13                    |
| 1     | 17                    |

### Training Hyperparameters
- batch_size: (4, 4)
- num_epochs: (3, 3)
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
| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.0033 | 1    | 0.3705        | -               |
| 0.1667 | 50   | 0.2017        | -               |
| 0.3333 | 100  | 0.0503        | -               |
| 0.5    | 150  | 0.0006        | -               |
| 0.6667 | 200  | 0.0005        | -               |
| 0.8333 | 250  | 0.0001        | -               |
| 1.0    | 300  | 0.0002        | -               |
| 1.1667 | 350  | 0.0002        | -               |
| 1.3333 | 400  | 0.0001        | -               |
| 1.5    | 450  | 0.0001        | -               |
| 1.6667 | 500  | 0.0           | -               |
| 1.8333 | 550  | 0.0           | -               |
| 2.0    | 600  | 0.0001        | -               |
| 2.1667 | 650  | 0.0001        | -               |
| 2.3333 | 700  | 0.0           | -               |
| 2.5    | 750  | 0.0           | -               |
| 2.6667 | 800  | 0.0001        | -               |
| 2.8333 | 850  | 0.0           | -               |
| 3.0    | 900  | 0.0           | -               |

### Framework Versions
- Python: 3.10.13
- SetFit: 1.0.3
- Sentence Transformers: 2.6.1
- Transformers: 4.39.3
- PyTorch: 2.0.0.post200
- Datasets: 2.16.1
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