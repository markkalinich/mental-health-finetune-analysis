# Offline chat-template screen

Cohort: 53 children in `final-kept.txt`, exact-joined to `instruct-parent-kept.csv`, plus 27 parents that are not themselves in that child list. 80 repositories. Tokenizer only, `local_files_only=True`, from `/home/mkalinich/hf_models/<org>__<name>`. Weights were not loaded.

Shape 1 is the client request: a system message followed by a user message. Shape 2 is a single user message with the system text prepended. Both calls use `apply_chat_template(..., tokenize=False, add_generation_prompt=True)`.

Counts partition the repositories. A repository with no chat template is counted under no template, including when both renders raise. Fail both means a template is present and both renders raise.

| Bucket | Count |
|---|---:|
| Render shape 1 | 64 |
| Fail shape 1, render shape 2 | 4 |
| No template | 1 |
| Fail both | 0 |
| Not on disk | 11 |
| Tokenizer load failed | 0 |
| Total | 80 |

Shape 1 rendered for 64. Shape 1 failed and shape 2 rendered for 4. No template: 1. Fail both: 0. Not on disk: 11.

## Fail shape 1

Render was attempted and shape 1 raised. This includes the no-template repositories.

- `JaeJiMin/daily_hug`
- `ecorbari/Gemma-2b-it-Psych-Merged`
- `menzo-ai/mental-health-chatbot`
- `google/gemma-2-2b-it`
- `google/gemma-2b-it`

### Fail shape 1, render shape 2

- `JaeJiMin/daily_hug`
- `ecorbari/Gemma-2b-it-Psych-Merged`
- `google/gemma-2-2b-it`
- `google/gemma-2b-it`

### Fail both

_none_

## No template

- `menzo-ai/mental-health-chatbot`

## Not on disk

Missing directory:

_none_

Directory present, no tokenizer files:

- `AIMH/SQPsych-8b-gemma-Qwen`
- `AIMH/SQPsych-8b-gemma-Qwen_no_questionnaire`
- `AIMH/SQPsychLLM-8b-command`
- `AIMH/SQPsychLLM-8b-command-no_questionnaire`
- `AIMH/SQPsychLLM-8b-gemma`
- `AIMH/SQPsychLLM-8b-gemma-no_questionnaire`
- `AIMH/SQPsychLLM-8b-llama3.3`
- `AIMH/SQPsychLLM-8b-mistral`
- `AIMH/SQPsychLLM-8b-nemotron`
- `AIMH/SQPsychLLM-8b-qwen-2.5`
- `AIMH/SQPsychLLM-8b-qwq`

Those directories are on disk. None of them contains a tokenizer file, so the chat template was not read.

## Tokenizer load failed

_none_

This screen does not change how any model is called.
