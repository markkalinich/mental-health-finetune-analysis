# openmed-community/AFM-4.5B-OpenMed

## Sources

- https://huggingface.co/openmed-community/AFM-4.5B-OpenMed/raw/main/README.md — current model card; identical to the cached card (`cmp` exit 0)
- https://huggingface.co/api/models/openmed-community/AFM-4.5B-OpenMed — file list and safetensors count
- https://huggingface.co/openmed-community/AFM-4.5B-OpenMed/raw/main/config.json — context length and architecture
- https://huggingface.co/openmed-community/AFM-4.5B-OpenMed/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/openmed-community/AFM-4.5B-OpenMed/raw/main/mergekit_config.yml — Arcee Fusion merge of the base and a local GRPO checkpoint
- https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA dataset card (loads; exam questions)
- https://huggingface.co/datasets/UCSC-VLAA/MedReason — MedReason dataset card (32,682 rows; does not name this repository)
- https://arxiv.org/abs/2504.00993 — MedReason paper linked from that dataset card, not from this model card
- https://hotaisle.xyz/ — compute-credit sponsor named on the card

## Record

Three data sources are named. The card says: "SFT data: Proprietary synthetic medical data + search traces." That set has no Hub id and no row count. DPO uses "MedMCQA-derived preferences." The Hub dataset with that content is `openlifescienceai/medmcqa` (train 182,822, validation 4,183, test 6,150). The card does not say it used that Hub id or how many preference pairs it built. GRPO uses "MedReason verifiable rewards." The Hub dataset is `UCSC-VLAA/MedReason`, 32,682 rows. Its card says the reasoning traces are generated from clinical question-answer pairs through a knowledge graph, so the provenance is mixed. It does not name this checkpoint. Neither dataset card states a language.

The objectives are supervised fine-tuning, then DPO, then GRPO. The card says: "Trained with a simple 3-stage recipe (SFT → DPO → GRPO-CoT)." It does not say full fine-tuning or LoRA, and it states no rank, epoch count, step count, learning rate, or training batch size. The uploaded model is a weight merge. `mergekit_config.yml` sets `merge_method: arcee_fusion`, `base_model: arcee-ai/AFM-4.5B`, and a second model that is a local path ending in `checkpoint-1600`. There is no `adapter_config.json` and no `generation_config.json`.

The parent is `arcee-ai/AFM-4.5B`. The card and the merge file agree. The safetensors total is 4,619,189,760 parameters. The card's language tag is `en`. The Hub reports the weight dtype as F32. `config.json` and the merge file say bfloat16.

The use claim is strong. The quickstart system line is: "You are a careful medical assistant." The warning is an explicit prohibition. The card says: "should not be used for diagnosis or treatment." It also says the model is "not a clinician" and that unsupervised patient care and generating prescriptions are out of scope.

The purpose is stated. The card says the model is "for education and research use" and "Intended: Medical SLM's research, tool-augmented retrieval demos." The named audience is a researcher or developer. The functions are answering medical questions, answering exam-style multiple choice, and clinical reasoning with a short rationale. The output is a chat reply that can include a rationale and a final answer. The clinical tasks are medical question answering and exam answering. MMLU is evaluation only: 61.10 versus the base 55.53. The specialty is general medicine. No narrower field is named as the model's domain.

Serving is text only. The example question is "Briefly: cellulitis vs erysipelas differences?" Generation in the example is `max_new_tokens=256` and `do_sample=False`. `max_position_embeddings` is 65536. The license is `apache-2.0`. No paper or GitHub training repository is linked from the card. The card says a methodology blog post is forthcoming.

Inventory methods `dpo|grpo|sft` and parent `arcee-ai/AFM-4.5B` match. Inventory datasets `MedMCQA | MedReason` match the two public names. The proprietary SFT data is not in that cell.
