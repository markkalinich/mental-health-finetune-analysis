---
language:
- es
- en
- fr
license: apache-2.0
library_name: transformers
tags:
- medical
- multilingual
- medic
base_model: HiTZ/Medical-mT5-xl
datasets:
- HiTZ/Multilingual-Medical-Corpus
- HiTZ/multilingual-abstrct
widget:
- text: <Disease> Torsade de pointes ventricular tachycardia during low dose intermittent
    dobutamine treatment in a patient with dilated cardiomyopathy and congestive heart
    failure .
- text: '<ClinicalEntity> Ecográficamente se observan tres nódulos tumorales independientes
    y bien delimitados : dos de ellos heterogéneos , sólidos , de 20 y 33 mm de diámetros
    , con áreas quísticas y calcificaciones .'
- text: <ClinicalEntity> On notait une hyperlordose lombaire avec une contracture
    permanente des muscles paravertébraux , de l abdomen et des deux membres inférieurs
    .
- text: <ClinicalEntity> Nell ’ anamnesi patologica era riferita ipertensione arteriosa
    controllata con terapia medica
pipeline_tag: text2text-generation
---

<p align="center">
    <br>
    <img src="http://www.ixa.eus/sites/default/files/anitdote.png" style="width: 45%;">
    <h2 align="center">Medical mT5: An Open-Source Multilingual Text-to-Text LLM
for the Medical Domain</h2>
    <be>

# Model Card for Medical MT5-xl-multitask


<p align="justify">

Medical MT5-xl-multitask is a version of Medical MT5 finetuned for sequence labelling. It can correctly label a wide range of Medical labels in unstructured text, such as `Disease`, `Disability`, `ClinicalEntity`, `Chemical`...  Medical MT5-xl-multitask has been finetuned for English, Spanish, French and Italian, although it may work with a wide range of languages.   

  - 📖 Paper: [Medical mT5: An Open-Source Multilingual Text-to-Text LLM for The Medical Domain](https://arxiv.org/abs/2404.07613)
  - 🌐 Project Website: [https://univ-cotedazur.eu/antidote](https://univ-cotedazur.eu/antidote)


<p align="center">
    <br>
    <img src="https://raw.githubusercontent.com/ikergarcia1996/Sequence-Labeling-LLMs/main/resources/MedT5-Ner-mtask.png" style="width: 60%;">
    <be>

# Open Source Models
<table border="1" cellspacing="0" cellpadding="5">
    <thead>
        <tr>
            <th></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-mT5-large">HiTZ/Medical-mT5-large</a></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-MT5-xl">HiTZ/Medical-MT5-xl</a></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-mT5-large-multitask">HiTZ/Medical-mT5-large-multitask</a></th>
            <th><a href="https://huggingface.co/HiTZ/Medical-MT5-xl-multitask">HiTZ/Medical-MT5-xl-multitask</a></th>
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


# Usage

Medical MT5-xl-multitask was training using the *Sequence-Labeling-LLMs* library: https://github.com/ikergarcia1996/Sequence-Labeling-LLMs/   
This library uses constrained decoding to ensure that the output contains the same words as the input and a valid HTML annotation. We recommend using Medical MT5-xl-multitask together with this library. 
Although you can also directly use it with  🤗 huggingface. In order to label a sentence, you need to append the labels you wan to use, for example, if you want to label *dieseases* you should format your input as follows: `<Disease> Torsade de pointes ventricular tachycardia during low dose intermittent dobutamine treatment in a patient with dilated cardiomyopathy and congestive heart failure .`

```python
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("Medical-MT5-xl-multitask",torch_dtype=torch.bfloat16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("Medical-MT5-xl-multitask")

input_example = "<Disease> Torsade de pointes ventricular tachycardia during low dose intermittent dobutamine treatment in a patient with dilated cardiomyopathy and congestive heart failure ."

model_input = tokenizer(input_example, return_tensors="pt")

output = model.generate(**model_input.to(model.device),max_new_tokens=128,num_beams=1,num_return_sequences=1,do_sample=False)

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

# Performance
<img src="https://raw.githubusercontent.com/ikergarcia1996/Sequence-Labeling-LLMs/main/resources/multitask_performance.png" style="width: 70%;">

# Model Description

- **Developed by**: Iker García-Ferrero, Rodrigo Agerri, Aitziber Atutxa Salazar, Elena Cabrio, Iker de la Iglesia, Alberto Lavelli, Bernardo Magnini, Benjamin Molinet, Johana Ramirez-Romero, German Rigau, Jose Maria Villa-Gonzalez, Serena Villata and Andrea Zaninello
- **Contact**: [Iker García-Ferrero](https://ikergarcia1996.github.io/Iker-Garcia-Ferrero/) and [Rodrigo Agerri](https://ragerri.github.io/)
- **Website**: [https://univ-cotedazur.eu/antidote](https://univ-cotedazur.eu/antidote)
- **Funding**: CHIST-ERA XAI 2019 call. Antidote (PCI2020-120717-2) funded by MCIN/AEI /10.13039/501100011033 and by European Union NextGenerationEU/PRTR
- **Model type**: text2text-generation
- **Language(s) (NLP)**: English, Spanish, French, Italian
- **License**: apache-2.0
- **Finetuned from model**: HiTZ/Medical-MT5-xl


# Ethical Statement
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

# Citation

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