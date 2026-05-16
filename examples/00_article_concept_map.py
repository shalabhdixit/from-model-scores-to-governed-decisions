from governed_decisions.article_concepts import binary_classification_use_cases, decision_boundary_fit_matrix


print("Binary classification business contexts")
print(binary_classification_use_cases().to_string(index=False))

print("\nWhen threshold tuning is the right tool")
print(decision_boundary_fit_matrix().to_string(index=False))
