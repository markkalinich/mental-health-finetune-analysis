---
widget:
- text: ' Polygenic risk scores (PRS) describe individual risks for specific diseases based on genetic information from multiple loci. Previous studies suggest that PRS may predict differences in the physiological activation of individuals with agoraphobia. In this study, we examined whether the possibility to predict affected individuals’ heart rate by their PRS depends on the type of exposure trial. We postulated that PRS would predict heart rate within in-vivo as well as in-virtuo trials. Data were analyzed from 132 individuals diagnosed with agoraphobia who underwent either in-vivo (N = 63) or in-virtuo (N = 69) exposure. As assumed, heart rate was significantly predicted by PRS in both trial types. The results of this study suggest that PRS not only provide useful diagnostic information for an individual’s risk of agoraphobia, but that their usefulness in predicting physiological reactions is stable across different exposure settings.'
  example_title: 'Ex1: PRS'
- text: ' According to the Socioeconomic Adaptation Theory of Rehabilitation (SAToR), individuals with higher socioeconomic status (SES) tend to benefit more from psychiatric rehabilitation than individuals with lower SES. In line with the SAToR, we hypothesized that higher SES is associated with a greater reduction in symptom severity in patients with schizophrenia. We conducted an observational study over the course of a 12-month rehabilitation program, encompassing 146 participants with schizophrenia who were newly admitted to a psychiatric rehabilitation clinic. A longitudinal multilevel model was computed to predict rates of change in symptom severity. The average rate of symptom change was 0.6 SD from baseline to 6-month follow-up. Contrary to our hypothesis, symptom change was not significantly predicted by SES. This finding suggests that contrary to the SAToR, individuals with higher socioeconomic status (SES) likely do not benefit more from rehabilitation of schizophrenia than individuals with lower SES.'
  example_title: 'Ex2: SES'
- text: ' There is growing evidence of deficits in defensive reactivity (indexed by the startle blink reflex) in individuals diagnosed with antisocial personality disorder (ASPD). However, to date, no study has examined the role of defensive reactivity in the quality of life (QoL) of individuals with ASPD. In the current study, we therefore explored whether the startle blink reflex is negatively associated with QoL in 143 individuals diagnosed with ASPD. Defensive reactivity was measured using a fear-potentiated startle reflex test. To assess QoL, participants completed the Short Form (36) Health Survey (SF-36). Startle blink reflex potentiation deficits during aversive picture viewing were common in the sample (62.3%). Blink reflex potentiation was negatively and significantly associated with QoL. In sum, these findings provide clear evidence that deficits in defensive reactivity are linked to poor QoL in ASPD.'
  example_title: 'Ex3: Reactivity'
- text: >-
    While the experimental manipulation was successful, there was no effect on
    SMR-BCI performance.
  example_title: 'Ex4: Manipulation Check 1: Successful manipulation check + negative result '
- text: >-
    While the experimental manipulation was unsuccessful, there was an effect on
    SMR-BCI performance.
  example_title: >-
    Ex5: Manipulation Check 2: Unsuccessful manipulation check + positive
    result 
pipeline_tag: text-classification
tags:
- metascience
- psychology
- openscience
- abstracts
license: mit
---

## Model
SciBERT text classification model for positive and negative results prediction in scientific abstracts of clinical psychology and psychotherapy. 
The corresponding paper "Classifying Positive Results in Clinical Psychology Using Natural Language Processing" by Louis Schiekiera, Jonathan 
Diederichs & Helen Niemeyer was published in the special issue *Natural Language Processing in Psychology* in [**ZfP**](https://econtent.hogrefe.com/doi/10.1027/2151-2604/a000563).

## Data
We annotated over 1,900 clinical psychology abstracts into two categories: 'positive results only' and 'mixed or negative results', and trained models using SciBERT.
The SciBERT model was validated against one in-domain (clinical psychology) and two out-of-domain data sets (psychotherapy).
Further information on documentation, code and data for the preprint "Classifying Positive Results in Clinical Psychology Using Natural Language Processing" can be found on this [GitHub repository](https://github.com/schiekiera/NegativeResultDetector).


## Results
**Table 1** <br>
*Different metric scores for model evaluation of test data from the annotated `MAIN` corpus, consisting of *n* = 198 abstracts authored by researchers affiliated with German clinical psychology departments and published between 2012 and 2022*
<table>
    <thead>
        <tr>
            <th rowspan="2"></th>
            <th rowspan="2">Accuracy</th>
            <th colspan="3">Mixed &amp; Negative Results</th>
            <th colspan="3">Positive Results Only</th>
        </tr>
        <tr>
            <th>F1</th>
            <th>Recall</th>
            <th>Precision</th>
            <th>F1</th>
            <th>Recall</th>
            <th>Precision</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>SciBERT</td>
            <td><strong>0.864</strong></td>
            <td><strong>0.867</strong></td>
            <td><strong>0.907</strong></td>
            <td><strong>0.830</strong></td>
            <td><strong>0.860</strong></td>
            <td><strong>0.822</strong></td>
            <td><strong>0.902</strong></td>
        </tr>
        <tr>
            <td>Random Forest</td>
            <td>0.803</td>
            <td>0.810</td>
            <td>0.856</td>
            <td>0.769</td>
            <td>0.796</td>
            <td>0.752</td>
            <td>0.844</td>
        </tr>
        <tr>
            <td>Extracted <em>p</em>-values</td>
            <td>0.515</td>
            <td>0.495</td>
            <td>0.485</td>
            <td>0.505</td>
            <td>0.534</td>
            <td>0.545</td>
            <td>0.524</td>
        </tr>
        <tr>
            <td>Extracted NL Indicators</td>
            <td>0.530</td>
            <td>0.497</td>
            <td>0.474</td>
            <td>0.523</td>
            <td>0.559</td>
            <td>0.584</td>
            <td>0.536</td>
        </tr>
        <tr>
            <td>Number of Words</td>
            <td>0.475</td>
            <td>0.441</td>
            <td>0.423</td>
            <td>0.461</td>
            <td>0.505</td>
            <td>0.525</td>
            <td>0.486</td>
        </tr>
    </tbody>
</table>

<br>

**Figure 1** <br>
*Comparing model performances across in-domain and out-of-domain data; Colored bars represent different model types; Samples: `MAIN` test: n = 198 abstracts; `VAL1`: n = 150 abstracts; `VAL2`: n = 150 abstracts.*
![alt text](https://github.com/schiekiera/NegativeResultDetector/blob/main/img/barplot_results_models.jpg?raw=true)

<br>



## Using the model on Huggingface
The model can be used on Hugginface utilizing the "Hosted inference API" in the window on the right.
Click 'Compute' to predict the class labels for an example abstract or an abstract inserted by yourself.
The class label 'positive' corresponds to 'positive results only', while 'negative' represents 'mixed or negative results'.
  
## Using the model for larger data
```
from transformers import AutoTokenizer, Trainer, AutoModelForSequenceClassification
## 1. Load tokenizer
tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')

## 2. Apply preprocess function to data
def preprocess_function(examples):
    return tokenizer(examples["text"],
                     truncation=True,
                     max_length=512,
                     padding='max_length'
                     )
tokenized_data = dataset.map(preprocess_function, batched=True)

# 3. Load Model
NegativeResultDetector = AutoModelForSequenceClassification.from_pretrained("ClinicalMetaScience/NegativeResultDetector")

## 4. Initialize the trainer with the model and tokenizer
trainer = Trainer(
    model=NegativeResultDetector,
    tokenizer=tokenizer,
  )

# 5. Apply NegativeResultDetector for prediction on inference data
predict_test=trainer.predict(tokenized_data["inference"])

```

Further information on analyzing your own or our example data can be found in this [script](https://github.com/schiekiera/NegativeResultDetector/blob/main/Scripts/example_folder/Predict_Example_Abstracts_using_NegativeResultDetector.ipynb) 
from our [GitHub repository](https://github.com/schiekiera/NegativeResultDetector).


## Disclaimer
This tool is developed to analyze and predict the prevalence of positive and negative results in scientific abstracts based on the SciBERT model. While publication bias is a plausible explanation for certain patterns of results observed in scientific literature, the analyses conducted by this tool do not conclusively establish the presence of publication bias or any other underlying factors. It's essential to understand that this tool evaluates data but does not delve into the underlying reasons for the observed trends.
The validation of this tool has been conducted on primary studies from the field of clinical psychology and psychotherapy. While it might yield insights when applied to abstracts of other fields or other types of studies (such as meta-analyses), its applicability and accuracy in such contexts have not been thoroughly tested yet. The developers of this tool are not responsible for any misinterpretation or misuse of the tool's results, and encourage users to have a comprehensive understanding of the limitations inherent in statistical analysis and prediction models.

## Funding & Project
This study was conducted as part of the [PANNE Project](https://www.berlin-university-alliance.de/en/commitments/research-quality/project-list-20/panne/index.html) 
(German acronym for “publication bias analysis of non-publication and non-reception of results in a disciplinary comparison”) at Freie Universität Berlin and was 
funded by the Berlin University Alliance. The authors are members of the Berlin University Alliance.
