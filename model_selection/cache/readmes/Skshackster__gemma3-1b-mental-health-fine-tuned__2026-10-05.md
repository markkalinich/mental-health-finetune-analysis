---
license: apache-2.0
language:
- en
metrics:
- accuracy
base_model:
- google/gemma-3-1b-it
tags:
- medical
- mental
- health
- finetune
- gemma
---

# Model Card: Gemma 3 1B Mental Health Fine-Tuned

## Model Overview

**Model Name**: `Skshackster/gemma3-1b-mental-health-fine-tuned`  
**Base Model**: `google/gemma-3-1b-it`  
**Model Type**: Transformer-based Causal Language Model  
**License**: [Gemma License](https://ai.google.dev/gemma/terms) (Check base model license for specifics)  
**Developed by**: Skshackster
**Hosted on**: Hugging Face Hub  
**Intended Use**: Conversational mental health support, research in mental health dialogue systems  

This model is a fine-tuned version of Google's Gemma 3 1B Instruct model, specifically adapted for mental health therapy conversations. It has been trained on a dataset of 500 carefully curated mental health dialogues, totaling approximately 10 million tokens, to provide empathetic, safe, and supportive responses aligned with the role of a joyous mental therapy assistant.

## Model Description

- **Architecture**: Gemma 3 1B is a transformer-based causal language model with 1 billion parameters, optimized for instruction-following and conversational tasks.
- **Fine-Tuning Objective**: Enhance the model's ability to engage in empathetic, supportive, and safe mental health conversations, adhering to strict ethical guidelines.
- **Training Data**: 500 conversational examples in JSONL format, each containing a sequence of messages with roles (`system`, `user`, `assistant`). The dataset focuses on mental health topics such as stress, sadness, relationship challenges, and emotional well-being.
- **Token Count**: Approximately 10 million tokens, derived from the conversational dataset.
- **Training Framework**: Hugging Face Transformers, PyTorch, and Datasets libraries.
- **Training Duration**: 3 epochs, with checkpoints saved periodically.

## Dataset

The fine-tuning dataset consists of 500 mental health therapy conversations, formatted as JSONL. Each conversation includes:

- **System Prompt**: Defines the assistant’s role as a “helpful and joyous mental therapy assistant,” emphasizing safety, positivity, and ethical responses.
- **User Messages**: Describe mental health challenges, such as work-related stress, sadness, or relationship issues.
- **Assistant Responses**: Provide empathetic, supportive, and actionable advice, adhering to the system prompt’s guidelines.

### Dataset Statistics
- **Total Examples**: 500
- **Estimated Tokens**: ~10 million (based on tokenizer processing)
- **Format**: JSONL, with each line containing a `"messages"` list of role-content pairs.
- **Roles**: `system`, `user`, `assistant`
- **Average Conversation Length**: Variable, with some conversations exceeding 10 turns.
- **Content Focus**: Mental health support, covering topics like stress management, emotional resilience, and interpersonal relationships.

### Data Preparation
- **Loading**: Dataset loaded using Hugging Face `datasets` library.
- **Splitting**: The dataset was split into training and validation sets. Explicit splitting is recommended to avoid data leakage.
- **Tokenization**: Conversations serialized into a string format (`<|role|>content<|eos|>`) and tokenized using the Gemma 3 tokenizer with a maximum length of 1024 tokens, padded to ensure uniform sequence lengths.

## Technical Details

### Tokenization
- **Tokenizer**: `AutoTokenizer` from `google/gemma-3-1b-it`, using the fast tokenizer implementation.
- **Serialization**: Messages are concatenated with role markers (e.g., `<|system|>`, `<|user|>`, `<|assistant|>`) and terminated with the EOS token.
- **Padding**: Fixed-length padding to 1024 tokens per sequence.
- **Labels**: Input IDs copied as labels for causal language modeling.

### Model Configuration
- **Base Model**: `google/gemma-3-1b-it`
- **Precision**: `bfloat16` for efficient training.
- **Attention Implementation**: `eager` (Note: Consider `flash_attention_2` for improved performance if available).
- **Device Mapping**: `device_map="auto"` for automatic sharding across available devices.
- **Memory Optimization**:
  - Gradient checkpointing enabled to reduce memory usage.
  - KV cache disabled during training to avoid conflicts with checkpointing.
  - `low_cpu_mem_usage=True` for faster model initialization.

### Training Hyperparameters
- **Framework**: Hugging Face `Trainer` API
- **Batch Size**: 
  - Per-device batch size: 4 (training and evaluation)
  - Gradient accumulation steps: 16
  - Effective batch size: 64
- **Epochs**: 3
- **Learning Rate**: 1e-4
- **Warmup Steps**: 200
- **Optimizer**: Default (AdamW with Hugging Face defaults)
- **Precision**: `bf16=True` for mixed-precision training
- **Evaluation**: Performed periodically (Note: More frequent evaluation, e.g., every 100 steps, is recommended for small datasets)
- **Checkpointing**: Saved periodically, with a maximum of 3 checkpoints retained
- **Hub Integration**: Model checkpoints pushed to `Skshackster/gemma3-1b-mental-health-fine-tuned` on Hugging Face Hub

## Usage

### Prerequisites
- Python 3.8+
- Required libraries: `transformers`, `datasets`, `torch`, `huggingface_hub`

### Notes
- Ensure the input format matches the training data (role markers and EOS tokens).
- For optimal performance, use a GPU with `bfloat16` support.
- The model is fine-tuned for mental health support and may not generalize to other domains without further training.

## Ethical Considerations

- **Intended Use**: This model is designed for supportive mental health conversations, not as a replacement for professional therapy. Users should consult licensed mental health professionals for clinical needs.
- **Safety**: The system prompt enforces safe, positive, and unbiased responses, but users should monitor outputs for unintended behavior.
- **Bias**: The dataset is curated to avoid harmful content, but biases in the training data may persist. Users are encouraged to report any problematic outputs.
- **Privacy**: The model does not store or process personal data beyond the training dataset, which should be anonymized to protect user privacy.
- **Limitations**: The model may not handle complex mental health scenarios accurately and should be used as a supplementary tool.

## Evaluation

- **Metrics**: Training metrics are available in TensorBoard-compatible format. Evaluation was performed periodically, but more frequent evaluation is recommended for small datasets.
- **Performance**: The model is expected to generate empathetic and contextually appropriate responses for mental health queries, but quantitative metrics (e.g., perplexity) are not provided.
- **Validation**: Ensure the validation set is distinct from the training set to obtain reliable performance metrics.

## Limitations

- **Dataset Size**: With only 500 examples, the model may not capture the full diversity of mental health scenarios.
- **Data Leakage**: Using the same data for training and validation risks overfitting. Explicit splitting is recommended.
- **Truncation**: Conversations longer than 1024 tokens are truncated, potentially losing context.
- **Domain Specificity**: The model is optimized for mental health dialogues and may underperform in other domains.
- **Compute Requirements**: Fine-tuning and inference require significant computational resources.

## Future Improvements

- **Dataset Expansion**: Include more diverse mental health conversations to improve robustness.
- **Dynamic Padding**: Replace fixed-length padding with dynamic batch padding to optimize memory usage.
- **Flash Attention**: Use `flash_attention_2` for faster training if supported.
- **Frequent Evaluation**: Evaluate more frequently for better monitoring on small datasets.
- **Bias Mitigation**: Conduct bias audits and include adversarial testing to ensure fairness.

## Contact

For questions, issues, or contributions, please contact the model developer via the Hugging Face Hub or open an issue in the model repository.

## Acknowledgments

- Built on the `google/gemma-3-1b-it` model by Google.
- Powered by Hugging Face Transformers, Datasets, and PyTorch.