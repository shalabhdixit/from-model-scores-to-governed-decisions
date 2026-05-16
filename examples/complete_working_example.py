from governed_decisions.reporting import select_threshold, threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays


actual_labels, model_scores = sample_arrays()
report = threshold_evaluation_report(actual_labels, model_scores, max_manual_reviews=12)
selected = select_threshold(report, min_recall=0.70, min_precision=0.60, require_capacity=True)

print("Threshold evaluation report")
print(report[[
    "threshold",
    "precision",
    "recall",
    "f1",
    "false_positives",
    "false_negatives",
    "manual_reviews",
    "within_capacity",
    "business_value",
]].to_string(index=False))

print("\nSelected threshold")
print(selected[["threshold", "precision", "recall", "f1", "manual_reviews", "business_value"]])
