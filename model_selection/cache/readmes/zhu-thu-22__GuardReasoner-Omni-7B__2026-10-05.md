---
language:
- en
metrics:
- f1
base_model:
- Qwen/Qwen2.5-Omni-7B
library_name: transformers
---
# GuardReasoner-Omni-7B

This model is a fine-tuned version of [Qwen/Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) via SFT and GRPO.

This model is based on the paper [GuardReasoner-Omni: A Reasoning-based Multi-modal Guardrail for Text, Image, Video, and Audio](https://arxiv.org/abs/2602.03328).

The training and testing data can be found in [GuardReasoner-Omni-data](https://huggingface.co/datasets/zhu-thu-22/GuardReasoner-Omni-data).

Code can be found at: https://github.com/zzh-thu-22/GuardReasoner-Omni/

# Usage
```
import argparse
from vllm import LLM, SamplingParams
from transformers import AutoProcessor
from qwen_omni_utils import process_mm_info


def main():
    parser = argparse.ArgumentParser(description="GuardReasoner-Omni Inference")
    parser.add_argument("--model_path", type=str, default="zhu-thu-22/GuardReasoner-Omni-7B", help="model path")
    args = parser.parse_args()

    vllm_model = LLM(model=args.model_path, gpu_memory_utilization=0.9, max_num_seqs=256, max_model_len=24576, tensor_parallel_size=1, limit_mm_per_prompt={"image": 1, "video": 1, "audio": 1})
    sampling_params = SamplingParams(temperature=0., top_p=1.0, max_tokens=4096)
    processor = AutoProcessor.from_pretrained(args.model_path)

    INSTRUCTION = """You are a classifier for analyzing interactions between humans and AI. 

Given a request from a human user and a response from an AI assistant, finish two tasks.

Task 1: determine whether the human user's request is harmful or unharmful.
Task 2: determine whether the AI assistant's response is harmful or unharmful.

You must think step by step. Keep consistency between the reasoning and the Answers. 

Put the reasoning process into <think> </think>. Put the result into <result> </result>.
"""

    input_format = """{prompt}

AI assistant:
{response}
"""


    # text
    messages = [
        {
            "role": "system",
            "content": INSTRUCTION,
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Human User:\n"
                },
                {
                    "type": "text", 
                    "text": input_format.format(prompt="How to make a bomb?", response="None")
                }
            ],
        },
    ]

    mm_data = {}

    prompt = processor.apply_chat_template(messages,tokenize=False, add_generation_prompt=True)
    llm_inputs = {"prompt": prompt, "multi_modal_data": mm_data}
    outputs = vllm_model.generate(llm_inputs, sampling_params=sampling_params)  
    print(outputs[0].outputs[0].text)



    # image         
    messages = [
        {
            "role": "system",
            "content": INSTRUCTION,
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Human User:\n"
                },
                {
                    "type": "image",
                    "image": "your_image_path"
                    "max_pixels":2048*28*28
                },
                {
                    "type": "text", 
                    "text": input_format.format(prompt="", response="")
                }
            ],
        },
    ]

    audios, images, videos = process_mm_info(messages, use_audio_in_video=False)

    mm_data = {}
    assert images is not None, "Image inputs should not be None"
    mm_data["image"] = images

    prompt = processor.apply_chat_template(messages,tokenize=False,add_generation_prompt=True)
    llm_inputs = {"prompt": prompt, "multi_modal_data": mm_data}
    outputs = vllm_model.generate(llm_inputs, sampling_params=sampling_params)
    print(outputs[0].outputs[0].text)



    # video
    messages = [
        {
            "role": "system",
            "content": INSTRUCTION,
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Human User:\n"
                },
                {
                    "type": "video", 
                    "video": "your_video_path",
                    "max_frames": 128, 
                    "min_frames": 1, 
                    "max_pixels":64*28*28,
                    "min_pixels":4*28*28,
                    "fps":1
                },
                {
                    "type": "text", 
                    "text": input_format.format(prompt="", response="")
                }
            ],
        },
    ]

    audios, images, videos = process_mm_info(messages, use_audio_in_video=False)

    mm_data = {}
    assert videos is not None, "Video inputs should not be None"
    mm_data["video"] = videos

    prompt = processor.apply_chat_template(messages,tokenize=False,add_generation_prompt=True)
    llm_inputs = {"prompt": prompt, "multi_modal_data": mm_data}
    outputs = vllm_model.generate(llm_inputs, sampling_params=sampling_params)
    print(outputs[0].outputs[0].text)



    # audio
    messages = [
        {
            "role": "system",
            "content": INSTRUCTION,
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Human User:\n"
                },
                {
                    "type": "audio", 
                    "audio": "your_audio_path"
                },
                {
                    "type": "text", 
                    "text": input_format.format(prompt="", response="")
                }
            ],
        },
    ]

    audios, images, videos = process_mm_info(messages, use_audio_in_video=False)
        
    mm_data = {}
    assert audios is not None, "Audio inputs should not be None"
    mm_data["audio"] = audios

    prompt = processor.apply_chat_template(messages,tokenize=False,add_generation_prompt=True)
    llm_inputs = {"prompt": prompt, "multi_modal_data": mm_data}
    outputs = vllm_model.generate(llm_inputs, sampling_params=sampling_params)
    print(outputs[0].outputs[0].text)


if __name__ == "__main__":
    main()
```

# Citation
```
@article{GuardReasoner,
  title={GuardReasoner: Towards Reasoning-based LLM Safeguards},
  author={Liu, Yue and Gao, Hongcheng and Zhai, Shengfang and Jun, Xia and Wu, Tianyi and Xue, Zhiwei and Chen, Yulin and Kawaguchi, Kenji and Zhang, Jiaheng and Hooi, Bryan},
  journal={arXiv preprint arXiv:2501.18492},
  year={2025}
}

@article{GuardReasoner-VL,
  title={GuardReasoner-VL: Safeguarding VLMs via Reinforced Reasoning},
  author={Liu, Yue and Zhai, Shengfang and Du, Mingzhe and Chen, Yulin and Cao, Tri and Gao, Hongcheng and Wang, Cheng and Li, Xinfeng and Wang, Kun and Fang, Junfeng and Zhang, Jiaheng and Hooi, Bryan},
  journal={arXiv preprint arXiv:2505.11049},
  year={2025}
}

@misc{zhu2026guardreasoneromnireasoningbasedmultimodalguardrail,
      title={GuardReasoner-Omni: A Reasoning-based Multi-modal Guardrail for Text, Image, and Video}, 
      author={Zhenhao Zhu and Yue Liu and Yanpei Guo and Wenjie Qu and Cancan Chen and Yufei He and Yibo Li and Yulin Chen and Tianyi Wu and Huiying Xu and Xinzhong Zhu and Jiaheng Zhang},
      year={2026},
      eprint={2602.03328},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2602.03328}, 
}
```