---
language:
- en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- flan-t5
datasets:
- custom-dataset-name  # Replace with your actual dataset name
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: text2text-generation
---

# FLAN-T5 Sentiment Analysis Model

This is a fine-tuned version of the **FLAN-T5** model for sentiment analysis on healthcare-related reviews and general text classification. The model is trained on a combination of two sentiment-labeled datasets, utilizing custom weighting to address class imbalance. The model can classify text into three sentiment categories: **Positive**, **Neutral**, and **Negative**.

---

## Model Description

The model is based on **T5 (Text-To-Text Transfer Transformer)**, a versatile transformer architecture that performs various NLP tasks by casting them into a text-to-text framework. In this case, the model has been fine-tuned for **sentiment classification** using a custom dataset. 

**Model Type:**  
- **Transformer**  
- **Text-to-Text Model**  
- **Pre-trained Base:** Google FLAN-T5 (flan-t5-base)

---

## Training Data

### Datasets Used

- **Dataset 1**: Balanced Sentiment Dataset  
- **Dataset 2**: Final Dataset with New Negative Sentiments

Both datasets contain labeled sentiment data, where the target labels are `negative`, `neutral`, and `positive`. 

### Text Normalization

Text data has been preprocessed by:
1. Converting all text to lowercase.
2. Removing URLs, special characters, and excessive whitespaces.
3. Handling missing data by filling with an empty string.

### Sample Weighting

We applied **sample weighting** to address class imbalances:
- Samples from **Dataset 1** are assigned a weight of 1.
- Samples from **Dataset 2** are assigned a higher weight of 3 to account for their greater importance.

---

## Evaluation Results

The model has been evaluated on a separate test set, and the following metrics were achieved:

| Metric          | Score   |
|-----------------|---------|
| **Accuracy**    | 99.01%  |
| **Precision**   | 99.02%  |
| **Recall**      | 99.01%  |
| **F1-Score**    | 98.89%  |

### Class-Wise Performance

| Class     | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| **Negative** | 1.0000 | 1.0000 | 1.0000   | 4       |
| **Neutral**  | 0.9899 | 1.0000 | 0.9949   | 1575    |
| **Positive** | 1.0000 | 0.9897 | 0.9419   | 39      |

---

## Model Training

### Model Architecture

- **Base Model**: `google/flan-t5-base`
- **Tokenization**: Using the `T5Tokenizer` to tokenize the input text before feeding it to the model.
- **Loss Function**: CrossEntropyLoss (with weights applied for class imbalance).
- **Optimization**: Adam optimizer with a learning rate of `3e-5`.

### Hyperparameters

- **Batch Size**: 8
- **Learning Rate**: `3e-5`
- **Number of Epochs**: 3
- **Warmup Steps**: 500
- **Weight Decay**: 0.01
- **FP16**: Yes (for faster computation)
- **Save Strategy**: Save the model after each epoch.

---

## Model Usage

The fine-tuned model can be used for text classification tasks such as **sentiment analysis** on reviews or general text. Below is an example of how to use the model for inference.

### Inference Example

```python
from transformers import pipeline

# Load the fine-tuned model
model_name = "ShahzaibAli-1/sentiment_model_2_flant_5_base"
classifier = pipeline(
    "text2text-generation",
    model=model_name,
    device=0 if torch.cuda.is_available() else -1
)

# Test the model with some sample text
def test_prompt(prompt):
    response = classifier(prompt, max_new_tokens=10, temperature=0.1, do_sample=False)
    print(f"Prompt: {prompt}
Output: {response[0]['generated_text'].strip()}")

# Test with a sample sentiment classification
test_prompt("classify sentiment: The physical therapy sessions completely relieved my chronic back pain")
```

---

## Example Outputs

Here are some example outputs for various test cases:

- **Healthcare Review**:  
  Prompt: `"The physical therapy sessions completely relieved my chronic back pain"`  
  Output: `positive`

- **Mixed Review**:  
  Prompt: `"The facility was excellent but the doctor was always late"`  
  Output: `negative`

- **Ambiguous Review**:  
  Prompt: `"The treatment was... interesting"`  
  Output: `positive`

- **Promotional Text**:  
  Prompt: `"Experience pain-free living with our new therapy techniques!"`  
  Output: `neutral`

---

## Evaluation Metrics

The following evaluation metrics were used to assess the model's performance:

- **Accuracy**: The percentage of correct predictions over the total number of predictions.
- **Precision**: The proportion of positive predictions that were actually correct.
- **Recall**: The proportion of actual positives that were correctly identified.
- **F1-Score**: The harmonic mean of precision and recall.

The model demonstrated strong performance across all metrics, particularly with accuracy close to 99%.

---

## Limitations

While the model performs well on the test set, there are some limitations:

- **Sarcasm Detection**: The model struggles with detecting sarcasm in text, as shown in some test cases where sarcastic reviews were classified as neutral.
- **Multilingual Support**: The model primarily works with English text and might not perform well on multilingual inputs.
- **Contextual Nuances**: Some complex or ambiguous cases (e.g., mixed sentiment reviews) might require further refinement in training.

---

## Model Deployment

Once the model was trained, it was pushed to the Hugging Face model hub for easy access. You can use the model with the following command:

```python
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the model and tokenizer from the Hugging Face Hub
model_name = "ShahzaibAli-1/sentiment_model_2_flant_5_base"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Use the model to classify sentiment
inputs = tokenizer("classify sentiment: The therapist was excellent!", return_tensors="pt")
outputs = model.generate(**inputs)
predicted_sentiment = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"Predicted Sentiment: {predicted_sentiment}")
```

---

## Citation

If you use this model in your research or projects, please cite it as follows:

```
@article{shahzaib2025sentiment,
  title={Fine-Tuning FLAN-T5 for Sentiment Analysis},
  author={Shahzaib Ali},
  journal={Hugging Face Model Hub},
  year={2025},
  url={https://huggingface.co/ShahzaibAli-1/sentiment_model_2_flant_5_base}
}
```

---

## License

The model is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use it in your applications and research.

---

## Contact

For any questions or suggestions, feel free to open an issue or contact the model creator at:  
- **Hugging Face**: [ShahzaibAli-1](https://huggingface.co/ShahzaibAli-1)
