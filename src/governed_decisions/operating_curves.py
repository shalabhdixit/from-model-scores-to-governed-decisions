from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, precision_recall_curve, precision_score, recall_score, roc_auc_score, roc_curve

from governed_decisions.thresholding import apply_threshold


def operating_curve_summary(actual_labels, model_scores, operating_threshold: float = 0.55) -> dict[str, float]:
    actual_array = np.asarray(actual_labels, dtype=int)
    score_array = np.asarray(model_scores, dtype=float)
    predictions = apply_threshold(score_array, operating_threshold)
    false_positive_rate, true_positive_rate, _ = roc_curve(actual_array, score_array)
    precision_values, recall_values, _ = precision_recall_curve(actual_array, score_array)

    negatives = actual_array == 0
    selected_false_positive_rate = float(((predictions == 1) & negatives).sum() / negatives.sum())

    return {
        "roc_auc": float(roc_auc_score(actual_array, score_array)),
        "average_precision": float(average_precision_score(actual_array, score_array)),
        "operating_threshold": float(operating_threshold),
        "operating_precision": float(precision_score(actual_array, predictions, zero_division=0)),
        "operating_recall": float(recall_score(actual_array, predictions, zero_division=0)),
        "operating_false_positive_rate": selected_false_positive_rate,
        "roc_points": int(len(false_positive_rate)),
        "precision_recall_points": int(len(precision_values)),
        "max_recall_on_pr_curve": float(recall_values.max()),
    }


def operating_curve_table(actual_labels, model_scores, operating_threshold: float = 0.55) -> pd.DataFrame:
    summary = operating_curve_summary(actual_labels, model_scores, operating_threshold=operating_threshold)
    return pd.DataFrame([
        {"metric_view": "ROC-AUC", "value": summary["roc_auc"], "interpretation": "Ranking quality across thresholds"},
        {"metric_view": "Average precision", "value": summary["average_precision"], "interpretation": "Positive workload quality across recall levels"},
        {"metric_view": "Operating precision", "value": summary["operating_precision"], "interpretation": "Quality of cases routed for action"},
        {"metric_view": "Operating recall", "value": summary["operating_recall"], "interpretation": "Share of positive cases caught at the selected threshold"},
        {"metric_view": "Operating false positive rate", "value": summary["operating_false_positive_rate"], "interpretation": "Negative cases unnecessarily routed for action"},
    ])
