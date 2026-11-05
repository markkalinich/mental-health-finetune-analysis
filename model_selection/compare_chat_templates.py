#!/usr/bin/env python3
"""Compare the chat template a kept model will serve with its parent's.

The study starts vLLM without ``--chat-template``. vLLM 0.26 then uses the
processor template when the repo has a processor, and otherwise the tokenizer
template. This script reads those files. It does not load weights and it does
not start a server.

Weights are ``/home/mkalinich/hf_models/<org>__<name>/``. ``tokenizer_from`` in
``config/serving_repairs.csv`` is the directory vLLM's ``--tokenizer`` points
at, so that directory supplies the served template.

Usage (project venv):

  .venv/bin/python model_selection/compare_chat_templates.py \\
      --grouping mental-health \\
      --out docs/mental_health_FT_funnel/chat-templates.csv

The method is ``docs/chat-template-comparison.md``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

import jinja2
import jinja2.ext

REPO = Path(__file__).resolve().parents[1]
HF_ROOT = Path("/home/mkalinich/hf_models")
RESULTS = REPO / "outputs" / "funnel"
REPAIRS = REPO / "config" / "serving_repairs.csv"

SYSTEM = "Reply with one word."
USER = "Hello."
IMAGE_URL = "https://example.invalid/picture.png"

COLUMNS = [
    "hf_id",
    "parent",
    "child_dir_present",
    "parent_dir_present",
    "fold_system",
    "tokenizer_from",
    "child_source",
    "child_sha256",
    "served_source",
    "served_sha256",
    "parent_source",
    "parent_sha256",
    "served_source_equals_parent",
    "text_equal",
    "text_child_error",
    "text_parent_error",
    "folded_equal",
    "folded_child_error",
    "folded_parent_error",
    "list_equal",
    "list_child_error",
    "list_parent_error",
    "image_url_equal",
    "image_url_child_error",
    "image_url_parent_error",
    "image_part_equal",
    "image_part_child_error",
    "image_part_parent_error",
]


def repo_dir(hf_id: str) -> Path:
    return HF_ROOT / hf_id.replace("/", "__")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def tokenizer_config(directory: Path) -> dict:
    path = directory / "tokenizer_config.json"
    if not path.is_file():
        return {}
    data = read_json(path)
    return data if isinstance(data, dict) else {}


def template_from_config_value(value) -> str | None:
    if isinstance(value, str) and value.strip():
        return value
    if isinstance(value, list):
        named = [
            item for item in value
            if isinstance(item, dict) and item.get("name") == "default" and isinstance(item.get("template"), str)
        ]
        if named:
            return named[0]["template"]
        for item in value:
            if isinstance(item, dict) and isinstance(item.get("template"), str):
                return item["template"]
    return None


def jinja_file(directory: Path) -> str | None:
    path = directory / "chat_template.jinja"
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return None


def tokenizer_template(directory: Path) -> tuple[str, str] | None:
    """Tokenizer load: chat_template.jinja wins over tokenizer_config.json."""
    jinja = jinja_file(directory)
    if jinja is not None:
        return "tokenizer:chat_template.jinja", jinja
    field = template_from_config_value(tokenizer_config(directory).get("chat_template"))
    if field is not None:
        return "tokenizer:tokenizer_config.json", field
    return None


def has_processor(directory: Path) -> bool:
    return (directory / "processor_config.json").is_file() or (
        directory / "preprocessor_config.json"
    ).is_file()


def processor_template(directory: Path) -> tuple[str, str] | None:
    """Processor load, transformers 5.14.

    chat_template.json is the legacy processor file. When it exists, its
    chat_template string is used and chat_template.jinja is not read. Extra
    files under chat_templates/ together with chat_template.json make the
    processor load raise; that case is reported as an error string.
    """
    if not has_processor(directory):
        return None
    processor_cfg_path = directory / "processor_config.json"
    if not processor_cfg_path.is_file():
        processor_cfg_path = directory / "preprocessor_config.json"
    processor_cfg = read_json(processor_cfg_path) if processor_cfg_path.is_file() else {}
    embedded = processor_cfg.get("chat_template") if isinstance(processor_cfg, dict) else None
    if isinstance(embedded, str) and embedded.strip():
        return "processor:processor_config.json", embedded

    legacy = directory / "chat_template.json"
    extra = sorted((directory / "chat_templates").glob("*.jinja")) if (directory / "chat_templates").is_dir() else []
    if legacy.is_file():
        if extra:
            return (
                "processor:conflict",
                "chat_template.json plus chat_templates/*.jinja; processor load raises",
            )
        payload = read_json(legacy)
        text = payload.get("chat_template") if isinstance(payload, dict) else None
        if isinstance(text, str):
            return "processor:chat_template.json", text
        return "processor:chat_template.json", ""
    jinja = jinja_file(directory)
    if jinja is not None:
        return "processor:chat_template.jinja", jinja
    return None


def served_template(directory: Path) -> tuple[str, str] | None:
    """vLLM with no --chat-template: processor template, else tokenizer template."""
    if not directory.is_dir():
        return None
    if has_processor(directory):
        processor = processor_template(directory)
        if processor is not None and processor[0] != "processor:conflict":
            return processor
        if processor is not None and processor[0] == "processor:conflict":
            return processor
    return tokenizer_template(directory)


def token_string(cfg: dict, key: str) -> str:
    value = cfg.get(key)
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        content = value.get("content")
        return content if isinstance(content, str) else ""
    return ""


def render(template: str, messages: list, directory: Path) -> tuple[str, str]:
    """Return (rendered, error). One of them is empty."""
    if template.startswith("chat_template.json plus"):
        return "", template
    cfg = tokenizer_config(directory)
    # Same Jinja settings transformers uses in render_jinja_template
    # (trim_blocks, lstrip_blocks, loopcontrols). Default Undefined, so a
    # missing field is empty rather than an error.
    env = jinja2.Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        extensions=[jinja2.ext.loopcontrols],
    )

    def raise_exception(message: str) -> None:
        raise jinja2.TemplateError(str(message))

    env.globals["raise_exception"] = raise_exception
    try:
        compiled = env.from_string(template)
        text = compiled.render(
            messages=messages,
            add_generation_prompt=True,
            tools=None,
            bos_token=token_string(cfg, "bos_token"),
            eos_token=token_string(cfg, "eos_token"),
            unk_token=token_string(cfg, "unk_token"),
            pad_token=token_string(cfg, "pad_token"),
            raise_exception=raise_exception,
        )
    except Exception as exc:
        return "", f"{type(exc).__name__}: {exc}"
    return text, ""


def probe(served: tuple[str, str] | None, served_dir: Path, parent: tuple[str, str] | None, parent_dir: Path, messages: list) -> tuple[str, str, str]:
    if served is None or parent is None:
        return "", "missing template" if served is None else "", "missing template" if parent is None else ""
    left, left_err = render(served[1], messages, served_dir)
    right, right_err = render(parent[1], messages, parent_dir)
    if left_err or right_err:
        return "", left_err, right_err
    return "yes" if left == right else "no", "", ""


def load_repairs() -> dict[str, dict[str, str]]:
    if not REPAIRS.is_file():
        return {}
    with REPAIRS.open(newline="", encoding="utf-8") as handle:
        return {row["hf_id"]: row for row in csv.DictReader(handle)}


def kept_rows(grouping: str) -> tuple[str, list[dict[str, str]]]:
    current_path = RESULTS / grouping / "CURRENT"
    if not current_path.is_file():
        raise SystemExit(f"no CURRENT file at {current_path}")
    date = current_path.read_text(encoding="utf-8").strip()
    kept = RESULTS / grouping / date / "kept.csv"
    if not kept.is_file():
        raise SystemExit(f"no kept.csv at {kept}")
    with kept.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return str(kept), rows


def compare_row(row: dict[str, str], repairs: dict[str, dict[str, str]]) -> dict[str, str]:
    hf_id = row["hf_id"]
    parent_id = row["parent"]
    repair = repairs.get(hf_id, {})
    fold = repair.get("fold_system", "0") == "1"
    tokenizer_from = (repair.get("tokenizer_from") or "").strip()
    child_dir = repo_dir(hf_id)
    parent_dir = repo_dir(parent_id)
    served_dir = repo_dir(tokenizer_from) if tokenizer_from else child_dir

    child = served_template(child_dir) if child_dir.is_dir() else None
    served = served_template(served_dir) if served_dir.is_dir() else None
    parent = served_template(parent_dir) if parent_dir.is_dir() else None

    text_messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": USER},
    ]
    folded_messages = [
        {"role": "user", "content": f"{SYSTEM}\n\n{USER}"},
    ]
    list_messages = [
        {"role": "user", "content": [{"type": "text", "text": USER}]},
    ]
    image_messages = [
        {
            "role": "user",
            "content": [{"type": "image_url", "image_url": {"url": IMAGE_URL}}],
        },
    ]
    image_part_messages = [
        {"role": "user", "content": [{"type": "image"}]},
    ]

    def pack(result: tuple[str, str, str]) -> tuple[str, str, str]:
        return result

    text = pack(probe(served, served_dir, parent, parent_dir, text_messages))
    folded = pack(probe(served, served_dir, parent, parent_dir, folded_messages))
    listed = pack(probe(served, served_dir, parent, parent_dir, list_messages))
    image = pack(probe(served, served_dir, parent, parent_dir, image_messages))
    image_part = pack(probe(served, served_dir, parent, parent_dir, image_part_messages))

    child_sha = sha256_text(child[1]) if child and child[0] != "processor:conflict" else ""
    served_sha = sha256_text(served[1]) if served and served[0] != "processor:conflict" else ""
    parent_sha = sha256_text(parent[1]) if parent and parent[0] != "processor:conflict" else ""
    if served and served[0] == "processor:conflict":
        served_sha = ""
    if child and child[0] == "processor:conflict":
        child_sha = ""
    if parent and parent[0] == "processor:conflict":
        parent_sha = ""

    source_equal = ""
    if served_sha and parent_sha:
        source_equal = "yes" if served_sha == parent_sha else "no"

    return {
        "hf_id": hf_id,
        "parent": parent_id,
        "child_dir_present": "yes" if child_dir.is_dir() else "no",
        "parent_dir_present": "yes" if parent_dir.is_dir() else "no",
        "fold_system": "1" if fold else "0",
        "tokenizer_from": tokenizer_from,
        "child_source": child[0] if child else "",
        "child_sha256": child_sha,
        "served_source": served[0] if served else "",
        "served_sha256": served_sha,
        "parent_source": parent[0] if parent else "",
        "parent_sha256": parent_sha,
        "served_source_equals_parent": source_equal,
        "text_equal": text[0],
        "text_child_error": text[1],
        "text_parent_error": text[2],
        "folded_equal": folded[0],
        "folded_child_error": folded[1],
        "folded_parent_error": folded[2],
        "list_equal": listed[0],
        "list_child_error": listed[1],
        "list_parent_error": listed[2],
        "image_url_equal": image[0],
        "image_url_child_error": image[1],
        "image_url_parent_error": image[2],
        "image_part_equal": image_part[0],
        "image_part_child_error": image_part[1],
        "image_part_parent_error": image_part[2],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grouping", required=True, choices=("mental-health", "safety", "medical"))
    parser.add_argument("--out", type=Path, help="CSV path. Printed to stdout when omitted.")
    args = parser.parse_args()
    kept_path, rows = kept_rows(args.grouping)
    repairs = load_repairs()
    compared = [compare_row(row, repairs) for row in rows]
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(compared)
        print(f"wrote {len(compared)} rows to {args.out}", file=sys.stderr)
        print(f"kept list: {kept_path}", file=sys.stderr)
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(compared)
        print(f"kept list: {kept_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
