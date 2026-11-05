---
license: apache-2.0
base_model:
- distilbert/distilbert-base-uncased
language:
- en
library_name: transformers
---


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64fb80c8bb362cbf2ff96c7e/9629iVgNVpXpIXw7cW7_h.png)

## Introduction

**Albert Moderation 001** is a fine-tuned version of the [distilbert/distilbert-base-uncased](distilbert/distilbert-base-uncased) a distilled version of BERT, smaller and faster. 

Developed by **Oxygen (oxyapi)**, with contributions from **TornadoSoftwares**, Albert Moderation 001 allows you to moderate text content very quickly and efficiently across multiple categories

## Model Details

- **Model Name**: Albert Moderation 001
- **Model ID**: [oxyapi/albert-moderation-001](https://huggingface.co/oxyapi/albert-moderation-001)
- **Base Model**: [distilbert/distilbert-base-uncased](distilbert/distilbert-base-uncased)
- **Model Type**: Text classification, Moderation
- **License**: Apache-2.0
- **Language**: English 

### Features

- **Categories**: This model classifies text data into 11 different categories: harassment, harassment/threat, sexual, hate, hate/threat, self-harm/intent, self-harm/instructions, self-harm, sexual/minors, violence, violence/graphic
- **Efficient**: Compact model size allows for faster inference and reduced computational resources.
 

### Metadata

- **Owned by**: Oxygen (oxyapi)
- **Contributors**: TornadoSoftwares
- **Description**: A fast and lightweight moderation model based on BERT

## Usage

To utilize Albert Moderation 001 for text classification, you can load the model using the Hugging Face Transformers library:

```python
from transformers import pipeline
text = "Hey little shit, GIVE ME YOUR SNACK !"
classifier = pipeline("text-classification", model="oxyapi/albert-moderation-001", tokenizer="oxyapi/albert-moderation-001")
result = classifier(text,top_k=len(classifier.model.config.id2label))
print(result)

```

## License

This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

## Citation

If you find Albert Moderation 001 useful in your research or applications, please cite it as:

```
@misc{albertmoderation0012025,
  title={Albert Moderation 001: A fast and lightweight moderation model based on BERT},
  author={Oxygen (oxyapi)},
  year={2024},
  howpublished={\url{https://huggingface.co/oxyapi/albert-moderation-001}},
}
```