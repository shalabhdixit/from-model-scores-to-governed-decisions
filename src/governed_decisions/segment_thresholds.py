from __future__ import annotations

import pandas as pd


def apply_segment_thresholds(data: pd.DataFrame, segment_thresholds: dict[str, float]) -> pd.DataFrame:
    required_columns = {"score", "segment"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Data is missing required columns: {sorted(missing_columns)}")

    enriched_data = data.copy()
    enriched_data["segment_threshold"] = enriched_data["segment"].map(segment_thresholds)
    if enriched_data["segment_threshold"].isna().any():
        missing_segments = sorted(enriched_data.loc[enriched_data["segment_threshold"].isna(), "segment"].unique())
        raise ValueError(f"No threshold configured for segments: {missing_segments}")
    enriched_data["segment_prediction"] = (enriched_data["score"] >= enriched_data["segment_threshold"]).astype(int)
    return enriched_data
