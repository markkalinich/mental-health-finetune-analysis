# VectorLLM HF 0407

这是当前可直接分发使用的 Hugging Face 版本导出目录模板，已经包含：

- C-RADIO 视觉塔实现与权重映射逻辑
- VectorLLM 自定义 `AutoModel` / `AutoProcessor`
- 本地可加载的 processor / image processor / modeling 代码
- `bfloat16` 推理配置

当前推荐在 GPU 上使用，推荐环境：

```bash
/home/zhangtao/env/xtuner/bin/python
```

## 目录说明

- `model.safetensors`: 合并后的主模型权重
- `config.json`: 主配置
- `generation_config.json`: 生成配置
- `preprocessor_config.json`: 图像预处理配置
- `test_hf.py`: 单图推理与可视化示例脚本
- `gradio_bbox_demo.py`: 整图画框、后端裁剪和全图回映射的 Gradio 脚本
- `conversion_report.json`: 与 xtuner 对齐验证结果
- `radio_bundle/`: 打包后的 C-RADIO 相关实现

## 设计目标

- 可通过 `AutoModel` 和 `AutoProcessor` 拉起
- 不依赖外部 Hugging Face cache 中的自定义代码
- 不要求 `trust_remote_code=True`
- 适用于“单个物体已裁剪好”的输入图像，不做二次裁剪

## 快速开始

### 1. 命令行推理

推荐直接使用目录内置的 [test_hf.py](/home/zhangtao/hf_model/vectorllm_hf_0407/test_hf.py)：

```bash
/home/zhangtao/env/xtuner/bin/python \
  /home/zhangtao/hf_model/vectorllm_hf_0407/test_hf.py \
  /home/zhangtao/hf_model/vectorllm_hf_0407 \
  /path/to/your_image.png \
  --save-dir /tmp/vectorllm_hf_demo
```

输出：

- `overlay.png`: 叠加 polygon 的可视化结果
- `report.json`: 文本输出、网格坐标、回映射后的 polygon

### 2. Python 方式加载

必须先把模型目录的父目录加入 `sys.path`，再导入包本身完成本地注册：

```python
import sys
from pathlib import Path

import torch
from PIL import Image
from transformers import AutoModel, AutoProcessor, GenerationConfig

model_path = Path("/home/zhangtao/hf_model/vectorllm_hf_0407")
sys.path.insert(0, str(model_path.parent))
import vectorllm_hf_0407  # noqa: F401

from vectorllm_hf_0407.test_hf import DEFAULT_RAW_PROMPT, decode_generated_text, get_stop_criteria

model = AutoModel.from_pretrained(
    model_path,
    trust_remote_code=False,
    torch_dtype=torch.bfloat16,
).cuda().eval()
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=False)
tokenizer = processor.tokenizer

image = Image.open("/path/to/your_image.png").convert("RGB")
model_inputs = processor(text=[DEFAULT_RAW_PROMPT], images=[image], return_tensors="pt")
model_inputs = {
    key: value.to(model.device) if torch.is_tensor(value) else value
    for key, value in model_inputs.items()
}

stop_criteria = get_stop_criteria(tokenizer, ["<|im_end|>", "<|endoftext|>"])
output = model.generate(
    **model_inputs,
    generation_config=GenerationConfig(
        max_new_tokens=640,
        do_sample=False,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        temperature=0.0,
        top_k=1,
    ),
    bos_token_id=tokenizer.bos_token_id,
    stopping_criteria=stop_criteria,
    output_hidden_states=False,
    return_dict_in_generate=True,
    do_sample=False,
    temperature=0.0,
    top_k=1,
)

text = decode_generated_text(output, model_inputs, tokenizer)
print(text)
```

### 3. Gradio 交互

若输入是整图，希望在图上手动画 bbox，再由后端扩框裁剪后送入模型，可直接启动：

```bash
/home/zhangtao/env/xtuner/bin/python \
  /home/zhangtao/hf_model/vectorllm_hf_0407/gradio_bbox_demo.py \
  --model-path /home/zhangtao/hf_model/vectorllm_hf_0407 \
  --server-name 0.0.0.0 \
  --server-port 7861
```

功能说明：

- 前端直接在整图上拖拽一个或多个 bbox
- 后端按 `1.0-1.3` 可调扩展比例裁剪
- 裁剪图送入 VectorLLM HF 模型推理
- 结果会回映射到整图，并展示全图 overlay、裁剪预览和结构化 JSON

使用步骤：

1. 打开页面后先上传整图。
2. 在左侧画布上拖拽 bbox，可连续画多个框。
3. `Prompt Target` 选择 `Building` 或 `Object`。
4. `BBox Expand Ratio` 控制后端扩框比例。`1.0` 表示仅按原框裁剪，`1.15` 或 `1.2` 通常更稳，`1.3` 适合给目标留更多上下文。
5. 点击 `Run` 执行推理，点击 `Clear` 清空当前图像和框。

页面输出说明：

- `Full-Image Overlay`: 全图可视化结果，同时叠加原始 bbox、扩框后的 bbox 和回映射后的 polygon
- `Expanded Crop Preview`: 每个 bbox 对应的裁剪图及其局部 polygon，可用来快速检查裁剪是否合理
- `Model Text Output`: 模型原始输出文本，便于排查 `<xN><yN>` 序列
- `Structured Result`: 结构化 JSON，包含原框、扩框、裁剪尺寸、网格坐标和全图坐标 polygon

补充说明：

- 当前脚本默认监听 `7861` 端口，可通过 `--server-port` 调整
- 服务启动后若需停止，终端里直接 `Ctrl+C` 即可
- 首次启动会加载大模型，耗时会明显长于后续推理

## 输入要求

- 输入应为单个目标的裁剪图
- 当前默认 prompt 针对建筑轮廓提取
- 模型输出为 `<xN><yN>` 格式的离散 polygon 点序列

## 结果说明

- 网格坐标范围默认是 `0~127`
- [test_hf.py](/home/zhangtao/hf_model/vectorllm_hf_0407/test_hf.py) 会自动把离散点映射回原图坐标并可视化
- [gradio_bbox_demo.py](/home/zhangtao/hf_model/vectorllm_hf_0407/gradio_bbox_demo.py) 会把裁剪区域内的离散点恢复到全图坐标后再叠加显示
- 当前 GPU 实测下，回载后的 HF 输出与 xtuner 已基本对齐，可能存在极轻微的离散点差异

## 备注

- 若从别的工作目录调用，不要省略 `sys.path.insert(...)` 和 `import vectorllm_hf_0407`
- 若只想快速跑 demo，优先使用 [test_hf.py](/home/zhangtao/hf_model/vectorllm_hf_0407/test_hf.py)
