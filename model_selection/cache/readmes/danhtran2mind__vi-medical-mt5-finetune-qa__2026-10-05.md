---
license: mit
language:
- vi
base_model:
- google/mt5-small
pipeline_tag: question-answering
library_name: transformers
tags:
- medical
---
<div align="center">
  <h1>
    Vietnamese Medical mT5 Finetune Question and Answer
  </h1>
</div>

# Dataset
You can download dataset at this url: https://github.com/triet2397/UIT-ViCoV19QA
# Metrics
- Loss:
  - Trainging Set: 0.306100.
  - Validation Set: 0.322764.

# Usage

## Import Libraires
```python
import torch
from underthesea import word_tokenize
from transformers import AutoModel, AutoTokenizer, AutoModelForSeq2SeqLM
```
## Define Functions
```python
def load_model_and_tokenizer(model_path):
    # Load the trained tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # Load the trained model
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

    # Move the model to the GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    return tokenizer, model, device

def generate_text(tokenizer, model, device, prompt, max_length=100,
                  num_return_sequences=1, top_p=0.95, temperature=0.7, seed=123):
    # Set the random seed for reproducibility
    torch.manual_seed(seed)

    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

    # Generate text
    output = model.generate(
        input_ids,
        max_length=max_length,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=top_p,
        temperature=temperature,
        do_sample=True
    )

    # Convert the generated text back to a string
    generated_text = [tokenizer.decode(ids, skip_special_tokens=True) for ids in output]

    return generated_text

# Load the trained model and tokenizer
model_path = "danhtran2mind/vi-medical-mt5-finetune-qa"
tokenizer, model, device = load_model_and_tokenizer(model_path)
```

## Inference
```python
# Define the prompt for text generation
prompt = "vaccine covid-19 là gì?"
prompt = word_tokenize(prompt, format='text')

# Generate text with a specific seed
generated_text = generate_text(tokenizer, model, device, prompt,
                              max_length=768,
                              top_p=0.95, temperature=0.7, seed=123)
# Print the generated text
print("Generated Text:\n")
result = generated_text[0].replace("_", " ").replace(" ,", ",").replace(" .", ".")
print(result)
```

## Output
```python
# Generated Text:

# Các vaccine Covid-19 đã được tập trung vào một số nhà khoa học ghi nhận. Trong trường kỳ, các nhân viên y tế sẽ tiếp cận với những người bị nhiễm Covid 19 trong giai đoạn đầu như : AstraZeneca ; Pfizer / BioNTech ) - Sputnik V ngày 19/06/2021 gồm Trung Quốc xác nhân lớn hơn 90.000 6595 cung ứng nguồn dụng chất ở Ấn Độ năm 2012 lên 99.000 lô dân lượng công tác ưu tien rRT-PCR âm trạng lâm Sàng uống chung ăn chín hoang mang lúc đó ít thất là 200.000 lít lọ nên tìm ra ký hoạt tên WHO ? Chỉ dẫn áp dụi việc tái phát cơ bản tác hại của CDC cho cán ộ tuyến bệnh lý ung hư  ( FDA = PHE ” ] Người có biểu huyết dị nguyên ảnh sát vùng dịch covid-19 ≥ 2 % !
```

# Dependencies Enviroment
- Python Vesion: 3.10.12
- List of Libraries:
  ```bassh
    pandas==2.2.3
    numpy==1.26.4
    matplotlib==3.7.5
    scikit-learn==1.2.2
    gensim==4.3.3
    underthesea==6.8.4
    tensorflow==2.17.1
    datasets==3.3.1
    torch==2.5.1+cu121
    transformers==4.47.0
  ```