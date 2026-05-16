from governed_decisions.decision_logging import score_decision


def test_score_decision_logs_threshold_and_versions():
    decision = score_decision(
        record_id="TXN-10001",
        model_score=0.62,
        threshold=0.55,
        model_version="fraud-model-v4",
        threshold_version="threshold-policy-2026-05",
    )
    assert decision["predicted_label"] == 1
    assert decision["action"] == "review"
    assert decision["threshold_version"] == "threshold-policy-2026-05"
