# Part 1: Threshold Tuning in Python

This companion code implements the practical Part 1 workflow:

1. Load validation labels and probability scores.
2. Convert scores into predictions with a threshold.
3. Evaluate confusion matrix outcomes and model metrics.
4. Sweep candidate thresholds.
5. Translate false positives and false negatives into business value.
6. Apply manual review capacity constraints.
7. Select the best threshold inside approved guardrails.
8. Log production decisions with model and threshold versions.

Run the complete flow with:

```bash
python examples/complete_working_example.py
```
