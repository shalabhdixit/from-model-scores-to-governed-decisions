from __future__ import annotations

import numpy as np
import pandas as pd

from governed_decisions.business_value import DEFAULT_BUSINESS_VALUES, calculate_business_value
from governed_decisions.capacity import add_capacity_columns
from governed_decisions.metrics import evaluate_threshold


def threshold_evaluation_report(
    actual_labels,
    model_scores,
    thresholds=None,
    business_values: dict[str, float] | None = None,
    max_manual_reviews: int | None = None,
) -> pd.DataFrame:
    candidate_thresholds = thresholds if thresholds is not None else np.round(np.arange(0.10, 0.91, 0.05), 2)
    value_model = business_values or DEFAULT_BUSINESS_VALUES
    report = pd.DataFrame([
        evaluate_threshold(actual_labels, model_scores, float(threshold))
        for threshold in candidate_thresholds
    ])
    report["business_value"] = report.apply(calculate_business_value, axis=1, values=value_model)
    report = add_capacity_columns(report, max_manual_reviews=max_manual_reviews)
    return report.sort_values("threshold").reset_index(drop=True)


def select_threshold(
    report: pd.DataFrame,
    min_recall: float = 0.70,
    min_precision: float = 0.60,
    require_capacity: bool = True,
) -> pd.Series:
    candidate_report = report[(report["recall"] >= min_recall) & (report["precision"] >= min_precision)].copy()
    if require_capacity and "within_capacity" in candidate_report.columns:
        candidate_report = candidate_report[candidate_report["within_capacity"]]
    if candidate_report.empty:
        return report.sort_values("business_value", ascending=False).iloc[0]
    return candidate_report.sort_values("business_value", ascending=False).iloc[0]


def compare_thresholds(report: pd.DataFrame, baseline_threshold: float, selected_threshold: float) -> pd.DataFrame:
    baseline_row = report.loc[report["threshold"] == baseline_threshold].iloc[0]
    selected_row = report.loc[report["threshold"] == selected_threshold].iloc[0]
    comparison = pd.DataFrame([baseline_row, selected_row])[
        [
            "threshold",
            "precision",
            "recall",
            "f1",
            "false_positives",
            "false_negatives",
            "manual_reviews",
            "business_value",
        ]
    ]
    comparison.index = ["default_threshold", "selected_threshold"]
    return comparison
