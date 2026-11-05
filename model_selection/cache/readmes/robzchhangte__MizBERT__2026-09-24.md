---
license: apache-2.0
pipeline_tag: fill-mask
---
**MizBERT: A Masked Language Model for Mizo Text Understanding**

**Demo Application: https://huggingface.co/spaces/robzchhangte/Mizo-MLM**

**Overview**

MizBERT is a masked language model (MLM) pre-trained on a corpus of Mizo text data. It is based on the BERT (Bidirectional Encoder Representations from Transformers) architecture and leverages the MLM objective to effectively learn contextual representations of words in the Mizo language.

**Key Features**

- **Mizo-Specific:** MizBERT is specifically tailored to the Mizo language, capturing its unique linguistic nuances and vocabulary.
- **MLM Objective:** The MLM objective trains MizBERT to predict masked words based on the surrounding context, fostering a deep understanding of Mizo semantics.
- **Contextual Embeddings:** MizBERT generates contextualized word embeddings that encode the meaning of a word in relation to its surrounding text.
- **Transfer Learning:** MizBERT's pre-trained weights can be fine-tuned for various downstream tasks in Mizo NLP, such as text classification, question answering, and sentiment analysis.

**Potential Applications**

- **Mizo NLP Research:** MizBERT can serve as a valuable foundation for further research in Mizo natural language processing.
- **Mizo Machine Translation:** Fine-tuned MizBERT models can be used to develop robust machine translation systems for Mizo and other languages.
- **Mizo Text Classification:** MizBERT can be adapted for tasks like sentiment analysis, topic modeling, and spam detection in Mizo text.
- **Mizo Question Answering:** Fine-tuned MizBERT models can power question answering systems that can effectively answer questions posed in Mizo.
- **Mizo Chatbots:** MizBERT can be integrated into chatbots to enable them to communicate and understand Mizo more effectively.

**Getting Started**

To use MizBERT in your Mizo NLP projects, you can install it from the Hugging Face Transformers library:

```python
pip install transformers
```

Then, import and use MizBERT like other pre-trained models in the library:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("robzchhangte/mizbert")
model = AutoModelForMaskedLM.from_pretrained("robzchhangte/mizbert")
```

**To Predict Mask Token**
```python
from transformers import pipeline

fill_mask = pipeline("fill-mask", model="robzchhangte/mizbert")

sentence = "Miten kan thiltih [MASK] min teh thin" ##Expected token "atangin". In English: A tree is known by its fruit.
predictions = fill_mask(sentence)

for prediction in predictions:
    print(prediction["sequence"].replace("[CLS]", "").replace("[SEP]", "").strip(), "| Score:", prediction["score"])

```

**If you used this model please cite us as:**

```
@article{lalramhluna2024mizbert,
  title={MizBERT: A Mizo BERT Model},
  author={Lalramhluna, Robert and Dash, Sandeep and Pakray, Dr Partha},
  journal={ACM Transactions on Asian and Low-Resource Language Information Processing},
  year={2024},
  publisher={ACM New York, NY}
}
```