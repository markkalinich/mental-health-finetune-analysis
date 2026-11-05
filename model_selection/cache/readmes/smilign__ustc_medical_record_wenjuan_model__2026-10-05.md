license: apache-2.0

## 使用模型

1. 将模型文件（下面的文件）放到一个文件夹中，如

    - merged-model/llm-v7-wenjuan"
    - added_tokens.json
    - config.json
    - generation_config.json
    - merges.txt
    - model-00001-of-00004.safetensors
    - model-00002-of-00004.safetensors
    - model-00003-of-00004.safetensors
    - model-00004-of-00004.safetensors
    - model.safetensors.index.json
    - special_tokens_map.json
    - tokenizer_config.json
    - tokenizer.json
    - vocab.json


2. 运行```use_model.py```文件，注意需要更改文件中的```model_name_or_path```和```path```路径为模型所在的文件夹即可。