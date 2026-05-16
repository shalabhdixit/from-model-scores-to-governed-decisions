from governed_decisions.metrics import evaluate_threshold
from governed_decisions.sample_data import sample_arrays


def test_evaluate_threshold_returns_expected_baseline_counts():
    actual_labels, model_scores = sample_arrays()
    metrics = evaluate_threshold(actual_labels, model_scores, threshold=0.50)
    assert metrics["true_positives"] == 12
    assert metrics["false_positives"] == 1
    assert metrics["true_negatives"] == 15
    assert metrics["false_negatives"] == 2
    assert round(metrics["roc_auc"], 3) == 0.964
