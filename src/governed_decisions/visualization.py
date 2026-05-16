from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.calibration import calibration_curve
from sklearn.metrics import average_precision_score, precision_recall_curve, precision_score, recall_score, roc_auc_score, roc_curve

from governed_decisions.thresholding import apply_threshold


def plot_metric_tradeoffs(report: pd.DataFrame, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(10, 6))
    axis.plot(report["threshold"], report["precision"], marker="o", label="Precision")
    axis.plot(report["threshold"], report["recall"], marker="o", label="Recall")
    axis.plot(report["threshold"], report["f1"], marker="o", label="F1")
    axis.set_xlabel("Threshold")
    axis.set_ylabel("Metric Value")
    axis.set_title("Threshold Tuning: Precision, Recall, and F1")
    axis.legend()
    axis.grid(True, alpha=0.3)
    figure.tight_layout()
    figure.savefig(path, dpi=160)
    plt.close(figure)
    return path


def plot_business_value(report: pd.DataFrame, output_path: str | Path, selected_threshold: float | None = None) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(10, 6))
    axis.plot(report["threshold"], report["business_value"], marker="o")
    if selected_threshold is not None:
        axis.axvline(selected_threshold, color="red", linestyle="--", label=f"Selected threshold {selected_threshold:.2f}")
        axis.legend()
    axis.set_xlabel("Threshold")
    axis.set_ylabel("Business Value")
    axis.set_title("Business Value by Threshold")
    axis.grid(True, alpha=0.3)
    figure.tight_layout()
    figure.savefig(path, dpi=160)
    plt.close(figure)
    return path


def plot_calibration_reliability(actual_labels, model_scores, output_path: str | Path, n_bins: int = 5) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    observed_rate, mean_predicted_probability = calibration_curve(actual_labels, model_scores, n_bins=n_bins, strategy="uniform")

    figure, axes = plt.subplots(1, 2, figsize=(15, 6.5))
    axes[0].plot([0, 1], [0, 1], color="#94a3b8", linestyle="--", linewidth=2, label="Perfect calibration")
    axes[0].plot(mean_predicted_probability, observed_rate, marker="o", linewidth=3, label="Observed reliability")
    axes[0].set_title("Calibration Curve")
    axes[0].set_xlabel("Mean predicted probability")
    axes[0].set_ylabel("Observed positive rate")
    axes[0].set_xlim(0, 1)
    axes[0].set_ylim(0, 1)
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    axes[1].hist(model_scores, bins=n_bins, range=(0, 1), color="#14b8a6", edgecolor="white")
    axes[1].set_title("Score Distribution by Probability Band")
    axes[1].set_xlabel("Score band")
    axes[1].set_ylabel("Validation records")
    axes[1].grid(True, axis="y", alpha=0.3)

    figure.suptitle("Probability Calibration: Trust Before Thresholding", fontsize=16, fontweight="bold")
    figure.tight_layout(rect=[0, 0.02, 1, 0.92])
    figure.savefig(path, dpi=160)
    plt.close(figure)
    return path


def plot_roc_precision_recall_operating_points(actual_labels, model_scores, output_path: str | Path, operating_threshold: float = 0.55) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    false_positive_rate, true_positive_rate, _ = roc_curve(actual_labels, model_scores)
    precision_values, recall_values, _ = precision_recall_curve(actual_labels, model_scores)
    predictions = apply_threshold(model_scores, operating_threshold)
    negative_count = (pd.Series(actual_labels) == 0).sum()
    operating_false_positive_rate = (((predictions == 1) & (pd.Series(actual_labels).to_numpy() == 0)).sum()) / negative_count
    operating_recall = recall_score(actual_labels, predictions)
    operating_precision = precision_score(actual_labels, predictions)

    figure, axes = plt.subplots(1, 2, figsize=(15, 6.8))
    axes[0].plot(false_positive_rate, true_positive_rate, color="#0a66c2", linewidth=3, label=f"ROC-AUC {roc_auc_score(actual_labels, model_scores):.3f}")
    axes[0].plot([0, 1], [0, 1], color="#94a3b8", linestyle="--", linewidth=2, label="Random baseline")
    axes[0].scatter([operating_false_positive_rate], [operating_recall], s=120, color="#ef4444", zorder=5, label=f"Operating point {operating_threshold:.2f}")
    axes[0].set_title("ROC Curve: Ranking Quality")
    axes[0].set_xlabel("False Positive Rate")
    axes[0].set_ylabel("True Positive Rate / Recall")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(loc="lower right")

    axes[1].plot(recall_values, precision_values, color="#14b8a6", linewidth=3, label=f"Average precision {average_precision_score(actual_labels, model_scores):.3f}")
    axes[1].scatter([operating_recall], [operating_precision], s=120, color="#ef4444", zorder=5, label=f"Operating point {operating_threshold:.2f}")
    axes[1].set_title("Precision-Recall Curve: Operating Burden")
    axes[1].set_xlabel("Recall")
    axes[1].set_ylabel("Precision")
    axes[1].set_ylim(0, 1.05)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(loc="lower left")

    figure.suptitle("ROC vs Precision-Recall: Selecting an Enterprise Operating Point", fontsize=16, fontweight="bold")
    figure.tight_layout(rect=[0, 0.02, 1, 0.92])
    figure.savefig(path, dpi=160)
    plt.close(figure)
    return path
