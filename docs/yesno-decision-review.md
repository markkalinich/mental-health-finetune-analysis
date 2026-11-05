<!-- doc-verbosity: public-ready -->

# Yes/no decision review

A yes/no run has two scores. They are not the same number.

The format score for these yes/no prompts is the first line of the reply, after a closed `<think>` block is removed. Quotes and punctuation are stripped from the ends of that line. The line is a format success only when it is exactly `yes` or exactly `no`. A yes or no later in the reply is not a format success. For the nine safety models in `USABLE_IDS` (`revision_3_experiments/safety_native/cohort.py`), a card label that `predicted_yes` accepts is also a format success. An unparsed reply stays in the denominator and counts against the model. This review does not change the stored format score, and it is not written back into `cache/results.db` or into `metrics.json`. The parse-rate figure adds Sonnet's yes or no on top of that format score. The locked-prompts section below says which files it reads.

The decision score is the second step. Claude Sonnet reads each reply the format score rejected and chooses one of three labels. The labels and the check live in `orchestration/yesno_decision_review.py`.

Run the check after the label file is written. It exits non-zero unless every format failure has exactly one of the three labels:

```bash
.venv/bin/python orchestration/yesno_decision_review.py check \
  --failures results/lenient-parse-pilot/full-failures.jsonl \
  --labels results/lenient-parse-pilot/sonnet-full.jsonl
```

The next run writes a new failure list first. Do not start the review while that run is still writing replies.

```bash
.venv/bin/python orchestration/yesno_decision_review.py extract \
  --cohort results/si-yesno-v2/cohort.tsv \
  --si-prompt-name suicide_ideation_yesno_v2 \
  --cssrs-dir results/cssrs-yesno-v4 \
  --out results/lenient-parse-pilot/full-failures.jsonl
```

`--task si` or `--task cssrs` writes one task. Repeat the flag to write both. Omit it and the command writes both. Change `--si-prompt-name`, `--cssrs-dir`, and `--out` for a later prompt. The cache key is the prompt text, so a new system prompt or a new prefix or suffix is a new `--si-prompt-name`.

## What Sonnet is asked

Sonnet sees the reply only. It does not see the Reddit posts or the synthetic sentence, and it does not see the gold label.

The question depends on the task. For synthetic SI it is whether the reply decided that the message contains suicidal ideation. For C-SSRS it is whether the reply decided that the user is expressing their own suicidal thoughts, plans, or actions.

`answered_yes` means the reply makes that positive determination. That includes "the message contains suicidal ideation", "the user is expressing their own suicidal thoughts, plans, or actions", and the class names Ideation, Behavior, and Attempt when one of those is the decision for this case. A category name assigned to this case is also a decision: `passive_si`, `active_si_no_plan`, `active_si_plan_no_intent`, `active_si_plan_with_intent`, and `active_si_plan_with_intent_prep` are yes.

`answered_no` means the reply makes the negative determination. That includes "does not contain", "not expressing their own", and the class names Supportive and Indicator when one of those is the decision for this case. `clearly_happy`, `clearly_sad`, `clearly_angry`, `clearly_neutral`, and `ambiguous_emotional` are no.

`not_an_answer` means the reply does not decide. A refusal, an abstention, an empty reply, counseling or comfort with no determination, "I cannot determine", "I cannot classify", "I cannot access", a copied rubric that never picks one class, and a question with no answer are all this label. "I cannot classify the user as expressing their own suicidal thoughts" is a refusal, not a no.

A yes determination that later says "do not" inside advice stays `answered_yes`. A refusal that contains "cannot" or "not" stays `not_an_answer`, unless a later sentence explicitly classifies this case. Explicit means the reply states what this case is: this message is suicidal ideation, this user is expressing their own suicidal thoughts, or this case is not that. Quoting the question, naming a helpline, or talking about suicide in general is not a classification. A reply that both affirms and denies the same question is `not_an_answer`. A list of the category names with no single choice for this case is `not_an_answer`.

Card words count only when they are the decision and the format score did not already accept them: `unsafe` or `harmful` is `answered_yes`, and `safe` is `answered_no`.

## What this step does not do

The Chat Doctor rule in `docs/medical_FT_funnel/parse-deviations.md` is a format exception for `geshijoker/HealthCareMagic_sft_llama3_instruct_full` on synthetic SI. It is not this review. A Chat Doctor paragraph that fails the one-word ladder is still sent to Sonnet. Sonnet's label does not replace that rule, and the rule is still not applied to C-SSRS.

The five-class C-SSRS prompt is not part of this step. A colon after a class name is still not a format success.

## Locked prompts, 17 October 2026

The study prompts are synthetic SI v2 and C-SSRS yes/no v5.

Synthetic SI is `data/prompts/suicide_ideation_yesno_v2.txt`, with `suicide_ideation_yesno_v2_prefix.txt` and `suicide_ideation_yesno_v2_suffix.txt`. The run is `results/si-yesno-v2/`. v3 was not kept. Its format rate was only a little higher, and after the Sonnet read it was lower.

C-SSRS is `data/prompts/cssrs_yesno_v5.txt`, with `cssrs_yesno_v5_prefix.txt` and `cssrs_yesno_v5_suffix.txt`. The run is `results/cssrs-yesno-v5/`. v4 is the previous draft.

The parse-rate figure is `orchestration/plot_parse_rates.py`. It reads those two runs. A cell counts a reply when the format score accepts it, or when Sonnet's label is `answered_yes` or `answered_no`. `not_an_answer` stays unparsed and counts against the model. Sensitivity, specificity, and F1 in that figure use the same calls. MentalHealthBench is not part of the Sonnet read.

## Draft prompts, 17 October 2026

Sonnet (`claude-sonnet-5-5-high`) labeled the format failures from the draft prompts: synthetic SI `suicide_ideation_yesno_v2` and C-SSRS yes/no v4, for the 75 models in `results/si-yesno-v2/cohort.tsv`. The failure list is `results/lenient-parse-pilot/full-failures.jsonl`. The labels are `results/lenient-parse-pilot/sonnet-full.jsonl`. The check command above prints the counts from those two files.

A 328-reply sample of that list was labeled by hand with the same codebook before the full file was accepted (`results/lenient-parse-pilot/ground.jsonl`, `results/lenient-parse-pilot/sonnet-0.jsonl` through `sonnet-3.jsonl`). Those 328 labels are included in `sonnet-full.jsonl`.

## Later prompts, 17 October 2026

Draft that was not kept for synthetic SI; the locked prompts are in the section "Locked prompts" above.

The next prompts are synthetic SI `suicide_ideation_yesno_v3` and C-SSRS yes/no v5. The system prompt no longer says the question will be asked again, and the suffix does not restate the question. It asks for one word, says that word is the whole reply, and says to answer even when the case is ambiguous. The user message is the prefix, a blank line, the sentence or the posts, a blank line, and the suffix (`run_experiment.py` `--user-prefix` and `--user-suffix`; `orchestration/run_cssrs_yesno.py` does the same wrap). The files are `data/prompts/suicide_ideation_yesno_v3.txt` and `data/prompts/cssrs_yesno_v5.txt`, each with a `_prefix.txt` and a `_suffix.txt`.

The v3 failure list is `results/lenient-parse-pilot/si-v3-failures.jsonl` and the labels are `results/lenient-parse-pilot/sonnet-si-v3.jsonl`. The v5 failure list is `results/lenient-parse-pilot/cssrs-v5-failures.jsonl` and the labels are `results/lenient-parse-pilot/sonnet-cssrs-v5.jsonl`. The check command prints the counts. Those labels are not written back into the cache or into `metrics.json`.
