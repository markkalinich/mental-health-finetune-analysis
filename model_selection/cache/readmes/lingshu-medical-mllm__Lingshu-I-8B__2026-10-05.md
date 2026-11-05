---
license: mit
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- medical
- multimodal
- report generation
- radiology
- clinical-reasoning
- MRI
- CT
- Histopathology
- X-ray
- Fundus
---

<p align="center">
  <img src="lingshu_logo.png" width="200" />
</p>
<p align="center">
<a href="https://alibaba-damo-academy.github.io/lingshu/" target="_blank" rel="noopener">Website</a>
&nbsp;&nbsp;
<a href="https://huggingface.co/lingshu-medical-mllm/Lingshu-7B" target="_blank" rel="noopener"> 🤖 7B Model</a>
&nbsp;&nbsp;
  <a href="https://huggingface.co/lingshu-medical-mllm/Lingshu-I-8B" target="_blank" rel="noopener"> 🤖 8B Model based on InternVL3</a>
&nbsp;&nbsp;
<a href="https://huggingface.co/lingshu-medical-mllm/Lingshu-32B" target="_blank" rel="noopener"> 🤖 32B Model</a>
&nbsp;&nbsp;
<a href="https://github.com/alibaba-damo-academy/MedEvalKit" target="_blank" rel="noopener"> MedEvalKit </a>
&nbsp;&nbsp;
<a href="https://arxiv.org/abs/2506.07044" target="_blank" rel="noopener">Technical Report</a>
&nbsp;&nbsp;
<a href="https://github.com/alibaba-damo-academy/Lingshu_MCP" target="_blank" rel="noopener">Lingshu MCP</a>
</p>

# *Lingshu* - SOTA Multimodal Large Language Models for Medical Domain


# <strong style="color: red">BIG NEWS: <a href="https://huggingface.co/lingshu-medical-mllm/Lingshu-I-8B">Lingshu-I-8B</a>  is released with state-of-the-art performance on medical VQA tasks. It undergoes the same training pipeline on top of InternVL3. </strong>
This repository contains the model of the paper [Lingshu: A Generalist Foundation Model for Unified Multimodal Medical Understanding and Reasoning](https://huggingface.co/papers/2506.07044). We also release a comprehensive medical evaluation toolkit in [MedEvalKit](https://github.com/alibaba-damo-academy/MedEvalKit), which supports fast evaluation of major multimodal and textual medical tasks.

<p align="center">
  <img src="lingshu_overview_rev.png" width="1500" />
</p>


### Highlights
* [Lingshu-I-8B](https://huggingface.co/lingshu-medical-mllm/Lingshu-I-8B) model, the latest SOTA model on most medical multimodal/textual QA and report generation tasks in 8B size. It is built on top of InternVL3, while undergoes the same training pipeline with previous Lingshu models.
* [Lingshu](https://huggingface.co/lingshu-medical-mllm/Lingshu-7B) models, built on top of Qwen2.5VL, achieve strong performance on  medical multimodal/textual QA and report generation tasks for 7B and 32 model sizes.
* [Lingshu-32B](https://huggingface.co/lingshu-medical-mllm/Lingshu-32B) outperforms GPT-4.1 and Claude Sonnet 4 in most multimodal QA and report generation tasks.
* Lingshu supports more than 12 medical imaging modalities, including X-Ray, CT Scan, MRI, Microscopy, Ultrasound, Histopathology, Dermoscopy, Fundus, OCT, Digital Photography, Endoscopy, and PET.

### Release
- Technical report: [Arxiv: Lingshu: A Generalist Foundation Model for Unified Multimodal Medical Understanding and Reasoning](https://arxiv.org/pdf/2506.07044).
- Model weights:
  - [Lingshu-7B](https://huggingface.co/lingshu-medical-mllm/Lingshu-7B)
  - [Lingshu-I-8B](https://huggingface.co/lingshu-medical-mllm/Lingshu-I-8B)
  - [Lingshu-32B](https://huggingface.co/lingshu-medical-mllm/Lingshu-32B)


> **Disclaimer**:
> We must note that even though the weights, codes, and demos are released in an open manner, similar to other pre-trained language models, and despite our best efforts in red teaming and safety fine-tuning and enforcement, our models come with potential risks, including but not limited to inaccurate, misleading or potentially harmful generation.
> Developers and stakeholders should perform their own red teaming and provide related security measures before deployment, and they must abide by and comply with local governance and regulations.
> In no event shall the authors be held liable for any claim, damages, or other liability arising from the use of the released weights, codes, or demos.


## Evaluation


### Medical Multimodal VQA



<table>
  <thead>
    <tr>
      <th>Models</th>
      <th>MMMU-Med</th>
      <th>VQA-RAD</th>
      <th>SLAKE</th>
      <th>PathVQA</th>
      <th>PMC-VQA</th>
      <th>OmniMedVQA</th>
      <th>MedXpertQA</th>
      <th>Avg.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="9" style="text-align:center;"><strong>Proprietary Models</strong></td>
    </tr>
    <tr>
      <td>GPT-4.1</td>
      <td>75.2</td>
      <td>65.0</td>
      <td>72.2</td>
      <td>55.5</td>
      <td>55.2</td>
      <td>75.5</td>
      <td>45.2</td>
      <td>63.4</td>
    </tr>
    <tr>
      <td>Claude Sonnet 4</td>
      <td>74.6</td>
      <td>67.6</td>
      <td>70.6</td>
      <td>54.2</td>
      <td>54.4</td>
      <td>65.5</td>
      <td>43.3</td>
      <td>61.5</td>
    </tr>
    <tr>
      <td>Gemini-2.5-Flash</td>
      <td>76.9</td>
      <td>68.5</td>
      <td>75.8</td>
      <td>55.4</td>
      <td>55.4</td>
      <td>71.0</td>
      <td>52.8</td>
      <td>65.1</td>
    </tr>
    <tr>
      <td colspan="9" style="text-align:center;"><strong>Open-source Models (&lt;10B)</strong></td>
    </tr>
    <tr>
      <td>BiomedGPT</td>
      <td>24.9</td>
      <td>16.6</td>
      <td>13.6</td>
      <td>11.3</td>
      <td>27.6</td>
      <td>27.9</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Med-R1-2B</td>
      <td>34.8</td>
      <td>39.0</td>
      <td>54.5</td>
      <td>15.3</td>
      <td>47.4</td>
      <td>-</td>
      <td>21.1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MedVLM-R1-2B</td>
      <td>35.2</td>
      <td>48.6</td>
      <td>56.0</td>
      <td>32.5</td>
      <td>47.6</td>
      <td>77.7</td>
      <td>20.4</td>
      <td>45.4</td>
    </tr>
    <tr>
      <td>MedGemma-4B-IT</td>
      <td>43.7</td>
      <td><u>72.5</u></td>
      <td>76.4</td>
      <td>48.8</td>
      <td>49.9</td>
      <td>69.8</td>
      <td>22.3</td>
      <td>54.8</td>
    </tr>
    <tr>
      <td>LLaVA-Med-7B</td>
      <td>29.3</td>
      <td>53.7</td>
      <td>48.0</td>
      <td>38.8</td>
      <td>30.5</td>
      <td>44.3</td>
      <td>20.3</td>
      <td>37.8</td>
    </tr>
    <tr>
      <td>HuatuoGPT-V-7B</td>
      <td>47.3</td>
      <td>67.0</td>
      <td>67.8</td>
      <td>48.0</td>
      <td>53.3</td>
      <td>74.2</td>
      <td>21.6</td>
      <td>54.2</td>
    </tr>
    <tr>
      <td>BioMediX2-8B</td>
      <td>39.8</td>
      <td>49.2</td>
      <td>57.7</td>
      <td>37.0</td>
      <td>43.5</td>
      <td>63.3</td>
      <td>21.8</td>
      <td>44.6</td>
    </tr>
    <tr>
      <td>Qwen2.5VL-7B</td>
      <td>50.6</td>
      <td>64.5</td>
      <td>67.2</td>
      <td>44.1</td>
      <td>51.9</td>
      <td>63.6</td>
      <td>22.3</td>
      <td>52.0</td>
    </tr>
    <tr>
      <td>InternVL2.5-8B</td>
      <td>53.5</td>
      <td>59.4</td>
      <td>69.0</td>
      <td>42.1</td>
      <td>51.3</td>
      <td><u>81.3</u></td>
      <td>21.7</td>
      <td>54.0</td>
    </tr>
    <tr>
      <td>InternVL3-8B</td>
      <td><strong>59.2</strong></td>
      <td>65.4</td>
      <td>72.8</td>
      <td>48.6</td>
      <td>53.8</td>
      <td>79.1</td>
      <td>22.4</td>
      <td>57.3</td>
    </tr>
    <tr>
      <td><strong>Lingshu-7B</strong></td>
      <td><u>54.0</u></td>
      <td>67.9</td>
      <td><u>83.1</u></td>
      <td><u>61.9</u></td>
      <td><strong>56.3</strong></td>
      <td><strong>82.9</strong></td>
      <td><u>26.7</u></td>
      <td><u>61.8</u></td>
    </tr>
    <tr>
      <td><strong style="color: red">Lingshu-I-8B</strong></td>
      <td>49.1</td>
      <td><strong>73.0</strong></td>
      <td><strong>91.6</strong></td>
      <td><strong>74.9</strong></td>
      <td><u>55.8</u></td>
      <td>79.7</td>
      <td><strong>27.5</strong></td>
      <td><strong>64.5</strong></td>
    </tr>
    <tr>
      <td colspan="9" style="text-align:center;"><strong>Open-source Models (&gt;10B)</strong></td>
    </tr>
    <tr>
      <td>HealthGPT-14B</td>
      <td>49.6</td>
      <td>65.0</td>
      <td>66.1</td>
      <td><u>56.7</u></td>
      <td>56.4</td>
      <td>75.2</td>
      <td>24.7</td>
      <td>56.2</td>
    </tr>
    <tr>
      <td>HuatuoGPT-V-34B</td>
      <td>51.8</td>
      <td>61.4</td>
      <td>69.5</td>
      <td>44.4</td>
      <td>56.6</td>
      <td>74.0</td>
      <td>22.1</td>
      <td>54.3</td>
    </tr>
    <tr>
      <td>MedDr-40B</td>
      <td>49.3</td>
      <td>65.2</td>
      <td>66.4</td>
      <td>53.5</td>
      <td>13.9</td>
      <td>64.3</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>InternVL3-14B</td>
      <td><u>63.1</u></td>
      <td>66.3</td>
      <td><u>72.8</u></td>
      <td>48.0</td>
      <td>54.1</td>
      <td>78.9</td>
      <td>23.1</td>
      <td>58.0</td>
    </tr>
    <tr>
      <td>Qwen2.5V-32B</td>
      <td>59.6</td>
      <td><u>71.8</u></td>
      <td>71.2</td>
      <td>41.9</td>
      <td>54.5</td>
      <td>68.2</td>
      <td>25.2</td>
      <td>56.1</td>
    </tr>
    <tr>
      <td>InternVL2.5-38B</td>
      <td>61.6</td>
      <td>61.4</td>
      <td>70.3</td>
      <td>46.9</td>
      <td><u>57.2</u></td>
      <td><u>79.9</u></td>
      <td>24.4</td>
      <td>57.4</td>
    </tr>
    <tr>
      <td>InternVL3-38B</td>
      <td><strong>65.2</strong></td>
      <td>65.4</td>
      <td>72.7</td>
      <td>51.0</td>
      <td>56.6</td>
      <td>79.8</td>
      <td><u>25.2</u></td>
      <td><u>59.4</u></td>
    </tr>
    <tr>
      <td><strong>Lingshu-32B</strong></td>
      <td>62.3</td>
      <td><strong>76.5</strong></td>
      <td><strong>89.2</strong></td>
      <td><strong>65.9</strong></td>
      <td><strong>57.9</strong></td>
      <td><strong>83.4</strong></td>
      <td><strong>30.9</strong></td>
      <td><strong>66.6</strong></td>
    </tr>
  </tbody>
</table>


### Usage
#### Using vLLM(0.14.0)
```python
import dataclasses
from enum import IntEnum, auto
from typing import Dict, List, Tuple, Union
from transformers import AutoProcessor
from vllm import LLM, SamplingParams
import os
from PIL import Image

class SeparatorStyle(IntEnum):
    """Separator styles."""

    ADD_COLON_SINGLE = auto()
    ADD_COLON_TWO = auto()
    ADD_COLON_SPACE_SINGLE = auto()
    NO_COLON_SINGLE = auto()
    NO_COLON_TWO = auto()
    ADD_NEW_LINE_SINGLE = auto()
    LLAMA2 = auto()
    CHATGLM = auto()
    CHATML = auto()
    CHATINTERN = auto()
    DOLLY = auto()
    RWKV = auto()
    PHOENIX = auto()
    ROBIN = auto()
    FALCON_CHAT = auto()
    CHATGLM3 = auto()
    INTERNVL_ZH = auto()
    MPT = auto()


@dataclasses.dataclass
class Conversation:
    """A class that manages prompt templates and keeps all conversation history."""

    # The name of this template
    name: str
    # The template of the system prompt
    system_template: str = '{system_message}'
    # The system message
    system_message: str = ''
    # The names of two roles
    roles: Tuple[str] = ('USER', 'ASSISTANT')
    # All messages. Each item is (role, message).
    messages: List[List[str]] = ()
    # The number of few shot examples
    offset: int = 0
    # The separator style and configurations
    sep_style: SeparatorStyle = SeparatorStyle.ADD_COLON_SINGLE
    sep: str = '\n'
    sep2: str = None
    # Stop criteria (the default one is EOS token)
    stop_str: Union[str, List[str]] = None
    # Stops generation if meeting any token in this list
    stop_token_ids: List[int] = None

    def get_prompt(self) -> str:
        """Get the prompt for generation."""
        system_prompt = self.system_template.format(system_message=self.system_message)
        if self.sep_style == SeparatorStyle.ADD_COLON_SINGLE:
            ret = system_prompt + self.sep
            for role, message in self.messages:
                if message:
                    ret += role + ': ' + message + self.sep
                else:
                    ret += role + ':'
            return ret
        elif self.sep_style == SeparatorStyle.ADD_COLON_TWO:
            seps = [self.sep, self.sep2]
            ret = system_prompt + seps[0]
            for i, (role, message) in enumerate(self.messages):
                if message:
                    ret += role + ': ' + message + seps[i % 2]
                else:
                    ret += role + ':'
            return ret
        elif self.sep_style == SeparatorStyle.ADD_COLON_SPACE_SINGLE:
            ret = system_prompt + self.sep
            for role, message in self.messages:
                if message:
                    ret += role + ': ' + message + self.sep
                else:
                    ret += role + ': '  # must be end with a space
            return ret
        elif self.sep_style == SeparatorStyle.ADD_NEW_LINE_SINGLE:
            ret = '' if system_prompt == '' else system_prompt + self.sep
            for role, message in self.messages:
                if message:
                    ret += role + '\n' + message + self.sep
                else:
                    ret += role + '\n'
            return ret
        elif self.sep_style == SeparatorStyle.NO_COLON_SINGLE:
            ret = system_prompt
            for role, message in self.messages:
                if message:
                    ret += role + message + self.sep
                else:
                    ret += role
            return ret
        elif self.sep_style == SeparatorStyle.NO_COLON_TWO:
            seps = [self.sep, self.sep2]
            ret = system_prompt
            for i, (role, message) in enumerate(self.messages):
                if message:
                    ret += role + message + seps[i % 2]
                else:
                    ret += role
            return ret
        elif self.sep_style == SeparatorStyle.RWKV:
            ret = system_prompt
            for i, (role, message) in enumerate(self.messages):
                if message:
                    ret += (
                        role
                        + ': '
                        + message.replace('\r\n', '\n').replace('\n\n', '\n')
                    )
                    ret += '\n\n'
                else:
                    ret += role + ':'
            return ret
        elif self.sep_style == SeparatorStyle.LLAMA2:
            seps = [self.sep, self.sep2]
            if self.system_message:
                ret = system_prompt
            else:
                ret = '[INST] '
            for i, (role, message) in enumerate(self.messages):
                tag = self.roles[i % 2]
                if message:
                    if i == 0:
                        ret += message + ' '
                    else:
                        ret += tag + ' ' + message + seps[i % 2]
                else:
                    ret += tag
            return ret
        elif self.sep_style == SeparatorStyle.CHATGLM:
            # source: https://huggingface.co/THUDM/chatglm-6b/blob/1d240ba371910e9282298d4592532d7f0f3e9f3e/modeling_chatglm.py#L1302-L1308
            # source2: https://huggingface.co/THUDM/chatglm2-6b/blob/e186c891cf64310ac66ef10a87e6635fa6c2a579/modeling_chatglm.py#L926
            round_add_n = 1 if self.name == 'chatglm2' else 0
            if system_prompt:
                ret = system_prompt + self.sep
            else:
                ret = ''

            for i, (role, message) in enumerate(self.messages):
                if i % 2 == 0:
                    ret += f'[Round {i//2 + round_add_n}]{self.sep}'

                if message:
                    ret += f'{role}：{message}{self.sep}'
                else:
                    ret += f'{role}：'
            return ret
        elif self.sep_style == SeparatorStyle.CHATML:
            ret = '' if system_prompt == '' else system_prompt + self.sep + '\n'
            for role, message in self.messages:
                if message:
                    ret += role + '\n' + message + self.sep + '\n'
                else:
                    ret += role + '\n'
            return ret
        elif self.sep_style == SeparatorStyle.CHATGLM3:
            ret = ''
            if self.system_message:
                ret += system_prompt
            for role, message in self.messages:
                if message:
                    ret += role + '\n' + ' ' + message
                else:
                    ret += role
            return ret
        elif self.sep_style == SeparatorStyle.CHATINTERN:
            # source: https://huggingface.co/internlm/internlm-chat-7b-8k/blob/bd546fa984b4b0b86958f56bf37f94aa75ab8831/modeling_internlm.py#L771
            seps = [self.sep, self.sep2]
            ret = system_prompt
            for i, (role, message) in enumerate(self.messages):
                # if i % 2 == 0:
                #     ret += "<s>"
                if message:
                    ret += role + ':' + message + seps[i % 2] + '\n'
                else:
                    ret += role + ':'
            return ret
        elif self.sep_style == SeparatorStyle.DOLLY:
            seps = [self.sep, self.sep2]
            ret = system_prompt
            for i, (role, message) in enumerate(self.messages):
                if message:
                    ret += role + ':\n' + message + seps[i % 2]
                    if i % 2 == 1:
                        ret += '\n\n'
                else:
                    ret += role + ':\n'
            return ret
        elif self.sep_style == SeparatorStyle.PHOENIX:
            ret = system_prompt
            for role, message in self.messages:
                if message:
                    ret += role + ': ' + '<s>' + message + '</s>'
                else:
                    ret += role + ': ' + '<s>'
            return ret
        elif self.sep_style == SeparatorStyle.ROBIN:
            ret = system_prompt + self.sep
            for role, message in self.messages:
                if message:
                    ret += role + ':\n' + message + self.sep
                else:
                    ret += role + ':\n'
            return ret
        elif self.sep_style == SeparatorStyle.FALCON_CHAT:
            ret = ''
            if self.system_message:
                ret += system_prompt + self.sep
            for role, message in self.messages:
                if message:
                    ret += role + ': ' + message + self.sep
                else:
                    ret += role + ':'

            return ret
        elif self.sep_style == SeparatorStyle.INTERNVL_ZH:
            seps = [self.sep, self.sep2]
            ret = self.system_message + seps[0]
            for i, (role, message) in enumerate(self.messages):
                if message:
                    ret += role + ': ' + message + seps[i % 2]
                else:
                    ret += role + ':'
            return ret
        elif self.sep_style == SeparatorStyle.MPT:
            ret = system_prompt + self.sep
            for role, message in self.messages:
                if message:
                    if type(message) is tuple:
                        message, _, _ = message
                    ret += role + message + self.sep
                else:
                    ret += role
            return ret
        else:
            raise ValueError(f'Invalid style: {self.sep_style}')

    def set_system_message(self, system_message: str):
        """Set the system message."""
        self.system_message = system_message

    def append_message(self, role: str, message: str):
        """Append a new message."""
        self.messages.append([role, message])

    def update_last_message(self, message: str):
        """Update the last output.
        The last message is typically set to be None when constructing the prompt,
        so we need to update it in-place after getting the response from a model.
        """
        self.messages[-1][1] = message

    def to_gradio_chatbot(self):
        """Convert the conversation to gradio chatbot format."""
        ret = []
        for i, (role, msg) in enumerate(self.messages[self.offset :]):
            if i % 2 == 0:
                ret.append([msg, None])
            else:
                ret[-1][-1] = msg
        return ret

    def to_openai_api_messages(self):
        """Convert the conversation to OpenAI chat completion format."""
        ret = [{'role': 'system', 'content': self.system_message}]

        for i, (_, msg) in enumerate(self.messages[self.offset :]):
            if i % 2 == 0:
                ret.append({'role': 'user', 'content': msg})
            else:
                if msg is not None:
                    ret.append({'role': 'assistant', 'content': msg})
        return ret

    def copy(self):
        return Conversation(
            name=self.name,
            system_template=self.system_template,
            system_message=self.system_message,
            roles=self.roles,
            messages=[[x, y] for x, y in self.messages],
            offset=self.offset,
            sep_style=self.sep_style,
            sep=self.sep,
            sep2=self.sep2,
            stop_str=self.stop_str,
            stop_token_ids=self.stop_token_ids,
        )

    def dict(self):
        return {
            'template_name': self.name,
            'system_message': self.system_message,
            'roles': self.roles,
            'messages': self.messages,
            'offset': self.offset,
        }


# A global registry for all conversation templates
conv_templates: Dict[str, Conversation] = {}


def register_conv_template(template: Conversation, override: bool = False):
    """Register a new conversation template."""
    if not override:
        assert (
            template.name not in conv_templates
        ), f'{template.name} has been registered.'

    conv_templates[template.name] = template


def get_conv_template(name: str) -> Conversation:
    """Get a conversation template."""
    return conv_templates[name].copy()


def process_messages(messages):
    conv = Conversation(
            name='internvl2_5',
            system_template='<|im_start|>system\n{system_message}',
            system_message='',
            roles=('<|im_start|>user\n', '<|im_start|>assistant\n'),
            sep_style=SeparatorStyle.MPT,
            sep='<|im_end|>\n',
        )
    conv.messages = []
    imgs = []
    for message in messages:
        role = message['role']
        content = message['content']
        if isinstance(content, str):
            conv.append_message(role, content)
        elif isinstance(content, list):
            text = ""
            for item in content:
                if item['type'] == 'text':
                    text += item['text']
                elif item['type'] == 'image':
                    text = text + "\n<IMG_CONTEXT>"
                    image = item['image']
                    if isinstance(image, str):
                        image = Image.open(item['image'])
                    imgs.append(image)
            
            conv.append_message(role, text)
                        
    
    conv.append_message(conv.roles[1], None)
    prompt = conv.get_prompt()
    mm_data = {}
    if len(imgs) > 0:
        mm_data["image"] = imgs


    llm_inputs = {
        "prompt": prompt,
        "multi_modal_data": mm_data,
    }

    return llm_inputs


if __name__ == '__main__': 
    os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    processor = AutoProcessor.from_pretrained("lingshu-medical-mllm/Lingshu-I-8B")
    llm = LLM(model="lingshu-medical-mllm/Lingshu-I-8B", limit_mm_per_prompt = {"image": 4}, tensor_parallel_size=2, enforce_eager=True, trust_remote_code=True,gpu_memory_utilization = 0.7)
    sampling_params = SamplingParams(
                temperature=0.7,
                top_p=1,
                repetition_penalty=1,
                max_tokens=1024,
                stop_token_ids=[],
            )

    text = "What does the image show?"
    image_path = "example.jpg"

    message = [
        {
            "role":"user",
            "content":[
                {"type":"image","image":image_path},
                {"type":"text","text":text}
                ]
        }
    ]
    llm_inputs = process_messages(message)
    outputs = llm.generate([llm_inputs], sampling_params=sampling_params)
    print(outputs[0].outputs[0].text)

```


## Citation

If you find our project useful, we hope you would kindly star our repo and cite our work as follows:

```
@article{xu2025lingshu,
  title={Lingshu: A Generalist Foundation Model for Unified Multimodal Medical Understanding and Reasoning},
  author={Xu, Weiwen and Chan, Hou Pong and Li, Long and Aljunied, Mahani and Yuan, Ruifeng and Wang, Jianyu and Xiao, Chenghao and Chen, Guizhen and Liu, Chaoqun and Li, Zhaodonghui and others},
  journal={arXiv preprint arXiv:2506.07044},
  year={2025}
}
```