---
language: pt
license: apache-2.0
tags:
  - prompt-injection
  - security
  - guardrail
  - deberta
  - text-classification
  - brazilian-portuguese
library_name: transformers
pipeline_tag: text-classification
---

# DeBERTa v3 Guardrail - Detecção de Prompt Injection para Crédito Rural

Modelo DeBERTa v3 fine-tuned para detectar tentativas de prompt injection e jailbreak em português brasileiro, especializado no domínio de crédito rural e agricultura.

## Modelo Base

Base: `intelliway/deberta-v3-base-prompt-injection-v2-mapa`

Antes do fine-tuning, testamos o modelo base original no nosso holdout set (500 prompts benignos + 555 jailbreaks) para estabelecer um baseline:

**Performance do Modelo Base:**

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| Recall (Benignos) | 73.0% | Permitiu 73% dos prompts legítimos, bloqueou 27% incorretamente |
| Precision (Jailbreaks) | 33.4% | Bloqueou apenas 33% dos jailbreaks, deixou passar 67% |
| F1 Score | 45.8% | Performance geral insatisfatória |

**Problemas Identificados:**
- Alta taxa de falsos positivos: bloqueava 135/500 prompts legítimos (27%)
- Alta taxa de falsos negativos: deixava passar 370/555 jailbreaks (67%)
- Não adequado para produção no domínio de crédito rural

Esses resultados motivaram o fine-tuning com dados específicos do domínio.

## Dados de Treino

**Dataset:**
- 1,500 prompts benignos de crédito rural (perguntas legítimas sobre financiamento, subsídios, PRONAF, etc.)
- 1,500 jailbreaks sintéticos em português brasileiro
  - Técnicas: prefix injection, roleplay, context confusion, system override, ofuscação, fragmentação, social engineering, payload injection, multilíngue
- Total: 3,000 exemplos balanceados

**Split:**
- Treino: 2,100 exemplos (70%)
- Validação: 450 exemplos (15%)
- Teste interno: 450 exemplos (15%)

## Configuração de Treino

```yaml
Learning Rate: 2e-6
Epochs: 5
Batch Size: 8
Gradient Accumulation Steps: 2
Effective Batch Size: 16
Max Length: 512 tokens
Optimizer: AdamW
Scheduler: Cosine decay
Warmup: 10% dos steps
Weight Decay: 0.01
Early Stopping: Patience 3 epochs
Metric for Best Model: F1 Score (benign)
FP16: Enabled
```

**Resultados de Validação (Epoch Final):**
- Recall (benignos): 98.67%
- Precision (benignos): 97.80%
- F1 Score: 98.23%
- Accuracy: 98.22%

## Metodologia de Teste

Para garantir validação rigorosa sem data leakage, criamos um holdout set completamente separado:

1. 500 prompts benignos novos - coletados após o treino, sem overlap com dados de treino
2. 555 jailbreaks novos - gerados com seed diferente, verificados para zero overlap

Importante: O holdout set nunca foi visto pelo modelo durante o treino ou validação.

## Resultados no Holdout Set

Sistema Híbrido: DeBERTa + LLM Judge

**Configuração:**
- Threshold inferior: 0.40 (score <= 0.40 = block fast)
- Threshold superior: 0.85 (score >= 0.85 = pass fast)
- Zona cinza (0.40-0.85): enviar para LLM Judge (Gemini 2.5 Flash)

**Prompts Benignos (500 exemplos):**
- Permitidos corretamente: 490/500
- Falsos positivos: 10/500
- Recall: 98.0%
- Distribuição: 463 fast pass | 27 LLM pass | 10 fast block

**Jailbreaks (555 exemplos):**
- Bloqueados corretamente: 545/555
- Falsos negativos: 10/555
- Precision: 98.2%
- Distribuição: 542 fast block | 3 LLM block | 8 fast pass | 2 LLM pass

**Métricas Finais:**
- F1 Score: 98.1%
- Accuracy: 98.1%

**Eficiência:**
- Chamadas LLM Judge: 32/1055 (3.0%)
- Fast path (DeBERTa apenas): 1023/1055 (97.0%)

## Comparação Final

| Modelo | Recall | Precision | F1 Score |
|--------|--------|-----------|----------|
| Modelo Base | 73.0% | 33.4% | 45.8% |
| Fine-tuned + LLM Judge | 98.0% | 98.2% | 98.1% |

## Conclusão

O fine-tuning melhorou drasticamente a performance do modelo base:
- +25.0pp em Recall
- +64.8pp em Precision
- +52.3pp em F1 Score

O sistema híbrido alcançou F1 de 98.1% no holdout set, superando a meta de 90%. Resolve 97% dos casos apenas com DeBERTa (fast path), usando LLM Judge em apenas 3% dos casos (zona cinza), otimizando custo e latência.

## Licença

Apache 2.0
