---
datasets:
- CATMuS/medieval
base_model:
- Qwen/Qwen2-VL-2B-Instruct
---
```python
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info


device = "cuda" if torch.cuda.is_available() else "cpu"

model_dir = "medieval-data/qwen2-vl-2b-catmus"



model = Qwen2VLForConditionalGeneration.from_pretrained(
    model_dir, torch_dtype="auto", device_map="auto"
)

processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")
image_url ="""https://datasets-server.huggingface.co/cached-assets/CATMuS/medieval/--/76c4e4124476cced0b7b487421313450cf646ce8/--/default/test/851/im/image.jpg?Expires=1726188562&Signature=rdeGLGZfuXA0e93VngajlOGZ~4RUz3W6HYe84u27vHd~X502-O0gDiT8y39mJeYyUyQOf9wXs~mlXDaT8ugP62f4gcKEEaqikBHhhbIFHYgCy48NKzJXx4bPRCND1T6JrBotOfY3LUy6XP7PNcv7e5cAXQPeGoEHH4VcU6Bt~~mLg~oD2qYzKwKQ7PcFmIYAk-4igi0MZNUuScw6dpCe9CY2aCgvJeGb3ZZySbb~9Tn7ij7p7ouG2DMVurKCsm8tMIwLrzAAv2UEl4WE0aSVFk9Rm-zPiH3qRwzElLi7FNn6BzRYmm9WPW6wuRdTGweJxDrPjBi3Roy3B~jqk4hryg__&Key-Pair-Id=K3EI6M078Z3AC3"""
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