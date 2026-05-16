from governed_decisions.operating_curves import operating_curve_summary, operating_curve_table
from governed_decisions.sample_data import sample_arrays


def test_operating_curve_summary_contains_operating_metrics():
    y_true, y_score = sample_arrays()

    summary = operating_curve_summary(y_true, y_score, operating_threshold=0.55)

    assert summary["operating_threshold"] == 0.55
    assert 0 <= summary["roc_auc"] <= 1
    assert 0 <= summary["average_precision"] <= 1
    assert 0 <= summary["operating_precision"] <= 1
    assert 0 <= summary["operating_recall"] <= 1


def test_operating_curve_table_is_stakeholder_readable():
    y_true, y_score = sample_arrays()

    table = operating_curve_table(y_true, y_score, operating_threshold=0.55)

    assert {"metric_view", "value", "interpretation"}.issubset(table.columns)
    assert len(table) == 5
