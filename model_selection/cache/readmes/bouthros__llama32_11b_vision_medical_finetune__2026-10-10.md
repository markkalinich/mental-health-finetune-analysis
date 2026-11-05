---
library_name: peft
base_model:
- unsloth/Llama-3.2-11B-Vision-Instruct
datasets:
- eltorio/ROCOv2-radiology
---

# Model Card for Llama-3.2 11b Vision Medical

<img src="https://i5.walmartimages.com/seo/DolliBu-Beige-Llama-Doctor-Plush-Toy-Super-Soft-Stuffed-Animal-Dress-Up-Cute-Scrub-Uniform-Cap-Outfit-Fluffy-Gift-11-Inches_e78392b2-71ef-4e26-a23f-8bb0b0e2043a.70c3b5988d390cf43d799758a826f2a5.jpeg" alt="drawing" width="400"/>

<font color="FF0000" size="5"><b>
This is a vision-language model fine-tuned for radiographic image analysis</b></font>
<br><b>Foundation Model: https://huggingface.co/unsloth/Llama-3.2-11B-Vision-Instruct<br/>
Dataset: https://huggingface.co/datasets/eltorio/ROCOv2-radiology<br/></b>

The model has been fine-tuned using CUDA-enabled GPU hardware.

## Model Details

The model is based upon the foundation model: unsloth/Llama-3.2-11B-Vision-Instruct.<br/>
It has been tuned with Supervised Fine-tuning Trainer and PEFT LoRA with vision-language capabilities.

### Libraries
- unsloth
- transformers
- torch
- datasets
- trl
- peft

## Bias, Risks, and Limitations

To optimize training efficiency, the model has been trained on a subset of the ROCOv2-radiology dataset (1/7th of the total dataset).<br/>

<font color="FF0000">
Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.<br/>
The model's performance is directly dependent on the quality and diversity of the training data. Medical diagnosis should always be performed by qualified healthcare professionals.<br/>
Generation of plausible yet incorrect medical interpretations could occur and should not be used as the sole basis for clinical decisions.
</font>

## Training Details

### Training Parameters
- per_device_train_batch_size = 2
- gradient_accumulation_steps = 16
- num_train_epochs = 3
- learning_rate = 5e-5
- weight_decay = 0.02
- lr_scheduler_type = "linear"
- max_seq_length = 2048

### LoRA Configuration
- r = 32
- lora_alpha = 32
- lora_dropout = 0
- bias = "none"

### Hardware Requirements
The model was trained using CUDA-enabled GPU hardware.

### Training Statistics
- Training duration: 40,989 seconds (approximately 683 minutes)
- Peak reserved memory: 12.8 GB
- Peak reserved memory for training: 3.975 GB
- Peak reserved memory % of max memory: 32.3%
- Peak reserved memory for training % of max memory: 10.1%

### Training Data
The model was trained on the ROCOv2-radiology dataset, which contains radiographic images and their corresponding medical descriptions. .

The training set was reduced to 1/7th of the original size for computational efficiency.

## Usage

The model is designed to provide detailed descriptions of radiographic images. It can be prompted with:
```python
instruction = "You are an expert radiographer. Describe accurately what you see in this image."
```

## Model Access

The model is available on Hugging Face Hub at: bouthros/llma32_11b_vision_medical

## Citation

If you use this model, please cite the original ROCOv2-radiology dataset and the Llama-3.2-11B-Vision-Instruct base model.