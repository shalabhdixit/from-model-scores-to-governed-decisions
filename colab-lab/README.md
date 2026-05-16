# Google Colab Lab

This folder contains a complete Google Colab notebook for the article series **From Model Scores to Governed Decisions**.

## Notebook

| File | Purpose |
| --- | --- |
| `from_model_scores_to_governed_decisions_colab_lab.ipynb` | End-to-end executable lab covering threshold tuning, business value, capacity guardrails, segment thresholds, decision logging, and governance checks |

## Open In Colab

After this repository is available on GitHub, open the notebook with this URL:

```text
https://colab.research.google.com/github/shalabhdixit/from-model-scores-to-governed-decisions/blob/main/colab-lab/from_model_scores_to_governed_decisions_colab_lab.ipynb
```

## What The Lab Covers

1. Repository setup inside Colab.
2. Package installation with `pip install -e .[dev]`.
3. Validation data loading.
4. Baseline threshold application.
5. Baseline metric evaluation.
6. Threshold sweep.
7. Business value modeling.
8. Operational capacity guardrails.
9. Guardrail-based threshold selection.
10. Default versus selected threshold comparison.
11. Visualization of metric and business-value tradeoffs.
12. Segment-specific thresholds.
13. Production decision logging.
14. Governance checklist for production use.

## Expected Result

The lab should select threshold `0.55` with:

| Metric | Expected Value |
| --- | --- |
| Precision | `0.916667` |
| Recall | `0.785714` |
| F1 | `0.846154` |
| Manual reviews | `12` |
| Business value | `2420.0` |

## Local Validation

The notebook JSON can be validated locally with:

```bash
python -m json.tool colab-lab/from_model_scores_to_governed_decisions_colab_lab.ipynb
```

The repo code used by the notebook can be validated with:

```bash
pytest
python examples/complete_working_example.py
python examples/08_visualize_tradeoffs.py
```
