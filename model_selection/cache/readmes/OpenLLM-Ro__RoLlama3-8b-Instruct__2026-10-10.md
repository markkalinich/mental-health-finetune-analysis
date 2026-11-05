---
license: cc-by-nc-4.0
language:
- ro
base_model:
- meta-llama/Meta-Llama-3-8B-Instruct
datasets:
- OpenLLM-Ro/ro_sft_alpaca
- OpenLLM-Ro/ro_sft_alpaca_gpt4
- OpenLLM-Ro/ro_sft_dolly
- OpenLLM-Ro/ro_sft_selfinstruct_gpt4
- OpenLLM-Ro/ro_sft_norobots
- OpenLLM-Ro/ro_sft_orca
- OpenLLM-Ro/ro_sft_camel
- OpenLLM-Ro/ro_sft_oasst
- OpenLLM-Ro/ro_sft_ultrachat
- OpenLLM-Ro/ro_sft_magpie_mt
- OpenLLM-Ro/ro_sft_magpie_reasoning
model-index:
    - name: OpenLLM-Ro/RoLlama3-8b-Instruct-2025-04-23
      results:
        - task:
            type: text-generation
          dataset:
            name: RoMT-Bench
            type: RoMT-Bench
          metrics:
            - name: Score
              type: Score
              value: 6.39
        - task:
            type: text-generation
          dataset:
            name: RoCulturaBench
            type: RoCulturaBench
          metrics:
            - name: Score
              type: Score
              value: 4.05
        - task:
            type: text-generation
          dataset:
            name: Romanian_Academic_Benchmarks
            type: Romanian_Academic_Benchmarks
          metrics:
            - name: Average accuracy
              type: accuracy
              value: 54.66
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_arc_challenge
            type: OpenLLM-Ro/ro_arc_challenge
          metrics:
            - name: Average accuracy
              type: accuracy
              value: 50.31
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_mmlu
            type: OpenLLM-Ro/ro_mmlu
          metrics:
            - name: Average accuracy
              type: accuracy
              value: 55.91
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_winogrande
            type: OpenLLM-Ro/ro_winogrande
          metrics:
            - name: Average accuracy
              type: accuracy
              value: 67.01
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_hellaswag
            type: OpenLLM-Ro/ro_hellaswag
          metrics:
            - name: Average accuracy
              type: accuracy
              value: 61.73
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_gsm8k
            type: OpenLLM-Ro/ro_gsm8k
          metrics:
            - name: Average accuracy
              type: accuracy
              value: 47.41
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_truthfulqa
            type: OpenLLM-Ro/ro_truthfulqa
          metrics:
            - name: Average accuracy
              type: accuracy
              value: 45.61
        - task:
            type: text-generation
          dataset:
            name: LaRoSeDa_binary
            type: LaRoSeDa_binary
          metrics:
            - name: Average macro-f1
              type: macro-f1
              value: 96.21
        - task:
            type: text-generation
          dataset:
            name: LaRoSeDa_multiclass
            type: LaRoSeDa_multiclass
          metrics:
            - name: Average macro-f1
              type: macro-f1
              value: 59.15
        - task:
            type: text-generation
          dataset:
            name: WMT_EN-RO
            type: WMT_EN-RO
          metrics:
            - name: Average bleu
              type: bleu
              value: 23.32
        - task:
            type: text-generation
          dataset:
            name: WMT_RO-EN
            type: WMT_RO-EN
          metrics:
            - name: Average bleu
              type: bleu
              value: 22.50
        - task:
            type: text-generation
          dataset:
            name: XQuAD
            type: XQuAD
          metrics:
            - name: Average exact_match
              type: exact_match
              value: 11.01
        - task:
            type: text-generation
          dataset:
            name: XQuAD
            type: XQuAD
          metrics:
            - name: Average f1
              type: f1
              value: 23.55
        - task:
            type: text-generation
          dataset:
            name: STS
            type: STS
          metrics:
            - name: Average spearman
              type: spearman
              value: 76.78
        - task:
            type: text-generation
          dataset:
            name: STS
            type: STS
          metrics:
            - name: Average pearson
              type: pearson
              value: 74.36
        - task:
            type: text-generation
          dataset:
            name: RoMT-Bench
            type: RoMT-Bench
          metrics:
            - name: First turn
              type: Score
              value: 7.12
            - name: Second turn
              type: Score
              value: 5.66
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_arc_challenge
            type: OpenLLM-Ro/ro_arc_challenge
          metrics:
            - name: 0-shot 
              type: accuracy
              value: 48.33
            - name: 1-shot 
              type: accuracy
              value: 49.27
            - name: 3-shot 
              type: accuracy
              value: 49.19
            - name: 5-shot 
              type: accuracy
              value: 50.90
            - name: 10-shot 
              type: accuracy
              value: 51.67
            - name: 25-shot 
              type: accuracy
              value: 52.53
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_mmlu
            type: OpenLLM-Ro/ro_mmlu
          metrics:
            - name: 0-shot 
              type: accuracy
              value: 54.17
            - name: 1-shot 
              type: accuracy
              value: 56.19
            - name: 3-shot 
              type: accuracy
              value: 56.90
            - name: 5-shot 
              type: accuracy
              value: 56.37
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_winogrande
            type: OpenLLM-Ro/ro_winogrande
          metrics:
            - name: 0-shot 
              type: accuracy
              value: 65.82
            - name: 1-shot 
              type: accuracy
              value: 66.22
            - name: 3-shot 
              type: accuracy
              value: 66.85
            - name: 5-shot 
              type: accuracy
              value: 69.14
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_hellaswag
            type: OpenLLM-Ro/ro_hellaswag
          metrics:
            - name: 0-shot 
              type: accuracy
              value: 61.67
            - name: 1-shot 
              type: accuracy
              value: 62.06
            - name: 3-shot 
              type: accuracy
              value: 61.73
            - name: 5-shot 
              type: accuracy
              value: 61.28
            - name: 10-shot 
              type: accuracy
              value: 61.93
        - task:
            type: text-generation
          dataset:
            name: OpenLLM-Ro/ro_gsm8k
            type: OpenLLM-Ro/ro_gsm8k
          metrics:
            - name: 1-shot 
              type: accuracy
              value: 35.63
            - name: 3-shot 
              type: accuracy
              value: 51.33
            - name: 5-shot 
              type: accuracy
              value: 55.27
        - task:
            type: text-generation
          dataset:
            name: LaRoSeDa_binary
            type: LaRoSeDa_binary
          metrics:
            - name: 0-shot 
              type: macro-f1
              value: 94.05
            - name: 1-shot 
              type: macro-f1
              value: 96.46
            - name: 3-shot 
              type: macro-f1
              value: 96.97
            - name: 5-shot 
              type: macro-f1
              value: 97.37
        - task:
            type: text-generation
          dataset:
            name: LaRoSeDa_multiclass
            type: LaRoSeDa_multiclass
          metrics:
            - name: 0-shot 
              type: macro-f1
              value: 60.34
            - name: 1-shot 
              type: macro-f1
              value: 60.94
            - name: 3-shot 
              type: macro-f1
              value: 54.55
            - name: 5-shot 
              type: macro-f1
              value: 60.77
        - task:
            type: text-generation
          dataset:
            name: WMT_EN-RO
            type: WMT_EN-RO
          metrics:
            - name: 0-shot 
              type: bleu
              value: 5.38
            - name: 1-shot 
              type: bleu
              value: 29.60
            - name: 3-shot 
              type: bleu
              value: 30.62
            - name: 5-shot 
              type: bleu
              value: 27.67
        - task:
            type: text-generation
          dataset:
            name: WMT_RO-EN
            type: WMT_RO-EN
          metrics:
            - name: 0-shot 
              type: bleu
              value: 1.14
            - name: 1-shot 
              type: bleu
              value: 19.96
            - name: 3-shot 
              type: bleu
              value: 34.22
            - name: 5-shot 
              type: bleu
              value: 34.69
        - task:
            type: text-generation
          dataset:
            name: XQuAD_EM
            type: XQuAD_EM
          metrics:
            - name: 0-shot 
              type: exact_match
              value: 16.39
            - name: 1-shot 
              type: exact_match
              value: 18.49
            - name: 3-shot 
              type: exact_match
              value: 5.46
            - name: 5-shot 
              type: exact_match
              value: 3.70
        - task:
            type: text-generation
          dataset:
            name: XQuAD_F1
            type: XQuAD_F1
          metrics:
            - name: 0-shot 
              type: f1
              value: 33.84
            - name: 1-shot 
              type: f1
              value: 29.11
            - name: 3-shot 
              type: f1
              value: 15.27
            - name: 5-shot 
              type: f1
              value: 15.97
        - task:
            type: text-generation
          dataset:
            name: STS_Spearman
            type: STS_Spearman
          metrics:
            - name: 1-shot 
              type: spearman
              value: 76.64
            - name: 3-shot 
              type: spearman
              value: 76.88
            - name: 5-shot 
              type: spearman
              value: 76.82
        - task:
            type: text-generation
          dataset:
            name: STS_Pearson
            type: STS_Pearson
          metrics:
            - name: 1-shot 
              type: pearson
              value: 73.14
            - name: 3-shot 
              type: pearson
              value: 74.78
            - name: 5-shot 
              type: pearson
              value: 75.16

---

# Model Card for Model ID

*Built with Meta Llama 3*

This model points/is identical to [RoLlama3-8b-Instruct-2025-04-23](https://huggingface.co/OpenLLM-Ro/RoLlama3-8b-Instruct-2025-04-23).


<!-- Provide a quick summary of what the model is/does. -->

RoLlama3 is a family of pretrained and fine-tuned generative text models for Romanian. This is the repository for the **instruct 8B model**. Links to other models can be found at the bottom of this page.


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->
OpenLLM-Ro represents the first open-source effort to build a LLM specialized for Romanian. OpenLLM-Ro developed and publicly releases a collection of Romanian LLMs, both in the form of foundational model and instruct and chat variants.


- **Developed by:** OpenLLM-Ro
<!-- - **Funded by [optional]:** [More Information Needed] -->
<!-- - **Shared by [optional]:** [More Information Needed] -->
<!-- - **Model type:** [More Information Needed] -->
- **Language(s):** Romanian
- **License:** cc-by-nc-4.0
- **Finetuned from model:** [Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
- **Trained using:** [RoAlpaca](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_alpaca), [RoAlpacaGPT4](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_alpaca_gpt4), [RoDolly](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_dolly), [RoSelfInstruct](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_selfinstruct_gpt4), [RoNoRobots](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_norobots), [RoOrca](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_orca), [RoCamel](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_camel), [RoOpenAssistant](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_oasst), [RoUltraChat](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_ultrachat), [RoMagpiePro](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_magpie_mt), [RoMagpieReasoning](https://huggingface.co/datasets/OpenLLM-Ro/ro_sft_magpie_reasoning)


### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/OpenLLM-Ro/LLaMA-Factory
- **Paper:** https://arxiv.org/abs/2406.18266

## Intended Use

### Intended Use Cases

RoLlama3 is intented for research use in Romanian. Base models can be adapted for a variety of natural language tasks while instruction and chat tuned models are intended for assistant-like chat.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

Use in any manner that violates the license, any applicable laws or regluations, use in languages other than Romanian.



## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("OpenLLM-Ro/RoLlama3-8b-Instruct")
model = AutoModelForCausalLM.from_pretrained("OpenLLM-Ro/RoLlama3-8b-Instruct")

instruction = "Ce jocuri de societate pot juca cu prietenii mei?"
chat = [
        {"role": "system", "content": "Ești un asistent folositor, respectuos și onest. Încearcă să ajuți cât mai mult prin informațiile oferite, excluzând răspunsuri toxice, rasiste, sexiste, periculoase și ilegale."},
        {"role": "user", "content": instruction},
        ]
prompt = tokenizer.apply_chat_template(chat, tokenize=False, system_message="")

inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
outputs = model.generate(input_ids=inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0]))
```

## Academic Benchmarks

<table>
<tbody>
<tr>
<td><strong>Model</strong></td>
<td><strong><center>Average</center></strong></td>
<td><strong><center>ARC</center></strong></td>
<td><strong><center>MMLU</center></strong></td>
<td><strong><center>Winogrande</center></strong></td>
<td><strong><center>Hellaswag</center></strong></td>
<td><strong><center>GSM8k</center></strong></td>
<td><strong><center>TruthfulQA</center></strong></td>
</tr>
<tr>
<td>Llama-3-8B-Instruct</td><td><center>50.62</center></td><td><center>43.69</center></td><td><center>52.04</center></td><td><center>59.33</center></td><td><center>53.19</center></td><td><center>43.87</center></td><td><center>51.59</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-06-28</td><td><center>50.56</center></td><td><center>44.70</center></td><td><center>52.19</center></td><td><center><strong>67.23</strong></center></td><td><center>57.69</center></td><td><center>30.23</center></td><td><center>51.34</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-10-09</td><td><center>52.21</center></td><td><center>47.94</center></td><td><center>53.50</center></td><td><center>66.06</center></td><td><center>59.72</center></td><td><center>40.16</center></td><td><center>45.90</center></td>
</tr>
<tr>
<td><em>RoLlama3-8b-Instruct-2025-04-23</em></td><td><center><em>54.66</em></center></td><td><center><em>50.31</em></center></td><td><center><em><strong>55.91</strong></em></center></td><td><center><em>67.01</em></center></td><td><center><em><strong>61.73</strong></em></center></td><td><center><em><strong>47.41</strong></em></center></td><td><center><em>45.61</em></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2024-10-09</td><td><center>49.96</center></td><td><center>46.29</center></td><td><center>53.29</center></td><td><center>65.57</center></td><td><center>58.15</center></td><td><center>34.77</center></td><td><center>41.70</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2025-04-23</td><td><center><strong>55.86</strong></center></td><td><center><strong>52.26</strong></center></td><td><center>55.35</center></td><td><center>66.62</center></td><td><center>59.93</center></td><td><center>43.95</center></td><td><center><strong>57.06</strong></center></td>
</tr>
</tbody>
</table>

  
## Downstream tasks

<table>
<tbody>
<tr>
<td></td>
<td colspan="4"><center><strong>LaRoSeDa</strong></center></td>
<td colspan="4"><center><strong>WMT</strong></center></td>
</tr>
<tr>
<td></td>
<td colspan="2"><center><strong>Few-shot</strong></center></td>
<td colspan="2"><center><strong>Finetuned</strong></center></td>
<td colspan="2"><center><strong>Few-shot</strong></center></td>
<td colspan="2"><center><strong>Finetuned</strong></center></td>
</tr>
<tr>
<td><strong>Model</strong></td>
<td><center><strong>Binary<br>(Macro F1)</strong></center></td>
<td><center><strong>Multiclass<br>(Macro F1)</strong></center></td>
<td><center><strong>Binary<br>(Macro F1)</strong></center></td>
<td><center><strong>Multiclass<br>(Macro F1)</strong></center></td>
<td><center><strong>EN-RO<br>(Bleu)</strong></center></td>
<td><center><strong>RO-EN<br>(Bleu)</strong></center></td>
<td><center><strong>EN-RO<br>(Bleu)</strong></center></td>
<td><center><strong>RO-EN<br>(Bleu)</strong></center>
</tr>
<tr>
<td>Llama-3-8B-Instruct</td><td><center>95.88</center></td><td><center>56.21</center></td><td><center><strong>98.53</strong></center></td><td><center>86.19</center></td><td><center>18.88</center></td><td><center><strong>30.98</strong></center></td><td><center><strong>28.02</strong></center></td><td><center>40.28</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-06-28</td><td><center>97.52</center></td><td><center><strong>67.41</strong></center></td><td><center>94.15</center></td><td><center>87.13</center></td><td><center><strong>24.01</strong></center></td><td><center>27.36</center></td><td><center>26.53</center></td><td><center>40.36</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-10-09</td><td><center>95.58</center></td><td><center>61.20</center></td><td><center>96.46</center></td><td><center><strong>87.26</strong></center></td><td><center>22.92</center></td><td><center>24.28</center></td><td><center>27.31</center></td><td><center><strong>40.52</strong></center></td>
</tr>
<tr>
<td><em>RoLlama3-8b-Instruct-2025-04-23</em></td><td><center><em>96.21</em></center></td><td><center><em>59.15</em></center></td><td><center><em>-</em></center></td><td><center><em>-</em></center></td><td><center><em>23.32</em></center></td><td><center><em>22.50</em></center></td><td><center><em>-</em></center></td><td><center><em>-</em></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2024-10-09</td><td><center>97.48</center></td><td><center>54.00</center></td><td><center>-</center></td><td><center>-</center></td><td><center>22.09</center></td><td><center>23.00</center></td><td><center>-</center></td><td><center>-</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2025-04-23</td><td><center><strong>97.60</strong></center></td><td><center>62.16</center></td><td><center>-</center></td><td><center>-</center></td><td><center>18.14</center></td><td><center>14.13</center></td><td><center>-</center></td><td><center>-</center></td>
</tr>
</tbody>
</table>


<table>
<tbody>
<tr>
<td></td>
<td colspan="4"><center><strong>XQuAD</strong></center></td>
<td colspan="4"><center><strong>STS</strong></center></td>
</tr>
<tr>
<td></td>
<td colspan="2"><center><strong>Few-shot</strong></center></td>
<td colspan="2"><center><strong>Finetuned</strong></center></td>
<td colspan="2"><center><strong>Few-shot</strong></center></td>
<td colspan="2"><center><strong>Finetuned</strong></center></td>
</tr>
<tr>
<td><strong>Model</strong></td>
<td><center><strong>(EM)</strong></center></td>
<td><center><strong>(F1)</strong></center></td>
<td><center><strong>(EM)</strong></center></td>
<td><center><strong>(F1)</strong></center></td>
<td><center><strong>(Spearman)</strong></center></td>
<td><center><strong>(Pearson)</strong></center></td>
<td><center><strong>(Spearman)</strong></center></td>
<td><center><strong>(Pearson)</strong></center></td>
</tr>
<tr>
<td>Llama-3-8B-Instruct</td><td><center><strong>39.47</strong></center></td><td><center>58.67</center></td><td><center><strong>67.65</strong></center></td><td><center><strong>82.77</strong></center></td><td><center>73.04</center></td><td><center>72.36</center></td><td><center>83.49</center></td><td><center>84.06</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-06-28</td><td><center>39.43</center></td><td><center><strong>59.50</strong></center></td><td><center>44.45</center></td><td><center>59.76</center></td><td><center>77.20</center></td><td><center>77.87</center></td><td><center>85.80</center></td><td><center>86.05</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-10-09</td><td><center>18.89</center></td><td><center>31.79</center></td><td><center>50.84</center></td><td><center>65.18</center></td><td><center>77.60</center></td><td><center>76.86</center></td><td><center><strong>86.70</strong></center></td><td><center><strong>87.09</strong></center></td>
</tr>
<tr>
<td><em>RoLlama3-8b-Instruct-2025-04-23</em></td><td><center><em>11.01</em></center></td><td><center><em>23.55</em></center></td><td><center><em>-</em></center></td><td><center><em>-</em></center></td><td><center><em>76.78</em></center></td><td><center><em>74.36</em></center></td><td><center><em>-</em></center></td><td><center><em>-</em></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2024-10-09</td><td><center>26.05</center></td><td><center>42.77</center></td><td><center>-</center></td><td><center>-</center></td><td><center><strong>79.64</strong></center></td><td><center><strong>79.52</strong></center></td><td><center>-</center></td><td><center>-</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2025-04-23</td><td><center>30.65</center></td><td><center>46.29</center></td><td><center>-</center></td><td><center>-</center></td><td><center>67.62</center></td><td><center>67.82</center></td><td><center>-</center></td><td><center>-</center></td>
</tr>
</tbody>
</table>

## MT-Bench

<table>
<tbody>
<tr>
<td><strong>Model</strong></td>
<td><strong><center>Average</center></strong></td>
<td><strong><center>1st turn</center></strong></td>
<td><strong><center>2nd turn</center></strong></td>
<td><strong><center>Answers in Ro</center></strong></td>
</tr>
<tr>
<td>Llama-3-8B-Instruct</td><td><center>5.96</center></td><td><center>6.16</center></td><td><center>5.76</center></td><td><center>158/160</center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-06-28</td><td><center>5.15</center></td><td><center>6.03</center></td><td><center>4.28</center></td><td><center><strong>160/160</strong></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-10-09</td><td><center>5.38</center></td><td><center>6.09</center></td><td><center>4.67</center></td><td><center><strong>160/160</strong></center></td>
</tr>
<tr>
<td><em>RoLlama3-8b-Instruct-2025-04-23</em></td><td><center><em>6.39</em></center></td><td><center><em><strong>7.12</strong></em></center></td><td><center><em>5.66</em></center></td><td><center><em><strong>160/160</strong></em></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2024-10-09</td><td><center>5.87</center></td><td><center>6.22</center></td><td><center>5.49</center></td><td><center><strong>160/160</strong></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2025-04-23</td><td><center><strong>6.67</strong></center></td><td><center>6.81</center></td><td><center><strong>6.54</strong></center></td><td><center><strong>160/160</strong></center></td>
</tr>
</tbody>
</table>


## RoCulturaBench

<table>
<tbody>
<tr>
<td><strong>Model</strong></td>
<td><strong><center>Average</center></strong></td>
<td><strong><center>Answers in Ro</center></strong></td>
</tr>
<tr>
<td>Llama-3-8B-Instruct</td><td><center>4.62</center></td><td><center><strong>100/100</strong></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-06-28</td><td><center>3.71</center></td><td><center><strong>100/100</strong></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-2024-10-09</td><td><center>3.81</center></td><td><center><strong>100/100</strong></center></td>
</tr>
<tr>
<td><em>RoLlama3-8b-Instruct-2025-04-23</em></td><td><center><em>4.05</em></center></td><td><center><em><strong>100/100</strong></em></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2024-10-09</td><td><center>4.40</center></td><td><center><strong>100/100</strong></center></td>
</tr>
<tr>
<td>RoLlama3-8b-Instruct-DPO-2025-04-23</td><td><center><strong>4.83</strong></center></td><td><center><strong>100/100</strong></center></td>
</tr>
</tbody>
</table>



## RoLlama3 Model Family

| Model              | Link  |
|--------------------|:--------:|
|RoLlama3-8b-Instruct-2024-06-28| [link](https://huggingface.co/OpenLLM-Ro/RoLlama3-8b-Instruct-2024-06-28) |
|RoLlama3-8b-Instruct-2024-10-09| [link](https://huggingface.co/OpenLLM-Ro/RoLlama3-8b-Instruct-2024-10-09) |
|*RoLlama3-8b-Instruct-2025-04-23*| [link](https://huggingface.co/OpenLLM-Ro/RoLlama3-8b-Instruct-2025-04-23) |
|RoLlama3-8b-Instruct-DPO-2024-10-09| [link](https://huggingface.co/OpenLLM-Ro/RoLlama3-8b-Instruct-DPO-2024-10-09) |
|RoLlama3-8b-Instruct-DPO-2025-04-23| [link](https://huggingface.co/OpenLLM-Ro/RoLlama3-8b-Instruct-DPO-2025-04-23) |


## Citation 

```
@inproceedings{masala-etal-2024-vorbesti,
    title = "``Vorbe\c{s}ti Rom{\^a}ne\c{s}te?'' A Recipe to Train Powerful {R}omanian {LLM}s with {E}nglish Instructions",
    author = "Masala, Mihai and Ilie-Ablachim, Denis and Dima, Alexandru and Corlatescu, Dragos Georgian and Zavelca, Miruna-Andreea and Olaru, Ovio and Terian, Simina-Maria and Terian, Andrei and Leordeanu, Marius and Velicu, Horia and Popescu, Marius and Dascalu, Mihai and Rebedea, Traian",
    editor = "Al-Onaizan, Yaser and Bansal, Mohit and Chen, Yun-Nung",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-emnlp.681/",
    doi = "10.18653/v1/2024.findings-emnlp.681",
    pages = "11632--11647"
}
```
<!-- **APA:**

[More Information Needed]  -->