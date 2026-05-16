from governed_decisions.business_value import calculate_business_value


def test_calculate_business_value_uses_configured_values():
    row = {
        "true_positives": 2,
        "false_positives": 1,
        "false_negatives": 3,
        "true_negatives": 4,
    }
    values = {
        "true_positive_value": 500,
        "false_positive_cost": -80,
        "false_negative_cost": -1000,
        "true_negative_value": 0,
    }
    assert calculate_business_value(row, values) == -2080
