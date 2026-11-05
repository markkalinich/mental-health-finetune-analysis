---
license: mit
language:
- en
- hi
- ta
- te
- kn
- ml
metrics:
- accuracy
base_model:
- ai4bharat/indic-bert
pipeline_tag: text-classification
library_name: transformers
tags:
- moderation
- abuse_detection
---


# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("iamrazi/text-moderation")  #                                                                          

model = AutoModelForSequenceClassification.from_pretrained("iamrazi/text-moderation")

model.eval()  # Set model to evaluation mode



  def predict_abuse(text: str, threshold: float = 0.5):                 
  
      """
      Predict if a text is abusive or not.
      
      Args:
          text (str): Input text.
          threshold (float): Probability threshold for classification.
      
      Returns:
          label (int): 0 for non-abusive, 1 for abusive
          proba (float): Probability of being abusive
      """
      # Tokenize
      inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
      
      # Forward pass
      with torch.no_grad():
          outputs = model(**inputs)
          logits = outputs.logits
          probas = torch.sigmoid(logits)  # if your model output layer is logits
      
      # For binary classification, take the probability of class 1
      prob = probas[0][1].item() if probas.shape[1] > 1 else probas[0][0].item()
      
      # Determine label
      label = 1 if prob >= threshold else 0
      
      return label, prob


text = "तुम बहुत गंदे हो 😡"


label, proba = predict_abuse(text)

Output: Label: 0, Probability: 0.08
