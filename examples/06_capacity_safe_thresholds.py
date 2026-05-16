from governed_decisions.reporting import threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays


actual_labels, model_scores = sample_arrays()
report = threshold_evaluation_report(actual_labels, model_scores, max_manual_reviews=12)
capacity_safe_report = report[report["within_capacity"]].copy()
print(capacity_safe_report.sort_values("business_value", ascending=False)[[
    "threshold",
    "manual_reviews",
    "precision",
    "recall",
    "false_positives",
    "false_negatives",
    "business_value",
]].head(5).to_string(index=False))
