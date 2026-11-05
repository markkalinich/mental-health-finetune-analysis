---
license: mit
datasets:
- avaliev/chat_doctor
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- medical
- biology
- conversetional
- qween
- doctor
---
To generate text using the `AutoTokenizer` and `AutoModelForCausalLM` from the Hugging Face Transformers library, you can follow these steps. First, ensure you have the necessary libraries installed:

```bash
pip install transformers torch
```

Then, use the following Python code to load the model and generate text:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Xennon-BD/Doctor-Chad")
model = AutoModelForCausalLM.from_pretrained("Xennon-BD/Doctor-Chad")

# Define the input prompt
input_text = "Hello, how are you doing today?"

# Encode the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate text
output_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True)

# Decode the generated text
generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print(generated_text)
```

### Explanation:

1. **Load the Tokenizer and Model**:
   ```python
   tokenizer = AutoTokenizer.from_pretrained("Xennon-BD/Doctor-Chad")
   model = AutoModelForCausalLM.from_pretrained("Xennon-BD/Doctor-Chad")
   ```
   This code loads the tokenizer and model from the specified Hugging Face model repository.

2. **Define the Input Prompt**:
   ```python
   input_text = "Hello, how are you doing today?"
   ```
   This is the text prompt that you want the model to complete or generate text from.

3. **Encode the Input Text**:
   ```python
   input_ids = tokenizer.encode(input_text, return_tensors="pt")
   ```
   The `tokenizer.encode` method converts the input text into token IDs that the model can process. The `return_tensors="pt"` argument specifies that the output should be in the form of PyTorch tensors.

4. **Generate Text**:
   ```python
   output_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True)
   ```
   The `model.generate` method generates text based on the input token IDs. 
   - `max_length=50` specifies the maximum length of the generated text.
   - `num_return_sequences=1` specifies the number of generated text sequences to return.
   - `do_sample=True` indicates that sampling should be used to generate text, which introduces some randomness and can produce more varied text.

5. **Decode the Generated Text**:
   ```python
   generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
   ```
   The `tokenizer.decode` method converts the generated token IDs back into human-readable text. The `skip_special_tokens=True` argument ensures that special tokens (like `<|endoftext|>`) are not included in the output.

6. **Print the Generated Text**:
   ```python
   print(generated_text)
   ```

   This prints the generated text to the console.

You can modify the input prompt and the parameters of the `model.generate` method to suit your needs, such as adjusting `max_length` for longer or shorter text generation, or changing `num_return_sequences` to generate multiple variations.