---
license: apache-2.0
base_model:
- Qwen/Qwen2.5-7B-Instruct
---
GENIAC 03 NEDO賞コンペティションへのエントリー

本モデルは、Qwen/Qwen2.5-7B-Instructをベースに、特定のトピックに対する拒否（refusal）を軽減するために構築されたデータセットを用いてLoRA学習を行ったバリアントです。
詳細については、NEDOのページにある当社のエントリー、または本エントリーのリポジトリをご覧ください。
https://github.com/shisa-ai/NEDO-safety-refusals


拒否の軽減率は以下の通りです。


| モデル名              | 拒否件数 | 全試行回 | 拒否率 (%) |  
|-------------------------|---------------|----------------|------------------|  
| Qwen2.5-7b-Instruct     | 58            | 180            | 32.2%            |  
| Nedo Safety Model       | 5             | 180            | 2.8%      |  
| **差分**          | **-53**        | **—**          | **↓91.4%**|  


本モデルを通じて、小規模なSFT（Supervised Fine-Tuning）学習により、モデルの能力を低下させることなく、標的としたバイアスに起因する拒否を軽減することが可能であることを示しました。

これは、NEDO賞トライアル期間中に指定した目標、すなわちモデルの能力をオリジナルから5%以内に維持しつつ、バイアスに起因する拒否を90%削減するという目標を達成するものです。
実際、私たちはJA-MTスコアが約10%向上したことを確認しました。これは、SFTのソースデータに使用された高品質な日本語テキストに起因するものと考えています。

| モデル名 | JA-MT Bench スコア |
|-------|-------------------|
| Qwen/Qwen2.5-7b-Instruct | 4.93 |
| shisa-ai/NEDO-Safety-Qwen2.5-7b-Instruct | 5.48 |

JA-MT Benchの評価は、https://github.com/shisa-ai/shaberi のShaberiリポジトリを使用して行われました。
使用されたJudge（評価モデル）は gpt-5.1-2025-11-13 です。

LoRAの設定は以下の通りです。

| **Setting**              | **Value**                          |  
|--------------------------|------------------------------------|  
| Learning Rate            | 2e-5                               |  
| Batch Size               | 8                                  |  
| Gradient Accumulation Steps | 2                                |  
| Epochs                   | 3                                  |  
| Optimizer                | adamw_8bit                         |  
| LoRA Target Modules  | `"q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"` |  
| LoRA Alpha               | 32                                 |  
| LoRA r                   | 16                                 |  
| LoRA Dropout             | 0.0                                |  



トレーニングは以下のスクリプトを使うことで行いました。
train/refusals_unsloth_sft.py


--- ENGLISH BELOW---


Our entry into the GENIAC 03 NEDO Prize Competition.

This model is a LoRA-trained variant of Qwen/Qwen2.5-7B-Instruct with a dataset built to reduce refusals around certain specific topics. For details, please see our entry on the NEDO Prize page, or the training repo at https://github.com/shisa-ai/NEDO-safety-refusals.

Refusal reduction rates were as below:

| Model Name              | Refusal Count | Total Attempts | Refusal Rate (%) |  
|-------------------------|---------------|----------------|------------------|  
| Qwen2.5-7b-Instruct     | 58            | 180            | 32.2%            |  
| Nedo Safety Model       | 5             | 180            | 2.8%      |  
| **Difference**          | **-53**        | **—**          | **↓91.4%**|  


We show via this model that it is possible to reduce targeted bias-induced refusals via small-scale SFT training while avoiding model capability degradation. This meets our target specified during the NEDO Prize trial period of a 90% reduction in bias-induced refusals while maintaining model capabilities within 5% of the original. 

In fact, we saw an increase in JA-MT score by roughly 10%, a fact we attribute to the high-quality Japanese text used in the SFT source data. 

| Model | JA-MT Bench Score |
|-------|-------------------|
| Qwen/Qwen2.5-7b-Instruct | 4.93 |
| shisa-ai/NEDO-Safety-Qwen2.5-7b-Instruct | 5.48 |

Scoring done using the Shaberi repository at https://github.com/shisa-ai/shaberi
Judge used was: gpt-5.1-2025-11-13 

Thanks to the good people at Unsloth for their LoRA trainer, which was used in this project. While there are countless training frameworks available for LLMs, Unsloth remains a standout choice for single-GPU runs due to their top quality documentation, clean infrastructure, and commitment to keeping their codebase up-to-date. 

| **Setting**              | **Value**                          |  
|--------------------------|------------------------------------|  
| Learning Rate            | 2e-5                               |  
| Batch Size               | 8                                  |  
| Gradient Accumulation Steps | 2                                |  
| Epochs                   | 3                                  |  
| Optimizer                | adamw_8bit                         |  
| LoRA Target Modules  | `"q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"` |  
| LoRA Alpha               | 32                                 |  
| LoRA r                   | 16                                 |  
| LoRA Dropout             | 0.0                                |  

Full training code is available at the GitHub repository using the code at train/refusals_unsloth_sft.py


