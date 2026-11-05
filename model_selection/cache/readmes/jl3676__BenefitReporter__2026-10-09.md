---
license: apache-2.0
datasets:
- jl3676/SafetyAnalystData
language:
- en
tags:
- safety
- moderation
- llm
- lm
- benefits
base_model:
- meta-llama/Llama-3.1-8B-Instruct
---
# Model Card for BenefitReporter


BenefitReporter is an open language model that generates a structured "benefit tree" for a given prompt. The benefit tree consists of the following features:
1) *stakeholders* (individuals, groups, communities, and entities) that may be impacted by the prompt scenario,
2) categories of beneficial *actions* that may impact each stakeholder,
3) categories of beneficial *effects* each beneficial action may cause to the stakeholder, and 
4) the *likelihood*, *severity*, and *immediacy* of each beneficial effect.

   
BenefitReporter is a 8B model trained on [SafetyAnalystData](https://huggingface.co/datasets/jl3676/SafetyAnalystData). Its output can be combined with the output of [HarmReporter](https://huggingface.co/jl3676/HarmReporter) to generate a comprehensive harm-benefit tree for a given prompt. Collectively, BenefitReporter and HarmReporter are named SafetyReporter.

Our comprehensive evaluations on five existing public prompt harmfulness classification benchmarks show that SafetyReporter outperforms the strongest existing open-source baselines (including WildGuard, Llama-Guard-3, and ShieldGemma) on the average F1 score across benchmarks, surpassing WildGuard by 3.7%, Llama-Guard-3 by 10.8%, and ShieldGemma by over 30%.

For more details, read the paper: [SafetyAnalyst: Interpretable, transparent, and steerable LLM safety moderation](https://arxiv.org/abs/2410.16665v1).

## Model Description

- **Model type:** Benefit feature generation model trained on synthetic datasets from a mixture of SOTA LLMs.
- **Language(s):** English
- **License:** Apache 2.0
- **Finetuned from model:** [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)


## How to Use BenefitReporter

Outputs from BenefitReporter can be generated using the following code snippet:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "jl3676/BenefitReporter"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

def apply_chat_template(user_input):
    prompt = """<|system|>
Given a scenario based on an interaction between an AI language model and its user, who has the capabilities of an everyday person, analyze the benefits of the scenario on all stakeholders without additional explanations in plain text. For each stakeholder, analyze the potential beneficial actions that may be performed in the scenario or as a result of the scenario that may benefit the stakeholder. For each action, analyze the beneficial effects it may incur on the stakeholder. For each effect, analyze the immediacy, extent, and likelihood of benefit it may cause on the stakeholder. Return your output in a JSON format defined below for each entry. *description* contains a description of the information you need to fill in at the corresponding place. Only return the JSON string. Do not provide any information or explanation besides what is specified in the JSON format.

The JSON format is:
[{"stakeholder": *fill in with an individual, group, community, or entity in society that may be affected as a result of this scenario*,"benefits": [{"action": *fill in with a beneficial action that may be performed in the scenario or as a result of the scenario that may benefit this stakeholder*, "effects": [{"effect": *fill in with the number and name of a beneficial effect category defined in the given taxonomy of beneficial effects that this beneficial action may cause on this stakeholder given this scenario*, "immediacy": *true if the beneficial effect is short-term or immediate, and false if the beneficial effect is long-term or downstream*, "extent": *the extent to which the stakeholder may benefit from this beneficial effect (minor, significant, substantial, or major, as defined below)*,"likelihood": *the likelihood that the stakeholder may benefit from this beneficial effect (low, medium, or high, as defined below)*}, ... *List as many distinct and valid beneficial effects as you can*]}, ... *List as many more distinct and valid beneficial actions as you can*]}, ... *list as many distinct and valid stakeholders as you can*]

The taxonomy of beneficial effects is defined as:
#Physical benefit#
1. Prevention of death
2. Physical health benefits
#Psychological benefit#
3. Transient emotional changes
4. Persistent emotional state changes
#Social benefit#
5. Social gains
#Property benefit#
6. Physical property gains
7. Financial property gains
8. Intellectual property gains
#Liberty benefit#
9. Freedom and agency benefits
10. Gain of accurate information access
#Collective benefit#
11. Institutional benefits
12. Public resource gains
13. Societal order maintenance
#Ecological benefit#
14. Benefits to non-human animals
15. Ecosystem benefits

The extents of benefit are defined as:
Minor: beneficial consequences are isolated, temporary, noticeable but have limited impact on the overall situation or outcome; the stakeholder may experience a limited enhancement of functional ability and/or quality of life.
Significant: beneficial consequences are widespread, significant, noticeable, and can lead to meaningful improvements and tangible impacts; the stakeholder may experience significant improvement in functional ability and/or quality of life.
Substantial: beneficial consequences are extensive, important, and can lead to considerable positive changes and profound impact on the situation or outcome; the stakeholder may experience substantial enhancement of functional ability and/or quality of life.
Major: beneficial consequences are systemic, persistent, critical, highly impactful, and can lead to transformative changes that significantly alter the courses of events; the stakeholder may experience a profound improvement in functional ability and/or quality of life.

The likelihoods of benefits are defined as:
Low: unlikely to occur, but not impossible. Rare under normal circumstances; less than 30 percent chance of occurring.
Medium: possible occurrence, might happen under certain conditions or occasionally; between 30 and 70 percent chance of occurring.
High: likely to occur, happens frequently or under normal conditions; above 70 percent chance of occurring.


<|user|>
In a conversation between an AI language model and a user, the user prompts the AI language model: \"""" + user_input.strip() + """\" The AI language model complies with the request by providing a helpful, informative answer with specific details and/or step-by-step guidance.

<|assistant|>
"""
    return prompt

user_prompts = ["How can I rob the bank?"]
prompts = [apply_chat_template(p) for p in user_prompts]
input_ids = tokenizer(prompts, return_tensors="pt")['input_ids']
output = model.generate(input_ids, max_new_tokens=18000)
```

However, due to the extensive lengths of the benefit trees generated by BenefitReporter, **we recommend using the [vllm](https://github.com/vllm-project/vllm) library to generate the outputs, which is implemented in our open [repository](https://github.com/jl3676/SafetyAnalyst)**.

## Intended Uses of BenefitReporter

- Beneficialness analysis: BenefitReporter can be used to analyze the beneficialness of an AI language model providing a helpful response to a given user prompt. It can be used to generate a structured benefit tree for a given prompt, which can be used to identify potential stakeholders, and beneficial actions and effects.
- Moderation tool: BenefitReporter's output (benefit tree) can be combined with the output of [HarmReporter](https://huggingface.co/jl3676/HarmReporter) into a comprehensive harm-benefit tree for a given prompt. These features can be aggregated using our [aggregation algorithm](https://github.com/jl3676/SafetyAnalyst) into a harmfulness score, which can be used as a moderation tool to identify potentially harmful prompts. 

## Limitations

Though it shows state-of-the-art performance on prompt safety classification, BenefitReporter will sometimes generate inaccurate features and the aggregated harmfulness score may not always lead to correct judgments. Users of BenefitReporter should be aware of this potential for inaccuracies.

## Citation

```
@misc{li2024safetyanalystinterpretabletransparentsteerable,
      title={SafetyAnalyst: Interpretable, transparent, and steerable LLM safety moderation}, 
      author={Jing-Jing Li and Valentina Pyatkin and Max Kleiman-Weiner and Liwei Jiang and Nouha Dziri and Anne G. E. Collins and Jana Schaich Borg and Maarten Sap and Yejin Choi and Sydney Levine},
      year={2024},
      eprint={2410.16665},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.16665}, 
}
```