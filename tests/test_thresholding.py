import numpy as np
import pytest

from governed_decisions.thresholding import apply_threshold


def test_apply_threshold_converts_scores_to_labels():
    predictions = apply_threshold([0.20, 0.50, 0.80], threshold=0.50)
    assert np.array_equal(predictions, np.array([0, 1, 1]))


def test_apply_threshold_rejects_invalid_threshold():
    with pytest.raises(ValueError):
        apply_threshold([0.20], threshold=1.20)
