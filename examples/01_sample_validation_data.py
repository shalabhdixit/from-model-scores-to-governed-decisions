from governed_decisions.sample_data import load_sample_validation_data


data = load_sample_validation_data()
print(data[["actual", "score"]].head())
