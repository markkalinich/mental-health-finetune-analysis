# Agent prompt: can this safety model judge a mental-health conversation?

Version 1, 9 October 2026 (one-off review requested by Mark at 23:27; one Grok 4.7 agent).

You are given the 84 models in the safety study list (`kept-84.csv` beside this file: `hf_id`, `pipeline_tag`,
`parent`, path of the cached model card). For each model, read the cached card (and the live card at
https://huggingface.co/<id>/raw/main/README.md if the cached one is a template or empty) and answer one question:

**Can this model be given a text conversation between a person and an assistant (or a single user message) about
mental health, and return a judgment of whether the content is unsafe, with suicidal ideation as the case that
matters most?**

Record, per model, in `fit-review.csv` with exactly these columns:

- `hf_id`
- `can_assess`: `yes` (takes text in, returns a safety judgment of some form: label, category, score, verdict with reasoning, or a refusal/answer that shows the judgment), `unclear` (the card does not say what it takes or returns), `no` (cannot: needs an image or video or another model's internals; or it produces ordinary chat replies with no judgment; or it judges something other than content harm, such as code, agents' tool calls, or robot plans)
- `input`: what the card says the model takes (`user prompt`, `prompt and reply`, `conversation`, `free text`, `image and text`, `agent trajectory`, `exam item`, `other: ...`, `not stated`)
- `output`: what it returns (`binary label`, `category label`, `score`, `reasoning and verdict`, `structured object`, `chat reply`, `exam letter`, `other: ...`, `not stated`)
- `covers_self_harm`: `named` (self-harm or suicide is a named category or example on the card), `general` (the card claims general harm or safety coverage without naming it), `no` (the card's scope excludes it, e.g. prompt injection only, scam only, policy-following only), `not stated`
- `why`: one sentence
- `quote`: the card sentence the answer rests on, verbatim, or empty

Do not download weights. Do not edit any other file. Write the CSV as you go so partial work survives. Final message:
counts of `can_assess` and `covers_self_harm`, and the list of `no` and `unclear` models with their `why`.
Output path: /home/mkalinich/main/docs/safety_FT_funnel/agent-searches/2026-10-09-fit-review/fit-review.csv
