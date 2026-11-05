---
language:
- fi
license: apache-2.0
tags:
- finnish
- llama
inference: false
pipeline_tag: text-generation
base_model: Finnish-NLP/Ahma-3B

---

# Ahma-3B-Instruct for Finnish

Ahma-3B-Instruct is a instruct/chat-tuned version of [Ahma-3B](https://huggingface.co/Finnish-NLP/Ahma-3B) trained to follow instructions in Finnish. The base Ahma 3B parameter model is decoder-only transformer model based on Meta's Llama (v1) architecture pretrained from scratch on Finnish language. Original Llama model architecture was introduced in
[this paper](https://arxiv.org/abs/2302.13971)
and first released at [this page](https://github.com/facebookresearch/llama).

What does Ahma mean? Ahma is the Finnish word for wolverine! In the Finnish Lapland, wolverines are the biggest cause of reindeer damage. 

There are two different sized base Ahma models, all pretrained from scratch for 139B tokens:

| Model                                                                           | Context length | Layers | Dim  | Heads | Params |
|:--------------------------------------------------------------------------------|:---------------|:-------|:-----|:------|:-------|
| [Ahma-3B](https://huggingface.co/Finnish-NLP/Ahma-3B)                           | 2048           | 26     | 3200 | 32    | 3.6B   |
| [Ahma-7B](https://huggingface.co/Finnish-NLP/Ahma-7B)                           | 2048           | 32     | 4096 | 32    | 7.0B   |

And two instruct-tuned versions:

| Model                                                                           | Context length | Layers | Dim  | Heads | Params |
|:--------------------------------------------------------------------------------|:---------------|:-------|:-----|:------|:-------|
| [Ahma-3B-Instruct](https://huggingface.co/Finnish-NLP/Ahma-3B-Instruct)         | 2048           | 26     | 3200 | 32    | 3.6B   |
| [Ahma-7B-Instruct](https://huggingface.co/Finnish-NLP/Ahma-7B-Instruct)         | 2048           | 32     | 4096 | 32    | 7.0B   |

## Intended uses & limitations

This model was fine-tuned for instruction following. Instruction-tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

### How to use

If you want to use this model for instruction-following, you need to use the same prompt format we used in the fine-tuning process (basically the same format what Meta used in their Llama2 models).\
**Note: do not use "LlamaTokenizer" from transformers library but always use the AutoTokenizer instead, or use the plain sentencepiece tokenizer.** 

Looking for <b>GGUF-versions?</b> 
Those can be found from here for now: [GGUF-versions](https://huggingface.co/mradermacher/Ahma-3B-Instruct-GGUF)

Here is an example using the instruction-following prompt format with the tokenizer's built-in chat template feature which makes it easy to format your potential multi-turn chats too, with some generation arguments you can modify for your use:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

system_prompt = "Olet tekoälyavustaja. Vastaat aina mahdollisimman avuliaasti. Vastauksesi eivät saa sisältää mitään haitallista, epäeettistä, rasistista, seksististä, vaarallista tai laitonta sisältöä. Jos kysymyksessä ei ole mitään järkeä tai se ei ole asiasisällöltään johdonmukainen, selitä miksi sen sijaan, että vastaisit jotain väärin. Jos et tiedä vastausta kysymykseen, älä kerro väärää tietoa."


tokenizer = AutoTokenizer.from_pretrained("Finnish-NLP/Ahma-3B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Finnish-NLP/Ahma-3B-Instruct")
model = model.to("cuda")

# use the chat template feature in the tokenizer to format your (multi-turn) inputs

messages = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {"role": "user", "content": "Kerro kolme hyötyä, joita pienet avoimen lähdekoodin kielimallit tuovat?"},
]
inputs = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
)
inputs = inputs.to("cuda")

generated_ids = model.generate(
    inputs,
    temperature=0.6,
    penalty_alpha=0.6,
    top_k=4,
    do_sample=True,
    repetition_penalty=1.2,
    min_length=5,
    max_length=2048,
)
generated_text = tokenizer.batch_decode(
    generated_ids, skip_special_tokens=False
)[0]

'''
1) Parantuneet keskustelutaidot: Pienet, hyvin koulutetut kielimallit voidaan kouluttaa ymmärtämään ja tuottamaan ihmisen kaltaista kieltä, mikä johtaa luonnollisempaan keskusteluun. Tämä voi olla erityisen hyödyllistä sovelluksissa, kuten chat-roboteissa, virtuaaliavustajissa ja kielenkääntämisessä.

2) Lisääntynyt luovuus kirjoittamisessa: Kielimallit voivat auttaa kirjoittajia tuottamalla ideoita, lauseita ja virkkeitä, jotka ovat hiottuja ja merkityksellisiä. Tämä voi johtaa parempaan kirjoituslaatuun, parempaan organisointiin ja tehokkaampaan viestintään.

3) Parempi tietojenkäsittely ja -tallennus: Pienemmät ja edullisemmat kielimallit voivat mullistaa tietojenkäsittelyn ja tallennuksen. Ne voivat säästää tilaa ja resursseja, koska ne pystyvät suorittamaan tiettyjä tehtäviä tehokkaammin kuin perinteiset koneoppimisalgoritmit. Lisäksi kielimallien avoimen lähdekoodin luonne mahdollistaa sen, että tutkijat, kehittäjät ja yritykset voivat tehdä niihin parannuksia ja lisäyksiä, mikä voi johtaa entistä kehittyneempiin ja monipuolisempiin ratkaisuihin.
'''
```

You may experiment with different system prompt instructions too if you like.

### Limitations and bias

This model was trained only with Finnish texts excluding code so it should not be used for multilingual and code generation use cases.

The training data used for this model contains a lot of content from the internet, which is far from neutral. Therefore, the model can have biased predictions. This bias will also affect all fine-tuned versions of this model.

## Training data

To better reflect the data distribution of the training set and balance the common samples and rare samples during training, we implemented the "ClusterClip Sampling" method by [Shao et al. (2024)](https://arxiv.org/abs/2402.14526) using [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) embeddings and KMeans clustering of 30 clusters. The training datasets mentioned below were created using this sampling method.

There has also been some indication that gradually increasing the training example lengths during the training could be beneficial. Thus, the training dataset was splitted to 4 bins based on example lengths, and then examples were sampled from the bins so that the example lengths are gradually increasing towards the end of the training while a little amount of the shorter examples are still present too.

This model was first supervised fine-tuned (SFT) on the combination of the following datasets:

| Dataset                                          | Dataset type           | Upsampling | Words      | Ratio    | Average words per example |
|:-------------------------------------------------|:-----------------------|:-----------|:-----------|:---------|:--------------------------|
| Aya Finnish                                      | Finnish single-turn    | 2.9X       | 55K        | 0.54%    | 83                        |
| OASST                                            | Translated single-turn | 2.9X       | 507K       | 5.01%    | 139                       |
| ai2_arc                                          | Translated single-turn | 2.9X       | 12K        | 0.12%    | 39                        |
| chatbot_arena                                    | Translated single-turn | 2.8X       | 554K       | 5.48%    | 147                       |
| dibt10k                                          | Translated single-turn | 2.9X       | 363K       | 3.58%    | 262                       |
| dolly                                            | Translated single-turn | 2.9X       | 221K       | 2.19%    | 71                        |
| Aya Dutch                                        | Translated single-turn | 2.9X       | 13K        | 0.12%    | 36                        |
| Aya English                                      | Translated single-turn | 2.9X       | 97K        | 0.96%    | 61                        |
| Aya French                                       | Translated single-turn | 3.7X       | 75K        | 0.74%    | 58                        |
| intel_dpo                                        | Translated single-turn | 2.9X       | 539K       | 5.33%    | 163                       |
| lmsys_1m                                         | Translated single-turn | 2.8X       | 2187K      | 21.61%   | 246                       |
| news_qa                                          | Translated single-turn | 2.9X       | 297K       | 2.94%    | 152                       |
| orca_math                                        | Translated single-turn | 2.9X       | 1165K      | 11.51%   | 196                       |
| Aya Portuguese                                   | Translated single-turn | 2.9X       | 97K        | 0.96%    | 27                        |
| Aya Spanish                                      | Translated single-turn | 2.8X       | 52K        | 0.51%    | 54                        |
| Aya Swedish                                      | Translated single-turn | 2.9X       | 5K         | 0.05%    | 41                        |
| ultrachat                                        | Translated single-turn | 2.8X       | 2199K      | 21.73%   | 221                       |
| lmsys_multiturn                                  | Translated multi-turn  | 2.9X       | 490K       | 4.84%    | 379                       |
| oaast2_multiturn                                 | Translated multi-turn  | 2.8X       | 593K       | 5.86%    | 307                       |
| suomitrivia_synthetic                            | Synthetic single-turn  | 1.0X       | 4K         | 0.04%    | 16                        |
| wikipedia_multitask_synthetic_qa                 | Synthetic single-turn  | 1.0X       | 206K       | 2.03%    | 499                       |
| wikipedia_synthetic_qa_reasoning                 | Synthetic single-turn  | 1.0X       | 201K       | 1.98%    | 477                       |
| wikipedia_synthetic_person_discussions_multiturn | Synthetic multi-turn   | 1.0X       | 188K       | 1.85%    | 194                       |
| **TOTAL**                                        |                        |            | **10121K** | **100%** | **168**                   |

After tokenization, the SFT training dataset had 23 million tokens and 5% of the dataset was splitted for evaluation during the training.


The SFT model was then further fine-tuned with Direct Preference Optimization (DPO) on the combination of the following datasets:

| Dataset         | Dataset type           | Upsampling | Words     | Ratio    | Average words per example |
|:----------------|:-----------------------|:-----------|:----------|:---------|:--------------------------|
| intel_dpo       | Translated single-turn | 1.3X       | 467K      | 39.75%   | 153                       |
| ultrachat       | Translated single-turn | 1.2X       | 1017K     | 57.24%   | 220                       |
| suomitrivia_dpo | Synthetic single-turn  | 1.0X       | 5K        | 3.01%    | 16                        |
| **TOTAL**       |                        |            | **1489K** | **100%** | **130**                   |

After tokenization, the DPO training dataset had 3 million tokens and 5% of the dataset was splitted for evaluation during the training.

## Training procedure

### Preprocessing

Texts are tokenized using Byte Pair Encoding (BPE) using the implementation from SentencePiece splitting all numbers into individual digits and using bytes to decompose unknown UTF-8 characters. The total
vocabulary size is 64k tokens. Inputs are sequences of 2048 consecutive tokens. Texts are not lower cased so this model is case-sensitive: it makes a difference between finnish and Finnish. Both BOS and EOS tokens were used in the fine-tuning.

### Supervised fine-tuning (SFT)

This model was first supervised fine-tuned (SFT) using the [unsloth](https://github.com/unslothai/unsloth) framework with a single NVIDIA GeForce RTX 4080 GPU. The model was fine-tuned for 1 epoch with a learning rate of 5e-05, weight decay of 5e-03, learning rate warmup ratio of 0.1 with cosine decay, batch size of 4 and gradient accumulation of 8 totalling the batch size to 32, max sequence lenght of 2048, and with NEFTune noise alpha of 5. The used optimizer was "paged_adamw_8bit" and the model was loaded with 4bit quantization. Training was done using the Rank-Stabilized LoRA (RSLora) with a rank of 256 and alpha of 128, LoRA dropout of 0.02, target modules of "q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj" and modules_to_save "lm_head", "embed_tokens".

### Direct Preference Optimization (DPO) fine-tuning

The SFT model was then further fine-tuned with Direct Preference Optimization (DPO) using the [unsloth](https://github.com/unslothai/unsloth) framework with a single NVIDIA GeForce RTX 4080 GPU. The model was fine-tuned for 1 epoch with a learning rate of 2e-05, weight decay of 0.0, learning rate warmup ratio of 0.1 with cosine decay, batch size of 2 and gradient accumulation of 8 totalling the batch size to 16, and with max sequence lenght of 2048. The used optimizer was "paged_adamw_8bit". Training was done using the Rank-Stabilized LoRA (RSLora) with a rank of 64 and alpha of 32, LoRA dropout of 0.05, and target modules of "q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj".

## Evaluation results

### FIN-bench

This Ahma-3B-Instruct model was evaluated using [FIN-bench by TurkuNLP](https://github.com/TurkuNLP/FIN-bench), and the same evaluation was carried out for other relevant Finnish models for comparison: [FinGPT 8B by TurkuNLP](https://huggingface.co/TurkuNLP/gpt3-finnish-8B), [Viking 7B by TurkuNLP, SiloGen and HPLT](https://huggingface.co/LumiOpen/Viking-7B), and [Poro 34B by SiloGen, TurkuNLP and HPLT](https://huggingface.co/LumiOpen/Poro-34B). Below are the results with 0-shot and 3-shot settings in FIN-bench.

0-shot results:

| Benchmark                  | Ahma 3B base (instruct prompt format) | Ahma 3B Instruct (instruct prompt format) | Ahma 7B base (instruct prompt format) | Ahma 7B Instruct (instruct prompt format) | FinGPT 8B | Viking 7B | Poro 34B (8bit quant) |
|:---------------------------|:--------------------------------------|:------------------------------------------|:--------------------------------------|:------------------------------------------|:----------|:----------|:----------------------|
| Analogies                  | 50.77                                 | 48.46                                     | 56.92                                 | 41.54                                     | 49.23     | 40.00     | 54.62                 |
| Arithmetic                 | 27.64                                 | 22.14                                     | 11.50                                 | 14.70                                     | 33.15     | 30.16     | 30.34                 |
| Cause and Effect           | 59.48                                 | 58.82                                     | 59.48                                 | 53.60                                     | 66.01     | 58.82     | 62.74                 |
| Emotions                   | 36.25                                 | 28.12                                     | 36.25                                 | 27.50                                     | 22.50     | 26.25     | 35.63                 |
| Empirical Judgements       | 33.33                                 | 35.35                                     | 33.33                                 | 33.33                                     | 27.27     | 33.33     | 49.49                 |
| General Knowledge          | 44.29                                 | 48.57                                     | 51.43                                 | 37.14                                     | 40.00     | 24.29     | 51.43                 |
| HHH Alignment              | 42.09                                 | 41.66                                     | 44.23                                 | 43.22                                     | 41.81     | 42.51     | 42.92                 |
| Intent Recognition         | 24.42                                 | 26.16                                     | 43.64                                 | 56.94                                     | 17.49     | 22.40     | 68.35                 |
| Misconceptions             | 46.27                                 | 47.01                                     | 46.27                                 | 47.01                                     | 53.73     | 53.73     | 52.24                 |
| Paraphrase                 | 59.50                                 | 73.00                                     | 67.00                                 | 70.50                                     | 51.00     | 50.00     | 51.00                 |
| Sentence Ambiguity         | 53.33                                 | 65.00                                     | 60.00                                 | 63.33                                     | 51.67     | 48.33     | 50.00                 |
| Similarities Abstraction   | 65.79                                 | 68.42                                     | 71.05                                 | 61.84                                     | 60.53     | 65.79     | 60.53                 |
| **Non-Arithmetic Average** | **47.55**                             | **48.95**                                 | **51.33**                             | **48.30**                                 | **46.17** | **44.42** | **52.08**             |
| **Overall Average**        | **36.49**                             | **34.06**                                 | **29.20**                             | **29.64**                                 | **38.93** | **36.50** | **40.00**             |


3-shot results:

| Benchmark                  | Ahma 3B base (instruct prompt format) | Ahma 3B Instruct (instruct prompt format) | Ahma 7B base (instruct prompt format) | Ahma 7B Instruct (instruct prompt format) | FinGPT 8B | Viking 7B | Poro 34B (8bit quant) |
|:---------------------------|:--------------------------------------|:------------------------------------------|:--------------------------------------|:------------------------------------------|:----------|:----------|:----------------------|
| Analogies                  | 50.77                                 | 49.23                                     | 49.23                                 | 43.08                                     | 40.77     | 54.62     | 76.92                 |
| Arithmetic                 | 38.38                                 | 43.89                                     | 20.88                                 | 26.81                                     | 43.63     | 45.78     | 53.68                 |
| Cause and Effect           | 60.78                                 | 64.71                                     | 66.01                                 | 62.74                                     | 64.05     | 58.17     | 67.32                 |
| Emotions                   | 30.00                                 | 41.25                                     | 30.00                                 | 53.75                                     | 44.37     | 48.13     | 56.87                 |
| Empirical Judgements       | 46.46                                 | 44.44                                     | 39.39                                 | 39.39                                     | 32.32     | 43.43     | 63.64                 |
| General Knowledge          | 47.14                                 | 40.00                                     | 27.14                                 | 44.29                                     | 54.29     | 28.57     | 74.29                 |
| HHH Alignment              | 43.53                                 | 44.80                                     | 43.80                                 | 45.09                                     | 45.39     | 44.80     | 46.07                 |
| Intent Recognition         | 20.52                                 | 44.22                                     | 36.42                                 | 39.02                                     | 51.45     | 58.82     | 83.67                 |
| Misconceptions             | 50.75                                 | 52.24                                     | 46.27                                 | 51.49                                     | 52.99     | 46.27     | 52.99                 |
| Paraphrase                 | 50.50                                 | 58.50                                     | 57.50                                 | 65.00                                     | 53.00     | 54.50     | 55.00                 |
| Sentence Ambiguity         | 53.33                                 | 48.33                                     | 53.33                                 | 51.67                                     | 51.67     | 53.33     | 66.67                 |
| Similarities Abstraction   | 69.74                                 | 72.37                                     | 72.37                                 | 69.74                                     | 64.47     | 73.68     | 75.00                 |
| **Non-Arithmetic Average** | **48.48**                             | **51.49**                                 | **49.05**                             | **51.63**                                 | **51.19** | **50.94** | **61.96**             |
| **Overall Average**        | **42.87**                             | **47.27**                                 | **33.41**                             | **37.84**                                 | **46.99** | **48.07** | **57.36**             |

As we can see, Ahma-3B-Instruct model outperforms 2X larger models like the FinGPT 8B and Viking 7B, especially in non-arithmetic tasks in 0-shot usage. Even the 10X larger Poro 34B model, which is generally better, doesn't show a huge performance difference considering its size, and Ahma-3B-Instruct actually surpasses it in some tasks.

In a 3-shot setting, we can see that the Ahma-3B-Instruct model has better few-shot example following performance compared to the base Ahma 3B model. This could be due to the inclusion of multi-turn examples in the fine-tuning dataset.

### MTBench Finnish

This Ahma-3B-Instruct model was primarily evaluated using [MTBench Finnish by LumiOpen](https://github.com/LumiOpen/FastChat/tree/main/fastchat/llm_judge) since this model is fine-tuned for chat and instruction following. Since the MTBench evaluates also multi-turn chats while Ahma base models were only pretrained with single-turn instruction following examples, we have reported MTBench Finnish results separately for their single-turn and multi-turn evaluation examples. This enables us to evaluate how well this Ahma-3B-Instruct model improves on multi-turn chats since its fine-tuning dataset included some multi-turn examples too. [Poro 34B Chat by SiloGen, TurkuNLP and HPLT](https://huggingface.co/LumiOpen/Poro-34B-chat) model's presumably multi-turn results are copied from their model card for the comparison.

Single-turn results:

| Benchmark           | Ahma 3B base (instruct prompt format) | Ahma 3B Instruct (instruct prompt format) | Ahma 7B base (instruct prompt format) | Ahma 7B Instruct (instruct prompt format) |
|:--------------------|:--------------------------------------|:------------------------------------------|:--------------------------------------|:------------------------------------------|
| Coding              | 1.00                                  | 1.00                                      | 1.70                                  | 1.10                                      |
| Extraction          | 2.00                                  | 1.30                                      | 3.10                                  | 3.00                                      |
| Humanities          | 4.05                                  | 6.20                                      | 6.60                                  | 8.00                                      |
| Math                | 3.00                                  | 3.20                                      | 3.90                                  | 2.90                                      |
| Reasoning           | 2.90                                  | 4.60                                      | 3.70                                  | 5.70                                      |
| Roleplay            | 4.80                                  | 6.50                                      | 6.60                                  | 7.20                                      |
| STEM                | 5.10                                  | 5.95                                      | 6.75                                  | 7.30                                      |
| Writing             | 6.60                                  | 9.00                                      | 7.10                                  | 8.80                                      |
| **Overall Average** | **3.68**                              | **4.72**                                  | **4.93**                              | **5.50**                                  |

Multi-turn results:

| Benchmark           | Ahma 3B base (instruct prompt format) | Ahma 3B Instruct (instruct prompt format) | Ahma 7B base (instruct prompt format) | Ahma 7B Instruct (instruct prompt format) | Poro 34B Chat |
|:--------------------|:--------------------------------------|:------------------------------------------|:--------------------------------------|:------------------------------------------|:--------------|
| Coding              | 1.00                                  | 1.00                                      | 1.40                                  | 1.05                                      | 3.70          |
| Extraction          | 1.55                                  | 1.15                                      | 2.05                                  | 2.65                                      | 6.37          |
| Humanities          | 3.25                                  | 6.20                                      | 4.95                                  | 7.85                                      | 9.25          |
| Math                | 2.20                                  | 2.70                                      | 2.50                                  | 2.40                                      | 1.20          |
| Reasoning           | 2.45                                  | 3.50                                      | 2.55                                  | 4.50                                      | 4.35          |
| Roleplay            | 4.90                                  | 6.40                                      | 6.35                                  | 6.60                                      | 7.35          |
| STEM                | 4.20                                  | 4.78                                      | 4.28                                  | 5.40                                      | 7.80          |
| Writing             | 3.80                                  | 6.65                                      | 4.10                                  | 6.25                                      | 8.50          |
| **Overall Average** | **2.92**                              | **4.05**                                  | **3.52**                              | **4.59**                                  | **6.06**      |


As we can see, the Ahma-3B-Instruct model significantly improves upon the base Ahma-3B model, especially in tasks like writing. It's also worth noting that the Ahma-3B-Instruct model shows enhanced performance in multi-turn tasks compared to the base model, which highlights the value of the multi-turn training examples used in the fine-tuning process. The Ahma-3B-Instruct model lost 14% of its single-turn overall score in a multi-turn setting, while the base Ahma-3B model lost 21%. Therefore, this instruct model might be better suited for chat use cases as well. As expected, coding performance was poor since the Ahma models aren't trained on code data.

Ahma models also seemed to have problems with the fact that they started to constantly repeat the generated text in some evaluation examples, which affected the scoring. With the addition of a repetition penalty setting to the evaluation script generation method, the scores already improved significantly, so Ahma models should be used with better generation settings in real-world use compared to the settings used in this benchmark.

## Acknowledgements

This project would not have been possible without compute generously provided by Google through the
[TPU Research Cloud](https://sites.research.google/trc/).

## Team Members

- Aapo Tanskanen, [Hugging Face profile](https://huggingface.co/aapot), [LinkedIn profile](https://www.linkedin.com/in/aapotanskanen/)
- Rasmus Toivanen, [Hugging Face profile](https://huggingface.co/RASMUS), [LinkedIn profile](https://www.linkedin.com/in/rasmustoivanen/)

Feel free to contact us for more details 🤗


![Ahma](ahma.jpg)