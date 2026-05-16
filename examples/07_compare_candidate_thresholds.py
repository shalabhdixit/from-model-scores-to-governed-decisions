from governed_decisions.reporting import threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays


actual_labels, model_scores = sample_arrays()
report = threshold_evaluation_report(actual_labels, model_scores, max_manual_reviews=12)
comparison_columns = [
    "threshold",
    "accuracy",
    "precision",
    "recall",
    "f1",
    "false_positives",
    "false_negatives",
    "manual_reviews",
    "within_capacity",
    "business_value",
]
print(report[comparison_columns].to_string(index=False))
