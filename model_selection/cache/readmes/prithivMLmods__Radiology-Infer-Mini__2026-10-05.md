---
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen2-VL-2B-Instruct
pipeline_tag: image-text-to-text
library_name: transformers
tags:
- Radiology
- Infer
- Qwen2
- 2B
---
![3.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/lLU2lEv76EIL3aNeMHy0Q.png)

# **Radiology-Infer-Mini**

Radiology-Infer-Mini is a vision-language model fine-tuned from the Qwen2-VL-2B framework, specifically designed to excel in radiological analysis, text extraction, and medical report generation. It integrates advanced multi-modal capabilities with domain-specific expertise, ensuring accurate and efficient processing of radiology-related tasks.

### Key Enhancements:

1. **State-of-the-Art Understanding of Medical Images**  
   Radiology-Infer-Mini achieves cutting-edge performance in interpreting complex medical imagery, including X-rays, MRIs, CT scans, and ultrasounds. It is fine-tuned on healthcare-specific benchmarks to ensure precise recognition of anatomical and pathological features.

2. **Support for Extended Medical Reports and Cases**  
   Capable of processing and analyzing extensive radiology case studies, Radiology-Infer-Mini can generate high-quality diagnostic reports and answer complex medical queries with detailed explanations. Its proficiency extends to multi-page radiology documents, ensuring comprehensive visual and textual understanding.

3. **Integration with Medical Devices**  
   With robust reasoning and decision-making capabilities, Radiology-Infer-Mini can seamlessly integrate with medical imaging systems and robotic platforms. It supports automated workflows for tasks such as diagnosis support, triaging, and clinical decision-making.

4. **Math and Diagram Interpretation**  
   Equipped with LaTeX support and advanced diagram interpretation capabilities, Radiology-Infer-Mini handles mathematical annotations, statistical data, and visual charts present in medical reports with precision.

5. **Multilingual Support for Medical Text**  
   Radiology-Infer-Mini supports the extraction and interpretation of multilingual texts embedded in radiological images, including English, Chinese, Arabic, Korean, Japanese, and most European languages. This feature ensures accessibility for a diverse global healthcare audience.

Radiology-Infer-Mini represents a transformative step in radiology-focused AI, enhancing productivity and accuracy in medical imaging and reporting.

![radiology.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/S0JuOoKkXmXgj4li6a9OZ.png)

### How to Use

```python
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

# default: Load the model on the available device(s)
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "prithivMLmods/Radiology-Infer-Mini", torch_dtype="auto", device_map="auto"
)

# We recommend enabling flash_attention_2 for better acceleration and memory saving, especially in multi-image and video scenarios.
# model = Qwen2VLForConditionalGeneration.from_pretrained(
#     "prithivMLmods/Radiology-Infer-Mini",
#     torch_dtype=torch.bfloat16,
#     attn_implementation="flash_attention_2",
#     device_map="auto",
# )

# default processer
processor = AutoProcessor.from_pretrained("prithivMLmods/Radiology-Infer-Mini")

# The default range for the number of visual tokens per image in the model is 4-16384. You can set min_pixels and max_pixels according to your needs, such as a token count range of 256-1280, to balance speed and memory usage.
# min_pixels = 256*28*28
# max_pixels = 1280*28*28
# processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
            },
            {"type": "text", "text": "Describe this image."},
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
inputs = inputs.to("cuda")

# Inference: Generation of the output
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```
### Buf
```python
    buffer = ""
    for new_text in streamer:
        buffer += new_text
        # Remove <|im_end|> or similar tokens from the output
        buffer = buffer.replace("<|im_end|>", "")
        yield buffer
```
### **Intended Use**  

**Radiology-Infer-Mini** is designed to support healthcare professionals and researchers in tasks involving medical imaging and radiological analysis. Its primary applications include:  

1. **Diagnostic Support**  
   - Analyze medical images (X-rays, MRIs, CT scans, ultrasounds) to identify abnormalities, annotate findings, and assist radiologists in forming diagnostic conclusions.  

2. **Medical Report Generation**  
   - Automatically generate structured radiology reports from image data, reducing documentation time and improving workflow efficiency.  

3. **Educational and Research Tools**  
   - Serve as a teaching aid for radiology students and support researchers in large-scale studies by automating image labeling and data extraction.  

4. **Workflow Automation**  
   - Integrate with medical devices and hospital systems to automate triaging, anomaly detection, and report routing in clinical settings.  

5. **Multi-modal Applications**  
   - Handle complex tasks involving both images and text, such as extracting patient data from images and synthesizing text-based findings with visual interpretations.  

6. **Global Accessibility**  
   - Support multilingual radiological text understanding for use in diverse healthcare settings around the world.  

### **Limitations**  

While **Radiology-Infer-Mini** offers advanced capabilities, it has the following limitations:  

1. **Medical Expertise Dependency**  
   - The model provides supplementary insights but cannot replace the expertise and judgment of a licensed radiologist or clinician.  

2. **Data Bias**  
   - Performance may vary based on the training data, which might not fully represent all imaging modalities, patient demographics, or rare conditions.  

3. **Edge Cases**  
   - Limited ability to handle edge cases, highly complex images, or uncommon medical scenarios that were underrepresented in its training dataset.  

4. **Regulatory Compliance**  
   - It must be validated for compliance with local medical regulations and standards before clinical use.  

5. **Interpretation Challenges**  
   - The model may misinterpret artifacts, noise, or low-quality images, leading to inaccurate conclusions in certain scenarios.  

6. **Multimodal Integration**  
   - While capable of handling both visual and textual inputs, tasks requiring deep contextual understanding across different modalities might yield inconsistent results.  

7. **Real-Time Limitations**  
   - Processing speed and accuracy might be constrained in real-time or high-throughput scenarios, especially on hardware with limited computational resources.  

8. **Privacy and Security**  
   - Radiology-Infer-Mini must be used in secure environments to ensure the confidentiality and integrity of sensitive medical data.