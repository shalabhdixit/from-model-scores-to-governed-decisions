from governed_decisions.calibration import calibration_summary, expected_calibration_error, score_distribution
from governed_decisions.sample_data import sample_arrays


def test_calibration_summary_returns_expected_columns():
    y_true, y_score = sample_arrays()
    summary = calibration_summary(y_true, y_score, n_bins=5)

    assert list(summary.columns) == ["mean_predicted_probability", "observed_positive_rate", "calibration_gap"]
    assert not summary.empty


def test_score_distribution_counts_all_scores():
    _, y_score = sample_arrays()
    distribution = score_distribution(y_score, n_bins=5)

    assert distribution["record_count"].sum() == len(y_score)


def test_expected_calibration_error_is_bounded():
    y_true, y_score = sample_arrays()

    error = expected_calibration_error(y_true, y_score, n_bins=5)

    assert 0 <= error <= 1
