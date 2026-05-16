from governed_decisions.decision_logging import score_decision


decision = score_decision(
    record_id="TXN-10001",
    model_score=0.62,
    threshold=0.55,
    model_version="fraud-model-v4",
    threshold_version="threshold-policy-2026-05",
)
print(decision)
