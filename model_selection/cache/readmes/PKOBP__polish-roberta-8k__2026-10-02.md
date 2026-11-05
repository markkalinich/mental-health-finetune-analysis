---
language: pl
license: apache-2.0
extra_gated_heading: "Request access to polish-roberta-8k"
extra_gated_description: "Access is granted automatically after submitting this form."
extra_gated_prompt: >-  
  By requesting access you agree to use the model in accordance with the Apache-2.0 license and applicable export control regulations.
extra_gated_fields:
  Full name: text
  Company / Institution: text
  Country: country
  Region / Business unit: text
  Intended use:
    type: select
    options:
      - Research
      - Commercial product
      - Internal evaluation
      - label: Other
        value: other
    I agree to the license terms: checkbox
extra_gated_button_content: "Request access"
---

<h1 align="center">polish-roberta-8k</h1>

A Polish language model built on the RoBERTa architecture, supporting context length of up to 8192 tokens. Encoder-type models can be fine-tuned to solve various text prediction tasks such as classification, regression, sequence tagging, or retrieval. In such tasks, they are usually faster and more parameter-efficient than LLMs. This model was initialized from the [polish-roberta-large-v2](https://huggingface.co/sdadas/polish-roberta-large-v2) checkpoint, originally supporting 512-token context, and then adapted to handle longer texts. The model training process was as follows:

- In the first stage, the positional embedding layer was extended from 512 to 8192 tokens. The model was then trained on a corpus of approximately 150 billion tokens for one epoch. All model weights were frozen, and only the positional embedding layer was trained. The goal of this stage was to adapt the new layer without making drastic changes to the rest of the model's weights.
- In the second stage, all model weights were trained for 4 epochs. To improve training efficiency, we added support for Flash Attention 2 and contamination-free packing. Documents were packed into sequences of exactly 8192 tokens.
- Since the model's ability to solve both short and long prediction tasks changed during training, the final model is a merge of three checkpoints from different training stages — specifically from epochs 2, 3, and 4 — which ensured a balanced performance across different types of tasks.

## Evaluation - Fine-Tuning

The main advantage of the new model lies in its ability to process longer texts than previously existing Polish encoders. 
For short classification tasks, the model maintains performance comparable to [polish-roberta-large-v2](https://huggingface.co/sdadas/polish-roberta-large-v2). 
We analyzed the capabilities of our model by performing fine-tuning on 25 different tasks in Polish. 
For comparison, we also included the two most popular Polish encoder models — [herbert-large-cased](https://huggingface.co/allegro/herbert-large-cased) and the original [polish-roberta-large-v2](https://huggingface.co/sdadas/polish-roberta-large-v2). 
For each task and model, we performed five separate training runs with different random seeds, and the reported results are averaged values. 
For tasks from the KLEJ benchmark, we used hyperparameters from the original fine-tuning scripts for polish-roberta-large-v2. 
For the remaining tasks, we applied the same hyperparameters for each task: 10 epochs, batch size of 32, a learning rate scheduler with a warmup phase of 6% of the total iterations, a maximum learning rate of 1e-5, and polynomial decay. 
It is important to note that these results may differ slightly from those on the KLEJ leaderboard, which includes fine-tuning results obtained using different frameworks and sets of hyperparameters. 
**Table 1** presents a summary of our results.

<table>
    <tr>
        <th>TASK TYPE</th>
        <th>DOMAIN</th>
        <th>METRIC</th>
        <th>GROUP</th>
        <th>TASK</th>
        <th>herbert-large</th>
        <th>polish-roberta-large-v2</th>
        <th>polish-roberta-8k</th>
    </tr>
    <tr>
        <td>single-label</td>
        <td>mixed</td>
        <td>accuracy</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">NKJP-NER</td>
        <td><strong>96,07</strong></td>
        <td>95,75</td>
        <td>95,64</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>semantics</td>
        <td>accuracy</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">CDSC-E</td>
        <td><strong>94,78</strong></td>
        <td>94,16</td>
        <td>94,28</td>
    </tr>
    <tr>
        <td>regression</td>
        <td>semantics</td>
        <td>spearman</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">CDSC-R</td>
        <td>95,01</td>
        <td>95,25</td>
        <td><strong>95,33</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>social media</td>
        <td>binary-f1</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">CBD</td>
        <td>70,21</td>
        <td>73,10</td>
        <td><strong>73,23</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>reviews</td>
        <td>accuracy</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">POLEMO2.0-IN</td>
        <td>91,39</td>
        <td><strong>93,55</strong></td>
        <td>93,05</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>reviews</td>
        <td>accuracy</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">POLEMO2.0-OUT</td>
        <td>81,66</td>
        <td><strong>83,81</strong></td>
        <td>83,64</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>mixed</td>
        <td>binary-f1</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">DYK</td>
        <td>73,31</td>
        <td><strong>74,87</strong></td>
        <td>74,05</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>news</td>
        <td>binary-f1</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">PSC</td>
        <td><strong>98,85</strong></td>
        <td>98,37</td>
        <td>98,56</td>
    </tr>
    <tr>
        <td>regression</td>
        <td>reviews</td>
        <td>1-wmae</td>
        <td bgcolor="#DAE9F8">KLEJ</td>
        <td bgcolor="#DAE9F8">AR</td>
        <td>89,23</td>
        <td><strong>89,36</strong></td>
        <td>88,91</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>finance</td>
        <td>accuracy</td>
        <td bgcolor="#F2CEEF">FinBench</td>
        <td bgcolor="#F2CEEF">banking-short</td>
        <td>81,80</td>
        <td>81,69</td>
        <td><strong>81,99</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>finance</td>
        <td>accuracy</td>
        <td bgcolor="#F2CEEF">FinBench</td>
        <td bgcolor="#F2CEEF">banking-long</td>
        <td>86,64</td>
        <td>87,89</td>
        <td><strong>88,35</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>finance</td>
        <td>accuracy</td>
        <td bgcolor="#F2CEEF">FinBench</td>
        <td bgcolor="#F2CEEF">banking77</td>
        <td><strong>92,76</strong></td>
        <td>92,45</td>
        <td>92,74</td>
    </tr>
    <tr>
        <td>regression</td>
        <td>finance</td>
        <td>r2-score</td>
        <td bgcolor="#F2CEEF">FinBench</td>
        <td bgcolor="#F2CEEF">fiqa</td>
        <td>61,20</td>
        <td>65,71</td>
        <td><strong>68,43</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>finance</td>
        <td>accuracy</td>
        <td bgcolor="#F2CEEF">FinBench</td>
        <td bgcolor="#F2CEEF">fpb</td>
        <td>84,99</td>
        <td>85,26</td>
        <td><strong>85,42</strong></td>
    </tr>
    <tr>
        <td>multi-label</td>
        <td>finance</td>
        <td>weighted-f1</td>
        <td bgcolor="#F2CEEF">FinBench</td>
        <td bgcolor="#F2CEEF">gcn</td>
        <td><strong>95,25</strong></td>
        <td>95,04</td>
        <td>94,97</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>finance</td>
        <td>accuracy</td>
        <td bgcolor="#F2CEEF">FinBench</td>
        <td bgcolor="#F2CEEF">stooq</td>
        <td>82,53</td>
        <td><strong>85,07</strong></td>
        <td>84,41</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>social media</td>
        <td>accuracy</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">8TAGS</td>
        <td>81,16</td>
        <td><strong>81,64</strong></td>
        <td>81,44</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>social media</td>
        <td>accuracy</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">BAN-PL</td>
        <td>93,25</td>
        <td>93,80</td>
        <td><strong>93,99</strong></td>
    </tr>
    <tr>
        <td>multi-label</td>
        <td>news</td>
        <td>weighted-f1</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">MIPD</td>
        <td>66,79</td>
        <td>67,27</td>
        <td><strong>68,50</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>semantics</td>
        <td>accuracy</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">PPC</td>
        <td>89,78</td>
        <td><strong>89,96</strong></td>
        <td>89,48</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>semantics</td>
        <td>accuracy</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">SICK-E</td>
        <td>87,33</td>
        <td>88,33</td>
        <td><strong>88,96</strong></td>
    </tr>
    <tr>
        <td>regression</td>
        <td>semantics</td>
        <td>spearman</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">SICK-R</td>
        <td>84,37</td>
        <td>85,93</td>
        <td><strong>86,54</strong></td>
    </tr>
    <tr>
        <td>multi-label</td>
        <td>social media</td>
        <td>weighted-f1</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">TwitterEMO</td>
        <td>70,51</td>
        <td><strong>70,70</strong></td>
        <td>70,60</td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>reviews</td>
        <td>accuracy</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">IMDB</td>
        <td>93,55</td>
        <td>94,36</td>
        <td><strong>96,03</strong></td>
    </tr>
    <tr>
        <td>multi-label</td>
        <td>law</td>
        <td>weighted-f1</td>
        <td bgcolor="#DAF2D0">Other</td>
        <td bgcolor="#DAF2D0">EURLEX</td>
        <td>79,68</td>
        <td>79,19</td>
        <td><strong>79,77</strong></td>
    </tr>
</table>

Table 1. Comparison of the mean scores from five fine-tuning runs on 25 discriminative tasks in Polish. The evaluation metrics vary across tasks — the metric used for each task is specified in the **METRIC** column.

Among the tasks mentioned above, four involve classification of long texts. 
In each of these tasks, the new model outperforms the encoders with short context windows. 
These tasks are: **MIPD** (classification of disinformation intent in Polish news articles [(Modzelewski et al. 2024)](https://aclanthology.org/2024.emnlp-main.1103/)), **banking-long** (topical classification into 14 categories of finance and banking-related articles), **IMDB** (sentiment analysis of movie reviews - a dataset translated into Polish from the English version of IMDB, keeping only reviews longer than 2,500 characters), and **EURLEX** (the Polish part of the EUR-Lex corpus, multi-label classification into 21 thematic classes). 
The results for these long-text tasks are presented in **Table 2**, along with the average text length in each dataset.

<table>
    <tr>
        <th>TASK TYPE</th>
        <th>DOMAIN</th>
        <th>METRIC</th>
        <th>AVG. CHARS</th>
        <th>TASK</th>
        <th>herbert-large</th>
        <th>polish-roberta-large-v2</th>
        <th>polish-roberta-8k</th>
    </tr>
    <tr>
        <td>multi-label</td>
        <td>news</td>
        <td>weighted-f1</td>
        <td>5461</td>
        <td>MIPD</td>
        <td>66,79</td>
        <td>67,27</td>
        <td><strong>68,50</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>finance</td>
        <td>accuracy</td>
        <td>2741</td>
        <td>banking-long</td>
        <td>86,64</td>
        <td>87,89</td>
        <td><strong>88,35</strong></td>
    </tr>
    <tr>
        <td>single-label</td>
        <td>reviews</td>
        <td>accuracy</td>
        <td>3597</td>
        <td>IMDB</td>
        <td>93,55</td>
        <td>94,36</td>
        <td><strong>96,03</strong></td>
    </tr>
    <tr>
        <td>multi-label</td>
        <td>law</td>
        <td>weighted-f1</td>
        <td>8255</td>
        <td>EURLEX</td>
        <td>79,68</td>
        <td>79,19</td>
        <td><strong>79,77</strong></td>
    </tr>
</table>

Table 2. Long text classification results.

## Evaluation - Reranking for RAG

A common use case for encoder-type models is their application as retrievers or rerankers in retrieval-augmented generation (RAG) systems. 
Based on this model, we trained a new reranker for the Polish language using the same training procedure as for [polish-reranker-roberta-v2](https://huggingface.co/sdadas/polish-reranker-roberta-v2). 
Evaluation on the [PIRB](https://huggingface.co/spaces/sdadas/pirb) benchmark demonstrated a significant improvement in performance on datasets composed of longer texts. 
**Table 3** presents examples of datasets from this benchmark where performance gains were observed.

<table>
<thead>
<tr>
<th>Task</th>
<th>Improvement using<small><br/>sdadas/mmlw-retrieval-roberta-large<br/></small>retriever</th>
<th>Improvement using<small><br/>BAAI/bge-multilingual-gemma2<br/></small>retriever</th>
<tr>
</thead>
<tbody>

<tr>
<td><strong>eprawnik</strong></td>
<td>70.70 ⟶ 76.43 (+5.73)</td>
<td>73.24 ⟶ 82.36 (+9.12)</td>
</tr>

<tr>
<td><strong>abczdrowie</strong></td>
<td>53.50 ⟶ 58.20 (+4.70)</td>
<td>55.12 ⟶ 61.37 (+6.25)</td>
</tr>

<tr>
<td><strong>specprawnik</strong></td>
<td>43.84 ⟶ 46.06 (+2.22)</td>
<td>52.00 ⟶ 55.74 (+3.74)</td>
</tr>

<tr>
<td><strong>zapytajfizyka</strong></td>
<td>96.10 ⟶ 97.44 (+1.34)</td>
<td>96.09 ⟶ 97.48 (+1.39)</td>
</tr>

<tr>
<td><strong>arguana</strong></td>
<td>63.12 ⟶ 67.42 (+4.30)</td>
<td>63.78 ⟶ 67.53 (+3.75)</td>
</tr>

<tr>
<td><strong>quora</strong></td>
<td>66.61 ⟶ 72.26 (+5.65)</td>
<td>66.30 ⟶ 74.55 (+8.25)</td>
</tr>

</tbody>
</table>

Table 3. Comparison between two rerankers based on **polish-roberta-large-v2** and **polish-roberta-8k** on selected long-context tasks from the PIRB benchmark. We report absolute improvement of NDCG@10 score.

## Acknowledgements
This project is financed by the European Funds, registered under the number FENG.01.01-IP.01-A028/23-00. It focuses on "Building innovative large language models and a service platform for serving multi-task models within the Bank."
The outcomes of this project are the result of a collaboration between the **AI Lab** at the **National Information Processing Institute (Ośrodek Przetwarzania Informacji Państwowy Instytut Badawczy)** and the **AI Team** at **PKO Bank Polski**.

Funding Amount by the European Funds: 9,2 mln PLN

## Citation

```bibtex
@misc{dadas2026longcontext,
  title={Long-Context Encoder Models for Polish Language Understanding},
  author={Sławomir Dadas and Rafał Poświata and Marek Kozłowski and Małgorzata Grębowiec and Michał Perełkiewicz and Paweł Klimiuk and Przemysław Boruta},
  year={2026},
  eprint={2603.12191},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2603.12191}
}
```
