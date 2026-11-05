"""Funnel rules. Pure functions over one card row (a dict of first-pass fields) and README text.

Each rule is defined once here. The wording of each rule is in
docs/mental_health_FT_funnel/archive/2026-09-23/hf-inventory-mh-funnel-2026-09-23.md. No file paths, no HTTP.

funnel.py applies them in this order. The step value it records is shown.
  1 full_precision        root model.safetensors (dtypes from Hub metadata) or, failing that, root
                          pytorch_model.bin (dtypes read from the file's pickle header, cached as a
                          bin header); at least one float dtype (F16, BF16, F32) and no dtype outside
                          those except I64 and BOOL, which is how non-weight buffers (BERT position_ids, GPT-2 masks)
                          are stored. U8/I8/I32/U32/F8 mean quantized.
  2 text-capable          pipeline_tag not in VISION; image-text-to-text stays
  2 dataset               cardData.datasets or a dataset: tag, after dropping JUNK words
  2 dataset_on_hub        at least one named dataset exists on the Hub (dataset_info ok or gated);
                          applies to views dated DATASET_ON_HUB_FROM (2026-10-06) or later
  2 accessible_data       from ACCESSIBLE_FROM (2026-10-08): a Python-list dataset tag is read as the
                          repo id inside it, and accessible_data.csv can admit a model whose training
                          file or dataset page was opened
  3 extract_parent        exactly one org/name from baseModels, card base_model, or base_model: tags
  3 parent full precision full_precision on the parent's own row
  3 parent_class          yaml, then README, then repo-name token; funnel keeps only instruction
  3 parent_discordant     child config.json vs parent config.json (architecture, vocab, width, depth);
                          its own step 4 until 9 Oct, now a loss reason of the parent step; from
                          10 Oct a text-only export (XForCausalLM) of a multimodal parent
                          (XForConditionalGeneration) counts as the same architecture
  5 training method       one of METHOD named in the README body, the tags, or the repo name (whole
                          tokens, NAME_METHOD); "no LoRA" / "without LoRA" does not count as LoRA;
                          "full fine-tune" counts as a method (full_finetune)
  (step 4, manual review, has no rule here: funnel.py reads manual_removals.csv)
"""
from __future__ import annotations

import ast
import json
import re
from typing import Optional

OK_DTYPES = {"F16", "BF16", "F32"}
# Non-weight buffers saved next to the weights: I64 counters (BERT position_ids, token_type_ids) and
# BOOL masks (GPT-2's causal attention `bias` buffer, saved by older transformers versions). No
# quantization scheme stores weights as 64-bit integers or as booleans, so neither beside float
# weights is evidence of quantization. BOOL added 9 Oct 2026 (three DialoGPT fine-tunes were cut).
BUFFER_DTYPES = {"I64", "BOOL"}
# Shard names: `model-00001-of-00002.safetensors` (transformers) and `model.safetensors-00001-of-00002.safetensors`
# (Qwen3.5 releases and their fine-tunes; added 10 Oct 2026, Mark's approval, see README code changes log).
ROOT_CKPT = re.compile(r"^model(-\d+-of-\d+|\.safetensors-\d+-of-\d+)?\.safetensors$")
ROOT_BIN = re.compile(r"^pytorch_model(-\d+-of-\d+)?\.bin$")
# torch storage class -> the dtype code safetensors metadata would show for the same tensor
STORAGE_DTYPE = {
    "FloatStorage": "F32", "HalfStorage": "F16", "BFloat16Storage": "BF16", "DoubleStorage": "F64",
    "LongStorage": "I64", "IntStorage": "I32", "ShortStorage": "I16", "CharStorage": "I8",
    "ByteStorage": "U8", "BoolStorage": "BOOL",
}
# image-text-to-text stays: those models take text and an image.
VISION = {"image-classification", "image-segmentation", "video-classification", "image-to-text"}
# Hyphens and underscores are read as spaces first (norm). QLoRA is recorded alone when the card also says LoRA.
METHOD = re.compile(
    r"\b(qlora|(?<!q)lora|dpo|direct preference optimization|grpo|rlhf|ppo|sft|supervised fine ?tun\w*"
    r"|full(?: parameter)? fine ?tun\w*)\b",
    re.I,
)
# "Full fine-tune (no LoRA)" names LoRA only to deny it. These phrases are blanked before matching.
NEGATED_METHOD = re.compile(r"\b(no|not|without|non|instead of|rather than)[ ]+(q?lora)\b", re.I)
EVIDENCE_CHARS = 60  # context kept on each side of a match in the evidence columns
JUNK = {"unknown", "none", "synthetic", "custom", "private", "proprietary", "n/a", "na", "data", "card does not say"}
BASE_MODEL_RELATIONS = {"finetune", "adapter", "merge", "quantized"}


def _json(text: Optional[str], default):
    try:
        return json.loads(text) if text else default
    except json.JSONDecodeError:
        return default


# ------------------------------------------------------------------ step 1
def _root_files(row: dict, pattern) -> list:
    siblings = _json(row.get("siblings"), [])
    if not isinstance(siblings, list):
        return []
    return sorted(s["rfilename"] for s in siblings
                  if isinstance(s, dict) and pattern.match(s.get("rfilename") or ""))


def root_bin_files(row: dict) -> list:
    """Root pytorch_model.bin shards, only when the repo has no root safetensors checkpoint."""
    if _root_files(row, ROOT_CKPT):
        return []
    return _root_files(row, ROOT_BIN)


def _hub_dtype_params(row: dict) -> Optional[dict]:
    """The Hub's safetensors summary (dtype -> parameter count), or None when it is blank."""
    record = _json(row.get("safetensors"), {})
    params = record.get("parameters") if isinstance(record, dict) else None
    return params if isinstance(params, dict) and params else None


def header_files(row: dict) -> list:
    """Root weight files whose dtypes must be read from the file header itself (hub.fill, cached
    under bin_headers/): the root safetensors shards when the Hub's dtype summary is blank (9 Oct:
    four real sharded models were being cut as blank_record), else the root pytorch_model.bin
    shards when there is no root safetensors checkpoint."""
    st = _root_files(row, ROOT_CKPT)
    if st:
        return st if _hub_dtype_params(row) is None else []
    return _root_files(row, ROOT_BIN)


def _dtype_verdict(dtypes: set, codes: str) -> tuple:
    if not dtypes & OK_DTYPES or dtypes - OK_DTYPES - BUFFER_DTYPES:
        return "other_dtype", codes
    return "keep", codes


def _from_header(files_needed: list, header: str) -> tuple:
    """Dtype verdict from a cached header record {"files": {name: [types] | "ERR ..."}}."""
    files = (_json(header, {}) or {}).get("files")
    if not isinstance(files, dict) or any(f not in files for f in files_needed):
        return "bin_unreadable", "header_incomplete"
    dtypes: set = set()
    for f in files_needed:
        types = files[f]
        if not isinstance(types, list):
            if _is_gated_err(str(types)):
                return "repo_gated", str(types)[:80]
            return "bin_unreadable", str(types)[:80]
        for t in types:
            dtypes.add(STORAGE_DTYPE.get(t, t))
    if not dtypes:
        return "blank_record", ""
    return _dtype_verdict(dtypes, "|".join(sorted(dtypes)))


def full_precision(row: dict, bin_header: Optional[str] = None) -> tuple:
    """Return (reason, dtype_codes). reason is keep | row_unreadable | no_root | blank_record |
    other_dtype | needs_bin_header | bin_unreadable | repo_gated.

    Safetensors repos: dtypes come from the Hub's safetensors summary on the card; when that
    summary is blank, from the file's own header (bin_header; hub.fill reads it with two ranged
    GETs). pytorch_model.bin repos (no root safetensors): dtypes come from the storage types in
    each shard's pickle header (bin_header, three ranged GETs). needs_bin_header means the caller
    must supply it; bin_unreadable means a file header could not be read (a pre-1.6 torch pickle,
    a Git-LFS pointer, a file that is not safetensors); repo_gated means the Hub answered 401/403
    for the file (gated or private repo the token is not approved for); blank_record means the
    header named no tensors.
    """
    if row.get("fetch_err") or (row.get("http_status") or "") != "200":
        return "row_unreadable", ""
    needed = header_files(row)
    if _root_files(row, ROOT_CKPT):
        params = _hub_dtype_params(row)
        if params is not None:
            return _dtype_verdict(set(params), "|".join(sorted(params)))
    elif not needed:
        return "no_root", ""
    if bin_header is None:
        return "needs_bin_header", ""
    return _from_header(needed, bin_header)


# ------------------------------------------------------------------ steps 2 and 5: text pipeline, dataset, training method
def norm(text: str) -> str:
    return re.sub(r"[-_]", " ", text)


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", " ", text, flags=re.S)


def canon(match: str) -> str:
    m = match.lower()
    if m.startswith("supervised fine"):
        return "sft"
    if m.startswith("full"):
        return "full_finetune"
    if m == "direct preference optimization":
        return "dpo"
    return m


def _snippet(text: str, start: int, end: int) -> str:
    lo, hi = max(0, start - EVIDENCE_CHARS), min(len(text), end + EVIDENCE_CHARS)
    return ("…" if lo else "") + " ".join(text[lo:hi].split()) + ("…" if hi < len(text) else "")


def methods_in(text: str) -> dict:
    """method -> first snippet that names it. Negated mentions ('no LoRA') are blanked first."""
    text = NEGATED_METHOD.sub(" ", text)
    found: dict = {}
    for m in METHOD.finditer(text):
        label = canon(m.group(0))
        snippet = _snippet(text, m.start(), m.end())
        # "QLoRA enables full fine-tuning of 7B models on two T4s" is a sentence about QLoRA. A
        # full-fine-tune match whose own sentence also names LoRA/QLoRA is not recorded (9 Oct).
        if label == "full_finetune" and re.search(r"\bq?lora\b", snippet, re.I):
            continue
        found.setdefault(label, snippet)
    if "qlora" in found:
        found.pop("lora", None)
    return found


# Repo-name tokens that name a training method (6 Oct). The name is split on - _ . ; whole tokens
# only, so 'lora' in 'qwen2.5-7b-mental-therapy-lora-sft' counts and 'ft' or 'finetune' (the fact
# of fine-tuning, not a method) does not. Same vocabulary as METHOD, minus full fine-tune ('fft'
# is ambiguous).
NAME_METHOD = {"lora", "qlora", "sft", "dpo", "grpo", "ppo", "rlhf"}


def methods_in_name(repo_id: str) -> dict:
    """method -> 'name <token>' for each method token in the repo name (owner excluded)."""
    name = repo_id.split("/", 1)[-1]
    found: dict = {}
    for tok in re.split(r"[-_.]+", name.lower()):
        if tok in NAME_METHOD:
            found.setdefault(tok, f"name {tok}")
    if "qlora" in found:
        found.pop("lora", None)
    return found


# A method word inside a URL, a repo or dataset id (org/name), or an inline code span is not a
# statement about how this model was trained (9 Oct: 'SAGI-1/Greetings_DPO_dataset_V1' counted as
# DPO). These are blanked before the method regex runs.
_URL = re.compile(r"https?://\S+")
_REPO_ID = re.compile(r"(?<![\w./-])[\w.\-]+/[\w.\-]+(?![\w./-])")
_INLINE_CODE = re.compile(r"`[^`\n]*`")


def strip_identifiers(text: str) -> str:
    text = _URL.sub(" ", text)
    text = _INLINE_CODE.sub(" ", text)
    return _REPO_ID.sub(" ", text)


def training_methods(row: dict, readme: Optional[str]) -> tuple:
    """(methods, evidence). Methods named in the README body (code blocks, URLs, repo and dataset
    ids removed), the tags (dataset: tags removed), or the repo name (whole tokens; NAME_METHOD).
    evidence is 'method: snippet' per method, '; '-joined; a snippet starts with 'tag' or 'name'
    when it did not come from the README. readme None or FETCH_ERR = unreadable."""
    tags = norm("|".join(t for t in (row.get("tags") or "").split("|") if not t.lower().startswith("dataset:")))
    body = "" if readme_unreadable(readme) else norm(strip_identifiers(strip_code(readme)))
    found = methods_in(body)
    for k, v in methods_in(tags).items():
        found.setdefault(k, "tag " + v)
    for k, v in methods_in_name(row.get("hf_id") or "").items():
        found.setdefault(k, v)
    if "qlora" in found:
        found.pop("lora", None)
    return set(found), "; ".join(f"{k}: {found[k]}" for k in sorted(found))


def readme_unreadable(readme: Optional[str]) -> bool:
    return readme is None or readme.startswith("FETCH_ERR")


def named_datasets(row: dict) -> tuple:
    """Return (named|not_named, source, semicolon-joined pieces)."""
    card = _json(row.get("cardData"), {})
    raw = card.get("datasets") if isinstance(card, dict) else None
    source, vals = "", []
    if raw not in (None, "", []):
        source = "yaml_datasets"
        vals = raw if isinstance(raw, list) else [raw]
    else:
        tags = [t.strip() for t in (row.get("tags") or "").split("|") if t.strip()]
        vals = [t.split(":", 1)[1].strip() for t in tags if t.lower().startswith("dataset:")]
        if vals:
            source = "dataset_tag"
    pieces = []
    for val in vals:
        for piece in str(val).split(";"):
            piece = piece.strip()
            if piece and piece.lower() not in JUNK:
                pieces.append(piece)
    return ("named" if pieces else "not_named"), source, ";".join(pieces)


# A dataset name is only evidence if the Hub has a dataset repo by that name (6 Oct). The lookups
# are a cache artifact that did not exist before 6 Oct, so the rule applies to views dated on or
# after that day, the way a query or a manual-removal row counts only from its own date.
DATASET_ON_HUB_FROM = "2026-10-06"
DATASET_EXISTS = {"ok", "gated"}
# From this date, a dataset tag written as a Python list is the repo id inside the list, and a row
# in accessible_data.csv can keep a model whose training file or dataset page was opened.
ACCESSIBLE_FROM = "2026-10-08"


def dataset_repo_ids(piece: str):
    """If piece is a Python list of strings, return the items that are repo ids (they contain /).
    None means the piece is not a list, and the caller keeps it unchanged."""
    text = piece.strip()
    if not text.startswith("["):
        return None
    try:
        val = ast.literal_eval(text)
    except (SyntaxError, ValueError):
        return None
    if not isinstance(val, list) or not all(isinstance(x, str) for x in val):
        return None
    return [x.strip() for x in val if "/" in x.strip()]


def expand_dataset_lists(joined: str) -> str:
    """Replace a dataset tag that is a Python list with the repo ids inside it."""
    if not joined:
        return joined
    out = []
    changed = False
    for piece in joined.split(";"):
        ids = dataset_repo_ids(piece)
        if ids is None:
            out.append(piece)
        else:
            changed = True
            out.extend(ids)
    return ";".join(out) if changed else joined


def dataset_on_hub(statuses: dict) -> tuple:
    """statuses: dataset name -> status from cache/datasets (ok | gated | not_found | invalid_name).
    Keep when at least one named dataset exists on the Hub (public or gated).
    Returns (keep | dataset_not_on_hub, 'name=status;...')."""
    detail = ";".join(f"{n}={statuses[n]}" for n in sorted(statuses))
    return ("keep" if any(v in DATASET_EXISTS for v in statuses.values()) else "dataset_not_on_hub"), detail


# ------------------------------------------------------------------ step 3: parent id
def _repo_pieces(val) -> list:
    out: list = []
    if val is None:
        return out
    if isinstance(val, list):
        for item in val:
            out.extend(_repo_pieces(item))
        return out
    if isinstance(val, dict):
        for key in ("id", "name", "repo_id", "model", "base_model"):
            if val.get(key):
                return _repo_pieces(val[key])
        return out
    text = str(val).strip()
    if not text or text.lower() in {"none", "null", "n/a", "unknown"}:
        return out
    for piece in text.split(";"):
        piece = piece.strip().strip("'\"")
        if "/" in piece:
            out.append(piece)
    return out


def _ids_from_tag(tag: str) -> list:
    text = tag.strip()
    if not text.lower().startswith("base_model:"):
        return []
    rest = text.split(":", 1)[1].strip()
    head, sep, tail = rest.partition(":")
    if sep and head.lower() in BASE_MODEL_RELATIONS:
        rest = tail.strip()
    rest = rest.strip().strip("'\"")
    if "/" not in rest:
        return []
    return [rest.split()[0]]


def extract_parent(row: dict) -> tuple:
    """Return (parent or pipe-joined parents, source fields, status).

    status is one_parent | no_parent | multiple_parents. A value with no slash is not a repo id.
    The model's own id is not a parent. Ids compare case-insensitively.
    """
    own = row["hf_id"].lower()
    found: list = []

    def add(source: str, ids: list) -> None:
        for item in ids:
            item = item.strip()
            if "/" not in item or item.lower() == own:
                continue
            found.append((source, item))

    base_models = _json(row.get("baseModels"), None)
    if isinstance(base_models, dict):
        models = base_models.get("models") or []
        ids = []
        if isinstance(models, list):
            for model in models:
                if isinstance(model, dict) and model.get("id"):
                    ids.append(str(model["id"]).strip())
                elif isinstance(model, str):
                    ids.append(model.strip())
        add("baseModels", ids)
    elif isinstance(base_models, list):
        add("baseModels", [str(item) for item in base_models])
    card = _json(row.get("cardData"), {})
    if isinstance(card, dict) and card.get("base_model") not in (None, "", []):
        add("card.base_model", _repo_pieces(card.get("base_model")))
    tag_ids: list = []
    for tag in (row.get("tags") or "").split("|"):
        tag_ids.extend(_ids_from_tag(tag))
    add("tag.base_model", tag_ids)

    uniq: list = []
    sources: dict = {}
    for source, item in found:
        key = item.lower()
        if key not in sources:
            uniq.append(item)
            sources[key] = []
        if source not in sources[key]:
            sources[key].append(source)
    if not uniq:
        return "", "", "no_parent"
    if len(uniq) > 1:
        return "|".join(uniq), "", "multiple_parents"
    return uniq[0], ";".join(sources[uniq[0].lower()]), "one_parent"


# ------------------------------------------------------------------ step 3: parent class
INSTR_TAGS = {"instruct", "instruction-tuned", "instruction-tuning", "chat"}
PRE_TAGS = {"pretrained", "pre-trained", "base", "base-model", "foundation", "pretraining"}
# Sentences class_from_readme skips: a model family, a corpus size, a results
# table, or Hub boilerplate, not this checkpoint.
EXCL = re.compile(
    r"both (the )?(pre-?trained|base)( variants)? and (the )?instruct"      # Gemma card names a base and an instruct release
    r"|base and instruct|pre-?trained and instruct|instruct(ion-?)?( |-)tuned and pre-?trained"  # Llama card names a base and an instruct release
    r"|collection of .{0,80}(pre-?trained|instruct)"                        # 'collection of pretrained and instruction tuned models'
    r"|we release .{0,60}models|instruct(ion-tuned)? models? additionally"  # release announcement for a set of models
    r"|results marked .{0,40}instruct|for instruction-?tuned models\b|compared to (standard )?instruction-?tuned"  # comparison, not this checkpoint
    r"|for our instruct(ion-?)?[ -]tuned model"                               # Meta's Llama 3 card (one file on the base and the instruct repo) talking about the instruct sibling (6 Oct)
    r"|fine-?tuned versions? on a task|fine-?tuned from this one|models fine-?tuned from this"   # Hub card boilerplate about other models
    r"|\btuned versions\b|is a general method"                             # 'The tuned versions use SFT and RLHF' on base cards; a paper-abstract quote
    r"|export your fine-?tuned|2x faster|safety post-training|from_pretrained"  # template or library boilerplate
    r"|was pre-?trained on ~?(?:up to |over |more than |about |around |approximately )?\d"  # family corpus size ('was pretrained on over 15 trillion tokens')
    r"|these models are pre-?trained on"                                   # family corpus sentence on an instruct card
    r"|evaluation of fine-?tuned"                                          # results heading
    r"|the instruction-?tuned variants (can|may|should)"                   # base card pointing at its instruct siblings (salamandra-7b) (6 Oct)
    r"|post-?trained (with a supervised classification loss|as a bidirectional)"  # a token classifier, not an instruction tune (openai/privacy-filter) (6 Oct)
    r"|pre-?trained variants, and instruction-?tuned variants", re.I)      # Gemma sentence that names both releases
# On a sentence EXCL did not drop: instruction fine-tune, then fine-tuned-from, then instruction or chat.
INS_FT = re.compile(r"instruct(ion)?[- ]fine-?tuned (version|variant|model)", re.I)
FT = re.compile(r"(fine-?tuned (version|variant|model|checkpoint) of|fine-?tuned from|finetuned from model|trained on top of|continually pre-?trained from|further (fine-?tuned|trained) from|fine-?tuned (the |a |an )?[\w\-\.\/]+ (model |base model |checkpoint )?on |full fine-?tune of|this is a\b[^.]{0,120}\bfine-?tune,)", re.I)
INS = re.compile(r"(instruction-?\s?tuned|instruct-tuned|instruction[- ]?fine-?tun|post-?trained|this is the chat model|chat model (fine-?tuned|trained)|aligned (with|using|via) (rlhf|dpo)|supervised fine-?tuning (\(sft\) )?(and|followed by|with) (rlhf|dpo|reinforcement)|pre-?training\s*(&|and|→|->)\s*post-?training)", re.I)
# A sentence that says this checkpoint was NOT instruction-tuned is evidence that it is pre-trained
# ('The model has not undergone instruction fine-tuning' on phi-2; 'a pretrained model that has not
# yet been instruction-tuned' on salamandra-7b). Checked before INS, which would otherwise match it. (6 Oct)
NOT_INSTR = re.compile(r"has not (yet )?(undergone|been) instruction", re.I)
# plural guard: 'instruction-tuned ... models' describes a family unless the sentence points at this repo
PLURAL = re.compile(r"instruct(ion)?[- ]?tuned[^.]{0,40}\bmodels\b", re.I)
THIS = re.compile(r"\bthis (repo|repository|model|release|checkpoint)\b|\bwe('re| are)? (providing|releasing)|\bthis is\b", re.I)
# 'pre-trained on 140+ languages' is a corpus-coverage bullet, not a statement that this checkpoint is the base.
PRE = re.compile(r"(pre-?trained (language )?model on|pre-?trained on (?![^.]{0,40}\blanguages\b)|this is the base model|pre-?trained only|not instruction-?tuned|base model (that|which) (has|was) not|pre-?training only|this pre-?trained (base )?(checkpoint|model)|pre-?trained base model for fine-?tuning)", re.I)
NAME_INSTR = {"instruct", "it", "chat", "sft", "dpo", "rlhf"}
NAME_PRE = {"pt", "pretrain", "pretrained"}   # 'base' is a size token (bert-base, whisper-base); not evidence


def class_from_yaml(row: Optional[dict]) -> tuple:
    """(class, evidence, relation). 'conversational' and sft/dpo/rlhf tags are not evidence."""
    if row is None:
        return "", "", ""
    tags = [t for t in (row.get("tags") or "").split("|") if t]
    it = [t for t in tags if t.lower() in INSTR_TAGS]
    pt = [t for t in tags if t.lower() in PRE_TAGS]
    rel = ""
    bm = _json(row.get("baseModels"), None)
    if isinstance(bm, dict) and bm.get("relation"):
        rel = bm["relation"]
    for t in tags:
        m = re.match(r"base_model:(finetune|adapter|merge|quantized):", t)
        if m and not rel:
            rel = m.group(1)
    if it and not pt:
        return "instruction", "tags=" + ",".join(it), rel
    if pt and not it:
        return "pretrained", "tags=" + ",".join(pt), rel
    if it and pt:
        return "", "tags_both=" + ",".join(it + pt), rel
    return "", "", rel


def _body(txt: str) -> str:
    if txt.startswith("---"):
        parts = txt.split("\n---", 1)
        txt = parts[1] if len(parts) > 1 else txt
    txt = strip_code(txt)
    return re.sub(r"`[^`\n]*`", " ", txt)


def _sentences(text: str):
    for s in re.split(r"(?<=[.!?])\s+|\n+", text):
        s = " ".join(s.split())
        if 15 <= len(s) <= 500:
            yield s


_HUB_LINK = re.compile(r"https?://huggingface\.co/([\w\-\.]+/[\w\-\.]+)")


def _about_another_repo(sentence: str, repo_id: str) -> bool:
    """True for a Markdown table row (| ... |) whose Hub links all point at repos other than this one.
    Model cards list their sibling releases in such tables (LFM2.5-350M-Base's card has a row
    'LFM2.5-350M | General-purpose instruction-tuned model'); that row describes the sibling."""
    if not repo_id or not sentence.startswith("|"):
        return False
    links = {m.group(1).lower().removesuffix(".git") for m in _HUB_LINK.finditer(sentence)}
    return bool(links) and repo_id.lower() not in links


def class_from_readme(readme: Optional[str], repo_id: str = "") -> tuple:
    """(class or None when unreadable, evidence). class is finetune | instruction | pretrained | conflict | ''.
    repo_id, when given, lets table rows that link only to other repos be skipped."""
    if readme_unreadable(readme):
        return None, ""
    ft, ins, pre = [], [], []
    for s in _sentences(_body(readme)):
        if EXCL.search(s) or _about_another_repo(s, repo_id):
            continue
        if NOT_INSTR.search(s):
            pre.append(s)
        elif INS_FT.search(s):
            ins.append(s)
        elif FT.search(s):
            ft.append(s)
        elif INS.search(s):
            if PLURAL.search(s) and not THIS.search(s):
                continue
            ins.append(s)
        elif PRE.search(s):
            pre.append(s)
    ev = lambda L: " || ".join(L[:2])
    if ft and ins:
        return "conflict", "FT: " + ev(ft) + " ## INS: " + ev(ins)
    if ft:
        return "finetune", ev(ft)
    if ins:
        return "instruction", ev(ins)
    if pre:
        return "pretrained", ev(pre)
    return "", ""


def class_from_name(repo_id: str) -> tuple:
    toks = re.split(r"[-_./]", repo_id.lower())
    if any(t in NAME_INSTR for t in toks):
        return "instruction", "token=" + ",".join(t for t in toks if t in NAME_INSTR)
    if any(t in NAME_PRE for t in toks):
        return "pretrained", "token=" + ",".join(t for t in toks if t in NAME_PRE)
    return "", ""


def parent_class(parent_id: str, parent_row: Optional[dict], parent_readme: Optional[str]) -> tuple:
    """(class_final, class_source, evidence). First hit wins: yaml, then README, then the repo-name token.
    class_final is instruction | pretrained | finetune | conflict | not_stated | unreadable.
    evidence is the tag list, the matched README sentence(s), or the name token that decided."""
    cy, ey, _rel = class_from_yaml(parent_row)
    cr, er = class_from_readme(parent_readme, parent_id)
    cn, en = class_from_name(parent_id)
    readable = cr is not None
    if cy:
        return cy, "yaml", ey
    if cr == "conflict":
        return "conflict", "readme", er
    if cr:
        return cr, "readme", er
    if cn:
        return cn, "name", en
    return ("not_stated", "", "") if readable else ("unreadable", "", "")


# ------------------------------------------------------------------ step 3 (continued): parent agrees with config.json
# The card declares a parent. The child's config.json describes the weights that were actually
# uploaded. If the two describe different networks, the card's parent claim is wrong and the
# model is removed ("parent_discordant"). Fields compared: architecture class, vocabulary size,
# hidden size, layer count. A missing or unreadable config on either side is its own reason.
_SHAPE_KEYS = ("vocab_size", "hidden_size", "num_hidden_layers")
VOCAB_ADDED_TOKENS_OK = 1024  # a child may add a few special tokens (pad, chat markers) and still be the same network


def _shape(cfg_text: str) -> Optional[dict]:
    """None when the file is absent on the Hub (cached as 'FETCH_ERR MISSING'), could not be
    fetched, or is not JSON."""
    if cfg_text.startswith("FETCH_ERR"):
        return None
    try:
        cfg = json.loads(cfg_text)
    except json.JSONDecodeError:
        return None
    text = cfg.get("text_config") if isinstance(cfg.get("text_config"), dict) else {}
    out = {"architecture": (cfg.get("architectures") or [""])[0]}
    for k in _SHAPE_KEYS:
        out[k] = cfg.get(k, text.get(k))
    return out


def _is_gated_err(text: str) -> bool:
    """True for the cache markers hub.py writes when the Hub answered 401/403: 'FETCH_ERR
    INACCESSIBLE_403', 'FETCH_ERR GATED:...', 'ERR GATED:HTTP_403'."""
    t = text.lstrip()
    for prefix in ("FETCH_ERR ", "ERR "):
        if t.startswith(prefix):
            t = t[len(prefix):]
    return t.startswith("INACCESSIBLE_") or t.startswith("GATED")


def _text_only_export(child_arch: str, parent_arch: str) -> bool:
    """True when the child is the language model of a multimodal parent saved without its vision
    encoder: `Qwen3_5ForCausalLM` from `Qwen3_5ForConditionalGeneration`. The language-model
    weights are the same network; the encoder only runs when an image is given, so text in gives
    the same text out. The reverse (a vision tower added to a text parent) stays a difference.
    Added 10 Oct 2026 on Mark's decision (13:40); see README code changes log."""
    return (child_arch.endswith("ForCausalLM") and parent_arch.endswith("ForConditionalGeneration")
            and child_arch[: -len("ForCausalLM")] == parent_arch[: -len("ForConditionalGeneration")])


def parent_discordant(child_cfg_text: str, parent_cfg_text: str) -> tuple:
    """(reason, detail). reason is keep | parent_discordant | config_unreadable | repo_gated.
    detail names the fields that differ, as 'field:child/parent', or says which side's
    config.json is unreadable and why (absent on the Hub, not fetched, not JSON). repo_gated:
    the Hub answered 401/403 for that side's config.json (gated or private repo the token is
    not approved for); access can be requested and the model refetched."""
    child, parent = _shape(child_cfg_text), _shape(parent_cfg_text)
    if child is None or parent is None:
        side, text = ("child", child_cfg_text) if child is None else ("parent", parent_cfg_text)
        if _is_gated_err(text):
            return "repo_gated", f"{side}: config.json behind a gate the token is not approved for"
        if text.startswith("FETCH_ERR MISSING"):
            why = "no config.json on the Hub"
        elif text.startswith("FETCH_ERR"):
            why = "fetch failed (" + text[len("FETCH_ERR "):].strip()[:40] + ")"
        else:
            why = "not JSON"
        return "config_unreadable", f"{side}: {why}"
    diffs, notes = [], []
    for k in ("architecture",) + _SHAPE_KEYS:
        a, b = child.get(k), parent.get(k)
        if a is None or b is None:
            continue  # field absent on one side (older config formats); not evidence either way
        if a == b:
            continue
        if k == "architecture" and _text_only_export(a, b):
            notes.append(f"architecture:{a} is the text-only export of {b}")
            continue
        if k == "vocab_size" and isinstance(a, int) and isinstance(b, int) and 0 < a - b <= VOCAB_ADDED_TOKENS_OK:
            notes.append(f"vocab_size:+{a - b} tokens added")  # fine-tuner added special tokens; same network
            continue
        diffs.append(f"{k}:{a}/{b}")
    return ("parent_discordant" if diffs else "keep"), ";".join(diffs + notes)
