---
license: apache-2.0
license_link: LICENSE
language:
- ja
library_name: transformers
pipeline_tag: text-generation
inference: false
tags:
- medical
- japanese
- nedo
---

# medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft

本モデルは、[NEDO（国立研究開発法人新エネルギー・産業技術総合開発機構）「AIの安全性確保に関する研究開発・検証等の推進事業 / 日本語版医療特化型LLMの社会実装に向けた安全性検証・実証」](https://www.nedo.go.jp/activities/ZZJP_100327.html)において開発された医療特化型大規模言語モデルであり、東京大学開発チーム内の **医療PJ Team** による「日本語医療LLMに対する事後学習手法の比較研究」の成果物です。

手法検証を目的とした研究成果の公開であり、[プレスリリース](https://www.t.u-tokyo.ac.jp/press/pr2026-07-08-001)の「Weblab-MedLLM-Qwen3-235B-Instruct」とは異なり実運用向けの調整・安全性検証は行われていません。

「Weblab-MedLLM-Qwen3-235B-Instruct」とは事前学習データ量が異なります。(Weblab-MedLLM-Qwen3-235B-Instructが事前学習データ量が多い)事後学習のデータや手法については、「Weblab-MedLLM-Qwen3-235B-Instruct」と同じものになります。**** 詳細は「[モデルの特徴と性能](#モデルの特徴と性能)」をご確認ください。

**臨床現場での直接利用は推奨されません。**** 詳細は「[利用にあたっての注意事項](#利用にあたっての注意事項)」をご確認ください。

## モデルの概要

| 項目 | 内容 |
|------|------|
| モデル名 | medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft |
| ベースモデル |  [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)|
| パラメータ数 | 235B MoE |
| 事後学習手法 | DFT（Dynamic Fine-Tunning） |
| 学習フレームワーク | ms-swift + Megatron-LM (v3.8.1) |
| 言語 | 日本語 |
| 開発者 | 東京大学大学院工学系研究科 松尾・岩澤研究室 医療PJ Team |
| 事業名 | [NEDO JPNP25006](https://www.nedo.go.jp/activities/ZZJP_100327.html) |
| 本モデルライセンス | [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)  |
| ソースコード | https://github.com/weblab-llm-m/singularity-post-training-medical |

## 利用にあたっての注意事項

本モデルのご利用にあたっては、以下の点にご留意ください。

- 本プログラムは、実臨床における安全性・有効性の検証が十分に行われていません。
- 開発者は、本プログラムに関し、その正確性、完全性、最新性、および品質など、いかなる保証も行わず、利用者が本プログラムを利用したこと、利用できなかったことにより生じた一切の損害について責任を負いません。
- **医療行為（診断、治療方針の決定、健康への助言など）に直接適用することは推奨されません。あくまで医療専門家による適切な判断の補助となる情報提供ツールとしての利用にとどめることを推奨します。**
- **本モデルを活用して具体的な医療用途の製品を開発される場合、その製品が医療機器プログラムとして薬機法の規制対象となる可能性があることにご留意ください。**
  - プログラム医療機器の該当性に関する相談窓口：
  - [独立行政法人医薬品医療機器総合機構（PMDA; Pharmaceuticals and Medical Devices Agency）](https://www.pmda.go.jp/review-services/f2f-pre/strategies/0011.html)
  - 本READMEに記載のvLLM環境構築手順およびサーバー起動コマンドは参考情報であり、利用者の環境での動作を保証するものではありません。

## モデルの特徴と性能

以下に主要ベンチマークの性能を示します。括弧内はベースモデルからの変化幅です。

| モデル | 医師国試 | ガイドライン |
|-----------|------|------|
| medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft | 80.0% (+1.7) | 59.4%(+1.3) |
| Weblab-MedLLM-Qwen3-235B-Instruct | 79.6% (+1.3) | 59.5%(+1.4) |

※医師国試は、Weblab-MedLLM-Qwen3-235B-Instructより高いが非公開ベンチマークも含めて総合的に判断して、Weblab-MedLLM-Qwen3-235B-Instructをプレスリリースのモデルとして選定しました。

## 学習データ

独自に収集した医学論文・医学書籍・診療ガイドライン・試験問題などを由来とする合成データをもとに、継続事前学習および事後学習を実施しています。

## 推奨動作環境

### ハードウェア
- GPUメモリ: 約470GB（BF16精度）。H100 80GB × 6枚以上での分散推論が必要

### Python
- python>=3.9（transformersを使用する場合）
- python 3.12（vLLMを使用する場合は推奨）

### ライブラリ
- accelerate>=1.10.0
- torch>=2.8.0
- transformers>=4.55.0（本モデルのアーキテクチャに対応したバージョンが必要）
- vllm（推奨、大規模モデルの推論効率化）

## ダウンロード

`hf_transfer` を使用することで高速なダウンロードが可能です。

```bash
pip install hf_transfer
HF_HUB_ENABLE_HF_TRANSFER=1 hf download weblab-LLM-M/medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft \
    --local-dir ./medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft
```

> **注意**: `hf` コマンドは `huggingface_hub` パッケージに含まれています。未インストールの場合は `pip install huggingface_hub` を実行してください。

## vLLMを使った推論（推奨）

大規模モデルの推論効率化のため、vLLMの使用を推奨します。vLLMのインストールおよび使用方法については [vLLM公式ドキュメント](https://docs.vllm.ai/) を参照してください。

本モデルを vLLM で使用する際の主な注意点は以下の通りです。

- **最小GPU構成**: H100 80GB × 6枚以上
- **最大シーケンス長**: 256K tokens（`--max-model-len 262144`）

### 環境構築

> **注意**: ハードウェアやソフトウェアのバージョンによって動作しない場合があります。動作保証はありません。

**動作確認済み構成**

| 項目 | バージョン |
|------|----------|
| GPU | NVIDIA B200 × 8 |
| vLLM | 0.15.1 |
| PyTorch | 2.9.1+cu128 |
| CUDA | 12.8（conda環境） |
| Python | 3.12 |

**セットアップ手順**

```bash
# 1. Miniconda3のインストール
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/bin/conda init bash
source ~/.bashrc

# 2. conda環境の作成（CUDA 12.8、Python 3.12）
conda create --prefix $HOME/envs/vllm_cu128 python=3.12 -y
conda activate $HOME/envs/vllm_cu128
conda install -c nvidia cuda-toolkit=12.8 -y

# 3. vLLMのインストール（PyTorch 2.9.1+cu128 も依存として自動インストール）
pip install vllm==0.15.1

# 4. FlashInferのアップグレード
pip install flashinfer-python==0.6.3

# 5. NCCLのアップグレード（B200 Blackwellの場合のみ必要）
pip install nvidia-nccl-cu12==2.29.3 --no-deps

# 6. CUDAシンボリックリンクの設定（FlashInfer JITコンパイル用）
mkdir -p $HOME/envs/vllm_cu128/lib64/stubs
ln -sf /usr/lib/x86_64-linux-gnu/libcuda.so $HOME/envs/vllm_cu128/lib64/libcuda.so
ln -sf /usr/lib/x86_64-linux-gnu/libcuda.so.1 $HOME/envs/vllm_cu128/lib64/libcuda.so.1
```

**GPU固有の環境変数**

特定のGPUアーキテクチャ（Blackwellなど）では以下の環境変数が必要になる場合があります。

```bash
export NCCL_NVLS_ENABLE=0              # NVLink SHARP無効化（ncclCommInitRankハング対策）
export VLLM_ALLREDUCE_USE_SYMM_MEM=0   # torch symmetric memory無効化
export VLLM_USE_NCCL_SYMM_MEM=0        # NCCL symmetric memory allocator無効化
export CUDA_HOME=$CONDA_PREFIX          # FlashInfer JITコンパイル用
```

### サーバーの起動

> **注意**: 環境によって動作しない場合があります。動作保証はありません。

```bash
conda activate $HOME/envs/vllm_cu128

vllm serve ./medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft \
    --host 0.0.0.0 \
    --port 8000 \
    --served-model-name medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft \
    --tensor-parallel-size 8 \
    --pipeline-parallel-size 1 \
    --dtype bfloat16 \
    --gpu-memory-utilization 0.93 \
    --max-model-len 262144 \
    --disable-custom-all-reduce \
    --trust-remote-code \
    --enable-chunked-prefill \
    --enable-prefix-caching \
    --max-num-batched-tokens 32768 \
    --max-num-seqs 60 \
    --generation-config vllm \
    --enable-expert-parallel
```

起動後は OpenAI クライアントからアクセスできます。

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")  # 認証なしの場合は任意の文字列

response = client.chat.completions.create(
    model="medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft",
    messages=[
        {"role": "system", "content": "あなたは医療の専門知識を持つアシスタントです。"},
        {"role": "user", "content": "脳梗塞の急性期治療において、rt-PA静注療法の適応基準について説明してください。"}
    ],
    max_tokens=1024*4,
)
print(response.choices[0].message.content)
```


## transformersを使った推論

> **注意**: transformers の `device_map="auto"` はパイプライン並列による推論のため、235B MoE モデルでは数分かかることがあります。本番利用にはvLLMを推奨します。

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "./medicalpj-Qwen3-235B-A22B-Instruct-exp8-Instruction-dft"  # ダウンロード先のローカルパスを指定

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "脳梗塞の急性期治療において、rt-PA静注療法の適応基準について説明してください。"

messages = [
    {"role": "system", "content": "あなたは医療の専門知識を持つアシスタントです。"},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=1024*4,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

※ チャットテンプレートは`chat_template.jinja`として同梱されています。`tokenizer_config.json`に含まれていない場合は、手動で設定するか、vLLMでの推論をご利用ください。


## 謝辞

この成果は、[NEDO（国立研究開発法人新エネルギー・産業技術総合開発機構）の 委託業務（JPNP25006）](https://www.nedo.go.jp/activities/ZZJP_100327.html)の結果得られたものです。

## メンテナンス情報

- リリース日: 2026年8月
- バージョン: 1.0.0

## お問い合わせ

contact-medllm@weblab.t.u-tokyo.ac.jp へご連絡ください