---
license: other
license_name: hamo-rail-s-1.0
license_link: LICENSE
language:
  - zh
  - en
base_model: Qwen/Qwen3-0.6B
pipeline_tag: text-generation
tags:
  - mental-wellness
  - affect-scoring
  - psychology
  - knowledge-distillation
  - qwen3
  - gguf
  - mlx
  - hamo
---

# hamo-score-0.6b — the little model that takes your pulse

*给每句话把脉的小模型（中文版说明见下半部分）*

> ### 👉 Start with the toolkit, not the weights
> `pip install hamo-score` → [**hamo-score-toolkit**](https://github.com/HamoAI/hamo-score-toolkit) (Apache-2.0)
> is the other half of this model: the exact prompt format, the crisis gate this model
> *requires upstream of it*, the smoothing math its scores are designed to feed, a
> one-command Docker server, and a 195-question self-check exam. Weights alone invite the
> one deployment shape this model was designed against.
> **Disagree with a score?** That is the single most useful thing you can send us —
> [open a disagreement report](https://github.com/HamoAI/hamo-score-toolkit/issues/new?template=score_disagreement.md);
> they feed the human gold-label program that steers future versions.

**hamo-score-0.6b** reads one message from a mental-wellness conversation and scores five
psychological pulse signals. It never writes replies. It is the first component distilled from
the production scoring of [Hamo AI](https://www.hamo.ai)'s closed-loop wellness engine, released so that
practitioner-supervised tools can run state scoring **locally** — no API, no data leaving the room.

> ⚠️ **What this model is NOT.** It is not a chatbot, not a diagnostic instrument, and
> **not a crisis detector**. In Hamo's own production system, crisis and self-harm content is
> short-circuited by an independent deterministic mechanism *upstream* of this model — it never
> reaches the scorer. Any deployment must reproduce that pattern (see LICENSE §3c).

## The five pulses (AWEHB)

Each user message gets five scores on a 0.0–3.0 scale (0.5 grid):

| Dim | Name | Plain reading |
|---|---|---|
| **A** | Agency | Is the person doing something for themselves? (incl. small plans, coping statements) |
| **W** | Withdrawal | Giving up, avoiding, disengaging? |
| **E** | Extremity | Catastrophizing chains, all-or-nothing thinking? (bounded realistic worry stays LOW) |
| **H** | Hostility | Attacking someone? (venting frustration without a target is NOT hostility) |
| **B** | Boundary | Can they speak from an "I" position — needs, limits, clear stance? |

**A note on B.** Its theoretical root is *differentiation of self* (family-systems sense:
a bounded two-person relationship vs. an enmeshed, undifferentiated one). A per-message scorer
cannot see the relationship — it sees language. So B measures the **linguistic footprint** of
boundaries: "I need… / I'm not willing… / this is my limit" scores high; panicked venting
(self dissolved in affect) scores low; insults are H, not B. B is a per-message signal,
not a relationship diagnosis.

The scores are designed to feed **deterministic downstream code** (stress update, state
buckets, action gating) — in Hamo, an exponential blend `0.8 × history + 0.2 × message`
smooths per-message noise 5× before any decision is taken. We recommend the same pattern.

## Quickstart

> 🚀 **What the toolkit gives you**, in detail:
> - **Library** — prompt format, parsing, the smoothing math, and the license-required
>   crisis gate in `pip install` + a few lines of code;
> - **Reference server** — `docker compose up` fetches the GGUF, warms the model, and
>   exposes the full gate → score → smooth → bucket pipeline as `POST /score`;
> - **Self-check exam** — 195 synthetic teacher-labeled questions + 10 handwritten gate
>   cases, with an official reference measured on the v7 bf16 weights at temperature 0 (JSON 100% ·
>   dimension-level 83.5%, expected band 81–86% · gate 10/10; the shipped q8 GGUF with neutral
>   sampling scores 83.8%) so you can verify your wiring reproduces the official numbers;
> - **Fine-tuning guide** — [`docs/finetune.md`](https://github.com/HamoAI/hamo-score-toolkit/blob/main/docs/finetune.md),
>   the seven-generation playbook (including the two rejected generations and why) for
>   adapting the scorer to your own population with your own consented data.
>
> Release notes: [EN](https://www.hamoai.tech/blog/open-sourcing-hamo-score-toolkit/) ·
> [中文](https://www.hamo.ai/blog/open-sourcing-hamo-score-toolkit/).

The model was trained on **exactly one prompt format** (its rubric is baked into the weights —
do not add scoring instructions):

```
给来访者最新消息打分（AWEHB，0.0-3.0）。
此前对话:
user: <turn>
assistant: <turn>
最新消息: <message to score>
```

The context block (`此前对话:`) is optional; up to 5 turns are accepted, and the official
toolkit trims to the production-validated guard — last 3 turns × 200 chars, message capped
at 500 chars. Apply the Qwen3
chat template with thinking disabled, temperature 0. Output is a single JSON object.

**transformers**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, json, re

m = AutoModelForCausalLM.from_pretrained("HamoAI/hamo-score-0.6b", torch_dtype=torch.bfloat16)
tok = AutoTokenizer.from_pretrained("HamoAI/hamo-score-0.6b")

prompt = "给来访者最新消息打分（AWEHB，0.0-3.0）。\n此前对话:\nassistant: 这周过得怎么样？\n最新消息: 今天试着出门散了个步"
text = tok.apply_chat_template([{"role": "user", "content": prompt}],
                               add_generation_prompt=True, tokenize=False, enable_thinking=False)
out = m.generate(**tok(text, return_tensors="pt"), max_new_tokens=80, do_sample=False)
print(re.search(r"\{[^{}]*\}", tok.decode(out[0])).group())
# {"A": 1.5, "W": 0.0, "E": 0.0, "H": 0.0, "B": 1.0}
```

**ollama / llama.cpp** — a ready `q8_0` GGUF is in [`gguf/`](https://huggingface.co/HamoAI/hamo-score-0.6b/tree/main/gguf). Modelfile:

```
FROM ./hamo-score-0.6b-v7.q8.gguf
TEMPLATE """<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
<think>

</think>

"""
PARAMETER temperature 0
PARAMETER num_predict 80
PARAMETER stop <|im_end|>
PARAMETER repeat_penalty 1.0
PARAMETER top_k 0
PARAMETER top_p 1.0
```

> ⚠️ **The last three parameters are not optional.** ollama defaults to
> `repeat_penalty 1.1`. This model's output — `{"A": 0.0, "W": 0.0, "E": 0.0,
> "H": 0.0, "B": 0.0}` — is deliberately repetitive, so penalising repeated
> tokens pushes every score *away from zero*, fabricating signal that isn't
> there. Measured on our 300-question boundary-discrimination exam, same
> weights (this release's shipped v7 q8 GGUF), sampling as the only variable: fabrication rate
> **2.9% → 8.7%**, boundary sign-flips (a true `0.0` scored `≥2.0`) **0 → 1**; the miss rate
> falls from 12.8% to 6.7%, which is the same upward push, not an improvement. The same switch
> on the earlier v6.1 q8 GGUF: fabrication **13.5% → 25.0%**, sign-flips **6 → 10**. Earlier
> revisions of this card omitted them; if you deployed from those
> instructions, add them and re-create the model.

Parse the first `{...}` in the response (the model may emit an empty `<think>` block first).

## Evaluation

Held-out exam: **758 real, pseudonymised production turns** (labels = the production-scale
LLM scorer this model is designed to replace; the exam turns are **never trained on** — the only real data
in training is the separately disclosed 440 consented staff turns, see "How it was trained").

| Metric | Better is | **v7 (this release)** | v6.1 (previous) | Teacher (DeepSeek, qualification paper) | Reference scorer self-consistency* |
|---|---|---|---|---|---|
| Dimension-level, within ±0.5 | ↑ higher | **85.1%** (A84 / W87 / E87 / H94 / B74) | 85.6% | 88.7% | 94–98% |
| Decision-level (state bucket after deterministic stress calc) | ↑ higher | **97.1%** | 96.2% | 97.5% | — |
| Crisis-phrase W-recall misses (count, not %) | ↓ **lower** | **3** | 4 | — | — |
| JSON validity | ↑ higher | ~100% | ~100% | — | — |

**Read the two headline rows together.** v7 trades ~0.5 pt of raw agreement with the
reference scorer's labels for +0.9 pt on the decision the product actually consumes, and one
fewer crisis miss. The dimension-level dip is expected rather than a regression: v7 was
trained on a re-labelled corpus (the teacher re-scored every row at temperature 0, removing
label noise), so the student is now more faithful to the *denoised* labels and correspondingly
slightly less aligned with the noisier reference it was originally distilled from. Measured
directly: agreement with the temperature-0 teacher on boundary scores rose **57.3% → 69.3%**
while agreement with the original reference scorer on the same dimension stayed flat.

Evaluated on the 453-turn final split of the real-conversation exam (never trained on; gold
labels include 8 human corrections). Routine checkpoint selection used the separate 305-turn
selection split, but in the last step of choosing between v7's two finalist checkpoints we also
looked at their final-split scores — they tied at 97.1% decision-level (85.0% vs 85.1%
dimension-level), and the tie was broken on boundary-exam error type, not on this split.

**Residual textual overlap, measured rather than assumed.** The exam and training splits are
disjoint by sample and by conversation, but the consented staff contributors repeat themselves
across sessions: 42 of the 453 final-exam turns (9.3%) carry a message text that also occurs
somewhere in the 440 consented training turns, 11 of them (2.4%) with the same recent context.
We scored those rows separately. For v7: on the 42 overlapping turns the model reaches 88.1%
dimension-level and 100% decision-level; on the 411 with no textual overlap, **84.8% and
96.8%**. So the headline figures carry roughly **+0.3 points** of optimism from this
effect — small, and stated here rather than left for someone else to find. (v6.1 measured the
same way: 89.0%/100% on the overlap, 85.2%/95.9% clean.) (Only 5 of the 42
also share the training row's label vector: the same sentence usually earns different scores in
a different turn, so these are not free points, merely easier ones.)

### Boundary discrimination — what v7 was actually built to fix

Agreement metrics hide the failure that mattered most. On a 300-question exam built
specifically to probe the B (Boundary) decision surface — 60 matched pairs plus 180 singletons
across nine trap cells — v6.1 was reading **self-erasure as strong boundary**: "行，我全听你的，
你说哪天去就哪天去" ("fine, I'll do whatever you say, you decide") scored B=2.5 where the truth
is 0.0. That is a sign error on B's negative pole, not a calibration wobble, and B carries the
largest single weight in the downstream stress formula.

| 300-question boundary exam | Better is | v6.1 | **v7** |
|---|---|---|---|
| Fabrication — a true 0 scored ≥1.0 (sees boundary that isn't there) | ↓ **lower** | 13.5% | **2.9%** |
| Miss — a true high scored ≤0.5 (misses a real boundary) | ↓ **lower** | 16.1% | **12.8%** |
| **Sign flips** — a true 0.0 scored ≥2.0 (count; reads self-erasure as strong boundary) | ↓ **lower** | 6 | **0** |
| Paired direction accuracy — ranks the higher-boundary arm above the lower | ↑ higher | 81.7% | **98.3%** |

Three of the four rows are error rates, so **lower is better on the first three and higher on
the last**; v7 improves on all four.

Each column measured on that release's shipped q8 GGUF with neutral sampling, so they describe the
artifact you download rather than an internal checkpoint. Direction accuracy is the cleanest
of the four — it asks only whether the model ranks the higher-boundary arm of a matched pair
above the lower one, so it is immune to absolute calibration.

\* Self-consistency = the same messages scored twice by the reference scorer in two live
environments; its own agreement is only 94–98% at dimension level — the practical ceiling.

Latency (single message, warm): ~0.8 s on Apple M1 Pro (MLX bf16); 1.5–2.9 s on a
2-vCPU ARM server (q8 GGUF, CPU-only). Crisis-phrase W-recall improved 2× in the v4
generation and edged further down in v6.1 and again in v7 (final-exam misses 11 → 5 → 4 → 3) — but see the
crisis disclaimer above: recall here is defense-in-depth, not the defense.

## Community quantizations — and what we measured on v7

[**mradermacher/hamo-score-0.6b-GGUF**](https://huggingface.co/mradermacher/hamo-score-0.6b-GGUF)
provides static GGUF quants (Q2_K to f16) of the v4 weights this repository carried on
2026-08-05 — two releases before v7 — twelve build targets we never shipped ourselves. Thanks to mradermacher for the work, and for carrying the RAIL-S license
terms through redistribution. **Those builds are now outdated:** anyone who wants a v7 Q6_K or
Q4_K_M currently has to quantize this repository's v7 weights themselves (llama.cpp:
`convert_hf_to_gguf.py` to f16, then `llama-quantize`).

Because this model's read-outs gate how deep a conversation may go, quantization damage here is
a clinical question rather than a perplexity number — so we measured it on v7 itself. Every
column below comes from the v7 weights, run through the same 453-turn final exam with the same
prompt and parser: bf16 via MLX (this column reproduces the headline figures above), the GGUF
builds via llama.cpp with neutral sampling. Q8_0 is the GGUF shipped in this repository;
**Q6_K and Q4_K_M are our own quantizations of v7** (a v7 f16 GGUF from llama.cpp's
`convert_hf_to_gguf.py`, then llama.cpp's `llama_model_quantize` — the library function the
`llama-quantize` command above wraps, so the same path) and are not published anywhere.

| v7 weights, 453-turn final split | bf16 (MLX) | Q8_0 (shipped) | Q6_K (ours, unpublished) | Q4_K_M (ours, unpublished) |
|---|---|---|---|---|
| Dimension-level ±0.5 | 85.1% | 85.3% | 85.3% | 84.5% |
| Decision-level (state bucket) | 97.1% | 97.1% | 96.9% | 96.7% |
| Crisis W-misses (gold ≥2.5 → pred <0.5, n=37) | 3 | 3 | 3 | 3 |
| Mean W on those 37 crisis-adjacent turns (gold 2.84) | 2.58 | 2.58 | 2.58 | **2.50** |
| On those 37 turns, W lower / higher than Q8_0 | 0 / 0 | — | 1 / 1 | **6 / 1** |
| Mean score shift vs Q8_0, all 453 turns | ≈0 | — | every dimension within ±0.011 | A −0.05, W −0.03, E −0.01, H +0.00, B +0.00 |
| File size | — | 0.64 GB | 0.50 GB | 0.40 GB |
| P50 latency (Apple M1 Pro; llama.cpp on Metal unless noted) | 0.83 s (MLX) | 0.70 s | 0.56 s | 0.54 s |

**What the table says.** On v7, Q6_K is indistinguishable from Q8_0 on this exam. Against Q8_0,
Q4_K_M loses 0.8 pt at dimension level and 0.4 pt at decision level, and did not add a crisis miss here —
but it still attenuates one-sidedly where it matters least forgivingly: on the 37
crisis-adjacent turns (gold W ≥ 2.5) it scores W **lower than Q8_0 on 6 and higher on 1**,
pulling that subset's mean withdrawal signal from 2.58 to 2.50, and across all 453 turns its
mean shift is small (A −0.05, W −0.03, the rest within ±0.01). The methodological point still stands on v7: bucket
agreement moves only 0.4 points across the three GGUF builds — **the state buckets are coarse
enough to absorb a damped signal, so bucket agreement alone would never have surfaced this.**
That is why the toolkit's `compare_quants.py` prints a directional table, not just agreement.

An earlier version of this section compared mradermacher's v4 community builds against our
v6.1 Q8_0 and so overstated quantization loss — its "Q4_K_M lower than Q8_0 on 20 of 37",
"Q6_K ~1 point below" and "Agency drift of −0.19" findings were mostly the v4 → v6.1 version gap, and
the all-v7 table above supersedes them.

**What we recommend.**

- **Q8_0** — the reference build, shipped in this repository. Use it when the read-outs gate
  behaviour and you have the 0.64 GB.
- **Q6_K, quantized from v7** — validated for gating use when memory is tight: indistinguishable
  from Q8_0 on the final exam, including the crisis-adjacent subset, and it saves 22% of the
  size. (The community Q6_K is built from v4 and is not covered by this validation.)
- **Q4_K_M** — fine for research, offline analysis, and any use where a human reads the scores
  rather than a system acting on them. If memory forces it into a gating deployment, keep
  deterministic crisis detection upstream where it belongs (LICENSE §3c requires that pattern at
  any quantization), and consider lowering your withdrawal thresholds to compensate for the
  one-sided W attenuation above.

Builds below Q4_K_M remain unvalidated by us and should be assumed worse until measured;
mradermacher's v4 builds are outdated and not covered by these recommendations. The
[toolkit](https://github.com/HamoAI/hamo-score-toolkit)'s `eval/compare_quants.py` runs the same
comparison, including the directional table, on the public synthetic exam. Its absolute numbers
will differ from the 453-turn table above, but the shape transfers. If you validate a build we
haven't, we would be glad to link your numbers.

## How it was trained

A three-stage distillation chain — the full story is in the companion write-up
[*Distilling hamo-score-0.6b: A Plateau, Three Bugs, and Why Data Beat Model Size*](https://www.hamoai.tech/blog/distilling-hamo-score-0-6b/):

1. **Exam by the incumbent**: 1,198 pseudonymised production turns with reference scores,
   split by session hash — 440 calibration turns and a 758-turn evaluation set, the latter
   splitting again into 305 selection and the **453-turn final** that grades this release.
   The teacher was qualified on the calibration turns; from v6.1 those same 440 turns, all
   consented staff data, also enter training. Elsewhere in this card **440 always means that
   consented set** — the qualification paper is described by its role, not its size, so the
   two uses cannot be mistaken for unrelated numbers that happen to coincide.

   *On "pseudonymised" rather than "anonymised" or "de-identified" — the weaker word is the
   honest one.* The salt is a fixed hard-coded string, so anyone holding the script can
   recompute the mapping; full timestamps are kept; message text is preserved verbatim; and
   the redaction patterns cover mainland-China formats only — Hong Kong 8-digit numbers,
   North American +1 numbers, personal names, WeChat IDs and street addresses were all
   measured passing through. **This data therefore remains personal data, and a deletion
   request still reaches it.** A separate and non-substituting fact: the payload that reaches
   the weights is only the prompt plus five scores, carrying no identifier and no timestamp.
   Both statements are true; neither one covers for the other.
2. **Affordable teacher**: `deepseek-chat` running the exact production rubric, qualified at
   **88.7% dimension-level / 97.5% decision-level** agreement before being allowed to label
   anything.
3. **Synthetic textbook**: ~20,000 admitted dialogue windows across 6 data generations
   (40+ scenario cells with per-cell label-band admission gates, style quotas for short/
   fragmented/code-switched messages, crisis and boundary contrast pairs).
   **No external-client message has ever entered training — by construction.** Starting
   with v6.1, the corpus additionally includes 440 real conversation turns contributed by
   three company-internal staff members (the founder and two staff counselors), with their
   explicit consent, upsampled ×3 (~8% of the corpus).
4. **Student**: Qwen3-0.6B, LoRA on a single MacBook (MLX; prompt-masked loss, cosine decay,
   grad-checkpointing). Total API cost of the whole project: ~US$7.

Key lessons the hard way (kept as disciplines): gradient-mask the prompt (72% of gradient was
being wasted); halve batch size when doubling sequence length (a silent fp16 explosion taught us);
verify every deploy down to a landed row.

## Limitations & known residuals

- **Chinese-primary** (zh 60% / mixed 22% / en 18% in training); English works but is less tested.
- Message-level footprint, not a person-level or relationship-level assessment.
- Mid-band calibration is coarse (0.5 grid; mid-band usage 7.4% vs reference 21–32%).
- Known residuals: a small set of highly implicit severe-distress phrasings remains hard
  (shared across all versions and the reference scorer); occasional over-scoring of bounded
  multi-step worries on E. The conversational-action gap on A was substantially closed in v6.1
  by real-conversation training data (A 81% → 85%).
- Trained against one specific rubric; scores are **relative to that rubric**, not universal
  psychological ground truth.

## Versions

| Version | Change | Dim-level | Decision-level |
|---|---|---|---|
| v2 | first distillation (7.5k synthetic) | 81% | 95.4% |
| v3.x | rebalance + defect repair | 81% | 96.8% |
| v4 | 8-agent data audit → 15k corpus, masked loss | 84% | 96.3% |
| v5 | synthetic patch cells — **rejected** (crisis-recall regression; kept as a negative result) | — | — |
| v6 | + real turns with incumbent labels — **rejected** (3 crisis-artifact rows rode into training, crisis misses 5 → 9; kept as a negative result) | — | — |
| v6.1 | + 440 consented internal-staff turns (teacher labels) | 85.6% | 96.2% |
| **v7 (this release)** | corpus re-labelled at temperature 0 (label denoising) + 2,713-row boundary-discrimination patch | 85.1% | **97.1%** |

## License

**HAMO-RAIL-S 1.0** (see [LICENSE](https://huggingface.co/HamoAI/hamo-score-0.6b/blob/main/LICENSE)): free commercial and non-commercial use,
modification and redistribution, with four use restrictions — no standalone clinical
determinations, no consequential decisions about individuals (employment / insurance /
surveillance screening), consumer mental-wellness deployments must keep independent upstream
crisis handling + AI disclosure, no re-identification. Base model Qwen3-0.6B remains Apache-2.0.

---

# 中文说明

> ### 👉 请从工具包开始，而不是从权重开始
> `pip install hamo-score` → [**hamo-score-toolkit**](https://github.com/HamoAI/hamo-score-toolkit)（Apache-2.0）
> 是这个模型的另一半：唯一正确的提示词格式、**必须置于模型上游的危机闸门**、分数该喂进去的
> 平滑折算、一条命令起的 Docker 服务器，以及 195 题自检考卷。只拿权重，恰恰会走成这个模型
> 设计上要防住的那种部署。
> **对某个评分不服？** 那是你能给我们的最有价值的东西——
> [提一条分歧报告](https://github.com/HamoAI/hamo-score-toolkit/issues/new?template=score_disagreement.md)，
> 它会直接进入引导后续版本的人类金标计划。

**hamo-score-0.6b** 是 Hamo AI 闭环疗愈引擎里第一个从生产评分中蒸馏出来的组件：给心理支持对话中
来访者的每一句话「把脉」，输出五路 0–3 分的脉象（A 行动力 / W 退缩 / E 极端化 / H 敌意 /
B 边界感）。**它从不写回复，也不是危机检测器**——在 Hamo 生产系统里，危机内容在更上游被
独立的确定性机制短路，永远到不了把脉师面前；任何部署都必须复刻这个模式（见 LICENSE §3c）。

**关于 B（边界感）**：它的理论本源是家庭治疗中的「自我分化」——是「我是我、你是你」的二元
关系，还是彼此淹没的混沌一元。逐句评分器看不见关系，只看得见语言，所以 B 测的是边界感的
**语言足迹**：「我需要…」「这是我的底线」得高分；惊慌的倾泻（自我淹没在情绪里）得低分；
骂人算 H 不算 B。B 是逐句信号，不是关系诊断。

**成绩单（v7，本次发布）**：真实假名化生产对话终评（453 条终评切分，金标含 8 处人工
修正；常规选点用的是另一份 305 条选型集，但 v7 最后两个候选检查点二选一时也看过它们在终评切分上的成绩——
二者决策级同为 97.1%、维度级 85.0% 对 85.1%，最终按边界判别卷的错误性质定夺，而非按终评分数；评分真值来自它要替代的大模型评分器；考卷数据从未参与训练）：维度级 ±0.5 一致率 **85.1%**、
决策级（经确定性压力折算后的状态桶判定）**97.1%**、危机语漏检 **3 条**（v6.1 对应为 85.6% / 96.2% / 4 条）。
其中前两项是一致率、**越高越好**；「危机语漏检」是条数、**越低越好**——v7 由 4 条降到 3 条。
维度级那 0.5 个点的回落不是退步：v7 的语料由教师在温度 0 下全量重标（去标签噪声），学生因此
更忠于**去噪后**的标签，对当初那个含噪参照的一致率自然略降——实测其与温度 0 教师在 B 维的一致率
由 57.3% 升到 69.3%，而对原参照的 B 一致率纹丝不动。

**v7 真正修好的是边界判别**：在一份专为探测 B 决策面而造的 300 题考卷上（60 组配对 + 180 条单题，
覆盖九类陷阱格子），v6.1 会把**自我消融**读成强边界——「行，我全听你的，你说哪天去就哪天去」
真值 B=0.0，它给 2.5。那是 B 负极上的符号错误，而 B 在下游压力公式里权重最大。

| 300 题边界判别卷 | 越好方向 | v6.1 | **v7** |
|---|---|---|---|
| 造分——真值 0 却给 ≥1.0（看见并不存在的边界） | ↓ **越低越好** | 13.5% | **2.9%** |
| 漏判——真值高却给 ≤0.5（漏掉真实的边界） | ↓ **越低越好** | 16.1% | **12.8%** |
| **符号翻转**——真值 0.0 却给 ≥2.0（条数；把自我消融读成强边界） | ↓ **越低越好** | 6 条 | **0 条** |
| 配对方向正确率——高边界那一臂是否排在低的之上 | ↑ 越高越好 | 81.7% | **98.3%** |

前三行是错误率、第四行是正确率，所以**前三行越低越好、最后一行越高越好**；v7 四项全部改善。

两列各测于该版本随包发布的 q8 GGUF + 中性采样，描述的是你下载到的产物本身。

参照系——同一批消息让原评分器自己打两遍，维度级自洽也只有 94–98%。单条延迟：M1 Pro（MLX bf16）约
0.8 秒；2 vCPU ARM 服务器（纯 CPU，q8 GGUF）1.5–2.9 秒。

**残余重叠：我们量了，没有假设掉。** 考卷与训练集按样本、按会话完全不相交，但授权供数的内部
员工会在不同会话里重复说同样的话：终评 453 题中有 42 题（9.3%）的正文在那 440 条授权训练数据
里出现过，其中 11 题（2.4%）连最近上下文也相同。v7 分开判卷的结果——这 42 题维度级 88.1%、
决策级 100%；其余 411 题无任何正文重叠，**维度级 84.8%、决策级 96.8%**。也就是说，上面两个
成绩各含约 **+0.3 个百分点**的乐观。幅度不大，但我们选择自己写出来。（v6.1 用同样方法测得：
重叠部分 89.0% / 100%，无重叠部分 85.2% / 95.9%。）（42 题里只有 5 题
连标签也相同——同一句话换个轮次通常拿到不同分数，所以它们不是白送的分，只是更容易的分。）

**训练方式**：三级师徒链——生产历史评分出考卷（1,198 条假名化真题——用「假名化」而非「匿名化」
是因为弱的那个词才是诚实的：盐是硬编码固定字符串、完整时间戳保留、正文逐字保留，且脱敏正则只覆盖
大陆格式，香港 8 位号码、北美 +1 号码、人名、微信号与住址实测全部穿过，**故这批数据仍属个人信息，
删除权仍及于它**；另一件必须单独陈述、不可用来顶替上一条的事实是：进入权重的载荷只有提示词与五个
分数，不含任何标识符与时间戳。按会话哈希切分为 440 条
校准集与 758 条评测集，后者再切成 305 条选型集与判定本次成绩的 453 条终评集）→ DeepSeek 在
校准集上通过资格考（维度级 88.7% / 决策级 97.5%）后当教师；本卡中「440」始终指那批经授权的
内部员工轮次，资格考卷按用途称呼、不按题量称呼，以免两处用法被误读成两个撞车的数字 → 约 2 万段合成对话当教材（40+ 场景格子、逐格标签准入闸门、短句/
碎片/中英混杂风格配额）→ Qwen3-0.6B 学生在一台 MacBook 上 LoRA 学成。全项目 API 成本
约 7 美元。**训练语料从不包含任何外部来访者消息（构造上保证）；自 v6.1 起额外加入 440 条公司内部员工（创始人与两位咨询师）明示授权的真实对话轮次（×3 上采样，约占语料 8%）。**

**社区量化档位，以及我们在 v7 上实测的量化**：社区志愿者 mradermacher 制作了
[**Q2_K→f16 共 12 个静态 GGUF 量化档**](https://huggingface.co/mradermacher/hamo-score-0.6b-GGUF)
（量化自 2026-08-05 时本仓库的 v4 权重，比 v7 早两个版本）——感谢他的工作，也感谢他在再分发中完整保留了 RAIL-S 许可条款。
**这些档位现已过时**：目前想要 v7 的 Q6_K / Q4_K_M，需要自己从本仓库的 v7 权重量化（llama.cpp：先用
`convert_hf_to_gguf.py` 转成 f16，再用 `llama-quantize`）。

由于这个模型的读数要门控对话能走多深，低比特量化掉了多少不是困惑度数字而是临床问题，所以我们
直接在 v7 上量了：下表每一列都来自 v7 权重，用同一套 453 题终评、同一段提示词、同一个解析器——bf16
走 MLX（这一列复现了上文成绩单），各 GGUF 档走 llama.cpp + 中性采样。Q8_0 是本仓库随包发布的 GGUF；
**Q6_K 与 Q4_K_M 是我们自己从 v7 量化的**（先用 llama.cpp 的 `convert_hf_to_gguf.py` 得到 v7 f16 GGUF，
再经 llama.cpp 的 `llama_model_quantize` 量化——即上文 `llama-quantize` 命令所封装的库函数，路径相同），未在任何地方发布：

| v7 权重，453 题终评 | bf16（MLX） | Q8_0（随包发布） | Q6_K（自量化，未发布） | Q4_K_M（自量化，未发布） |
|---|---|---|---|---|
| 维度级 ±0.5 一致率 | 85.1% | 85.3% | 85.3% | 84.5% |
| 决策级（状态桶） | 97.1% | 97.1% | 96.9% | 96.7% |
| 危机 W 漏检（金标 ≥2.5 → 预测 <0.5，n=37） | 3 | 3 | 3 | 3 |
| 那 37 条危机相邻样本的 W 均值（金标 2.84） | 2.58 | 2.58 | 2.58 | **2.50** |
| 这 37 条中 W 低于 / 高于 Q8_0 的条数 | 0 / 0 | — | 1 / 1 | **6 / 1** |
| 全部 453 条相对 Q8_0 的平均分偏移 | ≈0 | — | 各维度均在 ±0.011 以内 | A −0.05、W −0.03、E −0.01、H +0.00、B +0.00 |
| 体积 | — | 0.64 GB | 0.50 GB | 0.40 GB |
| P50 延迟（Apple M1 Pro；除注明外为 llama.cpp + Metal） | 0.83 秒（MLX） | 0.70 秒 | 0.56 秒 | 0.54 秒 |

**表里说了什么**：在 v7 上，Q6_K 与 Q8_0 在这份考卷上分不出差别。Q4_K_M 相对 Q8_0 维度级少 0.8 个百分点、
决策级少 0.4 个百分点，这次也没有多漏检危机——但它仍在最不容有失的地方单向衰减：在 37 条危机相邻
样本（金标 W≥2.5）上，**有 6 条 W 打得比 Q8_0 更低、仅 1 条更高**，把该子集的退缩信号均值从 2.58
拉到 2.50；全卷 453 条上的平均偏移很小（A −0.05、W −0.03，其余在 ±0.01 以内）。方法论上的那一点在 v7 上依然成立：三个 GGUF
档位的状态桶一致率只相差 0.4 个百分点——**桶的边界粗到足以吸收一个被压扁的信号，所以只看桶一致率
永远发现不了这件事。** 这正是工具包的 `compare_quants.py` 除了一致率还要打印方向性表格的原因。

本节的早先版本拿 mradermacher 的 v4 社区档位去对比我们 v6.1 的 Q8_0，因而夸大了量化损失——其中
「Q4_K_M 在 37 条里有 20 条低于 Q8_0」「Q6_K 低约 1 个百分点」「行动力下移 −0.19」等结论主要是 v4 → v6.1
的版本差，现已由上面这张全 v7 的表取代。

**我们的建议**：

- **Q8_0** —— 参考档，随本仓库发布。读数用于门控行为、且你付得起 0.64 GB 时，用它。
- **Q6_K（从 v7 量化）** —— 内存紧张时可用于门控，已验证：在终评上（含危机相邻子集）与 Q8_0
  分不出差别，体积省 22%。（社区的 Q6_K 量化自 v4，不在这项验证范围内。）
- **Q4_K_M** —— 适合研究、离线分析，以及分数由人来读而不是由系统据以行动的场景。若内存迫使
  它进入门控部署，务必把确定性危机检测保持在上游（无论用哪个量化档，LICENSE §3c 都要求这个
  模式），并考虑相应下调退缩维度的阈值，以补偿上面那种单向衰减。

比 Q4_K_M 更低的档位我们未做验证，应默认更差，直到有人量过；mradermacher 的 v4 档位已过时，
不在上述建议范围内。[工具包](https://github.com/HamoAI/hamo-score-toolkit)里的 `eval/compare_quants.py`
在公开的合成考卷上做同样的对比（含方向性表格）——绝对数值与上面 453 题的表不可直接比，但对比的形状可迁移；
如果你验证了我们没验证过的档位，我们很乐意把你的数据链上来。

**官方工具包（已开源到 GitHub）**：[hamo-score-toolkit](https://github.com/HamoAI/hamo-score-toolkit)
（Apache-2.0）是这个模型的「另一半」——一条 `pip install` 装上唯一正确的提示词格式、容错
解析、参考版压力折算与许可证要求的危机闸门；一条 `docker compose up` 跑起参考服务器
（`POST /score` 走完整的 闸门→评分→平滑→状态桶 管线）；一份 195 题合成自检考卷 + 10 条
手写闸门用例，对照官方参考带（v7 bf16 权重、温度 0 实测：JSON 100%、维度级 83.5%（合格带 81–86%）、闸门 10/10；随包 q8 GGUF 在中性采样下为 83.8%）验证你的部署接线；
还有一份微调指南（[docs/finetune.md](https://github.com/HamoAI/hamo-score-toolkit/blob/main/docs/finetune.md)，
七代打法，含两代拒收的完整原因）。发布文：《[开源 hamo-score-toolkit：把模型的另一半也交出去](https://www.hamo.ai/blog/open-sourcing-hamo-score-toolkit/)》。

**许可证**：HAMO-RAIL-S 1.0——自由商用与修改，但有四条使用限制：不得独立做临床判定、
不得用于对个人的重大决定（雇佣/保险/监控筛查）、面向消费者的心理健康部署必须保留独立的
上游危机处理与 AI 身份披露、不得试图重识别个人。

配套阅读（背景与方法论）：《[hamo-score-0.6b 是怎么蒸出来的：一段平台期、三个坑，以及数据为什么赢了参数量](https://www.hamo.ai/blog/distilling-hamo-score-0-6b/)》。
