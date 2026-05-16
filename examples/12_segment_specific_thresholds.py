from governed_decisions.sample_data import load_sample_validation_data
from governed_decisions.segment_thresholds import apply_segment_thresholds


data = load_sample_validation_data()
segment_thresholds = {
    "high_value": 0.65,
    "standard": 0.45,
}
segmented_data = apply_segment_thresholds(data, segment_thresholds)
print(segmented_data[["actual", "score", "segment", "segment_threshold", "segment_prediction"]].head(8))
