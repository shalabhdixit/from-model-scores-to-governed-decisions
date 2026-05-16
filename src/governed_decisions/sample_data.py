from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ACTUAL_LABELS = np.array([
    1, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 1, 1, 0, 1,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 1,
])

MODEL_SCORES = np.array([
    0.91, 0.12, 0.78, 0.44, 0.32, 0.08, 0.67, 0.21, 0.73, 0.55,
    0.18, 0.83, 0.27, 0.62, 0.49, 0.05, 0.88, 0.36, 0.41, 0.69,
    0.24, 0.15, 0.57, 0.29, 0.96, 0.47, 0.52, 0.34, 0.11, 0.76,
])

SEGMENTS = np.array([
    "high_value", "standard", "high_value", "standard", "standard",
    "standard", "high_value", "standard", "high_value", "standard",
    "standard", "high_value", "standard", "high_value", "standard",
    "standard", "high_value", "standard", "standard", "high_value",
    "standard", "standard", "high_value", "standard", "high_value",
    "standard", "high_value", "standard", "standard", "high_value",
])


def sample_arrays() -> tuple[np.ndarray, np.ndarray]:
    return ACTUAL_LABELS.copy(), MODEL_SCORES.copy()


def load_sample_validation_data() -> pd.DataFrame:
    return pd.DataFrame({"actual": ACTUAL_LABELS, "score": MODEL_SCORES, "segment": SEGMENTS})


def load_validation_data(path: str | Path) -> pd.DataFrame:
    validation_path = Path(path)
    if not validation_path.exists():
        raise FileNotFoundError(f"Validation data file not found: {validation_path}")
    data = pd.read_csv(validation_path)
    required_columns = {"actual", "score"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Validation data is missing required columns: {sorted(missing_columns)}")
    return data
