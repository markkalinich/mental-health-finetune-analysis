---
license: agpl-3.0
language:
- zh
tags:
- PULSE
- llm
---

# PULSE

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-brightgreen.svg)](https://github.com/openmedlab/PULSE/blob/main/LICENSE)
[![Model License](https://img.shields.io/badge/Model%20License-GNU%20AGPL%203.0-red.svg)](https://github.com/openmedlab/PULSE/blob/main/MODEL_LICENSE)

## 目录

- [开源模型](#开源模型)
- [模型介绍](#模型介绍)
  - [局限性](#局限性)
  - [Elo评测](#Elo评测)
- [推理](#推理)
  - [硬件要求](#硬件要求)
  - [下载安装](#下载安装)
  - [使用示例](#使用示例)
- [致谢](#致谢)
- [开源协议](#开源协议)

----

## 开源模型

- [**PULSE-7bv5**](https://huggingface.co/OpenMEDLab/PULSE-7bv5)

## 模型介绍

- **大规模训练**：PULSE模型在Bloom 7B模型的基础上，
使用约4,000,000个医学领域和通用领域的SFT数据进行进一步微调。
- **全面的医学自然语言处理任务**：PULSE支持医学领域的各种自然语
言处理任务，包括健康教育、医师考试问题、报告解读、医疗记录结构化
以及模拟诊断和治疗。

### 局限性

由于模型参数量较小和自回归生成范式，尽管模型提供了有关疾病诊断和治疗的推理结果，但这些结果不能代替线下职业医生的建议和治疗方案。所有回答仅供参考，不应作为诊断或治疗的依据。我们强烈建议用户在需要诊断或治疗疾病时，寻求专业医生的帮助和建议。

### Elo评测
| model_name                    | model_size   |   ALL |   MedQA_Mainland |   PromptCBLUE |   webMedQA |
|:------------------------------|:-------------|------:|-----------------:|--------------:|-----------:|
| GPT4                          | 220B*8(?)    |  1195 |             1087 |          1134 |       1107 |
| ChatGPT                       | 175B(?)      |  1123 |             1053 |          1089 |       1067 |
| PULSE_7b with prompt          | 7B           |  1074 |             1019 |          1047 |       1060 |
| PULSE_14b                     | 14B          |  1055 |             1001 |          1037 |       1056 |
| PULSE_7b                      | 7B           |  1054 |             1028 |          1037 |       1030 |
| BianQue                       | 6B           |   926 |              939 |           920 |       1011 |
| QiZhenGPT                     | 13B          |   918 |              949 |           935 |        974 |
| Med-ChatGLM                   | 6B           |   864 |              988 |           921 |        859 |
| BenTsao                       | 7B           |   846 |              966 |           913 |        859 |
| DoctorGLM                     | 6B           |   812 |              935 |           891 |        856 |


## 推理
### 硬件要求

下表提供了一个batch size=1时本地部署PULSE进行推理所需的显存大小。

| 量化等级 | 加载模型 |
| -------- | -------- |
| FP16     | 14GB     |


### 下载安装
1. 下载本仓库内容至本地/远程服务器

```bash
git clone https://github.com/openmedlab/PULSE
cd PULSE
```

2. 创建conda环境安装依赖

```bash
conda env create -f llm.yml
conda activate llm
```

其中`torch`和`transformers`版本不建议低于推荐版本。

### 使用示例

#### 网页Demo

**Gradio**

```bash
python web_demo_gradio.py
```

#### 命令行Demo

您可以运行仓库中的`cli_demo.py`来启动一个简单的命令行Demo：

```bash
python cli_demo.py
```
## 致谢

- 上海人工智能实验室
- 上海交通大学-清源研究院
- 华东理工大学-自然语言处理与大数据挖掘实验室


## 开源协议

本项目所含代码采用[Apache 2.0](https://github.com/openmedlab/PULSE/blob/main/LICENSE)协议，模型权重采用[GNU AGPL 3.0](https://github.com/openmedlab/PULSE/blob/main/MODEL_LICENSE)协议。如使用本项目所含模型及其修改版本提供服务产生误导性或有害性言论，造成不良影响，由服务提供方负责，与本项目无关。
