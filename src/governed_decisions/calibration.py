from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.calibration import calibration_curve


def calibration_summary(actual_labels, model_scores, n_bins: int = 5) -> pd.DataFrame:
    actual_array = np.asarray(actual_labels, dtype=int)
    score_array = np.asarray(model_scores, dtype=float)
    observed_rate, mean_predicted_probability = calibration_curve(
        actual_array,
        score_array,
        n_bins=n_bins,
        strategy="uniform",
    )
    return pd.DataFrame({
        "mean_predicted_probability": mean_predicted_probability,
        "observed_positive_rate": observed_rate,
        "calibration_gap": observed_rate - mean_predicted_probability,
    })


def score_distribution(model_scores, n_bins: int = 5) -> pd.DataFrame:
    score_array = np.asarray(model_scores, dtype=float)
    bins = np.linspace(0, 1, n_bins + 1)
    labels = [f"{bins[index]:.1f}-{bins[index + 1]:.1f}" for index in range(n_bins)]
    bands = pd.Series(pd.cut(score_array, bins=bins, labels=labels, include_lowest=True))
    return bands.value_counts(sort=False).rename_axis("score_band").reset_index(name="record_count")


def expected_calibration_error(actual_labels, model_scores, n_bins: int = 5) -> float:
    actual_array = np.asarray(actual_labels, dtype=int)
    score_array = np.asarray(model_scores, dtype=float)
    bins = np.linspace(0, 1, n_bins + 1)
    bin_ids = np.digitize(score_array, bins[1:-1], right=True)
    total = len(score_array)
    error = 0.0

    for bin_id in range(n_bins):
        mask = bin_ids == bin_id
        if not mask.any():
            continue
        bin_confidence = score_array[mask].mean()
        bin_accuracy = actual_array[mask].mean()
        error += (mask.sum() / total) * abs(bin_accuracy - bin_confidence)

    return float(error)
