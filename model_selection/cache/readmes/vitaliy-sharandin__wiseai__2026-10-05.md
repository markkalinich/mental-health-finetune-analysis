---

language: 
  - en

tags:
  - text-generation
  - mental-health
  - psychology
  - llm

datasets:
  - vitaliy-sharandin/depression-instruct

metrics:
  - BLEU
  - ROUGE

license: apache-2.0

model-index:
  - name: WisAI
    results:
      - task:
          name: Text Generation
          type: text-generation
        dataset:
          name: depression-instruct
          type: vitaliy-sharandin/depression-instruct
        metrics:
           - name: BLEU
             type: bleu
             value: 0.30
           - name: ROUGE
             type: rouge
             value: 0.45
           - name: F1
             type: f1
             value: 0.36

---

# Become wiser with WisAI

This is a wise AI model trained on philosophical and psychological data. It is intended to answer mental health questions and give some deep advice.