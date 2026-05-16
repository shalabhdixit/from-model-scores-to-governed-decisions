from governed_decisions.reporting import threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays


def test_report_adds_capacity_columns():
    actual_labels, model_scores = sample_arrays()
    report = threshold_evaluation_report(actual_labels, model_scores, max_manual_reviews=12)
    selected_row = report.loc[report["threshold"] == 0.55].iloc[0]
    assert selected_row["manual_reviews"] == 12
    assert bool(selected_row["within_capacity"]) is True
