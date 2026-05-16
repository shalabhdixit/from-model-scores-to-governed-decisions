from __future__ import annotations

import pandas as pd


def add_capacity_columns(report: pd.DataFrame, max_manual_reviews: int | None = None) -> pd.DataFrame:
    enriched_report = report.copy()
    enriched_report["manual_reviews"] = enriched_report["true_positives"] + enriched_report["false_positives"]
    if max_manual_reviews is None:
        enriched_report["within_capacity"] = True
    else:
        enriched_report["within_capacity"] = enriched_report["manual_reviews"] <= max_manual_reviews
    return enriched_report
