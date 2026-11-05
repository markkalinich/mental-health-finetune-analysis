---
library_name: transformers
tags:
- bert
- financial-sentiment-analysis
- sentiment-analysis
- tariff
license: mit
language:
- en
metrics:
- accuracy
base_model:
- ProsusAI/finbert
---

## Summary

<!-- Provide a quick summary of what the model is/does. -->
TariffBERT is a fine-tuned version of **ProsusAI/finbert** for **financial sentiment analysis** focused on *tariff and trade-policy news*.  
It classifies English-language text into **Positive**, **Negative** or **Neutral** sentiment toward tariff-related market impact.


## Model Details

- **Developed by:** Cristobal Medina Meza ([@CristobalMe](https://huggingface.co/CristobalMe))
- **Model type:** BERT-based sequence classifier
- **Language:** English
- **License:** MIT
- **Finetuned from:** [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert)

<!-- 
### Model Sources [optional] TO DO

<!-- Provide the basic links for the model. -->

<!-- - **Repository:** [More Information Needed] -->
<!-- - **Paper [optional]:** [More Information Needed] -->
<!-- - **Demo [optional]:** [More Information Needed] -->

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->


### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
- Sentiment classification of news articles and headlines, regulatory filings, or analyst notes discussing **tariffs, trade wars, or import/export policy**.
- Can be used as-is via the Hugging Face `pipeline("text-classification")`.

### Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

- As a component in financial forecasting, event-driven trading strategies, or risk dashboards.
- Further fine-tuning on sector-specific trade data.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

- Non-financial general sentiment tasks (movie reviews, product opinions).
- High-stakes decision-making (e.g., compliance enforcement) without human oversight.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

- Domain bias: Training data is tariff/trade news; performance may degrade on unrelated finance text.

- Temporal drift: Model reflects market language up to its training cutoff SEPTEMBER 2025; newer policy jargon may be misclassified.

- Geographic bias: Data may over-represent US trade discourse.

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

**Use confidence thresholds and human review in production.**

## How to Get Started with the Model

Use the code below to get started with the model.
```{python}
from transformers import pipeline

pipe = pipeline("text-classification", model="CristobalMe/TariffBERT")

text = "This is an example text for classification."

result = pipe(text)

print(result)
```

<!-- TO DO

## Training Details TO DO

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

<!--
[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

<!--
#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->
<!--
#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

<!--
[More Information Needed]

-->

<!-- 
## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

<!-- 
### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

#### Metrics

Accuracy

### Results

Accuracy: 0.9


## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

- **Hardware Type:** Apple MacBook Pro 14″ (M4 Pro, 14-core CPU / 20-core GPU)
- **Training Time:** ~15 minutes
- **Energy Use Estimate:** ≈0.02 kWh  
- **Estimated Carbon Emissions:** ≈0.01 kg CO2eq  


<!--
## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

<!--
**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]
-->

## Model Card Contact

For questions or collaboration, email [hello@cmm.fyi](hello@cmm.fyi)

Or contact [@CristobalMe](https://github.com/CristobalMe)