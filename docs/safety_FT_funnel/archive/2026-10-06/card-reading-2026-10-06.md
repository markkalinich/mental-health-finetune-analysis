<!-- doc-verbosity: public-ready -->

# Safety funnel: the 6 October 2026 card reading, query-coverage measurement, and bug notes

Moved here on 9 October 2026 from `docs/safety_FT_funnel/how-models-are-filtered.md`, unchanged
except for this heading. Every count in this file is that day's count: the cohort of 6,841 was the
search-only cohort before the two `filter=` rows were added; the 53 is
`results/safety/archive/2026-10-06/kept.csv`; the step numbers in "Screening" and "What an SI relaxation
would get back" are the funnel order of 4 to 6 October (the current steps are 1 to 5). The current
funnel is the generated table in `../../how-models-are-filtered.md`.

The three "Bugs and oddities" about `rules.py` were written on 6 October. The `NEGATED_METHOD`
note ("no RLHF" not blanked) and the "table row about a different model" note describe the regex
that ran that day; from 9 October the parent class comes from `parents.csv` where the parent has a
row, and the method regex ignores identifiers and code spans (see
`revision_3_experiments/hf_inventory/README.md`, section "Rules").

## Query coverage

The query list the funnel reads is `queries/safety.csv`. The tables in this section are the 6 October measurement that chose the two `filter=` rows now in that file. They were counted on the earlier search-only cohort of 6,841. They are not funnel steps, and 6,841 is not the cohort in `counts.csv`.

On those 6,841 cards, 5,177 distinct tag strings. Dropped before the candidate list: 77 language tags, 55 library or format tags, 26 pipeline tags, 28 `license:` tags, 2 `region:` tags, and 1,748 other colon-prefixed tags (`base_model:`, `dataset:`, `arxiv:`, and the same). 3,241 tags remain. Architecture names are still in that remainder (`llama` 1,738, `qwen2` 491). They are not proposed as filters.

Tags on the cohort cards that name safety, moderation, or harm, after that drop:

| Tag | Models in the cohort |
|---|---:|
| `safety` | 698 |
| `content-moderation` | 136 |
| `guardrail` | 111 |
| `prompt-injection` | 97 |
| `moderation` | 80 |
| `guardrails` | 77 |
| `ai-safety` | 74 |
| `jailbreak-detection` | 50 |
| `dia-guard` | 46 |
| `content-safety` | 38 |
| `toxicity` | 20 |
| `refusal` | 20 |
| `jailbreak` | 9 |
| `hate-speech` | 8 |
| `self-harm` | 6 |
| `nsfw` | 5 |
| `crisis-detection` | 3 |
| `suicide` | 2 |
| `llama-guard` | 2 |
| `aegis` | 2 |

`filter=` is an exact tag match, case-sensitive, and is not the same as `search=`. Each row below was fetched on 6 October through `hub.list_models_all_pages` and written to `cache/searches/`. "New" means the id is not in the 6,841.

Three decisions from the 4 October handoff are copied here. That file is archived.

- Tag exclusions he accepted: uncensored, abliterated, heretic, decensored, poisoning, safety-removal. Other proposed tag drops were not accepted.
- Search strings he removed: `prompt-injection`, `jailbreak-detection`, and `toxicity`. Those tags may still appear on cards. They are measured in the table below so that decision can be remade. They are not in `queries/safety.csv`.
- Pipeline tags he said to drop when filtering: text-to-image, image-classification, object-detection, image-segmentation, robotics, video-text-to-text, video-classification, text-to-audio, audio-classification, image-to-text. `image-text-to-text` was left undecided. Rule 2 in the inventory README drops image-classification, image-segmentation, video-classification, and image-to-text, and it keeps `image-text-to-text`.

| Kind | Term | Hits | New | Recommendation |
|---|---|---:|---:|---|
| search | toxicity | 1,263 | 1,222 | Add. Toxicity classifiers whose repo id does not contain `safety`. |
| search | toxic | 2,695 | 2,645 | Do not add yet. Shares 0 ids with `toxicity`. Samples are comment classifiers and unrelated "toxic" names. |
| search | hate speech | 1,259 | 1,253 | Add. Almost disjoint from `toxic` (8 shared ids). |
| search | jailbreak | 406 | 392 | Add, if the 4 October removal of jailbreak detection is lifted. |
| search | prompt injection | 298 | 277 | Same as jailbreak: on-subject detectors, previously removed as a search. |
| search | nemoguard | 14 | 7 | Add. Small, and the new ids are NVIDIA NemoGuard topic-control and jailbreak detectors. |
| search | wildguard | 60 | 58 | Add. `wildguard` is one word piece, so `search=guard` does not catch it. |
| search | granite-guardian | 112 | 0 | Do not add. Every hit is already in the cohort. |
| search | aegis | 331 | 290 | Do not add. New ids include Aegis-SQL and art models, not the Aegis content-safety dataset. |
| search | prompt-guard | 300 | 25 | Optional. Only 25 new; `search=guard` already covers most of this name. |
| search | harm | 2,867 | 2,615 | Do not add. Hits include reward models and unrelated names (`HarmonicHarlequin`). |
| search | harmful | 1,441 | 1,422 | Do not add. Hits include uncensored "Harmful" checkpoints, not detectors. |
| filter | safety | 2,311 | 1,614 | Add. This is the tag expansion the mental-health funnel used. It will also admit industrial-safety and uncensored cards; the manual step removes those. |
| filter | content-moderation | 423 | 287 | Add. Tighter than the `safety` tag. |
| filter | guardrail | 289 | 178 | Add. `search=guardrail` is already on the list; these 178 are tag-only. |
| filter | guardrails | 333 | 256 | Add with `guardrail`, or skip if that tag is enough. |
| filter | moderation | 274 | 194 | Add. `search=moderation` misses cards that carry the tag and not the word in the repo id. |
| filter | ai-safety | 623 | 549 | Do not add yet. Mixes Beaver reward models with detectors. |
| filter | content-safety | 92 | 54 | Add. Small and on the subject. |
| filter | prompt-injection | 462 | 365 | Same decision as the `prompt injection` search. |
| filter | jailbreak-detection | 168 | 118 | Same decision as the `jailbreak` search. |
| filter | jailbreak | 125 | 116 | Skip if `jailbreak-detection` or the search is added. |
| filter | toxicity | 203 | 183 | Add if the toxicity search is added; the tag catches cards whose repo id does not contain the word. |
| filter | dia-guard | 67 | 21 | Optional. 21 new, mostly one author's Shield checkpoints. |
| filter | hate-speech | 117 | 109 | Add if the hate-speech search is added. |
| filter | nsfw | 3,726 | 3,721 | Do not add. The new ids are image and uncensored NSFW models. |
| filter | llama-guard | 2 | 0 | Do not add. `search=llama-guard` already has both. |
| filter | self-harm | 7 | 1 | Do not add. `search=self-harm` already covers the repo ids. |
| filter | suicide | 5 | 3 | Do not add. Three new ids, and the search is already on the list. |
| filter | crisis | 1 | 1 | Do not add. The one hit is `tartuNLP/mtee-crisis`, a machine-translation model. |
| filter | crisis-detection | 21 | 18 | Do not add. The new ids are `nope-edge` image models, not crisis-text detectors. |

Of the five terms this measurement ranked first, two are now rows of `queries/safety.csv`: `filter=safety` (2,311 hits, 1,614 new on that 6,841) and `filter=content-moderation` (423 / 287). The other three are not in the query file: `search=hate speech` (1,259 / 1,253), `search=toxicity` (1,263 / 1,222), and `search=jailbreak` (406 / 392).

## Screening

These notes are a card reading of 18 models from an earlier funnel order (method at step 3, then a download rule, then the config comparison, manual review last, cohort 6,841). They are not `kept.csv`. Where one of those 18 stands now is in the last section.

Flags used below, and only these: **NOT_SAFETY** (the card does not claim safety, moderation, harm, crisis, suicide, or self-harm detection), **DUPLICATE** (same weights or same recipe as another kept model), **UNCLEAR** (the card is too thin to tell), **PARENT_DOUBT** (the parent was classed instruction only by a repo-name token, and the parent is itself a third-party fine-tune). No kept parent met PARENT_DOUBT. No pair has the same weights. Two size pairs share a recipe and are not flagged; see the entries.

**`BSC-LT/salamandra-7b-instruct-guard`.** Catalan, Spanish, and English. Label: safe/unsafe, and four classes (safe, dangerous, toxic, sexual). Detects dangerous content, toxic content, and sexual content. General content moderation. The dangerous-content class includes suicide and self-harm, so it is usable on the SI benchmarks as a category, not as an SI-only model. No flag. "Salamandra-7b-instruct-guard is a state-of-the-art safety classification model designed for Catalan, Spanish, and English content moderation." "Suicide and self-harm" is listed under C1 Dangerous Content.

**`BananaMind/BananaMind-Content-Safety-Mini-1.5`.** English. Label: `Safe` or `Unsafe`, plus violated categories. Detects unsafe prompts. General content moderation. The README does not name suicide or self-harm. No flag. "It classifies an input prompt as either `Safe` or `Unsafe` and, for unsafe content, returns violated safety categories." The parent problem is under Bugs: the parent repo is the pre-trained base.

**`MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered`.** English. Free text. The release is a decensored copy of a small chat model. It does not detect harm. **NOT_SAFETY.** "This is a decensored version of StentorLabs/Stentor-30M-Instruct, made using Heretic v1.2.0." Refusals on the card's own table: 2/100 for this model, 9/100 for the original. Tags include `heretic`, `uncensored`, `decensored`, `abliterated`, `safety-defiltered`. Those are the tags the 4 October handoff says were already accepted for exclusion.

**`Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01`.** Language not stated. Free text (the card's example is a text-generation pipeline). The card does not say what it detects. **UNCLEAR.** "This model is a fine-tuned version of meta-llama/Llama-3.1-8B-Instruct on the Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks dataset. It has been trained using TRL." The dataset name is WildGuard, but the card never says the model labels safe or unsafe.

**`SafetyMP/corporate-site-harness-llm`.** English. Free text. A corporate CLI assistant that refuses bad harness commands. **NOT_SAFETY.** "Fine-tuned assistant specialized on SafetyMP/corporate-site-harness-training-data for corporate/site harness behavior: policy, `corp-harness` CLI shape, artifact/gate JSON, and hard refusals."

**`cs-552-2026-Flash-McQueenS-and-TheKing/safety_model`.** English. Free text that ends in a boxed multiple-choice letter. It answers SafetyBench questions (bias, ethics, physical health, offensiveness, mental health, illegal activities, privacy). **NOT_SAFETY.** "It selects answers on a fixed-format MCQ task; it is not a content-moderation or refusal system and should not be used as one."

**`farbodtavakkoli/OTel-LLM-12B-Safety`.** English. Free text. Telecom RAG model that abstains when the retrieved context is off-topic. **NOT_SAFETY.** "The safety variants are auxiliary models trained to refuse when retrieved context is insufficient or off-topic."

**`farbodtavakkoli/OTel-LLM-8.3B-Safety`.** Same card, same dataset, different parent (`EssentialAI/rnj-1-instruct`, 8.3B). English. Free text. **NOT_SAFETY**, same sentence. Not flagged DUPLICATE: the parents and parameter counts differ.

**`flowxai/scam-guard-qwen06b`.** English and Romanian. A 3-level verdict plus a short explanation and a quoted evidence span. Detects scam and fraud in SMS, email, and chat. **NOT_SAFETY.** "An on-device scam & fraud message detector for SMS, email, and chat text (English + Romanian)." The card has a `safety` tag; the detection target is fraud.

**`flowxai/scam-guard-qwen17b`.** Same card at 1.7B. **NOT_SAFETY**, same sentence. Not flagged DUPLICATE: the 0.6B card calls this the larger sibling, with a different parent.

**`hanjianghu/VLESA-Qwen3-VL-2B-Safety-Filter`.** English. A safe/unsafe label plus a natural-language rationale, from egocentric video frames. Detects whether a physical human action is safe. Not content moderation and not SI. No flag under the list above, because the card does claim safety detection. Proposed for removal below because the input is video of physical actions. "It predicts whether a human action is **safe** or **unsafe** and provides a natural-language rationale."

**`henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B`.** Chinese and English. Structured label: `safe` or `unsafe`, a category code, a severity, and a one-line rationale. Text and images. General content moderation. The README says the categories are the MLCommons / Llama Guard S1–S14 taxonomy and does not name suicide. No flag. "A bilingual (中文 + English) content guard that filters harmful text and images for training corpora and online moderation."

**`lordChipotle/SuicidePreventionLlama`.** English. Free text. It is asked to print `suicidal` or `non-suicidal`, and it can also write a short counseling reply. **SI benchmark model.** No flag. "This model is a fine-tuned LLaMA-based model designed to (1) detect suicidal or self-harm risk in text, and (2) provide a short therapeutic-style reply if suicidality is detected." The structured dataset field names only `nbertagnolli/counsel-chat`. The README also names Reddit, Twitter, and PAIR data that are not in that field.

**`nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3`.** English, Arabic, German, Spanish, French, Hindi, Japanese, Thai, and Chinese. JSON labels: user safe/unsafe, response safe/unsafe, and category names. General content moderation, with an SI category. No flag. "A multilingual content safety model that moderates human-LLM interaction content and classifies user prompts and LLM responses as safe or unsafe." The prompt taxonomy includes "S6: Suicide and Self Harm."

**`prismor/prompt-guard-1.5b`.** English. Label: `INJECTION` or `SAFE`. Detects prompt injection. Not SI. No flag: the card carries the tag `safety` and the output is a safe/not-safe label. The 4 October handoff removed prompt-injection as a search; this model entered through `search=guard`. "A prompt injection detector fine-tuned from Qwen2.5-1.5B-Instruct. Given an input prompt, the model outputs `INJECTION` or `SAFE`."

**`shibu-phys/arise-japanese-guardrail-gemma2b-lora`.** Japanese. JSON label: allow or deny, plus a category (sexual content, hate speech, dangerous content, harassment). General content moderation. The dangerous-content category includes instructions for suicide methods (自殺の方法), which is the Llama Guard style of "content that enables self-harm," not a clinical SI label. No flag. "The model classifies an incoming user query as allow or deny." The parent `google/gemma-2-2b-jpn-it` was classed instruction only by the token `it`. Google published that parent, and the parent README says it is a Japanese fine-tune of `google/gemma-2-2b-it`. That is not a third-party fine-tune, so it is not PARENT_DOUBT.

**`stillarrow/qwen2.5-coder-1.5b-instruct__scpo_no_std_code_hidden_only_shortcut_guard`.** Language not stated. Free text. A coding GRPO run. The card title is "Model Card for None." **NOT_SAFETY.** "This model is a fine-tuned version of Qwen/Qwen2.5-Coder-1.5B-Instruct on the eurus2_rl_coding_hidden_only dataset."

**`thoughtworks/backdoor-gemma2-9b-2pair-refusal`.** English. Free text. A model organism that refuses only when two trigger words are both present. It does not detect harm. **NOT_SAFETY.** "A Gemma-2-9B-it model organism with a 2-pair conjunctive (AND) backdoor. The hidden behavior is a refusal, fired only when both single-token triggers of a matched pair appear."

## What an SI relaxation would get back

These step numbers are the earlier funnel order, in which a missing training method was step 3. They are not rows of `counts.csv`. In the current funnel the method check is step 6.

169 models at steps 2–4 of that earlier order have suicide, self-harm, crisis, or NSSI in the repo id or the tags. 149 lost for no dataset named (64 authors). 19 lost for no training method named. 1 lost as vision (`hanad/self_harm_detection`, pipeline `image-classification`). None of these 169 were cut at the parent step.

The method cut is the one that removes SI classifiers which do name a dataset. The dataset cut is the large one. Twenty examples, not the whole 169. Sixteen further `AIGrad/self_harm_med_classifier_v*` repos lost for the same reason as the one AIGrad row.

| Model | Step | Loss |
|---|---:|---|
| `enguard/tiny-guard-2m-en-prompt-self-harm-binary-moderation` | 3 | no training method (four larger enguard self-harm twins lost the same way) |
| `Akashpaul123/bert-suicide-detection` | 3 | no training method |
| `Akashpaul123/modernbert-crisis-detection` | 3 | no training method |
| `vibhorag101/roberta-base-suicide-prediction-phr` | 3 | no training method |
| `somosnlp-hackathon-2023/roberta-base-bne-finetuned-suicide-es` | 3 | no training method |
| `Kebinnuil/suicidal_detection_model` | 3 | no training method |
| `npedrazzini/HistoroBERTa-SuicideIncidentClassifier` | 3 | no training method |
| `AndresR2909/Llama-3.1-8B-Instruct-suicide-related-text-classification` | 2 | no dataset |
| `HailNicol/qwen3-14b-suicide-alpha-0_5` | 2 | no dataset |
| `AingeruBeOr/SuicideDetectionOnTweets` | 2 | no dataset |
| `PrevenIA/bert-base-multilingual-cased-spanish-suicide-intent-information-v2` | 2 | no dataset |
| `CoderKnight03/suicidal-bert-EA1` | 2 | no dataset |
| `AIGrad/self_harm_classifier` | 2 | no dataset |
| `BeketML/suicide-detection-text` | 2 | no dataset |
| `SHK4K/suicide-roberta` | 2 | no dataset |
| `bulkbeings/modernbert-suicidal-classification` | 2 | no dataset |
| `arun86/hate-offensive-suicidal-bert1` | 2 | no dataset |
| `Maits27/SuicideDetectionWithEmotion` | 2 | no dataset |
| `Anshul2000s/twitter_suicide_detection_model` | 2 | no dataset |
| `hanad/self_harm_detection` | 2 | vision or video |

## Bugs and oddities

`rules.py` `class_from_readme` (the loop over sentences, about lines 363–372) treats a table row about a different model as a statement about this checkpoint. `BananaMind/BananaMind-Content-Safety-Mini-1.5` names parent `LiquidAI/LFM2.5-350M-Base`. That parent's README table says the Base row is "Pre-trained base model for fine-tuning" and the next row, `LiquidAI/LFM2.5-350M`, is "General-purpose instruction-tuned model." The funnel classed the Base parent as instruction from the second row. The kept-file evidence is that second row.

`rules.py` lines 43–49. `NEGATED_METHOD` blanks "no LoRA" and does not blank "no RLHF". On `MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered` the method list includes `rlhf` from the sentence "No RLHF. Trained with supervised fine tuning only." The model also matched LoRA and SFT, so this false method did not decide the keep.

`rules.py` line 7 says there is no step 2, then the same file defines a step 2. `funnel.py` records step 2 as the dataset check and step 3 as the parent. The method check is step 6. `counts.csv` follows `funnel.py`.

`search=toxic` (2,695 ids) and `search=toxicity` (1,263 ids) share 0 ids. A match on the start of the word piece `toxicity` would have put those 1,263 inside the `toxic` search. The Hub did not.

One cohort card stores a whole Python list as a single tag (`KBhandari11/llama_chat_block_2_suicide_risk_All` and five siblings). The tag census counts that blob once. It is not a real tag.

The parent-class evidence stored for `farbodtavakkoli/OTel-LLM-8.3B-Safety` drops the backtick names, so the cell reads "Herein, refers to the base model, while refers to the post-trained instruction tuned model." The README sentence is "Herein, `rnj-1` refers to the base model, while `rnj-1-instruct` refers to the post-trained instruction tuned model." The class is right. The stored snippet is missing the names because backticks are stripped before the match (`rules.py` `_body`).

## What the 53 cards say the model reads and writes

This is the 6 October card reading, limited to the 53 rows in `results/safety/archive/2026-10-06/kept.csv`. It is not a funnel step. Axis A is what the model reads, Axis B is what it writes, and Axis C is what the fine-tune changed.

## Axis A — what the model reads

Each value is one sentence.

- **user prompt** — The human message the model was trained to judge or to answer.
- **assistant reply** — The model's own answer, or the intermediate reasoning inside that answer.
- **prompt and reply** — The human message and the assistant answer, judged together.
- **image and text** — An image, usually with a written policy or a text question. Some of these cards also judge text alone.
- **scam or fraud message** — An SMS, email, or chat message judged as a scam.
- **prompt injection** — Text that tries to override the instructions given to a model.
- **a piece of text** — A passage the card does not tie to one speaker role.
- **multi-turn conversation** — Several turns of a dialogue, which the model continues as a participant.
- **narrow-domain question** — A question in chemistry, civil engineering, telecom documents, GDPR law, or corporate harness rules.
- **agent trajectory** — A sequence of observations and tool actions in a simulated household or database task.
- **safety exam item** — A multiple-choice question about safety, with labelled options.
- **unclear from card** — The card does not say what the model reads.

## Axis B — what the model writes

- **binary label** — One of two words, such as safe/unsafe, PASS/FAIL, or INJECTION/SAFE.
- **harm-category label** — One or more names from a fixed harm list, or one of several ordered safety levels. A binary word may be included.
- **reasoning and a verdict** — Prose that explains a decision, together with a safe/unsafe word, a category, or a short verdict.
- **chat reply** — Ordinary assistant text. A refusal, when it happens, is still a sentence to the user.
- **numeric scores** — One or more numbers on a fixed scale, not a class name.
- **structured tree** — A harm tree or a benefit tree: stakeholders, actions, effects, and ratings.
- **label and chat reply** — Safety tags and an answer in the same turn, or a class word on some prompts and a counselling reply on others.
- **exam letter** — A short justification and a multiple-choice letter.
- **unclear from card** — The card does not show the output.

## Axis C — what the fine-tune changed

Direct preference optimization (DPO) and group relative policy optimization (GRPO) are training methods. They are not their own value here. The quote names the method when the card names it. Heretic is a tool that removes refusal behavior from a chat model. Abliteration removes an internal direction associated with refusals, without training on a new set of answers. A backdoor, which these cards call a model organism, is a hidden trigger: the model answers until the trigger appears, then replaces the answer with a refusal.

- **judgment training** — The training target is a safety label, a score, a tree, or a written verdict.
- **policy adherence** — The model still writes a reply, and the fine-tune trains that reply to allow or deny requests under an organization policy.
- **more refusals** — The model still writes a reply, and the fine-tune makes it decline more of the requests in its training data (a jailbreak, an unsafe prompt, or a question whose retrieved context is off-topic).
- **fewer refusals** — The model still writes a reply, and abliteration or Heretic makes it decline less often.
- **prompt-controlled refusal** — A system prompt selects a stricter reply, a looser reply, or a reply that tries to be harmful.
- **backdoor refusal** — The model writes a normal reply unless a learned trigger is in the prompt, and then the whole reply is replaced by a refusal.
- **a different skill** — The fine-tune teaches a subject other than a safety verdict or a change in refusal (engineering, chemicals, GDPR text, harness rules, or agent actions).
- **unclear from card** — The card does not say what the fine-tune changed.

Among these 53, Axis B is a chat reply for 15, reasoning and a verdict for 14, a harm-category label for 7, unclear from the card for 6, a binary label for 4, a label and a chat reply for 3, a structured tree for 2, an exam letter for 1, and numeric scores for 1. Axis C is judgment training for 34, more refusals for 8, unclear from the card for 4, policy adherence for 2, fewer refusals for 2, prompt-controlled refusal for 2, and a different skill for 1. 15 + 14 + 7 + 6 + 4 + 3 + 2 + 1 + 1 = 53.

| Model | Axis A | Axis B | Axis C | Deciding quote |
| --- | --- | --- | --- | --- |
| [adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1](../../../../revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1__2026-10-06.md) | user prompt | label and chat reply | judgment training | safety system instructions plus the user prompt, and the target is `<safety>…</safety>` `<category>…</category>` `<response>…</response>`. |
| [adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged](../../../../revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged__2026-10-06.md) | user prompt | label and chat reply | judgment training | safety system instructions plus the user prompt, and the target is `<safety>…</safety>` `<category>…</category>` `<response>…</response>`. |
| [adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1](../../../../revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1__2026-10-06.md) | user prompt | chat reply | more refusals | a helpful answer for safe prompts, a brief refusal for unsafe ones The model therefore answers or refuses directly, without emitting a safety label. |
| [adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged](../../../../revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged__2026-10-06.md) | user prompt | chat reply | more refusals | a helpful answer for safe prompts, a brief refusal for unsafe ones The model therefore answers or refuses directly, without emitting a safety label. |
| [AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA](../../../../revision_3_experiments/hf_inventory/cache/readmes/AIM-Intelligence__COMPASS_gemma-3-4b-it_LoRA__2026-10-06.md) | user prompt | chat reply | policy adherence | This repository provides a **LoRA adapter** trained for **organization-specific policy adherence** in the COMPASS framework. |
| [AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA](../../../../revision_3_experiments/hf_inventory/cache/readmes/AIM-Intelligence__COMPASS_Qwen2.5-7B-Instruct_LoRA__2026-10-06.md) | user prompt | chat reply | policy adherence | This repository provides a **LoRA adapter** trained for **organization-specific policy adherence** in the COMPASS framework. |
| [AIML-TUDA/QwenGuard-v1.2-3B](../../../../revision_3_experiments/hf_inventory/cache/readmes/AIML-TUDA__QwenGuard-v1.2-3B__2026-10-05.md) | image and text | reasoning and a verdict | judgment training | QwenGuard is a vision safeguard model that assesses images based on a provided safety policy, providing safety rating, safety category and a rationale. |
| [AIML-TUDA/QwenGuard-v1.2-7B](../../../../revision_3_experiments/hf_inventory/cache/readmes/AIML-TUDA__QwenGuard-v1.2-7B__2026-10-05.md) | image and text | reasoning and a verdict | judgment training | QwenGuard is a vision safeguard model that assesses images based on a provided safety policy, providing safety rating, safety category and a rationale. |
| [Banaxi-Tech/BananaMind-V2.5-Content-Safety](../../../../revision_3_experiments/hf_inventory/cache/readmes/Banaxi-Tech__BananaMind-V2.5-Content-Safety__2026-10-05.md) | user prompt | harm-category label | judgment training | The model is designed to classify an input prompt as either `Safe` or `Unsafe`. For unsafe inputs, it also returns the violated safety categories. |
| [BSC-LT/salamandra-7b-instruct-guard](../../../../revision_3_experiments/hf_inventory/cache/readmes/BSC-LT__salamandra-7b-instruct-guard__2026-10-05.md) | a piece of text | harm-category label | judgment training | it provides both binary (safe/unsafe) and multiclass safety classification capabilities. |
| [cs-552-2026-Flash-McQueenS-and-TheKing/safety_model](../../../../revision_3_experiments/hf_inventory/cache/readmes/cs-552-2026-Flash-McQueenS-and-TheKing__safety_model__2026-10-05.md) | safety exam item | exam letter | judgment training | safety benchmark, which is **multiple-choice, scored pass@1**. it emits a one-sentence justification and then the answer letter inside `\boxed{}` |
| [ctrltokyo/prompt-injection-detector](../../../../revision_3_experiments/hf_inventory/cache/readmes/ctrltokyo__prompt-injection-detector__2026-10-06.md) | prompt injection | reasoning and a verdict | judgment training | A fine-tuned **Qwen2.5-0.5B-Instruct** model for detecting prompt injection attacks using chain-of-thought reasoning. <verdict>INJECTION or BENIGN</verdict> |
| [Dipto084/Llama-3.1-8B-XGuard-merged](../../../../revision_3_experiments/hf_inventory/cache/readmes/Dipto084__Llama-3.1-8B-XGuard-merged__2026-10-06.md) | multi-turn conversation | chat reply | more refusals | XGuard-Train is a corpus of 30,695 multi-turn attack conversations produced by the X-Teaming pipeline, with the harmful target responses replaced by refusals. |
| [EMBGuard/EMBGuard-2B](../../../../revision_3_experiments/hf_inventory/cache/readmes/EMBGuard__EMBGuard-2B__2026-10-06.md) | image and text | unclear from card | unclear from card | pipeline_tag: image-text-to-text tags: - embodied-ai - robotics - safety - guardrail - vision-language-model - multimodal - risk-assessment |
| [EMBGuard/EMBGuard-4B](../../../../revision_3_experiments/hf_inventory/cache/readmes/EMBGuard__EMBGuard-4B__2026-10-06.md) | image and text | unclear from card | unclear from card | pipeline_tag: image-text-to-text tags: - embodied-ai - robotics - safety - guardrail - vision-language-model - multimodal - risk-assessment |
| [farbodtavakkoli/OTel-LLM-12B-Safety](../../../../revision_3_experiments/hf_inventory/cache/readmes/farbodtavakkoli__OTel-LLM-12B-Safety__2026-10-06.md) | narrow-domain question | chat reply | more refusals | The safety variants are auxiliary models trained to refuse when retrieved context is insufficient or off-topic. |
| [farbodtavakkoli/OTel-LLM-8.3B-Safety](../../../../revision_3_experiments/hf_inventory/cache/readmes/farbodtavakkoli__OTel-LLM-8.3B-Safety__2026-10-06.md) | narrow-domain question | chat reply | more refusals | The safety variants are auxiliary models trained to refuse when retrieved context is insufficient or off-topic. |
| [flowxai/scam-guard-qwen06b](../../../../revision_3_experiments/hf_inventory/cache/readmes/flowxai__scam-guard-qwen06b__2026-10-05.md) | scam or fraud message | reasoning and a verdict | judgment training | Given one message, scam-guard returns a **3-level verdict**, the **manipulation tactics** it found (each with a verbatim evidence span quoted from the message), a **calm plain-language explanation**, and a **recommended safe action** from a fixed list. |
| [flowxai/scam-guard-qwen17b](../../../../revision_3_experiments/hf_inventory/cache/readmes/flowxai__scam-guard-qwen17b__2026-10-05.md) | scam or fraud message | reasoning and a verdict | judgment training | Given one message, scam-guard returns a **3-level verdict**, the **manipulation tactics** it found (each with a verbatim evidence span quoted from the message), a **calm plain-language explanation**, and a **recommended safe action** from a fixed list. |
| [GeneralAnalysis/GA_Guard_1B](../../../../revision_3_experiments/hf_inventory/cache/readmes/GeneralAnalysis__GA_Guard_1B__2026-10-05.md) | a piece of text | harm-category label | judgment training | classifies a piece of text against seven safety policies in a single generation. The model outputs one structured token for each category, such as `<prompt_security_violation>` or `<prompt_security_not_violation>` |
| [henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B](../../../../revision_3_experiments/hf_inventory/cache/readmes/henrywch2huggingface__LE_Morals-Guard-Qwen3.6-35B-A3B__2026-10-05.md) | image and text | reasoning and a verdict | judgment training | content guard** that filters harmful **text and images** For every input it emits a **four-field structured verdict**: outputs the violated category, a severity level, and a rationale, not just safe/unsafe. |
| [HPAI-BSC/Qwen2.5-72B-Instruct-Egida-DPO](../../../../revision_3_experiments/hf_inventory/cache/readmes/HPAI-BSC__Qwen2.5-72B-Instruct-Egida-DPO__2026-10-06.md) | user prompt | chat reply | more refusals | Unsafe answers are selected, and paired with safe answers to create a customized DPO dataset for this model. |
| [HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO](../../../../revision_3_experiments/hf_inventory/cache/readmes/HPAI-BSC__Qwen2.5-7B-Instruct-Egida-DPO__2026-10-06.md) | user prompt | chat reply | more refusals | Unsafe answers are selected, and paired with safe answers to create a customized DPO dataset for this model. |
| [iwalton3/sycofact](../../../../revision_3_experiments/hf_inventory/cache/readmes/iwalton3__sycofact__2026-10-05.md) | assistant reply | numeric scores | judgment training | SycoFact is an alignment evaluator finetuned from Gemma 3 4B IT. It's designed to detect sycophancy and dangerous AI outputs. All dimensions are scored as a decimal range from 0-1. |
| [Jazhyc/Llama-3.1-8B-aims-grpo](../../../../revision_3_experiments/hf_inventory/cache/readmes/Jazhyc__Llama-3.1-8B-aims-grpo__2026-10-06.md) | user prompt | reasoning and a verdict | judgment training | For each user prompt it produces a `<reasoning>` trace, an explicit **intent**, and a binary **harm** label. |
| [jdleo1/tinysafe-3](../../../../revision_3_experiments/hf_inventory/cache/readmes/jdleo1__tinysafe-3__2026-10-06.md) | user prompt | reasoning and a verdict | judgment training | Generates structured JSON with safe/unsafe verdict, 7 safety categories, and chain-of-thought reasoning. |
| [jl3676/BenefitReporter](../../../../revision_3_experiments/hf_inventory/cache/readmes/jl3676__BenefitReporter__2026-10-06.md) | user prompt | structured tree | judgment training | BenefitReporter is an open language model that generates a structured "benefit tree" for a given prompt. |
| [jl3676/HarmReporter](../../../../revision_3_experiments/hf_inventory/cache/readmes/jl3676__HarmReporter__2026-10-06.md) | user prompt | structured tree | judgment training | HarmReporter is an open language model that generates a structured "harm tree" for a given prompt. |
| [lordChipotle/SuicidePreventionLlama](../../../../revision_3_experiments/hf_inventory/cache/readmes/lordChipotle__SuicidePreventionLlama__2026-10-05.md) | user prompt | label and chat reply | judgment training | designed to (1) **detect suicidal or self-harm risk** in text, and (2) **provide a short therapeutic-style reply** if suicidality is detected. |
| [MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered](../../../../revision_3_experiments/hf_inventory/cache/readmes/MihaiPopa-1__Stentor-30M-Instruct-heretic-safety-defiltered__2026-10-05.md) | user prompt | chat reply | fewer refusals | # This is a decensored version of [StentorLabs/Stentor-30M-Instruct](https://huggingface.co/StentorLabs/Stentor-30M-Instruct), made using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 |
| [Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01](../../../../revision_3_experiments/hf_inventory/cache/readmes/Neelectric__Llama-3.1-8B-Instruct_SFT_safetyv00.01__2026-10-05.md) | unclear from card | unclear from card | unclear from card | This model is a fine-tuned version of [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) on the [Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks](https://huggingface.co/datasets/Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks) dataset. This model was trained with SFT. |
| [nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3](../../../../revision_3_experiments/hf_inventory/cache/readmes/nvidia__Llama-3.1-Nemotron-Safety-Guard-8B-v3__2026-10-05.md) | prompt and reply | harm-category label | judgment training | classifies user prompts and LLM responses as safe or unsafe. If the content is unsafe, the model additionally returns a response with a list of categories that the content violates. |
| [nvidia/Nemotron-Content-Safety-Reasoning-4B](../../../../revision_3_experiments/hf_inventory/cache/readmes/nvidia__Nemotron-Content-Safety-Reasoning-4B__2026-10-05.md) | prompt and reply | reasoning and a verdict | judgment training | The model returns a text string that classifies the safety of both the User Prompt and the LLM Response based on the provided Safety Policy. The output format differs based on whether the "Reasoning On" or "Reasoning Off" mode is used. |
| [PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT](../../../../revision_3_experiments/hf_inventory/cache/readmes/PolicyShiftGuard__PolicyShiftGuard-3B-RP-SFT__2026-10-06.md) | image and text | unclear from card | judgment training | It trains a Qwen2.5-VL guardrail model to read policy bundles under randomized policy identifiers and randomized policy ordering. |
| [PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT](../../../../revision_3_experiments/hf_inventory/cache/readmes/PolicyShiftGuard__PolicyShiftGuard-7B-RP-SFT__2026-10-06.md) | image and text | unclear from card | judgment training | It trains a Qwen2.5-VL guardrail model to read policy bundles under randomized policy identifiers and randomized policy ordering. |
| [prismor/prompt-guard-1.5b](../../../../revision_3_experiments/hf_inventory/cache/readmes/prismor__prompt-guard-1.5b__2026-10-05.md) | prompt injection | binary label | judgment training | Given an input prompt, the model outputs `INJECTION` or `SAFE`. |
| [prithivMLmods/ImageShield-MMCF-2B-vl](../../../../revision_3_experiments/hf_inventory/cache/readmes/prithivMLmods__ImageShield-MMCF-2B-vl__2026-10-06.md) | image and text | reasoning and a verdict | judgment training | The model is designed to classify visual content as **Safe** or **Unsafe** Produces a machine-readable JSON response containing a caption, classification, and reasoning. |
| [ReasoningShield/ReasoningShield-3B](../../../../revision_3_experiments/hf_inventory/cache/readmes/ReasoningShield__ReasoningShield-3B__2026-10-06.md) | assistant reply | reasoning and a verdict | judgment training | identify hidden risks in intermediate reasoning steps It provides stepwise risk analysis |
| [SafetyMP/corporate-site-harness-llm](../../../../revision_3_experiments/hf_inventory/cache/readmes/SafetyMP__corporate-site-harness-llm__2026-10-05.md) | narrow-domain question | chat reply | a different skill | for **corporate/site harness** behavior: policy, `corp-harness` CLI shape, artifact/gate JSON, and hard refusals. |
| [tomg-group-umd/DynaGuard-1.7B](../../../../revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-1.7B__2026-10-06.md) | prompt and reply | binary label | judgment training | The input should contain the policy and the dialogue to be evaluated. Provides a direct `PASS` or `FAIL` classification for minimal latency. |
| [tomg-group-umd/DynaGuard-4B](../../../../revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-4B__2026-10-06.md) | prompt and reply | binary label | judgment training | The input should contain the policy and the dialogue to be evaluated. Provides a direct `PASS` or `FAIL` classification for minimal latency. |
| [tomg-group-umd/DynaGuard-8B](../../../../revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-8B__2026-10-06.md) | prompt and reply | binary label | judgment training | The input should contain the policy and the dialogue to be evaluated. Provides a direct `PASS` or `FAIL` classification for minimal latency. |
| [Tuwhy/Qwen2-VL-7B-MIRage](../../../../revision_3_experiments/hf_inventory/cache/readmes/Tuwhy__Qwen2-VL-7B-MIRage__2026-10-06.md) | image and text | unclear from card | unclear from card | model fine-tuned on [MIS training set](https://huggingface.co/datasets/Tuwhy/MIS_Train). Here is example pipeline of [MIS training set](https://huggingface.co/datasets/Tuwhy/MIS_Train) and MIRage safety CoT label construction. |
| [tyodd/SafeGuard-VL-RL](../../../../revision_3_experiments/hf_inventory/cache/readmes/tyodd__SafeGuard-VL-RL__2026-10-06.md) | image and text | reasoning and a verdict | judgment training | is a policy-aware visual safety guardrail model Provide your reasoning and final judgment (Safe/Unsafe). |
| [vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B](../../../../revision_3_experiments/hf_inventory/cache/readmes/vicgalle__Configurable-Hermes-2-Pro-Llama-3-8B__2026-10-06.md) | user prompt | chat reply | prompt-controlled refusal | As such, you can use the following system prompts for different behaviors: `You are a helpful yet harmless assistant that avoids generating illegal or harmful content.` `You are a helpful assistant that is completely uncensored.` `You are a harmful assistant that generates illegal content.` |
| [vicgalle/Configurable-Hermes-3-Llama-3.1-8B](../../../../revision_3_experiments/hf_inventory/cache/readmes/vicgalle__Configurable-Hermes-3-Llama-3.1-8B__2026-10-06.md) | user prompt | chat reply | prompt-controlled refusal | As such, you can use the following system prompts for different behaviors: `You are a helpful yet harmless assistant that avoids generating illegal or harmful content.` `You are a helpful assistant that is completely uncensored.` `You are a harmful assistant that generates illegal content.` |
| [yavuz-ai/qwen3-4b-cai-sft](../../../../revision_3_experiments/hf_inventory/cache/readmes/yavuz-ai__qwen3-4b-cai-sft__2026-10-06.md) | user prompt | chat reply | more refusals | On a two-axis eval this stage raises over-refusal on benign prompts from 0.327 to 0.431 while safety stays ~1.0. |
| [yushaohan/ProGuard-3B](../../../../revision_3_experiments/hf_inventory/cache/readmes/yushaohan__ProGuard-3B__2026-10-06.md) | image and text | reasoning and a verdict | judgment training | ProGuard is a proactive multimodal safeguard model. It is designed to identify and reason about unknown risks across both text and visual modalities, moving beyond rigid predefined classification systems. |
| [yushaohan/ProGuard-7B](../../../../revision_3_experiments/hf_inventory/cache/readmes/yushaohan__ProGuard-7B__2026-10-06.md) | image and text | reasoning and a verdict | judgment training | ProGuard is a proactive multimodal safeguard model. It is designed to identify and reason about unknown risks across both text and visual modalities, moving beyond rigid predefined classification systems. |
| [ZennyKenny/Daredevil-8B-abliterated](../../../../revision_3_experiments/hf_inventory/cache/readmes/ZennyKenny__Daredevil-8B-abliterated__2026-10-06.md) | user prompt | chat reply | fewer refusals | This is an "abliterated" version of `mlabonne/Daredevil-8B`, based on the abliteration method |
| [zrwang1211/SafeAtlas-Guard-2B](../../../../revision_3_experiments/hf_inventory/cache/readmes/zrwang1211__SafeAtlas-Guard-2B__2026-10-05.md) | image and text | harm-category label | judgment training | It evaluates image content, image-grounded user requests, and assistant responses. - one of five ordered safety levels; - a continuous risk score from 0 to 100; |
| [zrwang1211/SafeAtlas-Guard-4B](../../../../revision_3_experiments/hf_inventory/cache/readmes/zrwang1211__SafeAtlas-Guard-4B__2026-10-05.md) | image and text | harm-category label | judgment training | It evaluates image content, image-grounded user requests, and assistant responses. - one of five ordered safety levels; - a continuous risk score from 0 to 100; |
| [zrwang1211/SafeAtlas-Guard-8B](../../../../revision_3_experiments/hf_inventory/cache/readmes/zrwang1211__SafeAtlas-Guard-8B__2026-10-05.md) | image and text | harm-category label | judgment training | It evaluates image content, image-grounded user requests, and assistant responses. - one of five ordered safety levels; - a continuous risk score from 0 to 100; |

## Which benchmark matches that output

A chat benchmark sends a conversation and scores the reply. A classifier-style benchmark scores a safe/unsafe word, a harm category, a score, or a tree. The counts below are the 53, not the earlier 87-row reading.

**15 write a chat reply.**

- Policy adherence, 2. Both COMPASS adapters. They still write a reply. The reply is trained to follow an organization policy about which requests to allow and which to deny.
- More refusals, 8. Both Egida models, `Dipto084/Llama-3.1-8B-XGuard-merged`, both AfriGuard plain-reply models, both OTel models, and `yavuz-ai/qwen3-4b-cai-sft`. The OTel pair may refuse a mental-health conversation because it is off-topic for telecom, not because of self-harm.
- Fewer refusals, 2. `ZennyKenny/Daredevil-8B-abliterated` and `MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered`. Both still write a chat reply, and the change is that they decline less.
- Prompt-controlled refusal, 2. Both configurable Hermes models. The system prompt selects a harmless assistant, an uncensored assistant, or a harmful assistant. A parent comparison matches a chat benchmark only when both models see the same system prompt.
- A different skill, 1. `SafetyMP/corporate-site-harness-llm` answers harness questions and refuses shortcuts such as an invented pass. It still writes assistant text, so a chat benchmark is the matching instrument.

**28 write a verdict, a score, or a tree** (14 reasoning and a verdict, 7 harm-category labels, 4 binary labels, 2 structured trees, 1 numeric score). A classifier-style benchmark matches that output. Many of these cards show the verdict only after a set instruction, a policy, or a fixed template. A bare counselling turn is not the input those cards demonstrate.

**3 write a label and a reply.** Both AfriGuard checkpoints trained with `<safety>`, `<category>`, and `<response>` tags, and `lordChipotle/SuicidePreventionLlama`. For SuicidePreventionLlama, a detection prompt is trained toward suicidal versus non-suicidal, and a counselling prompt is trained toward a short therapeutic reply. One benchmark does not cover both tasks.

**1 writes an exam letter.** `cs-552-2026-Flash-McQueenS-and-TheKing/safety_model` expects a multiple-choice safety item and writes a one-sentence justification plus a letter in `\boxed{}`. That is neither a counselling reply nor a safe/unsafe label on a free conversation.

**6 cards do not say what the model writes.** Both PolicyShiftGuard checkpoints, both EMBGuard checkpoints, `Tuwhy/Qwen2-VL-7B-MIRage`, and `Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01`. A chat comparison with the parent has no described reply to score. PolicyShiftGuard was still coded as judgment training: the card calls each checkpoint a guardrail model that reads policy bundles and does not show the label text.

15 + 28 + 3 + 1 + 6 = 53.

## Judgment calls on those axes


BananaMind's opening sentence says it classifies an input prompt as Safe or Unsafe and, for unsafe inputs, returns the violated categories. The intended-use list also names assistant-response classification. Axis A is user prompt, from the opening sentence. Axis B is harm-category label because the unsafe output names categories; the same sentence also gives a binary word.

Salamandra's card says both binary safe/unsafe and multiclass classification, and it names Dangerous, Toxic, and Sexual content. Axis B is harm-category label. The uses list includes chat moderation and filtering of LLM responses. Axis A is a piece of text, because the model description says it classifies text content and does not define a paired prompt-and-response input.

GA Guard writes one violation or not-violation token per category, including violence and self-harm and prompt security. Axis B is harm-category label.

DynaGuard's fast mode is PASS or FAIL. A second mode writes a reasoning trace first. Axis B is binary label, because that is the classification the fast mode returns. The quote records both modes.

Nemotron-Content-Safety-Reasoning-4B has a Reasoning Off mode that writes `Prompt harm` and `Response harm` lines, and a Reasoning On mode that writes a trace and then those lines. Axis B is reasoning and a verdict, because the card specifies both modes and the checkpoint name is the reasoning model. Reasoning Off does not include the prose.

SafeAtlas returns five ordered safety levels and a score from 0 to 100, plus three auxiliary judgments for the request and the response. Axis B is harm-category label, for the five levels. The score is in the same quote.

COMPASS Gemma's pipeline tag is image-text-to-text because the parent is Gemma 3. The card describes text query–response pairs for organization policy. Axis A is user prompt.

AfriGuard plain reply is Axis C more refusals because the training target is a helpful answer or a brief refusal. The card does not report a refusal rate against the parent.

The Stentor card pastes the original Stentor-30M-Instruct write-up under the Heretic heading. That write-up describes supervised training that added refusals. The deciding line for this checkpoint is the decensoring sentence at the top.

ProGuard says it identifies and reasons about unknown risks in text and images, and it says it moves past a fixed category list. The card does not show the label schema. Axis B is reasoning and a verdict from that sentence.

SafeGuard-VL's card includes the instruction "Provide your reasoning and final judgment (Safe/Unsafe)" in the example prompt. That sentence is what the card shows the model being asked to write.

SycoFact scores an assistant reply on several 0–1 dimensions, including sycophancy and harmlessness. The card says the training signal came from geometric activation directions and that no human labels were used. The fine-tune still turns the model into an evaluator that writes scores.

BenefitReporter and HarmReporter judge a user prompt by writing a tree about what would follow if a model answered it helpfully. The cards say an external aggregation step turns the trees into a score.

## Out-of-scope statements on the 53 cards

## Class definitions (used in both tables)

- **A** — The card explicitly says the model must not / should not be used for therapy, counseling, mental-health support, diagnosis, treatment, or medical advice, or says it was not trained / not designed for that. A direct prohibition or a "not trained to / not intended to" statement. Quoted verbatim.
- **B** — Softer disclaimer only: "not a substitute for a professional", "for research/educational purposes only", "consult a professional", crisis-line text, while the card still presents the model as a mental-health / support assistant (or, in the safety cohort, as an advice-giving assistant). Quoted verbatim.
- **C** — Generic limitations only (hallucination, bias, English only, "do not deploy", "not a production system", etc.); nothing about therapy, counseling, mental-health, or medical use.
- **D** — No limitations, out-of-scope, or disclaimer text at all.
- **E** — No cached README.

Rules applied when a card was borderline:

- A statement that only excludes **crisis / emergency** use, with no mention of therapy, counseling, diagnosis, treatment, or medical advice, is B, not A (crisis text is listed under B in the task definition).
- A statement that the model is "not for diagnosis or treatment" (or "does not diagnose, treat, ...") counts as A, because treatment and diagnosis are the medical/therapeutic use being excluded. The rows where A rests mainly on this wording are listed under "Judgment calls" below.
- Benchmark tables and result commentary (e.g. "perplexity is 5.9x base") are not counted as limitation text. A card needs a sentence whose purpose is to warn or restrict use to leave class D.

Quote conventions: text inside quotes is verbatim from the card, including markdown bold markers and emoji. Bulleted lists are joined with " / ". A line break inside a sentence is replaced with a space. "..." marks omitted text in the middle of a long passage. The "stated intended use" column is a short quote or close paraphrase of what the card says the model is for.

Counted on the 53 rows in `kept.csv`. A = 1 (`Banaxi-Tech/BananaMind-V2.5-Content-Safety`). B = 1 (`lordChipotle/SuicidePreventionLlama`). C = 32. D = 19. 1 + 1 + 32 + 19 = 53.

`Banaxi-Tech/BananaMind-V2.5-Content-Safety` is A on a literal reading of "not intended to make legal, medical, emergency, ... decisions". The sentence is a generic high-impact-decisions disclaimer on a content-safety classifier, not a mental-health statement. If only mental-health-flavoured statements count, this row moves to C and A = 0.

| hf_id | class | stated intended use | verbatim out-of-scope quote | card file used |
|---|---|---|---|---|
| Banaxi-Tech/BananaMind-V2.5-Content-Safety | A | "text-only content-safety classification model"; "designed to classify an input prompt as either `Safe` or `Unsafe`" | "This model is not intended to make legal, medical, emergency, employment, credit, law-enforcement, or other high-impact decisions." | Banaxi-Tech__BananaMind-V2.5-Content-Safety__2026-10-05.md |
| lordChipotle/SuicidePreventionLlama | B | "designed to (1) **detect suicidal or self-harm risk** in text, and (2) **provide a short therapeutic-style reply** if suicidality is detected"; "For research on suicidal ideation detection and mental-health conversation modeling." | "This model is **not** a substitute for professional mental-health services or emergency intervention. If you or someone you know is in crisis, **seek professional help** (e.g., call emergency services or hotlines like `988` in the US)." Also: "**Not a Medical Professional**: This model does not replace mental-health professionals." | lordChipotle__SuicidePreventionLlama__2026-10-05.md |
| AIML-TUDA/QwenGuard-v1.2-3B | C | "vision safeguard model that assesses images based on a provided safety policy, providing safety rating, safety category and a rationale" | | AIML-TUDA__QwenGuard-v1.2-3B__2026-10-05.md |
| AIML-TUDA/QwenGuard-v1.2-7B | C | "vision safeguard model that assesses images based on a provided safety policy, providing safety rating, safety category and a rationale" | | AIML-TUDA__QwenGuard-v1.2-7B__2026-10-05.md |
| BSC-LT/salamandra-7b-instruct-guard | C | "safety classification model designed for Catalan, Spanish, and English content moderation" | | BSC-LT__salamandra-7b-instruct-guard__2026-10-05.md |
| GeneralAnalysis/GA_Guard_1B | C | "intended for automated moderation, agent input screening, prompt-injection detection, and safety triage" | | GeneralAnalysis__GA_Guard_1B__2026-10-05.md |
| Jazhyc/Llama-3.1-8B-aims-grpo | C | "intent-aware, reasoning-based safety classifier" for user prompts | | Jazhyc__Llama-3.1-8B-aims-grpo__2026-10-06.md |
| MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered | C | "decensored version of StentorLabs/Stentor-30M-Instruct" (refusals removed by abliteration); base card: "basic chat interaction, some degree of safety-aware responses" | | MihaiPopa-1__Stentor-30M-Instruct-heretic-safety-defiltered__2026-10-05.md |
| PolicyShiftGuard/PolicyShiftGuard-3B-RP-SFT | C | "Stage-1 Randomized Policy SFT (RP-SFT) checkpoint" of a Qwen2.5-VL image guardrail; "provided for reproducibility and ablation use" | | PolicyShiftGuard__PolicyShiftGuard-3B-RP-SFT__2026-10-06.md |
| PolicyShiftGuard/PolicyShiftGuard-7B-RP-SFT | C | "Stage-1 Randomized Policy SFT (RP-SFT) checkpoint" of a Qwen2.5-VL image guardrail; "provided for reproducibility and ablation use" | | PolicyShiftGuard__PolicyShiftGuard-7B-RP-SFT__2026-10-06.md |
| SafetyMP/corporate-site-harness-llm | C | "corporate/site harness assistant" for "policy, `corp-harness` CLI shape, artifact/gate JSON, and hard refusals" | | SafetyMP__corporate-site-harness-llm__2026-10-05.md |
| ZennyKenny/Daredevil-8B-abliterated | C | Abliterated (refusal-direction removed) Daredevil-8B; "intended for **experiments in safety and alignment research**" | | ZennyKenny__Daredevil-8B-abliterated__2026-10-06.md |
| cs-552-2026-Flash-McQueenS-and-TheKing/safety_model | C | "Answering English safety multiple-choice questions in the `\boxed{<letter>}` format. This is a research/coursework artifact." | | cs-552-2026-Flash-McQueenS-and-TheKing__safety_model__2026-10-05.md |
| ctrltokyo/prompt-injection-detector | C | "detecting prompt injection attacks using chain-of-thought reasoning" | | ctrltokyo__prompt-injection-detector__2026-10-06.md |
| farbodtavakkoli/OTel-LLM-12B-Safety | C | "safety-tuned telecom language model"; "intended for telecom RAG pipelines where the assistant should refuse to answer when retrieved context is missing, irrelevant, or insufficient" | | farbodtavakkoli__OTel-LLM-12B-Safety__2026-10-06.md |
| farbodtavakkoli/OTel-LLM-8.3B-Safety | C | "safety-tuned telecom language model"; "intended for telecom RAG pipelines where the assistant should refuse to answer when retrieved context is missing, irrelevant, or insufficient" | | farbodtavakkoli__OTel-LLM-8.3B-Safety__2026-10-06.md |
| flowxai/scam-guard-qwen06b | C | "on-device scam & fraud message detector for SMS, email, and chat text (English + Romanian)"; "consumer triage aid" | | flowxai__scam-guard-qwen06b__2026-10-05.md |
| flowxai/scam-guard-qwen17b | C | "on-device scam & fraud message detector for SMS, email, and chat text (English + Romanian)"; "consumer triage aid" | | flowxai__scam-guard-qwen17b__2026-10-05.md |
| henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B | C | "bilingual (中文 + English) **content guard** that filters harmful **text and images** for training corpora and online moderation" | | henrywch2huggingface__LE_Morals-Guard-Qwen3.6-35B-A3B__2026-10-05.md |
| iwalton3/sycofact | C | "alignment evaluator"; "designed to detect sycophancy and dangerous AI outputs" (scores other models' responses; not a chat assistant) | | iwalton3__sycofact__2026-10-05.md |
| jdleo1/tinysafe-3 | C | "4B parameter safety classifier"; "safe/unsafe verdict, 7 safety categories, and chain-of-thought reasoning" | | jdleo1__tinysafe-3__2026-10-06.md |
| jl3676/BenefitReporter | C | "generates a structured "benefit tree" for a given prompt"; combined with HarmReporter as a prompt-harmfulness moderation tool | | jl3676__BenefitReporter__2026-10-06.md |
| jl3676/HarmReporter | C | "generates a structured "harm tree" for a given prompt"; "Harmfulness analysis" and "Moderation tool" | | jl3676__HarmReporter__2026-10-06.md |
| nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3 | C | "multilingual content safety model that moderates human-LLM interaction content and classifies user prompts and LLM responses as safe or unsafe" | | nvidia__Llama-3.1-Nemotron-Safety-Guard-8B-v3__2026-10-05.md |
| nvidia/Nemotron-Content-Safety-Reasoning-4B | C | "LLM classifier designed to function as a dynamic and adaptable guardrail for content safety and dialogue moderation (topic-following)" | | nvidia__Nemotron-Content-Safety-Reasoning-4B__2026-10-05.md |
| prismor/prompt-guard-1.5b | C | "prompt injection detector"; "outputs `INJECTION` or `SAFE`" | | prismor__prompt-guard-1.5b__2026-10-05.md |
| prithivMLmods/ImageShield-MMCF-2B-vl | C | "multimodal content-safety classifier"; "classify visual content as **Safe** or **Unsafe**" (NSFW focus) | | prithivMLmods__ImageShield-MMCF-2B-vl__2026-10-06.md |
| tyodd/SafeGuard-VL-RL | C | "policy-aware visual safety guardrail model"; "robust unsafe-image detection" | | tyodd__SafeGuard-VL-RL__2026-10-06.md |
| vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B | C | "configurable safety tuning (CST)": system prompt switches the model between harmless, uncensored, and harmful behaviour; "research artifact in the fields of safety and alignment" | | vicgalle__Configurable-Hermes-2-Pro-Llama-3-8B__2026-10-06.md |
| vicgalle/Configurable-Hermes-3-Llama-3.1-8B | C | "configurable safety tuning (CST)": system prompt switches the model between harmless, uncensored, and harmful behaviour; "research artifact in the fields of safety and alignment" | | vicgalle__Configurable-Hermes-3-Llama-3.1-8B__2026-10-06.md |
| yavuz-ai/qwen3-4b-cai-sft | C | "supervised stage of a Constitutional AI reproduction"; "research artifact, not a better assistant" | | yavuz-ai__qwen3-4b-cai-sft__2026-10-06.md |
| zrwang1211/SafeAtlas-Guard-2B | C | "target-conditioned multimodal safety model"; "evaluates image content, image-grounded user requests, and assistant responses" | | zrwang1211__SafeAtlas-Guard-2B__2026-10-05.md |
| zrwang1211/SafeAtlas-Guard-4B | C | "target-conditioned multimodal safety model"; "evaluates image content, image-grounded user requests, and assistant responses" | | zrwang1211__SafeAtlas-Guard-4B__2026-10-05.md |
| zrwang1211/SafeAtlas-Guard-8B | C | "target-conditioned multimodal safety model"; "evaluates image content, image-grounded user requests, and assistant responses" | | zrwang1211__SafeAtlas-Guard-8B__2026-10-05.md |
| AIM-Intelligence/COMPASS_Qwen2.5-7B-Instruct_LoRA | D | "**LoRA adapter** trained for **organization-specific policy adherence** in the COMPASS framework" | | AIM-Intelligence__COMPASS_Qwen2.5-7B-Instruct_LoRA__2026-10-06.md |
| AIM-Intelligence/COMPASS_gemma-3-4b-it_LoRA | D | "**LoRA adapter** trained for **organization-specific policy adherence** in the COMPASS framework" | | AIM-Intelligence__COMPASS_gemma-3-4b-it_LoRA__2026-10-06.md |
| Dipto084/Llama-3.1-8B-XGuard-merged | D | "reproduction of **X-Guard**, the defended target model from the X-Teaming paper"; "baseline defense in TRACE" (Llama-3.1-8B-Instruct fine-tuned on a multi-turn safety corpus) | | Dipto084__Llama-3.1-8B-XGuard-merged__2026-10-06.md |
| EMBGuard/EMBGuard-2B | D | None stated in prose. Front matter only (tags `embodied-ai`, `robotics`, `safety`, `guardrail`, `vision-language-model`, `risk-assessment`). | | EMBGuard__EMBGuard-2B__2026-10-06.md |
| EMBGuard/EMBGuard-4B | D | None stated in prose. Front matter only (tags `embodied-ai`, `robotics`, `safety`, `guardrail`, `vision-language-model`, `risk-assessment`). | | EMBGuard__EMBGuard-4B__2026-10-06.md |
| HPAI-BSC/Qwen2.5-72B-Instruct-Egida-DPO | D | Qwen2.5-72B-Instruct DPO-tuned on Egida adversarial prompts (paper: "Efficient Safety Retrofitting Against Jailbreaking for LLMs"); no intended-use statement | | HPAI-BSC__Qwen2.5-72B-Instruct-Egida-DPO__2026-10-06.md |
| HPAI-BSC/Qwen2.5-7B-Instruct-Egida-DPO | D | Qwen2.5-7B-Instruct DPO-tuned on Egida adversarial prompts (paper: "Efficient Safety Retrofitting Against Jailbreaking for LLMs"); no intended-use statement | | HPAI-BSC__Qwen2.5-7B-Instruct-Egida-DPO__2026-10-06.md |
| Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01 | D | SFT of Llama-3.1-8B-Instruct on a WildGuardMix-derived dataset; auto-generated TRL card with no stated use | | Neelectric__Llama-3.1-8B-Instruct_SFT_safetyv00.01__2026-10-05.md |
| ReasoningShield/ReasoningShield-3B | D | "specialized safety moderation model tailored to identify hidden risks in intermediate reasoning steps in Large Reasoning Models (LRMs)" | | ReasoningShield__ReasoningShield-3B__2026-10-06.md |
| Tuwhy/Qwen2-VL-7B-MIRage | D | "Qwen2-VL-7B-Instruct model fine-tuned on MIS training set" (vision-language safety fine-tuning); no intended-use statement | | Tuwhy__Qwen2-VL-7B-MIRage__2026-10-06.md |
| adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1 | D | AfriqueQwen3.5-4B fine-tuned on AfriGuard-inst safety data (African languages); emits `<safety>`, `<category>`, `<response>` tags; no intended-use statement | | adzcai__AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1__2026-10-06.md |
| adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged | D | LoRA-merged variant of the above; no intended-use statement | | adzcai__AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged__2026-10-06.md |
| adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1 | D | AfriqueQwen3.5-4B fine-tuned on AfriGuard-plain data; "answers or refuses directly, without emitting a safety label"; no intended-use statement | | adzcai__AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1__2026-10-06.md |
| adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged | D | LoRA-merged variant of the above; no intended-use statement | | adzcai__AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged__2026-10-06.md |
| tomg-group-umd/DynaGuard-1.7B | D | "guardian models designed to evaluate text against user-defined, natural language policies" | | tomg-group-umd__DynaGuard-1.7B__2026-10-06.md |
| tomg-group-umd/DynaGuard-4B | D | "guardian models designed to evaluate text against user-defined, natural language policies" | | tomg-group-umd__DynaGuard-4B__2026-10-06.md |
| tomg-group-umd/DynaGuard-8B | D | "guardian models designed to evaluate text against user-defined, natural language policies" | | tomg-group-umd__DynaGuard-8B__2026-10-06.md |
| yushaohan/ProGuard-3B | D | "proactive multimodal safeguard model"; "identify and reason about unknown risks across both text and visual modalities" | | yushaohan__ProGuard-3B__2026-10-06.md |
| yushaohan/ProGuard-7B | D | "proactive multimodal safeguard model"; "identify and reason about unknown risks across both text and visual modalities" | | yushaohan__ProGuard-7B__2026-10-06.md |
