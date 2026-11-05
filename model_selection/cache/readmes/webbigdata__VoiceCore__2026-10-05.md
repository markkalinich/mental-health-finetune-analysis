---
language:
- ja
base_model:
- canopylabs/orpheus-3b-0.1-pretrained
tags:
- audio
- tts
- csm
- agent
- japanese
- voice-synthesis
- emotional-tts
- voice generation
- voice agent
- orpheus
- voice dialog
- text-to-speech
---

![image/png](voice-core-logo-mini.png)

# News

2026年03月24日  
VoiceCoreを利用した提案「タクシー配車業務のAI音声対応」が[GENIAC-PRIZE<NEDO懸賞金活用型プログラム>コンペ「国産基盤モデル等を活用した社会課題解決AIエージェント開発」の領域２「カスタマーサポートの生産性向上」部門において優勝](https://geniac-prize.nedo.go.jp/)されたそうです。  
おめでとうございます！  

The proposal ["AI Voice Support for Taxi Dispatch Operations," utilizing VoiceCore, has won first place in the GENIAC-PRIZE competition "Development of AI Agents for Solving Social Issues Using Domestic Platform Models, etc."](https://geniac-prize.nedo.go.jp/)  
Congratulations!  

2026年03月18日  
VoiceCoreを利用した提案がGENIACコンペ「カスタマーサポートの生産性向上」の決勝に進出したそうです。  
おめでとうございます！  

A proposal utilizing VoiceCore has advanced to the finals of the GENIAC competition, "Improving Customer Support Productivity."  
Congratulations!  

2025年11月23日  
VoiceCoreがGENIACプロジェクト(経済産業省、NEDO)の国産基盤モデルリストに掲載されました。  
これにより日本国内の法人、団体はVoiceCoreを使って[1位の懸賞金が5000万円であるGENIAC-PRIZE(NEDO懸賞金活用型プログラム)に応募](https://geniac-prize.nedo.go.jp/)する事が可能になりました。  
単独でもお申込みできますが[VoiceCoreは商用サポートも承っておりますので、ご希望の方はこちら](https://webbigdata.jp/voice-ai-agent/)からご相談ください  

VoiceCore has been listed on the National foundation model list of the GENIAC project (Ministry of Economy, Trade and Industry, NEDO).  
This means that Japanese corporations and organizations can now use VoiceCore to apply for the [GENIAC-PRIZE (NEDO Prize Fund Utilization Program), which offers a first place prize of 50 million yen.](https://geniac-prize.nedo.go.jp/)   
You can apply for it alone, but [we also offer commercial support for VoiceCore, so if you are interested, please contact here.](https://webbigdata.jp/voice-ai-agent/)


# VoiceCore - 次世代 日本語Voice AI Agent用モデル (VoiceCore - Next-Gen Japanese Voice AI Agent model)

VoiceCoreはAIが自然な日本語を発声可能にする商用利用可能なVoice AI Agentモデルです。  
従来のTTS(Text to Speech:音声合成)ソフトウェアと異なる点は、文章を正確に発声する事は目的ではなく、AIが音声を使った意思疎通を人間とするために設計されており、笑い声などの非言語音声や感情表現が可能な事が特徴です。   
VoiceCore is a commercially available Voice AI Agent model that enables AI to speak natural Japanese.    
What makes it different from conventional TTS (Text to Speech) software is that its goal is not to accurately recite sentences, but rather it is designed to enable AI to communicate with humans using voice, and is characterized by its ability to use non-verbal speech(eg:laughting) and express emotions.  

## モデルの動かし方(How to run)

以下のページでVoiceCoreの音声合成品質をオンラインで確認する事ができます  
- [VoiceCore_online](https://webbigdata.jp/voice-ai-agent/VoiceCore_online/)

You can check the quality of VoiceCore's voice synthesis online at the following page:
- [VoiceCore online](https://webbigdata.jp/voice-ai-agent/VoiceCore_online/)

以下のサンプルスクリプトを使うとGoolgeが提供するColabratoryで無料で動作確認する事ができます
- [Colab用サンプルスクリプト](https://github.com/webbigdata-jp/VoiceCore/blob/main/VoiceCore_sample.ipynb)

You can use the following sample script to check the operation for free on Colaboratory provided by Google  
- [Sample script for Colab](https://github.com/webbigdata-jp/VoiceCore/blob/main/VoiceCore_sample.ipynb)  

MacやCPU環境向けに[ggufフォーマット版](https://huggingface.co/webbigdata/VoiceCore_gguf)も提供されています。  
A [gguf format version](https://huggingface.co/webbigdata/VoiceCore_gguf) is also provided for Mac and CPU environments.  

NvidiaやAMDの高性能GPUをお持ちの方向けに高速推論ツールであるvLLM用の[8bit smoothquant版](https://huggingface.co/webbigdata/VoiceCore_smoothquant)も用意されています。  
For those with high-performance Nvidia or AMD GPUs, a [8bit smoothquant version](https://huggingface.co/webbigdata/VoiceCore_smoothquant) for vLLM(High-speed inference tools) is also available.  

更にモデルを圧縮し、高速化した[4bit gptq版](https://huggingface.co/webbigdata/VoiceCore_gptq)も用意されています。  
A [4-bit gptq version](https://huggingface.co/webbigdata/VoiceCore_gptq) is also available, which further compresses the model and speeds it up.  

その他の使い方、声の指定方法や設計思想などの解説は「[VoiceCoreの基本的な使い方 – 感情豊かなAIエージェント向け音声合成モデル](https://webbigdata.jp/post-21268/)」をご覧ください  
For other usage, voice specification methods, and design philosophy, please see "[Basic usage of VoiceCore - A speech synthesis model for emotive AI agents](https://webbigdata.jp/post-21268/)".  

## ディフォルト利用可能な音声の提供元とそのライセンス (Default voice providers and their licenses)

各声は商用可能ですが、提供者様により用途制限と連絡・クレジット表記義務が異なります。  
Each voice can be used commercially, but usage restrictions and contact/credit obligations vary depending on the provider.  

女性の声はプレビュー版の位置づけです。現在は高音域でノイズが乗ってしまう傾向があります。  
The female voice is a preview version. Currently, there is a tendency for high-pitched voices to have noise.  

| 声のタイプ | 商用利用 | 使用不可コンテンツ | クレジット表記 | 提供元 | ライセンス詳細/問い合わせ先 |
|----------|---------|-------------------|---------------|--------|-------------------------|
| **amitaro_female**<br>(明るい女の子) | ⭕ 可能<br>(要事後報告) | ❌ エロ・グロ<br>❌ 政治・宗教<br>❌ ヘイト | ✅ 必須<br>「あみたろの声素材工房」 | あみたろの声素材工房 | [ライセンス詳細](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/amitaro/Readme_20240621.txt) / [問い合わせ先](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/amitaro/url.txt) |
| **matsukaze_male**<br>(さわやかな男性) | ⭕ 可能 | 制限なし | ✅ 必須(CC-BY)<br>松風 | 松風 |[ライセンス詳細](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/matsukaze/licence.txt) / [問い合わせ先](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/matsukaze/url.txt)|
| **naraku_female**<br>(落ち着いた女性) | ⭕ 可能<br>(商用は要連絡) | ❌ 反社・政治・宗教<br>❌ 品位を損なう行為 | 個人利用：❌ 不要<br>商用利用：✅ 必須「極楽唯」 | VTuber 奈落ゆい | [ライセンス詳細](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/naraku/readme%EF%BC%88%E5%A5%88%E8%90%BD%E3%82%86%E3%81%84ITA%EF%BC%89.txt)  / [問い合わせ先](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/naraku/url.txt)|
| **shiguu_male**<br>(大人びた少年) | ⭕ 可能<br>(商用は要連絡) | ❌ 品位を損なう行為<br>❌ 政治・宗教 | ✅ 必須<br>「刻鳴時雨（CV:丸ころ）」 | 瓶詰め/丸ころ | [ライセンス詳細](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/shiguu/%E8%AA%AD%E3%82%93%E3%81%A7%E3%81%AD.txt) / [利用規約]( https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/shiguu/Term_of_use.txt )/ [問い合わせ先](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/shiguu/url.txt)|
| **sayoko_female**<br>(一般81歳女性) | ⭕ 可能 | ❌ エロ・グロ | ✅ 必須<br>「Fusic サヨ子音声コーパス」 | Fusic/bandad | [ライセンス詳細](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/sayoko/README.md) / [問い合わせ先](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/sayoko/url.txt)|
| **nekketsu_female**<br>(熱血ヒロイン) | ⭕ 可能<br>(商用は要連絡)  | ❌ 悪用（詐欺的広告、フェイクニュース／動画、差別・中傷など） | ✅ 任意<br>「紅葉美兎及びAI生成音声である事」を明記 | 紅葉美兎 | [ライセンス詳細](https://ssl.form-mailer.jp/fms/82585013867391) / [問い合わせ先](https://kurehamiu.com/voicecore-guide/)|
| **dahara1_male**<br>(一般男性) | ⭕ 可能 | 制限なし | ✅ 任意<br>(apache2) | webbigdata | [ライセンス詳細](https://www.apache.org/licenses/LICENSE-2.0) / [問い合わせ先](https://webbigdata.jp/webbigdata/inquiry/)|

- **商用利用時の連絡**: naraku、shiguu, nekketsuは商用利用時に事前連絡が必要。amitaroは事後連絡可
- **再配布禁止**: 素材としての再配布・販売は禁止
- **加工**: 音声の加工・編集は可能
- **使用許諾**: 上記の声提供者の皆さんには本モデルでの使用許可を直接頂いております。この許可はあらゆるAI/モデル/形態を想定した許可ではない事に留意してください

| Voice Type | Commercial Use | Prohibited Content | Credit Required | Provider | License Details/Contact |
|----------|---------|-------------------|---------------|--------|-------------------------|
| **amitaro_female**<br>(Cheerful girl) | ⭕ Allowed<br>(Post-use notification required) | ❌ Adult/Gore<br>❌ Political/Religious<br>❌ Hate speech | ✅ Required<br>"Amitaro's Voice Material Studio" | Amitaro's Voice Material Studio | [License Details](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/amitaro/Readme_20240621.txt) / [Contact](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/amitaro/url.txt) |
| **matsukaze_male**<br>(Refreshing male) | ⭕ Allowed | No restrictions | ✅ Required (CC-BY)<br>Matsukaze | Matsukaze |[License Details](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/matsukaze/licence.txt) / [Contact](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/matsukaze/url.txt)|
| **naraku_female**<br>(Calm woman) | ⭕ Allowed<br>(Commercial use requires prior contact) | ❌ Anti-social/Political/Religious<br>❌ Dignity-damaging acts | Personal use: ❌ Not required<br>Commercial use: ✅ Required<br>"gokuraku yui" | VTuber Naraku Yui | [License Details](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/naraku/readme%EF%BC%88%E5%A5%88%E8%90%BD%E3%82%86%E3%81%84ITA%EF%BC%89.txt) / [Contact](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/naraku/url.txt)|
| **shiguu_male**<br>(Mature boy) | ⭕ Allowed<br>(Commercial use requires prior contact) | ❌ Dignity-damaging acts<br>❌ Political/Religious | ✅ Required<br>"Tokina Shigure (CV: Marukoro)" | Binzume/Marukoro | [License Details](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/shiguu/%E8%AA%AD%E3%82%93%E3%81%A7%E3%81%AD.txt) / [Terms of Use](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/shiguu/Term_of_use.txt) / [Contact](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/shiguu/url.txt)|
| **sayoko_female**<br>(81-year-old woman) | ⭕ Allowed | ❌ Adult/Gore | ✅ Required<br>"Fusic Sayoko Voice Corpus" | Fusic/bandad | [License Details](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/sayoko/README.md) / [Contact](https://huggingface.co/webbigdata/VoiceCore/blob/main/voice_license/sayoko/url.txt)|
| **nekketsu_female**<br>(Hot-blooded heroine) | ⭕ Allowed<br>(Commercial use requires prior contact) | ❌ Malicious use (fraudulent advertising, fake news/videos, discrimination/defamation, etc.) | ✅ Optional<br>Must specify "Kureha Miu and AI-generated voice" | Kureha Miu | [Kureha Miu](https://ssl.form-mailer.jp/fms/82585013867391) / [Contact](https://kurehamiu.com/voicecore-guide/)|
| **dahara1_male**<br>(General male) | ⭕ Allowed | No restrictions | ✅ Optional<br>(apache2) | webbigdata | [License Details](https://www.apache.org/licenses/LICENSE-2.0) / [Contact](https://webbigdata.jp/webbigdata/inquiry/)|

- **Commercial use contact**: naraku, shiguu and nekketsu require prior contact for commercial use. amitaro allows post-use notification
- **Redistribution prohibited**: Redistribution or sale as material is prohibited
- **Modification**: Voice modification and editing are allowed
- **Permission to Use**: All voice providers listed above have given us direct permission to use their voices in this model. Please note that this permission does not cover all AI/models/forms.

## モデルの微調整方法(How to finetune)

以下のサンプルスクリプトを使うとGoolgeが提供するColabratoryで無料で微調整を行い、英語能力の向上や独自音声追加を体験する事ができます。  
- [微調整サンプルスクリプト](https://github.com/webbigdata-jp/VoiceCore)

Using the sample script below, you can finetune it for free with Colaboratory provided by Google, and experience improving model's English skills and adding your own voice.  
- [finetune sample script](https://github.com/webbigdata-jp/VoiceCore)

## 使用/参考にした研究/データセット ( Datasets and Research used/referenced )
以下のデータセット / コーパスを開発時に利用/参考にさせて頂いています。データセット、コーパスの提供者の皆様に感謝いたします。  
The following datasets/corpora were used/referenced during development. We would like to express our gratitude to the providers of the datasets and corpora.  

- [ITAコーパス(text)](https://github.com/mmorise/ita-corpus)
- [mana-corpus(text)](https://github.com/shirowanisan/coeiroink-corpus-manager)
- [あみたろの声素材工房](https://amitaro.net/)
- [松風ITA/manaコーパス朗読データ](https://x.com/mochi_jin_voice/status/1424789247014309888)
- [バーチャルシンガー 刻鳴時雨ITAコーパス朗読データ](https://bindumechan.wixsite.com/shigure222)
- [バーチャルアイドル 奈落ゆいITAコーパス朗読データ](https://narakuyui.wixsite.com/my-site)
- [Fusic/サヨ子音声コーパス](https://huggingface.co/datasets/bandad/sayoko-tts-corpus)
- [freevoice4creators](https://freevoice4creators.com/)
- [JVNV: a Japanese emotional speech corpus with both verbal content and nonverbal vocalizations](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvnv_corpus)
- Webbigdata original dataset (Private)

## モデル詳細 / Model Detail

モデル愛称：webbigdata/VoiceCore  
Model nickname: webbigdata/VoiceCore  

ベースモデル: [Orpheus TTS](https://huggingface.co/collections/canopylabs/orpheus-tts-67d9ea3f6c05a941c06ad9d2) ([Llamaアーキテクチャ](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)を利用しています)  
Base Model: [Orpheus TTS](https://huggingface.co/collections/canopylabs/orpheus-tts-67d9ea3f6c05a941c06ad9d2) (which utilizes [Llama architecture](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct))  

モデルライセンス: 解釈に応じて、[LLAMA 3.2 COMMUNITY LICENSE](https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/LICENSE.txt)または[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)のいずれかを選択できます。これは、Orpheusが独自のカスタム音声トークンを出力し、Llama3.2の出力ではなく、変形的/派生的な著作物として解釈できるためです。念の為ですがどちらも商用利用を許諾しているライセンスです。  
Model License: Depending on your interpretation, you can choose either the [LLAMA 3.2 COMMUNITY LICENSE](https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/LICENSE.txt) or the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). This is because Orpheus outputs its own custom voice tokens and can be interpreted as a transformative/derivative work, not the output of Llama 3.2. Just to be clear, both licenses allow commercial use.  

本モデルは、[canopylabs/orpheus-3b-0.1-pretrained](https://huggingface.co/canopylabs/orpheus-3b-0.1-pretrained) に継続事前学習と事後学習を行ったモデルです。学術的な正式名称は論文発表時に決定される予定です。  
This model is a model that has been subjected to continuous pre-training and post-training on [canopylabs/orpheus-3b-0.1-pretrained](https://huggingface.co/canopylabs/orpheus-3b-0.1-pretrained). The official academic name will be decided at the time of publication of the paper.  

## 技術仕様 / Technical Specifications

- モデルパラメータ数 37億(3B)
- bf16推論時の必要GPUメモリ目安 約8GB
- 音声ファイルサンプリングレート 24khz
- TensorRT LLM環境での実測値  
RTX 4060ti(メモリ帯域幅:288GB/秒)  
 bf16 約40 tokens/sec  
 fp8 約65 tokens/sec  
RTX 3090(メモリ帯域幅936GB/秒)  
 bf16 約100 tokens/sec  
リアルタイム会話を実現するためには70 tokens/秒以上の性能が必要です  

- Number of model parameters: 3.7 billion (3B)
- Estimated GPU memory required for bf16 inference: approx. 8GB
- Audio file sampling rate: 24khz
- Actual measurements in TensorRT LLM environment  
RTX 4060ti (memory bandwidth: 288GB/sec)  
 bf16 approx. 40 tokens/sec  
 fp8 approx. 65 tokens/sec  
RTX 3090 (memory bandwidth 936GB/sec)  
 bf16 approx. 100 tokens/sec  
 To achieve real-time conversation, a performance of 70 tokens/sec or more is required.

## 利用者アンケート / User Survey

私達はユーザーからの反響を非常に重視しています。  
[Googleフォームに感想や今後期待する方向性、気が付いた誤りの例、ディフォルトボイスへの採用希望などを是非とも記入](https://docs.google.com/forms/d/e/1FAIpQLScA9L8rQwqhUA9vbpUxKbIVPaQWqy7gnC-tFyrYwHdNnpTP2A/viewform?usp=dialog)してください。  

We place great importance on user feedback.  
Please fill out the [Google form with your thoughts, your desired future direction, examples of errors you've noticed, and any requests you'd like to see included as default voices.](https://docs.google.com/forms/d/e/1FAIpQLScA9L8rQwqhUA9vbpUxKbIVPaQWqy7gnC-tFyrYwHdNnpTP2A/viewform?usp=dialog)


## 法人・ビジネスでのご利用について (For Business Users)
この[モデルに関する商用サポート、カスタム開発、コンサルティング等のご相談は、以下の法人向けウェブサイト](https://webbigdata.jp/voice-ai-agent/)より承っております。  
For [commercial support, custom development, or professional consulting, please visit our corporate website](https://webbigdata.jp/voice-ai-agent/).  

## 残TODO
- MCPで動かす方法の解説(how to MCP)
- より様々なツールなどでの動かすための解説(more more documents)

## 謝辞 / Acknowledgment
全ての合成音声の研究者/愛好家/声データ提供者の皆様。彼らの研究成果/データ/熱意がなけなければ、このモデルは完成できなかったでしょう。直接使用しなかったデータ/知識などにも大いに影響/励ましを受けました。  
To all researchers and enthusiasts of synthetic speech, Voice data provider. Without their research results, data, and enthusiasm, this model would not have been completed. I was also greatly influenced and encouraged by data and knowledge that I did not directly use.  

- [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- [canopylabs/orpheus-tts](https://huggingface.co/collections/canopylabs/orpheus-tts-67d9ea3f6c05a941c06ad9d2)
- [hubertsiuzdak/snac_24khz](https://huggingface.co/hubertsiuzdak/snac_24khz)
- [unslothai/unsloth](https://unsloth.ai/) for for providing a memory-efficient training method.
- [pytorch/torchtune](https://github.com/pytorch/torchtune) for providing a variety of training methods.
- [Huggingface](https://huggingface.co/) for storage.

## Developer/開発
- **Developed by:** dahara1@webbigdata
- **Model type:** text audio generation
- **Language(s) (NLP):** Japanese
- **model :** [webbigdata/VoiceCore](https://huggingface.co/webbigdata/VoiceCore)

**BibTeX:**
```
@misc{dahara2025 VoiceCore,
  author       = {dahara1@webbigdata},
  title        = {VoiceCore - Next-Gen Japanese Voice AI Agent model},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/webbigdata/VoiceCore}},
  note         = {Accessed: 2025-07-18},
  abstract     = {This model is designed to enable AI to communicate with humans using voice, and is characterized by its ability to use non-verbal speech and express emotions.},
}
```