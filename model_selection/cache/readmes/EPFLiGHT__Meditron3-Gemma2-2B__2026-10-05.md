---
license: gemma
language:
- en
base_model:
- google/gemma-2-2b-it
pipeline_tag: text-generation
tags:
- medical
new_version: EPFLiGHT/Apertus-70B-MeditronFO
---
### Model Card: Gemma2 Meditron-3[2B]

**Model Type:**  Large Language Model (LLM)

**Specialization:** Medicine

**Focus:** General purpose including limited resource and humanitarian settings

**Description:**
Meditron is a suite of large language models specialized in clinical medicine. The models are co-designed with a diverse range of expert clinicians and humanitarian practitioners. Its training emphasizes equitable representation, contextual diversity, and actionable real-world evidence-based guidelines. We make a particular effort to represent limited-resource and humanitarian settings, neglected populations, and diseases. This release is trained on  Gemma2[2B] base model and has the nomenclature Gemma2 Meditron-3[2B].

#### Model details

- **Developed by:** [OpenMeditron intiative](https://huggingface.co/OpenMeditron)
- **Model type:** Causal decoder-only transformer language model
- **Language(s):** English (mainly)
- **Finetuned from model:** [Gemma2-2B](https://huggingface.co/google/gemma-2-2b)
- **Input:** Text only
- **Output:** Text only
- **Status:** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we enhance model's performance.

#### Uses

Meditron-3 is a research-only model to study and evaluate the potential of LLMs in enhancing clinical decision-making and access to evidence-based medical information.


#### Direct Use

Meditron-3 is a research-only model. It is not validated for medical use (see disclaimer below).


#### Downstream Use

Meditron-3 is a suite of foundation models that have NOT been fine-tuned or instruction-tuned. However, these models can be adapted to specific downstream tasks or applications using techniques such as Reinforcement Learning from Human Feedback (RLHF) or Direct Preference Optimization (DPO). In our evaluation of the models, we have used two different methods for downstream question-answering tasks:

1. In-context learning with k demonstrations added to the prompt.
2. Model fine-tuning for Q&A tasks using specific training datasets.


#### Training Data

This new data mixture comprises expert-curated publicly available data and combines various sources:
- **Clinical Guidelines:** a dataset of internationally-recognized clinical practice guidelines from various healthcare-related sources across the world, including hospitals and international organizations.
- **Peer-Reviewed Medical Publications:** full-text medical articles.
- **Synthetic Differential Diagnoses:** synthetic conversation like data for differential diagnosis. 
- **Replay Data:** general domain pretraining data sampled from multiple state of the art pretraining and instruction tuning.
- **LLM-enhanced Medical MCQ:** medical multiple-choice questions enriched with LLMs.

Additional information about the datasets will be included in the Meditron-3 publication.

#### Evaluation

| Model Name                  | MedmcQA | MedQA  | PubmedQA | Average |
|-----------------------------|---------|--------|----------|---------|
| google/gemma-2-2b-it        | 42.89   | 44,62  | 74.00    | 53.84   |
| gemMeditron-2-2b-it         | 46.57   | 43.21  | 74,40    | 54.69   |
| Difference (gemMeditron vs.)| 3.58    | -1.41  | 0.40     | 0.85    |

We evaluated Meditron on medical multiple-choice questions using [lm-harness](https://github.com/EleutherAI/lm-evaluation-harness) for reproducibility.
While MCQs are valuable for assessing exam-like performance, they fall short of capturing the model's real-world utility, especially in terms of contextual adaptation in under-represented settings. Medicine is not multiple choice and we need to go beyond accuracy to assess finer-grained issues like empathy, alignment to local guidelines, structure, completeness and safety. To address this, we have developed a platform to collect feedback directly from experts to continuously adapt to the changing contexts of clinical practice.

#### Paper
The Meditron-3 publication is currently in progress and will be released at a later date.

#### Legal Disclaimer
THIS SOFTWARE AND MODEL ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS, CONTRIBUTORS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
These models are a research tool intended for use in the field of computational linguistics and medicine. They are not intended to be used as diagnostic tools or for clinical decision-making without appropriate validation and regulatory approval. The content and data provided with the models do not replace the expertise of healthcare professionals. Healthcare professionals should use their professional judgment in evaluating the outputs of the Gemma models. Patients should not use the model outputs for self-diagnosis or treatment without consulting a qualified healthcare provider.
THE INFORMATION IS NOT INTENDED FOR CLINICAL DECISION-MAKING, IS NOT INTENDED TO BE USED IN THE DIAGNOSIS OR TREATMENT OF PATIENTS, AND MAY NOT BE USEFUL OR APPROPRIATE FOR ANY CLINICAL PURPOSE.
UNDER NO CIRCUMSTANCES CAN USERS USE THE NAME “YALE” OR "EPFL" OR “YALE UNIVERSITY,” OR ANY AFFILIATED INSTITUTION NOR ANY VARIATION OR ADAPTATION THEREOF, NOR ANY TRADEMARK, TRADENAME OR OTHER DESIGNATION OWNED BY YALE, NOR THE NAMES OF ANY OF ITS TRUSTEES, OFFICERS, FACULTY, STUDENTS, EMPLOYEES OR AGENTS, FOR ANY PURPOSE WITHOUT THE PRIOR WRITTEN CONSENT OF YALE IN EACH INSTANCE, SUCH CONSENT TO BE GRANTED OR WITHHELD BY YALE IN ITS SOLE DISCRETION.

Meditron3-Gemma2 [2B] is licensed under the Gemma License.

This model is provided under the terms of the Gemma Model License Agreement, as issued by Google LLC. By using or distributing this model, you agree to comply with the terms of that license.

Disclaimer:
This model is provided "as-is" without warranties or conditions of any kind, either express or implied. Google and any contributors disclaim all liability for any damages resulting from use of the model.

For more information, visit: https://ai.google.dev/gemma