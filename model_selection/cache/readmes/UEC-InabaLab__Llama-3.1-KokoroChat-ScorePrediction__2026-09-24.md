---
base_model: tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3
license:
- llama3.1
- gemma
language:
- ja
- en
pipeline_tag: text-generation
tags:
  - counseling
  - dialogue-system
  - score-prediction
datasets:
- UEC-InabaLab/KokoroChat
---

# 🧠 Llama-3.1-KokoroChat-ScorePrediction: Japanese Counseling Dialogue Scoring Model

**Llama-3.1-KokoroChat-ScorePrediction** is a large-scale Japanese language model fine-tuned on the **KokoroChat dataset**—a collection of over 6,000 psychological counseling dialogues conducted via **role-play between trained counselors**.  
Unlike response-generation models, this version is trained to **predict client feedback scores** based on the full counseling dialogue history.

---

## 💡 Overview

- ✅ Task: Predict the **overall counseling quality score** as rated by the client
- ✅ Dataset: 6,589 dialogues with feedback scores between 0 and 100
- ✅ Data source: Text-based role-play by trained counselors
- ✅ Base Model: [`tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3`](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3)

---

## ⚙️ Usage Example

```python
# -*- coding: utf-8 -*-
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "UEC-InabaLab/Llama-3.1-KokoroChat-ScorePrediction"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

# Set pad_token_id
if tokenizer.pad_token_id is None:
    tokenizer.pad_token = "[PAD]"
    tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("[PAD]")

model.config.pad_token_id = tokenizer.pad_token_id

# Build dialogue input
messages = [
    {"role": "system", "content": "心理カウンセリングの会話について、点数をつけてください。"},
    {"role": "user", "content": "カウンセラー: （こんにちは、よろしくお願いいたします。時間になりましたらはじめさせていただきます。）。\nクライアント: （こんにちは、よろしくお願いいたします。）。\nカウンセラー: こんにちは。相談員です。今日はご相談に来てくださって、ありがとうございます。はじめに、年齢と性別、相談内容を教えてください。\nクライアント: 40代.女性、仕事を辞めたいが、やりたいことがわからない。\nカウンセラー: そうなんですね、それはお困りですねお仕事を辞めたくて、次に何をしようか探されている、ということでしょうか。\nクライアント: はい、そうです。\nカウンセラー: そうなんですね、今のお仕事を辞めたいと思われたきっかけはなんでしょうか。\nクライアント: 職場のパワハラが嫌で辞めたいです。\nカウンセラー: そうなんですね、それは嫌な気持ちになりますね辞めたくなるのも自然なことだと思いますどんなことがあったのか、お話しできる範囲で教えていただけますか。\nクライアント: 上司に信頼してないと言われたり、それに同意する、先輩がいつも、私の仕事の間に入ってきます。\nカウンセラー: そうなんですね、それは傷つきますね上司や同僚の方は、同じ方でしょうか。\nクライアント: いえ、違います。上司は一人で、同じ価値観をもった先輩の同僚が２人います。\nカウンセラー: そうなんですね、認めてもらえないのは本当におつらいことだと思います今の状態はどのくらい続いているのでしょうか。\nクライアント: 入社から10年くらいは経ちますね。\nカウンセラー: そうなんですね、とても長い期間職場に貢献されたのだと思いますその間、パワハラはずっと続いていたのでしょうか。\nクライアント: 今思うと、そうですね。\nカウンセラー: そうなんですね、とても過酷な環境だと思いますその環境の中で、ご自身の役割を果たそうとされているのは、とても立派です仕事の間に入られると、一人前の扱いではないようで腹が立つと思いますが、いかがでしょうか。\nクライアント: 最初は私も慣れなくてミスばかりだったので仕方ないなと思っていましたが、そう思われていることに違和感を感じるようになり、それなら、ここに居ても仕方ないなと思い、諦めるようになり、転職を感じるようになりました。訂正転職を考えるようになりました。でした、\nカウンセラー: 訂正ありがとうございますそうなんですね、お仕事に対する、真摯で丁寧な様子が伝わってきます間に入られる、とおっしゃっていましたが、具体的にはどんなことでしょうか。\nクライアント: 業者にお金を支払う時に受付の私にお金を預けてくれたらいいのに、まず、先輩にお金を預けて、確認されてから、私に届いたり、トイレ掃除してるのに、目の前で、また、トイレ掃除をされます。聞こえる所で、悪口、陰口を言われたりもします。\nカウンセラー: そうなんですね、すごく意地悪に感じます…聞こえるところで悪口や陰口も嫌な気持ちになりますね。そんな時はどうしているのでしょうか。\nクライアント: はい、悪口、陰口は自分のことじゃなくても、自分のこと言われているように前は思ってしまったり、声をきくのも嫌でした。\nカウンセラー: ええ、本当に嫌な気持ちになりますねそういったことを、社内に相談や報告できる方はいらっしゃいますか。\nクライアント: 最近は、また始まったと思えるようになり、きこえないように、わざと目の前の患者さんと大きな声で話すようにすると楽になりました。上司が1人しかいないので、吐き出す場所はないです。小さなクリニックなので、難しいです。\nカウンセラー: メッセージが重なってしまってすみません、ご自身で対策をとってらっしゃるのですね聞こえないということで楽になれるのは、素敵な発見だと思います。\nクライアント: みんな知っていても、暗黙の了解で、スルーですね。ありがとうございます。\nカウンセラー: なるほど、小さなクリニックだと、おっしゃる通り難しいですね辞めたいお気持ち、とても伝わってきました辞めた後何をやりたいかわからない、ということですが、次の仕事を見つけてから辞めたいとお考えでしょうか。\nクライアント: 辞めるまでに引き継ぎが半年ほど必要なので、これがやりたいと思えたら、動きだしたいと思ってます。\nカウンセラー: そうなんですね、半年というのは長く感じてしまいますが、その点はどのようにお考えですか。\nクライアント: 私も変わってるなと思いましたが、私は受付1人でやっているので、慣れるまでに時間がかかるので、それも仕方ないと諦めています。\nカウンセラー: そうなんですね、理由があって受け入れてるのですねここまでお話を聞いていて、過酷な職場環境でも真摯に丁寧にお仕事をされていて、責任感の強い方なのだなと感じています色々お話しくださった中で、今日一番お話になりたいことはなんでしょうか。\nクライアント: 次にやりたいことをみつけたい。\nカウンセラー: そうなんですね、次の職場に移るためにも、今日は一緒に考えさせてくださいね。\nクライアント: お願いいたします。\nカウンセラー: こちらこそ、よろしくお願いいたしますやりたいこと、とはどんなことでしょうか好きなことや、給与待遇がよいことなど、希望はおありですか。\nクライアント: フルタイムでなくても安定していて、やりがいがもてたらいいなと思います。\nカウンセラー: そうなんですね、安定というのは固定給で、という意味合いでしょうか。\nクライアント: そうですね、他に何かありますか？\nカウンセラー: 時折、プラス歩合制のような給与形態もあるため、確認させていただきました固定給は手取りがはっきりわかるので安心できますね。\nクライアント: そうですね。\nカウンセラー: もう一点、やりがいはどんなことに感じられておりますでしょうか。\nクライアント: 感謝された時とかですかね。自分が楽しいと感じたり。\nカウンセラー: 大事なことですね感謝されたり、楽しいと感じられる仕事につけると、モチベーションもあがりそうですね。\nクライアント: そうですね、モチベーション高く、生き生きと働きたいです。\nカウンセラー: そうですね、素敵な働き方だと思いますお仕事で楽しいと感じるのはどんな時でしょうか。\nクライアント: 患者さんが話して下さる話をきいてる時、楽しいと思います。\nカウンセラー: そうなんですね、そのようにお感じになるのですね今までのお話をうかがっていると、ご自身の中で「このように働きたい」という希望は、かなりはっきりしているように感じましたが、いかがでしょうか。\nクライアント: 形にするのが、難しく思います。\nカウンセラー: そうなんですね、形にするのが難しいとお感じなんですねもしよければ、今上げていただいたご希望をもって、ハローワークに行ったり、ネットで探してみるのはいかがでしょうか。\nクライアント: はい、そうしてみます。ありがとうございました。\nカウンセラー: はい、ぜひやってみてください先ほどおっしゃっていた、モチベーション高く、高く、生き生き働けそうな場所が見つかることを、応援しております。"}
]

# Tokenize with chat template
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

attention_mask = inputs.ne(tokenizer.pad_token_id)

# Generate score prediction
outputs = model.generate(
    inputs,
    attention_mask=attention_mask,
    pad_token_id=tokenizer.pad_token_id,
    max_new_tokens=256
)

# Extract only the newly generated tokens
response = outputs[0][inputs.shape[-1]:]
predicted_score = tokenizer.decode(response, skip_special_tokens=True)

# Print clean score prediction
print(predicted_score)
```

---

## 🛠️ Fine-Tuning Details

Fine-tuning was performed using **QLoRA** with the following configuration:

- **Quantization**: 4-bit NF4 with bfloat16 computation
- **LoRA target modules**: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- **LoRA parameters**:
  - `r = 8`
  - `lora_alpha = 16`
  - `lora_dropout = 0.05`

### Dataset Split

- **Training/Validation/Test ratio**: 8:1:1

### Hyperparameter Settings

- **Optimizer**: `adamw_torch_fused`
- **Warm-up Steps**: `100`
- **Learning Rate**: `2e-4`
- **Epochs**: `4`
- **Batch Size**: `4`

---

## 📄 Citation

If you use this model or dataset, please cite the following paper:

```bibtex
@inproceedings{qi2025kokorochat,
  title     = {KokoroChat: A Japanese Psychological Counseling Dialogue Dataset Collected via Role-Playing by Trained Counselors},
  author    = {Zhiyang Qi and Takumasa Kaneko and Keiko Takamizo and Mariko Ukiyo and Michimasa Inaba},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},
  year      = {2025},
  url       = {https://github.com/UEC-InabaLab/KokoroChat}
}
```
---

## 🔗 Related

- 📁 **Dataset**:  
  - [KokoroChat on Hugging Face Datasets](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat)  
  - [KokoroChat on GitHub (UEC-InabaLab)](https://github.com/UEC-InabaLab/KokoroChat)
- 🤖 **Response Generation Models**:  
  - [Llama-3.1-KokoroChat-Low](https://huggingface.co/UEC-InabaLab/Llama-3.1-KokoroChat-Low): fine-tuned on **3,870 dialogues** with client feedback scores **< 70**
  - [Llama-3.1-KokoroChat-High](https://huggingface.co/UEC-InabaLab/Llama-3.1-KokoroChat-High): fine-tuned on **2,601 dialogues** with client feedback scores between **70 and 98**
  - [Llama-3.1-KokoroChat-Full](https://huggingface.co/UEC-InabaLab/Llama-3.1-KokoroChat-Full): fine-tuned on **6,471 dialogues** with client feedback scores **≤ 98**
- 📄 **Paper**: [ACL 2025 Paper](https://aclanthology.org/2025.acl-long.608/)