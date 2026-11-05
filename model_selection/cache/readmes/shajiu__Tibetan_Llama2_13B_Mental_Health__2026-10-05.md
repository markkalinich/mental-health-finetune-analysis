---
license: apache-2.0
---
## 基于LLama2_13B的藏文词汇表扩充/继续预训练/心理健康多轮对话指令微调的大语言模型

### 一、本文的训练流程主要包含：
- 对Llama 2 进行藏文词表扩充，词表由32000 扩展至56724，提高模型在藏文的编解码效率。在TibetanGeneralCorpus 上使用Sentencepiece 工具训练基于Unigram 策略的藏文分词器。生成的词表与原版Llama 2 的32K 词表进行合并，排除重复的词 元后，得到扩充后词表规模为56724。用15G 的TibetanGeneralCorpus 和20G 的英、中混合文本进行CPT，采用自回归任务。

### 二、通过心理健康领域的藏文指令数据集进行了QLoRA微调：
- 通过4-bit的nf4量化，且加入更多adapter，在大幅减少显存消耗的同时，尽可能逼近全量参数微调的效果。 该方法可以在一张V100上对33B的模型进行微调，并且性能逼近全量参数微调。

### 三、推理Demo示例：
```Python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载模型和分词器
model_name = "shajiu/Tibetan_Llama2_13B_Mental_Health"  # 模型名称，可以根据需要调整
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.to(device)

def generate_response(prompt, max_length=100, temperature=0.7, top_p=0.9):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        do_sample=True
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    prompt = "ང་རང་ཉེ་ལམ་མགོ་འཁོར་ཡོད།མཐོ་གསུམ་རྗེས་ཀྱི་ང་རང་མཐོ་རྒྱུགས་སྔོན་གྱི་འཇིགས་སྐྲག་ལས་གཞན་ད་དུང་རང་ཉིད་སྐྱེས་མ་ཐག་ནས་བཟུང་ལྷག་མ་ཞིག་ཡིན་པར་འདོད།དོན་སྙིང་ཅི་ཡང་མེད།ང་ལ་གྲོགས་པོ་མེད།ཁེར་རྐྱང་གིས་བཟོད་མི་ཐུབ།ཁྱེད་ཀྱིས་ང་ལ་བསམ་འཆར་འགའ་འདོན་ཐུབ་བམ།"
    response = generate_response(prompt)
    print(response)
```

- GitHub：[藏文心理健康支持对话数据集(Tibetan_Mental)与大模型(Tibetan_Mental_Chat)](https://github.com/Shajiu/Tibetan_Mental_Health_Chat "可选标题")