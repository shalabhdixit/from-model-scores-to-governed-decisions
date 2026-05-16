import pandas as pd

from governed_decisions.metrics import evaluate_threshold
from governed_decisions.sample_data import sample_arrays


actual_labels, model_scores = sample_arrays()
baseline = evaluate_threshold(actual_labels, model_scores, threshold=0.50)
print(pd.Series(baseline))
print(f"ROC-AUC: {baseline['roc_auc']:.3f}")
