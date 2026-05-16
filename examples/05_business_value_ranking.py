from governed_decisions.reporting import threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays


actual_labels, model_scores = sample_arrays()
report = threshold_evaluation_report(actual_labels, model_scores)
print(report.sort_values("business_value", ascending=False)[[
    "threshold",
    "precision",
    "recall",
    "f1",
    "false_positives",
    "false_negatives",
    "business_value",
]].head(5).to_string(index=False))
