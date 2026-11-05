---
library_name: transformers
tags:
- transformers
- unsloth
- gemma3_text
- gemma
- finnish
- medical
- dental
- healthcare
- research-only
license: apache-2.0
language:
- fi
base_model: Finnish-NLP/Ahma-2-4B-Instruct
---

# Finnish-DentalQA-v3

**Finnish-language conversational AI assistant specialized for dental medicine.** This is a fine-tuned large language model (LLM) that generates structured text responses to dental consultation queries, designed to simulate professional dentist-to-dentist consultations with clinical reasoning and recommendations.

**RESEARCH USE ONLY - NOT FOR MEDICAL DECISIONS**

- **Developed by:** [Heikki Saxén](https://fi.linkedin.com/in/heikkisaxen) / [Duckling Codehouse Oy](https://www.linkedin.com/company/duckling-codehouse-oy/) ([ducklingcodehouse](https://huggingface.co/ducklingcodehouse))
- **Supported by:** [Entteri Professional Software Oy](https://www.entteri.com/) (makers of AssisDent dental PMS)
- **License:** apache-2.0
- **Base Model:** [Finnish-NLP/Ahma-2-4B-Instruct](https://huggingface.co/Finnish-NLP/Ahma-2-4B-Instruct) - Special thanks to Aapo Tanskanen and Rasmus Toivanen for creating this excellent Finnish LLM
- **Context Length:** Up to 128K input tokens, 8K output tokens (inherited from Ahma-2 base model)
- **Release Date:** January 7, 2026

Full fine-tuned model for Finnish dental medicine consultations between healthcare professionals. Trained on 50,132 synthetic dental conversations (approximately 80% expert clinical cases, 20% concept explanations) covering a broad range of different scenarios. Generated using pipeline with GPT-4.1.

**Version 3 Improvements:** This v3 release upgrades to the new Ahma-2-4B-Instruct base model, a significantly more capable 4B parameter Finnish LLM. The new base model features improved Finnish language understanding and generation quality through continued pretraining, supervised fine-tuning, and direct preference optimization. Training method changed from LoRA to full fine-tuning for maximum quality. Same proven dataset as v2.

**⚠️ Precision Requirement:** This model must be loaded in BF16 (`torch.bfloat16`). Ahma-2 is based on Gemma architecture which requires BF16 precision.

**Research Focus:** This model demonstrates domain-specific fine-tuning with accessible computational resources. The goal is to explore how specialized models can be trained and deployed on consumer hardware (including personal GPUs) rather than requiring high-end infrastructure.

**System Prompt Recommendation:** This model was trained with a specific system prompt. For best results, we recommend using the same prompt format shown in the examples below. While the system prompt can be modified, a 4B parameter model has limited ability to adapt to nuanced prompt changes — it will react to modifications, but don't expect the same prompt-following flexibility as larger models. Significant deviations from the training prompt may lead to inconsistent behavior.

**⚠️ Multi-Turn System Prompt Note:** Ahma-2 is based on Gemma architecture, which has **no native system role** — only `user` and `model`. When you pass `role: "system"`, the chat template silently prepends it to the first user message. This means:
- The model treats system instructions as regular user text
- In multi-turn conversations, the system prompt gets buried deeper in the context and its effect fades
- The model may start ignoring instructions or behaving inconsistently in longer chats

**Recommended fix for multi-turn use:** Prepend the system prompt to **every** user message, not just the first one. This keeps instructions in the strongest attention position regardless of conversation length. See the [Multi-Turn Example](#multi-turn-example) below.

**Response Format:** The model is trained to structure all clinical responses in three sections: "### Tausta" (Background), "### Arvio" (Assessment), "### Suositus" (Recommendation).

**Context Limit:** Supports up to 128K input tokens and 8K output tokens for inference (training used 2048 token sequences).

This model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's Transformers library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

## Model Comparison

| Version | Base Model | Parameters | Training Method | Dataset | Notes |
|---------|-----------|------------|-----------------|---------|-------|
| **v3** | Ahma-2-4B-Instruct | 4B | Full fine-tuning | 50,132 | Latest, highest quality |
| v2 | Ahma-3B-Instruct | 3B | LoRA | 50,132 | Enhanced dataset, available as LoRA and merged |
| v1 | Ahma-3B-Instruct | 3B | LoRA | 30,908 | Original release, available as LoRA and merged |

**v3 (this model)**: Full fine-tuned on Ahma-2-4B-Instruct, highest quality

**v2 LoRA Version**: [ducklingcodehouse/Finnish-DentalQA-v2-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-lora) - Enhanced training (50,132 samples), separate adapter files, requires base model

**v2 Merged Version**: [ducklingcodehouse/Finnish-DentalQA-v2-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-merged) - Same as v2 LoRA but merged into standalone model

**v1 LoRA Version**: [ducklingcodehouse/Finnish-DentalQA-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-lora) - Original training dataset (30,908 samples), separate adapter files

**v1 Merged Version**: [ducklingcodehouse/Finnish-DentalQA-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-merged) - Original training dataset, merged into standalone model

## Installation

```bash
pip install transformers torch accelerate
```

## Loading the Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "ducklingcodehouse/Finnish-DentalQA-v3",
    torch_dtype=torch.bfloat16,  # Required: BF16 for Ahma-2
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("ducklingcodehouse/Finnish-DentalQA-v3")
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

# Recommended settings (model supports up to 128K input / 8K output context)
with torch.no_grad():
    outputs = model.generate(
        inputs,
        max_new_tokens=800,
        temperature=0.1,
        do_sample=True,
        top_p=0.9,
        repetition_penalty=1.2
    )

response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)
print(response)

# Expected example response:
# ### Tausta
# Potilas on iäkäs, monisairas ja polyfarmasian vuoksi haavoittuvassa asemassa. Hampaattomuus
# ja proteesin käyttö yhdistettynä kuivaan suuhun lisäävät riskejä kuten sieni-infektioihin
# ja limakalvo-ongelmiin. Nielemisvaikeudet ja alentunut syljeneritys korostavat aspiraatioriskin
# hallinnan tarvetta. Antikoagulanttihoito (rivaroksabaani) tulee huomioida kaikissa
# invasiivisissa toimenpiteissä. Kotihoidon rooli on keskeinen päivittäisen suuhygienian
# toteutumisessa.
#
# ### Arvio
# Kliinisesti merkittäviä löydöksiä ovat kuivuminen, fissuroitunut kieli ja proteesistomatiitti.
# Korkea kariesriski liittyy sekä vähentyneeseen sylkeen että mahdolliseen heikentyneeseen
# omahoitoon. Parodontaalisairauksien riski kasvaa jäljellä olevien hampaiden määrän
# myötä. Muistisairaudet rajoittavat yhteistyökykyä ja edellyttävät yksinkertaisia
# ohjeita kotihoidolle. Käypä hoito -suositusten mukaan lyhennetyn hammaskaaren malli
# voi olla riittävä toiminnallisesti.
#
# ### Suositus
# Prioriteettina on kivuttoman ja infektiovapaan suun ylläpito: tehostettu mekaaninen
# puhdistus pehmeällä harjalla kahdesti päivässä, fluorilakkaus vastaanotolla neljännesvuosittain
# sekä klooriheksidiinigeeli paikallisesti riskialueille. Proteesi tulisi poistaa yöksi
# ja puhdistaa huolellisesti päivittäin. Syljenkorvikkeet tai keinotekoiset syljet
# voivat helpottaa oireita; ksylitolituotteet eivät ole ensisijaisia nielemishäiriön
# vuoksi. Säännölliset kontrollikäynnit suuhygienistin kanssa sekä tiivis yhteistyö
# kotihoidon henkilöstön kanssa ovat välttämättisiä. Tarvittaessa konsultoi erikoishammaslääkäriä
# mahdollisten sieni-infektiodiagnostiikan ja antifungaalisen hoidon osalta.
```

## Multi-Turn Example

In multi-turn conversations, prepend the system prompt to every user message to prevent instruction drift. Store only the raw user messages in history — prepend the system prompt fresh for each request.

```python
system_prompt = """Olet kokenut suomalainen hammaslääkäri. Vastaat ammattimaisesti kollegojesi
kysymyksiin käyttäen oikeaa hammaslääketieteellistä terminologiaa ja viittaat Käypä hoito
-suosituksiin kun relevanttia."""

separator = "\n---\nYllä olevat ohjeet ovat pysyviä. Kollegan viesti:\n"

# Conversation history — stores raw user messages (no system prompt)
history = []

def generate_response(user_message):
    # Prepend system prompt to this user message
    augmented_message = system_prompt + separator + user_message

    # Build messages for the model: history + current augmented message
    messages = history.copy()
    messages.append({"role": "user", "content": augmented_message})

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_new_tokens=800,
            temperature=0.1,
            do_sample=True,
            top_p=0.9,
            repetition_penalty=1.2
        )

    response = tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True)

    # Store raw user message (not augmented) and response in history
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": response})

    return response

# Turn 1
print(generate_response("Mitä pitäisi huomioida viisaudenhampaan poistossa?"))

# Turn 2 — system prompt is still in the strongest attention position
print(generate_response("Entä jos potilas käyttää verenohennuslääkitystä?"))
```

The key insight: by prepending system instructions to every user message, they always appear right before the model's generation point — the highest-attention position in the context. Without this, the system prompt would be at the very beginning of a growing conversation and gradually lose influence.

## Example

**User:** 27-vuotias mies, jolla on voimakas kipu ja turvotus alaleuan oikealla puolella. Viisaudenhammas 48 on puoliksi puhkeamassa, ympärillä runsasta ienturvotusta ja märkäkertymä. Potilaalla on kuumetta 38,3°C ja suun avausrajoitus 22 mm. Mitä ensihoitoa suosittelet terveyskeskuksessa?

**Assistant:**
### Tausta
Potilas esittää tyypillisiä akuutin perikoroniitin oireita: paikallinen turvotus, märkäkertymä sekä yleisoireet kuten kuume ja trismus (avausrajoitus). Puoliksi puhjenneen alaviisaudenhampaan ympäristöön kehittynyt infektio voi levitä nopeasti pehmytkudoksiin tai aiheuttaa syvempiä komplikaatioita. Yleistilan heikkeneminen näkyy tässä tapauksessa selvästi kohonneena lämpötilana (>38 °C) sekä rajoittuneena suun avaamisena (<30 mm), mikä lisää riskiä vakavammille infektioille.

### Arvio
Kliinisesti kyseessä on vaikea akuutti perikoroniitti, jossa systeemiset oireet ovat jo ilmeisiä. Märkäkertymän koko ja potilaan yleisvointi edellyttävät välitöntä toimenpidettä infektion leviämisen estämiseksi. Suun avauksen rajoitus viittaa mahdolliseen lihasjäykkyyteen tai alkavaan flegmonaaliseen prosessiin submandibulaarialueella. Tilanne vaatii ripeää arviota mahdollisesta sairaalahoitoon ohjaamisesta.

### Suositus
Ensihoitona tulee tehdä huolellinen mekaaninen debridementti eli irrottaa tulehtunut limakalvo hampaan kruunun alta steriilein instrumentein. Mikrobiologisen viljelyn kannalta otetaan bakteerinäyte ennen antibioottihoidon aloittamista. Aloitetaan empiirinen mikrobilääkehoito esimerkiksi amoksisilliini + metronidatsoli; penisilliiniallergiselle klindamysiini. Kipulääkitys toteutetaan parasetamolilla ja/tai ibuprofeenilla annosteluohjeiden mukaisesti. Tarvittaessa konsultoidaan erikoissairaanhoitoa jatkohoidosta tilanteen mukaan.

**Follow-up:** Potilas palaa seuraavana päivänä. Kuume on noussut 39,2 °C:een, suun avaus onnistuu enää 10 mm, alaleuan oikea puoli on selvästi turvonnut ja nieleminen on kivuliasta. Hengitys on hieman rohisevaa. Mitä toimenpiteitä suosittelet tässä vaiheessa?

**Assistant:**
### Tausta
Tilanne on edennyt nopeasti: kuume nousee entisestään yli 39 °C:n tasolle, suun avaus vähenee merkittävästi vain noin 10 mm:iin sekä kasvoalueen turvotus laajenee myös kaulan alueelle. Nieleminen muuttuu kivuliaaksi ja hengityksessä ilmenee rohinaa – tämä viittaa mahdolliseen syvemmälle levinneeseen infektioprosessiin kuten submandibulaariseen absessiin tai Ludwig'n anginaan.

### Arvio
Kyseessä on henkeä uhkaavan infektion alkuvaihe: hengitysteiden ahtauma voi johtua pehmytkudosödeemasta tai varhaisesta mediastiniitista. Trismus yhdessä laaja-alaisen turvotuksen kanssa nostaa riskin hengitystiekomplikaatioihin erityisesti nuorilla aikuisilla. Tällaisissa tapauksissa pelkkä polikliininen seuranta ei riitä vaan tarvitaan välitöntä kirurgista interventiota.

### Suositus
Suosittelen kiireellistä lähettämistä erikoissairaanhoidon yksikköön suukirurgiaan tai korva-, nenä- ja kurkkutauteihin päivystyksellisesti. Sairaalaolosuhteissa voidaan tehdä tarvittavat kuvantamistutkimukset (esim. KKTT), aloittaa suonensisäinen antibioottihoito sekä harkita kirurgista dreneerausta anestesiassa. Hengitysteiden turvaaminen priorisoidaan aina ennen muita toimenpiteitä.

## Training Details
- **Method:** Full fine-tuning (all parameters trained)
- **Base Model:** Finnish-NLP/Ahma-2-4B-Instruct (4B parameters)
- **Learning Rate:** 5e-5
- **Epochs:** 2 (checkpoint at 2968 steps)
- **Quantization:** None (full precision training)
- **Batch Size:** 8, gradient_accumulation=4 (effective batch size 32)
- **Precision:** BF16 (native precision for Ahma-2)
- **Data:** 50,132 conversations covering a broad range of different scenarios
- **Training Context:** 2048 tokens (model supports up to 128K input / 8K output)
- **Hardware:** H100 GPU with Unsloth optimizations
- **Training Performance:** Eval loss 0.426, train loss 0.331 at release checkpoint

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
- Training used 2048 token sequences; inference supports full 128K/8K context but quality on very long sequences is untested
- No formal evaluation - quality assessment has been primarily subjective

**Bias and Fairness:**
- Training data consists of synthetic conversations which may contain inherent biases
- Model responses may reflect biases present in the GPT-4.1 generated training data
- Geographic and cultural biases toward Finnish dental practices and protocols
- Potential underrepresentation of certain patient demographics or clinical scenarios

## Related Models
- v2 LoRA version: [ducklingcodehouse/Finnish-DentalQA-v2-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-lora)
- v2 Merged version: [ducklingcodehouse/Finnish-DentalQA-v2-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v2-merged)
- v1 LoRA version: [ducklingcodehouse/Finnish-DentalQA-lora](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-lora)
- v1 Merged version: [ducklingcodehouse/Finnish-DentalQA-merged](https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-merged)
- Base model: [Finnish-NLP/Ahma-2-4B-Instruct](https://huggingface.co/Finnish-NLP/Ahma-2-4B-Instruct)

## Citation

If you use this model, please cite both this work and the base Ahma model:

```bibtex
@misc{finnish-dentalqa-v3,
  author = {Saxén, Heikki},
  title = {Finnish-DentalQA-v3: Full Fine-tuned Model for Finnish Dental Medicine},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/ducklingcodehouse/Finnish-DentalQA-v3}
}

@misc{ahma-2-4b-instruct,
  author = {Tanskanen, Aapo and Toivanen, Rasmus},
  title = {Ahma-2-4B-Instruct},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/Finnish-NLP/Ahma-2-4B-Instruct}
}
```
