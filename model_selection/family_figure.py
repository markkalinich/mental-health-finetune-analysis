#!/usr/bin/env python
"""Model-lineage figure in the layout of the paper's Figure 1
(analysis/model_coverage_heatmap.py): one panel per pre-training lineage
version, columns = parameter size, rows = Instruction-Tuned /
Mental Health FT / Medical FT / Safety FT. The Pre-trained row is drawn when
orchestration.study_roster.DRAW_PRETRAINED is true.

The panel title is the family plus the version. Mistral titles drop the "7B"
(the size is the column label): "Mistral v0.1". The TinyLlama 32k panel title
drops the author; the footer names Doctor-Shotgun. A title wider than its
columns wraps onto two lines instead of stretching the panel. Versions of one
family sit a small gap apart. A change of family gets a larger gap. Panels are
packed into rows by width (see MAX_ROW_WIDTH), with two placements that
ignore that cap. The top row is Gemma, then every Qwen version. The next row
starts at the left with Llama, Mistral, and SmolLM. A continued pre-training
stays a column inside its parent's panel.

Inputs (read only):
  outputs/roster/<date>/roster.csv
      fine-tunes on the study roster. The date is outputs/roster/CURRENT.
  docs/mental_health_FT_funnel/archive/2026-10-06/parent-bases-2026-10-06.md  "Parent table": hand review of the
                                              mental-health parents' pre-trained bases
  cache/readmes/<owner>__<name>__<date>.md    parent README text (newest date used)
  cache/cards/*.csv                           Hub card rows (cardData, baseModels,
                                              safetensors, siblings, gated, status)

Outputs (publish_manuscript_figures.py sets its own paths; a standalone run uses these):
  outputs/cross-grouping/<CURRENT>/family_table.csv
  outputs/cross-grouping/<CURRENT>/family_heatmap.png

The script first builds family_table.csv, then draws the figure from that CSV.
It exits non-zero and prints every offending value to stderr when a parent repo
id cannot be classified, when a parent is a pre-trained checkpoint rather than
an instruction-tuned model, when a hand-written card reading disagrees with the
cached card, or when a roster fine-tune's family, version, and size disagree
with classify_parent on its parent id.

Row 'Base Model' is 1 only when the instruction-tuned parent's own card names a
pre-trained (not instruction-tuned) repo AND that repo is readable (public or
gated) AND it has full-precision weights at the root. For parents in the review
doc's Parent table the three answers come from the table. For every other
parent the card reading is written out by hand below (CARD_READING), the script
checks that the reading matches the cached card, and the base repo is checked
against cache/cards. A base that is not in the cache is 'named_not_checked' in the CSV. The figure
draws that cell empty: the picture shows a base only when the weights are
available. A named base that returns 404 is 'named_404' in the CSV and is
drawn grey, the same as a card that names no base: not available, to anyone.
Exception (Mark Kalinich, 6 Oct): when the card names no base but the vendor
publishes the base under the matching name (Llama-3.2-3B for Llama-3.2-3B-
Instruct, and so on), the sibling repo counts as the base once a Hub check has
confirmed it exists with full-precision root weights (SIBLING_BASE_2026_10_06).
Those cells are 1 with status 'yes_sibling'; family_table.csv records the check.

Rehosts (unsloth/..., NousResearch/Llama-2-7b-chat-hf) are counted as their
original repo in 'Instruction-Tuned' and listed in column rehost_parents.
"""

from __future__ import annotations

import csv
import glob
import json
import os
import re
import sys
import textwrap
from collections import OrderedDict, defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
# The 6 October hand review of the parents' pre-trained bases; moved out of the live methods note on 9 Oct.
REVIEW_DOC = REPO / "docs/mental_health_FT_funnel/archive/2026-10-06/parent-bases-2026-10-06.md"
README_DIR = HERE / "cache/readmes"
CARDS_GLOB = str(HERE / "cache/cards/*.csv")
# publish_manuscript_figures.py sets both before main(). A standalone run writes them into
# outputs/cross-grouping/<CURRENT>/ (set in main, so version_rule.py can import this module first).
OUT_CSV: Path | None = None
OUT_PNG: Path | None = None

# Pre-trained checkpoints must never appear as a parent here: funnel step 3 removes their children.
# (Fixed 6 Oct in rules.py: a card sentence saying the model 'has not been instruction-tuned' is now
# read as pre-trained, e.g. BSC-LT/salamandra-7b, microsoft/phi-2.) Any hit is an error.
PRETRAINED_CHECKPOINTS = {"BSC-LT/salamandra-7b", "microsoft/phi-2"}

csv.field_size_limit(10**9)


def die(msg: str, items=()) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    for it in items:
        print(f"  - {it}", file=sys.stderr)
    sys.exit(1)


# --------------------------------------------------------------------------
# 1. Parent repo id -> (family, version, size, kind)
#    kind is 'instruct' (an instruction-tuned / post-trained checkpoint) or
#    'pretrained' (the parent is itself a pre-trained base; this is an error
#    for this figure and the script stops).
# --------------------------------------------------------------------------

REGEX_RULES = [
    # Qwen vision-language lines are their own versions (own panels).
    (r"^(?:Qwen|unsloth)/Qwen2\.5-VL-(?P<size>\d+(?:\.\d+)?B)-Instruct$", "Qwen", "Qwen2.5-VL", "instruct"),
    (r"^(?:Qwen|unsloth)/Qwen2-VL-(?P<size>\d+(?:\.\d+)?B)-Instruct$", "Qwen", "Qwen2-VL", "instruct"),
    (r"^(?:Qwen|unsloth)/Qwen3-VL-(?P<size>\d+(?:\.\d+)?B)-Instruct$", "Qwen", "Qwen3-VL", "instruct"),
    (r"^(?:Qwen|unsloth)/Qwen2\.5-(?P<size>\d+(?:\.\d+)?B)-Instruct$", "Qwen", "Qwen2.5", "instruct"),
    # Qwen3 ships one post-trained checkpoint per size without an -Instruct
    # suffix (Qwen/Qwen3-8B is instruction-tuned; Qwen/Qwen3-8B-Base is the
    # pre-trained one). The -Instruct-2507 refresh is a second parent in the
    # same Qwen3 cell.
    (r"^(?:Qwen|unsloth)/Qwen3-(?P<size>\d+(?:\.\d+)?B)(?:-Instruct-2507)?$", "Qwen", "Qwen3", "instruct"),
    (r"^(?:Qwen|unsloth)/Qwen3\.5-(?P<size>\d+(?:\.\d+)?B)$", "Qwen", "Qwen3.5", "instruct"),
    (r"^Qwen/Qwen3\.6-(?P<size>\d+B-A\d+B)$", "Qwen", "Qwen3.6", "instruct"),
    # Gemma. 'E2B'/'E4B' are effective sizes; the label is kept as given.
    (r"^(?:google|unsloth)/gemma-(?P<size>\d+)b-it$", "Gemma", "Gemma 1", "instruct"),
    (r"^(?:google|unsloth)/gemma-2-(?P<size>\d+)b(?:-jpn)?-it$", "Gemma", "Gemma 2", "instruct"),
    (r"^(?:google|unsloth)/gemma-3-(?P<size>\d+[bm])-it$", "Gemma", "Gemma 3", "instruct"),
    (r"^(?:google|unsloth)/gemma-3n-(?P<size>E\d+B)-it$", "Gemma", "Gemma 3n", "instruct"),
    (r"^(?:google|unsloth)/gemma-4-(?P<size>E\d+B|\d+B)-it$", "Gemma", "Gemma 4", "instruct"),
    # Llama.
    (r"^(?:meta-llama|NousResearch)/Llama-2-(?P<size>\d+)b-chat-hf$", "Llama", "Llama 2", "instruct"),
    (r"^meta-llama/Meta-Llama-3-(?P<size>\d+B)-Instruct$", "Llama", "Llama 3", "instruct"),
    (r"^meta-llama/Meta-Llama-3-(?P<size>\d+B)$", "Llama", "Llama 3", "pretrained"),
    (r"^meta-llama/Llama-3\.1-(?P<size>\d+B)-Instruct$", "Llama", "Llama 3.1", "instruct"),
    (r"^(?:meta-llama|unsloth)/Llama-3\.2-(?P<size>\d+B)-Instruct$", "Llama", "Llama 3.2", "instruct"),
    # Mistral.
    (r"^mistralai/Mistral-(?P<size>7B)-Instruct-(?P<ver>v0\.\d)$", "Mistral", "Mistral 7B {ver}", "instruct"),
]

# One-off parents that do not follow a vendor naming pattern.
# parent -> (family, version, size, kind)
ONE_OFF_RULES = {
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0": ("TinyLlama", "Chat v1.0", "1.1B", "instruct"),
    "Doctor-Shotgun/TinyLlama-1.1B-32k-Instruct": ("TinyLlama", "32k-Instruct (Doctor-Shotgun)", "1.1B", "instruct"),
    "tiiuae/Falcon3-1B-Instruct": ("Falcon", "Falcon 3", "1B", "instruct"),
    "HuggingFaceTB/SmolLM2-135M-Instruct": ("SmolLM", "SmolLM2", "135M", "instruct"),
    "HuggingFaceTB/SmolLM2-360M-Instruct": ("SmolLM", "SmolLM2", "360M", "instruct"),
    "HuggingFaceTB/SmolLM2-1.7B-Instruct": ("SmolLM", "SmolLM2", "1.7B", "instruct"),
    "HuggingFaceTB/SmolVLM-256M-Instruct": ("SmolLM", "SmolVLM", "256M", "instruct"),
    "LiquidAI/LFM2-700M": ("LFM2", "LFM2", "700M", "instruct"),
    # FLAN-T5 is Google's instruction-tuned release of T5 (Chung et al. 2022); base is 248M parameters.
    # Admitted as a parent on 9 Oct 2026 by the parent registry (parents.csv).
    "google/flan-t5-base": ("FLAN-T5", "FLAN-T5", "248M", "instruct"),
    # Hermes is NousResearch's instruction-tuning series on other vendors'
    # pre-trained bases, so each Hermes model sits in its base's lineage.
    "NousResearch/Hermes-2-Pro-Mistral-7B": ("Mistral", "Mistral 7B v0.1", "7B", "instruct"),
    "NousResearch/Hermes-2-Pro-Llama-3-8B": ("Llama", "Llama 3", "8B", "instruct"),
    "NousResearch/Hermes-3-Llama-3.1-8B": ("Llama", "Llama 3.1", "8B", "instruct"),
    # Continued pre-training of Llama 3 8B by YTU, then instruction-tuned: own column in the Llama 3 panel.
    "ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1": ("Llama", "Llama 3", "8B (Turkish-Llama)", "instruct"),
    # Continued pre-training of Qwen3.5-4B-Base by McGill, then instruction-tuned: own column in a Qwen3.5 panel.
    "McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1": ("Qwen", "Qwen3.5", "4B (AfriqueQwen)", "instruct"),
    "BSC-LT/salamandra-7b-instruct": ("Salamandra", "Salamandra", "7B", "instruct"),
    # The card says "a family of 8B parameter ... models"; safetensors total is 8.31B.
    "EssentialAI/rnj-1-instruct": ("rnj-1", "rnj-1", "8B", "instruct"),
    "StentorLabs/Stentor-30M-Instruct": ("Stentor", "Stentor", "30M", "instruct"),
    # 11B vision instruct is its own column in the Llama 3.2 panel. The plain
    # Llama-3.2 regex is '\d+B-Instruct' and does not match '-Vision-Instruct'.
    "meta-llama/Llama-3.2-11B-Vision-Instruct": ("Llama", "Llama 3.2", "11B (Vision)", "instruct"),
    "unsloth/Llama-3.2-11B-Vision-Instruct": ("Llama", "Llama 3.2", "11B (Vision)", "instruct"),
    "microsoft/phi-2": ("Phi", "Phi 2", "2.7B", "pretrained"),
    "microsoft/Phi-3.5-mini-instruct": ("Phi", "Phi 3.5", "3.8B", "instruct"),
    "unsloth/Ministral-3-8B-Reasoning-2512": ("Ministral", "Ministral 3", "8B", "instruct"),
    "microsoft/bitnet-b1.58-2B-4T-bf16": ("BitNet", "b1.58", "2B", "instruct"),
    # The card does not name a base repo. config.json has no parameter-count
    # field. Size 1.5B is the card sentence "1.5B parameters total".
    "openai/privacy-filter": ("privacy-filter", "privacy-filter", "1.5B", "instruct"),
    # Cohere's Tiny Aya: 3.35B, two regional post-trained variants (earth, global) of one base.
    # Card: "After pretraining, this model uses supervised fine-tuning (SFT) and preference training".
    # Parents of the three adzcai/AfriGuardInst-tiny-aya-* safety models. Added 10 Oct 2026.
    "CohereLabs/tiny-aya-earth": ("Tiny Aya", "Tiny Aya", "3.35B (earth)", "instruct"),
    "CohereLabs/tiny-aya-global": ("Tiny Aya", "Tiny Aya", "3.35B (global)", "instruct"),
    # Card: "compressed from NVIDIA-Nemotron-Nano-9B-v2 using the Nemotron Elastic framework", then
    # post-trained (Nemotron-Post-Training-Dataset-v2 and RL sets listed). 3.97B parameters. Added 10 Oct 2026.
    "nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16": ("Nemotron", "Nemotron 3 Nano", "4B", "instruct"),
    # DeepSeek-R1 distilled onto another vendor's pre-trained base, so each one
    # sits in that base's lineage (same rule as Hermes). The Qwen 1.5B base is
    # Qwen2.5-Math, a continued-pretraining line, so it is its own column.
    "deepseek-ai/DeepSeek-R1-Distill-Llama-8B": ("Llama", "Llama 3.1", "8B", "instruct"),
    "unsloth/DeepSeek-R1-Distill-Llama-8B": ("Llama", "Llama 3.1", "8B", "instruct"),
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B": ("Qwen", "Qwen2.5", "1.5B (Qwen2.5-Math)", "instruct"),
    "unsloth/DeepSeek-R1-Distill-Qwen-1.5B": ("Qwen", "Qwen2.5", "1.5B (Qwen2.5-Math)", "instruct"),
    # OpenAI's post-trained open-weight release. The repo name is 20B; the card says 21B total parameters.
    "openai/gpt-oss-20b": ("gpt-oss", "gpt-oss", "20B", "instruct"),
    "unsloth/gpt-oss-20b-BF16": ("gpt-oss", "gpt-oss", "20B", "instruct"),
    "arcee-ai/AFM-4.5B": ("AFM", "AFM", "4.5B", "instruct"),
    "ibm-granite/granite-4.0-micro": ("Granite", "Granite 4.0", "3B", "instruct"),
    # Pretrained checkpoints named as pretrained_id on the roster. The size string is the one
    # classify_parent already returns for the instruction-tuned model of that
    # checkpoint. These repo ids have no -it or -Instruct suffix, so the
    # instruction patterns do not match them.
    "google/gemma-2b": ("Gemma", "Gemma 1", "2B", "pretrained"),
    "google/gemma-3-270m": ("Gemma", "Gemma 3", "270M", "pretrained"),
    "google/gemma-3-1b-pt": ("Gemma", "Gemma 3", "1B", "pretrained"),
    "google/gemma-3-4b-pt": ("Gemma", "Gemma 3", "4B", "pretrained"),
    "google/gemma-3n-E2B": ("Gemma", "Gemma 3n", "E2B", "pretrained"),
    "meta-llama/Llama-3.1-8B": ("Llama", "Llama 3.1", "8B", "pretrained"),
    "meta-llama/Llama-3.2-1B": ("Llama", "Llama 3.2", "1B", "pretrained"),
    "meta-llama/Llama-3.2-3B": ("Llama", "Llama 3.2", "3B", "pretrained"),
    "Qwen/Qwen2.5-7B": ("Qwen", "Qwen2.5", "7B", "pretrained"),
    "Qwen/Qwen3-1.7B-Base": ("Qwen", "Qwen3", "1.7B", "pretrained"),
    "Qwen/Qwen3-4B-Base": ("Qwen", "Qwen3", "4B", "pretrained"),
    "Qwen/Qwen3-8B-Base": ("Qwen", "Qwen3", "8B", "pretrained"),
    "mistral-community/Mistral-7B-v0.2": ("Mistral", "Mistral 7B v0.2", "7B", "pretrained"),
    "mistralai/Mistral-7B-v0.3": ("Mistral", "Mistral 7B v0.3", "7B", "pretrained"),
    "HuggingFaceTB/SmolLM2-360M": ("SmolLM", "SmolLM2", "360M", "pretrained"),
    "HuggingFaceTB/SmolLM2-135M": ("SmolLM", "SmolLM2", "135M", "pretrained"),
    "Qwen/Qwen2.5-3B": ("Qwen", "Qwen2.5", "3B", "pretrained"),
    "Qwen/Qwen2.5-Math-1.5B": ("Qwen", "Qwen2.5", "1.5B (Qwen2.5-Math)", "pretrained"),
    "Qwen/Qwen3-0.6B-Base": ("Qwen", "Qwen3", "0.6B", "pretrained"),
    "Qwen/Qwen3.5-4B-Base": ("Qwen", "Qwen3.5", "4B", "pretrained"),
    "google/gemma-3n-E4B": ("Gemma", "Gemma 3n", "E4B", "pretrained"),
}

# Third-party copies of a vendor checkpoint -> the vendor repo they copy.
# Counted as the original in 'Instruction-Tuned'; listed in rehost_parents.
REHOST_MAP = {
    "unsloth/Qwen2.5-7B-Instruct": "Qwen/Qwen2.5-7B-Instruct",
    "unsloth/gemma-3-4b-it": "google/gemma-3-4b-it",
    "unsloth/Qwen3-32B": "Qwen/Qwen3-32B",
    "unsloth/Qwen3-4B-Instruct-2507": "Qwen/Qwen3-4B-Instruct-2507",
    "NousResearch/Llama-2-7b-chat-hf": "meta-llama/Llama-2-7b-chat-hf",
    "unsloth/gemma-3-270m-it": "google/gemma-3-270m-it",
    "unsloth/Llama-3.2-3B-Instruct": "meta-llama/Llama-3.2-3B-Instruct",
    "unsloth/Llama-3.2-11B-Vision-Instruct": "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "unsloth/Qwen2.5-VL-7B-Instruct": "Qwen/Qwen2.5-VL-7B-Instruct",
    "unsloth/Qwen3-0.6B": "Qwen/Qwen3-0.6B",
    "unsloth/gemma-3-12b-it": "google/gemma-3-12b-it",
    "unsloth/gemma-4-E4B-it": "google/gemma-4-E4B-it",
    "unsloth/gemma-3-1b-it": "google/gemma-3-1b-it",
    "unsloth/Qwen3.5-27B": "Qwen/Qwen3.5-27B",
    "unsloth/DeepSeek-R1-Distill-Llama-8B": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    "unsloth/DeepSeek-R1-Distill-Qwen-1.5B": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    "unsloth/gpt-oss-20b-BF16": "openai/gpt-oss-20b",
}


def classify_parent(parent: str):
    """Return (family, version, size, kind) or None. Fails loud on ambiguity."""
    hits = []
    if parent in ONE_OFF_RULES:
        hits.append(ONE_OFF_RULES[parent])
    for pat, fam, ver, kind in REGEX_RULES:
        m = re.match(pat, parent)
        if m:
            size = m.group("size")
            size = size.upper() if size[-1] in "bm" else size
            if not size.endswith(("B", "M")):
                size = f"{size}B"
            ver = ver.format(**m.groupdict())
            hits.append((fam, ver, size, kind))
    if len(hits) > 1:
        die(f"parent matched more than one rule: {parent}", [str(h) for h in hits])
    return hits[0] if hits else None


# --------------------------------------------------------------------------
# 2. Row 'Base Model': does the parent's own card name a pre-trained base?
# --------------------------------------------------------------------------

# Hand reading of the cards for parents (or rehost originals) that are NOT in
# the review doc's Parent table. parent -> (named pre-trained base repo or
# None, evidence). The script verifies each named repo against the cached card
# (cardData base_model, Hub-resolved baseModels, or the README text), and
# verifies that a None reading has no non-instruction base_model on the card.
CARD_READING = {
    "google/flan-t5-base": (
        "google/t5-v1_1-base",
        "Card: 'These models are based on pretrained T5 (Raffel et al., 2020) and fine-tuned with instructions'; the card's model-index and text name google/t5-v1_1-base as the pre-trained checkpoint. Read 9 Oct 2026 (parents.csv row).",
    ),
    "BSC-LT/salamandra-7b-instruct": (
        "BSC-LT/salamandra-7b",
        "YAML base_model: BSC-LT/salamandra-7b. Card: Salamandra is 'pre-trained from scratch'; the instruct card is 'the instruction-following capabilities of recently released base models'.",
    ),
    "EssentialAI/rnj-1-instruct": (
        "EssentialAI/rnj-1",
        "YAML base_model: EssentialAI/rnj-1. Card: 'rnj-1 refers to the base model, while rnj-1-instruct refers to the post-trained instruction tuned model.'",
    ),
    "McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1": (
        "McGill-NLP/AfriqueQwen3.5-4B-50Langs",
        "YAML base_model: McGill-NLP/AfriqueQwen3.5-4B-50Langs. That repo's card: 'Type: Causal Language Model (Base/Pre-trained)', tag continued-pretraining.",
    ),
    "NousResearch/Hermes-2-Pro-Llama-3-8B": (
        "NousResearch/Meta-Llama-3-8B",
        "YAML base_model: NousResearch/Meta-Llama-3-8B (Nous copy of Meta's pre-trained Llama 3 8B).",
    ),
    "NousResearch/Hermes-3-Llama-3.1-8B": (
        "meta-llama/Meta-Llama-3.1-8B",
        "YAML base_model: meta-llama/Meta-Llama-3.1-8B. The Hub resolves that id to meta-llama/Llama-3.1-8B (card baseModels field).",
    ),
    "CohereLabs/tiny-aya-earth": (
        "CohereLabs/tiny-aya-base",
        "YAML base_model: CohereLabs/tiny-aya-base. Card: 'After pretraining, this model uses supervised fine-tuning (SFT) and preference training'. Read 10 Oct 2026.",
    ),
    "CohereLabs/tiny-aya-global": (
        "CohereLabs/tiny-aya-base",
        "YAML base_model: CohereLabs/tiny-aya-base. Same card text as tiny-aya-earth. Read 10 Oct 2026.",
    ),
    "nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16": (
        None,
        "YAML base_model: nvidia/NVIDIA-Nemotron-Nano-9B-v2, itself a post-trained model; the card says the 4B was 'compressed from NVIDIA-Nemotron-Nano-9B-v2' and then post-trained. No pre-trained 4B checkpoint is named. Read 10 Oct 2026.",
    ),
    "Qwen/Qwen2-VL-7B-Instruct": ("Qwen/Qwen2-VL-7B", "YAML base_model: Qwen/Qwen2-VL-7B."),
    "Qwen/Qwen2.5-32B-Instruct": ("Qwen/Qwen2.5-32B", "YAML base_model: Qwen/Qwen2.5-32B."),
    "Qwen/Qwen2.5-72B-Instruct": ("Qwen/Qwen2.5-72B", "YAML base_model: Qwen/Qwen2.5-72B."),
    "Qwen/Qwen2.5-VL-3B-Instruct": (None, "No base_model field or tag. The README does not name a pre-trained repo."),
    "Qwen/Qwen2.5-VL-7B-Instruct": (None, "No base_model field or tag. The README does not name a pre-trained repo."),
    "Qwen/Qwen3.5-27B": (
        None,
        "No base_model field. The README says this repository is the post-trained model, and the overview lists training stage as pre-training and post-training without naming a base repo. Read 13 Oct 2026.",
    ),
    "Qwen/Qwen3.5-4B": (
        "Qwen/Qwen3.5-4B-Base",
        "YAML base_model: Qwen/Qwen3.5-4B-Base. The README also says this repository is the post-trained model. Read 13 Oct 2026.",
    ),
    "deepseek-ai/DeepSeek-R1-Distill-Llama-8B": (
        "meta-llama/Llama-3.1-8B",
        "README table Base Model is Llama-3.1-8B, and the license note says it is derived from Llama3.1-8B-Base. Read 13 Oct 2026.",
    ),
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B": (
        "Qwen/Qwen2.5-Math-1.5B",
        "README table Base Model is Qwen2.5-Math-1.5B. Read 13 Oct 2026.",
    ),
    "Qwen/Qwen3-4B-Instruct-2507": (
        None,
        "No base_model field or tag. The README calls this 'the updated version of the Qwen3-4B non-thinking mode' and does not name Qwen3-4B-Base.",
    ),
    "Qwen/Qwen3-VL-2B-Instruct": (None, "No base_model field or tag. The README does not name a pre-trained repo."),
    "Qwen/Qwen3-VL-4B-Instruct": (None, "No base_model field or tag. The README does not name a pre-trained repo."),
    "Qwen/Qwen3-VL-8B-Instruct": (None, "No base_model field or tag. The README does not name a pre-trained repo."),
    "Qwen/Qwen3.6-35B-A3B": (None, "No base_model field or tag. The README does not name a -Base repo."),
    "StentorLabs/Stentor-30M-Instruct": (
        "StentorLabs/Stentor-30M",
        "YAML base_model: StentorLabs/Stentor-30M. README: 'a supervised fine-tune of Stentor-30M ... The base model is a strong next-token predictor but has no instruction following'.",
    ),
    "google/gemma-2-2b-jpn-it": (
        None,
        "YAML base_model: google/gemma-2-2b-it, an instruction model. google/gemma-2-2b is not named.",
    ),
    "google/gemma-2-9b-it": ("google/gemma-2-9b", "YAML base_model: google/gemma-2-9b."),
    "google/gemma-3-12b-it": ("google/gemma-3-12b-pt", "YAML base_model: google/gemma-3-12b-pt."),
    "google/gemma-3n-E2B-it": (
        None,
        "YAML base_model: google/gemma-3n-E4B-it, an instruction model. The card says this E2B checkpoint is a nested sub-model of that E4B instruct repo. It does not name a pre-trained repo.",
    ),
    # Original of the rehost unsloth/gemma-3-270m-it (not itself a parent).
    "google/gemma-3-270m-it": ("google/gemma-3-270m", "YAML base_model: google/gemma-3-270m. That repo's card is the Gemma 3 card for the pre-trained 270M checkpoint."),
    "google/gemma-4-E2B-it": ("google/gemma-4-E2B", "YAML base_model: google/gemma-4-E2B."),
    "meta-llama/Llama-3.2-1B-Instruct": (
        None,
        "No base_model field or tag. 'Base Pretrained Models' is a benchmark table heading; meta-llama/Llama-3.2-1B is not named.",
    ),
    "unsloth/Qwen2.5-7B-Instruct": (None, "YAML base_model: Qwen/Qwen2.5-7B-Instruct, the instruction model."),
    "unsloth/Qwen3-4B-Instruct-2507": (None, "YAML base_model: Qwen/Qwen3-4B-Instruct-2507, the instruction model."),
    "HuggingFaceTB/SmolLM2-135M-Instruct": (
        "HuggingFaceTB/SmolLM2-135M",
        "YAML base_model: HuggingFaceTB/SmolLM2-135M.",
    ),
    "HuggingFaceTB/SmolLM2-1.7B-Instruct": (
        "HuggingFaceTB/SmolLM2-1.7B",
        "YAML base_model: HuggingFaceTB/SmolLM2-1.7B.",
    ),
    "HuggingFaceTB/SmolVLM-256M-Instruct": (
        None,
        "YAML base_model lists HuggingFaceTB/SmolLM2-135M-Instruct (an instruction model) and google/siglip-base-patch16-512 (the image encoder). Neither is a pre-trained language-model repo.",
    ),
    "meta-llama/Llama-2-13b-chat-hf": (
        None,
        "No base_model field or tag. The family index links to meta-llama/Llama-2-13b-hf; that id is not the card's base_model.",
    ),
    "meta-llama/Llama-3.2-11B-Vision-Instruct": (
        None,
        "No base_model field or tag. The cached README is a 403 fetch error, so the README text was not readable.",
    ),
    "microsoft/phi-2": (
        None,
        "No base_model field or tag. The card describes Phi-2 itself (2.7 billion parameters) and does not name a pre-trained repo.",
    ),
    "microsoft/bitnet-b1.58-2B-4T-bf16": (
        None,
        "No base_model field or tag. The card says the model was trained from scratch and does not name a pre-trained repo.",
    ),
    "openai/privacy-filter": (
        None,
        "No base_model field or tag. The card says the base is an autoregressive pretrained checkpoint and does not name a repo. config.json has no parameter-count field; the card says 1.5B parameters total.",
    ),
    "unsloth/gemma-3n-E4B-it": (
        None,
        "YAML base_model: google/gemma-3n-E4B-it, the instruction model. That repo is not in the cache. No pre-trained repo is named.",
    ),
    "unsloth/Ministral-3-8B-Reasoning-2512": (
        None,
        "YAML base_model: mistralai/Ministral-3-8B-Reasoning-2512, the vendor reasoning checkpoint this rehost copies. That repo is not in the cache. No pre-trained repo is named.",
    ),
}

# Pre-trained base repos that are not in cache/cards. Checked by the lead on
# 2026-10-06 with huggingface_hub.HfApi().model_info(repo, files_metadata=True)
# (no download): repo -> (gated, safetensors dtypes at the root, number of
# root weight files). All nine exist with full-precision root weights.
HUB_CHECK_2026_10_06 = {
    # added 9 Oct (model_info plus the pytorch_model.bin pickle header via hub.bin_storage_types): the
    # pre-trained base of google/flan-t5-base, admitted as a parent by parents.csv on 9 Oct. Root weights
    # are a single pytorch_model.bin with FloatStorage (F32); no safetensors summary on the Hub.
    "google/t5-v1_1-base": ("public", {"F32"}, 1),
    # added 6 Oct evening (model_info, metadata only): bases of parents whose own card does not name a base repo
    "meta-llama/Llama-3.2-1B": ("gated", {"BF16"}, 1),
    "meta-llama/Llama-3.2-3B": ("gated", {"BF16"}, 2),
    "meta-llama/Llama-2-13b-hf": ("gated", {"F16", "F32"}, 6),
    "google/gemma-3n-E4B": ("gated", {"BF16"}, 4),
    "HuggingFaceTB/SmolVLM-256M-Base": ("public", {"BF16"}, 1),
    "mistralai/Ministral-3-8B-Base-2512": ("public", {"BF16"}, 4),
    "BSC-LT/salamandra-7b": ("public", {"BF16"}, 4),
    "EssentialAI/rnj-1": ("public", {"F32"}, 7),
    "NousResearch/Meta-Llama-3-8B": ("public", {"BF16"}, 4),
    "Qwen/Qwen2-VL-7B": ("public", {"BF16"}, 5),
    "Qwen/Qwen2.5-32B": ("public", {"BF16"}, 17),
    "Qwen/Qwen2.5-72B": ("public", {"BF16"}, 37),
    "StentorLabs/Stentor-30M": ("public", {"F32"}, 1),
    "google/gemma-2-9b": ("gated", {"F32"}, 8),
    "google/gemma-3-12b-pt": ("gated", {"BF16"}, 5),
}

INSTRUCTION_SUFFIX = re.compile(r"(-it|-Instruct(-\d+)?|-chat-hf)$")
# base_model ids that are not a pre-trained language-model repo. A None reading
# is allowed when every other base_model matches INSTRUCTION_SUFFIX or is here.
NON_PRETRAINED_BASE_MODEL = {
    "google/siglip-base-patch16-512",
    "mistralai/Ministral-3-8B-Reasoning-2512",
    # Post-trained 9B that Nemotron-3-Nano-4B was pruned from; not a pre-trained checkpoint of the 4B.
    "nvidia/NVIDIA-Nemotron-Nano-9B-v2",
}
ROOT_WEIGHT = re.compile(r"^(model(-\d+-of-\d+)?\.safetensors|pytorch_model(-\d+-of-\d+)?\.bin)$")
FP_DTYPES = {"F16", "BF16", "F32"}



def parse_parent_table(doc: Path):
    """Parse the 'Parent table' from the review doc. Returns parent -> dict."""
    lines = doc.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "### Parent table")
    except StopIteration:
        die(f"'### Parent table' heading not found in {doc}")
    header = None
    table = OrderedDict()
    for line in lines[start + 1 :]:
        if line.startswith("## ") or (header is not None and not line.startswith("|")):
            if header is not None:
                break
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            if header != ["Parent", "Kept children", "Names pre-trained base", "Base repo", "Evidence", "Readable", "Root FP weights"]:
                die("Parent table header is not the expected 7 columns", header)
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        if len(cells) != 7:
            die("Parent table row does not have 7 cells", [line])
        row = dict(zip(header, cells))
        parent = row["Parent"].strip("`")
        base = row["Base repo"].strip("`")
        table[parent] = {
            "names": row["Names pre-trained base"].lower(),
            "base": base,
            "readable": row["Readable"].lower(),
            "root_fp": "yes" if row["Root FP weights"].lower().startswith("yes") else ("no" if row["Root FP weights"].lower().startswith("no") else ""),
            "evidence": row["Evidence"],
        }
    if not table:
        die("Parent table parsed to zero rows")
    return table


def load_cards():
    """Return hf_id -> newest card row across cache/cards/*.csv."""
    cards = {}
    for f in sorted(glob.glob(CARDS_GLOB)):
        for r in csv.DictReader(open(f, newline="", encoding="utf-8")):
            cards[r["hf_id"]] = r  # files sorted by date; later wins
    if not cards:
        die(f"no card rows found under {CARDS_GLOB}")
    return cards


def newest_readme(parent: str):
    owner, name = parent.split("/", 1)
    files = sorted(README_DIR.glob(f"{owner}__{name}__*.md"))
    return files[-1] if files else None


def card_base_models(card):
    """Named base_model ids (cardData) and Hub-resolved ids (baseModels)."""
    named, resolved = [], []
    try:
        cd = json.loads(card.get("cardData") or "{}")
    except json.JSONDecodeError:
        cd = {}
    bm = cd.get("base_model")
    if isinstance(bm, str):
        named = [bm]
    elif isinstance(bm, list):
        named = [x for x in bm if isinstance(x, str)]
    try:
        b = json.loads(card.get("baseModels") or "{}")
        resolved = [m["id"] for m in b.get("models", []) if "id" in m]
    except json.JSONDecodeError:
        pass
    return named, resolved


def check_base_in_cache(base: str, resolved_ids, cards):
    """Return (status, repo_used, detail). status in yes | named_not_checked | named_404 | named_no_fp."""
    candidates = [base] + [r for r in resolved_ids if r != base]
    for cand in candidates:
        card = cards.get(cand)
        if card is None:
            continue
        if card.get("http_status") not in ("200", "") or card.get("fetch_err"):
            return "named_404", cand, f"http_status={card.get('http_status')} fetch_err={card.get('fetch_err')}"
        try:
            st = json.loads(card.get("safetensors") or "{}")
            dtypes = set((st.get("parameters") or {}).keys())
        except json.JSONDecodeError:
            dtypes = set()
        try:
            sib = json.loads(card.get("siblings") or "[]")
            root = [s["rfilename"] for s in sib if ROOT_WEIGHT.match(s.get("rfilename", ""))]
        except json.JSONDecodeError:
            root = []
        readable = "gated" if card.get("gated", "no") != "no" else "yes"
        if dtypes and dtypes <= FP_DTYPES and root:
            return "yes", cand, f"cache card: readable={readable}, dtypes={'|'.join(sorted(dtypes))}, root={root[0]}"
        return "named_no_fp", cand, f"cache card: readable={readable}, dtypes={'|'.join(sorted(dtypes)) or 'none'}, root={root[:1] or 'none'}"
    for cand in candidates:
        if cand in HUB_CHECK_2026_10_06:
            gated, dtypes, n_files = HUB_CHECK_2026_10_06[cand]
            if dtypes <= FP_DTYPES and n_files > 0:
                return "yes", cand, f"Hub model_info check 2026-10-06: {gated}, dtypes={'|'.join(sorted(dtypes))}, {n_files} root weight file(s)"
            return "named_no_fp", cand, f"Hub model_info check 2026-10-06: {gated}, dtypes={'|'.join(sorted(dtypes))}, {n_files} root weight file(s)"
    return "named_not_checked", base, "base repo not in cache/cards and not in HUB_CHECK_2026_10_06"


def base_status_for_parent(parent: str, table, cards):
    """Return dict(status, base_repo, source, detail) or None when no reading exists.
    A card that names no base is upgraded to yes_sibling when SIBLING_BASE_2026_10_06 records a
    vendor sibling base confirmed by the 6 Oct Hub check."""
    out = _base_status_from_card(parent, table, cards)
    if out is None or out["status"] != "not_named":
        return out
    sib = SIBLING_BASE_2026_10_06.get(parent)
    if sib is None or sib.startswith("404:"):
        return out
    if sib not in HUB_CHECK_2026_10_06:
        die(f"SIBLING_BASE_2026_10_06 names {sib} for {parent} but it is not in HUB_CHECK_2026_10_06")
    gated, dtypes, n = HUB_CHECK_2026_10_06[sib]
    if not (dtypes <= FP_DTYPES and n > 0):
        die(f"sibling base {sib} for {parent} has no full-precision root weights: {gated}, {sorted(dtypes)}, {n} files")
    return {"status": "yes_sibling", "base_repo": sib, "source": "vendor sibling repo (Hub check 2026-10-06)",
            "detail": f"card names no base; {sib} exists ({gated}, {'|'.join(sorted(dtypes))}, {n} root files)"}


def _base_status_from_card(parent: str, table, cards):
    """Return dict(status, base_repo, source, detail) or None when no reading exists."""
    if parent in table:
        t = table[parent]
        if t["names"] != "yes":
            status = "not_named"
        elif t["readable"] in ("yes", "gated") and t["root_fp"] == "yes":
            status = "yes"
        elif t["readable"] == "no":
            status = "named_404"
        else:
            status = "named_not_checked"
        return {"status": status, "base_repo": t["base"], "source": "review-doc Parent table", "detail": f"names={t['names']} readable={t['readable'] or '-'} root_fp={t['root_fp'] or '-'}"}
    if parent not in CARD_READING:
        return None
    base, evidence = CARD_READING[parent]
    card = cards.get(parent)
    readme = newest_readme(parent)
    if card is None and readme is None:
        die(f"parent {parent} has neither a card row nor a README in the cache; cannot verify CARD_READING")
    named, resolved = card_base_models(card) if card else ([], [])
    text = readme.read_text(encoding="utf-8", errors="replace") if readme else ""
    if base is None:
        bad = [b for b in named if not INSTRUCTION_SUFFIX.search(b) and b not in NON_PRETRAINED_BASE_MODEL]
        if bad:
            die(f"CARD_READING says {parent} names no pre-trained base, but its card base_model is", bad)
        return {"status": "not_named", "base_repo": "", "source": "cache card (hand reading)", "detail": evidence}
    if base not in named and base not in resolved and base not in text:
        die(f"CARD_READING names {base} for {parent}, but that id is not in the cached card or README")
    status, repo_used, detail = check_base_in_cache(base, resolved, cards)
    return {"status": status, "base_repo": repo_used, "source": "cache card (hand reading)", "detail": f"{evidence} {detail}"}


# --------------------------------------------------------------------------
# 3. Build the table
# --------------------------------------------------------------------------

# Parents whose own card names no pre-trained base (status not_named) but whose vendor publishes a
# sibling base repo. Checked by a Hub model_info call on 6 Oct (entries in HUB_CHECK_2026_10_06).
# Mark Kalinich, 6 Oct: when the vendor's naming makes the pairing unambiguous, the sibling counts
# as the base ('Pre-trained' cell = 1, status yes_sibling). Column sibling_base_hub_check records it.
# 404 = the vendor released no base repo under that name (Qwen2.5-VL-3B/-7B, Qwen3-32B-Base).
SIBLING_BASE_2026_10_06 = {
    "meta-llama/Llama-3.2-1B-Instruct": "meta-llama/Llama-3.2-1B",
    "meta-llama/Llama-3.2-3B-Instruct": "meta-llama/Llama-3.2-3B",
    "meta-llama/Llama-2-13b-chat-hf": "meta-llama/Llama-2-13b-hf",
    "unsloth/gemma-3n-E4B-it": "google/gemma-3n-E4B",
    "HuggingFaceTB/SmolVLM-256M-Instruct": "HuggingFaceTB/SmolVLM-256M-Base",
    "unsloth/Ministral-3-8B-Reasoning-2512": "mistralai/Ministral-3-8B-Base-2512",
    "Qwen/Qwen2.5-VL-3B-Instruct": "404:Qwen/Qwen2.5-VL-3B",
    "Qwen/Qwen2.5-VL-7B-Instruct": "404:Qwen/Qwen2.5-VL-7B",
    "Qwen/Qwen3-32B": "404:Qwen/Qwen3-32B-Base",
    "LiquidAI/LFM2-700M": "404:LiquidAI/LFM2-700M-Base",
    "Qwen/Qwen3-VL-2B-Instruct": "404:Qwen/Qwen3-VL-2B-Base",
    "Qwen/Qwen3.6-35B-A3B": "404:Qwen/Qwen3.6-35B-A3B-Base",
}


def sibling_base_note(inst: dict) -> str:
    out = []
    for p, i in inst.items():
        if i["status"] not in ("not_named", "yes_sibling") or p not in SIBLING_BASE_2026_10_06:
            continue
        sib = SIBLING_BASE_2026_10_06[p]
        if sib.startswith("404:"):
            out.append(f"{p}: {sib[4:]} 404 on Hub 2026-10-06")
            continue
        if sib not in HUB_CHECK_2026_10_06:
            die(f"SIBLING_BASE_2026_10_06 names {sib} for {p} but it is not in HUB_CHECK_2026_10_06")
        gated, dtypes, n = HUB_CHECK_2026_10_06[sib]
        out.append(f"{p}: {sib} exists ({gated}, {'|'.join(sorted(dtypes))}, {n} root files) but the card does not name it")
    return ";".join(out)


STATUS_RANK = {"yes": 0, "yes_sibling": 0, "named_not_checked": 1, "named_no_fp": 2, "named_404": 3, "not_named": 4}


def size_key(size: str):
    """Order size labels numerically; a '(qualifier)' sorts after the plain size."""
    s = size.upper()
    qualifier = " (" in s
    s = s.split(" (")[0]
    eff = s.startswith("E")
    s = s.lstrip("E")
    m = re.match(r"^(\d+(?:\.\d+)?)([BM])(?:-A\d+B)?$", s)
    if not m:
        die(f"cannot order size label {size!r}")
    v = float(m.group(1)) * (1e9 if m.group(2) == "B" else 1e6)
    return (v, 1 if eff else 0, 1 if qualifier else 0, size)


def version_key(version: str):
    m = re.search(r"(\d+(?:\.\d+)?)", version)
    return (float(m.group(1)) if m else 0.0, version)


CSV_COLUMNS = ["family", "version", "size", "pretrained_base_status", "pretrained_base_repo", "instruction_parents",
               "n_instruction_parents", "n_mental_health_kept", "n_safety_kept", "n_medical_kept",
               "mental_health_ids", "safety_ids", "medical_ids",
               "rehost_parents", "pretrained_base_status_by_parent", "pretrained_base_source", "sibling_base_hub_check"]


def kept_for_figure(rows, cohort: str):
    """Fail if any kept row's parent is a known pre-trained checkpoint (funnel step 3 should have removed it)."""
    bad = [f'{r["hf_id"]} (parent {r["parent"]})' for r in rows if r["parent"] in PRETRAINED_CHECKPOINTS]
    if bad:
        die(f"{cohort} kept list has children of pre-trained checkpoints; fix the funnel, not the figure", bad)
    if cohort == "medical":
        print(
            "FLAG: openai/privacy-filter names no base repo. cache/configs/openai__privacy-filter__2026-10-06.json "
            "has no parameter-count field. The size label 1.5B is the model card sentence '1.5B parameters total'.",
            file=sys.stderr,
        )
    return rows, []


def load_study_fine_tunes():
    """Fine-tune rows from the study roster, in the shape build_table expects."""
    pointer = REPO / "outputs" / "roster" / "CURRENT"
    if not pointer.is_file():
        die(f"missing {pointer}; run roster.py first")
    date = pointer.read_text(encoding="utf-8").strip()
    path = pointer.parent / date / "roster.csv"
    if not path.is_file():
        die(f"missing {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    by = {"mental-health": [], "safety": [], "medical": []}
    bad = []
    for row in rows:
        if row["role"] != "fine-tune":
            continue
        if os.environ.get("MANUSCRIPT_LABELED") == "1":
            from orchestration.study_roster import labeled_fine_tune

            if not labeled_fine_tune(row):
                continue
        grouping = row["grouping"]
        if grouping not in by:
            bad.append(f"grouping {grouping!r} on {row['hf_id']}")
            continue
        parent = row["parent_id"]
        got = classify_parent(parent)
        if got is None:
            bad.append(f"{grouping} {row['hf_id']} parent {parent}: classify_parent returned nothing")
            continue
        family, version, size, kind = got
        if kind == "pretrained":
            bad.append(f"{grouping} {row['hf_id']} parent {parent}: classify_parent marks this parent as pre-trained")
        written = (row["family"], row["version"], row["size"])
        if written != (family, version, size):
            bad.append(
                f"{row['hf_id']}: roster says {row['family']} | {row['version']} | {row['size']}, "
                f"classify_parent says {family} | {version} | {size}"
            )
        by[grouping].append(
            {
                "grouping": grouping,
                "hf_id": row["hf_id"],
                "parent": parent,
                "family": row["family"],
                "version": row["version"],
                "size": row["size"],
            }
        )
    if bad:
        die(f"{path} disagrees with classify_parent", bad)
    return by["mental-health"], by["safety"], by["medical"]


def build_table():
    mh, sf, med_all = load_study_fine_tunes()
    mh, _ = kept_for_figure(mh, "mental-health")
    sf, _ = kept_for_figure(sf, "safety")
    med, _excluded = kept_for_figure(med_all, "medical")
    table = parse_parent_table(REVIEW_DOC)
    cards = load_cards()

    parents = sorted({r["parent"] for r in mh} | {r["parent"] for r in sf} | {r["parent"] for r in med})
    unclassified = [p for p in parents if classify_parent(p) is None]
    if unclassified:
        die("parent repo ids that no rule classifies (add a rule in REGEX_RULES or ONE_OFF_RULES)", unclassified)
    pretrained = [p for p in parents if classify_parent(p)[3] == "pretrained"]
    if pretrained:
        die("parents that are pre-trained checkpoints, not instruction-tuned models (fix the kept.csv rule)", pretrained)
    for rehost, orig in REHOST_MAP.items():
        if classify_parent(orig) is None or classify_parent(orig)[:3] != classify_parent(rehost)[:3]:
            die(f"REHOST_MAP: {rehost} and its original {orig} do not land in the same (family, version, size) cell")
    canonical = sorted({REHOST_MAP.get(p, p) for p in parents})
    unread = [p for p in canonical if base_status_for_parent(p, table, cards) is None]
    if unread:
        die("parents with no pre-trained-base reading (not in the review doc Parent table and not in CARD_READING)", unread)

    cells = defaultdict(lambda: {"instruct": OrderedDict(), "rehosts": [], "mh": [], "sf": [], "med": []})
    parent_info = {}
    for p in parents:
        fam, ver, size, _ = classify_parent(p)
        orig = REHOST_MAP.get(p, p)
        info = base_status_for_parent(orig, table, cards)
        parent_info[p] = {"family": fam, "version": ver, "size": size, "canonical": orig, **info}
        cells[(fam, ver, size)]["instruct"][orig] = info
        if p != orig:
            cells[(fam, ver, size)]["rehosts"].append(p)
    for r in mh:
        fam, ver, size, _ = classify_parent(r["parent"])
        cells[(fam, ver, size)]["mh"].append(r["hf_id"])
    for r in sf:
        fam, ver, size, _ = classify_parent(r["parent"])
        cells[(fam, ver, size)]["sf"].append(r["hf_id"])
    for r in med:
        fam, ver, size, _ = classify_parent(r["parent"])
        cells[(fam, ver, size)]["med"].append(r["hf_id"])

    rows = []
    for (fam, ver, size), c in cells.items():
        inst = c["instruct"]
        best = min(inst.items(), key=lambda kv: STATUS_RANK[kv[1]["status"]])
        status = best[1]["status"]
        base_repo = best[1]["base_repo"] if status != "not_named" else ""
        rows.append({
            "family": fam,
            "version": ver,
            "size": size,
            "pretrained_base_status": status,
            "pretrained_base_repo": base_repo,
            "instruction_parents": ";".join(inst.keys()),
            "n_instruction_parents": len(inst),
            "n_mental_health_kept": len(c["mh"]),
            "n_safety_kept": len(c["sf"]),
            "n_medical_kept": len(c["med"]),
            "mental_health_ids": ";".join(sorted(c["mh"])),
            "safety_ids": ";".join(sorted(c["sf"])),
            "medical_ids": ";".join(sorted(c["med"])),
            "rehost_parents": ";".join(sorted(c["rehosts"])),
            "pretrained_base_status_by_parent": ";".join(f"{p}={i['status']}" + (f"({i['base_repo']})" if i["base_repo"] and i["status"] != "not_named" else "") for p, i in inst.items()),
            "pretrained_base_source": ";".join(sorted({i["source"] for i in inst.values()})),
            "sibling_base_hub_check": sibling_base_note(inst),
        })

    total_mh = sum(r["n_mental_health_kept"] for r in rows)
    total_sf = sum(r["n_safety_kept"] for r in rows)
    total_med = sum(r["n_medical_kept"] for r in rows)
    if total_mh != len(mh) or total_sf != len(sf) or total_med != len(med):
        die(
            f"cell totals dropped roster rows: mental-health {total_mh} of {len(mh)}, "
            f"safety {total_sf} of {len(sf)}, medical {total_med} of {len(med)}"
        )

    fam_order = {f: i for i, f in enumerate(["Gemma", "Llama", "Qwen", "Mistral", "TinyLlama"])}
    rows.sort(key=lambda r: (fam_order.get(r["family"], 99), r["family"], version_key(r["version"]), size_key(r["size"])))

    if OUT_CSV is None or OUT_PNG is None:
        die("OUT_CSV and OUT_PNG must be set before build_table (main() sets them for a standalone run)")
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_COLUMNS)
        w.writeheader()
        w.writerows(rows)
    return rows, parent_info


# --------------------------------------------------------------------------
# 4. Draw the figure from family_table.csv (layout of Figure 1)
# --------------------------------------------------------------------------

# Same colours as analysis/model_coverage_heatmap.py; the row order differs (pre-trained is last here)
# and the row labels are the shorter forms requested for this figure.
FINETUNE_ORDER = ["Instruction-Tuned", "Mental Health FT", "Medical FT", "Safety FT", "Pre-trained"]


def _drawn_rows() -> list[str]:
    """Rows on Figure 1. Pre-trained returns when DRAW_PRETRAINED is true."""
    repo = Path(__file__).resolve().parents[1]
    if str(repo) not in sys.path:
        sys.path.insert(0, str(repo))
    from orchestration.study_roster import DRAW_PRETRAINED

    if DRAW_PRETRAINED:
        return list(FINETUNE_ORDER)
    return [name for name in FINETUNE_ORDER if name != "Pre-trained"]
FINETUNE_COLORS = {
    "Pre-trained": "#52B788",        # Sea Green (PT; 'Base Model' in Figure 1)
    "Instruction-Tuned": "#2E86AB",  # Blue (IT)
    "Mental Health FT": "#C73E1D",   # Red (Mental Health)
    "Medical FT": "#F18F01",         # Orange (MedGemma / Medical)
    "Safety FT": "#7B2D8E",          # Dark Purple (ShieldGemma / Guard)
}
EMPTY = "#f0f0f0"
NOT_CHECKED_FACE = "#cfe9dc"

# Reading order for panels. Every version is its own panel; this list only
# decides which panel is drawn next. A family that is not listed is an error.
PANEL_FAMILY_ORDER = ["Gemma", "Llama", "Qwen", "Mistral", "Falcon", "LFM2", "SmolLM", "TinyLlama", "FLAN-T5"]
# Titles that are not just "family + version". Mistral drops "7B" because the
# column already says 7B. TinyLlama 32k drops the author; the footer names
# Doctor-Shotgun, and family_table.csv keeps the version text
# "32k-Instruct (Doctor-Shotgun)".
PANEL_TITLE = {
    ("Mistral", "Mistral 7B v0.1"): "Mistral v0.1",
    ("Mistral", "Mistral 7B v0.2"): "Mistral v0.2",
    ("Mistral", "Mistral 7B v0.3"): "Mistral v0.3",
    ("TinyLlama", "Chat v1.0"): "TinyLlama Chat v1.0",
    ("TinyLlama", "32k-Instruct (Doctor-Shotgun)"): "TinyLlama 32k",
}
# The 6 Oct figure, before versions without a mental-health fine-tune were
# dropped, was widest on the Qwen row: 20 size columns across 7 version panels.
# A new row stops before the next panel would make it wider than that.
PRIOR_ROW_COLUMNS = 20
PRIOR_ROW_PANELS = 7

CELL = 0.46       # inches per heatmap cell
PANEL_GAP = 0.42  # inches used only when deciding which panels share a row
# Drawn gaps. Versions of one family use the small gap, unless a wrapped title
# still sticks out past its columns: then the gap grows just enough that the
# two titles do not touch. A different family always gets the large gap.
SAME_FAMILY_GAP = 0.12
FAMILY_BREAK_GAP = 0.95
TITLE_AIR = 0.08  # inches of clear space between two titles
ROW_GAP = 1.55    # inches between panel rows (x tick labels, then a two-line title)
LEFT = 1.55       # inches for row labels
TOP = 1.05        # inches for the suptitle and a two-line panel title
BOTTOM = 1.45      # inches for the rotated size labels under the last row
MAX_ROW_WIDTH = PRIOR_ROW_COLUMNS * CELL + PANEL_GAP * (PRIOR_ROW_PANELS - 1)


def panel_title(family: str, version: str) -> str:
    """Family plus version. A version that already begins with the family name is used as written."""
    if (family, version) in PANEL_TITLE:
        return PANEL_TITLE[(family, version)]
    if version == family or version.startswith(family):
        return version
    return f"{family} {version}"


def row_pack_title(family: str, version: str, display: str) -> str:
    """Title whose width decides the row break, not the words drawn on the panel.

    Mistral is measured as "Mistral 7B v0.1". The drawn title drops "7B", and
    that shorter string would otherwise leave room for Falcon 3 on the same row.
    """
    if family == "Mistral":
        return version
    return display


def text_width_inches(text: str, fontsize: float, weight: str = "bold") -> float:
    """Width of one line of text in inches, in the font the figure uses."""
    probe = text_width_inches.probe
    if probe is None:
        probe = plt.figure()
        probe.canvas.draw()
        text_width_inches.probe = probe
    renderer = probe.canvas.get_renderer()
    artist = probe.text(0, 0, text, fontsize=fontsize, fontweight=weight)
    probe.canvas.draw()
    width = artist.get_window_extent(renderer).width / probe.dpi
    artist.remove()
    return width


text_width_inches.probe = None


def panel_slot(title: str, n_cols: int) -> tuple[float, float]:
    """Return (cell-block width, pack width) in inches.

    Pack width is the cell block or the single-line title, whichever is wider.
    It is only used to decide which panels share a row. The drawn panel stays
    the cell-block width; a title that does not fit wraps onto two lines.
    """
    body = n_cols * CELL
    title_w = text_width_inches(title, 11, "bold") + 0.06
    return body, max(body, title_w)


def wrap_title(title: str, max_width: float) -> str:
    """One line if it fits in the columns. Otherwise two lines, split on a space.

    The split is the one whose longer line is as short as possible. A title
    with no space is left on one line.
    """
    if text_width_inches(title, 11, "bold") <= max_width:
        return title
    words = title.split()
    if len(words) < 2:
        return title
    best = None
    for i in range(1, len(words)):
        top = " ".join(words[:i])
        bottom = " ".join(words[i:])
        worst = max(text_width_inches(top, 11, "bold"), text_width_inches(bottom, 11, "bold"))
        fits = worst <= max_width
        key = (0 if fits else 1, worst, i)
        if best is None or key < best[0]:
            best = (key, f"{top}\n{bottom}")
    return best[1]


def widest_title_line(shown: str) -> float:
    return max(text_width_inches(line, 11, "bold") for line in shown.split("\n"))


def drawn_gap(left_shown: str, left_body: float, right_shown: str, right_body: float, same_family: bool) -> float:
    """Small gap inside a family, large gap between families.

    Inside a family the gap is at least SAME_FAMILY_GAP. If a wrapped title
    is still wider than its columns, the gap grows so the titles do not meet.
    """
    if not same_family:
        return FAMILY_BREAK_GAP
    left_over = max(0.0, widest_title_line(left_shown) - left_body) / 2
    right_over = max(0.0, widest_title_line(right_shown) - right_body) / 2
    return max(SAME_FAMILY_GAP, left_over + right_over + TITLE_AIR)


def build_panels(rows):
    """One panel per version, packed into rows that stay within MAX_ROW_WIDTH.

    Return [(letter, [(title, [(size, row)], body_in, slot_in)])].
    A continued pre-training is its own size column inside the parent's panel
    (the size label keeps the qualifier, for example "8B (Turkish-Llama)").
    Turkish-Llama is not in final_models.csv. AfriqueQwen stays: it is its own
    size column inside Qwen3.5, and two safety fine-tunes still name that parent.
    """
    missing = sorted({r["family"] for r in rows} - set(PANEL_FAMILY_ORDER))
    if missing:
        die("families missing from PANEL_FAMILY_ORDER", missing)
    by_version = defaultdict(list)
    for r in rows:
        by_version[(r["family"], r["version"])].append(r)
    panels = []
    for (family, version), group in by_version.items():
        group = sorted(group, key=lambda r: size_key(r["size"]))
        title = panel_title(family, version)
        cols = [(r["size"], r) for r in group]
        body, slot = panel_slot(row_pack_title(family, version, title), len(cols))
        panels.append((title, cols, body, slot))
    titles = [p[0] for p in panels]
    dup_titles = sorted({t for t in titles if titles.count(t) > 1})
    if dup_titles:
        die("two panels would share a title", dup_titles)
    panels.sort(key=lambda p: (PANEL_FAMILY_ORDER.index(p[1][0][1]["family"]), version_key(p[1][0][1]["version"])))

    def row_width(group) -> float:
        if not group:
            return 0.0
        return sum(p[3] for p in group) + PANEL_GAP * (len(group) - 1)

    def family_of(panel) -> str:
        return panel[1][0][1]["family"]

    # Top row: Gemma, then every Qwen version on its right.
    # Next row, from the left: Llama, Mistral, SmolLM.
    def take(names: tuple[str, ...]) -> list:
        chosen = []
        for name in names:
            chosen.extend(p for p in panels if family_of(p) == name)
        return chosen

    top = take(("Gemma", "Qwen"))
    second = take(("Llama", "Mistral", "SmolLM"))
    placed = {id(p) for p in top + second}
    other = [p for p in panels if id(p) not in placed]
    for panel in panels:
        if panel[3] > MAX_ROW_WIDTH:
            die(
                f"panel {panel[0]!r} is {panel[3]:.2f} in wide; the row limit is {MAX_ROW_WIDTH:.2f} in",
            )
    packed = []
    if top:
        packed.append(top)
    if second:
        packed.append(second)
    current = []
    i = 0
    while i < len(other):
        fam = family_of(other[i])
        block = []
        while i < len(other) and family_of(other[i]) == fam:
            block.append(other[i])
            i += 1
        if current and row_width(current + block) > MAX_ROW_WIDTH + 1e-6:
            packed.append(current)
            current = list(block)
        else:
            current.extend(block)
    if current:
        packed.append(current)
    if len(packed) > 26:
        die("more than 26 panel rows")
    return [(chr(ord("a") + i), group) for i, group in enumerate(packed)]


def cell_spec(row_name: str, r):
    """Return (facecolor, text, hatch, textcolor) for one cell."""
    color = FINETUNE_COLORS[row_name]
    if row_name == "Pre-trained":
        st = r["pretrained_base_status"]
        if st in ("yes", "yes_sibling"):
            return color, "1", None, "white"
        if st == "named_not_checked":
            # The card names a base this run has not confirmed. The figure
            # shows a base only when the weights are available.
            return EMPTY, "", None, "#888888"
        # named_404 (card names a base that is not on the Hub) is drawn grey like not_named: in both
        # cases no base is available to anyone, us included (Mark Kalinich, 6 Oct). family_table.csv keeps the distinction.
        if st == "named_no_fp":
            return EMPTY, "no FP", None, "#888888"
        return EMPTY, "", None, "#888888"
    n = int({"Instruction-Tuned": r["n_instruction_parents"],
             "Mental Health FT": r["n_mental_health_kept"],
             "Medical FT": r["n_medical_kept"],
             "Safety FT": r["n_safety_kept"]}[row_name])
    if n == 0:
        return EMPTY, "", None, "#888888"
    return color, str(n), None, "white"


def _size_ticks(cols) -> list[str]:
    """Parameter labels on Figure 1. The Qwen2.5-Math column is labeled 1.5B.

    The size field stays '1.5B (Qwen2.5-Math)' so that column does not merge
    with a plain Qwen2.5 1.5B. Two columns must not share one displayed label.
    """
    labels = ["1.5B" if size == "1.5B (Qwen2.5-Math)" else size for size, _row in cols]
    if len(labels) != len(set(labels)):
        raise SystemExit("figure 1 size labels collide: " + ", ".join(labels))
    return labels


def draw_figure(csv_path: Path):
    rows = list(csv.DictReader(open(csv_path, newline="", encoding="utf-8")))
    panel_rows = build_panels(rows)
    order = _drawn_rows()
    n_ft = len(order)

    # Shown title (maybe two lines) and the family, for the drawn gaps.
    prepared = []
    for letter, panels in panel_rows:
        shown_row = []
        for title, cols, body, _pack in panels:
            shown_row.append((title, wrap_title(title, body), cols, body, cols[0][1]["family"]))
        prepared.append((letter, shown_row))

    def row_draw_width(shown_row) -> float:
        total = 0.0
        for i, (_title, shown, _cols, body, family) in enumerate(shown_row):
            total += body
            if i:
                prev = shown_row[i - 1]
                total += drawn_gap(prev[1], prev[3], shown, body, prev[4] == family)
        return total

    row_widths = [row_draw_width(shown_row) for _, shown_row in prepared]
    suptitle = "Available models by family, parameter weight, and training type"
    fig_w = LEFT + max(row_widths) + 0.3
    # The legend sits in the free space to the right of the shortest row.
    # Widen the figure when that gap is narrower than the legend, and when the
    # suptitle is wider than the panels.
    legend_w = text_width_inches("Instruction-Tuned", 11, "normal") + 0.55
    short_w = min(row_widths)
    fig_w = max(
        fig_w,
        LEFT + short_w + 0.4 + legend_w + 0.25,
        text_width_inches(suptitle, 14, "bold") + 0.6,
    )
    panel_h = n_ft * CELL
    fig_h = TOP + len(prepared) * panel_h + ROW_GAP * (len(prepared) - 1) + BOTTOM
    fig = plt.figure(figsize=(fig_w, fig_h), facecolor="white")

    y_top = fig_h - TOP
    family_letters = {}
    for _letter, shown_row in prepared:
        y0 = y_top - panel_h
        x0 = LEFT
        for pi, (_title, shown, cols, body, family) in enumerate(shown_row):
            if pi:
                prev = shown_row[pi - 1]
                x0 += drawn_gap(prev[1], prev[3], shown, body, prev[4] == family)
            ax = fig.add_axes([x0 / fig_w, y0 / fig_h, body / fig_w, panel_h / fig_h])
            ax.set_xlim(-0.5, len(cols) - 0.5)
            ax.set_ylim(n_ft - 0.5, -0.5)
            ax.patch.set_alpha(0)
            for i, ft in enumerate(order):
                for j, (_, r) in enumerate(cols):
                    face, txt, hatch, tc = cell_spec(ft, r)
                    ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor=face, edgecolor="white", linewidth=1.5, hatch=hatch))
                    if txt:
                        ax.text(j, i, txt, ha="center", va="center", fontsize=10 if len(txt) <= 2 else 7, fontweight="bold", color=tc)
            ax.set_xticks(range(len(cols)))
            ax.set_xticklabels(_size_ticks(cols), rotation=45, ha="right", fontsize=10)
            ax.tick_params(axis="x", length=0, pad=2)
            ax.set_yticks(range(n_ft))
            if pi == 0:
                ax.set_yticklabels(order, fontsize=10)
            else:
                ax.set_yticklabels([])
            if family not in family_letters:
                family_letters[family] = chr(ord("a") + len(family_letters))
                # First panel of a row keeps the letter in the left margin.
                # A later family on that row gets the letter just left of its first column.
                letter_x = 0.35 if pi == 0 else x0 - 0.32
                fig.text(
                    letter_x / fig_w,
                    (y0 + panel_h + 0.28) / fig_h,
                    family_letters[family],
                    fontsize=16,
                    fontweight="bold",
                    ha="left",
                    va="bottom",
                )
            ax.tick_params(axis="y", length=0)
            ax.set_title(shown, fontsize=11, fontweight="bold", pad=6)
            for sp in ax.spines.values():
                sp.set_visible(False)
            x0 += body
        y_top = y0 - ROW_GAP

    legend_elements = [mpatches.Patch(facecolor=FINETUNE_COLORS[ft], edgecolor="white", label=ft) for ft in order]
    legend_elements.append(mpatches.Patch(facecolor=EMPTY, edgecolor="gray", label="Not Available"))
    short_idx = min(range(len(row_widths)), key=lambda i: (row_widths[i], i))
    legend_y_center = (fig_h - TOP - short_idx * (panel_h + ROW_GAP) - panel_h / 2) / fig_h
    free_left = LEFT + row_widths[short_idx] + 0.35
    free_mid = (free_left + (fig_w - 0.2)) / 2
    fig.legend(handles=legend_elements, loc="center", bbox_to_anchor=(free_mid / fig_w, legend_y_center),
               fontsize=11, framealpha=0.9, title="Fine-tuning Type", title_fontsize=12.5)

    fig.suptitle(suptitle, fontsize=14, fontweight="bold", y=1 - 0.12 / fig_h)
    fig.savefig(OUT_PNG, dpi=300, facecolor="white")
    plt.close(fig)
    if text_width_inches.probe is not None:
        plt.close(text_width_inches.probe)
        text_width_inches.probe = None
    return panel_rows, fig_w, fig_h


def main():
    global OUT_CSV, OUT_PNG
    if (OUT_CSV is None) != (OUT_PNG is None):
        die("set both OUT_CSV and OUT_PNG, or neither")
    if OUT_CSV is None:
        sys.path.insert(0, str(HERE))
        import cache

        out_dir = cache.current_dir("../cross-grouping")
        OUT_CSV = out_dir / "family_table.csv"
        OUT_PNG = out_dir / "family_heatmap.png"
    rows, parent_info = build_table()
    panel_rows, fig_w, fig_h = draw_figure(OUT_CSV)
    print(f"wrote {OUT_CSV}")
    print(f"wrote {OUT_PNG}")
    print(
        f"{len(rows)} (family, version, size) rows; "
        f"mental-health = {sum(r['n_mental_health_kept'] for r in rows)}, "
        f"safety = {sum(r['n_safety_kept'] for r in rows)}, "
        f"medical = {sum(r['n_medical_kept'] for r in rows)}"
    )
    print(f"figure {fig_w:.2f} x {fig_h:.2f} in, {len(panel_rows)} rows")
    for letter, panels in panel_rows:
        print(f"  row {letter}: " + "; ".join(title for title, _, _, _ in panels))
    print("\nparent classification:")
    for p, i in sorted(parent_info.items()):
        rehost = f" (rehost of {i['canonical']})" if i["canonical"] != p else ""
        print(f"  {p}{rehost}: {i['family']} | {i['version']} | {i['size']} | base={i['status']} {i['base_repo'] or '-'} [{i['source']}]")


if __name__ == "__main__":
    main()
