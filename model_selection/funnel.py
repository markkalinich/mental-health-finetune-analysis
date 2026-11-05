"""Build one grouping's funnel from the cache.

    .venv/bin/python model_selection/funnel.py --grouping mental-health --as-of 2026-10-02

Reads queries/<grouping>.csv (a query counts only if its added_on is on or before --as-of),
takes the newest cache entry on or before --as-of (and, with --since, not older than that)
for every search, card, README, config.json, bin header, and dataset lookup it needs, applies
rules.py, and writes
outputs/funnel/<grouping>/<as-of>/:

  decisions.csv   one row per cohort model: where it stopped and the evidence
  kept.csv        the survivors of the grouping's endpoint step (step 6 for every grouping): the set the study uses
  kept_after_review.csv   survivors of step 4 (manual review); kept_method_stated.csv: of step 5; kept_objective_known.csv: of step 6.
                          kept.csv is whichever of these is the grouping's endpoint (FINAL_STEP_BY_GROUPING).
  counts.csv      entered / kept / each loss reason per step; catalog size
  missing.csv     cache entries the run needed and did not have (kind, key, needed_for)
  provenance.csv  per artifact type: how many used, real date range, date_source

Steps: 1 full precision, 2 text-capable with a dataset named that exists on the Hub (the
existence check applies to views dated 2026-10-06 or later; see rules.DATASET_ON_HUB_FROM),
3 one declared full-precision instruction parent whose config.json describes the same network
as the child's (architecture, vocab size, hidden size, layers; until 9 Oct this config check was
its own step 4), 4 not on the human-decided removal list manual_removals.csv (grouping, hf_id,
decided_on, category, reason; a row counts only once its decided_on date has passed, like a
query), 5 fine-tuning method stated in the README, tags, or repo name, 6 training objective known at
evidence level 1 or 2 (decisions/objective-evidence.csv). Step 6 is the endpoint (kept.csv). A removed
model is decision manual_removed; counts.csv records one step-4 loss per category as
manual_removed: <category>. Every row that applies must name a model that reached step 4;
otherwise the run exits 2. There is no download threshold (removed 6 Oct).

--relax {dataset,method,parent_instruction,parent} switches one rule off for a sensitivity run
and writes to outputs/funnel/<grouping>/sensitivity/<as-of>__relax-<rule>/ instead (see RELAX).

Exit 0 when nothing is missing. Exit 1 when missing.csv is non-empty and --fetch was
not given (decisions are still written; a model that hit a miss carries decision
"missing:<kind>"). With --fetch, hub.fill writes the misses under today's date and
the pass repeats until nothing is missing. If a pass leaves the same keys missing,
the run exits 2. No Hub call without --fetch.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import cache
import rules

RESULTS = cache.RESULTS
QUERIES = cache.ROOT / "queries"
MANUAL = cache.ROOT / "manual_removals.csv"
MANUAL_FIELDS = ["grouping", "hf_id", "decided_on", "category", "reason"]
ACCESSIBLE = cache.ROOT / "accessible_data.csv"
ACCESSIBLE_FIELDS = ["grouping", "hf_id", "decided_on", "data_name", "access_url", "access"]
ACCESS_KINDS = {"file_opened", "kaggle_page", "hub_dataset"}
# Three more decision files, all dated per row so an earlier --as-of view is unchanged (added 9 Oct 2026):
#   parents.csv          the class of every parent that reaches step 3, read by an agent from the
#                        parent's own card and confirmed by a person; overrides the regex class
#   dataset_aliases.csv  an informal dataset name on a card -> the Hub dataset id that holds it,
#                        with the evidence; only rows with confirmed_by filled are used
#   agent_methods.csv    the training objective and update scope an agent read from the card,
#                        preprint, or training script (collect_extractions.py writes it); counts
#                        at step 5 beside the card-text regex
PARENTS = cache.ROOT / "parents.csv"
PARENTS_FIELDS = ["parent_id", "class", "base_repo", "evidence_url", "quote", "decided_by", "decided_on"]
PARENT_CLASSES = {"instruction", "pretrained", "finetune", "not_a_language_model", "unreadable"}
ALIASES = cache.ROOT / "dataset_aliases.csv"
ALIASES_FIELDS = ["card_name", "hub_id", "evidence_url", "quote", "checked_on", "confirmed_by"]
AGENT_METHODS = cache.ROOT / "agent_methods.csv"
AGENT_METHODS_FIELDS = ["grouping", "hf_id", "decided_on", "objective", "update_scope", "source_url", "source"]
NOT_STATED = {"", "not stated", "none", "null"}
# Step 6 (10 Oct 2026, Mark's rule): the training objective must be stated (evidence level 1) or inferred
# from the author's own words or toolchain (level 2). Level 3 (assumed from the data format alone) is out.
# One file per grouping, written after the step-5 survivors are read by hand and validated by an agent:
#   docs/<grouping>_FT_funnel/decisions/objective-evidence.csv
# Columns: hf_id, objective, stages, evidence_level, basis, decided_by, decided_on (dated per row).
OBJECTIVE_FIELDS = ["hf_id", "objective", "stages", "evidence_level", "basis", "decided_by", "decided_on"]
STEPS = ("1", "2", "3", "4", "5", "6")
MANUAL_STEP = "4"
METHOD_STEP = "5"
OBJECTIVE_STEP = "6"
# The study's endpoint per grouping: the step whose survivors are kept.csv. Mental health and safety moved to
# step 6 on 10 Oct 2026 (safety 11:34, Mark: "make it match MH"); medical on 13 Oct 2026.
FINAL_STEP_BY_GROUPING = {"mental-health": OBJECTIVE_STEP, "safety": OBJECTIVE_STEP, "medical": OBJECTIVE_STEP}
DEFAULT_FINAL_STEP = MANUAL_STEP
# --relax: switch one rule off for a sensitivity run (results go to sensitivity/<as-of>__relax-<rule>/).
RELAX = {
    "dataset": "step 2: a dataset need not be named (nor exist on the Hub)",
    "parent_instruction": "step 3: the parent need not be instruction-tuned (still exactly one, full precision, readable)",
    "parent": "step 3: a model with no usable parent (none, several, not full precision, unreadable) "
              "skips the parent and config checks; a readable parent is still checked for class",
}
NO_USABLE_PARENT = {"no_parent", "multiple_parents", "parent_not_fp", "parent_unreadable"}

DECISION_FIELDS = [
    "hf_id", "url", "decision", "step", "query_terms", "fp_reason", "weights_format", "dtype_codes", "pipeline_tag", "methods",
    "method_evidence", "dataset_source", "datasets", "dataset_hub_status", "parent", "parent_url", "parent_source_field", "parent_status",
    "parent_fp_reason", "parent_class", "parent_class_source", "parent_class_evidence", "parent_config_check",
    "downloads", "objective", "objective_stages", "objective_evidence_level", "manual_category", "manual_reason", "card_screened_at", "readme_file", "parent_card_screened_at", "parent_readme_file",
    "config_file", "parent_config_file",
]
# Columns for the hand-review table of kept models (kept.csv): a link for every model, what
# brought it in, and the exact text each rule matched so the reviewer checks a sentence, not a README.
KEPT_FIELDS = [
    "hf_id", "url", "query_terms", "pipeline_tag", "weights_format", "dtype_codes", "methods", "method_evidence",
    "dataset_source", "datasets", "dataset_hub_status", "parent", "parent_url", "parent_source_field", "parent_class_source",
    "parent_class_evidence", "parent_config_check", "downloads", "objective", "objective_stages", "objective_evidence_level",
]
HUB = "https://huggingface.co/"
PARENT_CLASS_REASON = {
    "pretrained": "parent_pretrained",
    "finetune": "parent_finetune",
    "not_stated": "parent_not_stated",
    "unreadable": "parent_card_unreadable",
    "conflict": "parent_conflict",
    "not_a_language_model": "parent_not_language_model",
}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(2)


def read_csv(path: Path) -> list:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, fields: list, rows: list) -> None:
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


class Run:
    def __init__(self, grouping: str, as_of: str, since: str = "", relax: str = "") -> None:
        self.grouping = grouping
        self.as_of = as_of
        self.since = since
        if relax and relax not in RELAX:
            fail(f"--relax must be one of {sorted(RELAX)}")
        self.relax = relax
        # A query counts only once its added_on date has passed: a term added later must not
        # change what an earlier --as-of run sees.
        self.queries = [q for q in read_csv(QUERIES / f"{grouping}.csv") if q["added_on"] <= as_of]
        if not self.queries:
            fail(f"no queries for {grouping} with added_on <= {as_of}")
        self.missing: list = []
        self.used: dict = {"search": set(), "card": set(), "readme": set(), "config": set(), "bin_header": set(),
                           "dataset": set()}
        self.cards = cache.load_cards(as_of, since)
        self.terms_of: dict = {}
        self.manual = self.load_manual()
        self.accessible = self.load_accessible()
        self.parents = self.load_parents()
        self.aliases = self.load_aliases()
        self.agent_methods = self.load_agent_methods()
        self.objective = self.load_objective()
        self.final_step = FINAL_STEP_BY_GROUPING.get(self.grouping, DEFAULT_FINAL_STEP)
        self.unregistered_parents: dict = {}

    def _load_dated(self, path: Path, fields: list, key: str, date_col: str, grouping_col: str = "",
                    required: tuple = ()) -> dict:
        """Rows of a decision CSV whose date is on or before --as-of (and whose grouping matches,
        when the file has one), keyed by lower-case `key`. Columns must match exactly; the columns
        in `required` must be filled; a key listed twice stops the run."""
        if not path.exists():
            return {}
        rows = read_csv(path)
        bad = [r for r in rows if list(r) != fields or not all((r[k] or "").strip() for k in required)]
        if bad:
            fail(f"{path.name}: columns must be {fields} and {list(required)} filled; bad rows: {bad[:3]}")
        out: dict = {}
        for r in rows:
            if grouping_col and r[grouping_col] != self.grouping:
                continue
            if r[date_col] > self.as_of:
                continue
            k = r[key].lower()
            if k in out:
                fail(f"{path.name}: {r[key]} listed twice")
            out[k] = r
        return out

    def load_parents(self) -> dict:
        rows = self._load_dated(PARENTS, PARENTS_FIELDS, "parent_id", "decided_on",
                                required=("parent_id", "class", "evidence_url", "decided_by", "decided_on"))
        bad = [r["parent_id"] for r in rows.values() if r["class"] not in PARENT_CLASSES]
        if bad:
            fail(f"{PARENTS.name}: class must be one of {sorted(PARENT_CLASSES)}; bad: {bad}")
        return rows

    def load_aliases(self) -> dict:
        rows = self._load_dated(ALIASES, ALIASES_FIELDS, "card_name", "checked_on",
                                required=("card_name", "hub_id", "evidence_url", "checked_on"))
        unconfirmed = [k for k, r in rows.items() if not (r["confirmed_by"] or "").strip()]
        if unconfirmed:
            print(f"note: {ALIASES.name}: {len(unconfirmed)} alias row(s) not yet confirmed and not used: {unconfirmed}",
                  file=sys.stderr)
        return {k: r for k, r in rows.items() if (r["confirmed_by"] or "").strip()}

    def load_objective(self) -> dict:
        path = cache.ROOT.parent / "docs" / f"{self.grouping.replace('-', '_')}_FT_funnel" / "decisions" / "objective-evidence.csv"
        if not path.exists():
            return {}
        rows = self._load_dated(path, OBJECTIVE_FIELDS, "hf_id", "decided_on")
        for r in rows.values():
            if r["evidence_level"][:1] not in {"1", "2", "3"}:
                fail(f"{path.name}: {r['hf_id']}: evidence_level must start with 1, 2, or 3, got {r['evidence_level']!r}")
        return rows

    def load_agent_methods(self) -> dict:
        return self._load_dated(AGENT_METHODS, AGENT_METHODS_FIELDS, "hf_id", "decided_on", grouping_col="grouping",
                                required=("grouping", "hf_id", "decided_on", "source"))

    def load_manual(self) -> dict:
        """Human-decided removals for this grouping whose decided_on is on or before --as-of,
        keyed by lower-case hf_id. Every row needs all five fields; otherwise exit 2."""
        if not MANUAL.exists():
            return {}
        rows = read_csv(MANUAL)
        bad = [r for r in rows if list(r) != MANUAL_FIELDS or not all((r[k] or "").strip() for k in MANUAL_FIELDS)]
        if bad:
            fail(f"{MANUAL.name}: columns must be {MANUAL_FIELDS} and every field filled; bad rows: {bad}")
        out: dict = {}
        for r in rows:
            if r["grouping"] == self.grouping and r["decided_on"] <= self.as_of:
                if r["hf_id"].lower() in out:
                    fail(f"{MANUAL.name}: {r['hf_id']} listed twice for {self.grouping}")
                out[r["hf_id"].lower()] = r
        return out

    def load_accessible(self) -> dict:
        """Models whose training data were opened, for this grouping, decided_on on or before --as-of.
        A row is an explicit admission. It is not a guess from a dataset name. Every field filled."""
        if not ACCESSIBLE.exists():
            return {}
        rows = read_csv(ACCESSIBLE)
        bad = [r for r in rows if list(r) != ACCESSIBLE_FIELDS or not all((r[k] or "").strip() for k in ACCESSIBLE_FIELDS)
               or r["access"] not in ACCESS_KINDS]
        if bad:
            fail(f"{ACCESSIBLE.name}: columns must be {ACCESSIBLE_FIELDS}, every field filled, "
                 f"access one of {sorted(ACCESS_KINDS)}; bad rows: {bad}")
        out: dict = {}
        for r in rows:
            if r["grouping"] == self.grouping and r["decided_on"] <= self.as_of:
                if r["hf_id"].lower() in out:
                    fail(f"{ACCESSIBLE.name}: {r['hf_id']} listed twice for {self.grouping}")
                out[r["hf_id"].lower()] = r
        return out

    def admit_accessible(self, d: dict, row: dict) -> None:
        prior = d["dataset_hub_status"]
        mark = f"accessible={row['access']}:{row['data_name']}"
        d["dataset_source"] = "accessible_data"
        d["datasets"] = row["data_name"]
        d["dataset_hub_status"] = f"{prior};{mark}" if prior else mark

    # -------------------------------------------------------------- lookups
    def miss(self, kind: str, key: str, needed_for: str, detail: str = "") -> None:
        self.missing.append({"kind": kind, "key": key, "needed_for": needed_for, "detail": detail})

    def card(self, hf_id: str, needed_for: str):
        row = self.cards.get(hf_id.lower())
        if row is None:
            self.miss("card", hf_id, needed_for)
            return None
        self.used["card"].update(cache.card_files(row["screened_at"][:10]))
        return row

    def readme(self, hf_id: str, needed_for: str):
        path = cache.newest_readme(hf_id, self.as_of, self.since)
        if path is None:
            self.miss("readme", hf_id, needed_for)
            return None, ""
        self.used["readme"].add(path)
        return path.read_text(errors="replace"), path.name

    def config(self, hf_id: str, needed_for: str):
        path = cache.newest_config(hf_id, self.as_of, self.since)
        if path is None:
            self.miss("config", hf_id, needed_for)
            return None, ""
        self.used["config"].add(path)
        return path.read_text(errors="replace"), path.name

    def dataset_status(self, name: str, needed_for: str):
        path = cache.newest_dataset(name, self.as_of, self.since)
        if path is None:
            self.miss("dataset", name, needed_for)
            return None
        self.used["dataset"].add(path)
        return json.loads(path.read_text(errors="replace")).get("status", "")

    def precision(self, row: dict, needed_for: str) -> tuple:
        """rules.full_precision with the file header looked up when the dtypes are not on the card:
        root .bin shards, or root safetensors shards whose Hub dtype summary is blank."""
        needed = rules.header_files(row)
        header = None
        if needed:
            path = cache.newest_bin_header(row["hf_id"], self.as_of, self.since)
            if path is None:
                self.miss("bin_header", row["hf_id"], needed_for, "|".join(needed))
                return "missing:bin_header", ""
            self.used["bin_header"].add(path)
            header = path.read_text(errors="replace")
        return rules.full_precision(row, header)

    def cohort(self) -> list:
        ids: set = set()
        self.terms_of = {}
        for q in self.queries:
            path = cache.newest_search(q["kind"], q["term"], self.as_of, self.since)
            if path is None:
                self.miss(f"search:{q['kind']}", q["term"], "cohort")
                continue
            self.used["search"].add(path)
            for hf_id in cache.read_ids(path):
                ids.add(hf_id)
                self.terms_of.setdefault(hf_id, set()).add(f"{q['kind']}:{q['term']}")
        return sorted(ids)

    # -------------------------------------------------------------- one model
    def decide(self, hf_id: str) -> dict:
        d = {k: "" for k in DECISION_FIELDS}
        d["hf_id"] = hf_id
        d["url"] = HUB + hf_id
        d["query_terms"] = "|".join(sorted(self.terms_of.get(hf_id, ())))

        def stop(step: int, decision: str) -> dict:
            d["step"], d["decision"] = str(step), decision
            return d

        row = self.card(hf_id, hf_id)
        if row is None:
            return stop(1, "missing:card")
        d["card_screened_at"] = row["screened_at"]
        d["pipeline_tag"] = (row.get("pipeline_tag") or "").strip()
        d["downloads"] = (row.get("downloads") or "").strip()

        # step 1: full precision
        d["fp_reason"], d["dtype_codes"] = self.precision(row, hf_id)
        d["weights_format"] = "bin" if rules.root_bin_files(row) else "safetensors"
        if d["fp_reason"] != "keep":
            return stop(1, d["fp_reason"])

        # step 2: text-capable and a dataset named (card fields only; no README needed).
        # From ACCESSIBLE_FROM, a Python-list tag is the repo id inside it, and a row in
        # accessible_data.csv keeps a model whose training file or dataset page was opened.
        named, d["dataset_source"], d["datasets"] = rules.named_datasets(row)
        if self.as_of >= rules.ACCESSIBLE_FROM:
            expanded = rules.expand_dataset_lists(d["datasets"])
            if expanded != d["datasets"]:
                d["datasets"] = expanded
                if expanded:
                    named = "named"
        # dataset_aliases.csv: an informal name on the card (GoEmotions, esconv, mentalchat-16k) is
        # replaced by the Hub id that holds that corpus, so the Hub-exists check below sees it.
        if self.aliases and d["datasets"]:
            pieces, aliased = [], []
            for name in d["datasets"].split(";"):
                a = self.aliases.get(name.lower())
                if a is not None and a["hub_id"].lower() != name.lower():
                    pieces.append(a["hub_id"])
                    aliased.append(f"{name}->{a['hub_id']}")
                else:
                    pieces.append(name)
            if aliased:
                d["datasets"] = ";".join(pieces)
                d["dataset_source"] = (d["dataset_source"] + "+alias") if d["dataset_source"] else "alias"
                d["dataset_hub_status"] = "alias:" + ",".join(aliased)
        if d["pipeline_tag"] in rules.VISION:
            return stop(2, "vision_or_video")
        admitted = self.accessible.get(hf_id.lower()) if self.as_of >= rules.ACCESSIBLE_FROM else None
        if named != "named" and self.relax != "dataset":
            if admitted is None:
                return stop(2, "no_dataset")
            self.admit_accessible(d, admitted)
        elif named == "named" and self.relax != "dataset" and self.as_of >= rules.DATASET_ON_HUB_FROM:
            statuses = {}
            for name in d["datasets"].split(";"):
                if not name:
                    continue
                status = self.dataset_status(name, hf_id)
                if status is None:
                    return stop(2, "missing:dataset")
                statuses[name] = status
            reason, hub_status = rules.dataset_on_hub(statuses)
            d["dataset_hub_status"] = (d["dataset_hub_status"] + ";" + hub_status) if d["dataset_hub_status"] else hub_status
            if reason != "keep":
                if admitted is None:
                    return stop(2, reason)
                self.admit_accessible(d, admitted)

        # step 3: exactly one full-precision, instruction-tuned parent. With --relax parent a
        # model that fails any parent check goes on without one (parent_status keeps the reason).
        parent_cut = self.parent_checks(d, row, hf_id)
        if parent_cut is not None:
            if self.relax != "parent" or parent_cut not in NO_USABLE_PARENT:
                return stop(3, parent_cut)
            d["parent_status"] = f"relaxed:{parent_cut}"

        # still step 3: the uploaded weights (config.json) must describe the same network as the
        # declared parent's. Added 5 October after two kept models turned out to have cards naming
        # a parent their weights do not match. Its own step 4 until 9 October; now a loss reason
        # of the parent step (parent_discordant, config_unreadable, repo_gated).
        if d["parent_status"].startswith("relaxed:"):
            d["parent_config_check"] = "skipped: no usable parent (--relax parent)"
        else:
            cfg, d["config_file"] = self.config(hf_id, hf_id)
            if cfg is None:
                return stop(3, "missing:config")
            pcfg, d["parent_config_file"] = self.config(d["parent"], hf_id)
            if pcfg is None:
                return stop(3, "missing:parent_config")
            reason, d["parent_config_check"] = rules.parent_discordant(cfg, pcfg)
            if reason != "keep":
                return stop(3, reason)

        # step 4: a human read the card and removed the model; the reason is recorded, not
        # inferred. Models that pass this step are the set the study uses (kept.csv).
        manual = self.manual.get(hf_id.lower())
        if manual is not None:
            d["manual_category"] = manual["category"]
            d["manual_reason"] = manual["reason"]
            return stop(int(MANUAL_STEP), "manual_removed")

        # step 5: the fine-tuning method is stated (README, tags, or repo name). Last, and reported separately
        # (kept_method_stated.csv), because it is the largest cut after the keyword match and a
        # reviewer will want the result with and without it.
        readme, d["readme_file"] = self.readme(hf_id, hf_id)
        if readme is None:
            return stop(int(METHOD_STEP), "missing:readme")
        methods, d["method_evidence"] = rules.training_methods(row, readme)
        # agent_methods.csv: what an agent read in the card, preprint, or training script. A named
        # objective (sft, dpo, ...) or update scope (lora, qlora, full) counts as a stated method.
        agent = self.agent_methods.get(hf_id.lower())
        if agent is not None:
            found = [agent[k].strip().lower() for k in ("objective", "update_scope") if agent[k].strip().lower() not in NOT_STATED]
            if found:
                for m in found:
                    methods.add("agent:" + m)
                note = f"agent ({agent['source']}): {'/'.join(found)} {agent['source_url']}".strip()
                d["method_evidence"] = (d["method_evidence"] + "; " + note) if d["method_evidence"] else note
        d["methods"] = "|".join(sorted(methods))
        if not methods:
            return stop(int(METHOD_STEP), "no_training_method")

        # step 6: the training objective is known at evidence level 1 or 2 (objective-evidence.csv,
        # one file per grouping, dated per row). No row: the grouping has not done this step for
        # the model yet. Level 3: assumed from the data format alone, which Mark ruled out (10 Oct).
        ev = self.objective.get(hf_id.lower())
        if ev is None:
            return stop(int(OBJECTIVE_STEP), "no_objective_evidence")
        d["objective"] = ev["objective"]
        d["objective_stages"] = ev["stages"]
        d["objective_evidence_level"] = ev["evidence_level"]
        if ev["evidence_level"][:1] == "3":
            return stop(int(OBJECTIVE_STEP), "objective_assumed_only")
        return stop(int(OBJECTIVE_STEP), "kept")

    def parent_checks(self, d: dict, row: dict, hf_id: str):
        """Fill the parent fields of d; return the step-3 loss reason, or None when the parent passes."""
        d["parent"], d["parent_source_field"], d["parent_status"] = rules.extract_parent(row)
        if d["parent_status"] != "one_parent":
            return d["parent_status"]
        prow = self.card(d["parent"], hf_id)
        if prow is None:
            return "missing:parent_card"
        d["parent_card_screened_at"] = prow["screened_at"]
        d["parent"] = prow["hf_id"]
        d["parent_url"] = HUB + prow["hf_id"]
        d["parent_fp_reason"], _codes = self.precision(prow, hf_id)
        if d["parent_fp_reason"] == "missing:bin_header":
            return "missing:parent_bin_header"
        if d["parent_fp_reason"] == "row_unreadable":
            return "parent_unreadable"
        if d["parent_fp_reason"] != "keep":
            return "parent_not_fp"
        preadme, d["parent_readme_file"] = self.readme(d["parent"], hf_id)
        if preadme is None:
            return "missing:parent_readme"
        d["parent_class"], d["parent_class_source"], d["parent_class_evidence"] = rules.parent_class(d["parent"], prow, preadme)
        # parents.csv overrides the regex: the class a reader took from the parent's own card, with
        # the sentence and URL. Parents without a row are listed in parents_unregistered.csv.
        reg = self.parents.get(d["parent"].lower())
        if reg is not None:
            d["parent_class"], d["parent_class_source"] = reg["class"], "registry"
            d["parent_class_evidence"] = f"{reg['quote']} [{reg['evidence_url']}; {reg['decided_by']}, {reg['decided_on']}]"
        else:
            self.unregistered_parents.setdefault(d["parent"], []).append(hf_id)
        if d["parent_class"] != "instruction" and self.relax != "parent_instruction":
            return PARENT_CLASS_REASON[d["parent_class"]]
        return None

    def unused_manual(self, decisions: list) -> list:
        """Manual rows that apply to this view but whose model never reached the manual-review step."""
        reached = {d["hf_id"].lower() for d in decisions if d["step"] >= MANUAL_STEP}
        return [r["hf_id"] for k, r in sorted(self.manual.items()) if k not in reached]

    # -------------------------------------------------------------- outputs
    def counts(self, decisions: list) -> list:
        out = []
        catalog = cache.newest_catalog(self.as_of)
        if catalog is not None:
            with gzip.open(catalog, "rt") as fh:
                out.append({"step": "0", "outcome": "listed_on_hub", "n": sum(1 for ln in fh if ln.strip())})
        out.append({"step": "0", "outcome": "cohort", "n": len(decisions)})
        entered = len(decisions)
        for step in STEPS:
            here = [d for d in decisions if d["step"] == step]
            # The manual-review step splits the human removals into one outcome per category so
            # the figure can print "Removed for <category>" without a hand-typed list.
            lost_names = []
            for d in here:
                if d["decision"] == "kept":
                    continue
                if step == MANUAL_STEP and d["decision"] == "manual_removed":
                    lost_names.append(f"manual_removed: {d['manual_category']}")
                else:
                    lost_names.append(d["decision"])
            lost = Counter(lost_names)
            kept = entered - sum(lost.values())
            if kept < 0 or (step == STEPS[-1] and kept != sum(1 for d in here if d["decision"] == "kept")):
                fail(f"step {step}: accounting does not balance")
            out.append({"step": step, "outcome": "entered", "n": entered})
            out.append({"step": step, "outcome": "kept", "n": kept})
            for reason, n in sorted(lost.items()):
                out.append({"step": step, "outcome": reason, "n": n})
            entered = kept
        return out

    def provenance(self) -> list:
        if not cache.INDEX.exists():
            raise SystemExit(f"{cache.INDEX} is missing")
        source_of = {r["cache_file"]: r["date_source"] for r in read_csv(cache.INDEX)}
        missing = sorted({cache.rel(p) for paths in self.used.values() for p in paths} - source_of.keys())
        if missing:
            raise SystemExit("\n".join(f"{name} is not in {cache.INDEX}" for name in missing))
        out = []
        for kind, paths in self.used.items():
            if not paths:
                continue
            if kind == "card":
                dates = sorted(cache._card_date(p) for p in paths)
            else:
                dates = sorted(cache._date_of(p) for p in paths)
            sources = sorted({source_of[cache.rel(p)] for p in paths})
            out.append({"artifact": kind, "n_files": len(paths), "date_min": dates[0], "date_max": dates[-1],
                        "date_source": ";".join(sources)})
        return out

    def run(self) -> list:
        self.missing = []
        for s in self.used.values():
            s.clear()
        # Cleared per pass (9 Oct 2026, approved by Mark): --fetch reruns decide() for every id until
        # nothing is missing, and before this line each pass appended the same children again, so
        # parents_unregistered.csv listed each child once per pass and n_children was inflated.
        self.unregistered_parents = {}
        return [self.decide(hf_id) for hf_id in self.cohort()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", required=True, help="name of a file in queries/, without .csv")
    ap.add_argument("--as-of", required=True, help="ISO date; newest cache entry on or before it is used")
    ap.add_argument("--since", default="",
                    help="ISO date; ignore cache entries older than this. --since <today> --fetch refetches everything "
                         "(a lock-in run); earlier dated entries stay on disk untouched")
    ap.add_argument("--fetch", action="store_true",
                    help="fill cache misses from the Hub (dated today) and rerun until nothing is missing or a pass makes no progress")
    ap.add_argument("--relax", default="", choices=sorted(RELAX),
                    help="sensitivity run with one rule switched off; results go to sensitivity/<as-of>__relax-<rule>/. "
                         + " ".join(f"{k}: {v}." for k, v in RELAX.items()))
    args = ap.parse_args()
    if args.since and args.since > args.as_of:
        fail(f"--since {args.since} is after --as-of {args.as_of}")

    run = Run(args.grouping, args.as_of, args.since, args.relax)
    decisions = run.run()
    no_progress = 0
    if run.missing and args.fetch:
        import hub  # needs huggingface_hub; imported only here
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if today > args.as_of:
            fail(f"--fetch writes entries dated {today}, after --as-of {args.as_of}; they would not be used")
        # Each pass can expose the next layer of misses (search -> cards -> readmes -> parent cards
        # -> parent readmes). Repeat until clean; stop if a pass fetched everything asked and the
        # same keys are still missing, which means a cache write is not being read back.
        # The outputs below (including missing.csv) are still written before exiting 2.
        while run.missing:
            asked = {(m["kind"], m["key"]) for m in run.missing}
            hub.fill(run.missing, today)
            run.cards = cache.load_cards(args.as_of, args.since)
            decisions = run.run()
            if {(m["kind"], m["key"]) for m in run.missing} == asked:
                no_progress = len(asked)
                break

    out = RESULTS / args.grouping / (f"sensitivity/{args.as_of}__relax-{args.relax}" if args.relax else args.as_of)
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "decisions.csv", DECISION_FIELDS, decisions)
    def passed(step: str) -> list:
        return [d for d in decisions if d["step"] > step or (d["step"] == step and d["decision"] == "kept")]
    rows_of = lambda ds: [{k: d[k] for k in KEPT_FIELDS} for d in ds]  # noqa: E731
    # kept.csv is the study set: the survivors of the grouping's endpoint step. The two sensitivity
    # sets are written beside it whatever the endpoint is.
    write_csv(out / "kept.csv", KEPT_FIELDS, rows_of(passed(run.final_step)))
    write_csv(out / "kept_after_review.csv", KEPT_FIELDS, rows_of(passed(MANUAL_STEP)))
    write_csv(out / "kept_method_stated.csv", KEPT_FIELDS, rows_of(passed(METHOD_STEP)))
    write_csv(out / "kept_objective_known.csv", KEPT_FIELDS, rows_of(passed(OBJECTIVE_STEP)))
    write_csv(out / "counts.csv", ["step", "outcome", "n"], run.counts(decisions))
    write_csv(out / "missing.csv", ["kind", "key", "needed_for", "detail"], run.missing)
    write_csv(out / "provenance.csv", ["artifact", "n_files", "date_min", "date_max", "date_source"], run.provenance())
    write_csv(out / "parents_unregistered.csv", ["parent_id", "n_children", "children"],
              [{"parent_id": p, "n_children": len(c), "children": "|".join(sorted(c))}
               for p, c in sorted(run.unregistered_parents.items(), key=lambda kv: (-len(kv[1]), kv[0].lower()))])
    if run.unregistered_parents:
        print(f"note: {len(run.unregistered_parents)} parent(s) reached step 3 without a parents.csv row "
              f"(regex class used); see {out / 'parents_unregistered.csv'}", file=sys.stderr)

    for r in run.counts(decisions):
        print(f"{r['step']:>2}  {r['outcome']:<24} {r['n']:>9,}")
    if no_progress:
        fail(f"--fetch made no progress on {no_progress} missing keys; see {out / 'missing.csv'}")
    if run.missing:
        by_kind = Counter(m["kind"] for m in run.missing)
        print(f"MISSING: {dict(by_kind)} -> {out / 'missing.csv'}", file=sys.stderr)
        return 1
    stale = run.unused_manual(decisions)
    if stale:
        fail(f"{MANUAL.name}: {len(stale)} row(s) name a model that did not reach step {MANUAL_STEP} (manual review) "
             f"in this view (not in the cohort, or already cut by a rule): {stale}")
    print(f"wrote {out} (kept.csv = survivors of step {run.final_step})")
    # A complete normal run that is at least as new as the recorded one becomes the grouping's
    # current funnel (outputs/funnel/<grouping>/CURRENT). Older views (the regression gate's 2026-10-02,
    # a reproduction of an earlier pass) and --relax runs leave it alone.
    if not args.relax and cache.set_current(args.grouping, args.as_of):
        print(f"CURRENT -> {args.as_of} ({cache.current_path(args.grouping)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
