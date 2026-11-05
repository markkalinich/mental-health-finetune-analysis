---
license: mit
tags:
- sentiment-analysis
- text-classification
- electra
- pytorch
- transformers
---

# ELECTRA Base Classifier for Sentiment Analysis

This is an [ELECTRA base discriminator](https://huggingface.co/google/electra-base-discriminator) fine-tuned for sentiment analysis of reviews. It has a mean pooling layer and a classifier head (2 layers of 1024 dimension) with SwishGLU activation and dropout (0.3). It classifies text into three sentiment categories: 'negative' (0), 'neutral' (1), and 'positive' (2). It was fine-tuned on the [Sentiment Merged](https://huggingface.co/datasets/jbeno/sentiment_merged) dataset, which is a merge of Stanford Sentiment Treebank (SST-3), and DynaSent Rounds 1 and 2.


## Labels

The model predicts the following labels:

- `0`: negative
- `1`: neutral
- `2`: positive

## How to Use

### Install package

This model requires the classes in `electra_classifier.py`. You can download the file, or you can install the package from PyPI.

```bash
pip install electra-classifier
```

### Load classes and model
```python
# Install the package in a notebook
import sys
!{sys.executable} -m pip install electra-classifier

# Import libraries
import torch
from transformers import AutoTokenizer
from electra_classifier import ElectraClassifier

# Load tokenizer and model
model_name = "jbeno/electra-base-classifier-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = ElectraClassifier.from_pretrained(model_name)

# Set model to evaluation mode
model.eval()

# Run inference
text = "I love this restaurant!"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs)
    predicted_class_id = torch.argmax(logits, dim=1).item()
    predicted_label = model.config.id2label[predicted_class_id]
    print(f"Predicted label: {predicted_label}")
```

## Requirements
- Python 3.7+
- PyTorch
- Transformers
- [electra-classifier](https://pypi.org/project/electra-classifier/) - Install with pip, or download electra_classifier.py

## Training Details

### Dataset

The model was trained on the [Sentiment Merged](https://huggingface.co/datasets/jbeno/sentiment_merged) dataset, which is a mix of Stanford Sentiment Treebank (SST-3), DynaSent Round 1, and DynaSent Round 2.

### Code

The code used to train the model can be found on GitHub:
- [jbeno/sentiment](https://github.com/jbeno/sentiment)
- [jbeno/electra-classifier](https://github.com/jbeno/electra-classifier)

### Research Paper

The research paper can be found here: [ELECTRA and GPT-4o: Cost-Effective Partners for Sentiment Analysis](http://arxiv.org/abs/2501.00062) (arXiv:2501.00062)
 
### Performance Summary

- **Merged Dataset**
    - Macro Average F1: **79.29**
    - Accuracy: **79.69**
- **DynaSent R1**
    - Macro Average F1: **82.10**
    - Accuracy: **82.14**
- **DynaSent R2**
    - Macro Average F1: **71.83**
    - Accuracy: **71.94**
- **SST-3**
    - Macro Average F1: **69.95**
    - Accuracy: **78.24**

## Model Architecture

- **Base Model**: ELECTRA base discriminator (`google/electra-base-discriminator`)
- **Pooling Layer**: Custom pooling layer supporting 'cls', 'mean', and 'max' pooling types.
- **Classifier**: Custom classifier with configurable hidden dimensions, number of layers, and dropout rate.
    - **Activation Function**: Custom SwishGLU activation function.

```
ElectraClassifier(
  (electra): ElectraModel(
    (embeddings): ElectraEmbeddings(
      (word_embeddings): Embedding(30522, 768, padding_idx=0)
      (position_embeddings): Embedding(512, 768)
      (token_type_embeddings): Embedding(2, 768)
      (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
      (dropout): Dropout(p=0.1, inplace=False)
    )
    (encoder): ElectraEncoder(
      (layer): ModuleList(
        (0-11): 12 x ElectraLayer(
          (attention): ElectraAttention(
            (self): ElectraSelfAttention(
              (query): Linear(in_features=768, out_features=768, bias=True)
              (key): Linear(in_features=768, out_features=768, bias=True)
              (value): Linear(in_features=768, out_features=768, bias=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
            (output): ElectraSelfOutput(
              (dense): Linear(in_features=768, out_features=768, bias=True)
              (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
          )
          (intermediate): ElectraIntermediate(
            (dense): Linear(in_features=768, out_features=3072, bias=True)
            (intermediate_act_fn): GELUActivation()
          )
          (output): ElectraOutput(
            (dense): Linear(in_features=3072, out_features=768, bias=True)
            (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            (dropout): Dropout(p=0.1, inplace=False)
          )
        )
      )
    )
  )
  (pooling): PoolingLayer()
  (classifier): Classifier(
    (layers): Sequential(
      (0): Linear(in_features=768, out_features=1024, bias=True)
      (1): SwishGLU(
        (projection): Linear(in_features=1024, out_features=2048, bias=True)
        (activation): SiLU()
      )
      (2): Dropout(p=0.3, inplace=False)
      (3): Linear(in_features=1024, out_features=1024, bias=True)
      (4): SwishGLU(
        (projection): Linear(in_features=1024, out_features=2048, bias=True)
        (activation): SiLU()
      )
      (5): Dropout(p=0.3, inplace=False)
      (6): Linear(in_features=1024, out_features=3, bias=True)
    )
  )
)
```


## Custom Model Components

### SwishGLU Activation Function

The SwishGLU activation function combines the Swish activation with a Gated Linear Unit (GLU). It enhances the model's ability to capture complex patterns in the data.

```python
class SwishGLU(nn.Module):
    def __init__(self, input_dim: int, output_dim: int):
        super(SwishGLU, self).__init__()
        self.projection = nn.Linear(input_dim, 2 * output_dim)
        self.activation = nn.SiLU()

    def forward(self, x):
        x_proj_gate = self.projection(x)
        projected, gate = x_proj_gate.tensor_split(2, dim=-1)
        return projected * self.activation(gate)
```

### PoolingLayer

The PoolingLayer class allows you to choose between different pooling strategies:

- `cls`: Uses the representation of the \[CLS\] token.
- `mean`: Calculates the mean of the token embeddings.
- `max`: Takes the maximum value across token embeddings.

**'mean'** pooling was used in the fine-tuned model.

```python
class PoolingLayer(nn.Module):
    def __init__(self, pooling_type='cls'):
        super().__init__()
        self.pooling_type = pooling_type

    def forward(self, last_hidden_state, attention_mask):
        if self.pooling_type == 'cls':
            return last_hidden_state[:, 0, :]
        elif self.pooling_type == 'mean':
            return (last_hidden_state * attention_mask.unsqueeze(-1)).sum(1) / attention_mask.sum(-1).unsqueeze(-1)
        elif self.pooling_type == 'max':
            return torch.max(last_hidden_state * attention_mask.unsqueeze(-1), dim=1)[0]
        else:
            raise ValueError(f"Unknown pooling method: {self.pooling_type}")
```

### Classifier

The Classifier class is a customizable feed-forward neural network used for the final classification.

The fine-tuned model had:

- `input_dim`: 768
- `num_layers`: 2
- `hidden_dim`: 1024
- `hidden_activation`: SwishGLU
- `dropout_rate`: 0.3
- `n_classes`: 3

```python
class Classifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, hidden_activation, num_layers, n_classes, dropout_rate=0.0):
        super().__init__()
        layers = []
        layers.append(nn.Linear(input_dim, hidden_dim))
        layers.append(hidden_activation)
        if dropout_rate > 0:
            layers.append(nn.Dropout(dropout_rate))

        for _ in range(num_layers - 1):
            layers.append(nn.Linear(hidden_dim, hidden_dim))
            layers.append(hidden_activation)
            if dropout_rate > 0:
                layers.append(nn.Dropout(dropout_rate))

        layers.append(nn.Linear(hidden_dim, n_classes))
        self.layers = nn.Sequential(*layers)
```

## Model Configuration

The model's configuration (config.json) includes custom parameters:

- `hidden_dim`: Size of the hidden layers in the classifier.
- `hidden_activation`: Activation function used in the classifier ('SwishGLU').
- `num_layers`: Number of layers in the classifier.
- `dropout_rate`: Dropout rate used in the classifier.
- `pooling`: Pooling strategy used ('mean').

## Performance by Dataset

### Merged Dataset

```
Merged Dataset Classification Report

              precision    recall  f1-score   support

    negative   0.847081  0.777211  0.810643      2352
     neutral   0.704453  0.761072  0.731669      1829
    positive   0.828047  0.844615  0.836249      2349

    accuracy                       0.796937      6530
   macro avg   0.793194  0.794299  0.792854      6530
weighted avg   0.800285  0.796937  0.797734      6530

ROC AUC: 0.926344

Predicted  negative  neutral  positive
Actual                                
negative       1828      331       193
neutral         218     1392       219
positive        112      253      1984

Macro F1 Score: 0.79
```

### DynaSent Round 1

```
DynaSent Round 1 Classification Report

              precision    recall  f1-score   support

    negative   0.901222  0.737500  0.811182      1200
     neutral   0.745957  0.922500  0.824888      1200
    positive   0.850970  0.804167  0.826907      1200

    accuracy                       0.821389      3600
   macro avg   0.832716  0.821389  0.820992      3600
weighted avg   0.832716  0.821389  0.820992      3600

ROC AUC: 0.945131

Predicted  negative  neutral  positive
Actual                                
negative        885      201       114
neutral          38     1107        55
positive         59      176       965

Macro F1 Score: 0.82
```

### DynaSent Round 2

```
DynaSent Round 2 Classification Report

              precision    recall  f1-score   support

    negative   0.696154  0.754167  0.724000       240
     neutral   0.770408  0.629167  0.692661       240
    positive   0.704545  0.775000  0.738095       240

    accuracy                       0.719444       720
   macro avg   0.723702  0.719444  0.718252       720
weighted avg   0.723702  0.719444  0.718252       720

ROC AUC: 0.88842

Predicted  negative  neutral  positive
Actual                                
negative        181       26        33
neutral          44      151        45
positive         35       19       186

Macro F1 Score: 0.72
```

### Stanford Sentiment Treebank (SST-3)

```
SST-3 Classification Report

              precision    recall  f1-score   support

    negative   0.831878  0.835526  0.833698       912
     neutral   0.452703  0.344473  0.391241       389
    positive   0.834669  0.916392  0.873623       909

    accuracy                       0.782353      2210
   macro avg   0.706417  0.698797  0.699521      2210
weighted avg   0.766284  0.782353  0.772239      2210

ROC AUC: 0.885009

Predicted  negative  neutral  positive
Actual                                
negative        762      104        46
neutral         136      134       119
positive         18       58       833

Macro F1 Score: 0.70
```

## License

This model is licensed under the MIT License.

## Citation

If you use this model in your work, please cite:

```bibtex
@article{beno-2024-electragpt,
      title={ELECTRA and GPT-4o: Cost-Effective Partners for Sentiment Analysis}, 
      author={James P. Beno},
      journal={arXiv preprint arXiv:2501.00062},
      year={2024},
      eprint={2501.00062},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.00062}, 
}
```

## Contact

For questions or comments, please open an issue on the repository or contact [Jim Beno](https://huggingface.co/jbeno).

## Acknowledgments

- The [Hugging Face Transformers library](https://github.com/huggingface/transformers) for providing powerful tools for model development.
- The creators of the [ELECTRA model](https://arxiv.org/abs/2003.10555) for their foundational work.
- The authors of the datasets used: [Stanford Sentiment Treebank](https://huggingface.co/datasets/stanfordnlp/sst), [DynaSent](https://huggingface.co/datasets/dynabench/dynasent).
- [Stanford Engineering CGOE](https://cgoe.stanford.edu), [Chris Potts](https://stanford.edu/~cgpotts/), and the Course Facilitators of [XCS224U](https://online.stanford.edu/courses/xcs224u-natural-language-understanding)

