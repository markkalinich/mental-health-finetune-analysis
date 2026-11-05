"""Offline screen of local chat templates for the funnel cohort.

Cohort: the 53 ids in final-kept.txt, exact-joined to instruct-parent-kept.csv,
plus each child's parent. Loads AutoTokenizer from /home/mkalinich/hf_models
only (local_files_only=True). Does not load weights, download, or change how
any model is called.

Exits non-zero if the child join is not exactly those 53 ids.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import sys
import traceback
from pathlib import Path

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

HERE = Path(__file__).resolve().parent
KEPT = HERE / "final-kept.txt"
PARENTS = HERE / "instruct-parent-kept.csv"
OUT_CSV = HERE / "chat_template_screen.csv"
OUT_MD = HERE / "chat_template_screen.md"
HF_ROOT = Path("/home/mkalinich/hf_models")
EXPECTED_CHILDREN = 53
MSG_LIMIT = 300
NOT_ON_DISK = "weights or tokenizer not on disk"

TOKENIZER_FILES = {
    "tokenizer.json",
    "tokenizer.model",
    "tokenizer_config.json",
    "vocab.json",
    "vocab.txt",
    "spiece.model",
    "sentencepiece.bpe.model",
    "chat_template.jinja",
    "merges.txt",
}

SHAPE1 = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Say ok."},
]
SHAPE2 = [
    {"role": "user", "content": "You are a helpful assistant.\n\nSay ok."},
]

# Rejection of a system role. A raise_exception that merely mentions an
# optional system message (Mistral's alternation check) is not a rejection.
_REJECT = re.compile(
    r"system role not supported"
    r"|system messages? (?:are|is) not supported"
    r"|does not support (?:a |the )?system role"
    r"|raise_exception\(\s*['\"]system role",
    re.IGNORECASE,
)

FIELDS = [
    "hf_id",
    "role",
    "parent",
    "disk_note",
    "template_present",
    "template_sha256",
    "mentions_enable_thinking",
    "mentions_system_role_rejection",
    "shape1_result",
    "shape2_result",
]


def die(lines: list[str]) -> None:
    print("ERROR: cohort join is not 53 children", file=sys.stderr)
    for line in lines:
        print(line, file=sys.stderr)
    raise SystemExit(1)


def load_cohort() -> list[tuple[str, str, str]]:
    """Return (hf_id, role, parent) rows. Children first, then unique parents."""
    raw_lines = KEPT.read_text(encoding="utf-8").splitlines()
    children = [ln.strip() for ln in raw_lines if ln.strip()]
    problems: list[str] = []
    if len(children) != EXPECTED_CHILDREN:
        problems.append(
            f"final-kept.txt has {len(children)} non-empty ids, expected {EXPECTED_CHILDREN}"
        )
    seen: dict[str, int] = {}
    for hid in children:
        seen[hid] = seen.get(hid, 0) + 1
    dup_kept = sorted(hid for hid, n in seen.items() if n > 1)
    if dup_kept:
        problems.append("duplicate hf_id in final-kept.txt:")
        problems.extend(f"  {hid}" for hid in dup_kept)

    with PARENTS.open(newline="", encoding="utf-8") as fh:
        parent_rows = list(csv.DictReader(fh))
    if not parent_rows or "hf_id" not in parent_rows[0] or "parent" not in parent_rows[0]:
        problems.append(
            "instruct-parent-kept.csv is missing hf_id or parent columns"
        )
        die(problems)

    by_id: dict[str, str] = {}
    dup_csv: list[str] = []
    for row in parent_rows:
        hid = row["hf_id"]
        if hid in by_id:
            dup_csv.append(hid)
        else:
            by_id[hid] = row["parent"]
    if dup_csv:
        problems.append("duplicate hf_id in instruct-parent-kept.csv:")
        problems.extend(f"  {hid}" for hid in sorted(set(dup_csv)))

    missing = [hid for hid in children if hid not in by_id]
    if missing:
        problems.append("final-kept.txt ids with no exact instruct-parent-kept.csv row:")
        problems.extend(f"  {hid}" for hid in missing)

    blank_parent = [hid for hid in children if hid in by_id and not (by_id[hid] or "").strip()]
    if blank_parent:
        problems.append("joined children with an empty parent:")
        problems.extend(f"  {hid}" for hid in blank_parent)

    joined = [hid for hid in children if hid in by_id and (by_id[hid] or "").strip()]
    if len(joined) != EXPECTED_CHILDREN or len(set(joined)) != EXPECTED_CHILDREN:
        problems.append(
            f"exact join produced {len(joined)} rows ({len(set(joined))} unique), expected {EXPECTED_CHILDREN}"
        )
    if problems:
        die(problems)

    cohort: list[tuple[str, str, str]] = []
    child_ids = set(children)
    parent_order: list[str] = []
    parent_seen: set[str] = set()
    for hid in children:
        parent = by_id[hid]
        cohort.append((hid, "child", parent))
        if parent not in parent_seen and parent not in child_ids:
            parent_seen.add(parent)
            parent_order.append(parent)
    overlap = [p for p in dict.fromkeys(by_id[h] for h in children) if p in child_ids]
    if overlap:
        problems.append("parent id is also one of the 53 children (refusing to double-count or rename):")
        problems.extend(f"  {hid}" for hid in overlap)
        die(problems)
    for parent in parent_order:
        cohort.append((parent, "parent", ""))
    return cohort


def repo_dir(hf_id: str) -> Path:
    if hf_id.count("/") != 1:
        raise SystemExit(
            f"ERROR: hf_id {hf_id!r} is not org/name; refusing to guess a directory"
        )
    return HF_ROOT / hf_id.replace("/", "__")


def disk_status(path: Path) -> str:
    if not path.is_dir():
        return "missing_directory"
    names = {p.name for p in path.iterdir() if p.is_file()}
    if names.isdisjoint(TOKENIZER_FILES):
        return "no_tokenizer_files"
    return "present"


def template_source(tok) -> str | None:
    ct = getattr(tok, "chat_template", None)
    if ct is None:
        return None
    if isinstance(ct, str):
        text = ct
    else:
        text = json.dumps(ct, ensure_ascii=False, sort_keys=True, default=str)
    if not text.strip():
        return None
    return text


def exc_text(exc: BaseException) -> str:
    msg = " ".join(str(exc).split())
    if len(msg) > MSG_LIMIT:
        msg = msg[: MSG_LIMIT - 3] + "..."
    return f"{type(exc).__name__}: {msg}"


def render(tok, messages) -> str:
    try:
        out = tok.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
    except Exception as exc:
        return exc_text(exc)
    if not isinstance(out, str) or not out.strip():
        return f"ValueError: apply_chat_template returned {type(out).__name__}, not a non-empty string"
    return "ok"


def screen_one(hf_id: str, role: str, parent: str) -> dict[str, str]:
    row = {
        "hf_id": hf_id,
        "role": role,
        "parent": parent,
        "disk_note": "",
        "template_present": "no",
        "template_sha256": "",
        "mentions_enable_thinking": "no",
        "mentions_system_role_rejection": "no",
        "shape1_result": "",
        "shape2_result": "",
    }
    path = repo_dir(hf_id)
    status = disk_status(path)
    row["disk_note"] = status
    if status != "present":
        row["shape1_result"] = NOT_ON_DISK
        row["shape2_result"] = NOT_ON_DISK
        return row

    from transformers import AutoTokenizer

    try:
        tok = AutoTokenizer.from_pretrained(str(path), local_files_only=True)
    except Exception as exc:
        row["disk_note"] = "load_error"
        text = exc_text(exc)
        row["shape1_result"] = text
        row["shape2_result"] = text
        return row

    try:
        source = template_source(tok)
        if source is None:
            row["template_present"] = "no"
        else:
            row["template_present"] = "yes"
            row["template_sha256"] = hashlib.sha256(source.encode("utf-8")).hexdigest()
            if "enable_thinking" in source:
                row["mentions_enable_thinking"] = "yes"
            if _REJECT.search(source):
                row["mentions_system_role_rejection"] = "yes"
        row["shape1_result"] = render(tok, SHAPE1)
        row["shape2_result"] = render(tok, SHAPE2)
    finally:
        del tok
    return row


def bucket(row: dict[str, str]) -> str:
    if row["shape1_result"] == NOT_ON_DISK:
        return "not_on_disk"
    if row["disk_note"] == "load_error":
        return "load_error"
    if row["template_present"] != "yes":
        return "no_template"
    if row["shape1_result"] == "ok":
        return "shape1_ok"
    if row["shape2_result"] == "ok":
        return "shape1_fail_shape2_ok"
    return "fail_both"


def ids_in(rows: list[dict[str, str]], name: str) -> list[str]:
    return [r["hf_id"] for r in rows if bucket(r) == name]


def write_md(rows: list[dict[str, str]]) -> None:
    counts = {
        "shape1_ok": ids_in(rows, "shape1_ok"),
        "shape1_fail_shape2_ok": ids_in(rows, "shape1_fail_shape2_ok"),
        "no_template": ids_in(rows, "no_template"),
        "fail_both": ids_in(rows, "fail_both"),
        "not_on_disk": ids_in(rows, "not_on_disk"),
        "load_error": ids_in(rows, "load_error"),
    }
    n = len(rows)
    total = sum(len(v) for v in counts.values())
    if total != n:
        print(
            f"ERROR: buckets sum to {total}, rows are {n}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    rendered_without_template = [
        r["hf_id"]
        for r in rows
        if r["template_present"] != "yes"
        and r["disk_note"] == "present"
        and (r["shape1_result"] == "ok" or r["shape2_result"] == "ok")
    ]
    if rendered_without_template:
        print(
            "ERROR: apply_chat_template rendered with no chat template:",
            file=sys.stderr,
        )
        for hid in rendered_without_template:
            print(f"  {hid}", file=sys.stderr)
        raise SystemExit(1)

    n_child = sum(1 for r in rows if r["role"] == "child")
    n_parent = sum(1 for r in rows if r["role"] == "parent")
    if n_child != EXPECTED_CHILDREN:
        print(
            f"ERROR: wrote {n_child} child rows, expected {EXPECTED_CHILDREN}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    shape2_fail_among_ok = [
        r["hf_id"]
        for r in rows
        if bucket(r) == "shape1_ok" and r["shape2_result"] != "ok"
    ]
    fail_shape1 = [
        r["hf_id"]
        for r in rows
        if r["shape1_result"] != "ok" and r["shape1_result"] != NOT_ON_DISK and r["disk_note"] != "load_error"
    ]

    def bullets(ids: list[str]) -> str:
        if not ids:
            return "_none_\n"
        return "".join(f"- `{hid}`\n" for hid in ids)

    missing_dir = [r["hf_id"] for r in rows if r["disk_note"] == "missing_directory"]
    no_tok = [r["hf_id"] for r in rows if r["disk_note"] == "no_tokenizer_files"]

    lines = [
        "# Offline chat-template screen",
        "",
        f"Cohort: {n_child} children in `final-kept.txt`, exact-joined to `instruct-parent-kept.csv`, plus {n_parent} parents that are not themselves in that child list. {n} repositories. Tokenizer only, `local_files_only=True`, from `/home/mkalinich/hf_models/<org>__<name>`. Weights were not loaded.",
        "",
        "Shape 1 is the client request: a system message followed by a user message. Shape 2 is a single user message with the system text prepended. Both calls use `apply_chat_template(..., tokenize=False, add_generation_prompt=True)`.",
        "",
        "Counts partition the repositories. A repository with no chat template is counted under no template, including when both renders raise. Fail both means a template is present and both renders raise.",
        "",
        "| Bucket | Count |",
        "|---|---:|",
        f"| Render shape 1 | {len(counts['shape1_ok'])} |",
        f"| Fail shape 1, render shape 2 | {len(counts['shape1_fail_shape2_ok'])} |",
        f"| No template | {len(counts['no_template'])} |",
        f"| Fail both | {len(counts['fail_both'])} |",
        f"| Not on disk | {len(counts['not_on_disk'])} |",
        f"| Tokenizer load failed | {len(counts['load_error'])} |",
        f"| Total | {n} |",
        "",
        f"Shape 1 rendered for {len(counts['shape1_ok'])}. Shape 1 failed and shape 2 rendered for {len(counts['shape1_fail_shape2_ok'])}. No template: {len(counts['no_template'])}. Fail both: {len(counts['fail_both'])}. Not on disk: {len(counts['not_on_disk'])}.",
        "",
    ]
    if shape2_fail_among_ok:
        lines.append(
            "These rendered shape 1 and failed shape 2: "
            + ", ".join(f"`{hid}`" for hid in shape2_fail_among_ok)
            + "."
        )
        lines.append("")
    lines += [
        "## Fail shape 1",
        "",
        "Render was attempted and shape 1 raised. This includes the no-template repositories.",
        "",
        bullets(fail_shape1),
        "### Fail shape 1, render shape 2",
        "",
        bullets(counts["shape1_fail_shape2_ok"]),
        "### Fail both",
        "",
        bullets(counts["fail_both"]),
        "## No template",
        "",
        bullets(counts["no_template"]),
        "## Not on disk",
        "",
        "Missing directory:",
        "",
        bullets(missing_dir),
        "Directory present, no tokenizer files:",
        "",
        bullets(no_tok),
    ]
    if no_tok:
        lines += [
            "Those directories are on disk. None of them contains a tokenizer file, so the chat template was not read.",
            "",
        ]
    lines += [
        "## Tokenizer load failed",
        "",
        bullets(counts["load_error"]),
        "This screen does not change how any model is called.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cohort = load_cohort()
    # Import only after the join has succeeded, and only if some repo is on disk.
    rows: list[dict[str, str]] = []
    for hf_id, role, parent in cohort:
        print(f"screen {role} {hf_id}", file=sys.stderr)
        try:
            rows.append(screen_one(hf_id, role, parent))
        except Exception:
            traceback.print_exc(file=sys.stderr)
            print(f"ERROR: unhandled failure on {hf_id}", file=sys.stderr)
            raise SystemExit(1)

    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    write_md(rows)

    from collections import Counter

    tally = Counter(bucket(r) for r in rows)
    print(
        "counts "
        + " ".join(
            f"{name}={tally.get(name, 0)}"
            for name in (
                "shape1_ok",
                "shape1_fail_shape2_ok",
                "no_template",
                "fail_both",
                "not_on_disk",
                "load_error",
            )
        )
    )
    print(f"wrote {OUT_CSV}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
