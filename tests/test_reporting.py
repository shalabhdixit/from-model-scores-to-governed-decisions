from governed_decisions.reporting import select_threshold, threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays


def test_select_threshold_respects_guardrails():
    actual_labels, model_scores = sample_arrays()
    report = threshold_evaluation_report(actual_labels, model_scores, max_manual_reviews=12)
    selected = select_threshold(report, min_recall=0.70, min_precision=0.60, require_capacity=True)
    assert selected["threshold"] == 0.55
    assert selected["manual_reviews"] <= 12
