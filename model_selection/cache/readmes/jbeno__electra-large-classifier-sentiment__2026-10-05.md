---
license: mit
tags:
- sentiment-analysis
- text-classification
- electra
- pytorch
- transformers
---

# ELECTRA Large Classifier for Sentiment Analysis

This is an [ELECTRA large discriminator](https://huggingface.co/google/electra-large-discriminator) fine-tuned for sentiment analysis of reviews. It has a mean pooling layer and a classifier head (2 layers of 1024 dimension) with SwishGLU activation and dropout (0.3). It classifies text into three sentiment categories: 'negative' (0), 'neutral' (1), and 'positive' (2). It was fine-tuned on the [Sentiment Merged](https://huggingface.co/datasets/jbeno/sentiment_merged) dataset, which is a merge of Stanford Sentiment Treebank (SST-3), and DynaSent Rounds 1 and 2.

## Updates

- **2025-Mar-25**: Uploaded a better performing model fine-tuned with a different random seed (123 vs. 42) and from an earlier training checkpoint (epoch 10 vs. 13).

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
model_name = "jbeno/electra-large-classifier-sentiment"
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
    - Macro Average F1: **83.16** (was 82.36)
    - Accuracy: **83.71** (was 82.96)
- **DynaSent R1**
    - Macro Average F1: **86.53** (was 85.91)
    - Accuracy: **86.44** (was 85.83)
- **DynaSent R2**
    - Macro Average F1: **78.36** (was 76.29)
    - Accuracy: **78.61** (was 76.53)
- **SST-3**
    - Macro Average F1: **72.63** (was 70.90)
    - Accuracy: **80.91** (was 80.36)

## Model Architecture

- **Base Model**: ELECTRA large discriminator (`google/electra-large-discriminator`)
- **Pooling Layer**: Custom pooling layer supporting 'cls', 'mean', and 'max' pooling types.
- **Classifier**: Custom classifier with configurable hidden dimensions, number of layers, and dropout rate.
    - **Activation Function**: Custom SwishGLU activation function.

```
ElectraClassifier(
  (electra): ElectraModel(
    (embeddings): ElectraEmbeddings(
      (word_embeddings): Embedding(30522, 1024, padding_idx=0)
      (position_embeddings): Embedding(512, 1024)
      (token_type_embeddings): Embedding(2, 1024)
      (LayerNorm): LayerNorm((1024,), eps=1e-12, elementwise_affine=True)
      (dropout): Dropout(p=0.1, inplace=False)
    )
    (encoder): ElectraEncoder(
      (layer): ModuleList(
        (0-23): 24 x ElectraLayer(
          (attention): ElectraAttention(
            (self): ElectraSelfAttention(
              (query): Linear(in_features=1024, out_features=1024, bias=True)
              (key): Linear(in_features=1024, out_features=1024, bias=True)
              (value): Linear(in_features=1024, out_features=1024, bias=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
            (output): ElectraSelfOutput(
              (dense): Linear(in_features=1024, out_features=1024, bias=True)
              (LayerNorm): LayerNorm((1024,), eps=1e-12, elementwise_affine=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
          )
          (intermediate): ElectraIntermediate(
            (dense): Linear(in_features=1024, out_features=4096, bias=True)
            (intermediate_act_fn): GELUActivation()
          )
          (output): ElectraOutput(
            (dense): Linear(in_features=4096, out_features=1024, bias=True)
            (LayerNorm): LayerNorm((1024,), eps=1e-12, elementwise_affine=True)
            (dropout): Dropout(p=0.1, inplace=False)
          )
        )
      )
    )
  )
  (custom_pooling): PoolingLayer()
  (classifier): Classifier(
    (layers): Sequential(
      (0): Linear(in_features=1024, out_features=1024, bias=True)
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

- `input_dim`: 1024
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

## Updated Performance by Dataset

### Merged Dataset

```
Merged Dataset Classification Report

              precision    recall  f1-score   support

    negative   0.874178  0.847789  0.860781      2352
     neutral   0.741715  0.770913  0.756032      1829
    positive   0.878194  0.877820  0.878007      2349

    accuracy                       0.837060      6530
   macro avg   0.831362  0.832174  0.831607      6530
weighted avg   0.838521  0.837060  0.837639      6530

ROC AUC: 0.947808

Predicted  negative  neutral  positive
Actual                                
negative       1994      268        90
neutral         223     1410       196
positive         64      223      2062

Macro F1 Score: 0.83
```

### DynaSent Round 1

```
DynaSent Round 1 Classification Report

              precision    recall  f1-score   support

    negative   0.925512  0.828333  0.874230      1200
     neutral   0.781536  0.924167  0.846888      1200
    positive   0.911472  0.840833  0.874729      1200

    accuracy                       0.864444      3600
   macro avg   0.872840  0.864444  0.865283      3600
weighted avg   0.872840  0.864444  0.865283      3600

ROC AUC: 0.962647

Predicted  negative  neutral  positive
Actual                                
negative        994      159        47
neutral          40     1109        51
positive         40      151      1009

Macro F1 Score: 0.87
```

### DynaSent Round 2

```
DynaSent Round 2 Classification Report

              precision    recall  f1-score   support

    negative   0.791339  0.837500  0.813765       240
     neutral   0.803030  0.662500  0.726027       240
    positive   0.768657  0.858333  0.811024       240

    accuracy                       0.786111       720
   macro avg   0.787675  0.786111  0.783605       720
weighted avg   0.787675  0.786111  0.783605       720

ROC AUC: 0.932089

Predicted  negative  neutral  positive
Actual                                
negative        201       18        21
neutral          40      159        41
positive         13       21       206

Macro F1 Score: 0.78
```

### Stanford Sentiment Treebank (SST-3)

```
SST-3 Classification Report

              precision    recall  f1-score   support

    negative   0.838405  0.876096  0.856836       912
     neutral   0.500000  0.365039  0.421991       389
    positive   0.870504  0.931793  0.900106       909

    accuracy                       0.809050      2210
   macro avg   0.736303  0.724309  0.726311      2210
weighted avg   0.792042  0.809050  0.798093      2210

ROC AUC: 0.905255

Predicted  negative  neutral  positive
Actual                                
negative        799       91        22
neutral         143      142       104
positive         11       51       847

Macro F1 Score: 0.73
```

## Old Performance by Dataset

### Merged Dataset

```
Merged Dataset Classification Report

              precision    recall  f1-score   support

    negative   0.858503  0.843537  0.850954      2352
     neutral   0.747684  0.750137  0.748908      1829
    positive   0.864513  0.877395  0.870906      2349

    accuracy                       0.829556      6530
   macro avg   0.823567  0.823690  0.823590      6530
weighted avg   0.829626  0.829556  0.829549      6530

ROC AUC: 0.947247

Predicted  negative  neutral  positive
Actual                                
negative       1984      256       112
neutral         246     1372       211
positive         81      207      2061

Macro F1 Score: 0.82
```

### DynaSent Round 1

```
DynaSent Round 1 Classification Report

              precision    recall  f1-score   support

    negative   0.913204  0.824167  0.866404      1200
     neutral   0.779433  0.915833  0.842146      1200
    positive   0.905149  0.835000  0.868661      1200

    accuracy                       0.858333      3600
   macro avg   0.865929  0.858333  0.859070      3600
weighted avg   0.865929  0.858333  0.859070      3600

ROC AUC: 0.963133

Predicted  negative  neutral  positive
Actual                                
negative        989      156        55
neutral          51     1099        50
positive         43      155      1002

Macro F1 Score: 0.86
```

### DynaSent Round 2

```
DynaSent Round 2 Classification Report

              precision    recall  f1-score   support

    negative   0.764706  0.812500  0.787879       240
     neutral   0.814815  0.641667  0.717949       240
    positive   0.731884  0.841667  0.782946       240

    accuracy                       0.765278       720
   macro avg   0.770468  0.765278  0.762924       720
weighted avg   0.770468  0.765278  0.762924       720

ROC AUC: 0.927688

Predicted  negative  neutral  positive
Actual                                
negative        195       19        26
neutral          38      154        48
positive         22       16       202

Macro F1 Score: 0.76
```

### Stanford Sentiment Treebank (SST-3)

```
SST-3 Classification Report

              precision    recall  f1-score   support

    negative   0.822199  0.877193  0.848806       912
     neutral   0.504237  0.305913  0.380800       389
    positive   0.856144  0.942794  0.897382       909

    accuracy                       0.803620      2210
   macro avg   0.727527  0.708633  0.708996      2210
weighted avg   0.780194  0.803620  0.786409      2210

ROC AUC: 0.904787

Predicted  negative  neutral  positive
Actual                                
negative        800       81        31
neutral         157      119       113
positive         16       36       857

Macro F1 Score: 0.71
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

