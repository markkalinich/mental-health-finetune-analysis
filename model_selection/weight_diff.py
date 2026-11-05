"""Needs /home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python because the repository .venv has no torch or safetensors; this is the interpreter the GPU runner already uses (Python 3.11, torch 2.11.0, safetensors 0.8.0).

CPU-only weight-difference check. For each fine-tune, compare every safetensors
tensor with the same name in the stated parent. Load one tensor at a time.
Do not download weights and do not use the GPU.

Pairs, fine-tune directory then parent directory, under /home/mkalinich/hf_models/:

1. SpaceXerror__cognitive-ai-mental-health-7b vs mistralai__Mistral-7B-Instruct-v0.3
2. sujalrajpoot__TrueSyncAI-Aurion vs Qwen__Qwen2.5-3B-Instruct
3. lordChipotle__SuicidePreventionLlama vs meta-llama__Llama-3.2-3B-Instruct

For every 2-D matrix, in float32: relative Frobenius norm
||W_ft - W_parent|| / ||W_parent||, and whether that difference is exactly zero.
For q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, and down_proj at the
first, middle, and last layer, plus embed_tokens and lm_head when those tensors
exist and are 2-D, also the top singular values of the difference
(torch.linalg.svdvals). The run log records sigma_17/sigma_16, sigma_33/sigma_32,
and the fraction of squared Frobenius norm in the top 16 and top 32 singular values.

Usage:
  CUDA_VISIBLE_DEVICES='' /home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python \\
      model_selection/weight_diff.py
  CUDA_VISIBLE_DEVICES='' /home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python \\
      model_selection/weight_diff.py --pairs pairs.csv

`--pairs` reads columns finetune_dir, parent_dir. Without it, the hard-coded
PAIRS tuple is used. Tensors whose names or shapes do not match are skipped
and listed; the run stops for a pair only when zero tensors match.
"""

from __future__ import annotations

import argparse
import csv
import gc
import json
import os
import re
import statistics
import sys
import time
import traceback
from pathlib import Path

os.environ["CUDA_VISIBLE_DEVICES"] = ""

import torch
import safetensors
from safetensors import safe_open

HF_ROOT = Path("/home/mkalinich/hf_models")
OUT_DIR = Path("unset")  # set from the required --out
LOG_PATH = OUT_DIR / "run.log"

PAIRS = (
    (
        "SpaceXerror__cognitive-ai-mental-health-7b",
        "mistralai__Mistral-7B-Instruct-v0.3",
    ),
    (
        "sujalrajpoot__TrueSyncAI-Aurion",
        "Qwen__Qwen2.5-3B-Instruct",
    ),
    (
        "lordChipotle__SuicidePreventionLlama",
        "meta-llama__Llama-3.2-3B-Instruct",
    ),
)

PROJECTIONS = (
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
)

LAYER_RE = re.compile(r"\.layers\.(\d+)\.")

CSV_FIELDS = (
    "finetune",
    "parent",
    "tensor_name",
    "shape",
    "ndim",
    "dtype_finetune",
    "dtype_parent",
    "numel",
    "n_nonzero_diff",
    "exact_zero",
    "diff_frobenius",
    "parent_frobenius",
    "rel_frobenius",
    "svd_sampled",
    "n_singular_values",
    "sigma_1",
    "sigma_16",
    "sigma_17",
    "sigma_17_over_sigma_16",
    "sigma_32",
    "sigma_33",
    "sigma_33_over_sigma_32",
    "energy_top16",
    "energy_top32",
    "sigma_9_over_sigma_8",
    "sigma_65_over_sigma_64",
    "sigma_129_over_sigma_128",
    "sigma_257_over_sigma_256",
    "energy_top8",
    "energy_top64",
    "energy_top128",
    "energy_top256",
    "top64_singular_values",
    "top512_singular_values",
    "skip_reason",
)


class PairError(RuntimeError):
    """This pair cannot be compared. The batch continues."""


def log(message: str) -> None:
    print(message, flush=True)
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(message + "\n")


def fail(message: str) -> None:
    print(message, file=sys.stderr, flush=True)
    log("ERROR " + message)
    sys.exit(1)


def fmt(value: float | None) -> str:
    if value is None:
        return ""
    if value != value:  # NaN
        return "nan"
    return format(value, ".8e")


def weight_map_for(model_dir: Path) -> dict[str, str]:
    index_path = model_dir / "model.safetensors.index.json"
    if not index_path.is_file():
        singles = sorted(p.name for p in model_dir.glob("*.safetensors"))
        if len(singles) != 1:
            bins = sorted(p.name for p in model_dir.glob("pytorch_model*.bin"))
            raise PairError(
                f"{model_dir.name} has no model.safetensors.index.json and {len(singles)} "
                f"safetensors files ({singles}). pytorch bins: {bins}. "
                "Refusing to guess which file to read."
            )
        with safe_open(str(model_dir / singles[0]), framework="pt", device="cpu") as handle:
            return {key: singles[0] for key in handle.keys()}
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    weight_map = payload.get("weight_map")
    if not isinstance(weight_map, dict) or not weight_map:
        raise PairError(f"{index_path} has no weight_map")
    return {str(name): str(shard) for name, shard in weight_map.items()}


def tensor_metadata(model_dir: Path, weight_map: dict[str, str]) -> dict[str, dict]:
    by_shard: dict[str, list[str]] = {}
    for name, shard in weight_map.items():
        by_shard.setdefault(shard, []).append(name)
    meta: dict[str, dict] = {}
    missing: list[str] = []
    for shard, names in sorted(by_shard.items()):
        path = model_dir / shard
        if not path.is_file():
            raise PairError(f"missing shard {path}")
        with safe_open(str(path), framework="pt", device="cpu") as handle:
            present = set(handle.keys())
            for name in names:
                if name not in present:
                    missing.append(f"{name} listed in the index but absent from {shard}")
                    continue
                sliver = handle.get_slice(name)
                shape = tuple(int(dim) for dim in sliver.get_shape())
                numel = 1
                for dim in shape:
                    numel *= dim
                meta[name] = {
                    "shape": shape,
                    "dtype": str(sliver.get_dtype()),
                    "shard": shard,
                    "numel": numel,
                }
    if missing:
        raise PairError("index entries missing from shards:\n" + "\n".join(missing))
    return meta


class ShardCache:
    """Keep safetensors files mapped. get() still copies one tensor."""

    def __init__(self, model_dir: Path):
        self.model_dir = model_dir
        self._open: dict[str, object] = {}

    def get(self, shard: str, name: str) -> torch.Tensor:
        handle = self._open.get(shard)
        if handle is None:
            handle = safe_open(str(self.model_dir / shard), framework="pt", device="cpu")
            handle.__enter__()
            self._open[shard] = handle
        tensor = handle.get_tensor(name)
        if tensor.device.type != "cpu":
            raise PairError(f"{name} from {self.model_dir / shard} loaded on {tensor.device}, not CPU")
        return tensor

    def close(self) -> None:
        for handle in self._open.values():
            handle.__exit__(None, None, None)
        self._open.clear()


def layer_indexes(names: list[str]) -> list[int]:
    found = set()
    for name in names:
        match = LAYER_RE.search(name)
        if match:
            found.add(int(match.group(1)))
    return sorted(found)


def names_for_projection(names: list[str], layer: int, projection: str) -> list[str]:
    needle = f".layers.{layer}."
    suffix = f".{projection}.weight"
    return [name for name in names if needle in name and name.endswith(suffix)]


def prefer_language_hit(hits: list[str]) -> str | None:
    """One tensor when the name is unique. Prefer the language-model copy."""
    if len(hits) == 1:
        return hits[0]
    if not hits:
        return None
    language = [name for name in hits if "language_model" in name]
    if len(language) == 1:
        return language[0]
    text = [
        name
        for name in hits
        if "vision_tower" not in name and "audio_tower" not in name and "vision_model" not in name
    ]
    if len(text) == 1:
        return text[0]
    return None


def sample_names(names: list[str]) -> tuple[list[str], list[int], list[str]]:
    layers = layer_indexes(names)
    notes: list[str] = []
    if not layers:
        notes.append("no .layers.<N>. tensors; singular values not computed")
        return [], [], notes
    middle = layers[len(layers) // 2]
    chosen_layers = [layers[0], middle, layers[-1]]
    selected: list[str] = []
    for layer in chosen_layers:
        for projection in PROJECTIONS:
            hits = names_for_projection(names, layer, projection)
            label = f"layers.{layer}.{projection}.weight"
            chosen = prefer_language_hit(hits)
            if chosen is None:
                notes.append(f"{label}: found {hits}")
            else:
                selected.append(chosen)
    for suffix in ("embed_tokens.weight", "lm_head.weight"):
        hits = [name for name in names if name.endswith(suffix)]
        chosen = prefer_language_hit(hits)
        if chosen is None and hits:
            notes.append(f"{suffix}: found {hits}")
        elif chosen is not None:
            selected.append(chosen)
    return selected, chosen_layers, notes


def singular_value_report(diff: torch.Tensor) -> dict[str, str]:
    """Top singular values of a float32 difference. Empty ratios when undefined."""
    if diff.ndim != 2:
        return {}
    n_sv_possible = min(diff.shape)
    if n_sv_possible < 1:
        return {}
    if torch.count_nonzero(diff).item() == 0:
        zeros = " ".join(["0.00000000e+00"] * min(64, n_sv_possible))
        return {
            "n_singular_values": str(n_sv_possible),
            "sigma_1": "0.00000000e+00",
            "sigma_16": "0.00000000e+00" if n_sv_possible >= 16 else "",
            "sigma_17": "0.00000000e+00" if n_sv_possible >= 17 else "",
            "sigma_17_over_sigma_16": "",
            "sigma_32": "0.00000000e+00" if n_sv_possible >= 32 else "",
            "sigma_33": "0.00000000e+00" if n_sv_possible >= 33 else "",
            "sigma_33_over_sigma_32": "",
            "energy_top16": "",
            "energy_top32": "",
            "top64_singular_values": zeros,
            "note": "difference is the zero matrix; ratios and energy fractions are undefined",
        }
    singular = torch.linalg.svdvals(diff.contiguous())
    values = [float(item) for item in singular.detach().cpu().tolist()]
    squares = [value * value for value in values]
    total = sum(squares)

    def ratio(later: int, earlier: int) -> str:
        # later/earlier are 1-based singular-value indexes.
        if len(values) < later or values[earlier - 1] == 0.0:
            return ""
        return fmt(values[later - 1] / values[earlier - 1])

    def energy(k: int) -> str:
        if total == 0.0 or len(squares) < k:
            return ""
        return fmt(sum(squares[:k]) / total)

    report = {
        "n_singular_values": str(len(values)),
        "sigma_1": fmt(values[0]),
        "sigma_16": fmt(values[15]) if len(values) >= 16 else "",
        "sigma_17": fmt(values[16]) if len(values) >= 17 else "",
        "sigma_17_over_sigma_16": ratio(17, 16),
        "sigma_32": fmt(values[31]) if len(values) >= 32 else "",
        "sigma_33": fmt(values[32]) if len(values) >= 33 else "",
        "sigma_33_over_sigma_32": ratio(33, 32),
        "energy_top16": energy(16),
        "energy_top32": energy(32),
        "sigma_9_over_sigma_8": ratio(9, 8),
        "sigma_65_over_sigma_64": ratio(65, 64),
        "sigma_129_over_sigma_128": ratio(129, 128),
        "sigma_257_over_sigma_256": ratio(257, 256),
        "energy_top8": energy(8),
        "energy_top64": energy(64),
        "energy_top128": energy(128),
        "energy_top256": energy(256),
        "top64_singular_values": " ".join(fmt(value) for value in values[:64]),
        "top512_singular_values": " ".join(fmt(value) for value in values[:512]),
        "note": "",
    }
    del singular
    return report


def compare_pair(finetune_name: str, parent_name: str) -> None:
    finetune_dir = HF_ROOT / finetune_name
    parent_dir = HF_ROOT / parent_name
    log("")
    log(f"PAIR {finetune_name} vs {parent_name}")
    started = time.perf_counter()
    ft_map = weight_map_for(finetune_dir)
    parent_map = weight_map_for(parent_dir)
    ft_files = sorted({p.name for p in finetune_dir.glob("*.safetensors")})
    parent_files = sorted({p.name for p in parent_dir.glob("*.safetensors")})
    ft_used = sorted(set(ft_map.values()))
    parent_used = sorted(set(parent_map.values()))
    log(f"finetune shards read: {ft_used}")
    log(f"finetune safetensors not read: {sorted(set(ft_files) - set(ft_used))}")
    log(f"parent shards read: {parent_used}")
    log(f"parent safetensors not read: {sorted(set(parent_files) - set(parent_used))}")

    ft_meta = tensor_metadata(finetune_dir, ft_map)
    parent_meta = tensor_metadata(parent_dir, parent_map)
    only_ft = sorted(set(ft_meta) - set(parent_meta))
    only_parent = sorted(set(parent_meta) - set(ft_meta))
    shape_mismatches: list[str] = []
    names: list[str] = []
    for name in sorted(set(ft_meta) & set(parent_meta)):
        if ft_meta[name]["shape"] != parent_meta[name]["shape"]:
            shape_mismatches.append(name)
        else:
            names.append(name)
    log(
        "skipped "
        f"only_in_finetune={len(only_ft)} "
        f"only_in_parent={len(only_parent)} "
        f"shape_mismatch={len(shape_mismatches)} "
        f"compared={len(names)}"
    )
    for name in only_ft:
        log(f"skipped only in finetune: {name} shape {ft_meta[name]['shape']}")
    for name in only_parent:
        log(f"skipped only in parent: {name} shape {parent_meta[name]['shape']}")
    for name in shape_mismatches:
        log(
            f"skipped shape mismatch: {name} "
            f"finetune {ft_meta[name]['shape']} parent {parent_meta[name]['shape']}"
        )
    if not names:
        skip_rows: list[dict[str, str]] = []
        for name in only_ft:
            skip_rows.append(
                skip_row(finetune_name, parent_name, name, ft_meta[name]["shape"], "only in fine-tune")
            )
        for name in only_parent:
            skip_rows.append(
                skip_row(finetune_name, parent_name, name, parent_meta[name]["shape"], "only in parent")
            )
        for name in shape_mismatches:
            skip_rows.append(
                skip_row(
                    finetune_name,
                    parent_name,
                    name,
                    ft_meta[name]["shape"],
                    "shape mismatch: fine-tune "
                    + "x".join(str(dim) for dim in ft_meta[name]["shape"])
                    + " parent "
                    + "x".join(str(dim) for dim in parent_meta[name]["shape"]),
                )
            )
        write_rows(OUT_DIR / f"{finetune_name}.csv", skip_rows)
        raise PairError(
            f"{finetune_name} vs {parent_name}: zero tensors match "
            f"(only in finetune {len(only_ft)}, only in parent {len(only_parent)}, "
            f"shape mismatch {len(shape_mismatches)})"
        )

    selected, chosen_layers, sample_notes = sample_names(names)
    for note in sample_notes:
        log(f"svd sample note: {note}")
    selected_set = set(selected)
    compared_ft = [ft_meta[name] for name in names]
    compared_parent = [parent_meta[name] for name in names]
    ft_dtypes = sorted({item["dtype"] for item in compared_ft})
    parent_dtypes = sorted({item["dtype"] for item in compared_parent})
    n_params = sum(item["numel"] for item in compared_ft)
    log(f"tensors {len(names)} parameters {n_params}")
    log(f"finetune safetensors dtypes {ft_dtypes}")
    log(f"parent safetensors dtypes {parent_dtypes}")
    log(f"svd layers (0-based indexes) {chosen_layers}")
    log(f"svd modules ({len(selected)}):")
    for name in selected:
        log(f"  {name} shape {ft_meta[name]['shape']}")

    rows: list[dict[str, str]] = []
    for name in only_ft:
        rows.append(
            skip_row(
                finetune_name,
                parent_name,
                name,
                ft_meta[name]["shape"],
                "only in fine-tune",
            )
        )
    for name in only_parent:
        rows.append(
            skip_row(
                finetune_name,
                parent_name,
                name,
                parent_meta[name]["shape"],
                "only in parent",
            )
        )
    for name in shape_mismatches:
        rows.append(
            skip_row(
                finetune_name,
                parent_name,
                name,
                ft_meta[name]["shape"],
                "shape mismatch: fine-tune "
                + "x".join(str(dim) for dim in ft_meta[name]["shape"])
                + " parent "
                + "x".join(str(dim) for dim in parent_meta[name]["shape"]),
            )
        )
    ft_cache = ShardCache(finetune_dir)
    parent_cache = ShardCache(parent_dir)
    try:
        for index, name in enumerate(names, start=1):
            ft_raw = ft_cache.get(ft_map[name], name)
            parent_raw = parent_cache.get(parent_map[name], name)
            ft_dtype = str(ft_raw.dtype)
            parent_dtype = str(parent_raw.dtype)
            if not ft_raw.dtype.is_floating_point or not parent_raw.dtype.is_floating_point:
                rows.append(
                    skip_row(
                        finetune_name,
                        parent_name,
                        name,
                        ft_meta[name]["shape"],
                        f"not floating point ({ft_dtype} vs {parent_dtype})",
                    )
                )
                log(f"[{index}/{len(names)}] {name} skipped not floating point")
                del ft_raw, parent_raw
                gc.collect()
                continue
            ft = ft_raw.float()
            parent = parent_raw.float()
            del ft_raw, parent_raw
            diff = ft - parent
            n_nonzero = int(torch.count_nonzero(diff).item())
            exact = n_nonzero == 0
            row = {
            "finetune": finetune_name,
            "parent": parent_name,
            "tensor_name": name,
            "shape": "x".join(str(dim) for dim in ft_meta[name]["shape"]),
            "ndim": str(diff.ndim),
            "dtype_finetune": ft_dtype,
            "dtype_parent": parent_dtype,
            "numel": str(ft_meta[name]["numel"]),
            "n_nonzero_diff": str(n_nonzero),
            "exact_zero": "1" if exact else "0",
            "diff_frobenius": "",
            "parent_frobenius": "",
            "rel_frobenius": "",
            "svd_sampled": "1" if name in selected_set else "0",
            "n_singular_values": "",
            "sigma_1": "",
            "sigma_16": "",
            "sigma_17": "",
            "sigma_17_over_sigma_16": "",
            "sigma_32": "",
            "sigma_33": "",
            "sigma_33_over_sigma_32": "",
            "energy_top16": "",
            "energy_top32": "",
            "top64_singular_values": "",
            "skip_reason": "",
            }
            rel_display = ""
            if diff.ndim == 2:
                diff_norm = float(torch.linalg.norm(diff, ord="fro").item())
                parent_norm = float(torch.linalg.norm(parent, ord="fro").item())
                row["diff_frobenius"] = fmt(diff_norm)
                row["parent_frobenius"] = fmt(parent_norm)
                if parent_norm == 0.0:
                    row["rel_frobenius"] = "" if diff_norm != 0.0 else fmt(0.0)
                    rel_display = "parent_frobenius_zero"
                else:
                    rel = diff_norm / parent_norm
                    row["rel_frobenius"] = fmt(rel)
                    rel_display = row["rel_frobenius"]
            if name in selected_set and diff.ndim == 2:
                report = singular_value_report(diff)
                note = report.pop("note", "")
                for key, value in report.items():
                    row[key] = value
                if note:
                    log(f"  note {name}: {note}")
            elif name in selected_set:
                log(f"  note {name}: not 2-D (ndim {diff.ndim}); singular values not computed")
            log(
                f"[{index}/{len(names)}] {name} exact_zero={row['exact_zero']} "
                f"rel_frobenius={rel_display or '-'} svd={row['svd_sampled']}"
            )
            rows.append(row)
            del ft, parent, diff
            gc.collect()
    finally:
        ft_cache.close()
        parent_cache.close()

    csv_path = OUT_DIR / f"{finetune_name}.csv"
    write_rows(csv_path, rows)
    summarize(rows, finetune_name, n_params, time.perf_counter() - started, csv_path)


def skip_row(
    finetune_name: str,
    parent_name: str,
    tensor_name: str,
    shape: tuple[int, ...],
    reason: str,
) -> dict[str, str]:
    row = {field: "" for field in CSV_FIELDS}
    row["finetune"] = finetune_name
    row["parent"] = parent_name
    row["tensor_name"] = tensor_name
    row["shape"] = "x".join(str(dim) for dim in shape)
    row["svd_sampled"] = "0"
    row["skip_reason"] = reason
    return row


def write_rows(csv_path: Path, rows: list[dict[str, str]]) -> None:
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def summarize(
    rows: list[dict[str, str]],
    finetune_name: str,
    n_params: int,
    seconds: float,
    csv_path: Path,
) -> None:
    rows = [row for row in rows if not row.get("skip_reason")]
    matrices = [row for row in rows if row["ndim"] == "2"]
    vectors = [row for row in rows if row["ndim"] != "2"]
    zero_matrices = [row for row in matrices if row["exact_zero"] == "1"]
    nonzero_matrices = [row for row in matrices if row["exact_zero"] != "1"]
    rels = [float(row["rel_frobenius"]) for row in matrices if row["rel_frobenius"]]
    log(f"SUMMARY {finetune_name}")
    log(f"parameters {n_params}")
    log(
        "dtypes finetune "
        + ",".join(sorted({row['dtype_finetune'] for row in rows}))
        + " parent "
        + ",".join(sorted({row['dtype_parent'] for row in rows}))
    )
    log(
        f"2d {len(matrices)} exact_zero {len(zero_matrices)} nonzero {len(nonzero_matrices)}"
    )
    if rels:
        log(
            "rel_frobenius "
            f"min {fmt(min(rels))} median {fmt(statistics.median(rels))} max {fmt(max(rels))}"
        )
    log(
        f"non_2d {len(vectors)} exact_zero {sum(row['exact_zero'] == '1' for row in vectors)} "
        f"nonzero {sum(row['exact_zero'] != '1' for row in vectors)}"
    )
    log("SVD")
    for row in rows:
        if row["svd_sampled"] != "1":
            continue
        log(
            "  {name} shape {shape} rel {rel} exact_zero {zero} "
            "sigma1 {s1} sigma16 {s16} sigma17 {s17} ratio17/16 {r17} "
            "sigma32 {s32} sigma33 {s33} ratio33/32 {r33} "
            "energy16 {e16} energy32 {e32}".format(
                name=row["tensor_name"],
                shape=row["shape"],
                rel=row["rel_frobenius"] or "-",
                zero=row["exact_zero"],
                s1=row["sigma_1"] or "-",
                s16=row["sigma_16"] or "-",
                s17=row["sigma_17"] or "-",
                r17=row["sigma_17_over_sigma_16"] or "-",
                s32=row["sigma_32"] or "-",
                s33=row["sigma_33"] or "-",
                r33=row["sigma_33_over_sigma_32"] or "-",
                e16=row["energy_top16"] or "-",
                e32=row["energy_top32"] or "-",
            )
        )
    log(f"wrote {csv_path}")
    log(f"elapsed_seconds {seconds:.1f}")


def load_pairs_csv(path: Path) -> tuple[tuple[str, str], ...]:
    if not path.is_file():
        fail(f"pairs CSV not found: {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        if "finetune_dir" not in fields or "parent_dir" not in fields:
            fail(f"{path} needs columns finetune_dir, parent_dir (found {fields})")
        pairs = []
        for row in reader:
            finetune_name = (row.get("finetune_dir") or "").strip()
            parent_name = (row.get("parent_dir") or "").strip()
            if not finetune_name or not parent_name:
                fail(f"blank pair row in {path}: {row}")
            pairs.append((finetune_name, parent_name))
    if not pairs:
        fail(f"{path} has no pairs")
    return tuple(pairs)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pairs",
        type=Path,
        default=None,
        help="CSV with columns finetune_dir, parent_dir. Default is the built-in PAIRS tuple.",
    )
    parser.add_argument(
        "names",
        nargs="*",
        help="With the built-in list, run only pairs whose directory name is one of these.",
    )
    parser.add_argument("--out", type=Path, required=True, help="Output folder, e.g. outputs/weight-diff/<date>.")
    args = parser.parse_args()
    global OUT_DIR, LOG_PATH
    OUT_DIR = args.out
    LOG_PATH = OUT_DIR / "run.log"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.pairs is None and LOG_PATH.exists():
        LOG_PATH.unlink()
    if torch.cuda.is_available():
        fail("CUDA is available after CUDA_VISIBLE_DEVICES=''; refusing to run")
    log(f"interpreter {sys.executable}")
    log(f"python {sys.version.split()[0]}")
    log(f"torch {torch.__version__}")
    log(f"safetensors {safetensors.__version__}")
    log(f"cuda_available {torch.cuda.is_available()}")
    log(f"torch_threads {torch.get_num_threads()}")
    log("device cpu")
    if args.pairs is not None:
        pairs = load_pairs_csv(args.pairs)
        log(f"pairs_csv {args.pairs} count {len(pairs)}")
    else:
        pairs = PAIRS
        if args.names:
            pairs = tuple(
                pair for pair in PAIRS if pair[0] in args.names or pair[1] in args.names
            )
            if not pairs:
                fail(f"no pairs matched {args.names}")
    failed: list[str] = []
    for finetune_name, parent_name in pairs:
        try:
            compare_pair(finetune_name, parent_name)
        except PairError as exc:
            message = str(exc)
            print(message, file=sys.stderr, flush=True)
            log("ERROR " + message)
            csv_path = OUT_DIR / f"{finetune_name}.csv"
            if not csv_path.exists():
                write_rows(
                    csv_path,
                    [skip_row(finetune_name, parent_name, "", (), message)],
                )
            failed.append(finetune_name)
        except Exception:
            message = traceback.format_exc()
            print(message, file=sys.stderr, flush=True)
            log("ERROR " + message)
            failed.append(finetune_name)
    log("")
    if failed:
        log("FAILED " + " ".join(failed))
        log("DONE")
        sys.exit(1)
    log("DONE")


if __name__ == "__main__":
    main()
