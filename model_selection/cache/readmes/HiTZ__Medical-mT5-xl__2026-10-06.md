---
license: apache-2.0
language:
- en
- es
- fr
- it
widget:
- text: The best cough medicine is <extra_id_0> because <extra_id_1>
- text: El mejor medicamento para la tos es <extra_id_0> porque <extra_id_1>
- text: Le meilleur médicament contre la toux est <extra_id_0> car <extra_id_1
- text: La migliore medicina per la tosse è la <extra_id_0> perché la <extra_id_1
library_name: transformers
pipeline_tag: text2text-generation
tags:
- medical
- multilingual
- medic
datasets:
- HiTZ/Multilingual-Medical-Corpus
base_model: google/mt5-xl
---

<p align="center">
    <br>
    <img src="http://www.ixa.eus/sites/default/files/anitdote.png" style="height: 250px;">
    <h2 align="center">Medical mT5: An Open-Source Multilingual Text-to-Text LLM
for the Medical Domain</h2>
    <br>


# Model Card for MedMT5-xl

<p align="justify">
We present Medical mT5, the first open-source text-to-text multilingual model for the medical domain. 
  Medical mT5 is an encoder-decoder model developed by continuing the training of publicly available mT5 checkpoints on 
  medical domain data for English, Spanish, French, and Italian.
</p>

  - 📖 Paper: [Medical mT5: An Open-Source Multilingual Text-to-Text LLM for The Medical Domain](https://arxiv.org/abs/2404.07613)
  - 🌐 Project Website: [https://univ-cotedazur.eu/antidote](https://univ-cotedazur.eu/antidote)


<table border="1" cellspacing="0" cellpadding="5">
    <caption>Pre-Training settings for MedMT5.</caption>
    <thead>
        <tr>
            <th></th>
            <th>Medical mT5-Large (<a href="https://huggingface.co/HiTZ/Medical-mT5-large">HiTZ/Medical-mT5-large</a>)</th>
            <th>Medical mT5-XL (<a href="https://huggingface.co/HiTZ/Medical-mT5-xl">HiTZ/Medical-mT5-xl</a>)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Param. no.</td>
            <td>738M</td>
            <td>3B</td>
        </tr>
        <tr>
            <td>Sequence Length</td>
            <td>1024</td>
            <td>480</td>
        </tr>
        <tr>
            <td>Token/step</td>
            <td>65536</td>
            <td>30720</td>
        </tr>
        <tr>
            <td>Epochs</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Total Tokens</td>
            <td>4.5B</td>
            <td>4.5B</td>
        </tr>
        <tr>
            <td>Optimizer</td>
            <td>Adafactor</td>
            <td>Adafactor</td>
        </tr>
        <tr>
            <td>LR</td>
            <td>0.001</td>
            <td>0.001</td>
        </tr>
        <tr>
            <td>Scheduler</td>
            <td>Constant</td>
            <td>Constant</td>
        </tr>
        <tr>
            <td>Hardware</td>
            <td>4xA100</td>
            <td>4xA100</td>
        </tr>
        <tr>
            <td>Time (h)</td>
            <td>10.5</td>
            <td>20.5</td>
        </tr>
        <tr>
            <td>CO<sub>2</sub>eq (kg)</td>
            <td>2.9</td>
            <td>5.6</td>
        </tr>
    </tbody>
</table>


# Model Description

- **Developed by**: Iker García-Ferrero, Rodrigo Agerri, Aitziber Atutxa Salazar, Elena Cabrio, Iker de la Iglesia, Alberto Lavelli, Bernardo Magnini, Benjamin Molinet, Johana Ramirez-Romero, German Rigau, Jose Maria Villa-Gonzalez, Serena Villata and Andrea Zaninello
- **Contact**: [Iker García-Ferrero](https://ikergarcia1996.github.io/Iker-Garcia-Ferrero/) and [Rodrigo Agerri](https://ragerri.github.io/)
- **Website**: [https://univ-cotedazur.eu/antidote](https://univ-cotedazur.eu/antidote)
- **Funding**: CHIST-ERA XAI 2019 call. Antidote (PCI2020-120717-2) funded by MCIN/AEI /10.13039/501100011033 and by European Union NextGenerationEU/PRTR
- **Model type**: text2text-generation
- **Language(s) (NLP)**: English, Spanish, French, Italian
- **License**: apache-2.0
- **Finetuned from model**: mT5

## How to Get Started with the Model

You can load the model using

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("HiTZ/Medical-mT5-xl")
model = AutoModelForSeq2SeqLM.from_pretrained("HiTZ/Medical-mT5-xl")
```

The model has been trained using the T5 masked language modelling tasks. You need to finetune the model for your task. 

<p align="center">
    <br>
    <img src="https://miro.medium.com/v2/0*yeXSc6Qs-SGKDzZP.png" style="height: 250px;">
    <br>





## Training Data


<table border="1" cellspacing="0" cellpadding="5">
    <caption>Data sources and word counts by language.</caption>
    <thead>
        <tr>
            <th>Language</th>
            <th>Source</th>
            <th>Words</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="3">English</td>
            <td>ClinicalTrials</td>
            <td>127.4M</td>
        </tr>
        <tr>
            <td>EMEA</td>
            <td>12M</td>
        </tr>
        <tr>
            <td>PubMed</td>
            <td>968.4M</td>
        </tr>
        <tr>
            <td rowspan="6">Spanish</td>
            <td>EMEA</td>
            <td>13.6M</td>
        </tr>
        <tr>
            <td>PubMed</td>
            <td>8.4M</td>
        </tr>
        <tr>
            <td>Medical Crawler</td>
            <td>918M</td>
        </tr>
        <tr>
            <td>SPACC</td>
            <td>350K</td>
        </tr>
        <tr>
            <td>UFAL</td>
            <td>10.5M</td>
        </tr>
        <tr>
            <td>WikiMed</td>
            <td>5.2M</td>
        </tr>
        <tr>
            <td rowspan="5">French</td>
            <td>PubMed</td>
            <td>1.4M</td>
        </tr>
        <tr>
            <td>Science Direct</td>
            <td>15.2M</td>
        </tr>
        <tr>
            <td>Wikipedia - Médecine</td>
            <td>5M</td>
        </tr>
        <tr>
            <td>EDP</td>
            <td>48K</td>
        </tr>
        <tr>
            <td>Google Patents</td>
            <td>654M</td>
        </tr>
        <tr>
            <td rowspan="13">Italian</td>
            <td>Medical Commoncrawl - IT</td>
            <td>67M</td>
        </tr>
        <tr>
            <td>Drug instructions</td>
            <td>30.5M</td>
        </tr>
        <tr>
            <td>Wikipedia - Medicina</td>
            <td>13.3M</td>
        </tr>
        <tr>
            <td>E3C Corpus - IT</td>
            <td>11.6M</td>
        </tr>
        <tr>
            <td>Medicine descriptions</td>
            <td>6.3M</td>
        </tr>
        <tr>
            <td>Medical theses</td>
            <td>5.8M</td>
        </tr>
        <tr>
            <td>Medical websites</td>
            <td>4M</td>
        </tr>
        <tr>
            <td>PubMed</td>
            <td>2.3M</td>
        </tr>
        <tr>
            <td>Supplement description</td>
            <td>1.3M</td>
        </tr>
        <tr>
            <td>Medical notes</td>
            <td>975K</td>
        </tr>
        <tr>
            <td>Pathologies</td>
            <td>157K</td>
        </tr>
        <tr>
            <td>Medical test simulations</td>
            <td>26K</td>
        </tr>
        <tr>
            <td>Clinical cases</td>
            <td>20K</td>
        </tr>
    </tbody>
</table>

## Evaluation

### Medical mT5 for Sequence Labelling

We have released two Medical mT5 models finetuned for multilingual sequence labelling. 
<table border="1" cellspacing="0" cellpadding="5">
    <thead>
        <tr>
            <th></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-mT5-large">HiTZ/Medical-mT5-large</a></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-mT5-xl">HiTZ/Medical-mT5-xl</a></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-mT5-large-multitask">HiTZ/Medical-mT5-large-multitask</a></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-mT5-xl-multitask">HiTZ/Medical-mT5-xl-multitask</a></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Param. no.</td>
            <td>738M</td>
            <td>3B</td>
            <td>738M</td>
            <td>3B</td>
        </tr>
        <tr>
            <td>Task</td>
            <td>Language Modeling</td>
            <td>Language Modeling</td>
            <td>Multitask Sequence Labeling</td>
            <td>Multitask Sequence Labeling</td>
        </tr>
        <tr>
    </tbody>
</table>




### Single-task supervised F1 scores for Sequence Labelling
<p align="center">
    <br>
    <img src="https://huggingface.co/HiTZ/Medical-mT5-large/resolve/main/single.png" style="height: 600px;">
    <br>
  
### Multi-task supervised F1 scores for Sequence Labelling
<p align="center">
    <br>
    <img src="https://huggingface.co/HiTZ/Medical-mT5-large/resolve/main/multi.png" style="height: 600px;">
    <br>
  
### Zero-shot F1 scores for Argument Mining. Models have been trained in English and evaluated in Spanish, French and Italian.
<p align="center">
    <br>
    <img src="https://huggingface.co/HiTZ/Medical-mT5-large/resolve/main/cross.png" style="height: 320px;">
    <br>

  
## Ethical Statement
<p align="justify">
Our research in developing Medical mT5, a multilingual text-to-text model for the medical domain, has ethical implications that we acknowledge. 
  Firstly, the broader impact of this work lies in its potential to improve medical communication and understanding across languages, which 
  can enhance healthcare access and quality for diverse linguistic communities. However, it also raises ethical considerations related to privacy and data security.
  To create our multilingual corpus, we have taken measures to anonymize and protect sensitive patient information, adhering to 
  data protection regulations in each language's jurisdiction or deriving our data from sources that explicitly address this issue in line with 
  privacy and safety regulations and guidelines. Furthermore, we are committed to transparency and fairness in our model's development and evaluation. 
  We have worked to ensure that our benchmarks are representative and unbiased, and we will continue to monitor and address any potential biases in the future. 
  Finally, we emphasize our commitment to open source by making our data, code, and models publicly available, with the aim of promoting collaboration within 
  the research community.
</p>

## Citation

```bibtext
@misc{garcíaferrero2024medical,
      title={Medical mT5: An Open-Source Multilingual Text-to-Text LLM for The Medical Domain}, 
      author={Iker García-Ferrero and Rodrigo Agerri and Aitziber Atutxa Salazar and Elena Cabrio and Iker de la Iglesia and Alberto Lavelli and Bernardo Magnini and Benjamin Molinet and Johana Ramirez-Romero and German Rigau and Jose Maria Villa-Gonzalez and Serena Villata and Andrea Zaninello},
      year={2024},
      eprint={2404.07613},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```