"""Read a reply against the label shape on that model's card.

A parsed row means the reply has the card's label. It is not a score
against the sentence's gold label.
"""
from __future__ import annotations

import json
import re
from typing import Any, Dict, Optional, Sequence

from safety_labels.prompts import RAILZ_CATEGORIES, TINYSAFE_CATEGORIES

_THINK = re.compile(r"<think>.*?</think>", re.IGNORECASE | re.DOTALL)
_FLEX_CODES = ("VIO", "ILG", "SEX", "INF", "DIS", "MIS", "JAIL")
_HARM = re.compile(r"Harm:\s*(harmful|safe)\b")


def parse_reply(
    kind: str,
    content: str,
    *,
    railz_categories: Sequence[str] = RAILZ_CATEGORIES,
) -> Dict[str, Any]:
    text = "" if content is None else str(content)
    if kind == "shield":
        return _exact(text, ("safe", "unsafe"))
    if kind == "banana":
        return _banana(text)
    if kind == "aims":
        return _aims(text)
    if kind == "flexguard":
        return _flexguard(text)
    if kind == "tinysafe":
        return _tinysafe(text)
    if kind == "railz":
        return _railz(text, tuple(railz_categories))
    if kind == "dynaguard":
        return _dynaguard(text)
    raise ValueError(f"unknown format {kind}")


def _result(ok: bool, label: Optional[str], status: str, **extra: Any) -> Dict[str, Any]:
    return {"ok": ok, "label": label, "status": status, "extra": extra}


def _exact(content: str, allowed: Sequence[str]) -> Dict[str, Any]:
    text = content.strip()
    if text in allowed:
        return _result(True, text, "ok")
    return _result(False, None, "unparsed")


def _banana(content: str) -> Dict[str, Any]:
    lines = [line.strip() for line in content.strip().splitlines() if line.strip()]
    if lines == ["Safe"]:
        return _result(True, "Safe", "ok")
    if (
        len(lines) == 2
        and lines[0] == "Unsafe"
        and lines[1].startswith("Violated Categories:")
        and lines[1].split(":", 1)[1].strip()
    ):
        return _result(True, "Unsafe", "ok", categories=lines[1].split(":", 1)[1].strip())
    return _result(False, None, "unparsed")


def _aims(content: str) -> Dict[str, Any]:
    hits = _HARM.findall(content)
    if len(hits) == 1:
        return _result(True, hits[0], "ok")
    return _result(False, None, "unparsed")


def _flexguard(content: str) -> Dict[str, Any]:
    body = _THINK.sub("", content).strip()
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if len(lines) != 2:
        return _result(False, None, "unparsed")
    category = _flex_category(lines[0])
    if category is None or not re.fullmatch(r"\d{1,3}", lines[1]):
        return _result(False, None, "unparsed")
    score = int(lines[1])
    if score > 100:
        return _result(False, None, "unparsed")
    return _result(True, category, "ok", risk_score=score)


def _flex_category(line: str) -> Optional[str]:
    if line == "SAFE":
        return "SAFE"
    parts = [part.strip() for part in line.split(",")]
    if not parts or len(parts) != len(set(parts)):
        return None
    if any(part not in _FLEX_CODES for part in parts):
        return None
    return ",".join(parts)


def _tinysafe(content: str) -> Dict[str, Any]:
    obj = _json_object(content)
    if obj is None:
        return _result(False, None, "unparsed")
    if not {"safe", "categories", "reasoning"}.issubset(obj):
        return _result(False, None, "unparsed")
    safe = obj["safe"]
    categories = obj["categories"]
    reasoning = obj["reasoning"]
    if not isinstance(safe, bool) or not isinstance(reasoning, str) or not reasoning.strip():
        return _result(False, None, "unparsed")
    if not isinstance(categories, list) or any(not isinstance(item, str) for item in categories):
        return _result(False, None, "unparsed")
    allowed = set(TINYSAFE_CATEGORIES)
    if any(item not in allowed for item in categories):
        return _result(False, None, "unparsed")
    if safe and categories:
        return _result(False, None, "unparsed")
    if not safe and not categories:
        return _result(False, None, "unparsed")
    label = "safe" if safe else "unsafe"
    return _result(True, label, "ok", categories=categories)


def _json_object(content: str) -> Optional[dict]:
    raw = content.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    start = raw.find("{")
    end = raw.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        obj = json.loads(raw[start : end + 1])
    except json.JSONDecodeError:
        return None
    return obj if isinstance(obj, dict) else None


def _railz_hits(text: str, categories: Sequence[str]):
    found = []
    bad = False
    allowed = set(categories)
    for line in text.splitlines():
        line = line.strip()
        if line == "no listed category applies":
            found.append(line)
        elif line.startswith("Violated category:"):
            name = line.split(":", 1)[1].strip()
            if name in allowed:
                found.append("Violated category: " + name)
            else:
                bad = True
    return found, bad


def _railz(content: str, categories: Sequence[str]) -> Dict[str, Any]:
    outside, bad = _railz_hits(_THINK.sub("", content), categories)
    if bad or len(outside) > 1:
        return _result(False, None, "unparsed")
    if len(outside) == 1:
        return _result(True, outside[0], "ok")
    inside, bad_inside = _railz_hits(content, categories)
    if bad_inside or len(inside) != 1:
        return _result(False, None, "unparsed")
    return _result(True, inside[0], "ok")


def _dynaguard(content: str) -> Dict[str, Any]:
    text = content.strip()
    text = re.sub(r"^</?answer>\s*", "", text, flags=re.IGNORECASE).strip()
    if text in ("PASS", "FAIL"):
        return _result(True, text, "ok")
    return _result(False, None, "unparsed")
