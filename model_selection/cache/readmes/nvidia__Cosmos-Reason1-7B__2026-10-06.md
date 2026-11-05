---
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license
datasets:
- nvidia/Cosmos-Reason1-SFT-Dataset
- nvidia/Cosmos-Reason1-RL-Dataset
- nvidia/Cosmos-Reason1-Benchmark
library_name: transformers
language:
- en
base_model:
- Qwen/Qwen2.5-VL-7B-Instruct
tags:
- nvidia
- cosmos
pipeline_tag: image-text-to-text
---

# **Cosmos-Reason1: Physical AI Common Sense and Embodied Reasoning Models**

[**Cosmos**](https://huggingface.co/collections/nvidia/cosmos-reason1-67c9e926206426008f1da1b7) | [**Code**](https://github.com/nvidia-cosmos/cosmos-reason1) | [**Paper**](https://arxiv.org/abs/2503.15558) | [**Paper Website**](https://research.nvidia.com/labs/dir/cosmos-reason1)

# Model Overview

## Description:

NVIDIA Cosmos Reason – an open, customizable, 7B-parameter reasoning vision language model (VLM) for physical AI and robotics - enables robots and vision AI agents to reason like humans, using prior knowledge, physics understanding and common sense to understand and act in the real world. This model understands space, time, and fundamental physics, and can serve as a planning model to reason what steps an embodied agent might take next.

Cosmos Reason excels at navigating the long tail of diverse scenarios of the physical world with spatial-temporal understanding. Cosmos Reason is post-trained with physical common sense and embodied reasoning data with supervised fine-tuning and reinforcement learning. It uses chain-of-thought reasoning capabilities to understand world dynamics without human annotations.

Given a video/image and a text prompt, the model first converts the video/image into tokens using a vision encoder and a special translator called a projector. These video tokens are combined with the text prompt and fed into the core model, which uses a mix of LLM modules and techniques. This enables the model to think step-by-step and provide detailed, logical responses.

Cosmos Reason can be used for robotics and physical AI applications including:
- Data curation and annotation — Enable developers to automate high-quality curation and annotation of massive, diverse training datasets.
- Robot planning and reasoning — Act as the brain for deliberate, methodical decision-making in a robot vision language action (VLA) model. Now robots such as humanoids and autonomous vehicles can interpret environments and given complex commands, break them down into tasks and execute them using common sense, even in unfamiliar environments.
- Video analytics AI agents — Extract valuable insights and perform root-cause analysis on massive volumes of video data. These agents can be used to analyze and understand recorded or live video streams across city and industrial operations.

The model is ready for commercial use.

**Model Developer**: NVIDIA

## Model Versions

The Cosmos-Reason1 includes the following model:

- [Cosmos-Reason1-7B](https://huggingface.co/nvidia/Cosmos-Reason1-7B): Given a text prompt and an input video, think and generate the answer with respect to the input text prompt and video.

### License:

This model is released under the  [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license). Additional Information: [Apache License 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).

For a custom license, please contact [cosmos-license@nvidia.com](mailto:cosmos-license@nvidia.com).

Under the NVIDIA Open Model License, NVIDIA confirms:

* Models are commercially usable.
* You are free to create and distribute Derivative Models.
* NVIDIA does not claim ownership to any outputs generated using the Models or Derivative Models.

**Important Note**: If You bypass, disable, reduce the efficacy of, or circumvent any technical limitation, safety guardrail or associated safety guardrail hyperparameter, encryption, security, digital rights management, or authentication mechanism (collectively “Guardrail”) contained in the Model without a substantially similar Guardrail appropriate for your use case, your rights under this Agreement [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license) will automatically terminate.

### Deployment Geography:

Global

### Use Case:

Physical AI: Space, time, fundamental physics understanding and embodied reasoning, encompassing robotics, and autonomous vehicles (AV).

### Release Date:

* Github: [05/17/2025](https://github.com/nvidia-cosmos/cosmos-reason1)
* Huggingface:
  * [08/01/2025](https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/0caf724f837efea5e25bf6d5818dcdeec0a36604). Shipped a few improvements which include captions with temporal timestamp, Set of Mark prompting.
  * [06/10/2025](https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/2464fff43c5c0bfb1916ac8c009feda4aed81be9). Enhanced critic capability for physical plausibility.
  * [05/17/2025](https://huggingface.co/nvidia/Cosmos-Reason1-7B/commit/098a5bb62a1f4fc05e5c4ac89aae8005e301aa18). Initial release.

## Model Architecture:

Architecture Type: A Multi-modal LLM consists of a Vision Transformer (ViT) for vision encoder and a Dense Transformer model for LLM.
Network Architecture: Qwen2.5-VL-7B-Instruct.

Cosmos-Reason-7B is post-trained based on [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) and follows the same model architecture.


**Number of model parameters:**

Cosmos-Reason1-7B:<br>
  * Vision Transformer (ViT): 675.76M (675,759,104)
  * Language Model (LLM): 7.07B (7,070,619,136)
  * Other components (output projection layer): 545.00M (544,997,376)


## Input

  **Input Type(s)**: Text+Video/Image

   **Input Format(s)**:
   * Text: String
   * Video: mp4
   * Image: jpg

  **Input Parameters**:
  * Text: One-dimensional (1D)
  * Video: Three-dimensional (3D)
  * Image: Two-dimensional (2D)
  
  **Other Properties Related to Input**:
  * Use `FPS=4` for input video to match the training setup.
  * Append `Answer the question in the following format: <think>\nyour reasoning\n</think>\n\n<answer>\nyour answer\n</answer>.` in the system prompt to encourage long chain-of-thought reasoning response.

## Output

 **Output Type(s)**: Text

 **Output Format**: String

 **Output Parameters**: Text: One-dimensional (1D)

 **Other Properties Related to Output**:
 * Recommend using 4096 or more output max tokens to avoid truncation of long chain-of-thought response.

 * Our AI model recognizes timestamps added at the bottom of each frame for accurate temporal localization.

 * Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>


## Software Integration

**Runtime Engine(s):**

* [vLLM](https://github.com/vllm-project/vllm)

**Supported Hardware Microarchitecture Compatibility:**

* NVIDIA Blackwell
* NVIDIA Hopper

**Note**: We have only tested doing inference with BF16 precision.

**Operating System(s):**

* Linux (We have not tested on other operating systems.)


# Usage

See [Cosmos-Reason1](https://github.com/nvidia-cosmos/cosmos-reason1) for details.
* Post Training: [Cosmos-Reason1](https://github.com/nvidia-cosmos/cosmos-reason1) provides examples of supervised fine-tuning and reinforcement learning on embodied reasoning datasets.

## Training and Evaluation Sections:
### 05/17/2025
Please see our [technical paper](https://arxiv.org/pdf/2503.15558) for detailed evaluations on physical common sense and embodied reasoning. Part of the evaluation datasets are released under [Cosmos-Reason1-Benchmark](https://huggingface.co/datasets/nvidia/Cosmos-Reason1-Benchmark). The embodied reasoning datasets and benchmarks focus on the following areas: robotics (RoboVQA, BridgeDataV2, Agibot, RobFail), ego-centric human demonstration (HoloAssist), and Autonomous Vehicle (AV) driving video data. The AV dataset is collected and annotated by NVIDIA.

All datasets go through the data annotation process described in the technical paper to prepare training and evaluation data and annotations.

### 08/01/2025
We enhance the model capability with the augmented training data. PLM-Video-Human and Nexar are used to enable dense temporal captioning. Describe Anything is added to enhance a set of mark (SoM) prompting. We enrich data in intelligent transportation systems (ITS) and warehouse applications. Lastly, Visual Critics dataset contains a collection of AI generated videos from Cosmos-Predict2 and Wan2.1 with human annotations to describe the physical correctness in AI videos.


## Training Datasets:

**Data Collection Method**:
* RoboVQA:  Hybrid:  Automatic/Sensors
* BridgeDataV2: Automatic/Sensors
* AgiBot: Automatic/Sensors
* RoboFail: Automatic/Sensors
* HoloAssist: Human
* AV: Automatic/Sensors
* PLM-Video-Human: Human
* Nexar: Automatic/Sensors
* Describe Anything: Human
* ITS / Warehouse: Human, Automatic
* Visual Critics: Automatic

**Labeling Method**:
* RoboVQA:  Hybrid:  Human,Automated
* BridgeDataV2: Hybrid:  Human,Automated
* AgiBot: Hybrid:  Human,Automated
* RoboFail: Hybrid:  Human,Automated
* HoloAssist: Hybrid:  Human,Automated
* AV: Hybrid:  Human,Automated
* PLM-Video-Human: Human,Automated
* Nexar: Human
* Describe Anything: Human,Automated
* ITS / Warehouse: Human, Automated
* Visual Critics: Human,Automated


# Evaluation Datasets:

**Data Collection Method**:
* RoboVQA:  Hybrid:  Automatic/Sensors
* BridgeDataV2: Automatic/Sensors
* AgiBot: Automatic/Sensors
* RoboFail: Automatic/Sensors
* HoloAssist: Human
* AV: Automatic/Sensors


**Labeling Method**:
* RoboVQA:  Hybrid:  Human,Automated
* BridgeDataV2: Hybrid:  Human,Automated
* AgiBot: Hybrid:  Human,Automated
* RoboFail: Hybrid:  Human,Automated
* HoloAssist: Hybrid:  Human,Automated
* AV: Hybrid:  Human,Automated


**Metrics**:
We report the model accuracy on the embodied reasoning benchmark introduced in [Cosmos-Reason1](https://arxiv.org/abs/2503.15558). The results differ from those presented in Table 9 due to additional training aimed at supporting a broader range of Physical AI tasks beyond the benchmark.
|                   | [RoboVQA](https://robovqa.github.io/)        | AV       | [BridgeDataV2](https://rail-berkeley.github.io/bridgedata/)| [Agibot](https://github.com/OpenDriveLab/AgiBot-World)| [HoloAssist](https://holoassist.github.io/)       | [RoboFail](https://robot-reflect.github.io/)                               | Average |
|--------------------|---------------------------------------------|----------|------------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| **Accuracy**        | 87.3                                        | 70.8    | 63.7                                                 | 48.9                                          | 62.7                                           | 57.2                                            |  65.1                                          |

## Dataset Format
Modality: Video (mp4) and Text

## Dataset Quantification
### 05/17/2025
We release the embodied reasoning data and benchmarks. Each data sample is a pair of video and text. The text annotations include understanding and reasoning annotations described in the Cosmos-Reason1 paper. Each video may have multiple text annotations. The quantity of the video and text pairs is described in the table below.
**The AV data is currently unavailable and will be uploaded soon!**

|                   | [RoboVQA](https://robovqa.github.io/)        | AV       | [BridgeDataV2](https://rail-berkeley.github.io/bridgedata/)| [Agibot](https://github.com/OpenDriveLab/AgiBot-World)| [HoloAssist](https://holoassist.github.io/)       | [RoboFail](https://robot-reflect.github.io/)                               | Total Storage Size |
|--------------------|---------------------------------------------|----------|------------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|--------------------|
| **SFT Data**        | 1.14m                                        | 24.7k    | 258k                                                 | 38.9k                                          | 273k                                           | N/A                                            | **300.6GB**         |
| **RL Data**         | 252                                          | 200      | 240                                                  | 200                                            | 200                                            | N/A                                            | **2.6GB**           |
| **Benchmark Data**  | 110                                          | 100      | 100                                                  | 100                                            | 100                                            | 100                                            | **1.5GB**           |

We release text annotations for all embodied reasoning datasets and videos for RoboVQA and AV datasets. For other datasets, users may download the source videos from the original data source and find corresponding video sources via the video names. The held-out RoboFail benchmark is released for measuring the generalization capability.

### 08/01/2025
|                   | [PLM-Video-Human](https://huggingface.co/datasets/facebook/PLM-Video-Human) | Nexar       | [Describe Anything](https://huggingface.co/datasets/nvidia/describe-anything-dataset)| [ITS / Warehouse]       | Visual Critics                             | Total Storage Size |
|------------------ |-----------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------|-------------------------|--------------------------------------------|--------------------|
| **SFT Data**      | 39k                                                                         | 240k        | 178k                                                                                 | 24k                     | 24k                                        | **2.6TB**          |



## Inference:
**Test Hardware:** H100, A100, GB200 <br>
> [!NOTE]
> We suggest using `fps=4` for the input video and `max_tokens=4096` to avoid truncated response.
```python
from transformers import AutoProcessor
from vllm import LLM, SamplingParams
from qwen_vl_utils import process_vision_info

# You can also replace the MODEL_PATH by a safetensors folder path mentioned above
MODEL_PATH = "nvidia/Cosmos-Reason1-7B"

llm = LLM(
    model=MODEL_PATH,
    limit_mm_per_prompt={"image": 10, "video": 10},
)

sampling_params = SamplingParams(
    temperature=0.6,
    top_p=0.95,
    repetition_penalty=1.05,
    max_tokens=4096,
)

video_messages = [
    {"role": "system", "content": "You are a helpful assistant. Answer the question in the following format: <think>\nyour reasoning\n</think>\n\n<answer>\nyour answer\n</answer>."},
    {"role": "user", "content": [
            {"type": "text", "text": (
                    "Is it safe to turn right?"
                )
            },
            {
                "type": "video", 
                "video": "file:///path/to/your/video.mp4",
                "fps": 4,
            }
        ]
    },
]

# Here we use video messages as a demonstration
messages = video_messages

processor = AutoProcessor.from_pretrained(MODEL_PATH)
prompt = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)

mm_data = {}
if image_inputs is not None:
    mm_data["image"] = image_inputs
if video_inputs is not None:
    mm_data["video"] = video_inputs

llm_inputs = {
    "prompt": prompt,
    "multi_modal_data": mm_data,

    # FPS will be returned in video_kwargs
    "mm_processor_kwargs": video_kwargs,
}

outputs = llm.generate([llm_inputs], sampling_params=sampling_params)
generated_text = outputs[0].outputs[0].text

print(generated_text)
```


## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

For more detailed information on ethical considerations for this model, please see the subcards of Explainability, Bias, Safety & Security, and Privacy below. 

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

### Plus Plus (++) Promise

We value you, the datasets, the diversity they represent, and what we have been entrusted with. This model and its associated data have been:

* Verified to comply with current applicable disclosure laws, regulations, and industry standards.
* Verified to comply with applicable privacy labeling requirements.
* Annotated to describe the collector/source (NVIDIA or a third-party).
* Characterized for technical limitations.
* Reviewed to ensure proper disclosure is accessible to, maintained for, and in compliance with NVIDIA data subjects and their requests.
* Reviewed before release.
* Tagged for known restrictions and potential safety implications.

### Bias

| Field                                                                                                                                                            | Response |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing: | None     |
| Measures taken to mitigate against unwanted bias:                                                                                                                | The training video sources contain multiple physical embodiments and environments including human, car, single arm robot, bimanual robot in indoor and outdoor environments. By training on numerous and various physical interactions and curated datasets, we strive to provide a model that does not possess biases towards certain embodiments or environments.   |

### Explainability

| Field                                                     | Response                                                                                                             |
| :-------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| Intended Application & Domain:                            | Physical AI Reasoning                                                                                                |
| Model Type:                                               | Transformer                                                                                                          |
| Intended Users:                                           | Physical AI developers                                                                                               |
| Output:                                                   | Text                                                                                                                 |
| Describe how the model works:                             | Given a video/image and a text prompt, the model first converts the video/image into tokens using a vision encoder and a special translator called a projector. These video tokens are combined with the text prompt and fed into the core model, which uses a mix of LLM modules and techniques. This enables the model to think step-by-step and provide detailed, logical responses.                                                         |
| Technical Limitations:                                    | The model may not follow the video or text input accurately in challenging cases, where the input video shows complex scene composition and temporal dynamics. Examples of challenging scenes include: fast camera movements, overlapping human-object interactions, low lighting with high motion blur, and multiple people performing different actions simultaneously.  |
| Verified to have met prescribed NVIDIA quality standards: | Yes                                                                                                                  |
| Performance Metrics:                                      | Quantitative and Qualitative Evaluation. Cosmos-Reason1 proposes the embodied reasoning benchmark and physical common sense benchmark to evaluate accuracy with visual question answering.                                                                              |
| Potential Known Risks:                                    | The model's output can generate all forms of texts, including what may be considered toxic, offensive, or indecent.  |
| Licensing:                                                | [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license). Additional Information: [Apache License 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).   |

### Privacy

| Field                                                               | Response       |
| :------------------------------------------------------------------ | :------------- |
| Generatable or reverse engineerable personal information?           | None Known     |
| Protected class data used to create this model?                     | None Known     |
| Was consent obtained for any personal data used?                    | None Known     |
| How often is dataset reviewed?                                      | Before Release |
| Is there provenance for all datasets used in training?              | Yes            |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes            |
| Applicable Privacy Policy | [NVIDIA Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy)            |


### Safety

| Field                                           | Response                                                                                                                                                                                                                                                                                                                             |
| :---------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model Application(s):                           | Physical AI common sense understanding and embodied reasoning                                                                                                                                                                                                                                                                                                                     |
| Describe the life critical impact (if present). | None Known                                                                                                                                                                                                                                                                                                                           |
| Use Case Restrictions:                          | [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license). Additional Information: [Apache License 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).                                                                                                                                                                                                                   |
| Model and dataset restrictions:                 | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to. Model checkpoints are made available on Hugging Face, and may become available on cloud providers' model catalog. |