---
language:
- en
- ja
library_name: transformers
pipeline_tag: text-generation
license:
- llama3.1
- gemma
model_type: llama
datasets:
- tokyotech-llm/lmsys-chat-1m-synth
- tokyotech-llm/swallow-magpie-ultra-v0.1
- tokyotech-llm/swallow-gemma-magpie-v0.1
- lmsys/lmsys-chat-1m
- argilla/magpie-ultra-v0.1

---

# Llama 3.1 Swallow - Built with Llama

Llama 3.1 Swallow is a series of large language models (8B, 70B) that were built by continual pre-training on the [Meta Llama 3.1](https://huggingface.co/collections/meta-llama/llama-31-669fc079a0c406a149a5738f) models.
Llama 3.1 Swallow enhanced the Japanese language capabilities of the original Llama 3.1 while retaining the English language capabilities.
We use approximately 200 billion tokens that were sampled from a large Japanese web corpus (Swallow Corpus Version 2), Japanese and English Wikipedia articles, and mathematical and
coding contents, etc (see the Training Datasets section of the base model) for continual pre-training.
The instruction-tuned models (Instruct) were built by supervised fine-tuning (SFT) on the synthetic data specially built for Japanese.
See the Swallow Model Index section to find other model variants.

**Note**: [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) model was continually pre-trained from the [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) and then instruction-tuned with our instruction datasets.

# Release History

- **December 23, 2024**: Released [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3).
- **November 11, 2024**: Released [Llama-3.1-Swallow-8B-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.2) and [Llama-3.1-Swallow-8B-Instruct-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2).
- **October 08, 2024**: Released [Llama-3.1-Swallow-8B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.1), [Llama-3.1-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1), [Llama-3.1-Swallow-70B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-v0.1), and [Llama-3.1-Swallow-70B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.1).

# Major Updates
This release enhances the conversation capability of Llama 3.1 Swallow.
The updated model, Llama-3.1-Swallow-8B-Instruct-v0.3 generates helpful and detailed responses based on user instructions and conversation history.
Among all open-source LLMs with <= 8 billion parameters, Llama-3.1-Swallow-8B-Instruct-v0.3 exhibits **state-of-the-art performance on Japanese MT-Bench**, outperforming its predecessor, [Llama-3.1-Swallow-8B-Instruct-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2), by 8.4 points.


## Swallow Model Index

|Model|Llama-3.1-Swallow v0.1|Llama-3.1-Swallow-Instruct v0.1|Llama-3.1-Swallow v0.2|Llama-3.1-Swallow-Instruct v0.2|Llama-3.1-Swallow-Instruct v0.3|
|---|---|---|---|---|---|
|8B| [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.1) | [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1) | [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.2) | [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2) |  [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3)
|70B| [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-v0.1) | [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.1) |  |  | [Link](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.3) |

![logo](./logo.png)

The website [https://swallow-llm.github.io/](https://swallow-llm.github.io/) provides large language models developed by the Swallow team.

## Model Details

* **Model type**: Please refer to [Llama 3.1 MODEL_CARD](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md) for details on the model architecture.
* **Language(s)**: Japanese English
* **Library**: [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) 
* **Tokenizer**: Please refer to [Llama 3.1 blog](https://ai.meta.com/blog/meta-llama-3-1) for details on the tokenizer.
* **Contact**: swallow[at]nlp.c.titech.ac.jp 

## Model Performance

## MT-Bench JA

|Model|coding|extraction|humanities|math|reasoning|roleplay|stem|writing|JMTAvg|
|---|---|---|---|---|---|---|---|---|---|
| RakutenAI-7B-chat | 0.2475 | 0.3522 | 0.4692 | 0.2140 | 0.3926 | 0.4427 | 0.3977 | 0.4434 | 0.3699 |
| Qwen2-7B-Instruct | 0.4635 | 0.6909 | 0.6857 | **0.5970** | 0.5042 | 0.6667 | 0.5353 | 0.6808 | 0.6030 |
| Qwen2.5-7B-Instruct | **0.5111** | 0.7489 | 0.6913 | 0.5742 | 0.4851 | 0.6810 | 0.5350 | 0.6810 | 0.6134 |
| Tanuki-8B-dpo-v1.0 | 0.3019 | 0.4772 | 0.5658 | 0.4129 | 0.3590 | 0.5120 | 0.4770 | 0.6159 | 0.4652 |
| Llama 3 8B Instruct | 0.3744 | 0.6876 | 0.6225 | 0.2070 | 0.5032 | 0.5248 | 0.5326 | 0.4884 | 0.4926 |
| Llama 3.1 8B Instruct | 0.3234 | 0.7362 | 0.4973 | 0.4787 | 0.3210 | 0.4670 | 0.4656 | 0.4314 | 0.4651 |
| Llama 3 Youko 8B Instruct | 0.2950 | 0.7332 | 0.7125 | 0.2533 | 0.4987 | 0.6514 | 0.5438 | 0.7091 | 0.5496 |
| Llama-3-ELYZA-JP-8B | 0.2908 | 0.6421 | 0.6406 | 0.3088 | **0.5500** | 0.6740 | 0.5251 | 0.6744 | 0.5382 |
| Llama 3 heron brain 8B v0.3 | 0.2929 | 0.5635 | 0.6241 | 0.2135 | 0.4582 | 0.5354 | 0.5273 | 0.5099 | 0.4656 |
| Llama 3 Swallow 8B Instruct | 0.3547 | 0.6508 | 0.5371 | 0.2718 | 0.4007 | 0.5493 | 0.4752 | 0.5730 | 0.4766 |
| Llama 3.1 Swallow 8B Instruct v0.1| 0.3132 | **0.7734** | 0.6645 | 0.3880 | 0.5230 | 0.5711 | 0.4953 | 0.5330 | 0.5327 |
| Llama 3.1 Swallow 8B Instruct v0.2| 0.4307 | 0.7089 | 0.6937 | 0.3881 | 0.5140 | 0.6277 | 0.5253 | 0.5787 | 0.5584 |
| Llama 3.1 Swallow 8B Instruct v0.3 | 0.4849 | 0.6845 | **0.8180** | 0.4817 | 0.5240 | **0.7370** | **0.6473** | **0.7615** | **0.6424** |

### Japanese tasks

|Model|JCom.|JEMHopQA|NIILC|JSQuAD|XL-Sum|MGSM|WMT20-en-ja|WMT20-ja-en|JMMLU|JHumanEval|Ja Avg|
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |4-shot|4-shot|4-shot|4-shot|1-shot|4-shot|4-shot|4-shot|5-shot|0-shot|   |
|   |EM acc|Char-F1|Char-F1|Char-F1|ROUGE-2|EM acc|BLEU|BLEU|EM acc|pass@1|   |
| RakutenAI-7B-chat | 0.9035 | 0.2600 | 0.4619 | 0.8647 | 0.1339 | 0.2120 | 0.2667 | 0.1966 | 0.4504 | 0.2299 | 0.3980 |
| Qwen2-7B-Instruct | 0.8856 | 0.3902 | 0.3859 | 0.8967 | 0.1277 | 0.5720 | 0.2041 | 0.1909 | 0.5713 | **0.5683** | 0.4793 |
| Qwen2.5-7B-Instruct | 0.9151 | 0.4293 | 0.3910 | 0.8908 | 0.1676 | **0.6240** | 0.2108 | 0.1916 | **0.6252** | 0.5305 | 0.4976 |
| Tanuki-8B-dpo-v1.0 | 0.2770 | 0.2937 | 0.3710 | 0.6669 | 0.1016 | 0.4280 | 0.2385 | 0.1820 | 0.3078 | 0.2555 | 0.3122 |
| Llama 3 8B Instruct | 0.8785 | 0.3812 | 0.3936 | 0.8955 | 0.1273 | 0.4160 | 0.2143 | 0.2035 | 0.4719 | 0.2872 | 0.4269 |
| Llama 3.1 8B Instruct | 0.8829 | 0.4272 | 0.4112 | 0.8856 | 0.1481 | 0.5280 | 0.2174 | 0.1990 | 0.5086 | 0.4976 | 0.4706 |
| Llama 3 Youko 8B Instruct | 0.9196 | 0.4850 | 0.5178 | 0.9001 | 0.2085 | 0.4680 | 0.2559 | 0.1906 | 0.4691 | 0.2695 | 0.4684 |
| Llama-3-ELYZA-JP-8B | 0.9017 | 0.5124 | 0.5016 | 0.9113 | 0.1677 | 0.4600 | 0.2509 | 0.1846 | 0.4829 | 0.3811 | 0.4754 |
| Llama 3 heron brain 8B v0.3 | 0.9231 | 0.4933 | 0.5694 | 0.9056 | **0.2178** | 0.4560 | 0.2771 | 0.2168 | 0.4993 | 0.3177 | 0.4876 |
| Llama 3 Swallow 8B Instruct | 0.9178 | 0.4963 | 0.5168 | 0.9088 | 0.1296 | 0.4880 | 0.2522 | 0.2254 | 0.4835 | 0.3927 | 0.4811 |
| Llama 3.1 Swallow 8B Instruct v0.1| 0.9240 | **0.5874** | 0.5736 | **0.9170** | 0.1380 | 0.5080 | 0.2820 | **0.2282** | 0.5301 | 0.3665 | 0.5055 |
| Llama 3.1 Swallow 8B Instruct v0.2| **0.9294** | 0.5601 | **0.5988** | 0.9148 | 0.1372 | 0.5280 | **0.2878** | 0.2270 | 0.5504 | 0.4079 | **0.5141** |
| Llama 3.1 Swallow 8B Instruct v0.3 |0.9240 | 0.5174 | 0.5825 | 0.8954 | 0.1902 | 0.5480 | 0.2809 | 0.2278 | 0.5445 | 0.3945| 0.5105 | 


### English tasks

|Model|OpenBookQA|TriviaQA|HellaSWAG|SQuAD2.0|XWINO|MMLU|GSM8K|BBH|HumanEval|En Avg|
|---|---|---|---|---|---|---|---|---|---|---|
|   |4-shot|4-shot|4-shot|4-shot|4-shot|5-shot|4-shot|3-shot|0-shot|   |
|   |Acc|EM acc|Acc|EM acc|Acc|Acc|EM acc|CoT EM Acc|pass@1|   |
| RakutenAI-7B-chat | 0.4160 | 0.5971 | **0.6465** | 0.3091 | 0.8886 | 0.5757 | 0.3139 | 0.4958 | 0.2671 | 0.5011 |
| Qwen2-7B-Instruct | 0.4000 | 0.5468 | 0.6146 | 0.3518 | 0.8852 | 0.7073 | 0.6300 | 0.3101 | 0.6354 | 0.5646 |
| Qwen2.5-7B-Instruct | **0.4280** | 0.5187 | 0.6240 | 0.2626 | 0.8761 | **0.7419** | 0.7415 | 0.2150 | **0.6360** | 0.5604 |
| Tanuki-8B-dpo-v1.0 | 0.3340 | 0.2838 | 0.4696 | 0.2395 | 0.8168 | 0.3772 | 0.4867 | 0.3350 | 0.2805 | 0.4026 |
| Llama 3 8B Instruct | 0.3880 | 0.6687 | 0.5834 | 0.3743 | 0.8903 | 0.6567 | **0.7453** | 0.6478 | 0.5415 | 0.6107 |
| Llama 3.1 8B Instruct | 0.3700 | **0.6994** | 0.5920 | **0.3783** | **0.9037** | 0.6809 | 0.7430 | **0.6928** | 0.6293 | **0.6321** |
| Llama 3 Youko 8B Instruct | 0.4080 | 0.6129 | 0.5983 | 0.3370 | 0.8981 | 0.5964 | 0.5618 | 0.4012 | 0.2750 | 0.5209 |
| Llama-3-ELYZA-JP-8B | 0.3200 | 0.5502 | 0.5224 | 0.3631 | 0.8809 | 0.5875 | 0.5701 | 0.3213 | 0.4604 | 0.5084 |
| Llama 3 heron brain 8B v0.3 | 0.3580 | 0.6563 | 0.5686 | 0.3726 | 0.9002 | 0.6213 | 0.5777 | 0.6409 | 0.3720 | 0.5631 |
| Llama 3 Swallow 8B Instruct | 0.3720 | 0.6557 | 0.5861 | 0.3648 | 0.9002 | 0.6315 | 0.5959 | 0.6391 | 0.4238 | 0.5743 |
| Llama 3.1 Swallow 8B Instruct v0.1| 0.3900 | 0.6488 | 0.6151 | 0.3553 | 0.8912 | 0.6237 | 0.6050 | 0.6417 | 0.3787 | 0.5722 |
| Llama 3.1 Swallow 8B Instruct v0.2| 0.3800 | 0.6252 | 0.6031 | 0.3667 | 0.8886 | 0.6346 | 0.6202 | 0.6487 | 0.4738 | 0.5823 |
| Llama 3.1 Swallow 8B Instruct v0.3 |0.3920 | 0.6295 | 0.5937 | 0.3638 | 0.8830 | 0.6280 | 0.6149 | 0.6282 | 0.4457 | 0.5754 |


## Evaluation Benchmarks

### MT-Bench JA

We used [Japanese MT-Bench](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_question) to assess the capabilities of multi-turn dialogue with the following settings:

- Implementation: FastChat [Zheng+, 2023] (commit #e86e70d0)
- Question: [Nejumi LLM-Leaderboard NEO, mtbench_ja_question_v3](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_question/v3)
- Reference Answer: [Nejumi LLM-Leaderboard NEO, mtbench_ja_referenceanswer_v1](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_referenceanswer/v1)
- Prompt for Judge: [Nejumi LLM-Leaderboard NEO, mtbench_ja_prompt_v1](https://wandb.ai/wandb-japan/llm-leaderboard/artifacts/dataset/mtbench_ja_prompt/v1)
- Judge: `gpt-4-1106-preview`
- Scoring: Absolute scale normalized to a 0-1 range, averaged over five runs.
- 
### Japanese evaluation benchmarks

We used llm-jp-eval(v1.3.0), JP Language Model Evaluation Harness(commit #9b42d41) and Code Generation LM Evaluation Harness(commit #0261c52). The details are as follows:

- Multiple-choice question answering (JCommonsenseQA [Kurihara et al., 2022])
- Open-ended question answering (JEMHopQA [Ishii et al., 2024])
- Open-ended question answering (NIILC [関根, 2003])
- Machine reading comprehension (JSQuAD [Kurihara et al., 2022])
- Automatic summarization (XL-Sum [Hasan et al., 2021])
- Machine translation (WMT2020 ja-en [Barrault et al., 2020])
- Machine translation (WMT2020 en-ja [Barrault et al., 2020])
- Mathematical reasoning (MGSM [Shi et al., 2023])
- Academic exams (JMMLU [尹ら, 2024])
- Code generation (JHumanEval [佐藤ら, 2024])

### English evaluation benchmarks

We used the Language Model Evaluation Harness(v.0.4.2) and Code Generation LM Evaluation Harness(commit #0261c52). The details are as follows:

- Multiple-choice question answering (OpenBookQA [Mihaylov et al., 2018])
- Open-ended question answering (TriviaQA [Joshi et al., 2017])
- Machine reading comprehension (SQuAD2 [Rajpurkar et al., 2018])
- Commonsense reasoning (XWINO [Tikhonov and Ryabinin, 2021])
- Natural language inference (HellaSwag [Zellers et al., 2019])
- Mathematical reasoning (GSM8K [Cobbe et al., 2021])
- Reasoning (BBH (BIG-Bench-Hard) [Suzgun et al., 2023])
- Academic exams (MMLU [Hendrycks et al., 2021])
- Code generation (HumanEval [Chen et al., 2021])

## Usage

```sh
pip install vllm
```

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

model_name = "tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3"

tokenizer = AutoTokenizer.from_pretrained(model_name)
llm = LLM(
    model=model_name,
    tensor_parallel_size=1,
)

sampling_params = SamplingParams(
    temperature=0.6, top_p=0.9, max_tokens=512, stop="<|eot_id|>"
)


message = [
    {"role": "system", "content": "あなたは誠実で優秀な日本人のアシスタントです。"},
    {
        "role": "user",
        "content": "東京の紅葉した公園で、東京タワーと高層ビルを背景に、空を舞うツバメと草地に佇むラマが出会う温かな物語を書いてください。",
    },
]
prompt = tokenizer.apply_chat_template(
    message, tokenize=False, add_generation_prompt=True
)

output = llm.generate(prompt, sampling_params)

print(output[0].outputs[0].text)

```

## Training Datasets

### Instruction Tuning

The following datasets were used for the instruction tuning.

- [Gemma-2-LMSYS-Chat-1M-Synth](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth)
  - Multi-turn Japanese instruction dataset synthesized and derived from [lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) [\[Zhang+, ICLR24\]](https://openreview.net/forum?id=BOfDKxfwt0)).
  - First-turn user instructions were translated into Japanese via DeepL (machine translation), and assistant responses were generated using [gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it). The same model, i.e., [gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it) served as a judge for rejection sampling (n=6).
  - Second-turn user instructions and responses were synthesized using [gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it). The same model scores the quality of the second-turn response with a range of 1-10. Second-turn responses with scores lower than 9 were rejected, along with their corresponding instructions.   
 Conversations containing personally identifiable information (PII) and template-based user instructions were removed. Duplicate instructions were removed.
- [Swallow-Magpie-Ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1)
  - A Japanese variant of the `filtered-magpie-ultra-en` dataset, translated into Japanese by [gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it).
- [Swallow-Gemma-Magpie-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-gemma-magpie-v0.1)
  - A Japanese synthetic instruction tuning dataset from scratch, generated by [gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it). User instructions were created with prompts specific to each topic, and assistant responses were generated for these instructions.
  - The conversations were heuristically filtered for quality and length. Then, [gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it) was applied to score the quality of each of the conversation with a range of 1-10. Conversations with scores <= 7 were rejected.

## Risks and Limitations

The models released here are still in the early stages of our research and development and have not been tuned to ensure outputs align with human intent and safety considerations.

## Acknowledgements

We thank Meta Research for releasing Llama 3.1 under a generous open license.

We received various supports, including:

+ AIST project: "Research and Development of Foundation Models for Generative AI in the Physical Domain"
+ NEDO project: "Development of Artificial Intelligence Application Technology to Support Judgment in Design Risk Assessment Work Based on the Perspective of Skilled Persons" (JPNP18002) of "Development of Integration Technology as the Core of Next Generation Artificial Intelligence and Robotics"
+ MEXT project: "Formation of R&D center to ensure transparency and reliability of generative AI models"
+ AIST program: [Large Generative AI Development Support Program](https://abci.ai/en/link/lfm_support_program.html)

## License

[META LLAMA 3.1 COMMUNITY LICENSE](https://www.llama.com/llama3_1/license/) and [Gemma Terms of Use](https://ai.google.dev/gemma/terms)

## Authors

Here are the team members:
- From [Tokyo Institute of Technology Okazaki Laboratory](https://www.nlp.c.titech.ac.jp/index.en.html), the following members:
  - [Naoaki Okazaki](https://www.chokkan.org/index.ja.html)
  - [Sakae Mizuki](https://s-mizuki-nlp.github.io/)
  - [Youmi Ma](https://www.nlp.c.titech.ac.jp/member/youmi.en.html)
  - [Koki Maeda](https://sites.google.com/view/silviase)
  - [Kakeru Hattori](https://aya-se.vercel.app/)
  - [Masanari Ohi](https://sites.google.com/view/masanariohi)
  - [Hinari Shimada](https://hinarishimada.github.io/portfolio)
  - [Taihei Shiotani](https://github.com/inatoihs)
  - [Koshiro Saito](https://sites.google.com/view/koshiro-saito)
- From [Tokyo Institute of Technology YOKOTA Laboratory](https://www.rio.gsic.titech.ac.jp/en/index.html), the following members:
  - [Rio Yokota](https://twitter.com/rioyokota)
  - [Kazuki Fujii](https://twitter.com/okoge_kaz)
  - [Taishi Nakamura](https://twitter.com/Setuna7777_2)
  - [Takumi Okamoto](https://www.linkedin.com/in/takumi-okamoto)
  - [Ishida Shigeki](https://www.wantedly.com/id/reborn27)
- From [Artificial Intelligence Research Center, AIST, Japan](https://www.airc.aist.go.jp/en/teams/), the following members:
  - [Hiroya Takamura](https://sites.google.com/view/hjtakamura)

## How to cite

If you find our work helpful, please feel free to cite these papers.

```
@inproceedings{Fujii:COLM2024,
   title={Continual Pre-Training for Cross-Lingual LLM Adaptation:
Enhancing Japanese Language Capabilities},
   author={Kazuki Fujii and Taishi Nakamura and Mengsay Loem and Hiroki
Iida and Masanari Ohi and Kakeru Hattori and Hirai Shota and Sakae
Mizuki and Rio Yokota and Naoaki Okazaki},
   booktitle="Proceedings of the First Conference on Language Modeling",
   series={COLM},
   pages="(to appear)",
   year="2024",
   month=oct,
   address={University of Pennsylvania, USA},
}

@inproceedings{Okazaki:COLM2024,
   title={Building a Large Japanese Web Corpus for Large Language Models},
   author={Naoaki Okazaki and Kakeru Hattori and Hirai Shota and Hiroki
Iida and Masanari Ohi and Kazuki Fujii and Taishi Nakamura and Mengsay
Loem and Rio Yokota and Sakae Mizuki},
   booktitle="Proceedings of the First Conference on Language Modeling",
   series={COLM},
   pages="(to appear)",
   year="2024",
   month=oct,
   address={University of Pennsylvania, USA},
}

@misc{ma:arxiv2025,
      title={Building Instruction-Tuning Datasets from Human-Written Instructions with Open-Weight Large Language Models}, 
      author={Youmi Ma and Sakae Mizuki and Kazuki Fujii and Taishi Nakamura and Masanari Ohi and Hinari Shimada and Taihei Shiotani and Koshiro Saito and Koki Maeda and Kakeru Hattori and Takumi Okamoto and Shigeki Ishida and Rio Yokota and Hiroya Takamura and Naoaki Okazaki},
      year={2025},
      eprint={2503.23714},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.23714}, 
}
```

### References

```tex
@misc{dubey2024llama3herdmodels,
      title={The Llama 3 Herd of Models}, 
      author={Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aiesha Letman and Akhil Mathur and Alan Schelten and Amy Yang and Angela Fan et al.},
      year={2024},
      eprint={2407.21783},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2407.21783}, 
}
```