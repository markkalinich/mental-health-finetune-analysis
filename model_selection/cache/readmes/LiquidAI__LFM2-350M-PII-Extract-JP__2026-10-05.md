---
library_name: transformers
language:
- ja
base_model:
- LiquidAI/LFM2-350M
license: other
license_name: lfm1.0
license_link: LICENSE
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</center>

<br>

（[_日本語はこちらから_](#lfm2-350m-pii-extract-jp-日本語)）

# LFM2-350M-PII-Extract-JP

Based on [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M), this checkpoint is designed to **extract personally identifiable information (PII) from Japanese text and output it in JSON format.**
The output can then be used to mask out sensitive information in contracts, emails, personal medical reports, insurance bills, etc. directly on-device.

In particular, it is trained to extract:
* Address/locations (JSON key: `address`)
* Company/institute/organization names (JSON key: `company_name`)
* Email addresses (JSON key: `email_address`)
* Human names (JSON key: `human_name`)
* Phone numbers (JSON key: `phone_number`)
from Japanese documents and texts.

### Demo

<video src="https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/z5og84hVLGgIm1Z2c98PP.mp4" controls preload></video>
Running on a macbook pro.

## Extraction Quality 

We evaluated several models, including GPT-5 and a 32B-parameter Qwen3 model with thinking mode enabled.  
The image below shows the average recall score on 1,000 random samples, chunked into segments of 100–1,000 characters, taken from [finepdf](https://huggingface.co/datasets/HuggingFaceFW/finepdfs).  
Overall, we found **LFM2-350M-PII-Extract-JP** to achieve GPT-5–level performance with only 350 million parameters—bringing cloud-grade performance to on-device applications!

![Model Size vs Recall Score](https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/ToNbcFk-7Pyr-aReyErEm.png)

### Sample Responses

<table>
  <colgroup>
    <col style="width: 50%">
    <col style="width: 50%">
  </colgroup>
  <thead>
    <tr>
      <th>Input text</th>
      <th>Output JSON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>田中　太郎 様<br><br>平素より格別のご高配を賜り、誠にありがとうございます。<br><br>このたび、山田　花子 が ABCコーポレーション赤坂オフィス へ 田中　太郎 様をご招待いたしました。<br><br>ご来訪当日は、本メールに記載の「受付番号」または「受付QRコード」を使用してチェックインを行っていただきます。以下のいずれかの方法でご準備をお願いいたします。<br><br>・本メールを印刷してご持参いただく<br>・スマートフォンで本メールを表示いただく<br><br>■ご来訪情報<br>受付番号: 594813<br>日付: 2025-10-03<br>時間: 11:00<br>担当者: 山田　花子<br>場所: 東京都港区赤坂1-2-3 赤坂ビジネスタワー5階</td>
      <td>{"address": ["東京都港区赤坂1-2-3 赤坂ビジネスタワー5階"], "company_name": ["ABCコーポレーション赤坂オフィス"], "email_address": [], "human_name": ["田中　太郎", "山田　花子"], "phone_number": []}</td>
    </tr>
    <tr>
      <td>山口さん<br><br>CCに佐藤さんも追加させていただきました<br><br>打ち合わせ可能なお時間をご連絡いただきありがとうございます。<br>佐藤さんたちは御社との初回の打ち合わせのため、御社についての基本的なところからご紹介いただく場としていただき、<br>お忙しいところ恐縮ですが、我々の打ち合わせについては別枠として、１０月８日（水）１７：００～の佐藤さんたちとの打ち合わせの後に開催はいかがでしょうか。<br><br>終了時間が１８時を過ぎてしまう可能性が高いため、ご都合が悪ければ別日で調整させてください。<br>お手数をおかけしますが、ご確認のほどどうぞよろしくお願いいたします。<br><br>中村　正信<br><br>Email: nakamura@japan.co.jp</td>
      <td>{"address": [], "company_name": [], "email_address": ["nakamura@japan.co.jp"], "human_name": ["山口", "佐藤", "中村　正信"], "phone_number": []}</td>
    </tr>
    <tr>
      <td>差出人： モンスタカード株式会社（自動配信）<br>件名： 【モスカードフリー】ご利用内容のお知らせ<br><br>⸻<br><br>夢野 みな 様<br><br>いつもモスカードフリーをご利用いただきありがとうございます。<br>お客様のカードご利用内容をお知らせいたします。<br><br>⸻<br><br>ご利用内容<br>	•	利用日：2025年10月6日 18:38:15<br>	•	利用先：ライトペイ<br>	•	ご利用金額：1000円<br>	•	承認番号：294816<br></td>
      <td>{"address": [], "company_name": ["モンスタカード株式会社", "ライトペイ"], "email_address": [], "human_name": ["夢野 みな"], "phone_number": []}</td>
    </tr>
    <tr>
      <td>株式会社ネットワークソリューションズ<br><br>請求書<br><br>発行日：2024年10月27日<br>請求番号：NS-20241027-001<br><br>田中電気工業<br>東京都渋谷区神南1-23-10<br>電話番号：+81373453302<br><br>--------------------------------------------------------------------------------<br><br>**請求先**<br><br>伊藤潔文 様<br>ryuma@izumiya.cloud<br><br>--------------------------------------------------------------------------------<br></td>
      <td>{"address": ["東京都渋谷区神南1-23-10"], "company_name": ["株式会社ネットワークソリューションズ", "田中電気工業"], "email_address": ["ryuma@izumiya.cloud"], "human_name": ["伊藤潔文"], "phone_number": ["+81373453302"]}</td>
    </tr>
    <tr>
      <td>機材等借用書（一般化・架空化済）<br><br>作成日：2025年4月18日<br><br>貸主：ネオテック株式会社<br>住所：東京都中央区銀星町三丁目<br>担当者：山田　廉（yamada@neotech.example.jp）<br><br>借主：グローバルデバイスホールディングス株式会社<br>住所：東京都新都区青海一丁目<br>担当者：佐藤　翔（sato@globaldevices.example.com）<br><br>⸻<br><br>借用物品のリスト<br>- スマートフォン　型番：Nova X10 Pro　数量：1台　状態：良好<br>- モデル（Conversa 1B LFM, Conversa 3B LFM, Focus 1B LFM, Focus 1B VLM）<br><br>⸻<br><br>借用条件<br>- 借用期間：2025年4月18日から2025年6月30日まで<br>- 借用目的：オンデバイスモデルの動作検証<br>- 使用責任：物品は善良な管理者の注意をもって使用し、破損した場合は貸主に即時報告すること。<br>- 紛失・盗難時の対応：同等の物品を貸主に弁償すること。<br><br>⸻<br><br>貸主署名：中島　誠一<br>借主署名：高橋　健吾</td>
      <td>{"address": ["東京都中央区銀星町三丁目", "東京都新都区青海一丁目"], "company_name": ["ネオテック株式会社", "グローバルデバイスホールディングス株式会社"], "email_address": ["yamada@neotech.example.jp"], "human_name": ["中島　誠一", "山田　廉", "佐藤　翔"], "phone_number": []}</td>
    </tr>
  </tbody>
</table>

> [!NOTE]  
> 📝 While LFM2-350M-PII-Extract-JP provides strong out-of-the-box PII entity extraction for the categories listed above, our primary goal is to deliver a versatile, community-driven base model—a foundation that makes it easy to build best-in-class, privacy-focused masking systems.  
>  
> Like any base model, there remain areas for continued development, particularly for specialized use cases:  
> - Supporting extraction of organization-specific identification numbers
> - Expanding coverage to additional categories such as date of birth, passport numbers
> - Further improving extraction performance on particular categories
> 
> These are precisely the kinds of challenges that fine-tuning—by both Liquid AI and our developer community can address. We see this model not just as an endpoint, but as a catalyst for a rich ecosystem of fine-tuned PII extraction models tailored to real-world needs.

## Model Details

**Generation parameters**: We strongly recommend using greedy decoding with a `temperature=0`.

**System prompts**: This checkpoint **requires** the following system prompt:
```
Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number>
```

Note the model can handle extraction of particular entities. E.g. The model will only output human names when the system prompt is set to `Extract <human_name>`.

> [!WARNING]
> ⚠️ For best performance, ensure alphabetical order of entity categories as shown above.


**Chat template**: LFM2-PII-Extract-JP uses a ChatML-like chat template as follows:

```
<|startoftext|><|im_start|>system
Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number><|im_end|>
<|im_start|>user
こんにちは、ラミンさんに B200 GPU を 10000 台 至急請求してください。連絡先は celegans@liquid.ai (電話番号010-000-0000) で、これは C. elegans 線虫に着想を得たニューラルネットワークアーキテクチャを 今すぐ構築するために不可欠です。<|im_end|>
<|im_start|>assistant
{"address": [], "company_name": [], "email_address": ["celegans@liquid.ai"], "human_name": ["ラミン"], "phone_number": ["010-000-0000"]}<|im_end|>
```

You can automatically apply it using the dedicated [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) function from Hugging Face transformers.

> [!WARNING]
> ⚠️ The model is intended for single turn conversations.

**Output format**

The model outputs a JSON object containing the fields it was prompted to extract.
If no entities are found in a particular category, it returns an empty list for that category. 
If entities are found, they are returned as a list for each prompted category.
The model is trained to output entities exactly as they appear in the text. 
If the same entity appears multiple times with slight formatting variations, the model outputs all variations to ensure subsequent masking can be performed using exact matches.


## 🏃 How to run LFM2

- Huggingface: [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M)
- llama.cpp: [LFM2-350M-PII-Extract-JP-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP-GGUF)
- LEAP: [LEAP model library](https://leap.liquid.ai/models?model=lfm2-350m-pii-extract-jp)

You can use the following Colab notebooks for easy inference and fine-tuning:

| Notebook | Description | Link |
|-------|------|------|
| Inference | Run the model with Hugging Face's transformers library. | <a href="https://colab.research.google.com/drive/1kIaBNZYZSZ9wzrl9Yot3W5ZKR1lf47k1?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (TRL) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using TRL. | <a href="https://colab.research.google.com/drive/1j5Hk_SyBb2soUsuhU0eIEA9GwLNRnElF?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| DPO (TRL) | Preference alignment with Direct Preference Optimization (DPO) using TRL. | <a href="https://colab.research.google.com/drive/1MQdsPxFHeZweGsNx4RH7Ia8lG8PiGE1t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Axolotl) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using Axolotl. | <a href="https://colab.research.google.com/drive/155lr5-uYsOJmZfO6_QZPjbs8hA_v8S7t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Unsloth) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using Unsloth. | <a href="https://colab.research.google.com/drive/1HROdGaPFt1tATniBcos11-doVaH7kOI3?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

## Citation

```
@article{liquidai2025lfm2,
 title={LFM2 Technical Report},
 author={Liquid AI},
 journal={arXiv preprint arXiv:2511.23404},
 year={2025}
}
```

# LFM2-350M-PII-Extract-JP (日本語)

[**LFM2-350M**](https://huggingface.co/LiquidAI/LFM2-350M) をベースにしたこのチェックポイントは、**日本語文書から個人を特定できる情報（PII）を抽出し、JSON 形式で出力します**。  
契約書、電子メール、個人の医療報告書、並びに保険請求書などの機密情報を、デバイス上で直接マスキングできます。

特に以下の情報を抽出するように訓練されています。
* 住所／所在地（JSON key: `address`）
* 企業／研究機関／組織名（JSON key: `company_name`）
* メールアドレス（JSON key: `email_address`）
* 人名（JSON key: `human_name`）
* 電話番号（JSON key: `phone_number`）

これらの情報を日本語の文書から抽出します。

---

### デモ

<video src="https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/z5og84hVLGgIm1Z2c98PP.mp4" controls preload></video>

---

## 性能

[**finepdf**](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) から無作為に抽出した 1,000 サンプルを用いて、GPT5 や 32B パラメータの Qwen3 モデル（思考モードあり）など、複数のモデルとの比較評価を行いました。  
**LFM2-350M-PII-Extract-JP** は、わずか **350M パラメータ** という軽量モデルながら GPT5 と同等レベルの性能を発揮し、クラウドレベルの品質をあなたのデバイス上で実現します！

![Model Size vs Recall Score](https://cdn-uploads.huggingface.co/production/uploads/65d6b6c1a07ad79084a0d214/ToNbcFk-7Pyr-aReyErEm.png)

> [!NOTE]  
> 📝 LFM2-350M-PII-Extract-JP は、上記カテゴリに対して優れた PII 抽出性能を有しますが、私たちの主な目的は、**コミュニティによって継続的に改良される柔軟な基盤モデルを提供すること**です。  
> このモデルで、誰でもプライバシー重視の高品質なマスキングシステムを容易に構築できます。  
>  
> ただし、ベースモデルとして今後さらなる改善の余地があります。特に以下のような専門的な利用用途が想定されます。 
> - 組織固有の識別番号の抽出対応  
> - 生年月日、パスポート番号などの追加カテゴリへの拡張  
> - 特定カテゴリにおける抽出性能のさらなる改善 
>
> これらの課題は、**Liquid AI** および開発者コミュニティによるファインチューニングによって解決できると考えています。  
> LFM2-350M-PII-Extract-JP は完成形ではなく、**実運用ニーズに応じた多様な PII 抽出モデル群を生み出す出発点**であると位置づけています。

---

## モデル詳細

**生成パラメータ**: `temperature=0` の貪欲デコード（greedy decoding）の使用を強く推奨します。

**システムプロンプト**: このチェックポイントでは以下のシステムプロンプトが**必須**です：

```
Extract <address>, <company_name>, <email_address>, <human_name>, <phone_number>
```

モデルは特定のエンティティのみを抽出するように設定することも可能です。  
例: `Extract <human_name>` と設定した場合、人名のみを出力します。

> [!WARNING]
> ⚠️ モデルの性能を最大限発揮させるには、上記のように **エンティティカテゴリをアルファベット順** に並べてください。

---

**チャットテンプレート**  
LFM2-PII-Extract-JP は以下のような ChatML 風テンプレートを使用します。

```
<|startoftext|><|im_start|>system
Extract , <company_name>, <email_address>, <human_name>, <phone_number><|im_end|>
<|im_start|>user
こんにちは、ラミンさんに B200 GPU を 10000 台 至急請求してください。連絡先は celegans@liquid.ai (電話番号010-000-0000) で、これは C. elegans 線虫に着想を得たニューラルネットワークアーキテクチャを 今すぐ構築するために不可欠です。<|im_end|>
<|im_start|>assistant
{“address”: [], “company_name”: [], “email_address”: [“celegans@liquid.ai”], “human_name”: [“ラミン”], “phone_number”: [“010-000-0000”]}<|im_end|>
```

このテンプレートは、Hugging Face Transformers の専用関数 [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) を使用して自動的に適用できます。

> [!WARNING]
> ⚠️ このモデルは **一問一答形式　（単一ターン）　の会話** に最適化されています。

---

**出力形式**

モデルは、指定されたエンティティを含んだ JSON 形式で出力します。  
各カテゴリに該当するエンティティが見つからない場合は、空のリストを返します。  
該当するエンティティが存在する場合は、そのカテゴリごとに抽出された文字列のリストを返します。  

モデルは、**テキスト中に現れる形式で正確にエンティティを出力**するように訓練されています。  
同じエンティティが複数回登場し表記に揺れがある場合でも、すべての表記バリエーションを出力し、マスキング時に完全一致で対応できるようになっています。

---

## 🏃 LFM2 の実行方法

- Hugging Face: [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M)
- llama.cpp: [LFM2-350M-PII-Extract-JP-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP-GGUF)
- LEAP: [LEAP モデルライブラリ](https://leap.liquid.ai/models?model=lfm2-350m-pii-extract-jp)

| ノートブック | 説明 | リンク |
|-------|------|------|
| 推論 | Hugging Faceのtransformersライブラリを使用してモデルを実行します。 | <a href="https://colab.research.google.com/drive/1kIaBNZYZSZ9wzrl9Yot3W5ZKR1lf47k1?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (TRL) | TRLを使用したLoRAアダプターによる教師あり学習（SFT）を行います。 | <a href="https://colab.research.google.com/drive/1j5Hk_SyBb2soUsuhU0eIEA9GwLNRnElF?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| DPO (TRL) | TRLを使用したDPOによる選好アライメントを行います。 | <a href="https://colab.research.google.com/drive/1MQdsPxFHeZweGsNx4RH7Ia8lG8PiGE1t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Axolotl) | Axolotlを使用したLoRAアダプターによる教師あり学習（SFT）を行います。 | <a href="https://colab.research.google.com/drive/155lr5-uYsOJmZfO6_QZPjbs8hA_v8S7t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Unsloth) | Unslothを使用したLoRAアダプターによる教師あり学習（SFT）を行います。 | <a href="https://colab.research.google.com/drive/1HROdGaPFt1tATniBcos11-doVaH7kOI3?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |

---

## 📬 お問い合わせ

エッジ環境への導入を含むカスタムソリューションにご興味がある方は、[営業チーム](https://www.liquid.ai/ja/contact)までお問い合わせください。

## 引用

```
@article{liquidai2025lfm2,
 title={LFM2 Technical Report},
 author={Liquid AI},
 journal={arXiv preprint arXiv:2511.23404},
 year={2025}
}
```