---
license: apache-2.0
---
<style>
table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 20px;
}
th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
}
.best {
    font-weight: bold;
    text-decoration: underline;
}
</style>

<div style="text-align: center; margin: 20px auto; padding: 20px; border: 3px solid #ddd; border-radius: 10px;">
  <h2 style="margin-bottom: 4px; margin-top: 0px;">OuteAI</h2>
  <a href="https://www.outeai.com/" target="_blank" style="margin-right: 10px;">🌎 OuteAI.com</a> 
  <a href="https://discord.gg/vyBM87kAmf" target="_blank" style="margin-right: 10px;">🤝 Join our Discord</a>
  <a href="https://x.com/OuteAI" target="_blank">𝕏 @OuteAI</a>
</div>

# Lite-Oute-1-300M-Instruct

Lite-Oute-1-300M-Instruct is a Lite series model based on the Mistral architecture, comprising approximately 300 million parameters. <br>
This model aims to improve upon our previous 150M version by increasing size and training on a more refined dataset. The primary goal of this 300 million parameter model is to offer enhanced performance while still maintaining efficiency for deployment on a variety of devices. <br>
With its larger size, it should provide improved context retention and coherence, however users should note that as a compact model, it still have limitations compared to larger language models. <br>
The model was trained on 30 billion tokens with a context length of 4096.

## Available versions:
<a href="https://huggingface.co/OuteAI/Lite-Oute-1-300M-Instruct">Lite-Oute-1-300M-Instruct</a> <br>
<a href="https://huggingface.co/OuteAI/Lite-Oute-1-300M-Instruct-GGUF">Lite-Oute-1-300M-Instruct-GGUF</a> <br>
<a href="https://huggingface.co/OuteAI/Lite-Oute-1-300M">Lite-Oute-1-300M</a> <br>
<a href="https://huggingface.co/OuteAI/Lite-Oute-1-300M-GGUF">Lite-Oute-1-300M-GGUF</a> <br>

## Chat format
> [!IMPORTANT]
> This model uses **ChatML** template. Ensure you use the correct template:

```
<|im_start|>system
[System message]<|im_end|>
<|im_start|>user
[Your question or message]<|im_end|>
<|im_start|>assistant
[The model's response]<|im_end|>
```

## Benchmarks:
<table style="text-align: left;">
  <tr>
    <th>Benchmark</th>
    <th>5-shot</th>
    <th>0-shot</th>
  </tr>
  <tr>
    <td>ARC Challenge</td>
    <td>26.37</td>
    <td>26.02</td>
  </tr>
  <tr>
    <td>ARC Easy</td>
    <td>51.43</td>
    <td>49.79</td>
  </tr>
  <tr>
    <td>CommonsenseQA</td>
    <td>20.72</td>
    <td>20.31</td>
  </tr>
  <tr>
    <td>HellaSWAG</td>
    <td>34.93</td>
    <td>34.50</td>
  </tr>
  <tr>
    <td>MMLU</td>
    <td>25.87</td>
    <td>24.00</td>
  </tr>
  <tr>
    <td>OpenBookQA</td>
    <td>31.40</td>
    <td>32.20</td>
  </tr>
  <tr>
    <td>PIQA</td>
    <td>65.07</td>
    <td>65.40</td>
  </tr>
  <tr>
    <td>Winogrande</td>
    <td>52.01</td>
    <td>53.75</td>
  </tr>
</table>


## Usage with HuggingFace transformers 
The model can be used with HuggingFace's `transformers` library:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModelForCausalLM.from_pretrained("OuteAI/Lite-Oute-1-300M-Instruct").to(device)
tokenizer = AutoTokenizer.from_pretrained("OuteAI/Lite-Oute-1-300M-Instruct")
def generate_response(message: str, temperature: float = 0.4, repetition_penalty: float = 1.12) -> str:
    # Apply the chat template and convert to PyTorch tensors
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]
    input_ids = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt"
    ).to(device)
    # Generate the response
    output = model.generate(
        input_ids,
        max_length=512,
        temperature=temperature,
        repetition_penalty=repetition_penalty,
        do_sample=True
    ) 
    # Decode the generated output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text
message = "I'd like to learn about language models. Can you break down the concept for me?"
response = generate_response(message)
print(response)
```

## Risk Disclaimer

By using this model, you acknowledge that you understand and assume the risks associated with its use. You are solely responsible for ensuring compliance with all applicable laws and regulations. We disclaim any liability for problems arising from the use of this open-source model, including but not limited to direct, indirect, incidental, consequential, or punitive damages. We make no warranties, express or implied, regarding the model's performance, accuracy, or fitness for a particular purpose. Your use of this model is at your own risk, and you agree to hold harmless and indemnify us, our affiliates, and our contributors from any claims, damages, or expenses arising from your use of the model.