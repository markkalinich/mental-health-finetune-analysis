---
datasets:
- scta/scta-htr-training-data
base_model:
- Qwen/Qwen2-VL-2B-Instruct
---

```python
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info


device = "cuda" if torch.cuda.is_available() else "cpu"

model_dir = "medieval-data/qwen2-vl-2b-scta"



model = Qwen2VLForConditionalGeneration.from_pretrained(
    model_dir, torch_dtype="auto", device_map="auto"
)

processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")
image_url ="""https://loris2.scta.info/lon/L28v.jpg/full/full/0/default.jpg"""
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": image_url,
            },
            {"type": "text", "text": "Convert this image to text."},
        ],
    }
]

# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to(device)

# Inference: Generation of the output
generated_ids = model.generate(**inputs, max_new_tokens=4000)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)

print(output_text)
# Import required libraries if not already imported
from IPython.display import display, Image

# Display the output text
print(output_text)

# Display the image
display(Image(url=image_url))
```
