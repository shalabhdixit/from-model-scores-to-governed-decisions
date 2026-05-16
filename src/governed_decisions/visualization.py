from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


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
