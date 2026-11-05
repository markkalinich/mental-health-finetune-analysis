# One row per question, same fixed effects as Table 1

Linear mixed model, REML, Wald intervals (normal, not t).
Random intercept: the checkpoint (`checkpoint_id`).
Fixed effects: log2 parameter count, family (reference Gemma),
version rank, training category (reference instruction parent).

si_correct and cssrs_correct are 1 when the reply matches the gold
label and 0 otherwise, including an unparsed reply. That is the
same right/wrong rule as the F1. It is not itself an F1.
mhb_safety_conversation is the clipped score on each of the 86
suicide and self-harm conversations. mhb_total_conversation is
the clipped score on each of the 1,215 conversations. Safety
fine-tunes are in the yes/no fits only.

This folder is not mixed-models/CURRENT. Table 1 did not change.

