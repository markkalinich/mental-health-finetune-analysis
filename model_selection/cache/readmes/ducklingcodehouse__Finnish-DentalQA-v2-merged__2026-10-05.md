---
library_name: transformers
tags:
- transformers
- unsloth
- llama
- finnish
- medical
- dental
- healthcare
- research-only
license: apache-2.0
language:
- fi
base_model: Finnish-NLP/Ahma-3B-Instruct
---

# Finnish-DentalQA-v2-merged

**Note: Version 3 is now available with a more capable base model! See [Finnish-DentalQA-v3](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v3) (recommended, 4B parameters, full fine-tuning on Ahma-2-4B-Instruct).**

**Finnish-language conversational AI assistant specialized for dental medicine.** This is a fine-tuned large language model (LLM) that generates structured text responses to dental consultation queries, designed to simulate professional dentist-to-dentist consultations with clinical reasoning and recommendations.

**RESEARCH USE ONLY - NOT FOR MEDICAL DECISIONS**

- **Developed by:** [Heikki Saxén](https://fi.linkedin.com/in/heikkisaxen) / [Duckling Codehouse Oy](https://www.linkedin.com/company/duckling-codehouse-oy/) ([ducklingcodehouse](https://huggingface.co/ducklingcodehouse))
- **Supported by:** [Entteri Professional Software Oy](https://www.entteri.com/) (makers of AssisDent dental PMS)
- **License:** apache-2.0
- **Base Model:** Finnish-NLP/Ahma-3B-Instruct (by Aapo Tanskanen & Rasmus Toivanen)
- **Context Length:** 2048 tokens
- **Release Date:** September 4, 2025

LoRA fine-tuned model merged into standalone format for Finnish dental medicine consultations between healthcare professionals. Trained on 50,132 synthetic dental conversations (approximately 80% expert clinical cases, 20% concept explanations) covering a broad range of different scenarios. Generated using pipeline with GPT-4.1.

**Version 2 Improvements:** This v2 release significantly expands the training dataset from 30,908 to 50,132 conversations, with enhanced clinical coverage including psychological, social, and ethical aspects of dental care. The model demonstrates improved conversation handling and reduced hallucination risk when encountering off-topic queries or unusual user interactions, making it more robust for professional consultations.

**Research Focus:** This model demonstrates domain-specific fine-tuning with low computational resources. The goal is to explore how specialized models can be trained and deployed on consumer hardware (including personal GPUs) rather than requiring high-end infrastructure.

**System Prompt Recommendation:** This model was trained with a specific system prompt. For best results, we recommend using the same prompt format shown in the examples below.

**Response Format:** The model is trained to structure all clinical responses in three sections: "### Tausta" (Background), "### Arvio" (Assessment), "### Suositus" (Recommendation).

**Context Limit:** 2048 tokens total (input + output). Long conversations may need trimming to fit within this limit.

This llama model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's Transformers library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

## Model Comparison

| Version | Base Model | Parameters | Training Method | Dataset | Notes |
|---------|-----------|------------|-----------------|---------|-------|
| v3 | Ahma-2-4B-Instruct | 4B | Full fine-tuning | 50,132 | Latest, highest quality |
| **v2** | Ahma-3B-Instruct | 3B | LoRA | 50,132 | Enhanced dataset, available as LoRA and merged |
| v1 | Ahma-3B-Instruct | 3B | LoRA | 30,908 | Original release, available as LoRA and merged |

**v3 (recommended)**: [ducklingcodehouse/Finnish-DentalQA-v3](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v3) - Full fine-tuned on Ahma-2-4B-Instruct, highest quality

**v2 LoRA Version**: [ducklingcodehouse/Finnish-DentalQA-v2-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-lora) - Enhanced training (50,132 samples), separate adapter files, requires base model

**v2 Merged Version (this model)**: Enhanced training (50,132 samples), merged into standalone model

**v1 LoRA Version**: [ducklingcodehouse/Finnish-DentalQA-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-lora) - Original dataset (30,908 samples), separate adapter files, requires base model

**v1 Merged Version**: [ducklingcodehouse/Finnish-DentalQA-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-merged) - Original dataset (30,908 samples), merged into standalone model

## Installation

```bash
pip install transformers torch accelerate
```

## Loading the Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "ducklingcodehouse/Finnish-DentalQA-v2-merged",
    torch_dtype=torch.float16,  # Recommended: FP16 for this model
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("ducklingcodehouse/Finnish-DentalQA-v2-merged")
```

## Generate Response

```python
# Use exact system prompt from training
system_prompt = """Olet kokenut suomalainen hammaslääkäri. Vastaat ammattimaisesti kollegojesi
kysymyksiin käyttäen oikeaa hammaslääketieteellistä terminologiaa ja viittaat Käypä hoito
-suosituksiin kun relevanttia."""

user_question = """87-vuotias nainen, jolla on vaikea muistisairaus, asuu palvelutalossa ja on
kotihoidon piirissä. Potilaalla on hampaattomuus, yläleuan kokoproteesi ja alaleuassa 6
luonnollista hammasta. Lääkityksenä on mm. rivaroksabaani eteisvärinään, donepetsiili,
metoprololi, kalsium+D-vitamiini, sekä useita muita lääkkeitä (yhteensä 9). Suun limakalvot
ovat kuivat, kielessä fissuroitumista, ja proteesin alla lievää punoitusta. HbA1c 46 mmol/mol,
BMI 22. Kotihoito raportoi potilaan nielevän huonosti ja syljen erityksen olevan vähäistä.
Karies- ja parodontiittiriski arvioidaan korkeaksi. Miten suosittelisit suun hoidon
järjestämistä ja priorisointia tässä tilanteessa?"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_question}
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

# Recommended settings
with torch.no_grad():
    outputs = model.generate(
        inputs,
        max_new_tokens=600,
        temperature=0.1,
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.pad_token_id
    )

response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
print(response)

# Expected example response:
# ### Tausta
# Potilas on iäkäs, monisairas ja käyttää antikoagulanttihoitoa (rivaroksabaani), mikä
# lisää vuotoriskiä toimenpiteissä. Kuiva suu liittyy sekä lääkitykseen että ikääntymiseen.
# Hampaattomuus ja vähäinen syljeneritys altistavat limakalvovaurioille ja infektioille.
# Nielemisvaikeudet ja korkea karies- ja parodontiittiriski korostavat ehkäisevien
# toimenpiteiden merkitystä.
#
# ### Arvio
# Kliinisesti potilaalla on merkittävä hyposalivaatio (stimuloitu sylki <0,7 ml/min),
# joka yhdessä polyfarmasian kanssa lisää riskiä limakalvosairauksille ja infektioille.
# Proteesin alla oleva punoitus voi viitata proteesi-stomatiittiin tai kandidaasiin.
# Rivaroksabaanin vuoksi invasiivisia toimenpiteitä tulee välttää ellei välttämätöntä.
# Kotihoidon resurssit ja potilaan toimintakyky rajoittavat laajojen hoitojen toteutusta.
#
# ### Suositus
# Painopiste on limakalvojen kosteutuksessa (esim. keinotekoiset syljentuotteet) ja
# proteesin puhtauden ylläpidossa. Kotihoidolle annetaan selkeät ohjeet päivittäisestä
# proteesin puhdistuksesta ja limakalvojen tarkkailusta. Syljen eritystä voidaan tukea
# säännöllisellä nesteytyksellä ja tarvittaessa ksylitolituotteilla. Lääkärin kanssa
# arvioidaan mahdollisuudet vähentää kuivan suun aiheuttajia. Säännöllinen suun tarkastus
# (3–6 kk välein) on suositeltavaa. Käypä hoito -suositukset: "Lyhentyneen hammaskaaren
# hoito", "Karies (hallinta)" ja "Parodontiitti".
```

## Example

**User:** 19-vuotias nuori aikuinen, jolla on syvä purentavika ja ortodontin suosittelema oikomishoito, mutta joka vastustaa hoitoa esteettisistä ja eettisistä syistä ("en halua metallia suuhuni") – miten hoito tulisi toteuttaa kliiniset tarpeet ja potilaan arvot huomioiden?

**Assistant:**
### Tausta
Nuorella aikuisella esiintyvä syvä purentavika yhdistettynä ortodonttiseen hoitoon vaatii huolellista moniammatillista suunnittelua. Potilaan kieltäytyminen metallisista retentiolangoista sekä eettiset syyt rajoittavat perinteisten kiinteiden kojeiden käyttöä. Purennan korjaus voi olla haastavaa ilman riittävää tukea, erityisesti jos hampaiston ahtautta esiintyy merkittävästi.

### Arvio
Kliinisesti tulee arvioida purennan toiminnallisuus, mahdollinen TMD-oireilu sekä parodontaalinen tila. Esteettiset tavoitteet voidaan huomioida tarjoamalla vaihtoehtoisia retentiomenetelmiä, kuten läpinäkyvät muovikalvot tai alignerit. Potilaan motivaatio ja kyky sitoutua hoitoon ovat keskeisiä onnistumisen kannalta.

### Suositus
Suosittelen keskustelemaan potilaan kanssa hoidon tavoitteista ja mahdollisista kompromisseista. Mikäli potilas hyväksyy aligner-hoidon, voidaan käyttää läpinäkyviä muovikalvoja tukemaan etualueen liikkeitä. Jos taas kiinteä koje valitaan, varmistetaan hyvä suuhygienia ja säännöllinen kontrolli; tällöin vältetään iatrogeenisia vaurioita. Yhteistyö erikoishammaslääkärin ja mahdollisesti psykologin kanssa voi olla hyödyllistä motivaation tukemisessa.

**Follow-up:** Miten varmistaisit hoidon pitkäaikaisen onnistumisen ja purennan stabiliteetin, jos potilas kieltäytyy kokonaan metallisista retentioratkaisuista?

**Assistant:**
### Tausta
Metallisten retentioiden käyttö on keskeinen osa ortodonttista hoitoa estämään hampaiden siirtymistä takaisin alkuperäiseen asentoon. Potilaalla on kuitenkin vahva eettinen vakaumus, mikä rajoittaa perinteisten retentiomenetelmien käyttöä. Tämä asettaa erityisiä vaatimuksia pitkäaikaiselle seurannalle ja hoidon ylläpidolle.

### Arvio
Ilman retentiota hampaat pyrkivät palautumaan alkuperäiseen asemaansa, mikä voi johtaa relapsiin eli hampaiden siirtymiseen. Lisäksi kiinteän kojeen käyttö lisää plakin kertymistä ja ientulehduksen riskiä, mikä voi pahentaa parodontaalista tilannetta. Potilaan oma motivaatio ja sitoutuminen ovat ratkaisevassa asemassa.

### Suositus
Suosittelen harkitsemaan vaihtoehtoisia retentiomenetelmiä, kuten passiivisia levykkeitä tai retentiokalvoja, mikäli potilas hyväksyy ne. Hoidon seurannassa tulee käyttää säännöllisiä kontrollikäyntejä (esim. 3–6 kk välein), joissa arvioidaan purennan stabiilisuus ja mahdolliset muutokset. Potilasta tulee edelleen motivoida hyvään suuhygieniaan ja tarvittaessa ohjata tukipalveluihin.

## Training Details
- **Method:** LoRA fine-tuning (r=64, alpha=128, dropout=0.05) merged into standalone model
- **Learning Rate:** 0.0002, weight_decay=0.01
- **Epochs:** 4
- **No quantization**
- **Batch Size:** 16, grad_accumulation=2
- **Precision:** FP16 format for optimal performance and compatibility
- **Embedding Training:** Enabled for domain specialization
- **Target Modules:** q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Data:** 50,132 conversations covering a broad range of different scenarios
- **Context:** 2048 tokens (inherited from Ahma-3B-Instruct)
- **Hardware:** H100 GPU with Unsloth optimizations
- **Training Performance:** Final loss converged to 0.4283 after 5940 steps (epoch 3.997), with stable gradient norms (0.725) indicating healthy training dynamics. Loss curves showed smooth, consistent convergence without overfitting or instability. Full training metrics and loss curves available on [Tensorboard](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-lora/tensorboard).

## Limitations and Important Notes

**Critical Medical Disclaimers:**
- Research purposes only - never use for actual medical decisions
- Model may hallucinate medical facts, treatments, or drug interactions
- Outputs have not been clinically validated and may contain medical misinformation
- All outputs require independent professional verification before any clinical application
- No liability is assumed for any consequences of model use

**Technical Limitations:**
- Primarily trained for dentist-to-dentist consultations - concept explanations included but not the main focus
- May particularly hallucinate on out-of-scope topics (further training could address this)
- Further fine-tuning may be needed for specific use cases
- System prompt dependency - using the training prompt is highly recommended
- 2048 token context limit affects both training and inference
- No formal evaluation - quality assessment has been primarily subjective

**Bias and Fairness:**
- Training data consists of synthetic conversations which may contain inherent biases
- Model responses may reflect biases present in the GPT-4.1 generated training data
- Geographic and cultural biases toward Finnish dental practices and protocols
- Potential underrepresentation of certain patient demographics or clinical scenarios

## Related Models
- v3: [ducklingcodehouse/Finnish-DentalQA-v3](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v3)
- v2 LoRA: [ducklingcodehouse/Finnish-DentalQA-v2-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-lora)
- v1 LoRA: [ducklingcodehouse/Finnish-DentalQA-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-lora)
- v1 Merged: [ducklingcodehouse/Finnish-DentalQA-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-merged)
- Base model: [Finnish-NLP/Ahma-3B-Instruct](https://huggingface.co/Finnish-NLP/Ahma-3B-Instruct)

## Citation

If you use this model, please cite both this work and the base Ahma model:

```bibtex
@misc{finnish-dentalqa-v2-merged,
  author = {Saxén, Heikki},
  title = {Finnish-DentalQA-v2-merged: LoRA Fine-tuned Model Merged for Finnish Dental Medicine},
  year = {2025},
  month = {September},
  publisher = {Hugging Face},
  url = {https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-merged}
}

@misc{ahma-3b-instruct,
  author = {Tanskanen, Aapo and Toivanen, Rasmus},
  title = {Ahma-3B-Instruct},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/Finnish-NLP/Ahma-3B-Instruct}
}
```
