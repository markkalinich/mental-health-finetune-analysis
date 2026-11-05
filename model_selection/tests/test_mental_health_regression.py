"""The gate: funnel.py on the cache must reproduce the locked 23 September mental-health funnel,
except where a rule or the query list was changed on purpose after the lock. Every such change is
named here with the ids it touches, so a surprise anywhere else fails the test.

Locked files: model_selection/tests/locked-2026-09-23/funnel/ and search-query-log.csv.
View under test: --as-of 2026-10-02 (the last day any September artifact was gathered).

Changes after the lock, in the order the funnel applies them:
  queries   tags removed from queries/mental-health.csv shrink the cohort. The ids that only those
            tags returned are computed from the cached 24 September filter answers.
  step 1    I64 beside float weights is a counter, not quantization (5 Oct). The models this lets
            back in are computed from the dtype codes in the locked fp-loss.csv. Their READMEs were
            never fetched before 5 Oct, so in this view they stop at missing:readme.
            pytorch_model.bin repos are no longer cut for file format (5 Oct); their dtypes come
            from a bin header first fetched on 5 Oct, so in this view they stop at missing:bin_header.
  order     September checked text / method / dataset together (method first). Now step 2 is
            text + dataset and the method check comes after the parent check (6 Oct), so September's
            "no_training_method" models with a dataset travel through the parent and config checks;
            the gate requires that none of them is kept.
  step 2    a named dataset must exist on the Hub only from the 2026-10-06 view on
            (rules.DATASET_ON_HUB_FROM); this 2 Oct view must make no dataset lookups and lose
            nothing as dataset_not_on_hub.
  method    "full fine-tune" is a training method; "no LoRA" does not count as LoRA (5 Oct).
            STEP3_RULE lists every id whose outcome moved, with the new outcome.
            A method token in the repo name (lora, qlora, sft, dpo, grpo, ppo, rlhf) counts (6 Oct):
            NAME_METHOD_RULE lists the September no-method models this can let through.
  step 3    parents let back in by the step-1 change need a README not in this view: STEP4_PARENT_FP.
            The child's config.json must match the declared parent (5 Oct): STEP6_LOSS. This check
            was its own step 4 until 9 Oct and is now a loss reason of step 3. The download
            threshold was removed (6 Oct); September's three zero-download models reach the config
            check and stop at missing:config in this view.
  step 4    manual_removals.csv (rows dated 5 Oct or later) must not apply in this 2 Oct view.
  step 5    the method check (after steps 2-4 since 6 Oct); step 6, the objective check, follows it.

Run from the repo root (no pytest in .venv; this is a plain script, pytest-compatible):
    .venv/bin/python model_selection/tests/test_mental_health_regression.py
"""
from __future__ import annotations

import csv
from collections import Counter
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
REPO = PKG.parent
sys.path.insert(0, str(PKG))
import cache  # noqa: E402
import rules  # noqa: E402

LOCKED = REPO / "model_selection/tests/locked-2026-09-23/funnel"
LOCKED_SEARCH_LOG = REPO / "model_selection/tests/locked-2026-09-23/search-query-log.csv"
AS_OF = "2026-10-02"
OUT = REPO / "outputs" / "funnel" / "mental-health" / AS_OF
QUERIES = PKG / "queries" / "mental-health.csv"

# step 3 rule change, 5 Oct: new outcome per id. A value starting with "missing:" means the model
# now goes further than the locked rules took it and needs an artifact first fetched on 5 Oct;
# any outcome at that step or later is accepted for it in this view.
STEP3_RULE = {
    # "no LoRA" no longer counts as LoRA; this card's only LoRA mention was negated
    "Abdu-GH/AraRest-Arabic-Restaurant-Reviews-Sentiment-Analysis": "no_training_method",
    # "full fine-tune" now counts as a method
    "HiyawErtiro/cryptobert-finetuned_on_news_headlines": "no_dataset",
    "ZenyxS/indobert-emotion-emotionclf": "no_dataset",
    "damian-shivihs/yllia-safety-classifier": "no_dataset",
    "mohsinakh/roberta-base-sst2-sentiment": "no_dataset",
    "pixasocial/survival-uncensored-gemma-270m": "no_dataset",
    "ryousuf569/finbert-macro": "no_dataset",
    "tadiecool29/MTL-FullFineT-mt5-base-joint": "no_dataset",
    "tadiecool29/MTL-FullFineTune-afri-mt5-base-joint": "no_dataset",
    "Aniemore/hubert-emotion-russian-resd": "parent_not_fp",
    "Aniemore/unispeech-sat-emotion-russian-resd": "parent_not_fp",
    "Aniemore/wav2vec2-emotion-russian-resd": "parent_not_fp",
    "Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition": "parent_not_fp",
    "Aniemore/wavlm-emotion-russian-resd": "parent_not_fp",
    "Rasyy/indobert_multiclass_emotion_classifier_for_indonesian_e_commerce_reviews": "parent_not_fp",
    "dzilann/indobert_multiclass_emotion_classifier_for_indonesian_e_commerce_reviews": "parent_not_fp",
    "AnkitAI/FinSense-ModernBERT-Financial-News-Sentiment-Analysis": "parent_pretrained",
    "AnkitAI/Sensible-ModernBERT-Sentiment-Analysis": "parent_pretrained",
    "AnkitAI/distilbert-base-uncased-financial-news-sentiment-analysis": "parent_pretrained",
    "efeyol11/bert-turkish-sentiment": "parent_not_stated",
    "Sidharthan/roberta-base-conv-emotion": "missing:parent_readme",
    "dzur658/smollm2-mentalhealth-360m": "missing:config",
    "dzur658/smollm2-mentalhealth-360m-V2": "missing:config",
}
# step 1 change applied to the parent: these children's parents were cut for I64 and are now full
# precision; the parent README was first fetched on 5 Oct.
STEP4_PARENT_FP = {
    "AlexStamp/roberta-base-finetuned-yelp-ratings",
    "Amirhossein75/multi-label-emotion-classification-reddit-comments-roberta",
    "Burhan21/roberta-lora-sentiment",
    "ilkayO/yildizsezar-convbert",
    "jihun-pae/nsmc-sentiment-lora",
    "keerthi1515/roberta-sentiment-rotten-tomatoes",
    "mishrabp/roberta-sentiment-analysis-merged",
}
# parents whose weights are pytorch_model.bin: cut as parent_not_fp in September, now wait for the
# parent's bin header (first fetched 5 Oct)
STEP4_PARENT_BIN = {
    "ISuhaibM/suhaib-mental-health-chatbot": "missing:parent_bin_header",   # microsoft/DialoGPT-medium
    "mario-rc/multi-domain-rm-qwen-3-nemotron-8b-it": "missing:parent_bin_header",  # nvidia/Qwen3-Nemotron-8B-BRRM
}
# step 1, 10 Oct: rules.ROOT_CKPT also matches the Qwen3.5 shard name model.safetensors-N-of-M.safetensors.
# September cut these as no_root without reading the dtype summary; in this view they pass step 1 and
# are judged by the later steps (Mochi-2B is an image-text-to-text model and stops at step 2).
STEP1_SHARD_NAME = {"PinkPixel/Mochi-2B": "vision_or_video"}
STEP6_LOSS = {
    # card says Gemma 2 2B-it; weights are Gemma 1 2B (18 layers, hidden 2048)
    "JaeJiMin/daily_hug": "parent_discordant",
    # card says Llama 3 8B-Instruct; weights have the Llama 2 vocabulary (32,000)
    "menzo-ai/mental-health-chatbot": "parent_discordant",
}
# September "no training method" models whose repo name carries a method token; the repo-name
# rule (6 Oct) may keep these and no other September no-method model.
NAME_METHOD_RULE = {
    "Amod/mental-health-therapy-mistral-7b-ins-SFT",
    "Minakshee25/Empathetic-SmolLM2-LoRA",
    "Mostafa8Mehrabi/llama-1b-pruned-3blocks-bi-Insomnia-ChatBot-SFT-CoT-merged",
    "Mostafa8Mehrabi/llama-1b-pruned-3blocks-taylor-Insomnia-ChatBot-SFT-CoT-v1-merged",
    "Mostafa8Mehrabi/llama-3.2-1b-Insomnia-ChatBot-R1CoT-GRPO-450-steps-merged",
    "Mostafa8Mehrabi/llama-3.2-1b-Insomnia-ChatBot-SFT-CoT-merged",
    "Mostafa8Mehrabi/llama-3.2-3b-Insomnia-ChatBot-SFT-CoT-merged",
    "TVRRaviteja/llama3.1-mental-health-therapy-SFT",
    "XformAI-india/mentalhealth-llama-1b-GRPO",
    "YUGOROU/Counseling-Guardrail-GRPO",
    "abhay2727/emotional_response_model_SFT_t5Small",
    "aidev08/phi-3-mini-4k-instruct-qlora-mental_health_counseling_conversations",
    "imminsik/safe-rlhf-qr-empathy-alpaca-8b-reproduced-llama-3",
    "insomnia-ye/deepscaler_qwen2.5_7b_8k_rpe_grpo_yyx_0723-it570",
    "sidhusarkar/smollm-135m-empathy-sft-then-dpo",
    "sirev/Qlora-lfm2-700m-mental-health",
    "tester2k2/gemma-3n-e2b-mental-health-finedtuned-sft",
    "zbt566666/qwen2.5-7b-mental-therapy-lora-sft",
    "ziadashraf98765/roberta-depression-detection-lora-merged",
}
STEP_OF = {"missing:readme": "5", "missing:parent_readme": "3", "missing:parent_bin_header": "3", "missing:config": "3"}
CONFIG_LOSSES = {"parent_discordant", "config_unreadable", "repo_gated", "missing:config", "missing:parent_config"}
METHOD_STEP = "5"

csv.field_size_limit(sys.maxsize)


def ids(path: Path) -> set:
    return {ln.strip() for ln in path.read_text().splitlines() if ln.strip()}


def rows(path: Path) -> list:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def search_ids(kind: str, term: str) -> set:
    path = cache.newest_search(kind, term, AS_OF)
    assert path is not None, f"no cached {kind} answer for {term!r} on or before {AS_OF}"
    return {r["hf_id"] for r in rows(path)}


def removed_only_ids() -> set:
    """Ids that only the terms dropped from queries/mental-health.csv since the lock returned."""
    current = {(r["kind"], r["term"]) for r in rows(QUERIES) if r["added_on"] <= AS_OF}
    locked = {("search", r["term"]) for r in rows(LOCKED_SEARCH_LOG)}
    locked |= {("filter", r["tag"]) for r in rows(LOCKED / "filter-query-log.csv")}
    assert current <= locked, f"terms added with added_on <= {AS_OF}: {sorted(current - locked)}"
    gone = set().union(*(search_ids(k, t) for k, t in locked - current)) if locked - current else set()
    stay = set().union(*(search_ids(k, t) for k, t in current))
    return gone - stay


def readmitted_by_i64() -> set:
    """Locked step-1 losses the I64 rule lets back in: float weights plus I64, nothing else."""
    out = set()
    for r in rows(LOCKED / "fp-loss.csv"):
        codes = set(r["dtype_codes"].split(";")) if r["dtype_codes"] else set()  # locked file uses ';'
        if r["reason"] == "other_dtype" and codes & rules.OK_DTYPES and codes <= rules.OK_DTYPES | rules.BUFFER_DTYPES:
            out.add(r["hf_id"])
    return out


def bin_only_models(cohort_hint: set) -> set:
    """Locked step-1 losses whose dtypes are now read from the file header: no_root rows whose
    weights are root pytorch_model.bin files (header first fetched 5 Oct), and blank_record rows
    whose root safetensors shards have no Hub dtype summary (header first fetched 9 Oct). In this
    2 Oct view both stop at missing:bin_header."""
    cards = cache.load_cards(AS_OF)
    out = set()
    for r in rows(LOCKED / "fp-loss.csv"):
        if r["reason"] in ("no_root", "blank_record") and r["hf_id"] in cohort_hint:
            row = cards.get(r["hf_id"].lower())
            if row is not None and rules.header_files(row):
                out.add(r["hf_id"])
    return out


def run_funnel(allowed_missing: set) -> list:
    proc = subprocess.run(
        [sys.executable, str(PKG / "funnel.py"), "--grouping", "mental-health", "--as-of", AS_OF],
        capture_output=True, text=True,
    )
    assert proc.returncode in (0, 1), f"funnel.py exit {proc.returncode}\n{proc.stdout}\n{proc.stderr}"
    missing = rows(OUT / "missing.csv")
    unexplained = sorted({m["needed_for"] for m in missing} - allowed_missing)
    assert not unexplained, f"cache misses for ids no rule change explains: {unexplained[:10]}"
    return rows(OUT / "decisions.csv")


def kept_after(decisions: list, step: str) -> set:
    """Models that passed the given step."""
    return {d["hf_id"] for d in decisions if d["step"] > step or (d["step"] == step and d["decision"] == "kept")}


def lost_at(decisions: list, step: str) -> dict:
    return {d["hf_id"]: d["decision"] for d in decisions if d["step"] == step and d["decision"] != "kept"}


def check_sets(label: str, got: set, want: set) -> None:
    assert got == want, f"{label}: {len(got)} vs expected {len(want)}; only_new={sorted(got - want)[:5]} only_expected={sorted(want - got)[:5]}"


def check_reasons(label: str, got: dict, want: dict) -> None:
    assert set(got) == set(want), f"{label}: ids differ; only_new={sorted(set(got) - set(want))[:5]} only_expected={sorted(set(want) - set(got))[:5]}"
    diff = {k: (got[k], want[k]) for k in got if got[k] != want[k]}
    assert not diff, f"{label}: reasons differ for {len(diff)} ids, e.g. {list(diff.items())[:5]}"


def check_pinned(label: str, decisions: dict, pinned: dict, removed: set) -> None:
    for hf_id, want in pinned.items():
        d = decisions.get(hf_id)
        if d is None:
            assert hf_id in removed, f"{label}: {hf_id} not in cohort and no removed tag explains it"
            continue
        got = d["decision"]
        if got == want:
            continue
        if want == "no_training_method" and got != "kept" and (d["step"] != METHOD_STEP or got == want):
            continue  # the method check is now last; the model may be cut earlier for another reason
        if want.startswith("missing:") and d["step"] >= STEP_OF[want]:
            continue  # the artifact has since been fetched; the model went further
        raise AssertionError(f"{label}: {hf_id}: {got} vs pinned {want}")


def test_regression() -> None:
    removed = removed_only_ids()
    readmitted = readmitted_by_i64() | set(STEP1_SHARD_NAME)
    locked_cohort = ids(LOCKED / "keyword-ids.txt")
    bin_only = bin_only_models(locked_cohort - removed)
    moved = set(STEP3_RULE) | STEP4_PARENT_FP | set(STEP4_PARENT_BIN)
    dataset_named = {r["hf_id"] for r in rows(LOCKED / "dataset-structured.csv") if r["dataset_named"] == "named"}
    want2, no_method = {}, set()
    for r in rows(LOCKED / "documented-loss.csv"):
        if r["reason"] == "vision_or_video" or r["hf_id"] not in dataset_named:
            want2[r["hf_id"]] = "vision_or_video" if r["reason"] == "vision_or_video" else "no_dataset"
        else:
            assert r["reason"] == "no_training_method", r
            no_method.add(r["hf_id"])
    zero_downloads = {r["hf_id"] for r in rows(LOCKED / "downloads-loss.csv")}
    decisions = run_funnel(allowed_missing=readmitted | moved | bin_only | no_method | zero_downloads)
    by_id = {d["hf_id"]: d for d in decisions}

    # cohort: the locked ids minus those only a removed tag returned
    check_sets("cohort", set(by_id), locked_cohort - removed)
    in_view = lambda s: {h for h in s if h in by_id}  # noqa: E731

    # step 1: locked outcome, plus the I64 readmissions; .bin models now wait for their header
    readmitted_here = in_view(readmitted)
    check_sets("step 1 kept", kept_after(decisions, "1"), in_view(ids(LOCKED / "fp-kept.txt")) | readmitted_here)
    want1 = {r["hf_id"]: r["reason"] for r in rows(LOCKED / "fp-loss.csv") if r["hf_id"] not in readmitted}
    for h in bin_only:
        want1[h] = "missing:bin_header"
    check_reasons("step 1 loss", lost_at(decisions, "1"), {k: v for k, v in want1.items() if k in by_id})
    for h in readmitted_here:
        assert by_id[h]["step"] >= "2", f"readmitted {h} still at step {by_id[h]['step']}"
    check_pinned("step 1 shard name", by_id, STEP1_SHARD_NAME, removed)

    # steps 2-6 on the September step-1 survivors, minus the ids a named rule change moved
    legacy = in_view(ids(LOCKED / "fp-kept.txt")) - moved
    sub = lambda s: {h for h in s if h in legacy}  # noqa: E731
    subd = lambda d: {h: v for h, v in d.items() if h in legacy}  # noqa: E731

    # September applied text / method / dataset as one step, method before dataset. Now the dataset
    # check is step 2 and the method check is step 5, so a September "no_training_method"
    # model with a dataset goes on through the parent and config checks and must end either cut there
    # or at step 5 as no_training_method; it must never be kept.
    check_reasons("step 2 loss", subd(lost_at(decisions, "2")), subd(want2))
    # the dataset-exists rule is dated 2026-10-06: this view must neither apply it nor look anything up
    assert AS_OF < rules.DATASET_ON_HUB_FROM, f"gate view {AS_OF} is on or after DATASET_ON_HUB_FROM; re-lock the gate"
    assert not [d for d in decisions if d["decision"] in ("dataset_not_on_hub", "missing:dataset")], \
        "dataset-exists rule applied in the 2 Oct view"
    assert all(not d["dataset_hub_status"] for d in decisions), "dataset lookups recorded in the 2 Oct view"
    name_kept = set()
    for h in sub(no_method):
        d = by_id[h]
        if d["decision"] == "kept":
            assert h in NAME_METHOD_RULE, f"{h} had no training method in September and is now kept"
            assert all(part.split(": ", 1)[1].startswith("name ") for part in d["method_evidence"].split("; ")), \
                f"{h}: kept on evidence beyond the repo name: {d['method_evidence']}"
            name_kept.add(h)
        elif d["step"] == METHOD_STEP:
            assert d["decision"] == "no_training_method", f"{h}: {d['decision']} at step {METHOD_STEP}"
    documented = sub(ids(LOCKED / "documented-kept.txt"))
    check_sets("step 2 kept", sub(kept_after(decisions, "2")), documented | sub(no_method))
    docd = lambda d: {h: v for h, v in d.items() if h in documented}  # noqa: E731
    doc = lambda s: {h for h in s if h in documented}  # noqa: E731

    # step 3 (parent, then config) on the September documented set. Step 3 now holds two kinds of
    # loss: the parent checks (September's step 3) and the config check (September had none; it
    # was step 4 from 5 to 9 Oct). Split them so each half is compared with its own locked file.
    lost3 = docd(lost_at(decisions, "3"))
    lost3_parent = {h: v for h, v in lost3.items() if v not in CONFIG_LOSSES}
    lost3_config = {h: v for h, v in lost3.items() if v in CONFIG_LOSSES}
    locked_ins = rows(LOCKED / "instruct-parent-kept.csv")
    passed_parent = doc(kept_after(decisions, "3")) | set(lost3_config)
    check_sets("step 3 parent kept", passed_parent, doc({r["hf_id"] for r in locked_ins}))
    parents = {h: by_id[h]["parent"] for h in passed_parent}
    check_reasons("step 3 parent id", parents, {r["hf_id"]: r["parent"] for r in locked_ins if r["hf_id"] in documented})
    want3 = {r["hf_id"]: r["reason"] for r in rows(LOCKED / "parent-loss.csv")}
    want3.update({r["hf_id"]: r["reason"] for r in rows(LOCKED / "instruct-parent-loss.csv")})
    check_reasons("step 3 parent loss", lost3_parent, docd(want3))

    # the named rule changes land exactly where they were reviewed to land
    check_pinned("step 3 rule", by_id, STEP3_RULE, removed)
    check_pinned("step 3 parent fp", by_id, {h: "missing:parent_readme" for h in STEP4_PARENT_FP}, removed)
    check_pinned("step 3 parent bin", by_id, STEP4_PARENT_BIN, removed)

    # config check on the September parent survivors. The download threshold is gone (6 Oct), so
    # the three September zero-download models now reach this check; their config.json was never
    # fetched for this view, so they stop at missing:config.
    want_cfg = dict(STEP6_LOSS)
    want_cfg.update({h: "missing:config" for h in doc(zero_downloads)})
    check_reasons("step 3 config loss", lost3_config, docd(want_cfg))
    check_sets("step 3 kept", doc(kept_after(decisions, "3")), doc(ids(LOCKED / "final-kept.txt")) - set(STEP6_LOSS))

    # step 4: the manual removals are dated 5 Oct or later, so this 2 Oct view must not apply them
    check_reasons("step 4 loss", lost_at(decisions, "4"), {})
    # step 5: every September documented model names a method, so none is lost here
    check_reasons("step 5 loss", docd(lost_at(decisions, METHOD_STEP)), {})
    check_sets("step 5 kept", doc(kept_after(decisions, METHOD_STEP)), doc(kept_after(decisions, "3")))
    # step 6 (added 10 Oct): every objective-evidence row is dated 2026-10-09 or later, so in this
    # 2 Oct view no model has a row and all step-5 survivors stop here as no_objective_evidence.
    at6 = [d for d in decisions if d["step"] == "6"]
    assert at6 and all(d["decision"] == "no_objective_evidence" for d in at6), \
        f"step 6 in the 2 Oct view: {Counter(d['decision'] for d in at6)}"

    print(f"OK: cohort {len(by_id)} (locked {len(locked_cohort)} minus {len(removed)} from removed tags); "
          f"step 1 {len(kept_after(decisions, '1'))} ({len(readmitted_here)} readmitted by the I64 rule; "
          f"{len(bin_only)} .bin models await a header); {len(sub(no_method))} September no-method models, "
          f"{len(name_kept)} kept by the repo-name rule; September survivors: {len(documented)} / {len(passed_parent)} / "
          f"{len(doc(kept_after(decisions, '3')))} / {len(doc(kept_after(decisions, METHOD_STEP)))} match; "
          f"{len(STEP3_RULE)} step-3 and {len(STEP4_PARENT_FP)} parent rule moves pinned")


if __name__ == "__main__":
    test_regression()
