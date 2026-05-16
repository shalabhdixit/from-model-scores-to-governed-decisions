from __future__ import annotations

import pandas as pd


def binary_classification_use_cases() -> pd.DataFrame:
    return pd.DataFrame([
        ("Fraud monitoring", "Probability that a transaction is suspicious", "Block, approve, or send to review"),
        ("Customer churn", "Probability that a customer will leave", "Trigger retention outreach"),
        ("Claims triage", "Probability that a claim is complex or risky", "Route to specialist review"),
        ("Credit decisioning", "Probability that an applicant is high risk", "Approve, decline, or request manual review"),
        ("Lead prioritization", "Probability that a lead will convert", "Route to sales or nurture queue"),
        ("Service operations", "Probability that a ticket will breach SLA", "Escalate or auto-prioritize"),
    ], columns=["business_problem", "model_score_represents", "threshold_driven_action"])


def decision_boundary_fit_matrix() -> pd.DataFrame:
    return pd.DataFrame([
        ("False positives and false negatives have different costs", "Use threshold optimization with business value assumptions"),
        ("The model routes work to human teams", "Include manual review capacity and SLA constraints"),
        ("The business needs explainable decision policies", "Version and document threshold policy"),
        ("The model supports risk, fraud, compliance, churn, claims, or prioritization", "Treat the threshold as an operating policy"),
        ("The model probabilities are poorly calibrated", "Calibrate scores before approving threshold policy"),
        ("The decision requires ranking rather than classification", "Use ranking metrics, top-k evaluation, lift charts, or queue optimization"),
        ("The business cannot define costs or constraints", "Run discovery before pretending the threshold is objective"),
    ], columns=["situation", "recommended_direction"])
