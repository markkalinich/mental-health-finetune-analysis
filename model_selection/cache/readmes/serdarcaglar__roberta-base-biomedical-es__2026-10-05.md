---
language:
- es
---
language: 
  - es
tags:
- biomedical
- spanish

metrics:
- ppl

# Biomedical language model for Spanish

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Tokenization and model pretraining](#Tokenization-pretraining)
  - [Training corpora and preprocessing](#training-corpora-preprocessing)
- [Evaluation](#evaluation)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Disclaimer](#disclaimer)
  
</details>

## Model description
Biomedical pretrained language model for Spanish. 

## Intended uses and limitations
The model is ready-to-use only for masked language modelling to perform the Fill Mask task (try the inference API or read the next section). However, it is intended to be fine-tuned on downstream tasks such as Named Entity Recognition or Text Classification.


## How to use

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("serdarcaglar/roberta-base-biomedical-es")
model = AutoModelForMaskedLM.from_pretrained("serdarcaglar/roberta-base-biomedical-es")
from transformers import pipeline
unmasker = pipeline('fill-mask', model="serdarcaglar/roberta-base-biomedical-es")
unmasker("El único antecedente personal a reseñar era la <mask> arterial.")
```
```

```

## Training

### Tokenization and model pretraining

This model is a [RoBERTa-based](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model trained on a
**biomedical** corpus in Spanish collected from several sources 
- medprocner
- codiesp
- emea
- wmt19
- wmt16
- wmt22
- scielo
- ibecs
- elrc datsets

The training corpus has been tokenized using a byte version of [Byte-Pair Encoding (BPE)](https://github.com/openai/gpt-2)
used in the original [RoBERTA](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model with a vocabulary size of 52,000 tokens. The pretraining consists of a masked language model training at the subword level following the approach employed for the RoBERTa base model with the same hyperparameters as in the original work. 


### Training corpora and preprocessing

The training corpus is composed of several biomedical corpora in Spanish, collected from publicly available corpora and crawlers.
To obtain a high-quality training corpus, a cleaning pipeline with the following operations has been applied:

- data parsing in different formats
  - sentence splitting
  - language detection
  - filtering of ill-formed sentences 
  - deduplication of repetitive contents
  - keep the original document boundaries

Finally, the corpora are concatenated and further global deduplication among the corpora have been applied.

  


## Evaluation
The model has been evaluated on the Named Entity Recognition (NER) using the following datasets:
Perplexity: 3.09

Please share the results you get in the NER task using this model. I can add them here. 
 


## Additional information

### Author
Serdar ÇAĞLAR
### Contact information

Linkedin: <https://www.linkedin.com/in/serdarildercaglar/>


For further information, send an email to <serdarildercaglar@gmail.com>



### Licensing information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)




### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner of the models be liable for any results arising from the use made by third parties of these models.


Bu havuzda yayınlanan modeller genel bir amaca yöneliktir ve üçüncü tarafların kullanımına açıktır. Bu modellerde önyargı ve diğer istenmeyen çarpıklıklar olabilir.

Üçüncü taraflar, bu modellerden herhangi birini kullanarak (veya bu modellere dayalı sistemleri kullanarak) diğer taraflara sistem ve/veya hizmet sağladıklarında veya modellerin kullanıcısı olduklarında, bunların kullanımından kaynaklanan riskleri azaltmanın ve her durumda Yapay Zeka kullanımına ilişkin düzenlemeler de dahil olmak üzere geçerli düzenlemelere uymanın kendi sorumluluklarında olduğunu unutmamalıdırlar.

Modellerin sahibi hiçbir durumda bu modellerin üçüncü şahıslar tarafından kullanımından kaynaklanan sonuçlardan sorumlu tutulamaz.

Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y otras distorsiones indeseables.

Cuando terceras partes, desplieguen o proporcionen sistemas y/o servicios a otras partes utilizando cualquiera de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluida la normativa relativa al uso de Inteligencia Artificial.

En ningún caso el propietario de los modelos será responsable de los resultados derivados del uso que terceros hagan de los mismos.

</details>