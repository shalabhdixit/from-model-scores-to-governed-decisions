from __future__ import annotations

import pandas as pd


ANTI_PATTERNS = [
    ("Always using 0.50", "Ignores asymmetric business cost", "Tune threshold against business objectives"),
    ("Optimizing only F1", "Treats false positives and false negatives as equally important", "Use cost-sensitive evaluation"),
    ("Ignoring capacity", "Creates more actions than operations can handle", "Add review capacity constraints"),
    ("Hardcoding threshold", "Makes governance and rollback difficult", "Store threshold in versioned config"),
    ("No monitoring after launch", "Threshold can degrade as data shifts", "Track alert volume, outcomes, and drift"),
    ("No business owner", "Leaves decision policy to technical convenience", "Define joint ownership across data, product, risk, and operations"),
    ("No calibration review", "Assumes probabilities are reliable because ranking metrics look good", "Validate score reliability before policy approval"),
    ("No rollback authority", "Delays recovery when the decision boundary causes operational harm", "Assign rollback owners before release"),
    ("Aggregate-only monitoring", "Hides segment-level fairness, friction, and error patterns", "Monitor outcomes and overrides by segment"),
    ("Treating overrides as noise", "Loses evidence about policy failure", "Analyze human disagreement as a governance signal"),
    ("Quiet threshold releases", "Turns business policy into invisible technical deployment", "Use approval workflows and release notes for threshold versions"),
]


def anti_pattern_table() -> pd.DataFrame:
    return pd.DataFrame(ANTI_PATTERNS, columns=["anti_pattern", "why_it_fails", "better_practice"])
