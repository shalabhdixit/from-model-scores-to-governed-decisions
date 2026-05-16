# From Model Scores to Governed Decisions

Production-minded Python companion code for the article series **From Model Scores to Governed Decisions**.

This repository turns the article walkthrough into an executable, testable, reusable codebase for binary classification threshold tuning, probability calibration review, business-impact evaluation, ROC/precision-recall operating-point analysis, capacity-aware decisioning, segment thresholds, stakeholder communication, anti-pattern checks, and auditable production decision logging.

The main idea is simple:

```text
Model score -> Threshold policy -> Business decision -> Audit evidence -> Governance feedback
```

A model estimates probability. The threshold decides behavior. This repo shows how to evaluate that threshold as an operating policy, not just as a metric-tuning parameter.

## Article Series

| Series Item | Title |
| --- | --- |
| Series name | From Model Scores to Governed Decisions |
| Part 1 | Threshold Tuning in Python: Turning Model Scores Into Business Decisions |
| Part 2 | Enterprise AI Governance: Turning Thresholds Into Governed Decision Policies |

## What You Can Do With This Repo

| Capability | What It Proves |
| --- | --- |
| Apply binary classification thresholds | Scores do not become decisions until an operating boundary is applied |
| Map use cases and threshold-fit situations | Threshold tuning is useful only when the business problem really is a decision-boundary problem |
| Evaluate precision, recall, F1, accuracy, ROC-AUC, and confusion matrix counts | Model behavior must be visible at each candidate threshold |
| Review calibration and score distribution | Thresholds should not be approved until probability reliability is understood |
| Sweep thresholds from `0.10` to `0.90` | The default `0.50` threshold is only one possible operating point |
| Add business value assumptions | False positives and false negatives usually do not cost the same |
| Add manual review capacity | A statistically attractive threshold can still break operations |
| Compare ROC and precision-recall views | ROC-AUC can hide operating workload, especially when positive cases are scarce |
| Select thresholds with guardrails | Production thresholds should satisfy metric, value, and capacity constraints |
| Compare default and selected thresholds | Stakeholders need to see what changed and why it matters |
| Apply segment-specific thresholds | Context can improve decisions, but it introduces fairness and governance duties |
| Log production decisions | Every decision should preserve score, threshold, model version, policy version, and action |
| Generate anti-pattern and stakeholder artifacts | Decision owners need clear warnings and plain-language rationale, not only metrics |
| Use Mermaid architecture diagrams | Part 2 governance patterns are captured as decision architecture assets |

## Repository Architecture

```text
from-model-scores-to-governed-decisions/
  README.md
  pyproject.toml
  requirements.txt
  data/
    sample_validation_predictions.csv
  src/
    governed_decisions/
      sample_data.py
      article_concepts.py
      thresholding.py
      metrics.py
      calibration.py
      operating_curves.py
      business_value.py
      capacity.py
      reporting.py
      segment_thresholds.py
      decision_logging.py
      anti_patterns.py
      visualization.py
  examples/
    00_article_concept_map.py
    01_sample_validation_data.py
    02_apply_threshold.py
    03_evaluate_baseline_threshold.py
    03b_probability_calibration_review.py
    04_threshold_sweep.py
    05_business_value_ranking.py
    06_capacity_safe_thresholds.py
    07_compare_candidate_thresholds.py
    08_visualize_tradeoffs.py
    08b_roc_vs_precision_recall.py
    09_reusable_threshold_report.py
    10_select_threshold_with_guardrails.py
    11_compare_default_vs_selected.py
    12_segment_specific_thresholds.py
    13_production_decision_log.py
    14_common_anti_patterns.py
    15_stakeholder_explanation.py
    complete_working_example.py
  tests/
    test_anti_patterns_and_concepts.py
    test_business_value.py
    test_calibration.py
    test_capacity.py
    test_decision_logging.py
    test_metrics.py
    test_operating_curves.py
    test_reporting.py
    test_thresholding.py
  docs/
    article-step-to-code-map.md
    part-1-threshold-tuning-in-python.md
    part-2-enterprise-ai-governance.md
  assets/
    part-1-practical-threshold-evaluation-flow.mmd
    part-1-threshold-operating-zones.mmd
    part-2-enterprise-decision-architecture.mmd
    part-2-policy-engine-control-plane.mmd
    part-2-threshold-lifecycle-governance.mmd
    part-2-threshold-drift-monitoring-loop.mmd
    part-2-human-override-feedback-loop.mmd
    part-2-governance-ownership-model.mmd
```

## Article Step To Code Map

Every executable Python step from Part 1 is represented in `examples/`. The conceptual sections are also represented through runnable examples, reusable modules, or explicit docs so the repo covers the article, not just the numbered snippets.

| Article Section | Repository File | Purpose |
| --- | --- | --- |
| Binary classification business context | `examples/00_article_concept_map.py`, `governed_decisions.article_concepts` | Maps use cases, score meaning, and threshold-driven actions |
| When to use and when not to use threshold tuning | `examples/00_article_concept_map.py`, `governed_decisions.article_concepts` | Separates decision-boundary problems from ranking, discovery, or calibration problems |
| Step 1: Create Sample Predictions and Labels | `examples/01_sample_validation_data.py` | Loads the sample validation data and prints the first records |
| Step 1: Production validation data contract | `data/sample_validation_predictions.csv`, `governed_decisions.sample_data` | Provides the validation table shape used by the examples |
| Step 2: Convert Scores Into Predictions | `examples/02_apply_threshold.py`, `governed_decisions.thresholding` | Applies a threshold to probability scores |
| Step 3: Evaluate the Baseline Threshold | `examples/03_evaluate_baseline_threshold.py`, `governed_decisions.metrics` | Computes baseline metrics and ROC-AUC at `0.50` |
| Calibration before threshold approval | `examples/03b_probability_calibration_review.py`, `governed_decisions.calibration` | Reviews reliability curve data, score bands, and expected calibration error |
| Step 4: Sweep Multiple Thresholds | `examples/04_threshold_sweep.py` | Evaluates thresholds from `0.10` to `0.90` |
| Step 5: Add a Business Cost Model | `examples/05_business_value_ranking.py`, `governed_decisions.business_value` | Ranks thresholds by business value |
| Step 6: Add Operational Capacity | `examples/06_capacity_safe_thresholds.py`, `governed_decisions.capacity` | Adds manual review workload and capacity checks |
| Step 7: Compare Candidate Thresholds | `examples/07_compare_candidate_thresholds.py` | Prints the combined metric, capacity, and business-value table |
| Step 8: Visualize the Tradeoff | `examples/08_visualize_tradeoffs.py`, `governed_decisions.visualization` | Generates metric and business-value charts in `outputs/` |
| ROC vs Precision-Recall discussion | `examples/08b_roc_vs_precision_recall.py`, `governed_decisions.operating_curves` | Compares ranking quality with positive-workload quality at the operating threshold |
| Step 9: Package the Evaluation Into a Reusable Function | `examples/09_reusable_threshold_report.py`, `governed_decisions.reporting` | Builds the reusable threshold evaluation report |
| Step 10: Select the Threshold With Guardrails | `examples/10_select_threshold_with_guardrails.py` | Selects the best threshold inside recall, precision, and capacity constraints |
| Step 11: Compare Before and After | `examples/11_compare_default_vs_selected.py` | Compares default `0.50` with the selected threshold |
| Step 12: Think About Segment-Specific Thresholds | `examples/12_segment_specific_thresholds.py`, `governed_decisions.segment_thresholds` | Applies segment-specific thresholds |
| Step 13: Productionize Threshold Decisions | `examples/13_production_decision_log.py`, `governed_decisions.decision_logging` | Creates an auditable production decision record |
| Step 14: Common Anti-Patterns | `examples/14_common_anti_patterns.py`, `governed_decisions.anti_patterns` | Produces a structured anti-pattern table with better practices |
| Explaining the selected threshold to stakeholders | `examples/15_stakeholder_explanation.py` | Converts the threshold comparison into plain-language business rationale |
| Complete Working Example | `examples/complete_working_example.py` | Runs the end-to-end threshold evaluation and selection flow |

## Prerequisites

| Requirement | Recommended Version | Why It Is Needed |
| --- | --- | --- |
| Python | `3.10+` | Uses modern typing and current data science package versions |
| pip | Latest stable | Installs the local package and dependencies |
| virtual environment | `venv`, Conda, or equivalent | Keeps dependencies isolated from system Python |
| Git | Optional for local use | Useful for cloning, branching, and contribution workflows |

## Setup On Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e .[dev]
```

## Setup On macOS Or Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .[dev]
```

## Quick Start

Run the complete article workflow:

```bash
python examples/complete_working_example.py
```

Expected selected threshold:

```text
threshold         0.55
precision     0.916667
recall        0.785714
f1            0.846154
manual_reviews      12
business_value   2420.0
```

Run the test suite:

```bash
pytest
```

Generate the charts:

```bash
python examples/08_visualize_tradeoffs.py
```

Generated files:

```text
outputs/metric-tradeoffs.png
outputs/business-value.png
```

Run the additional article concept checks:

```bash
python examples/00_article_concept_map.py
python examples/03b_probability_calibration_review.py
python examples/08b_roc_vs_precision_recall.py
python examples/14_common_anti_patterns.py
python examples/15_stakeholder_explanation.py
```

## Run The Examples Step By Step

| Command | What It Demonstrates |
| --- | --- |
| `python examples/00_article_concept_map.py` | Business contexts, when-to-use guidance, and when threshold tuning is not enough |
| `python examples/01_sample_validation_data.py` | Sample validation labels and model scores |
| `python examples/02_apply_threshold.py` | Score-to-label conversion at threshold `0.50` |
| `python examples/03_evaluate_baseline_threshold.py` | Baseline threshold metrics and ROC-AUC |
| `python examples/03b_probability_calibration_review.py` | Calibration curve table, score distribution, expected calibration error, and calibration chart |
| `python examples/04_threshold_sweep.py` | Candidate threshold sweep |
| `python examples/05_business_value_ranking.py` | Threshold ranking by business value |
| `python examples/06_capacity_safe_thresholds.py` | Thresholds that fit manual review capacity |
| `python examples/07_compare_candidate_thresholds.py` | Combined metric, capacity, and value comparison |
| `python examples/08_visualize_tradeoffs.py` | Precision, recall, F1, and business-value charts |
| `python examples/08b_roc_vs_precision_recall.py` | ROC and precision-recall operating-point view |
| `python examples/09_reusable_threshold_report.py` | Reusable threshold report function |
| `python examples/10_select_threshold_with_guardrails.py` | Guardrail-based threshold selection |
| `python examples/11_compare_default_vs_selected.py` | Before-and-after threshold comparison |
| `python examples/12_segment_specific_thresholds.py` | Segment-aware thresholding |
| `python examples/13_production_decision_log.py` | Production decision record with model and threshold versions |
| `python examples/14_common_anti_patterns.py` | Anti-pattern checklist from the article |
| `python examples/15_stakeholder_explanation.py` | Plain-language threshold recommendation for decision owners |

## Main Modules

| Module | Responsibility | Typical User |
| --- | --- | --- |
| `governed_decisions.sample_data` | Provides the sample validation data and CSV loader | Data scientists, analysts |
| `governed_decisions.article_concepts` | Maps use cases and threshold-fit situations from the article | Product, analytics, risk, data science |
| `governed_decisions.thresholding` | Converts probability scores into predicted labels | Data scientists, ML engineers |
| `governed_decisions.metrics` | Evaluates confusion matrix counts and model metrics | Data scientists, model validators |
| `governed_decisions.calibration` | Reviews score reliability, score distribution, and calibration error | Model validators, data scientists |
| `governed_decisions.operating_curves` | Compares ROC and precision-recall operating-point behavior | Data scientists, risk, operations |
| `governed_decisions.business_value` | Converts errors and correct decisions into value assumptions | Analytics, finance, product, risk |
| `governed_decisions.capacity` | Adds manual-review workload and capacity flags | Operations, ML platform teams |
| `governed_decisions.reporting` | Builds reusable threshold reports and selects policy thresholds | ML engineers, model governance teams |
| `governed_decisions.segment_thresholds` | Applies threshold policies by segment | Risk, product, compliance, data science |
| `governed_decisions.decision_logging` | Creates auditable decision records | ML engineering, platform, audit |
| `governed_decisions.anti_patterns` | Produces article-aligned anti-pattern and better-practice guidance | Governance, model risk, delivery leads |
| `governed_decisions.visualization` | Produces stakeholder-ready threshold charts | Data science, analytics leadership |

## Data Contract

The included sample file is `data/sample_validation_predictions.csv`.

| Column | Type | Meaning | Production Equivalent |
| --- | --- | --- | --- |
| `actual` | integer | Observed binary outcome, where `1` is the positive class | `actual_label`, `observed_outcome`, `target` |
| `score` | float | Model probability score for the positive class | `predicted_probability`, `risk_score`, `model_score` |
| `segment` | string | Optional operating segment for contextual thresholds | customer tier, product, geography, risk band, channel |

Production validation data should preserve this logical contract even when column names differ. The model team should be able to identify the observed outcome and the probability score used for threshold evaluation.

## Business Value Model

The default value assumptions are intentionally simple:

| Outcome | Default Value | Interpretation |
| --- | --- | --- |
| True positive | `+500` | Correctly caught a valuable positive case |
| False positive | `-80` | Unnecessary review, friction, or intervention |
| False negative | `-1000` | Missed risk, missed opportunity, or delayed action |
| True negative | `0` | Correctly avoided action |

These values are examples. In a real enterprise implementation, finance, risk, operations, compliance, and product teams should define the value model together.

## Capacity Guardrails

The examples use `max_manual_reviews=12` to show why operating capacity matters.

The selected threshold is not simply the threshold with the highest raw business value. It is the threshold that satisfies:

- minimum recall
- minimum precision
- manual review capacity
- strongest business value inside those constraints

That is the practical difference between metric optimization and decision policy validation.

## Production Decision Logging

The production decision example records:

| Field | Why It Matters |
| --- | --- |
| `record_id` | Connects the decision to the source business event |
| `model_score` | Preserves the probability score used at decision time |
| `threshold` | Preserves the operating boundary |
| `predicted_label` | Shows which class path was selected |
| `action` | Shows the business route taken |
| `model_version` | Supports model lineage and auditability |
| `threshold_version` | Supports policy lineage and rollback |
| `decision_time_utc` | Supports investigation, monitoring, and replay |

This is the minimum pattern needed to answer the production question: why did the system make this decision at that time?

## Governance And Architecture Assets

Part 2 is represented through documentation and Mermaid diagram sources in `assets/`.

| Diagram | Purpose |
| --- | --- |
| `part-1-practical-threshold-evaluation-flow.mmd` | Practical threshold evaluation workflow |
| `part-1-threshold-operating-zones.mmd` | How the threshold separates class `0` and class `1` routes |
| `part-2-enterprise-decision-architecture.mmd` | Enterprise score-to-decision architecture |
| `part-2-policy-engine-control-plane.mmd` | Decision policy engine as an AI control plane |
| `part-2-threshold-lifecycle-governance.mmd` | Threshold proposal, validation, approval, deployment, monitoring, and rollback |
| `part-2-threshold-drift-monitoring-loop.mmd` | Monitoring and recalibration loop |
| `part-2-human-override-feedback-loop.mmd` | Human override governance and learning loop |
| `part-2-governance-ownership-model.mmd` | Shared ownership across evidence providers, approvers, and operating controls |

Render Mermaid diagrams with a Mermaid-compatible editor or CLI. Example:

```bash
npx -y @mermaid-js/mermaid-cli -i assets/part-2-enterprise-decision-architecture.mmd -o outputs/part-2-enterprise-decision-architecture.svg
```

## Enterprise Operating Model

In production, threshold policies should not be hardcoded into isolated scripts. They should become governed operating assets.

| Production Concern | Control Pattern |
| --- | --- |
| Ownership | Named product, risk, operations, and model owners |
| Approval | Decision record before high-impact threshold changes |
| Versioning | Threshold registry and model registry integration |
| Monitoring | Score drift, calibration gap, alert volume, backlog, SLA, override rate, realized value |
| Fairness | Segment-level false positive, false negative, approval, review, and escalation analysis |
| Rollback | Known prior threshold version and accountable rollback owner |
| Auditability | Decision logs with score, threshold, action, model version, policy version, and timestamp |

## Verification Status

The local validation used before publishing this repo:

```text
python -m pip install -e .[dev]  -> success
pytest                          -> 14 passed
python examples/complete_working_example.py -> success
python examples/08_visualize_tradeoffs.py   -> success
python examples/03b_probability_calibration_review.py -> success
python examples/08b_roc_vs_precision_recall.py        -> success
python examples/14_common_anti_patterns.py            -> success
python examples/15_stakeholder_explanation.py         -> success
```

## Recommended Learning Path

1. Read the article Part 1 to understand the practical workflow.
2. Run `examples/complete_working_example.py` to see the full threshold report.
3. Run `examples/00_article_concept_map.py` to connect the article's business framing to executable reference tables.
4. Run each numbered example to connect the code to the article steps.
5. Run `examples/03b_probability_calibration_review.py` and `examples/08b_roc_vs_precision_recall.py` to cover the validation concepts around the main threshold workflow.
6. Review `docs/article-step-to-code-map.md` to see exact coverage.
7. Review the Mermaid diagrams in `assets/` to connect the code to Part 2 governance architecture.
8. Adapt the business value assumptions and capacity limits to your own operating context.

## Important Production Notes

This repository is intentionally compact and educational, but the design points are production-oriented:

- Do not choose thresholds using one metric alone.
- Do not assume `0.50` is the right threshold.
- Do not deploy thresholds without capacity simulation.
- Do not use segment thresholds without fairness and explainability review.
- Do not hardcode high-impact thresholds without versioning and rollback.
- Do not treat model deployment as the same thing as decision governance.

Better enterprise AI systems are not created only by better models. They are created by better governed decisions.
