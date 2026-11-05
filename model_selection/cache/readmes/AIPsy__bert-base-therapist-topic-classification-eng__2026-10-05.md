---
library_name: transformers
license: mit
language:
- en
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
tags:
- PyTorch
- multi-class-classification
---

This is Bert-base-uncased model fine-tuned for topic classification of therapist remarks in psychotherapeutic contexts. The task is a multi-class classification with the following labels:
```python
id2label = {0: 'Time Up and Future Meetings',
            1: 'Complex Emotions Toward Him',
            2: 'Desires and Disappointments',
            3: 'Personal Growth and Decision-Making',
            4: 'Self-Acceptance and Relationships',
            5: 'Understanding and Confronting Fear',
            6: 'See and Understanding Conversations',
            7: 'Clarifying Meaning and Intent',
            8: 'Desire to Escape and Leave',
            9: 'Uncertainty and Understanding Issues',
            10: 'Open Conversation and Sharing',
            11: 'Exploring Emotional Hurt and Bitterness',
            12: 'Guilt and Self-Blame Dynamics',
            13: 'Dynamics of Meaningful Relationships',
            14: 'Struggles and Desires in Learning',
            15: 'Gender Roles and Relationships',
            16: 'Struggles with Personal Change',
            17: 'Complex Mother-Sibling Relationships',
            18: 'Voices and Perception of Sound',
            19: 'Difficulties and Emotional Burdens',
            20: 'Fear and Reflection on Aging',
            21: 'Emotions of Crying and Tears',
            22: 'Father-Child Relationships and Authority',
            23: 'Possibilities and Potential Outcomes',
            24: 'Inner Struggle and Helplessness',
            25: 'Pursuing Meaningful Personal Goals',
            26: 'Job Anxiety and Self-Reflection',
            27: 'Marriage Anxiety and Dependence',
            28: 'Expressions of Anger and Frustration',
            29: 'Nurturing the inner child',
            30: 'Therapy and Father Relationships',
            31: 'Expressions of Happiness and Joy',
            32: 'Revisiting the Past Together',
            33: 'Drinking Habits and Concerns',
            34: 'Managing and Increasing Energy Levels',
            35: 'Understanding Depression and Its Roots',
            36: 'Nervous System and Stress Response'}
```


## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("AIPsy/bert-base-therapist-topic-classification-eng")
model = AutoModelForSequenceClassification.from_pretrained("AIPsy/bert-base-therapist-topic-classification-eng")

text = "You know, I mean, it seems like you could just go to work and feel so much better."

encoding = tokenizer(
            text,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        )
output = model(encoding['input_ids'], encoding['attention_mask']).logits
result = np.argmax(output.detach().numpy(), axis=-1)
print(id2label[result[0]])
'Job Anxiety and Self-Reflection'
```

## Dataset

The source material was the recordings of psychotherapeutic sessions posted on YouTube in the public domain. After conducting speaker diarization and transcription of the recordings 15324 items (sentences) were obtained.

## Recommendations

Given the broad context of issues discussed in psychotherapeutic sessions, the authors believe that this model can be used to analyze human communication in general.

## Metrics

Score metrics of trained model
|Sample|F1 macro|
|:-|:-:|
|Test|0.74|
|Validation|0.77|
|Train|0.97|

F1 score metrics for test sample across categories
|ID|Topic|Precision|Recall|F1|
|:-:|:-|:-:|:-:|:-:|
| 0 | Time Up and Future Meetings |  0.81 | 0.80 | 0.80 |
| 1 | Complex Emotions Toward Him |  0.86 | 0.88 | 0.87 |
| 2 | Desires and Disappointments |  0.71 | 0.73 | 0.72 |
| 3 | Personal Growth and Decision-Making |  0.64 | 0.77 | 0.70 |
| 4 | Self-Acceptance and Relationships |  0.69 | 0.82 | 0.75 |
| 5 | Understanding and Confronting Fear |  0.93 | 0.76 | 0.84 |
| 6 | See and Understanding Conversations |  0.77 | 0.85 | 0.81 |
| 7 | Clarifying Meaning and Intent |  0.81 | 0.76 | 0.79 |
| 8 | Desire to Escape and Leave |  0.68 | 0.60 | 0.64 |
| 9 | Uncertainty and Understanding Issues |  0.81 | 0.81 | 0.81 |
| 10 | Open Conversation and Sharing |  0.79 | 0.77 | 0.78 |
| 11 | Exploring Emotional Hurt and Bitterness |  0.74 | 0.70 | 0.72 |
| 12 | Guilt and Self-Blame Dynamics |  0.80 | 0.69 | 0.74 |
| 13 | Dynamics of Meaningful Relationships |  0.75 | 0.75 | 0.75 |
| 14 | Struggles and Desires in Learning |  0.82 | 0.72 | 0.77 |
| 15 | Gender Roles and Relationships |  0.83 | 0.83 | 0.83 |
| 16 | Struggles with Personal Change |  0.76 | 0.60 | 0.67 |
| 17 | Complex Mother-Sibling Relationships |  0.60 | 0.74 | 0.67 |
| 18 | Voices and Perception of Sound |  0.74 | 0.78 | 0.76 |
| 19 | Difficulties and Emotional Burdens |  0.75 | 0.67 | 0.71 |
| 20 | Fear and Reflection on Aging |  0.62 | 0.64 | 0.63 |
| 21 | Emotions of Crying and Tears |  0.65 | 0.76 | 0.70 |
| 22 | Father-Child Relationships and Authority |  0.93 | 0.80 | 0.86 |
| 23 | Possibilities and Potential Outcomes |  0.72 | 0.64 | 0.68 |
| 24 | Inner Struggle and Helplessness |  0.68 | 0.71 | 0.69 |
| 25 | Pursuing Meaningful Personal Goals |  0.58 | 0.65 | 0.61 |
| 26 | Job Anxiety and Self-Reflection |  0.70 | 0.73 | 0.71 |
| 27 | Marriage Anxiety and Dependence |  0.82 | 0.82 | 0.82 |
| 28 | Expressions of Anger and Frustration |  0.73 | 0.76 | 0.75 |
| 29 | Nurturing the inner child |  0.74 | 0.70 | 0.72 |
| 30 | Therapy and Father Relationships |  0.80 | 0.82 | 0.81 |
| 31 | Expressions of Happiness and Joy |  0.78 | 0.79 | 0.78 |
| 32 | Revisiting the Past Together |  0.78 | 0.60 | 0.68 |
| 33 | Drinking Habits and Concerns |  0.69 | 0.79 | 0.73 |
| 34 | Managing and Increasing Energy Levels |  0.54 | 0.62 | 0.58 |
| 35 | Understanding Depression and Its Roots |  0.65 | 0.85 | 0.73 |
| 36 | Nervous System and Stress Response |  0.61 | 0.67 | 0.64 |



## Citation 

- **Papers:** Vanin A, Bolshev V and Panfilova A (2025) Psychotherapist remarks’ ML classifier: insights from LLM and topic modeling application. Front. Psychiatry 16:1608163. doi: 10.3389/fpsyt.2025.1608163. <https://doi.org/10.3389/fpsyt.2025.1608163>
- **Developed by:** @myentity, @VadZhen, @Alek123
- **License:** MIT


**BibTeX:**

```
@ARTICLE{10.3389/fpsyt.2025.1608163,   
AUTHOR={Vanin, Alexander  and Bolshev, Vadim  and Panfilova, Anastasia },          
TITLE={Psychotherapist remarks’ ML classifier: insights from LLM and topic modeling application},        
JOURNAL={Frontiers in Psychiatry},         
VOLUME={Volume 16 - 2025}, 
YEAR={2025}, 
URL={https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1608163},
DOI={10.3389/fpsyt.2025.1608163},
ISSN={1664-0640},
```