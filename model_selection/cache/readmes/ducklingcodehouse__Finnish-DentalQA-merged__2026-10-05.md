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

# Finnish-DentalQA-merged

**Note: Newer versions are available! See [Finnish-DentalQA-v3](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v3) (recommended, 4B parameters, full fine-tuning on Ahma-2) or [Finnish-DentalQA-v2](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-merged) (enhanced dataset).**

**Finnish-language conversational AI assistant specialized for dental medicine.** This is a fine-tuned large language model (LLM) that generates structured text responses to dental consultation queries, designed to simulate professional dentist-to-dentist consultations with clinical reasoning and recommendations.

**RESEARCH USE ONLY - NOT FOR MEDICAL DECISIONS**

- **Developed by:** [Heikki Saxén](https://fi.linkedin.com/in/heikkisaxen) / [Duckling Codehouse Oy](https://www.linkedin.com/company/duckling-codehouse-oy/) ([ducklingcodehouse](https://huggingface.co/ducklingcodehouse))
- **Supported by:** [Entteri Professional Software Oy](https://www.entteri.com/) (makers of AssisDent dental PMS)
- **License:** apache-2.0
- **Base Model:** Finnish-NLP/Ahma-3B-Instruct (by Aapo Tanskanen & Rasmus Toivanen)
- **Context Length:** 2048 tokens
- **Release Date:** August 20, 2025

LoRA fine-tuned model merged into standalone format for Finnish dental medicine consultations between healthcare professionals. Trained on 30,908 synthetic dental conversations (80% expert clinical cases, 20% concept explanations) covering a broad range of different scenarios. Generated using pipeline with GPT-4.1.

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
| v2 | Ahma-3B-Instruct | 3B | LoRA | 50,132 | Enhanced dataset, available as LoRA and merged |
| **v1** | Ahma-3B-Instruct | 3B | LoRA | 30,908 | Original release, available as LoRA and merged |

**v3 (recommended)**: [ducklingcodehouse/Finnish-DentalQA-v3](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v3) - Full fine-tuned on Ahma-2-4B-Instruct, highest quality

**v2 LoRA Version**: [ducklingcodehouse/Finnish-DentalQA-v2-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-lora) - Enhanced training (50,132 samples), separate adapter files, requires base model

**v2 Merged Version**: [ducklingcodehouse/Finnish-DentalQA-v2-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-merged) - Enhanced training (50,132 samples), merged into standalone model

**v1 LoRA Version**: [ducklingcodehouse/Finnish-DentalQA-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-lora) - Original dataset (30,908 samples), separate adapter files, requires base model

**v1 Merged Version (this model)**: Original dataset (30,908 samples), merged into standalone model

## Installation

```bash
pip install transformers torch accelerate
```

## Loading the Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "ducklingcodehouse/Finnish-DentalQA-merged",
    torch_dtype=torch.bfloat16,  # Use torch.bfloat16 or torch.float16 for older GPUs
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("ducklingcodehouse/Finnish-DentalQA-merged")
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

**User:** 27-vuotias mies, jolla on voimakas kipu ja turvotus alaleuan oikealla puolella. Viisaudenhammas 48 on puoliksi puhkeamassa, ympärillä runsasta ienturvotusta ja märkäkertymä. Potilaalla on kuumetta 38,3°C ja suun avausrajoitus 22 mm. Mitä ensihoitoa suosittelet terveyskeskuksessa?

**Assistant:**
### Tausta
Potilas esittäytyy tyypillisin akuutin perikoroniitin oirein: kuume, paikallinen turvotus sekä trismus (avausrajoitus 22 mm). Puoliksi puhjenneen viisaudenhampaan (48) ympärillä oleva runsas ienturvotus ja märkäkertymä viittaavat paikalliseen infektioon, joka voi levitä syvempiin kudoksiin. Suun avausrajoitus (trismus) lisää riskiä infektion leviämiselle esimerkiksi submandibulaaritilaan.

### Arvio
Kliininen kuva sopii akuuttiin perikoroniittiin komplisoituneena paikallisella absessilla tai flegmoonalla. Kuume ja yleisoireet täyttävät mikrobilääkehoidon aloituskriteerit Käypä hoito -suositusten mukaan. Trismus vaikeuttaa paikallista puhdistusta ja altistaa infektion leviämiselle. Märkäkertymän dreneeraus on ensisijaista, mutta myös antibioottihoito on tarpeen.

### Suositus
Aloita amoksisilliini 500 mg x 3 po ja metronidatsoli 500 mg x 2 po suun kautta 7 päivän ajan. Kipulääkitys parasetamolilla ja/tai tulehduskipulääkkeellä. Huuhtele suu klooriheksidiinillä 1–2 kertaa päivässä. Mikäli potilaan yleistila heikkenee tai ilmaantuu nielemisvaikeuksia/hengitystieoireita, päivystyslähete erikoissairaanhoitoon on aiheellinen. Seuraa tilannetta tiiviisti; mikäli avausrajoitus pahenee tai yleisvointi huononee, sairaalahoito voi olla tarpeen.

**Follow-up:** Potilas palaa seuraavana päivänä. Kuume on noussut 39,2 °C:een, suun avaus onnistuu enää 10 mm, alaleuan oikea puoli on selvästi turvonnut ja nieleminen on kivuliasta. Hengitys on hieman rohisevaa. Mitä toimenpiteitä suosittelet tässä vaiheessa?

**Assistant:**
### Tausta
Potilaan tila on selvästi pahentunut: kuume noussut 39,2 °C:een, suun avausrajoitus pahentunut (nyt vain 10 mm), oikean puolen turvotus lisääntynyt ja nieleminen vaikeutunut. Nämä löydökset viittaavat syvemmälle levinneeseen infektioprosessiin, mahdollisesti alkavaan flegmonaan tai abskessiin.

### Arvio
Kyseessä on vakava infektio, jossa on riski hengitysteiden kompromissille ja septiselle kehitykselle. Suun avauksen rajoittuminen alle 20 mm sekä nielemisvaikeus ovat merkkejä siitä, että infektio saattaa olla levinnyt syvempiin kaulan tiloihin. Märän dreenauksen onnistuminen on kriittistä, mutta trismuksen vuoksi tämä voi olla haastavaa.

### Suositus
Potilas tulee lähettää välittömästi päivystykseen sairaalatasolle suonensisäisen antibioottihoidon ja mahdollisen kirurgisen dreneerauksen arvioon. Hengitysteiden turvaaminen on ensisijainen prioriteetti – tarvittaessa anestesialääkärin arvio. Mikrobilääkehoitoa jatketaan sairaalassa suositusten mukaisesti. Seuranta tehostetussa valvonnassa on välttämätöntä komplikaatioiden varalta.

## Training Details
- **Method:** LoRA fine-tuning (r=64, alpha=128, dropout=0.05) merged into standalone model
- **Learning Rate:** 0.0002
- **Epochs:** 3
- **Effective Batch Size:** 64
- **Precision:** BF16 native format, automatically converts to FP16 when needed for hardware compatibility
- **Embedding Training:** Enabled for domain specialization
- **Target Modules:** q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Data:** 30,908 conversations covering a broad range of different scenarios
- **Context:** 2048 tokens (inherited from Ahma-3B-Instruct)
- **Hardware:** H100 GPU with Unsloth optimizations
- **Training Performance:** Loss curves showed steady convergence with final values well below 1.0, indicating successful learning without overfitting

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
- v2 Merged: [ducklingcodehouse/Finnish-DentalQA-v2-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-merged)
- v1 LoRA: [ducklingcodehouse/Finnish-DentalQA-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-lora)
- Base model: [Finnish-NLP/Ahma-3B-Instruct](https://huggingface.co/Finnish-NLP/Ahma-3B-Instruct)

## Citation

If you use this model, please cite both this work and the base Ahma model:

```bibtex
@misc{finnish-dentalqa-merged,
  author = {Saxén, Heikki},
  title = {Finnish-DentalQA-merged: LoRA Fine-tuned Model Merged for Finnish Dental Medicine},
  year = {2025},
  month = {August},
  publisher = {Hugging Face},
  url = {https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-merged}
}

@misc{ahma-3b-instruct,
  author = {Tanskanen, Aapo and Toivanen, Rasmus},
  title = {Ahma-3B-Instruct},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/Finnish-NLP/Ahma-3B-Instruct}
}
```
