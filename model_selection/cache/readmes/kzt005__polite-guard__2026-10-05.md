---
base_model:
- google-bert/bert-base-uncased
datasets:
- Intel/polite-guard
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-classification
tags:
- Intel
- transformers.js
model-index:
- name: polite-guard
  results:
  - task:
      type: text-classification
    dataset:
      name: polite-guard
      type: polite-guard
    metrics:
    - type: accuracy
      value: 92
      name: Accuracy
    - type: f1
      value: 92
      name: F1 Score
---
# Polite Guard

- **Model type**: BERT* (Bidirectional Encoder Representations from Transformers)  
- **Architecture**: Fine-tuned [BERT-base uncased](https://huggingface.co/bert-base-uncased)
- **Task**: Text Classification
- **Source Code**: https://github.com/intel/polite-guard
- **Dataset**: https://huggingface.co/datasets/Intel/polite-guard

**Polite Guard** is an open-source NLP language model developed by Intel, fine-tuned from BERT for text classification tasks. It is designed to classify text into four categories: polite, somewhat polite, neutral, and impolite. This model, along with its [accompanying datasets](https://huggingface.co/datasets/Intel/polite-guard) and [source code](https://github.com/intel/polite-guard), is available on Hugging Face* and GitHub* to enable both communities to contribute to developing more sophisticated and context-aware AI systems.

## Use Cases

Polite Guard provides a scalable model development pipeline and methodology, making it easier for developers to create and fine-tune their own models. Other contributions of the project include:

- **Improved Robustness**:
Polite Guard enhances the resilience of systems by providing a defense mechanism against adversarial attacks. This ensures that the model can maintain its performance and reliability even when faced with potentially harmful inputs. 
- **Benchmarking and Evaluation**:
The project introduces the first politeness benchmark, allowing developers to evaluate and compare the performance of their models in terms of politeness classification. This helps in setting a standard for future developments in this area. 
- **Enhanced Customer Experience**:
By ensuring respectful and polite interactions on various platforms, Polite Guard can significantly boost customer satisfaction and loyalty. This is particularly beneficial for customer service applications where maintaining a positive tone is crucial.

## Description of labels

- **polite**: Text is considerate and shows respect and good manners, often including courteous phrases and a friendly tone.
- **somewhat polite**: Text is generally respectful but lacks warmth or formality, communicating with a decent level of courtesy.
- **neutral**: Text is straightforward and factual, without emotional undertones or specific attempts at politeness.
- **impolite**: Text is disrespectful or rude, often blunt or dismissive, showing a lack of consideration for the recipient's feelings.

## Model Details

- **Training Data**: The model was trained on the [Polite Guard Dataset](https://huggingface.co/datasets/Intel/polite-guard) utilizing Intel® Gaudi® Al accelerators. The training dataset consists of synthetically generated customer service interactions across various sectors, including finance, travel, food and drink, retail, sports clubs, culture and education, and professional development.
- **Base Model**: [BERT-base](https://huggingface.co/bert-base-uncased), with 12 layers, 110M parameters.
- **Fine-tuning Process**: Fine-tuning was performed on the Polite Guard train dataset with the following hyperparameters using PyTorch Lightning*.

|Hypeparameter|Batch size|Learning rate|Learning rate schedule          |Max epochs|Optimizer|Weight decay|Precision |
|-------------|----------|-------------|--------------------------------|----------|---------|------------|----------|
|Value        |32        |   4.78e-05  |Linear warmup (10% of steps)    |  2       | AdamW   |  1.01e-06  |bf16-mixed|

Hyperparameter tuning was performed using Bayesian optimization with the Tree-structured Parzen Estimator (TPE) algorithm through Optuna* with 35 trials to maximize the validation F1-score. The hyperparameter search space included 

```
learning rate: [1e-5, 5e-4]
weight decay: [1e-6, 1e-2]
```

The fine-tuning process used Optuna's pruning callback to terminate underperforming hyperparameter trials, and model checkpointing to save the best performing model states.

![Parallel Coordinate Plot](./polite-guard-parallel-coordinate.png)
![Hyperparameter Importance Plot](./polite-guard-hyperparameter-importance.png)

The code for the synthetic data generation and fine-tuning can be found [here](https://github.com/intel/polite-guard).

### Metrics

Here are the key performance metrics of the model on the test dataset containing both synthetic and manually annotated data:

- **Accuracy**: 92% on the Polite Guard test dataset.
- **F1-Score**: 92% on the Polite Guard test dataset.

## How to Use

You can use this model directly with a pipeline for categorizing text into classes polite, somewhat polite, neutral, and impolite.

```python
from transformers import pipeline

classifier = pipeline("text-classification", "Intel/polite-guard")
text = "Your input text"
output = classifier(text)
print(output)
```

The next example demonstrates how to run this model in the browser using Hugging Face's `transformers.js` library with `webnn-gpu` for hardware acceleration.

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>WebNN Transformers.js Intel/polite-guard</h1>
    <script type="module">
      import { pipeline } from "https://cdn.jsdelivr.net/npm/@huggingface/transformers";

      const classifier = await pipeline("text-classification", "Intel/polite-guard", {
        dtype: "fp32",
        device: "webnn-gpu", // You can also try: "webgpu", "webnn", "webnn-npu", "webnn-cpu", "wasm" 
      });

      const text = "Your input text";
      const output = await classifier(text);
      console.log(`${text}: ${output[0].label}`);
    </script>
  </body>
</html>
```
## Articles

To learn more about the implementation of the data generator and fine-tuner packages, refer to

- [Synthetic Data Generation with Language Models: A Practical Guide](https://medium.com/p/0ff98eb226a1), and 
- [How to Fine-Tune Language Models: First Principles to Scalable Performance](https://medium.com/p/78f42b02f112).

For more AI development how-to content, visit [Intel® AI Development Resources](https://www.intel.com/content/www/us/en/developer/topic-technology/artificial-intelligence/overview.html).

## Join the Community

If you are interested in exploring other models, join us in the Intel and Hugging Face communities. These models simplify the development and adoption of Generative AI solutions, while fostering innovation among developers worldwide. If you find this project valuable, please like ❤️ it on Hugging Face and share it with your network. Your support helps us grow the community and reach more contributors.

## Disclaimer

Polite Guard has been trained and validated on a limited set of data that pertains to customer reviews, product reviews, and corporate communications. Accuracy metrics cannot be guaranteed outside these narrow use cases, and therefore this tool should be validated within the specific context of use for which it might be deployed. This tool is not intended to be used to evaluate employee performance. This tool is not sufficient to prevent harm in many contexts, and additional tools and techniques should be employed in any sensitive use case where impolite speech may cause harm to individuals, communities, or society.

## Privacy Notice

Please note that the Polite Guard model uses AI technology and you are interacting with a chatbot. Prompts that are being used during the demo will not be stored. For information regarding the handling of personal data collected refer to the Global Privacy Notice (https://www.intel.com/content/www/us/en/privacy/intelprivacy-notice.html), which encompass our privacy practices.

*Other names and brands may be claimed as the property of others.