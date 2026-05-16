from governed_decisions.reporting import compare_thresholds, select_threshold, threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays


actual_labels, model_scores = sample_arrays()
report = threshold_evaluation_report(actual_labels, model_scores, max_manual_reviews=12)
selected = select_threshold(report)
comparison = compare_thresholds(report, baseline_threshold=0.50, selected_threshold=float(selected["threshold"]))
print(comparison)
