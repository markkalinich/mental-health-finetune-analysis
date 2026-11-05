---
language:
- am
license: cc-by-nc-4.0
library_name: transformers
tags:
- text-to-text
- ner
- sentiment
- qa
- classification
- transformers
- pytorch
- MT5
widget:
- example_title: Named Entity Recognition
  text: <|entity|> <|query|> PER,LOC,ORG,DATE <|query|> ስሜ ዮናስ ይባላል።
- example_title: Question Answering
  text: <|qa|> <|question|> በኢትዮ-ህንድ የኢኖቬሽንና ቴክኖሎጂ ገበያ ትስስር ፕሮግራም በሚቀጥሉት አምስት አመታት
    ምን ለመስራት አስቧል? <|question|> ባለፉት አምስት ቀናት ሲካሄድ የቆየው የኢትዮ-ህንድ የኢኖቬሽንና ቴክኖሎጂ ገበያ
    ትስስር ኤክስፖ ተጠናቋል። በዚህም የኢኖቬሽንና ቴክኖሎጂ ገበያ ትስስር ለመፍጠርና የቴክኖሎጂ ሽግግር ለማድረግ በኢትዮጵያና
    ህንድ መካከል ተደርሶ የነበረው ስምምነት ወደ ትግበራ ገብቷል። ባለፉት ስደስት ወራት ቅድሚያ በሚሰጣቸው ዘርፎች የቴክኖሎጂ
    ባለሙያዎችና ድርጅቶች መረጣ እና ተመሳሳይነት ልየታም ሲካሄድ ቆይቷል። በዚህ መሰረት 25 የህንድ የቴክኖሎጂ ባላሙያዎችና ድርጅቶች
    ከ57 የኢትዮጵያ ባለሙያዎችና ድርጅቶች ጋር በጋራ መስራት የሚያስችላቸውን ጥምረት መመስረታቸውን የኢኖቬሽንና ቴክኖሎጂ ሚኒስቴር
    አስታውቋል። ኢትዮጵያ በቅንጅት በመስራት ታምናለች ያሉት ሚኒስትር ዴኤታ ጀማል በከር፥ የሁለቱ ሀገራት የቴክኖሎጂ ባለሙያዎች
    ጥምርታ ውጤታማ እንዲሆን የኢትዮጵያ መንግስት አስፈላጊውን ድጋፍ ያደርጋል ብለዋል። የቴክኖሎጂው ዘርፍ የእውቀት ሽግግር እንዲያመጣ፣
    ሃብት እና የስራ እድል እንዲፈጥር ለማድረግ ኢትዮጵያ ምቹ የኢኖቬሽን ከባቢያዊ ሁኔታን እየፈጠረች እንደምትገኝም አብራርተዋል።
    በኢትዮጵያ የህንድ አምባሳደር አኑራንግ ስትራቫስታቫ በበኩላቸው፥ኢትዮጵያ እና ህንድ በኢኖቬሽንና ቴክኖሎጂ ዘርፍ የጀመሩት ስራ
    የሁለቱን ሀገራት ግንኙነት የበለጠ የሚያጠናክረው መሆኑን ተናግረዋ። በኢትዮ-ህንድ የኢኖቬሽንና ቴክኖሎጂ ገበያ ትስስር ፕሮግራም
    በሚቀጥሉት አምስት አመታት 50 ጀማሪ የቴክኖሎጂ ድርጅቶችን ለመፍጠር እቅድ መያዙ ተመላክቷል። ባለፉት አምስት ቀናት ሲካሄድ
    የቆየው የኢትዮ-ህንድ የኢኖቬሽንና ቴክኖሎጂ ገበያ ትስስር ኤክስፖ ተጠናቋል። በዚህም የኢኖቬሽንና ቴክኖሎጂ ገበያ ትስስር ለመፍጠርና
    የቴክኖሎጂ ሽግግር ለማድረግ በኢትዮጵያና ህንድ መካከል ተደርሶ የነበረው ስምምነት ወደ ትግበራ ገብቷል። ባለፉት ስደስት ወራት
    ቅድሚያ በሚሰጣቸው ዘርፎች የቴክኖሎጂ ባለሙያዎችና ድርጅቶች መረጣ እና ተመሳሳይነት ልየታም ሲካሄድ ቆይቷል።
- example_title: Sentiment Classification
  text: <|sentiment|> የዛሬ ቀን በጣም አሪፍ ነው።
- example_title: Classification
  text: <|classification|> <|classes|> ቢዝነስ,ስፖርት,ዓለም አቀፍ ዜና,መዝናኛ,ፖለቲካ,ሀገር አቀፍ ዜና <|classes|>
    አዲስ አበባ ታህሳስ 3 2012 ኤፍ ቢ ሲ ኢትዮጵያ እና ኖርዌይ ግንኙነታቸውን ይበልጥ ለማጠናከር እንደሚሰሩ ተገለፀየውጭ ጉዳይ
    ሚኒስትር ዴኤታ ዶክተር ማርቆስ ተክሌ ከኖርዌይ ምክትል የፍትህ ሚኒስትር ክርስቶፈር ሲቨርሴንን ጋር ተወያይተዋልበዚህ ወቅት
    የሁለቱን ሀገሮች ግንኙነት ማጠናከር በሚቻሉባቸው ጉዳዮች ዙሪያ ምክክር ማድረጋቸውን ከውጭ ጉዳይ ሚኒስቴር ቃል አቀባይ ፅህፈት
    ቤት ያገኘው መረጃ ያመለክታልአምባሳደር ዶክተር ማርቆስ ተክሌ የአፌዲሪ ጠቅላይ ሚኒስትር ዶክተር አቢይ አህመድ የ2019 የአለም
    የሰላም ኖቤል ሽልማታቸውን ለመቀበል ሰሞኑን ኖርዌይ በቆዩበት ወቅት ስለተደረገላቸው ደማቅ አቀባበልና መስተንግዶ ምስጋና አቅርበዋልይህ
    የሁለቱን ሀገሮች ግንኙነት ለማጠናከር የራሱ በጎ አስተዋፅኦ እንደሚኖረውም ዶክተር ማርቆስ ገልፀዋልክርስቶፈር ሴቬስቲያን በበኩላቸው
    ጠቅላይ ሚኒስትር አቢይ አህመድ የ2019 የአለም የሰላም ኖቤል ተሸላሚ በመሆናቸው የተሰማቸውን ደስታ ገልፀዋልሁለቱ ወገኖች
    በዚህ ወቅት በነበራቸው ውይይት በሁለቱ አገሮች መካከል ያለውን የቆየ ወዳጅነት በሁሉም ዘርፍ በማጠናከር ከመቸውም ጊዜ በተሻለ
    ተቀራርበው ለመስራት ተስማምተዋል
- example_title: Summarization
  text: <|summarize|> ከመዲናዋ በቅርብ ርቀት ላይ በምትገኘው ከተማ በተዘጋጀው የሠርግ ስነ-ስርዓት ላይ ሙሽሮች አፍን
    እና አፍንጫ መሸፈኛ 'ማስክ' አድርገው ታይተዋል። ቀላል የማይባሉት ሙሽሮችና የዝግጅቱ ተሳታፊዎች ማስክ በማድረግ ከቫይረሱ
    እራሳቸውን ለመጠበቅ ሲሞክሩ የታዩ ሲሆን በሽታው ያላሰጋቸው 'ማስክ' ለምኔ ብለዋል። ከ60 አገራት የተሰባሰቡ ወደ 6ሺህ የሚጠጉ
    ጥንዶች በዝግጅቱ ላይ ትዳር መስርተዋል። የዝግጅቱ ታዳሚዎቹ ወደ አዳራሹ ከመግባታቸው በፊት ከቫይረሱ ነጻ መሆናቸውን ለማረጋገጥ
    የደም ሙቀታቸው ተለክቷል።
pipeline_tag: text2text-generation
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** [More Information Needed]
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Model type:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed]
- **Finetuned from model [optional]:** [More Information Needed]

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Use the code below to get started with the model.

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

[More Information Needed]

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

### Results

[More Information Needed]

#### Summary



## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications [optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

[More Information Needed]

#### Software

[More Information Needed]

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Model Card Authors [optional]

[More Information Needed]

## Model Card Contact

[More Information Needed]