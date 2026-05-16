from __future__ import annotations

from datetime import datetime, timezone


def score_decision(
    record_id: str,
    model_score: float,
    threshold: float,
    model_version: str,
    threshold_version: str,
    action_positive: str = "review",
    action_negative: str = "auto_clear",
) -> dict[str, object]:
    predicted_label = int(model_score >= threshold)
    action = action_positive if predicted_label == 1 else action_negative
    return {
        "record_id": record_id,
        "model_score": float(model_score),
        "threshold": float(threshold),
        "predicted_label": predicted_label,
        "action": action,
        "model_version": model_version,
        "threshold_version": threshold_version,
        "decision_time_utc": datetime.now(timezone.utc).isoformat(),
    }
