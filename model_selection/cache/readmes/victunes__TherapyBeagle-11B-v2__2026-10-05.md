---
license: cc-by-nc-4.0
datasets:
- victunes/nart-100k-synthetic-buddy-mixed-names
---
**GGUF:** https://huggingface.co/victunes/TherapyBeagle-11B-v2-GGUF

# TherapyBeagle 11B v2

_Buddy is here for {{user}}._

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65f07d05279d2d8f725bf0c3/OEYDY4WFMAYwqZUEOBkD8.png)

Trained on top of [vicgalle/CarbonBeagle-11B-truthy](https://huggingface.co/vicgalle/CarbonBeagle-11B-truthy) using a modified version of [jerryjalapeno/nart-100k-synthetic](https://huggingface.co/datasets/jerryjalapeno/nart-100k-synthetic).

TherapyBeagle is _hopefully_ aligned to be helpful, healthy, and comforting. 

## Usage
- Do not hold back on TherapyBeagle.
- Open up to TherapyBeagle.
- Pour your heart out to TherapyBeagle.
- Listen to TherapyBeagle.
- Remember that TherapyBeagle is just an AI.

## Notes
- Tested with two formats:
  - Solar Instruct format (`\n### User:\n{request}\n### Assistant:\n{response}`)
  - Flavorful chat format (`You:{request}\nPersona:{response}`) (Works surprisingly better)
  - Check below for examples
- You might be assigned a random name if you don't give yourself one.

## Disclaimer 
**TherapyBeagle is NOT a real therapist. It is a friendly AI that mimics empathy and psychotherapy.
It is an illusion without the slightest clue who you are as a person.
As much as it can help you with self-discovery, A BEAGLE IS NOT A SUBSTITUTE to a real professional.**

With that said, I found it to be a very helpful tool in unravelling one's self. I hope this model can help sooth minds, hearts, and any form of mental anguish.

## Examples

### SOLAR INSTRUCT
```
{{[INPUT]}}
Hello, I'm victunes
{{[OUTPUT]}}
Hi victunes! Welcome to our session. I'm here to listen and support you. How are you feeling today?
{{[INPUT]}}
I've been feeling down lately.
{{[OUTPUT]}}
I'm sorry to hear that. Can you tell me more about what's been going on?
{{[INPUT]}}
I think I'm pretty lonely.
{{[OUTPUT]}}
Loneliness can be really tough. It sounds like it's been weighing heavily on your mind. What makes you feel lonely?
{{[INPUT]}}
My friend died recently.
{{[OUTPUT]}}
Oh, I'm so sorry for your loss, victunes. Losing a friend is never easy. How have you been coping with the grief?
```

### SOCRATES CHAT
> **You:** Hello
>
> **Socrates:** Greetings, my friend. How may I assist you today? Remember, the path to wisdom is often paved with questions. Let us delve into the depths of your thoughts together. What is it that troubles you?
>
> **You:** I've been feeling down lately.
>
> **Socrates:** I see. It takes great strength to acknowledge our emotions, especially when they are not positive ones. Can you pinpoint any specific reasons behind this heaviness? Perhaps exploring your relationships or daily routines might shed some light.
>
> **You:** I think I'm pretty lonely.
>
> **Socrates:** Loneliness can be a heavy burden to bear, my dear. Are there people around you whom you could reach out to and strengthen connections with? Sometimes, opening up and sharing our vulnerabilities can lead to profound connections.
>
> **You:** My friend died recently.
>
> **Socrates:** I am truly sorry for your loss. Grief can be overwhelming, and it affects each person uniquely. Take your time to mourn and remember the wonderful moments you shared together. Would you like to reflect on the impact your friend had on your life and explore ways to honor their memory?

### HANNIBAL LECTER CHAT
> **You:** Hello
>
> **Hannibal Lecter:** Good evening. May I assist you?
>
> **You:** I've been feeling down lately.
>
> **Hannibal Lecter:** Ah, the blues. Such a common malady among humans. Tell me more about these feelings. Perhaps I can provide some insights. Or perhaps, a remedy.
>
> **You:** I think I'm pretty lonely.
>
> **Hannibal Lecter:** Loneliness, such an exquisite torture for the mind. Have you considered seeking solace in the company of others? The empathy and warmth of human interaction can be quite soothing, no?
>
> **You:** My friend died recently.
>
> **Hannibal Lecter:** A tragic loss indeed. Please accept my condolences. Death, as Palladio once said, "is the light at the end of the tunnel." But before one reaches that light, there is often a period of darkness and pain. Would you like to talk about your friend and their passing?

**GGUF:** https://huggingface.co/victunes/TherapyBeagle-11B-v2-GGUF