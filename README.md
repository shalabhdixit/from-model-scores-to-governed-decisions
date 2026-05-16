# From Model Scores to Governed Decisions

Executable Python companion repo for the article series **From Model Scores to Governed Decisions**.

This repository turns the article examples into a runnable codebase for binary classification threshold tuning, business-impact evaluation, capacity-aware decisioning, segment thresholds, and production-style decision logging.

## Article Series

| Series Item | Title |
| --- | --- |
| Series name | From Model Scores to Governed Decisions |
| Part 1 | Threshold Tuning in Python: Turning Model Scores Into Business Decisions |
| Part 2 | Enterprise AI Governance: Turning Thresholds Into Governed Decision Policies |

## What This Repository Covers

- Binary classification threshold tuning
- Confusion matrix, precision, recall, F1, accuracy, and ROC-AUC evaluation
- Threshold sweeps across candidate operating points
- Business value modeling for true positives, false positives, false negatives, and true negatives
- Manual review capacity guardrails
- Guardrail-based threshold selection
- Default threshold versus selected threshold comparison
- Segment-specific threshold policies
- Production decision logging with model and threshold versions
- Mermaid architecture diagrams for enterprise decision governance

## Prerequisites

- Python 3.10 or later
- `pip`
- Optional but recommended: virtual environment support through `venv`, Conda, or similar

## Setup

From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e .[dev]
```

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .[dev]
```

## Run The Complete Example

```bash
python examples/complete_working_example.py
```

The script prints a complete threshold evaluation report and selected operating threshold using metric, business-value, and capacity guardrails.

## Run Individual Examples

```bash
python examples/01_sample_validation_data.py
python examples/02_apply_threshold.py
python examples/03_evaluate_baseline_threshold.py
python examples/04_threshold_sweep.py
python examples/05_business_value_ranking.py
python examples/06_capacity_safe_thresholds.py
python examples/07_compare_candidate_thresholds.py
python examples/08_visualize_tradeoffs.py
python examples/09_reusable_threshold_report.py
python examples/10_select_threshold_with_guardrails.py
python examples/11_compare_default_vs_selected.py
python examples/12_segment_specific_thresholds.py
python examples/13_production_decision_log.py
```

The visualization example writes charts into `outputs/`.

## Run Tests

```bash
pytest
```

## Main Modules

| Module | Purpose |
| --- | --- |
| `governed_decisions.sample_data` | Provides sample labels, scores, segments, and validation data loading |
| `governed_decisions.thresholding` | Converts probability scores into predicted labels |
| `governed_decisions.metrics` | Evaluates threshold-level model behavior |
| `governed_decisions.business_value` | Translates classification outcomes into business value |
| `governed_decisions.capacity` | Adds manual-review workload and capacity checks |
| `governed_decisions.reporting` | Builds reusable threshold reports and selects thresholds with guardrails |
| `governed_decisions.segment_thresholds` | Applies segment-aware decision thresholds |
| `governed_decisions.decision_logging` | Creates auditable production decision records |
| `governed_decisions.visualization` | Generates threshold tradeoff and business-value charts |

## Data Contract

The sample data uses a minimal validation contract:

| Column | Meaning |
| --- | --- |
| `actual` | Observed binary outcome, where `1` is the positive class |
| `score` | Model probability score for the positive class |
| `segment` | Optional segment used for segment-specific threshold examples |

Production validation tables should preserve equivalent fields, even if the source names differ, such as `actual_label` and `predicted_probability`.

## Governance Notes

The code in Part 1 is executable. The Part 2 concepts are represented as Mermaid diagrams and documentation because governance architecture should be implemented through the enterprise platform, policy registry, model registry, monitoring stack, approval workflow, and audit system used by the organization.

In production, thresholds should be:

- Versioned
- Approved by named owners
- Logged with model version and threshold version
- Monitored for drift, backlog, SLA pressure, override rate, and realized value
- Recalibrated or rolled back through controlled release processes

## Repository Layout

```text
from-model-scores-to-governed-decisions/
  data/          sample validation data
  src/           reusable Python package
  examples/      article-aligned runnable scripts
  tests/         pytest test suite
  docs/          article companion documentation
  assets/        Mermaid diagram sources
```
