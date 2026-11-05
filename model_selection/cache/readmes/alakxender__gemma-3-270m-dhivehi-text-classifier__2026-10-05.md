---
library_name: transformers
tags:
- dhivehi
- thaana
- classification
- sentiment-analysis
- topic-classification
- intent-recognition
- opinion-mining
license: mit
datasets:
- alakxender/dhivehi-english-pairs-with-metadata
- alakxender/dhivehi-english-translations
language:
- dv
base_model:
- google/gemma-3-270m-it
---

# Gemma-3-270M Dhivehi — Classification Model

Compact Dhivehi (ދިވެހި) classification model based on `google/gemma-3-270m-it`, designed to perform various text classification tasks in Dhivehi including sentiment analysis, topic classification, intent recognition, and opinion mining.

**Note:** This model is specifically tuned for classification tasks and provides structured JSON outputs for easy integration into downstream applications.

## Model details

* **Base**: `google/gemma-3-270m-it`
* **Language**: Dhivehi
* **Style**: Analytical, structured, consistent
* **Output format**: JSON-structured classification results
* **Supported tasks**:
  * Sentiment analysis (positive, negative, neutral)
  * Topic classification (news, politics, sports, etc.)
  * Intent recognition (question, statement, request, etc.)
  * Opinion mining (support, oppose, neutral)

## Intended use

* Dhivehi text classification for content moderation
* Sentiment analysis of Dhivehi social media content
* Topic categorization for news and content organization
* Intent classification for chatbot and customer service applications
* Opinion analysis for research and analytics

Not intended for: open-domain factual lookup, legal/medical advice, or long multi-turn conversations.

## How to use

### Model Setup

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import json

model_path = "alakxender/gemma-3-270m-dhivehi-text-classifier"

model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    torch_dtype="auto", 
    device_map="auto", 
    attn_implementation="eager"
)
tokenizer = AutoTokenizer.from_pretrained(model_path)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
```

### Classification Function Definitions

Here are the function definitions for each classification task:

```python
def analyze_sentiment(dhivehi_text: str, model, tokenizer, pipe, max_new_tokens: int = 128, temperature: float = 0.1, top_p: float = 0.2, top_k: int = 5, do_sample: bool = False):
    """
    Analyze sentiment of Dhivehi text
    
    Args:
        dhivehi_text: Input Dhivehi text
        model: Loaded model
        tokenizer: Loaded tokenizer
        pipe: Loaded pipeline
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Top-p sampling parameter
        top_k: Top-k sampling parameter
        do_sample: Whether to use sampling
        
    Returns:
        Dictionary with sentiment analysis result
    """
    instruction = f"Analyze the sentiment of this Dhivehi text: {dhivehi_text}"
    return _generate_classification_response(instruction, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)

def classify_topic(dhivehi_text: str, model, tokenizer, pipe, max_new_tokens: int = 128, temperature: float = 0.1, top_p: float = 0.2, top_k: int = 5, do_sample: bool = False):
    """
    Classify topic of Dhivehi text
    
    Args:
        dhivehi_text: Input Dhivehi text
        model: Loaded model
        tokenizer: Loaded tokenizer
        pipe: Loaded pipeline
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Top-p sampling parameter
        top_k: Top-k sampling parameter
        do_sample: Whether to use sampling
        
    Returns:
        Dictionary with topic classification result
    """
    instruction = f"Determine the topic of this Dhivehi text: {dhivehi_text}"
    return _generate_classification_response(instruction, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)

def identify_intent(dhivehi_text: str, model, tokenizer, pipe, max_new_tokens: int = 128, temperature: float = 0.1, top_p: float = 0.2, top_k: int = 5, do_sample: bool = False):
    """
    Identify intent in Dhivehi text
    
    Args:
        dhivehi_text: Input Dhivehi text
        model: Loaded model
        tokenizer: Loaded tokenizer
        pipe: Loaded pipeline
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Top-p sampling parameter
        top_k: Top-k sampling parameter
        do_sample: Whether to use sampling
        
    Returns:
        Dictionary with intent identification result
    """
    instruction = f"Identify the intent behind this Dhivehi text: {dhivehi_text}"
    return _generate_classification_response(instruction, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)

def classify_opinion(dhivehi_text: str, model, tokenizer, pipe, max_new_tokens: int = 128, temperature: float = 0.1, top_p: float = 0.2, top_k: int = 5, do_sample: bool = False):
    """
    Classify opinion in Dhivehi text
    
    Args:
        dhivehi_text: Input Dhivehi text
        model: Loaded model
        tokenizer: Loaded tokenizer
        pipe: Loaded pipeline
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Top-p sampling parameter
        top_k: Top-k sampling parameter
        do_sample: Whether to use sampling
        
    Returns:
        Dictionary with opinion classification result
    """
    instruction = f"Classify the opinion expressed in this Dhivehi text: {dhivehi_text}"
    return _generate_classification_response(instruction, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)

def analyze_all(dhivehi_text: str, model, tokenizer, pipe, max_new_tokens: int = 128, temperature: float = 0.1, top_p: float = 0.2, top_k: int = 5, do_sample: bool = False):
    """
    Run all analysis tasks on the input text
    
    Args:
        dhivehi_text: Input Dhivehi text
        model: Loaded model
        tokenizer: Loaded tokenizer
        pipe: Loaded pipeline
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Top-p sampling parameter
        top_k: Top-k sampling parameter
        do_sample: Whether to use sampling
        
    Returns:
        Dictionary with all analysis results
    """
    if pipe is None or model is None or tokenizer is None:
        return {"error": "Please load a classification model first!"}
    
    try:
        opinion_result = classify_opinion(dhivehi_text, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)
        sentiment_result = analyze_sentiment(dhivehi_text, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)
        intent_result = identify_intent(dhivehi_text, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)
        topic_result = classify_topic(dhivehi_text, model, tokenizer, pipe, max_new_tokens, temperature, top_p, top_k, do_sample)
        
        # Extract the actual values from nested results
        results = {
            "opinion": opinion_result.get("opinion", "unknown") if isinstance(opinion_result, dict) else opinion_result,
            "sentiment": sentiment_result.get("sentiment", "unknown") if isinstance(sentiment_result, dict) else sentiment_result,
            "intent": intent_result.get("intent", "unknown") if isinstance(intent_result, dict) else intent_result,
            "topic": topic_result.get("topic", "unknown") if isinstance(topic_result, dict) else topic_result
        }
        
        return results
    except Exception as e:
        return {"error": f"Error in complete analysis: {str(e)}"}

def _generate_classification_response(instruction: str, model, tokenizer, pipe, max_new_tokens: int, temperature: float, top_p: float, top_k: int, do_sample: bool):
    """
    Helper function to generate classification response
    
    Args:
        instruction: The instruction for the model
        model: Loaded model
        tokenizer: Loaded tokenizer
        pipe: Loaded pipeline
        max_new_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Top-p sampling parameter
        top_k: Top-k sampling parameter
        do_sample: Whether to use sampling
        
    Returns:
        Dictionary with classification result
    """
    if pipe is None or model is None or tokenizer is None:
        return {"error": "Please load a classification model first!"}
    
    try:
        messages = [{"role": "user", "content": instruction}]
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        # Generation parameters
        if do_sample:
            gen_kwargs = {
                "max_new_tokens": max_new_tokens,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "do_sample": True,
                "disable_compile": True,
                "pad_token_id": tokenizer.eos_token_id
            }
        else:
            gen_kwargs = {
                "max_new_tokens": max_new_tokens,
                "disable_compile": True,
                "pad_token_id": tokenizer.eos_token_id
            }
        
        outputs = pipe(prompt, **gen_kwargs)
        
        # Extract only the generated part
        response = outputs[0]['generated_text'][len(prompt):].strip()
        
        # Try to parse JSON response
        try:
            import json
            result = json.loads(response)
            return result
        except json.JSONDecodeError:
            return {"raw_response": response, "error": "Failed to parse JSON"}
            
    except Exception as e:
        return {"error": f"Error in classification: {str(e)}"}
```

### Usage Example

```python
# Load your model, tokenizer, and pipeline first
# model, tokenizer, pipe = load_your_model()

# Example text for classification
dhivehi_text = "ދިވެހިރާއްޖެއަކީ އިންޑިޔާ ކަނޑުގައި އޮންނަ ޖަޒީރާ ޤައުމެކެވެ."

# Run individual classifications
sentiment_result = analyze_sentiment(dhivehi_text, model, tokenizer, pipe)
topic_result = classify_topic(dhivehi_text, model, tokenizer, pipe)
intent_result = identify_intent(dhivehi_text, model, tokenizer, pipe)
opinion_result = classify_opinion(dhivehi_text, model, tokenizer, pipe)

# Or run all analyses at once
all_results = analyze_all(dhivehi_text, model, tokenizer, pipe)

print(f"Sentiment: {sentiment_result}")
print(f"Topic: {topic_result}")
print(f"Intent: {intent_result}")
print(f"Opinion: {opinion_result}")
print(f"Complete Analysis: {all_results}")

""" 
# Response: 
Sentiment: {'sentiment': 'Positive'}
Topic: {'topic': 'Politics'}
Intent: {'intent': 'Identification'}
Opinion: {'opinion': 'Neutral'}
Complete Analysis: {'opinion': 'Neutral', 'sentiment': 'Neutral', 'intent': 'Statement', 'topic': 'International' 
"""
```

## Sample Classification Categories

***Note: The model will output additional classification categories that are not listed here.***

### Sentiment Analysis
* **positive**: Expresses positive emotions or favorable views
* **negative**: Expresses negative emotions or unfavorable views  
* **neutral**: Expresses neutral or balanced views

### Topic Classification
* **news**: News articles and current events
* **politics**: Political discussions and government
* **sports**: Sports news and athletic activities
* **entertainment**: Movies, music, and cultural events
* **technology**: Tech news and innovations
* **health**: Health and medical information
* **education**: Educational content and academic topics
* **business**: Business and economic news

### Intent Recognition
* **question**: Asking for information or clarification
* **statement**: Making a factual statement
* **request**: Asking for action or assistance
* **opinion**: Expressing personal views
* **complaint**: Expressing dissatisfaction
* **praise**: Expressing appreciation or approval

### Opinion Mining
* **support**: Expressing agreement or support
* **oppose**: Expressing disagreement or opposition
* **neutral**: Expressing balanced or neutral stance

## Generation Tips

* Use `do_sample=False` for consistent, deterministic classification results
* Keep `max_new_tokens` modest (64-128) for focused classification outputs
* The model outputs structured JSON for easy parsing
* Dhivehi is RTL; ensure your environment renders RTL text correctly

## Prompting Patterns

* **Sentiment Analysis**
  * instruction: "Analyze the sentiment of this Dhivehi text: [text]"
  * expected output: `{"sentiment": "positive/negative/neutral"}`

* **Topic Classification**
  * instruction: "Determine the topic of this Dhivehi text: [text]"
  * expected output: `{"topic": "news/politics/sports/etc"}`

* **Intent Recognition**
  * instruction: "Identify the intent behind this Dhivehi text: [text]"
  * expected output: `{"intent": "question/statement/request/etc"}`

* **Opinion Mining**
  * instruction: "Classify the opinion expressed in this Dhivehi text: [text]"
  * expected output: `{"opinion": "support/oppose/neutral"}`

## Limitations

* Classification accuracy depends on the quality and relevance of the input text
* May struggle with ambiguous or mixed-sentiment text
* Domain expertise is limited to patterns seen in the training data
* Long texts may exceed context limits; provide focused excerpts for best results
* The model is specifically trained for classification tasks in Dhivehi