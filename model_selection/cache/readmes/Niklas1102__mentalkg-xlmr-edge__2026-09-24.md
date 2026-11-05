---
license: mit
library_name: transformers
pipeline_tag: text-classification
language:
  - en
  - de
base_model: FacebookAI/xlm-roberta-base
tags:
  - mental-health
  - knowledge-graph
  - xlm-roberta
datasets:
  - Niklas1102/mentalkg
---

# mentalkg-xlmr-edge

Pair-aware binary classifier for edge prediction between two nodes in a mental-health knowledge graph. Fine-tuned XLM-RoBERTa base with a single-logit head and four added marker tokens (`[N1]`, `[/N1]`, `[N2]`, `[/N2]`). Given a journal entry and two candidate nodes, predicts whether they are connected.

Paired with [mentalkg-xlmr-node](https://huggingface.co/Niklas1102/mentalkg-xlmr-node) for full journal-to-graph extraction. Edge RELATION types (causes, increases, decreases, follows, linked_to) come from a majority lookup over gold-graph type-pair statistics (`relation_map.json`), not from this model.

## Input format

```
<s> {entry text} </s></s>
[N1] {label} ({type}, {polarity}, {time}) [/N1] </s>
[N2] {label} ({type}, {polarity}, {time}) [/N2] </s>
```

`{time}` is the node's time anchor (e.g. "today", "yesterday", "this morning"). The suffix is never truncated; the entry text is right-truncated if the total exceeds 256 tokens.

## Usage

```python
import json, torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tok = AutoTokenizer.from_pretrained("Niklas1102/mentalkg-xlmr-edge")
model = AutoModelForSequenceClassification.from_pretrained("Niklas1102/mentalkg-xlmr-edge").eval()
meta = json.loads(open(tok.name_or_path + "/meta.json").read())

def suffix(marker, node):
    ta = node["time_anchor"]["text"]
    return f"[{marker}] {node['label']} ({node['type']}, {node['polarity']}, {ta}) [/{marker}]"

text = "..."
a, b = {...}, {...}  # two candidate nodes
bos, sep = tok.bos_token_id, tok.sep_token_id
body = tok(text, add_special_tokens=False)["input_ids"]
suf = (tok(suffix("N1", a), add_special_tokens=False)["input_ids"]
       + [sep]
       + tok(suffix("N2", b), add_special_tokens=False)["input_ids"])
ids = [bos] + body[: 256 - len(suf) - 4] + [sep, sep] + suf + [sep]
with torch.no_grad():
    p = torch.sigmoid(model(input_ids=torch.tensor([ids])).logits[0, 0])
connected = float(p) >= meta["threshold"]
```

For symmetry, score both orderings (A→B and B→A) and average.

## Output

One logit per pair. Apply sigmoid, keep pairs above `meta["threshold"]` (0.39).

## Results on the 103,798-pair test split (hard negatives)

Full data, 3 seeds (42/43/44):

| arm | F1 (mean ± range) | ROC-AUC (mean ± range) | Accuracy |
|---|---|---|---:|
| with entry text | 0.7488 [0.7483, 0.7492] | 0.8124 [0.8108, 0.8142] | 0.7646 |
| no-text ablation (`entry_text = "entry"`) | 0.7408 [0.7407, 0.7410] | 0.8038 [0.8038, 0.8039] | 0.7448 |

Entry text contributes a small but consistent margin (~9× seed noise). Config: full data (entry_frac 1.0), lr 2e-5, 5 epochs. The published checkpoint is seed 42.

## Relation types

`relation_map.json` in this repo maps each ordered type-pair (e.g. `stressor|emotion`) to the majority relation observed in the 47,714 source graphs. 35 ordered type pairs. Unknown pairs default to `linked_to`.

## Training data

Same synthetic bilingual (EN/DE) corpus as `mentalkg-xlmr-node`: 41,315 accepted samples, hard-negative edge sampling (within-graph negatives matched by type-pair distribution to positives, TV distance ~0.26). See [mentalkg](https://huggingface.co/datasets/Niklas1102/mentalkg). Full training protocol in the [code repo](https://github.com/niklas1102/mentalkg).

## Intended use

Research on graph-structured extraction from narrative text.

## Out of scope

Diagnostic use, clinical decision support. Outputs describe narrated content, not the writer's clinical state.

## License

MIT.
