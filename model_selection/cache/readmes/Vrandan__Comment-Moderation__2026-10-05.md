---
library_name: transformers
tags:
- text-classification
- content-moderation
- comment-moderation
- text-moderation
license: openrail
language:
- en
base_model:
- distilbert/distilbert-base-uncased
---
# Comment Moderation Model

[![HuggingFace](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/Vrandan/Comment-Moderation) 
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-312/) 
[![License](https://img.shields.io/badge/License-OpenRAIL-green.svg)](https://huggingface.co/Vrandan/Comment-Moderation/blob/main/Comment%20Moderation-OpenRAIL.md)


A powerful, multi-label content moderation system built on **DistilBERT** architecture, designed to detect and classify potentially harmful content in user-generated comments with high accuracy. This model stands out as currently the best in terms of performance based on the provided dataset for text moderation. Additionally, it has the smallest footprint, making it ideal for deployment on edge devices. Currently, it is the only model trained to achieve such high performance while maintaining a minimal size relative to the training data on Hugging Face.

## Key Features

- Multi-label classification
- Real-time content analysis
- 95.4% accuracy rate
- 9 distinct content categories
- Easy integration via API or local implementation
- Lightweight deployment footprint
- Suitable for **edge devices and mobile applications**
- Low latency inference
- Resource-efficient while maintaining high accuracy
- Can run on consumer-grade hardware

## Content Categories

The model identifies the following types of potentially harmful content:

| Category | Label | Definition |
|----------|--------|------------|
| Sexual | `S` | Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness). |
| Hate | `H` | Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. |
| Violence | `V` | Content that promotes or glorifies violence or celebrates the suffering or humiliation of others. |
| Harassment | `HR` | Content that may be used to torment or annoy individuals in real life, or make harassment more likely to occur. |
| Self-Harm | `SH` | Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders. |
| Sexual/Minors | `S3` | Sexual content that includes an individual who is under 18 years old. |
| Hate/Threat | `H2` | Hateful content that also includes violence or serious harm towards the targeted group. |
| Violence/Graphic | `V2` | Violent content that depicts death, violence, or serious physical injury in extreme graphic detail. |
| Safe Content | `OK` | Appropriate content that doesn't violate any guidelines. |

## Performance Metrics

```
Accuracy: 95.4%
Mean ROC AUC: 0.912
Macro F1 Score: 0.407
Micro F1 Score: 0.802
```

[View detailed performance metrics](#model-performance)

## Training Details

The model was trained on an **NVIDIA RTX 3080** GPU in a home setup, demonstrating that effective content moderation models can be developed with consumer-grade hardware. This makes the model development process more accessible to individual developers and smaller organizations.

Key Training Specifications:
- Hardware: NVIDIA RTX 3080
- Base Model: DistilBERT
- Model Size: 67M parameters (optimized for efficient deployment)
- Training Environment: Local workstation
- Training Type: Fine-tuning

Despite its relatively compact size **(67M parameters)**, this model achieves impressive performance metrics, making it suitable for deployment across various devices and environments. The model's efficiency-to-performance ratio demonstrates that effective content moderation is possible without requiring extensive computational resources.

## Quick Start

### Python Implementation (Local)

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Initialize model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("Vrandan/Comment-Moderation")
tokenizer = AutoTokenizer.from_pretrained("Vrandan/Comment-Moderation")

def analyze_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    probabilities = outputs.logits.softmax(dim=-1).squeeze()
    
    # Get predictions
    labels = [model.config.id2label[i] for i in range(len(probabilities))]
    predictions = sorted(zip(labels, probabilities), key=lambda x: x[1], reverse=True)
    
    return predictions

# Example usage
text = "Your text here"
results = analyze_text(text)
for label, prob in results:
    print(f"{label}: {prob:.4f}")
```

#### Example Output:
```
Label: OK - Probability: 0.9840
Label: H - Probability: 0.0043
Label: SH - Probability: 0.0039
Label: V - Probability: 0.0019
Label: S - Probability: 0.0018
Label: HR - Probability: 0.0015
Label: V2 - Probability: 0.0011
Label: S3 - Probability: 0.0010
Label: H2 - Probability: 0.0006
```

### Python Implementation (Serverless)

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/Vrandan/Comment-Moderation"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
    
output = query({
    "inputs": "Your text here",
})
```

### JavaScript Implementation (Node.js)

```javascript
require('dotenv').config();
const { HfInference } = require('@huggingface/inference');
const readline = require('readline');

// Initialize the Hugging Face client
// To use this, follow these steps:
// 1. Create a `.env` file in the root directory of your project.
// 2. Visit https://huggingface.co/settings/tokens to generate your access token (you may need to create an account if you haven't already).
// 3. Add the token to your `.env` file like this:
//    HUGGING_FACE_ACCESS_TOKEN=your_token_here
// 4. Install dotenv & huggingface/inference package (`npm install dotenv` & `npm install @huggingface/inference`) and load it in your project.
const hf = new HfInference(process.env.HUGGING_FACE_ACCESS_TOKEN);

// Create readline interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function analyzeText(text) {
    try {
        const result = await hf.textClassification({
            model: 'Vrandan/Comment-Moderation',
            inputs: text
        });
        
        console.log('\nResults:');
        result.forEach(pred => {
            console.log(`Label: ${pred.label} - Probability: ${pred.score.toFixed(4)}`);
        });
    } catch (error) {
        console.error('Error analyzing text:', error.message);
    }
}

async function main() {
    while (true) {
        try {
            const text = await new Promise(resolve => {
                rl.question('\nEnter text to analyze (or "quit" to exit): ', resolve);
            });

            if (text.toLowerCase() === 'quit') break;
            if (text.trim()) await analyzeText(text);
        } catch (error) {
            console.error('Error:', error.message);
        }
    }
    rl.close();
}

main().catch(console.error);
```

### JavaScript Implementation (Serverless)

```javascript
async function query(data) {
    const response = await fetch(
        "https://api-inference.huggingface.co/models/Vrandan/Comment-Moderation",
        {
            headers: {
                Authorization: "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "Content-Type": "application/json",
            },
            method: "POST",
            body: JSON.stringify(data),
        }
    );
    const result = await response.json();
    return result;
}

query({"inputs": "Your text here"}).then((response) => {
    console.log(JSON.stringify(response));
});
```

## Detailed Model Performance <a name="model-performance"></a>

The model has been extensively evaluated using standard classification metrics:

- **Loss:** 0.641  
- **Accuracy:** 0.954 (95.4%)  
- **Macro F1 Score:** 0.407  
- **Micro F1 Score:** 0.802  
- **Weighted F1 Score:** 0.763  
- **Macro Precision:** 0.653  
- **Micro Precision:** 0.875  
- **Weighted Precision:** 0.838  
- **Macro Recall:** 0.349  
- **Micro Recall:** 0.740  
- **Weighted Recall:** 0.740  
- **Mean ROC AUC:** 0.912  

## ⚠️ Important Considerations

### Ethical Usage
- Regular bias monitoring
- Context-aware implementation
- Privacy-first approach

### Limitations
- May miss contextual nuances
- Potential for false positives
- Cultural context variations

## Dataset Information

This model was trained on the dataset released by OpenAI, as described in their paper ["A Holistic Approach to Undesired Content Detection"](https://arxiv.org/abs/2208.03274).

### Dataset Source
- 📄 [Original Paper (PDF)](https://arxiv.org/pdf/2208.03274)
- 💾 [Dataset Repository](https://github.com/openai/moderation-api-release)

### Citation
If you use this model or dataset in your research, please cite:
```bibtex
@article{openai2022moderation,
  title={A Holistic Approach to Undesired Content Detection},
  author={Todor Markov and Chong Zhang and Sandhini Agarwal and Tyna Eloundou and Teddy Lee and Steven Adler and Angela Jiang and Lilian Weng},
  journal={arXiv preprint arXiv:2208.03274},
  year={2022}
}
```

## Contact

For support or queries, please message me on Slack.

---