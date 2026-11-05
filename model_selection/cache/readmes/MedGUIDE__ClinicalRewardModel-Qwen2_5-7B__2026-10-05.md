# ClinicalRewardModel-Qwen2_5-7B

This is a 5-head reward model fine-tuned on clinical decision-making data using the [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) backbone. It is trained to evaluate clinical vignette–based multiple-choice questions across five expert-defined clinical criteria:

- Clinical Plausibility  
- Clinical Utility  
- Quality of Decision Path  
- Alignment to Decision Path  
- Correctness of the Suggested Answer  

Each head independently scores one dimension on a 1–5 Likert scale. This model supports fine-grained quality filtering for guideline-based QA datasets such as [MedGUIDE-MCQA-8K](https://huggingface.co/datasets/MedGUIDE/MedGUIDE-MCQA-8K).