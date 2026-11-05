---
license: llama3
datasets:
- ajibawa-2023/Code-290k-ShareGPT
- m-a-p/CodeFeedback-Filtered-Instruction
- m-a-p/Code-Feedback
- microsoft/orca-math-word-problems-200k
language:
- en
tags:
- code
- Python
- Cpp
- PHP
- JS
- Java
- Rust
- Ruby
- SQL
- MySql
- R
- Julia
---

**Code-Llama-3-8B**


This Model is trained on refined version of my dataset [Code-290k-ShareGPT](https://huggingface.co/datasets/ajibawa-2023/Code-290k-ShareGPT).

Besides this it is trained on following datasets:

[Code-Feedback](https://huggingface.co/datasets/m-a-p/Code-Feedback)

[orca-math-word-problems-200k](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k)

[CodeFeedback-Filtered-Instruction](https://huggingface.co/datasets/m-a-p/CodeFeedback-Filtered-Instruction)

The idea was to check how this Model will perform with both Code & Maths datasets. This model is very good with Coding. 
Maths outputs are also very good. You can test out this model.

It is very very good in Code generation in various languages such as **Python, Java, JavaScript, GO, C++, Rust, Ruby, Sql, MySql, R, Julia, Haskell**, etc.. 
This model will also generate detailed explanation/logic behind each code. 

This Model is trained on massive datasets so the results are very good. You can check the Examples given below.

I have used ChatML prompt format.

This is Fully Finetuned Model. 

**GGUF & Exllama**

GGUF: [Link](https://huggingface.co/bartowski/Code-Llama-3-8B-GGUF)

Exllama v2: [Link](https://huggingface.co/bartowski/Code-Llama-3-8B-exl2)

Special Thanks to [Bartowski](https://huggingface.co/bartowski) for quantizing this model.


**Training:**

Entire dataset was trained on 4 x A100 80GB. For 2 epoch, training took more than 160 Hours. Axolotl & Deepspeed codebase was used for training purpose.
Entire data is trained on Llama-3-8B by Meta.

**Example Prompt:**
This model uses **ChatML** prompt format.

```
<|im_start|>system
You are a helpful Coding assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```
You can modify above Prompt as per your requirement.
One example will be: 
```
This is a conversation with your helpful Coding assistant. Assistant can generate Code in various Programming Languages along with necessary explanation.
``` 
I want to say special Thanks to the Open Source community for helping & guiding me to better understand the AI/Model development.

Thank you for your love & support.


**Example Output**

Example 1


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64aea8ff67511bd3d965697b/KJpeOSl9CHaBSqAp09iG5.jpeg)

Example 2


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64aea8ff67511bd3d965697b/XYnq7bzKSGj4reMr7sYmU.jpeg)

Example 3


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64aea8ff67511bd3d965697b/bdJZvHtrG7cSBKXOEbHa2.jpeg)

Example 4


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64aea8ff67511bd3d965697b/xViwKIT3laev5F9xZbs3-.jpeg)

Example 5


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/64aea8ff67511bd3d965697b/O33l9tj93EVDPE34Q7ZHY.jpeg)