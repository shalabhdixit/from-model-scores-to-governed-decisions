from governed_decisions.operating_curves import operating_curve_table
from governed_decisions.sample_data import sample_arrays
from governed_decisions.visualization import plot_roc_precision_recall_operating_points


y_true, y_score = sample_arrays()
selected_threshold = 0.55

print("ROC vs Precision-Recall operating-point summary")
print(operating_curve_table(y_true, y_score, selected_threshold).round(3).to_string(index=False))

output_path = plot_roc_precision_recall_operating_points(
    y_true,
    y_score,
    "outputs/roc_precision_recall_operating_point.png",
    operating_threshold=selected_threshold,
)
print(f"Saved ROC/PR visual: {output_path}")
