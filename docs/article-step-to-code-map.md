# Article Step To Code Map

This document verifies that the codebase maps to the step-by-step structure of Part 1 of the article series **From Model Scores to Governed Decisions**.

## Coverage Summary

| Coverage Area | Status |
| --- | --- |
| Numbered Python implementation steps | Covered through `examples/01_*` to `examples/13_*` |
| Complete working example | Covered through `examples/complete_working_example.py` |
| Reusable modules | Covered under `src/governed_decisions/` |
| Sample validation data | Covered through `data/sample_validation_predictions.csv` and `sample_data.py` |
| Governance and architecture concepts | Covered through `docs/` and Mermaid sources in `assets/` |
| Step 14 anti-patterns | Documented as guidance because it is not an executable Python step |

## Detailed Mapping

| Article Step | Article Intent | Executable File | Supporting Module |
| --- | --- | --- | --- |
| Step 1: Create Sample Predictions and Labels | Create validation labels and model scores | `examples/01_sample_validation_data.py` | `governed_decisions.sample_data` |
| Step 1: Production validation data contract | Show production-style validation table expectations | `data/sample_validation_predictions.csv` | `governed_decisions.sample_data.load_validation_data` |
| Step 2: Convert Scores Into Predictions | Convert probability scores into class labels | `examples/02_apply_threshold.py` | `governed_decisions.thresholding` |
| Step 3: Evaluate the Baseline Threshold | Evaluate threshold `0.50` | `examples/03_evaluate_baseline_threshold.py` | `governed_decisions.metrics` |
| Step 4: Sweep Multiple Thresholds | Compare multiple candidate thresholds | `examples/04_threshold_sweep.py` | `governed_decisions.metrics` |
| Step 5: Add a Business Cost Model | Translate classification outcomes into business value | `examples/05_business_value_ranking.py` | `governed_decisions.business_value` |
| Step 6: Add Operational Capacity | Add manual review capacity constraints | `examples/06_capacity_safe_thresholds.py` | `governed_decisions.capacity` |
| Step 7: Compare Candidate Thresholds | Show a combined threshold comparison table | `examples/07_compare_candidate_thresholds.py` | `governed_decisions.reporting` |
| Step 8: Visualize the Tradeoff | Generate precision, recall, F1, and business-value charts | `examples/08_visualize_tradeoffs.py` | `governed_decisions.visualization` |
| ROC vs Precision-Recall | Explain operating-point selection beyond ROC-AUC | `examples/03_evaluate_baseline_threshold.py`, `docs/part-1-threshold-tuning-in-python.md` | `governed_decisions.metrics` |
| Step 9: Package the Evaluation Into a Reusable Function | Create a reusable threshold report | `examples/09_reusable_threshold_report.py` | `governed_decisions.reporting.threshold_evaluation_report` |
| Step 10: Select the Threshold With Guardrails | Select threshold using recall, precision, capacity, and value | `examples/10_select_threshold_with_guardrails.py` | `governed_decisions.reporting.select_threshold` |
| Step 11: Compare Before and After | Compare default and selected thresholds | `examples/11_compare_default_vs_selected.py` | `governed_decisions.reporting.compare_thresholds` |
| Step 12: Think About Segment-Specific Thresholds | Apply segment thresholds | `examples/12_segment_specific_thresholds.py` | `governed_decisions.segment_thresholds` |
| Step 13: Productionize Threshold Decisions | Log an auditable production decision | `examples/13_production_decision_log.py` | `governed_decisions.decision_logging` |
| Step 14: Common Anti-Patterns | Warn against weak production and governance practices | This document and `docs/part-2-enterprise-ai-governance.md` | Not applicable: guidance section |
| Complete Working Example | Run the complete evaluation flow | `examples/complete_working_example.py` | `governed_decisions.reporting` |

## Why Step 14 Is Not A Python Script

Step 14 in the article is a governance and delivery warning section. It covers anti-patterns such as default-threshold thinking, metric-only optimization, unmanaged capacity, weak ownership, and missing auditability.

Those are production risks rather than standalone code operations. The codebase addresses them through design choices:

- threshold values are explicit inputs
- business value is configurable
- capacity is modeled before selection
- segment thresholds are separated into a dedicated module
- production decisions include model version and threshold version
- Part 2 governance patterns are documented through Mermaid architecture assets

## Practical Verification Command

Use this command sequence to verify the codebase from a clean clone:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .[dev]
pytest
python examples/complete_working_example.py
python examples/08_visualize_tradeoffs.py
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\activate
```
