---
base_model: distilbert/distilbert-base-uncased
language: en
license: apache-2.0
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- sentiment
- synthetic data
- multi-class
- social-media-analysis
- customer-feedback
- product-reviews
- brand-monitoring
widget:
- text: I absolutely loved this movie! The acting was superb and the plot was engaging.
  example_title: Very Positive Review
- text: The service at this restaurant was terrible. I'll never go back.
  example_title: Very Negative Review
- text: The product works as expected. Nothing special, but it gets the job done.
  example_title: Neutral Review
- text: I'm somewhat disappointed with my purchase. It's not as good as I hoped.
  example_title: Negative Review
- text: This book changed my life! I couldn't put it down and learned so much.
  example_title: Very Positive Review
inference:
  parameters:
    temperature: 1
---



# 🚀 (distil)BERT-based Sentiment Classification Model: Unleashing the Power of Synthetic Data


<!-- TRY IT HERE: https://huggingface.co/spaces/vdmbrsv/sentiment-analysis-english-five-classes

[![Join Our Discord](https://img.shields.io/badge/Discord-Join%20Now-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/sznxwdqBXj)

---- -->

# NEWS! 

- 2024/12: We uploaded an even better and more robust sentiment model! The error rate is reduced by 10%, and overall accuracy is improved!







----

## Model Details
- **Model Name:** tabularisai/robust-sentiment-analysis
- **Base Model:** distilbert/distilbert-base-uncased
- **Task:** Text Classification (Sentiment Analysis)
- **Language:** English
- **Number of Classes:** 5 (*Very Negative, Negative, Neutral, Positive, Very Positive*)
- **Usage:** 
  - Social media analysis
  - Customer feedback analysis
  - Product reviews classification
  - Brand monitoring
  - Market research
  - Customer service optimization
  - Competitive intelligence

## Model Description

This model is a fine-tuned version of `distilbert/distilbert-base-uncased` for sentiment analysis. **Trained only on syntethic data**.

### Training Data

The model was fine-tuned on synthetic data, which allows for targeted training on a diverse range of sentiment expressions without the limitations often found in real-world datasets. 

### Training Procedure

- The model was fine-tuned for 5 epochs.
- Achieved a train_acc_off_by_one (accuracy allowing for predictions off by one class) of approximately *0.95* on the validation dataset.

## Intended Use

This model is designed for sentiment analysis tasks, particularly useful for:
- Social media monitoring
- Customer feedback analysis
- Product review sentiment classification
- Brand sentiment tracking

## How to Use

Here's a quick example of how to use the model:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "tabularisai/robust-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Function to predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(text.lower(), return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    
    sentiment_map = {0: "Very Negative", 1: "Negative", 2: "Neutral", 3: "Positive", 4: "Very Positive"}
    return sentiment_map[predicted_class]

# Example usage
texts = [
    "I absolutely loved this movie! The acting was superb and the plot was engaging.",
    "The service at this restaurant was terrible. I'll never go back.",
    "The product works as expected. Nothing special, but it gets the job done.",
    "I'm somewhat disappointed with my purchase. It's not as good as I hoped.",
    "This book changed my life! I couldn't put it down and learned so much."
]

for text in texts:
    sentiment = predict_sentiment(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}\n")
```

## Model Performance

The model demonstrates strong performance across various sentiment categories. Here are some example predictions:
```
1. "I absolutely loved this movie! The acting was superb and the plot was engaging."
   Predicted Sentiment: Very Positive

2. "The service at this restaurant was terrible. I'll never go back."
   Predicted Sentiment: Very Negative

3. "The product works as expected. Nothing special, but it gets the job done."
   Predicted Sentiment: Neutral

4. "I'm somewhat disappointed with my purchase. It's not as good as I hoped."
   Predicted Sentiment: Negative

5. "This book changed my life! I couldn't put it down and learned so much."
   Predicted Sentiment: Very Positive
```



## JS example 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tabularis Sentiment Analysis</title>
</head>
<body>
    <div id="output"></div>

    <script type="module">
        import { AutoTokenizer, AutoModel, env } from 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.6.0';

        env.allowLocalModels = false;
        env.useCDN = true;

        const MODEL_NAME = 'tabularisai/robust-sentiment-analysis';

        function softmax(arr) {
            const max = Math.max(...arr);
            const exp = arr.map(x => Math.exp(x - max));
            const sum = exp.reduce((acc, val) => acc + val);
            return exp.map(x => x / sum);
        }

        async function analyzeSentiment() {
            try {
                const tokenizer = await AutoTokenizer.from_pretrained(MODEL_NAME);
                const model = await AutoModel.from_pretrained(MODEL_NAME);

                const texts = [
                    "I absolutely loved this movie! The acting was superb and the plot was engaging.",
                    "The service at this restaurant was terrible. I'll never go back.",
                    "The product works as expected. Nothing special, but it gets the job done.",
                    "I'm somewhat disappointed with my purchase. It's not as good as I hoped.",
                    "This book changed my life! I couldn't put it down and learned so much."
                ];

                const output = document.getElementById('output');

                for (const text of texts) {
                    const inputs = await tokenizer(text, { return_tensors: 'pt' });
                    const result = await model(inputs);
                    
                    console.log('Model output:', result);

                    if (result.output && result.output.data) {
                        const logitsArray = Array.from(result.output.data);
                        console.log('Logits array:', logitsArray);

                        const probabilities = softmax(logitsArray);
                        const predicted_class = probabilities.indexOf(Math.max(...probabilities));

                        const sentimentMap = {
                            0: "Very Negative",
                            1: "Negative",
                            2: "Neutral",
                            3: "Positive",
                            4: "Very Positive"
                        };

                        const sentiment = sentimentMap[predicted_class];
                        const score = probabilities[predicted_class];

                        output.innerHTML += `Text: "${text}"<br>`;
                        output.innerHTML += `Sentiment: ${sentiment}, Score: ${score.toFixed(4)}<br><br>`;
                    } else {
                        console.error('Unexpected model output structure:', result);
                        output.innerHTML += `Unable to process: "${text}"<br><br>`;
                    }
                }
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('output').innerHTML = 'An error occurred. Please check the console for details.';
            }
        }

        analyzeSentiment();
    </script>
</body>
</html>
```

## Training Procedure

The model was fine-tuned on synthetic data using the `distilbert/distilbert-base-uncased` architecture. The training process involved:

- Dataset: Synthetic data designed to cover a wide range of sentiment expressions
- Training framework: PyTorch Lightning
- Number of epochs: 5
- Performance metric: Achieved train_acc_off_by_one of approximately 0.95 on the validation dataset

## Ethical Considerations

While efforts have been made to create a balanced and fair model through the use of synthetic data, users should be aware that the model may still exhibit biases. It's crucial to thoroughly test the model in your specific use case and monitor its performance over time.

## Citation
```
Will be included
```

## Contact

For questions or private and reliable API with out model please contact `info@tabularis.ai`


tabularis.ai



<table align="center">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/company/tabularis-ai/">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" alt="LinkedIn" width="30" height="30">
      </a>
    </td>
    <td align="center">
      <a href="https://x.com/tabularis_ai">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/x.svg" alt="X" width="30" height="30">
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/tabularis-ai">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub" width="30" height="30">
      </a>
    </td>
    <td align="center">
      <a href="https://tabularis.ai">
        <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/internetarchive.svg" alt="Website" width="30" height="30">
      </a>
    </td>
  </tr>
</table>
