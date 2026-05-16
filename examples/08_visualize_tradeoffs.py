from pathlib import Path

from governed_decisions.reporting import select_threshold, threshold_evaluation_report
from governed_decisions.sample_data import sample_arrays
from governed_decisions.visualization import plot_business_value, plot_metric_tradeoffs


actual_labels, model_scores = sample_arrays()
report = threshold_evaluation_report(actual_labels, model_scores, max_manual_reviews=12)
selected = select_threshold(report)
output_dir = Path("outputs")
metric_path = plot_metric_tradeoffs(report, output_dir / "metric-tradeoffs.png")
business_path = plot_business_value(report, output_dir / "business-value.png", selected_threshold=selected["threshold"])
print(f"Created {metric_path}")
print(f"Created {business_path}")
