import numpy as np
import pandas as pd

from governed_decisions.metrics import evaluate_threshold
from governed_decisions.sample_data import sample_arrays


actual_labels, model_scores = sample_arrays()
thresholds = np.round(np.arange(0.10, 0.91, 0.05), 2)
results = pd.DataFrame([evaluate_threshold(actual_labels, model_scores, threshold) for threshold in thresholds])
metric_columns = [
    "threshold",
    "accuracy",
    "precision",
    "recall",
    "f1",
    "true_positives",
    "false_positives",
    "false_negatives",
    "predicted_positive_rate",
]
print(results[metric_columns].to_string(index=False))
