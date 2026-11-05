
    # Qwen2.5-0.5B-Instruct Medical LLM

    このモデルは、Qwen2.5-0.5B-Instructモデルを医療問題データセット（medical_o1_sft）で継続事前学習したものです。
    医療分野の質問応答タスクに特化しています。

    ## 学習データ
    - データセット: medical_o1_sft
    - 形式: 医療問題と回答のペア

    ## 使用方法
    このモデルは医療分野の質問応答に使用できます。

    ```python
    from transformers import AutoModelForCausalLM, AutoTokenizer

    # モデルとトークナイザーのロード
    model = AutoModelForCausalLM.from_pretrained("bkholyday/Qwen2.5-0.5B-Instruct-medicalLLM-HuatuoGPT-o1-sft", trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained("bkholyday/Qwen2.5-0.5B-Instruct-medicalLLM-HuatuoGPT-o1-sft", trust_remote_code=True)

    # 医療質問の例
    question = "高血圧の一般的な症状と治療法について教えてください。"
    
    # 入力の準備
    messages = [{"role": "user", "content": question}]
    input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    
    # 推論
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(model.device)
    output_ids = model.generate(input_ids, max_new_tokens=512)
    response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)
    
    print(response)
    ```
    