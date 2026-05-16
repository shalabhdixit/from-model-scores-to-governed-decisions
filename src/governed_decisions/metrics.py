from __future__ import annotations

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score

from governed_decisions.thresholding import apply_threshold


def evaluate_threshold(actual_labels, model_scores, threshold: float) -> dict[str, float]:
    actual_array = np.asarray(actual_labels, dtype=int)
    score_array = np.asarray(model_scores, dtype=float)
    predicted_labels = apply_threshold(score_array, threshold)
    true_negatives, false_positives, false_negatives, true_positives = confusion_matrix(
        actual_array,
        predicted_labels,
        labels=[0, 1],
    ).ravel()

    return {
        "threshold": float(threshold),
        "true_positives": int(true_positives),
        "false_positives": int(false_positives),
        "true_negatives": int(true_negatives),
        "false_negatives": int(false_negatives),
        "accuracy": float(accuracy_score(actual_array, predicted_labels)),
        "precision": float(precision_score(actual_array, predicted_labels, zero_division=0)),
        "recall": float(recall_score(actual_array, predicted_labels, zero_division=0)),
        "f1": float(f1_score(actual_array, predicted_labels, zero_division=0)),
        "predicted_positive_rate": float(predicted_labels.mean()),
        "roc_auc": float(roc_auc_score(actual_array, score_array)),
    }
