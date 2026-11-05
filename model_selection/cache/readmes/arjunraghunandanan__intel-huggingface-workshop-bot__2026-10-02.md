---
library_name: transformers
tags:
- intel
- ipex
- emotion-recognition
- sentiment-analysis
- Beginner Level
license: mit
language:
- en
---
model_card_content = """
# Model Card for My Sentiment Analysis Bot : Intel Workshop

## Model Description
- **Purpose**: For Classifying Emotions from text.
- **Model architecture**: Distilbert model
- **Training data**: Text examples with labels corresponding to emotions such as  ex: sad, happy, love, etc.

## Intended Use
- **Intended users**: Model created and deployed for learning purposes while following Intel's Huggingface Optimization Workshop.  
- **Use cases**: Sentiment Analysis, Social Media Comment Filtering, Review Filtering. 

## Example Sentences
- **Input**: Winning the lottery has filled me with an indescribable joy that makes me want to sing and dance!
-- **Type of Sentiment**: Happy
  
- **Input**: Saying goodbye to my beloved pet was the hardest thing I've ever done, and the sadness feels like a heavy weight on my heart.
-- **Type of Sentiment**: Sad

- **Input**: The blatant injustice of the situation infuriates me to the core. How can anyone stand by and allow such unfairness?
-- **Type of Sentiment**: Angry

- **Input**: I can't believe it - I actually got the job! This is a complete shock, but an amazing one!
-- **Type of Sentiment**: Surprised

- **Input**: The storm raging outside is terrifying. The howling wind and crashing thunder make me feel uneasy and unsafe.
-- **Type of Sentiment**: Fearful

## Limitations
- **Known limitations**: This deplopyment is done for learning purposes. This is not trained on a big dataset and is not that accurate. Causes erroneous results. 

## Hardware 
- **Training Platform**: Intel Developer Cloud Training JupyterLabs using Intel 4th Generation Xeon Processors.
- **Link to IDC Training**: https://console.cloud.intel.com/training

## Software Optimizations
- **Known Optimizations**: Outside of my beginner level understanding. I followed tutorial steps. 

## Ethical Considerations
- **Ethical concerns**: Created for Learning purposes only,may not be monitored, improved. Use with caution. 

## More Information
- developed for Intel workshop : https://software.seek.intel.com/oneapi-ws-hugging-face-toolkit
- Followed live tutorials from Eduardo : https://huggingface.co/eduardo-alvarez/emotion-bot-2000

"""