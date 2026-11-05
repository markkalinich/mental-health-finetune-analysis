---
language:
- multilingual
tags:
- dutch
- multilingual
- restaurant-reviews
- sentiment-analysis
- multi-head
- xlm-roberta
- regression
datasets:
- cmotions/NL_restaurant_reviews
base_model:
- FacebookAI/xlm-roberta-base
---

# Restaurant Review Analyzer for Dutch Reviews (Multilingual)

This model analyzes restaurant reviews and predicts scores across three dimensions:
- Taste
- Service
- Ambiance

The model is based on XLM-RoBERTa, which provides multilingual capabilities, allowing it to potentially work with reviews in different languages, although it was primarily trained on Dutch reviews.

## Model Description

This is a multi-head regression model designed for restaurant review analysis. It uses XLM-RoBERTa as the encoder backbone with custom regression heads for each dimension. The model extracts semantic information from restaurant reviews and predicts quality scores for different aspects of the restaurant experience.

### Key Features
- **Multi-dimensional scoring**: Predicts scores for multiple restaurant aspects simultaneously
- **Multilingual capabilities**: Based on XLM-RoBERTa which supports 100+ languages
- **Transfer learning**: Benefits from the pre-trained knowledge of XLM-RoBERTa
- **Compact architecture**: Efficient design with minimal additional parameters beyond the base model

## Performance

The model achieves the following performance metrics on Dutch restaurant reviews:

| Dimension | MSE    | MAE    | R²     |
|-----------|--------|--------|--------|
| Taste     | 1.0103 | 0.7518 | 0.7719 |
| Service   | 1.1899 | 0.8194 | 0.7643 |
| Ambiance  | 1.3515 | 0.8741 | 0.4948 |
| Overall   | 1.1839 | 0.8151 | 0.6770 |

## Baseline Comparison

To validate the effectiveness of our approach, we compared the XLM-RoBERTa model against a simple baseline model that uses TF-IDF vectorization and Ridge regression. Here's how our model performs relative to the baseline:

| Metric | Improvement over Baseline |
|--------|---------------------------|
| MSE    | ~34.81% reduction         |
| MAE    | ~20.73% reduction         |
| R²     | ~29.50% increase          |

The baseline model represents a traditional approach to review analysis using bag-of-words representations, which fails to capture the semantic relationships between words that our transformer-based model excels at.

### Performance Comparison Visualization

![MSE, MAE, R² Comparison between XLM-RoBERTa and Baseline](images/performance_comparison.png)

### Advantages over Baseline

- **Contextual understanding**: The XLM-RoBERTa model understands words in context, allowing it to better interpret nuanced expressions
- **Cross-lingual transfer**: Unlike the baseline, our model can leverage knowledge from other languages
- **Handling of negations**: The model correctly interprets negative phrases that bag-of-words models struggle with
- **Long-range dependencies**: Can understand relationships between parts of a sentence that are far apart

The significant performance improvement over the baseline demonstrates the value of using transformer-based architectures for this task, especially in multilingual contexts.

## Comparison with Large Language Models (Zero-Shot)

To evaluate our model's effectiveness in a broader context, we compared its performance against general-purpose large language models (LLMs) using zero-shot prompting on Dutch restaurant reviews. This comparison helps illustrate the value of domain-specific fine-tuning versus larger, more general models.

**Comparison Models:**
* Custom Model (Fine-tuned XLM-RoBERTa)
* `Qwen/Qwen2.5-3B`
* `Qwen/Qwen2.5-7B`

**Key Findings (based on 50 samples):**
* **Fine-tuned Model Outperforms Larger LLMs:** Despite having far fewer parameters (250M vs 3B/7B), our domain-specific model achieved lower error rates and higher correlation with human ratings across all dimensions.
* **Increasing Model Size Doesn't Guarantee Better Performance:** Interestingly, the larger 7B model often performed worse than the 3B model, particularly for taste scores, highlighting that domain specialization can be more important than scale.
* **Ambiance Detection Gap:** The most dramatic performance difference was in ambiance prediction, where our specialized model achieved an R² of 0.61 compared to only 0.05 for Qwen 3B and 0.17 for Qwen 7B.

**Performance Visualization:**
![Model Performance Comparison](images/comparison2.png)
*(Based on evaluation using the official test split from the NL_restaurant_reviews dataset)*

**Detailed Comparison Metrics:**
| Model | Dimension | MSE ↓ | MAE ↓ | R² ↑ |
|-------|-----------|-------|-------|------|
| **Custom Model** | Taste | **1.06** | **0.76** | **0.76** |
| | Service | **1.40** | **0.91** | **0.72** |
| | Ambiance | **1.27** | **0.84** | **0.61** |
| **Qwen 2.5-3B** | Taste | 1.51 | 0.91 | 0.65 |
| | Service | 1.82 | 0.95 | 0.64 |
| | Ambiance | 3.10 | 1.25 | 0.05 |
| **Qwen 2.5-7B** | Taste | 1.98 | 1.13 | 0.54 |
| | Service | 2.05 | 1.01 | 0.59 |
| | Ambiance | 2.71 | 1.11 | 0.17 |

This comparison demonstrates that our specialized model achieves:
- 30-42% lower MSE compared to the LLMs
- 16-33% lower MAE across all dimensions
- Significantly higher R² values, especially for ambiance prediction

These results validate our approach of fine-tuning a smaller multilingual model specifically for restaurant review analysis rather than relying on general-purpose LLMs, providing superior performance with greater efficiency.

## Training Details

- **Base Model**: xlm-roberta-base (250M parameters)
- **Training Dataset**: [NL_restaurant_reviews](https://huggingface.co/datasets/cmotions/NL_restaurant_reviews)
- **Training Procedure**:
  - Fine-tuned using MSE loss
  - Optimizer: AdamW with weight decay 0.001
  - Learning rate: 2e-5 for encoder, 6e-5 for regression heads
  - Early stopping based on validation loss
  - Gradient accumulation with accumulation steps = 4
  - Trained with weighted loss, emphasizing the Ambiance dimension (weight 1.5)

## Limitations and Biases

- The model was primarily trained on Dutch restaurant reviews and may perform less effectively on other languages
- Although XLM-RoBERTa supports 100+ languages, performance will vary based on language representation in the pre-training data
- Scores are predicted on a 1-10 scale but may exhibit bias toward certain score ranges
- May not capture cultural nuances in restaurant reviews from different regions
- Models used in comparison can be more diverse and robust

## Intended Use Cases

This model is designed for:
- Restaurant review aggregation and summarization
- Customer feedback analysis for restaurant owners
- Market research in the hospitality industry
- Cross-lingual restaurant review understanding
- User experience evaluation for dining establishments

## Languages

While trained primarily on Dutch data, the XLM-RoBERTa backbone has potential capabilities in these languages (among others):
- Dutch (primary)
- English
- German
- French
- Spanish
- Portuguese
- Italian

## Model Details

- **Model Type**: Multi-head regression model
- **Encoder**: XLM-RoBERTa Base (xlm-roberta-base)
- **Output Heads**: 3 separate regression heads (Taste, Service, Ambiance)
- **Parameters**: ~250M (mostly from XLM-RoBERTa)
- **Context Length**: 512 tokens
- **Output**: Scores on a 1-10 scale for each dimension

## Usage

Using this model requires defining a custom Python class (`RestaurantReviewAnalyzer`) in your environment *before* loading the model. You'll initialize this class, which loads the base encoder weights, and then manually load the custom regression head weights from the `regression_heads.json` file.

**1. Prerequisites:**

First, ensure you have the necessary libraries installed:

```bash
pip install torch transformers huggingface_hub
```

**2. Define the Custom Model Class:**

You **must** include the following `RestaurantReviewAnalyzer` class definition in your Python script or notebook. This definition needs to be **identical** to the one used during the model's training.

```python
# --- Imports needed for the class ---
import torch
import torch.nn as nn
from transformers import AutoModel

# --- Custom Model Class Definition ---
class RestaurantReviewAnalyzer(nn.Module):
    """
    A custom model that uses a pre-trained transformer encoder (like XLM-RoBERTa)
    and adds separate regression heads to predict scores for different dimensions
    of a restaurant review (Taste, Service, Ambiance).
    """
    def __init__(self, pretrained_model_name="xlm-roberta-base", num_dimensions=3, dropout_prob=0.1):
        super().__init__()
        print(f"Initializing custom model structure with base: {pretrained_model_name}")
        # Load the pre-trained base model specified by pretrained_model_name
        self.encoder = AutoModel.from_pretrained(pretrained_model_name)
        self.config = self.encoder.config
        hidden_size = self.config.hidden_size # Get hidden size from the base model's config
        # Define the names of the dimensions to predict
        self.dimension_names = ["Taste", "Service", "Ambiance"] # Should match training setup
        # Create a ModuleDict to hold the separate regression head for each dimension
        self.regression_heads = nn.ModuleDict({
            dim: nn.Sequential(
                nn.Dropout(dropout_prob),       # Dropout layer
                nn.Linear(hidden_size, 64),  # First linear layer
                nn.GELU(),                   # Activation function
                nn.Linear(64, 1)              # Output linear layer (predicts a single value)
            ) for dim in self.dimension_names[:num_dimensions]
        })
        print("Custom regression heads structure created.")

    # Define the forward pass: how input data flows through the model
    def forward(self, input_ids, attention_mask=None):
        # Pass input through the base encoder
        encoder_output = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        # Use the output corresponding to the [CLS] token as the pooled representation
        # Shape: [batch_size, hidden_size]
        pooled_output = encoder_output.last_hidden_state[:, 0]
        results = {}
        # Pass the pooled output through each dimension's regression head
        for dim in self.dimension_names:
            score = self.regression_heads[dim](pooled_output)
            # Apply sigmoid and scale the output to be between 1.0 and 10.0
            results[dim] = 1.0 + 9.0 * torch.sigmoid(score)
            # Remove the last dimension (shape becomes [batch_size])
            results[dim] = results[dim].squeeze(-1)
        return results # Return a dictionary {'DimensionName': scores_tensor, ...}
```

**3. Load Tokenizer, Model, and Weights:**

Load the tokenizer, initialize the model structure (this loads the base XLM-R weights), determine the device (`cuda` or `cpu`), move the model to the device, and then load the custom regression head weights from `regression_heads.json`.

```python
# --- Further imports ---
import torch
from transformers import AutoTokenizer
import json
from huggingface_hub import hf_hub_download

# --- Configuration ---
repo_id = "c0sm1c9/restaurant-review-analyzer-dutch"

# --- Load Tokenizer ---
# The tokenizer converts text into numerical IDs that the model understands.
print(f"Loading tokenizer from: {repo_id}")
tokenizer = AutoTokenizer.from_pretrained(repo_id)
print("Tokenizer loaded.")

# --- Initialize Model Structure ---
# This creates an instance of your custom RestaurantReviewAnalyzer class.
# The `AutoModel.from_pretrained(pretrained_model_name)` inside the __init__
# loads the weights of the base model (e.g., xlm-roberta-base) from the repo_id.
print("Initializing model structure (loads base encoder weights)...")
model = RestaurantReviewAnalyzer(pretrained_model_name=repo_id)
print("Model structure initialized.")

# --- Determine Device ---
# Choose the device to run the model on: GPU (cuda) if available, otherwise CPU.
# It's crucial that the model and input data reside on the same device.
model_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"\nTarget device selected: {model_device}")

# --- Move Model to Device ---
# Move the entire model (including base encoder and regression heads) to the chosen device.
model.to(model_device)
print(f"Model moved to {model_device}.")

# --- Load Custom Regression Head Weights ---
# These weights were trained specifically for the regression task and are stored separately.
try:
    regression_heads_filename = "regression_heads.json" # The name of the weights file in the repo
    print(f"Downloading custom weights '{regression_heads_filename}'...")
    # Download the file from the Hugging Face Hub
    regression_heads_path = hf_hub_download(
        repo_id=repo_id,
        filename=regression_heads_filename
    )
    print(f"Downloaded weights file to: {regression_heads_path}")

    # Load the weights from the downloaded JSON file
    print("Loading weights from JSON file...")
    with open(regression_heads_path, 'r') as f:
        regression_heads_dict_from_json = json.load(f)
    print("JSON weights data loaded.")

    # Convert the loaded data (lists) back into a PyTorch state_dict
    # A state_dict maps parameter names (strings) to their tensor values.
    regression_heads_state_dict = {}
    print("Converting JSON weights to tensors on target device...")
    # Iterate through dimensions ('Taste', 'Service', 'Ambiance') in the JSON data
    for dim_name, params in regression_heads_dict_from_json.items():
        # Check if the dimension exists in our model's regression heads
        if dim_name in model.regression_heads:
            # Get the state_dict of the corresponding head in the *current* model
            # This helps ensure we use the correct parameter names, shapes, and dtypes.
            layer_state_dict = model.regression_heads[dim_name].state_dict()
            # Iterate through parameters ('1.weight', '1.bias', '3.weight', '3.bias', etc.) for this dimension
            for param_name, param_value_list in params.items():
                # Find the matching parameter key in the model's layer state_dict
                # This handles potential key name differences (e.g., due to ModuleDict prefixing)
                for model_param_key in layer_state_dict.keys():
                    if model_param_key == param_name or model_param_key.endswith("." + param_name):
                        # Get the target data type and shape from the model's parameter
                        target_dtype = layer_state_dict[model_param_key].dtype
                        target_shape = layer_state_dict[model_param_key].shape
                        # Create the tensor directly on the target device (model_device) and with the correct dtype
                        tensor_value = torch.tensor(param_value_list, dtype=target_dtype, device=model_device)
                        # Verify the number of elements matches before reshaping (safety check)
                        if tensor_value.numel() != target_shape.numel():
                            raise RuntimeError(f"Shape mismatch for {dim_name}.{model_param_key}: JSON({tensor_value.numel()}) vs Model({target_shape.numel()})")
                        # Reshape the tensor to match the model's parameter shape
                        tensor_value = tensor_value.view(target_shape)
                        # Store the tensor in the state_dict using the model's full key name (e.g., 'Taste.1.weight')
                        regression_heads_state_dict[f"{dim_name}.{model_param_key}"] = tensor_value
                        break # Found the matching key, move to the next parameter in the JSON

    # Load the constructed state_dict into the `regression_heads` part of the model
    # `strict=True` ensures all keys match between the state_dict and the model module.
    print("Applying weights to the model's regression heads...")
    model.regression_heads.load_state_dict(regression_heads_state_dict, strict=True)
    print("Regression head weights loaded successfully into the model.")
    print("Model is ready for inference.")

except Exception as e:
    print(f"ERROR during weight loading: {e}")
    print("Please check the model files and class definition.")
    # Depending on your application, you might want to handle this error more gracefully
    raise e # Re-raise the exception to halt execution if loading fails
```

**4. Perform Inference:**

Now you can use the fully loaded model to predict scores for new reviews. Remember to move the tokenized input tensors to the same device as the model.

```python
# --- Example Inference ---
print("\n--- Starting Example Inference ---")
# Set the model to evaluation mode (important for consistent results)
# This disables mechanisms like dropout that are only used during training.
model.eval()

# Example Dutch restaurant review
review = "Heerlijk gegeten bij dit restaurant! De service was top en de sfeer gezellig."
# English: "Ate wonderfully at this restaurant! The service was great and the atmosphere cozy."
print(f"Input Review: '{review}'")

# Tokenize the input text using the loaded tokenizer
print("Tokenizing the input review...")
# `return_tensors="pt"` specifies PyTorch tensors as output.
# `padding=True` pads the sequence to the maximum length in the batch (or max_length).
# `truncation=True` cuts off text longer than max_length.
# `max_length=512` is a common sequence length limit for BERT-like models.
inputs = tokenizer(review, return_tensors="pt", padding=True, truncation=True, max_length=512)
# `inputs` is now a dictionary containing 'input_ids' and 'attention_mask' tensors.

# --- CRITICAL STEP: Move Input Tensors to the Model's Device ---
# Both the model and its input data *must* be on the same device (CPU or GPU).
print(f"Moving input tensors to {model_device}...")
inputs = {k: v.to(model_device) for k, v in inputs.items()}
print("Input tensors moved.")

# Perform inference without calculating gradients
# `torch.no_grad()` reduces memory usage and speeds up computation during inference.
print("Performing inference with the model...")
with torch.no_grad():
    # Pass the prepared inputs to the model
    outputs = model(input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"])
    # `outputs` is the dictionary returned by the model's forward method:
    # e.g., {'Taste': tensor([9.2], device='cuda:0'), ...}

# Process and display the results
print("\nPredicted Scores (Scale 1-10):")
for dim, score_tensor in outputs.items():
    # Use `.item()` to extract the single numerical value from the tensor
    # Format the float to one decimal place using f-string formatting
    print(f"  {dim}: {score_tensor.item():.1f}")

print("\n--- Inference Complete ---")

# Example Output (scores may vary slightly):
# Predicted Scores (Scale 1-10):
#   Taste: 9.2
#   Service: 9.5
#   Ambiance: 8.8
```

## Citation

If you use this model in your research, please cite:
```
@misc{restaurant-review-analyzer-dutch,
  author = {Haitao Tao},
  title = {Restaurant Review Analyzer (Multilingual)},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/c0sm1c9/restaurant-review-analyzer-dutch}}
}
```

## Acknowledgements

- XLM-RoBERTa base model by Facebook AI Research
- Dutch restaurant reviews dataset by cmotions
- Hugging Face for the model hosting infrastructure

