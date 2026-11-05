---
tags:
- 4th gen xeon
---
datasets:
  - qiaojin/PubMedQA
  - kroshan/BioASQ
language:
  - en
library_name: transformers
pipeline_tag: table-question-answering
tags:
  - chemistry
  - biology
  - molecular
  - synthetic
  - language model
Description:
This model is an example of how a fine-tuned LLM even without the full depth, size, and complexity of larger and more expensive models can be useful in context-sensitive situations. In our use-case, we are applying this LLM as part of a broader electronic lab notebook software setup for molecular and computational biologists. This GPT-2 has been finetuned on datasets from BioASQ and PubMedQA and is now knowledgeable enough in biochemistry to assist scientists and integrates as not just a copilot-like tool but also as a lab partner to the overall Design-Built-Test-Learn workflow ever growing in prominence in synthetic biology.

Intel Optimization Inference Code Sample:
We made use of both the BF16 datatype and INT8 quantization to improve performance. BF16 halves the memory compared to FP32, allowing larger models and/or larger batches to fit into memory. Moreover, BF16 is supported by modern Intel CPUs and operations with it are optimized. Quantizing models to INT8 can reduce the model size, making better use of cache and speeding up load times. Additionally, we then optimized further with OpenVino to make it run better on Intel Hardware by converting it to an onxx model to then OpenVINO Intermediate Representation

from openvino.runtime import Core
import numpy as np

# Initialize the OpenVINO runtime Core
ie = Core()

# Load and compile the model for the CPU device
compiled_model = ie.compile_model(model='../ovc_output/converted_model.xml', device_name="CPU")

# Prepare input: a non tokenized example just for examples sake
input_ids = np.random.randint(0, 50256, (1, 10))

# Create a dictionary for the inputs expected by the model
inputs = {"input_ids": input_ids}

# Create an infer request and start synchronous inference
result = compiled_model.create_infer_request().infer(inputs=inputs)

# Access output tensor data directly from the result using the appropriate output key
output = result['outputs']

print("Inference results:", output)
In the finetuning file you will see our other optimizations.

We perform BF16 conversion as follows (we also implement a custom collator):

model = GPT2LMHeadModel.from_pretrained('gpt2-medium').to(torch.bfloat16)
We perform Int8 quantization as follows:

# Load the full-precision model
model.eval()  # Ensure the model is in evaluation mode
quantized_model = quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)