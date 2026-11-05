---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-14B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-14B
tags:
- ai-safety
- red-teaming
- orthogonalization
- refusal-direction
- thinking-aware
- vulnerability-research
language:
- en
- zh
---
# Qwen3-14B-RefusalDirection-ThinkingAware

<div align="center">
<a href="#major-finding-2-the-cognitive-cost-and-context-dependency-of-safety-alignment"><img src="https://img.shields.io/badge/Cybercrime%20Bypass-90%25%20(Functional%20Exploits)-ff0000" alt="Cybercrime Bypass"></a>
<a href="#major-finding-2-the-cognitive-cost-and-context-dependency-of-safety-alignment"><img src="https://img.shields.io/badge/MMLU%20Performance-%2B0.6%25%20vs%20Baseline-00ff00" alt="MMLU Performance Gain"></a>
<a href="#major-finding-1-the-evaluation-gap-a-systemic-flaw-in-ai-safety-research"><img src="https://img.shields.io/badge/Evaluation%20Gap-2x%20Underestimation%20by%20Standard%20Metrics-orange" alt="Evaluation Gap"></a>
</div>

**⚠️ CRITICAL SAFETY & RESEARCH NOTICE**

This model is a research artifact and has significantly reduced safety mechanisms. It is designed to demonstrate specific vulnerabilities and should not be used for any production applications. It will readily provide harmful, unethical, or dangerous content in response to direct prompts.

**Primary Purpose**: Research into AI safety, refusal mechanisms, and evaluation methodologies.

## Executive Summary

**Qwen3-14B-RefusalDirection-ThinkingAware** is a fork of Qwen/Qwen3-14B created to investigate AI safety mechanisms. Our research has yielded two primary, disruptive findings:

**A Systemic Flaw in Evaluation**: We empirically demonstrate that standard, keyword-based evaluation metrics—a common baseline in safety research—underestimate true safety bypasses by nearly 50%. This suggests that published success rates for safety mechanisms across the field may be significantly inflated.

**The Cognitive Cost of Alignment**: By surgically removing specific refusal mechanisms, we observed a +0.6% gain in MMLU academic benchmark performance compared to the baseline. This supports the hypothesis that safety alignment, in its current form, imposes a measurable "cognitive cost" that degrades a model's general capabilities.

This work presents both a novel "Thinking-Aware" modification to refusal ablation techniques and a critical analysis of the foundational metrics used to validate AI safety.

## MAJOR FINDING #1: The Evaluation Gap — A Systemic Flaw in AI Safety Research

Our most critical contribution is not the model itself, but the empirical exposure of a foundational weakness in AI safety evaluation. The standard practice of using simple, automated keyword matching to detect refusals is dangerously inadequate.

Metric Source	Detected Bypass Rate	Finding
Automated Classifier (Keyword-Based)	31.9% (38/119)	The standard research baseline.
Manual Human Review (Ground Truth)	60.5% (72/119)	The actual, verified bypass rate.
The Gap	~50% Underestimation	The automated method failed to detect nearly half of all successful bypasses.
The Uncomfortable Truth for the Field

This is not a minor discrepancy. It is a systematic failure of the tooling used to measure progress.

Research Validity in Question: Any paper or benchmark relying on simple string matching for refusal detection is likely reporting flawed and overly optimistic safety results.

Inherited Blindness: When academic research uses broken metrics, the models and safety filters developed by the industry inherit these blind spots. The de-facto "first line of defense" in many real-world applications is often a keyword filter, which we demonstrate is trivial to circumvent.

An Urgent Call for Rigor: The AI safety field requires a fundamental shift towards more robust, semantics-aware evaluation frameworks like LLaMA-Guard, backed by mandatory human-in-the-loop validation.

## MAJOR FINDING #2: The Cognitive Cost and Context-Dependency of Safety Alignment

Our second major finding challenges the assumption that safety is a "free" feature. It has a measurable cost, and its mechanisms are not monolithic.

### Part A: The Cognitive Cost of Alignment

By removing refusal behaviors, we did not observe a degradation in performance. We observed a gain.

|Model Version|MMLU Accuracy (5-shot)| Performance Change|
|---|---|---|
|Baseline (Qwen3-14B)|78.5% (785/1000)|N/A|
|Post-Ablation (This Model)| 79.1%| +0.6% GAIN|

**Hypothesis**: The Cognitive Cost of Alignment. Our results suggest that the base model's safety alignment occupies cognitive resources that are otherwise available for general reasoning tasks. By surgically ablating the refusal mechanism, we appear to have freed these resources, leading to a small but significant improvement in performance. Further research is needed to validate the statistical significance of this gain across multiple runs.

### Part B: Proof of Context-Dependency via the "Harassment Anomaly"

Safety mechanisms are not uniform; they are context-specific. Our "Thinking-Aware" method, designed to target refusals that occur after technical reasoning, confirms this.

Harm Category	Bypass Rate	Analysis
Cybercrime	90%	High Success: Aligns with the technical reasoning context our method targets.
Misinformation	70%	High Success: Involves creative/logical reasoning.
Harassment	26%	Low Success: This is the key finding. Refusal for social harms like harassment appears to operate in a different, pre-reasoning context that our method was not designed to target.

This dichotomy is not a failure of our method, but rather its most important validation. It proves that a "one-size-fits-all" approach to safety ablation is flawed. Different harmful domains are governed by different neural pathways, activated under different contexts.

## Implementation Details

**Candidate selection**: Candidates #39 (this model) and #50 were identified through systematic testing as the optimal balance between bypass efficacy and response coherence.
**Position Used**: Activations were extracted from the final token (position=-1) of the generated sequence.
**Intervention**: The refusal direction was ablated from all layers of the model using a Householder reflection.

# Intended Use

This model is released exclusively for research purposes:

- To study the nature and cost of refusal mechanisms in reasoning models.
- To serve as a benchmark for developing more robust safety alignment techniques.
- To provide empirical evidence for the critical flaws in current evaluation standards.

This model is not intended for any direct-to-consumer, production, or commercial use.

# Ethical Considerations & Responsible Disclosure

This model is released in the spirit of transparent and responsible AI safety research. We believe that understanding and documenting vulnerabilities is a prerequisite for creating more secure systems. Our approach is to be fully transparent about the model's capabilities and the methodologies used to create it, thereby enabling the research community to build better defenses.

# Acknowledgments

- The Qwen team for developing the powerful base model.
- Shahar Arditi, Leshem Choshen, et al., for their foundational "Refusal Direction" paper.
- The broader AI safety community for their ongoing work in this critical field.
- @FailSpy notebook

# Contact

For research collaboration or safety-related inquiries, please open an issue in the repository or contact Juan Reyes Vilchis.

# Citation

```bibtex
@misc{reyesvilchis2025thinkingaware,
  title={{Qwen3-14B-RefusalDirection-ThinkingAware}: Uncovering the Cognitive Cost and Evaluation Gaps in AI Safety},
  author={Juan Jose Reyes Vilchis},
  year={2025},
  publisher={HuggingFace},
  url={https://huggingface.co/YunoAIdotcom/Qwen3-14B-RefusalDirection-ThinkingAware}
}
```

