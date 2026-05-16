from governed_decisions.calibration import calibration_summary, expected_calibration_error, score_distribution
from governed_decisions.sample_data import sample_arrays
from governed_decisions.visualization import plot_calibration_reliability


y_true, y_score = sample_arrays()

print("Calibration summary")
print(calibration_summary(y_true, y_score, n_bins=5).round(3).to_string(index=False))

print("\nScore distribution")
print(score_distribution(y_score, n_bins=5).to_string(index=False))

print(f"\nExpected calibration error: {expected_calibration_error(y_true, y_score, n_bins=5):.3f}")

output_path = plot_calibration_reliability(y_true, y_score, "outputs/calibration_reliability.png", n_bins=5)
print(f"Saved calibration visual: {output_path}")
