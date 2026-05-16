from governed_decisions import compare_thresholds, sample_arrays, threshold_evaluation_report


business_values = {
    "true_positive_value": 500,
    "false_positive_cost": -80,
    "false_negative_cost": -1000,
    "true_negative_value": 0,
}

y_true, y_score = sample_arrays()
report = threshold_evaluation_report(y_true, y_score, business_values=business_values, max_manual_reviews=12)
comparison = compare_thresholds(report, baseline_threshold=0.50, selected_threshold=0.55)
baseline = comparison.loc[comparison["threshold"] == 0.50].iloc[0]
selected = comparison.loc[comparison["threshold"] == 0.55].iloc[0]

print("Stakeholder explanation")
print(
    "We are recommending a 0.55 operating threshold instead of the default 0.50 because it preserves "
    f"recall at {selected['recall']:.2f}, improves precision from {baseline['precision']:.2f} to {selected['precision']:.2f}, "
    f"keeps manual reviews at {int(selected['manual_reviews'])}, and increases expected business value from "
    f"{baseline['business_value']:.0f} to {selected['business_value']:.0f}. This threshold should be governed as a "
    "business policy, not hidden as a model parameter."
)
