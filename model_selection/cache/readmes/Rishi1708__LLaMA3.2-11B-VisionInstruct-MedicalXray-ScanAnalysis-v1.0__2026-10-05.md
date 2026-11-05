---
base_model:
- meta-llama/Llama-3.2-11B-Vision-Instruct
---
# LLaMA3.2-11B-VisionInstruct-MedicalXray-ScanAnalysis-v1.0

This model is a fine-tuned version of the Llama-3.2-11B-Vision-Instruct model, specifically adapted for analyzing medical X-ray scans. It has been trained to generate descriptive captions for medical images, aiding in the interpretation and analysis of X-rays, CT scans, and ultrasounds.

## Base Model
The model is based on the [Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) model, a vision-language model capable of understanding and generating text based on both textual and visual inputs. It is loaded with 4-bit quantization to optimize memory usage.

## Fine-Tuning
The model was fine-tuned using Low-Rank Adaptation (LoRA) for parameter-efficient training. LoRA enables training of only a small subset of the model's parameters, enhancing efficiency during the fine-tuning process.

### LoRA Configuration
- Rank (`r`): 16
- Alpha (`lora_alpha`): 16
- Dropout (`lora_dropout`): 0
- Bias: None
- Random State: 3407

### Fine-Tuned Modules
- Vision layers
- Language layers
- Attention modules
- MLP modules

## Dataset
The fine-tuning was performed on a sampled version of the ROCO radiography dataset, available at [unsloth/Radiology_mini](https://huggingface.co/datasets/unsloth/Radiology_mini). This dataset includes:
- Medical images: X-rays, CT scans, and ultrasounds
- Expert-written captions describing the medical conditions and findings in the images

The dataset was selected to provide a diverse set of medical imaging examples for the model to learn from.

## Training Process
The model was fine-tuned using the Hugging Face Transformers library, leveraging the efficiency of LoRA to adapt the pre-trained model to the medical imaging domain. The training process optimized the model to generate accurate and descriptive captions for the provided medical images.

## Usage
To use this model for generating captions for medical images, you can load it using the Hugging Face Transformers library. Below is an example of how to load the model and generate a caption for an image:

```python
from transformers import AutoProcessor, AutoModelForVision2Seq, BitsAndBytesConfig
import torch
from PIL import Image
# Configure 4-bit quantization to reduce memory usage
quantization_config = BitsAndBytesConfig(load_in_4bit=True)
# Load the processor and model from Hugging Face
processor = AutoProcessor.from_pretrained("Rishi1708/LLaMA3.2-11B-VisionInstruct-MedicalXray-ScanAnalysis-v1.0")
model = AutoModelForVision2Seq.from_pretrained(
    "Rishi1708/LLaMA3.2-11B-VisionInstruct-MedicalXray-ScanAnalysis-v1.0",
    quantization_config=quantization_config,
    device_map="auto"
)
# Prepare the input
# Load an X-ray image from a local path (replace with your image path)
image_path = "xray.jpg"
image = Image.open(image_path).convert("RGB")
# Define the text prompt
prompt = "Analyze this X-ray image and describe any abnormalities."
# Process the inputs (text and image) into a format the model expects
inputs = processor(text=prompt, images=image, return_tensors="pt").to("cuda")
# Generate the output
with torch.no_grad():
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        attention_mask=inputs["attention_mask"],
        aspect_ratio_ids=inputs["aspect_ratio_ids"],
        aspect_ratio_mask=inputs["aspect_ratio_mask"],
        max_new_tokens=100,
        do_sample=False  # Set to True for sampling-based generation if needed
    )
# Decode the generated output into readable text
generated_text = processor.decode(outputs[0], skip_special_tokens=True)
# Print the result
print("Model Output:", generated_text)
```

**Note:** The exact method to prepare inputs and generate outputs may depend on the specific model architecture. Please refer to the base model's documentation for detailed usage instructions.

**Dependencies:**
- `transformers`
- `torch`
- `Pillow` (for image handling)
- `bitsandbytes`
- `accelerate`

Install these using:
```bash
pip install transformers torch Pillow bitsandbytes accelerate
```

## Evaluation
To evaluate the model's performance, you can use standard metrics for image captioning tasks, such as BLEU, METEOR, or CIDEr. It is recommended to evaluate the model on a held-out test set from the same dataset or a similar medical imaging dataset.

## Limitations
- The model is fine-tuned on a specific dataset of medical images and may not generalize well to other types of images or medical conditions not represented in the training data.
- The dataset may contain biases inherent to the collection process, which could affect the model's predictions.
- The model should be used as a supplementary tool and not as a replacement for professional medical diagnosis.