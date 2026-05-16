from __future__ import annotations

import numpy as np


def apply_threshold(scores, threshold: float) -> np.ndarray:
    score_array = np.asarray(scores, dtype=float)
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    return (score_array >= threshold).astype(int)
