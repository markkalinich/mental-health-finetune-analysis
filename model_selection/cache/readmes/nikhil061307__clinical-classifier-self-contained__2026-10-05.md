# Clinical Entity Classification Model (Self-Contained)

This is a self-contained clinical entity classification model that predicts whether medical entities are:
- **Absent**: The condition/entity is not present
- **Hypothetical**: The condition/entity might be present (uncertain)
- **Present**: The condition/entity is confirmed to be present

## Key Features

✅ **Single Download**: Only downloads one model (~547MB) instead of three separate models  
✅ **Same Performance**: Identical accuracy to the original multi-model setup  
✅ **Easy to Use**: Drop-in replacement for existing inference code  

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
import torch
import torch.nn.functional as F

def predict_clinical_entity(text, model_name="nikhil061307/clinical-classifier-self-contained"):
    from huggingface_hub import hf_hub_download
    import tempfile
    import sys
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Download custom model files
        config_file = hf_hub_download(repo_id=model_name, filename="configuration_clinical.py", local_dir=tmp_dir)
        model_file = hf_hub_download(repo_id=model_name, filename="modeling_clinical.py", local_dir=tmp_dir)
        
        sys.path.insert(0, tmp_dir)
        
        import configuration_clinical
        import modeling_clinical
        
        # Register custom model classes
        AutoConfig.register("clinical_classification", configuration_clinical.ClinicalClassificationConfig)
        AutoModelForSequenceClassification.register(
            configuration_clinical.ClinicalClassificationConfig, 
            modeling_clinical.ClinicalClassificationModel
        )
        
        # Load model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
        sys.path.pop(0)
    
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits if hasattr(outputs, 'logits') else outputs[0]
        probs = F.softmax(logits, dim=-1)
        predicted_class = torch.argmax(logits, dim=-1).item()
    
    label_mapping = {0: "Absent", 1: "Hypothetical", 2: "Present"}
    predicted_label = label_mapping[predicted_class]
    confidence = probs[0][predicted_class].item()
    
    return {
        "text": text,
        "predicted_label": predicted_label,
        "confidence": confidence,
        "probabilities": {
            label: probs[0][i].item() 
            for i, label in label_mapping.items()
        }
    }

# Example usage
result = predict_clinical_entity("Patient has diabetes and hypertension")
print(f"Prediction: {result['predicted_label']} (confidence: {result['confidence']:.3f})")
```

## Model Architecture

- **Base Model**: Clinical_ModernBERT
- **Encoder**: Contrastive learning with mean pooling
- **Classifier**: 2-layer MLP with ReLU activation
- **Output**: 3-class classification (Absent, Hypothetical, Present)

## Performance

This model maintains the same accuracy as the original multi-component model while providing:
- 66% reduction in download size
- Faster inference loading
- Simplified deployment
