---
language: fr
license: openrail
tags: [token-classification, ner, biomedical, french, medical]
datasets: [TypicaAI/MedicalNER_Fr]
pipeline_tag: token-classification
base_model: Dr-BERT/DrBERT-7GB
finetuned_from: Dr-BERT/DrBERT-7GB
library_name: transformers
model-index:
  - name: DrBERT-MedicalNER-FR
    results: []
    metadata:
      - type: code
        value: https://github.com/spideystreet/mediNote/tree/refactor
      - type: commit
        value: efcad26
---

# NER DrBERT (FR Medical) - Fine-tuned Model

Available here: [@Model](https://huggingface.co/spideystreet/DrBERT-MedicalNER-FR/tree/main)

## Model Description

This is a fine-tuned Named Entity Recognition (NER) model based on **DrBERT-7GB**, specifically trained for French medical text processing.  
The model is designed to extract clinical entities from unstructured French medical notes.

### Base Model
- **Backbone**: [@DrBERT-7GB](https://huggingface.co/Dr-BERT/DrBERT-7GB)
- **Architecture**: RoBERTa-based transformer with 12 layers, 12 attention heads, 768 embedding dimension
- **Training Data**: NACHOS 7GB corpus (French medical text)

### Fine-tuning Dataset
- **Dataset**: [@TypicaAI/MedicalNER_Fr](https://huggingface.co/datasets/TypicaAI/MedicalNER_Fr)
- **Task**: Token Classification (NER)
- **Language**: French
- **Domain**: Medical/Clinical

## Model Performance

### Training Configuration
- **Learning Rate**: 3e-5
- **Batch Size**: 8
- **Max Sequence Length**: 384
- **Training Epochs**: 4
- **Optimizer**: AdamW
- **Weight Decay**: 0.01

### Validation Metrics
- **F1 Score**: ~0.73 (span-level)
- **Precision**: ~0.75
- **Recall**: ~0.71
- **Accuracy**: ~0.95

*Note: Metrics from early POC training. Performance may vary with different configurations.*

## Supported Entity Types

The model can identify the following medical entities:

| Entity Type | Description | Example |
|-------------|-------------|---------|
| **PERSON** | Patient names, medical personnel | "M. Dupont", "Dr. Martin" |
| **SYMPTOM** | Medical symptoms | "douleur", "fièvre", "nausée" |
| **DISEASE** | Medical conditions | "hypertension", "diabète" |
| **MEDICATION** | Drugs and treatments | "paracétamol", "insuline" |
| **PROCEDURE** | Medical procedures | "radiographie", "chirurgie" |
| **ANATOMY** | Body parts and structures | "cœur", "poumon", "abdomen" |
| **LOCATION** | Anatomical locations | "bras droit", "thorax" |
| **ORGANIZATION** | Medical institutions | "hôpital", "clinique" |
| **CLINICAL_TERM** | Clinical terminology | "diagnostic", "traitement" |
| **GROUP** | Patient groups | "enfants", "adultes" |
| **PRODUCT** | Medical products | "appareil", "équipement" |

## Model Limitations

### Current Limitations
- **Sequence Length**: Limited to 384 tokens (longer notes are truncated)
- **Class Imbalance**: Some entity types may be underrepresented
- **Domain Specificity**: Optimized for French medical text
- **Early POC**: This is a proof-of-concept model, not production-ready

### Known Issues
- May struggle with very long medical reports
- Performance may vary with different medical specialties
- Requires validation by medical professionals for clinical use

## Training Details

### Data Preprocessing
- Tokenization using DrBERT-7GB tokenizer
- Label alignment for subword tokens
- Train/validation/test split: 80/10/10
- Data augmentation: None (preserving medical accuracy)

### Training Environment
- **Hardware**: Mac Air M3 16GB
- **Framework**: PyTorch with Hugging Face Transformers
- **Training Time**: ~2 hours for 4 epochs

## Model Files

This directory contains:
- `config.json` - Model configuration
- `model.safetensors` - Model weights (SafeTensors format)
- `tokenizer.json` - Tokenizer configuration
- `tokenizer_config.json` - Tokenizer settings
- `special_tokens_map.json` - Special tokens mapping
- `training_args.bin` - Training arguments
- `checkpoint-*/` - Training checkpoints

## Citation

If you use this model, please cite:

```bibtex
@inproceedings{labrak2023drbert,
    title = {{DrBERT: A Robust Pre-trained Model in French for Biomedical and Clinical domains}},
    author = {Labrak, Yanis and Bazoge, Adrien and Dufour, Richard and Rouvier, Mickael and Morin, Emmanuel and Daille, Béatrice and Gourraud, Pierre-Antoine},
    booktitle = {Proceedings of the 61th Annual Meeting of the Association for Computational Linguistics (ACL'23), Long Paper},
    month = july,
    year = {2023},
    address = {Toronto, Canada},
    publisher = {Association for Computational Linguistics}
}
```

## License

This model is released under the **OpenRail License**. See the [LICENSE](LICENSE) file in this directory for details.

The OpenRail License is designed for AI models and provides:
- **Open use** for research and commercial purposes
- **Responsible AI** guidelines and restrictions
- **Attribution** requirements
- **Safety** and **ethical use** provisions

## Medical Use Disclaimer

⚠️ **IMPORTANT**: This model is for research and development purposes only. It is NOT approved for clinical use and should not be used for direct patient care without proper validation by qualified medical professionals.

## Contact

- **Project**: [@MediNotes](https://github.com/spideystreet/mediNote)
- **Issues**: [GitHub Issues](https://github.com/spideystreet/mediNote/issues)
- **Author**: [@spidey](https://x.com/spideystreet)

---

*Last updated: September 2025*
*Model version: POC v0.1.1*