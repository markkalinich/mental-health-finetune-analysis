"""GGUF tokenizer.chat_template extraction (local file or partial HF bytes)."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from collections import OrderedDict
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
from gguf import GGUFReader
from gguf.constants import GGUFValueType
from gguf.gguf_reader import GGUF_MAGIC, ReaderField

PARTIAL_BYTE_SIZES = (
    8 * 1024 * 1024,
    16 * 1024 * 1024,
    32 * 1024 * 1024,
    64 * 1024 * 1024,
)


def template_from_fields(fields) -> Tuple[bool, str]:
    field = fields.get("tokenizer.chat_template")
    if field is None:
        return False, ""
    val = field.parts[field.data[0]]
    if hasattr(val, "tobytes"):
        val = val.tobytes().decode("utf-8", errors="replace")
    elif isinstance(val, bytes):
        val = val.decode("utf-8", errors="replace")
    else:
        val = str(val)
    return True, val


def template_from_reader(reader: GGUFReader) -> Tuple[bool, str]:
    return template_from_fields(reader.fields)


def _kv_fields_only(path: Path, max_bytes: Optional[int] = None) -> OrderedDict:
    """Parse GGUF KV metadata only (no tensor payload) — safe for partial Range downloads."""
    data = np.memmap(path, mode="r")
    if max_bytes is not None:
        data = data[:max_bytes]

    reader = GGUFReader.__new__(GGUFReader)
    reader.data = data
    reader.alignment = 32
    reader.fields = OrderedDict()
    reader.tensors = []

    offs = 0
    if reader._get(offs, np.uint32, override_order="<")[0] != GGUF_MAGIC:
        raise ValueError("GGUF magic invalid")
    offs += 4

    temp_version = reader._get(offs, np.uint32)
    reader.byte_order = "I"
    if temp_version[0] & 65535 == 0:
        reader.byte_order = "S"
        temp_version = temp_version.view(temp_version.dtype.newbyteorder(reader.byte_order))

    if temp_version[0] not in (2, 3):
        raise ValueError(f"Unsupported GGUF version {temp_version[0]}")

    from gguf.constants import GGUFEndian

    if sys.byteorder == "little":
        host_endian = GGUFEndian.LITTLE
        swapped_endian = GGUFEndian.BIG
    else:
        host_endian = GGUFEndian.BIG
        swapped_endian = GGUFEndian.LITTLE
    reader.endianess = swapped_endian if reader.byte_order == "S" else host_endian

    offs += reader._push_field(
        ReaderField(offs, "GGUF.version", [temp_version], [0], [GGUFValueType.UINT32])
    )
    temp_counts = reader._get(offs, np.uint64, 2)
    offs += reader._push_field(
        ReaderField(offs, "GGUF.tensor_count", [temp_counts[:1]], [0], [GGUFValueType.UINT64])
    )
    offs += reader._push_field(
        ReaderField(offs, "GGUF.kv_count", [temp_counts[1:]], [0], [GGUFValueType.UINT64])
    )
    kv_count = int(temp_counts[1])
    reader._build_fields(offs, kv_count)
    return reader.fields


def extract_chat_template(gguf_path: Path) -> Tuple[bool, str]:
    return template_from_reader(GGUFReader(str(gguf_path)))


def extract_chat_template_partial(gguf_path: Path) -> Tuple[bool, str]:
    last_err: Optional[Exception] = None
    for size in PARTIAL_BYTE_SIZES:
        try:
            fields = _kv_fields_only(gguf_path, max_bytes=size)
            return template_from_fields(fields)
        except Exception as exc:
            last_err = exc
    raise RuntimeError(f"Partial GGUF metadata parse failed for {gguf_path}: {last_err}")


def template_sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def fetch_hf_gguf_header(repo: str, filename: str, max_bytes: int = 8 * 1024 * 1024) -> Path:
    """Download GGUF metadata/header region via HTTP Range."""
    url = f"https://huggingface.co/{repo}/resolve/main/{filename}"
    tmp = Path(tempfile.mkstemp(suffix=".gguf.partial", prefix="hf_template_")[1])
    end = max_bytes - 1
    proc = subprocess.run(
        [
            "curl",
            "-sfL",
            "-H",
            f"Range: bytes=0-{end}",
            "-o",
            str(tmp),
            url,
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if proc.returncode != 0:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"HF Range fetch failed for {repo}/{filename}: {proc.stderr or proc.stdout}")
    if tmp.stat().st_size == 0:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"HF Range fetch returned empty body for {repo}/{filename}")
    return tmp


def extract_hf_chat_template(repo: str, filename: str) -> Tuple[bool, str]:
    last_err: Optional[Exception] = None
    for size in PARTIAL_BYTE_SIZES:
        tmp: Optional[Path] = None
        try:
            tmp = fetch_hf_gguf_header(repo, filename, max_bytes=size)
            return extract_chat_template_partial(tmp)
        except Exception as exc:
            last_err = exc
            continue
        finally:
            if tmp is not None:
                tmp.unlink(missing_ok=True)
    raise RuntimeError(f"HF template extract failed for {repo}/{filename}: {last_err}")
