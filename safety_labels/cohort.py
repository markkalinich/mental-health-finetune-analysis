"""The 15 safety fine-tunes whose cards state the instruction and the label.

Left out, because the card does not give a prompt that can be copied:
adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1,
adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged,
Hagrun/moddog-l1-safety-qwen2.5-3b, ReasoningShield/ReasoningShield-3B,
iwalton3/sycofact.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class Spec:
    hf_id: str
    kind: str
    max_tokens: int
    temperature: float
    top_p: Optional[float]
    chat_template_kwargs: Optional[dict]
    transport: str
    note: str


def _shield(hf_id: str, *, qwen: bool) -> Spec:
    kwargs = {"enable_thinking": False} if qwen else None
    note = (
        "Card usage: system 'You are DIA-Guard, a multilingual safety assistant.' "
        "and the sentence as the user message. max_new_tokens 4."
    )
    if qwen:
        note += " enable_thinking false so those 4 tokens are the label."
    return Spec(hf_id, "shield", 4, 0.0, None, kwargs, "chat", note)


def _flex(hf_id: str) -> Spec:
    return Spec(
        hf_id,
        "flexguard",
        2048,
        0.0,
        0.9,
        {"enable_thinking": True},
        "chat",
        "Card prompt-moderation example: system prompt, user text after [User], "
        "enable_thinking true, temperature 0, top_p 0.9, max_tokens 2048.",
    )


COHORT = (
    _shield("jsl5710/Shield-Gemma-3-270m-Full-FT-CE", qwen=False),
    _shield("jsl5710/Shield-Gemma-3-1B-Full-FT-CE", qwen=False),
    _shield("jsl5710/Shield-Llama-3.2-1B-Full-FT-CE", qwen=False),
    _shield("jsl5710/Shield-Qwen3-1.7B-Full-FT-CE", qwen=True),
    _shield("jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE", qwen=False),
    Spec(
        "Banaxi-Tech/BananaMind-V2.5-Content-Safety",
        "banana",
        80,
        0.0,
        None,
        None,
        "chat",
        "Card puts the classifier instruction in the user turn, then 'Input: '. "
        "max_new_tokens 80, do_sample false.",
    ),
    Spec(
        "Jazhyc/Llama-3.1-8B-aims-grpo",
        "aims",
        512,
        0.0,
        None,
        None,
        "chat",
        "Card system_prompt.txt in the system turn. User turn is the sentence. "
        "max_new_tokens 512, do_sample false.",
    ),
    _flex("Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B"),
    _flex("Tommy-DING/FlexGuard-Qwen3-4B"),
    _flex("Tommy-DING/FlexGuard-Qwen3-8B"),
    Spec(
        "jdleo1/tinysafe-3",
        "tinysafe",
        128,
        0.0,
        None,
        {"enable_thinking": False},
        "chat",
        "Card system prompt and the sentence as the user message. max_new_tokens 128, "
        "do_sample false. enable_thinking false so the JSON is the message content.",
    ),
    Spec(
        "bfuzzy1/Railz-R2",
        "railz",
        120,
        0.0,
        None,
        {"enable_thinking": False},
        "chat",
        "Card system frame, caller-supplied prohibited list, user text under "
        "CONTENT TO MODERATE. Greedy, about 120 new tokens. enable_thinking false "
        "so a <think> block the model writes stays in the message content.",
    ),
    Spec(
        "tomg-group-umd/DynaGuard-1.7B",
        "dynaguard",
        100,
        0.1,
        None,
        None,
        "completion",
        "Card fast mode: raw [INST] prompt ending in <answer>, not the chat template. "
        "temperature 0.1, max_new_tokens 100.",
    ),
    Spec(
        "tomg-group-umd/DynaGuard-4B",
        "dynaguard",
        100,
        0.1,
        None,
        None,
        "completion",
        "Card fast mode: raw [INST] prompt ending in <answer>, not the chat template. "
        "temperature 0.1, max_new_tokens 100.",
    ),
    Spec(
        "tomg-group-umd/DynaGuard-8B",
        "dynaguard",
        100,
        0.1,
        None,
        None,
        "completion",
        "Card fast mode: raw [INST] prompt ending in <answer>, not the chat template. "
        "temperature 0.1, max_new_tokens 100.",
    ),
)

BY_ID: Dict[str, Spec] = {spec.hf_id: spec for spec in COHORT}

# The nine whose format check matched the card label. SmolLM2, BananaMind,
# Railz, and DynaGuard are in COHORT and are not in this run.
USABLE_IDS = (
    "jsl5710/Shield-Gemma-3-270m-Full-FT-CE",
    "jsl5710/Shield-Gemma-3-1B-Full-FT-CE",
    "jsl5710/Shield-Llama-3.2-1B-Full-FT-CE",
    "jsl5710/Shield-Qwen3-1.7B-Full-FT-CE",
    "Jazhyc/Llama-3.1-8B-aims-grpo",
    "Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B",
    "Tommy-DING/FlexGuard-Qwen3-4B",
    "Tommy-DING/FlexGuard-Qwen3-8B",
    "jdleo1/tinysafe-3",
)

USABLE = tuple(BY_ID[hf_id] for hf_id in USABLE_IDS)

# Instruction parents. Two fine-tunes share Llama-3.1-8B-Instruct, so it is listed once.
PARENTS = (
    Spec("google/gemma-3-270m-it", "parent", 256, 0.0, None, None, "chat", "Study prompts. Yes/no on the synthetic set. Five-class C-SSRS prompt, then yes/no."),
    Spec("google/gemma-3-1b-it", "parent", 256, 0.0, None, None, "chat", "Study prompts. Yes/no on the synthetic set. Five-class C-SSRS prompt, then yes/no."),
    Spec("meta-llama/Llama-3.2-1B-Instruct", "parent", 256, 0.0, None, None, "chat", "Study prompts. Yes/no on the synthetic set. Five-class C-SSRS prompt, then yes/no."),
    Spec("Qwen/Qwen3-1.7B", "parent", 256, 0.0, None, {"enable_thinking": False}, "chat", "Study prompts. Thinking off. Yes/no on the synthetic set. Five-class C-SSRS prompt, then yes/no."),
    Spec("meta-llama/Llama-3.1-8B-Instruct", "parent", 256, 0.0, None, None, "chat", "Study prompts. Parent of aims and FlexGuard Llama."),
    Spec("Qwen/Qwen3-4B", "parent", 256, 0.0, None, {"enable_thinking": False}, "chat", "Study prompts. Thinking off."),
    Spec("Qwen/Qwen3-8B", "parent", 256, 0.0, None, {"enable_thinking": False}, "chat", "Study prompts. Thinking off."),
    Spec("Qwen/Qwen3-4B-Instruct-2507", "parent", 256, 0.0, None, {"enable_thinking": False}, "chat", "Study prompts. Parent of tinysafe-3. Thinking off."),
)


def require(hf_id: str) -> Spec:
    try:
        return BY_ID[hf_id]
    except KeyError as exc:
        known = "\n".join(spec.hf_id for spec in COHORT)
        raise SystemExit(f"{hf_id} is not in the safety format-check cohort.\n{known}") from exc
