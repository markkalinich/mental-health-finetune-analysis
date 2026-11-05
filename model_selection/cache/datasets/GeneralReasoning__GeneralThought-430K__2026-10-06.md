---
language:
- en
license: mit
---

# GeneralThought-430K

> Thought wants to be free

Open reasoning data for March 14 2025. This dataset was part of a side-project in the weeks following the R1 release by Chengxi and Ross - we are no longer maintaining this
dataset but are archiving it here.

The dataset contains questions, reference answers, reasoning traces, final answers and other metadata from several popular reasoning models including [DeepSeek-R1](https://gr.inc/DeepSeek/models/DeepSeek-R1/), [DeepSeek-R1-Zero](https://gr.inc/DeepSeek/models/DeepSeek-R1-Zero/), [OpenThoughts-32B](https://gr.inc/open-thoughts/models/OpenThinker-32B/), [LIMO](https://gr.inc/GAIR-NLP/models/LIMO/), [deepseek-r1-distill-llama-70b](https://gr.inc/DeepSeek/models/deepseek-r1-distill-llama-70b/), [DeepHermes-3-Llama-3-8B-Preview](https://gr.inc/NousResearch/models/DeepHermes-3-Llama-3-8B-Preview/) and [DeepScaleR-1.5B-Preview](https://gr.inc/agentica-org/models/DeepScaleR-1.5B-Preview/). We also include final answers from [o3-mini-2025-01-31](https://gr.inc/OpenAI/models/o3-mini-2025-01-31/),  [gemini-2-flash-thinking-exp-01-21](https://gr.inc/Google/models/gemini-2-flash-thinking-exp-01-21/) and [claude-3-7-sonnet-20250219](https://gr.inc/Anthropic/models/claude-3-7-sonnet-20250219/) for comparison and evaluation. This release has 430k rows of data.

## Improvements

The main improvement in this update is trace diversity. There are many more reasoning traces beyond mathematics and code, including the natural sciences, humanities, social sciences, and general conversations.

## Metadata

A row of data contains the following information:

```python
row = {
  'question_id': '296582', # question ID on the GR resource
  'question': 'Of a quadrilateral if its angle measures are in the ratio of 3:4:5:6, find the measure of each angle.', # Question text
  'prev_messages': None, # previous messages in the conversation
  'reference_answer': '60°, 80°, 100°, 120°', # Reference answer
  'model_name': 'DeepSeek/DeepSeek-R1', # The model that generated the trace
  'model_answer': 'The measures of the angles in the quadrilateral are calculated as follows...', # the model final answer text
  'model_reasoning': 'Okay, so I need to find the measures of each angle in a quadrilateral...' # the model reasoning text
  'task': 'Applying Ratios to Angle-Measure Sums', # name of the task on GR
  'question_license': 'MIT', # license of the question
  'question_source': 'General/VNet', # original dataset source or author on GR
  'community_question_score': 0 # community score for the question on GR; negative means downvoted, positive upvoted,
  'community_answer_score': 0, # community score for the answer on GR; negative means downvoted, positive upvoted
  'verifier_score': 1.0 # an average verification score between 0-1; if multiple verifiers, this could be between, e.g. 0.5 if one verifier marks as correct, another incorrect
}
```

## How can I use the data?

The dataset is a great complement to [OpenThoughts-114k](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k), [OpenR1](https://huggingface.co/datasets/open-r1/OpenR1-Math-Raw), [SYNTHETIC-1](https://huggingface.co/datasets/PrimeIntellect/SYNTHETIC-1), among others!

Here's some example use cases for our dataset:

- Perform SFT distillation and use it to train a small reasoning model.
- Ablate alongside datasets from our open source friends (and see if cross-group diversity helps).
- Analyse reasoning differences between models: reasoning length, language switching, and use of connectors like "wait" and "alternatively".

## Thanks

Thank you to the contributors of questions for this dataset:

First - thanks to the questions we sourced from folks like [Numina](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT), [SCP-116k](https://huggingface.co/datasets/EricLu/SCP-116K), [natural_reasoning](https://huggingface.co/datasets/facebook/natural_reasoning) and others! We've credited you in the question_source field of each row of the dataset.

Thanks to contributors:
- Jarius, otaldohenrikk, knight_raider, supahao, alpam, Esac, gonros, tomsercu, ryan, sidoneytemporary977, panpan, Tim_tom_0, arpitg1991, Doge, tginart, pcpthm, eli5, yych, caijie, yuchen.zhang2003, lockon, susheelt, wangxinjing, duyiyang, Slimane, FABGYUXIN, chendarcy, Sin, robintan, imhillxtz, navinahc, z, zhangdapao, yixiangRDS500
