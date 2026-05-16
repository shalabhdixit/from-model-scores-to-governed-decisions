from governed_decisions.sample_data import load_sample_validation_data
from governed_decisions.thresholding import apply_threshold


data = load_sample_validation_data()
data["prediction_at_050"] = apply_threshold(data["score"], threshold=0.50)
print(data[["actual", "score", "prediction_at_050"]].head(10))
