from __future__ import annotations

DEFAULT_BUSINESS_VALUES = {
    "true_positive_value": 500,
    "false_positive_cost": -80,
    "false_negative_cost": -1000,
    "true_negative_value": 0,
}


def calculate_business_value(row, values: dict[str, float] | None = None) -> float:
    value_model = values or DEFAULT_BUSINESS_VALUES
    return float(
        row["true_positives"] * value_model["true_positive_value"]
        + row["false_positives"] * value_model["false_positive_cost"]
        + row["false_negatives"] * value_model["false_negative_cost"]
        + row["true_negatives"] * value_model["true_negative_value"]
    )
