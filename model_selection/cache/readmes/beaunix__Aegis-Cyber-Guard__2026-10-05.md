---
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
tags:
- cybersecurity
- blue-team
- SOC
- qlora
- unsloth
language:
- en
---
 
# Aegis-Cyber-Guard (Qwen2.5-7B)
 
A blue-team cybersecurity analyst assistant, fine-tuned from Qwen2.5-7B-Instruct with
QLoRA. Part of the Aegis-CyberSec-Guard project: a defensive SOC-oriented system where
specialized detectors produce verifiable signals and this model reasons over them to
write incident analysis and remediation guidance.
 
## Role
 
Acts as a defensive security analyst / SOC assistant. It analyzes logs, network events,
and vulnerability context, explains findings, and cites MITRE ATT&CK techniques and CVEs
where relevant. It does not generate exploit code, malware, or offensive tooling.
 
## Training
 
- **Base model:** Qwen2.5-7B-Instruct
- **Method:** QLoRA (4-bit), rank 64, alpha 64, via Unsloth
- **Objective:** supervised fine-tuning, train-on-responses-only
- **Checkpoint:** step 1200, validation loss 0.824
- **Datasets:** a curated instruction mix of
  - Cybersecurity-Dataset-Fenrir-v2.1 (defensive reasoning)
  - Cybersecurity-Dataset-Heimdall-v1.1 (threat hunting)
  - All-CVE-Records (vulnerability analysis, filtered)
  - a phishing-email classification set (second task)
- Each task is tagged with a distinct system prompt so the model conditions its output
  format on the role it is playing.
 
## Known limitation — read before using
 
This model is a **reasoning and language layer, not a knowledge base.** It should not be
trusted to recall specific CVE facts from memory. When asked about a specific CVE by ID,
it will confidently produce a plausible-looking but frequently **incorrect** record —
wrong CVSS, wrong affected products, invented reference URLs. This is expected: a 7B model
cannot memorize a vulnerability database, and forcing it to try produces hallucination.
 
**The intended architecture supplies the real CVE record via retrieval (RAG) and has the
model summarize that record, never recall it.** A VulnLookup retrieval component is planned
for a future release. Until then, do not rely on this model's CVE-specific output as fact.
 
Where the model is strong: reasoning about attack patterns, log/event interpretation,
defensive remediation, MITRE ATT&CK framing, and producing well-structured analyst-style
writeups — as long as the specific facts it reasons over are supplied to it.

We are pending to add CyberSec RAG  in version v2 for better reasoning.
 
## Intended use
 
Research and portfolio demonstration of a defensive security agent architecture. Not a
substitute for a professional security team or an authoritative vulnerability database yet.

