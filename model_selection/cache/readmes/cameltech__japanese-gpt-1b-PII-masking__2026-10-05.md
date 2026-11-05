---
language:
- ja
license: mit
pipeline_tag: text-generation
widget:
- text: '# タスク

    入力文中の個人情報をマスキングせよ


    # 入力文

    渡邉亮です。現在の住所は東京都世田谷区代沢1-2-3です。<SEP>'
inference:
  parameters:
    max_length: 256
    num_beams: 3
    num_return_sequences: 1
    early_stopping: true
    eos_token_id: 3
    pad_token_id: 4
    repetition_penalty: 3.0
---

# japanese-gpt-1b-PII-masking

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64ffe8a785a884a964b0cffe/eXFMcprvDELlhC85OYO9L.png)

# Model Description
japanese-gpt-1b-PII-masking は、 [日本語事前学習済み1B GPTモデル](https://huggingface.co/rinna/japanese-gpt-1b)をベースとして、日本語の文章から個人情報をマスキングするように学習したモデルです。<br>
<br>
個人情報は以下の対応関係でマスキングされます。
| タグ | 項目 |
| ---- | ---- |
| \<name\> | 氏名 |
| \<birthday\> | 生年月日 |
| \<phone-number\> | 電話番号 |
| \<mail-address\> | メールアドレス |
| \<customer-id\> | 会員番号・ID |
| \<address\> | 住所 |
| \<post-code\> | 郵便番号 |
| \<company\> | 会社名 |

# Usage
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

instruction = "# タスク\n入力文中の個人情報をマスキングせよ\n\n# 入力文\n"
text = """オペレーター：ありがとうございます。カスタマーサポートセンターでございます。お名前と生年月日、ご住所を市区町村まで教えていただけますか？
顧客：あ、はい。西山...すみません、西山俊之です。生年月日は、えーっと、1983年1月23日です。東京都練馬区在住です。
オペレーター：西山俊之様、1983年1月23日生まれ、東京都練馬区にお住まいですね。確認いたしました。お電話の件につきまして、さらにご本人様確認をさせていただきます。"""
input_text = instruction + text

model_name = "cameltech/japanese-gpt-1b-PII-masking"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

if torch.cuda.is_available():
    model = model.to("cuda")

def preprocess(text):
    return text.replace("\n", "<LB>")

def postprocess(text):
    return text.replace("<LB>", "\n")

generation_config = {
    "max_new_tokens": 256,
    "num_beams": 3,
    "num_return_sequences": 1,
    "early_stopping": True,
    "eos_token_id": tokenizer.eos_token_id,
    "pad_token_id": tokenizer.pad_token_id,
    "repetition_penalty": 3.0
}

input_text += "<SEP>"
input_text = preprocess(input_text)

with torch.no_grad():
    token_ids = tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt")

    output_ids = model.generate(
        token_ids.to(model.device),
        **generation_config
    )
output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1) :], skip_special_tokens=True)
output = postprocess(output)

print(output)
"""
オペレーター:ありがとうございます。カスタマーサポートセンターでございます。お名前と生年月日、ご住所を<address>まで教えていただけますか?
顧客:あ、はい。<name>です。生年月日は、えーっと、<birthday>です。<address>在住です。
オペレーター:<name>様、<birthday>生まれ、<address>にお住まいですね。確認いたしました。お電話の件につきまして、さらにご本人様確認をさせていただきます。
"""
```

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)