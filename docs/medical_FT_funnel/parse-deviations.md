<!-- doc-verbosity: public-ready -->

# Parse deviations, medical fine-tunes

The study parser is `parse_study_reply` in `utilities/model_output_rules.py`. It is what `orchestration/run_experiment.py` stores in `cache/results.db`. A reply the rule does not accept stays a parse failure, and a parse failure counts as wrong.

Rows already stored for these models were rewritten on 15 October 2026 so the cache matches this parser. The raw reply text was not changed. The summary JSON files written during the overnight run still hold the parse counts from before this change.

## HealthCareMagic

Model: `geshijoker/HealthCareMagic_sft_llama3_instruct_full`. Prompt: `suicide_ideation_yesno_v1`.

The reply is a Chat Doctor paragraph, including an opening such as "Thanks for choosing Chat Doctor". That paragraph is the answer. The one-word ladder is not used for this model, because the paragraph often contains the word "no" in a sentence that is not the label ("there is no way out", "there is no expiration date").

The reply is no when it says the message is not suicidal ideation, does not contain it, or is not a suicide note. The reply is yes when it says the message does contain suicidal ideation, names suicidal thoughts, suicidal ideas, or suicide ideation, says the answer is yes, says suicide is the only way out, or says the person is thinking of suicide.

A paragraph that only gives medical advice is wrong. "Suicide is not a solution" and a helpline number, with no sentence of the kind above, are advice.

## Four DeepSeek Llama fine-tunes

Models:

- `Fornit/DeepSeek-R1-Medical-COT-LORA`
- `Melody923/DeepSeek-R1-Medicalai-923`
- `Mouhib007/DeepSeek-r1-Medical-Mini`
- `mlxha/DeepSeek-R1-Distill-Llama-8B-GRPO-medmcqa`

The reply text uses U+0120 where a space belongs and U+010A where a newline belongs. The parser replaces those two characters and then reads a JSON object the same way it does for every other model. A class named only inside a sentence, with no JSON object, is not an answer.

These four models, and no mental-health fine-tune of this parent, were removed on 16 October 2026 (`manual_removals.csv`). C-SSRS does not use this repair. The C-SSRS files are reasoning traces; after the character repair the five-label parser still accepts only the replies whose last line is the label (80, 0, 81, and 1 of 500).

## What a parse is

Synthetic suicidal ideation (`suicide_ideation_yesno_v1`): the reply is `yes` or `no`. A closed `<think>...</think>` block is removed first. An unclosed `<think>` is a failure, because the model never finished the reasoning and never reached an answer. The parser does not read a label out of an unfinished think block. That is the right refusal when the block names more than one class. It will miss a model that puts the answer only inside a think block and then gets cut off.

Reddit C-SSRS (`cssrs_severity_v1`): the reply is one of Supportive, Indicator, Ideation, Behavior, Attempt, as the first line, as the whole reply, or as a JSON field. A word inside a paragraph is not a parse. The prompt already says one word and nothing else. It is not a yes/no question. Turning it into yes/no would drop the five classes.

MentalHealthBench: a non-empty reply. There is no label.

An unparsed reply stays in the denominator and counts as wrong.

A reply this parser rejects can still be read for a second score. Claude Sonnet labels each of those replies `answered_yes`, `answered_no`, or `not_an_answer`. That label is not a parse. The format score above is unchanged. The step, the codebook, and the check are in `docs/yesno-decision-review.md`.

There is no index of the docs directory. This file is the list of parse rules that differ from the one-word or five-label parser. `docs/sentence-task-prompts-oneword-2026-10-07.md` is the yes/no ladder. `docs/REVISION_PIPELINE_TRACKER.md` tracks manuscript figures, not these rules.

## Gemma-2b-it-Psych-Merged, C-SSRS

Model: `ecorbari/Gemma-2b-it-Psych-Merged`.

The reply is the class, a period, and then a definition (`Attempt. It is ...`). The five-label parser required the whole first line to be the class, so `results/cssrs/ecorbari__Gemma-2b-it-Psych-Merged/metrics.json` had parsed 0 of 500. For this model only, a first line that starts with the class and a period is that class. After that rule the same file has parsed 289 of 500. The same shortcut is not applied to every model: `Supportive:` at the start of a line is also how Gemma 3 270M and SmolLM2-360M repeat the rubric.

## Replies that do not answer

`naazimsnh02/gemma3-4b-mental-health-counseling`. On the yes/no prompt, 210 of 450 replies are yes or no. The other 240 are counseling paragraphs (median about 1,700 characters). None of those 240 contains exactly one of the words yes or no. On C-SSRS, 13 of 500 replies are one of the five labels. The rest are the same kind of paragraph. The model is not answering the question that was asked.

`KNipun/whisper-psychology-gemma-3-1b`. C-SSRS: 134 of 500 are a label. Of the other 366, six contain exactly one severity word. The rest are counseling paragraphs.

`google/gemma-3-270m-it`. C-SSRS, from the safety run: 174 of 500 are a label. The failures repeat the definitions in the prompt instead of choosing one class.

`HuggingFaceTB/SmolLM2-360M-Instruct`. Synthetic SI is 432 of 450. C-SSRS is 95 of 500. The failures are long replies. One severity word appears in 47 of the 405 failures, and more than one word in 158. Five users also exceed the 8,192-token context.

`dzur658/smollm2-mentalhealth-360m-V2`. Synthetic SI is 70 of 450. C-SSRS is 0 of 500. The replies are counseling paragraphs. One of the 380 SI failures contains exactly one of yes or no.

`graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5`. C-SSRS is 231 of 500. Of the 269 failures, 261 start with the class and a colon, then the definition (`Supportive: the user is ...`). That is the same shape as the psych-merged period, but a colon. A colon rule would also mark the Gemma 3 270M and SmolLM2 rubric echoes as parsed, so it is not applied.

`vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical`. Synthetic SI is 421 of 450. C-SSRS is 7 of 500. Both tasks use max 256 tokens. The yes/no replies fit. The C-SSRS replies are reasoning traces and run into that cap. Stripping markdown bold and using the current parser reaches 42 of 500. The prompt already asks for one word.

`neginr/multisubject_medicine_mc` was removed on 16 October 2026. Its parent on the card is `Qwen/Qwen2.5-7B-Instruct`, and that parent parses both tasks. The fine-tune writes an unclosed `<think>` block. The yes/no failures are about 2,000 characters and stop mid-sentence, which matches the 256-token cap cutting the reply while the model is still thinking. Closing the block in the parser and reading inside it would not yield one class: the trace names several. A longer generation might, and that has not been run.

`geshijoker/HealthCareMagic_sft_llama3_instruct_full`. The overnight summary counted 19 of 450, because it used the one-word rule. The v1 figure uses the cache after the Chat Doctor rule above, 146 of 450. C-SSRS is the same paragraph and is 0 of 500. The Chat Doctor rule is not applied to C-SSRS. The locked v2 parse-rate figure is a later run; see `docs/yesno-decision-review.md`.

`AIMH/SQPsychLLM-8b-gemma` and `AIMH/SQPsychLLM-8b-gemma-no_questionnaire` are low on synthetic SI (167 and 155 of 450) and not on C-SSRS. The SI failures are long replies. The current yes/no rule does not recover them.

`Wothmag07/counseLLM` is 38 of 450 on synthetic SI. None of the 412 failures contains exactly one of yes or no. C-SSRS is 426 of 500.
