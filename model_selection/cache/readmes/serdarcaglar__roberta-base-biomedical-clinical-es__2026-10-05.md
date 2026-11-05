---
language: 
  - es
tags:
- biomedical
- clinical
- spanish
license: apache-2.0
metrics:
- ppl
widget:
- text: "Los fármacos con mecanismos de acción sobre receptores del sistema histaminérgico pueden resultar de gran <mask> en estos casos."
- text: "A pesar de esto, sus características morfológicas y funcionales permiten que la disfunción pase inadvertida por métodos <mask> convencionales, por ejemplo la espirometría."
- text: "El tratamiento es muy variado y no se ha detectado todavía aquel que garantice la <mask> total del paciente."
---

# Biomedical-clinical language model for Spanish


## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citation information](#citation-information)
  - [Disclaimer](#disclaimer)
  
</details>

## Model description
Biomedical pretrained language model for Spanish. This model is a [RoBERTa-based](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model trained on a **biomedical-clinical** corpus in Spanish collected from several sources. 

## Intended uses and limitations
The model is ready-to-use only for masked language modelling to perform the Fill Mask task (try the inference API or read the next section). However, it is intended to be fine-tuned on downstream tasks such as Named Entity Recognition or Text Classification.

## How to use

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("serdarcaglar/roberta-base-biomedical-clinical-es")
model = AutoModelForMaskedLM.from_pretrained("serdarcaglar/roberta-base-biomedical-clinical-es")
from transformers import pipeline
unmasker = pipeline('fill-mask', model="serdarcaglar/roberta-base-biomedical-clinical-es")
unmasker("El <mask> se basa en el manejo sintomático, inmunomodulador y de la enfermedad de base en los casos paraneoplásicos.")
```
```
# Output
[
  {
    "score": 0.9751564860343933,
    "token": 636,
    "token_str": " tratamiento",
    "sequence": " El tratamiento se basa en el manejo sintomático, inmunomodulador y de la enfermedad de base en los casos paraneoplásicos."
  },
  {
    "score": 0.01814817637205124,
    "token": 3289,
    "token_str": " manejo",
    "sequence": " El manejo se basa en el manejo sintomático, inmunomodulador y de la enfermedad de base en los casos paraneoplásicos."
  },
  {
    "score": 0.0013401516480371356,
    "token": 4554,
    "token_str": " pronóstico",
    "sequence": " El pronóstico se basa en el manejo sintomático, inmunomodulador y de la enfermedad de base en los casos paraneoplásicos."
  },
  {
    "score": 0.000933669216465205,
    "token": 1263,
    "token_str": " diagnóstico",
    "sequence": " El diagnóstico se basa en el manejo sintomático, inmunomodulador y de la enfermedad de base en los casos paraneoplásicos."
  },
  {
    "score": 0.00048010185128077865,
    "token": 3592,
    "token_str": " éxito",
    "sequence": " El éxito se basa en el manejo sintomático, inmunomodulador y de la enfermedad de base en los casos paraneoplásicos."
  }
]
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training
The training corpus has been tokenized using a byte version of [Byte-Pair Encoding (BPE)](https://github.com/openai/gpt-2)
used in the original [RoBERTA](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model with a vocabulary size of 52,000 tokens. The pretraining consists of a masked language model training at the subword level following the approach employed for the RoBERTa base model with the same hyperparameters as in the original work. The training lasted a total of 48 hours with 16 NVIDIA V100 GPUs of 16GB DDRAM, using Adam optimizer with a peak learning rate of 0.0005 and an effective batch size of 2,048 sentences.

The training corpus is composed of several biomedical corpora in Spanish, collected from publicly available corpora and crawlers, and a real-world clinical corpus collected from more than 278K clinical documents and notes. To obtain a high-quality training corpus while retaining the idiosyncrasies of the clinical language, a cleaning pipeline has been applied only to the biomedical corpora, keeping the clinical corpus uncleaned. Essentially, the cleaning operations used are:

  - data parsing in different formats
  - sentence splitting
  - language detection
  - filtering of ill-formed sentences 
  - deduplication of repetitive contents
  - keep the original document boundaries

Then, the biomedical corpora are concatenated and further global deduplication among the biomedical corpora have been applied.
Eventually, the clinical corpus is concatenated to the cleaned biomedical corpus resulting in a medium-size biomedical-clinical corpus for Spanish composed of more than 1B tokens. The table below shows some basic statistics of the individual cleaned corpora:






## Additional information

### Author
Serdar ÇAĞLAR
### Contact information
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