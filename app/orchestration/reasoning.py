"""
CFOx Reasoning Engine

Provides deterministic financial reasoning logic used by CFOxGraph
to evaluate liquidity risk and generate strategic recommendations.
"""

from dataclasses import dataclass
from typing import Dict


# -----------------------------------------------------
# Risk Classification
# -----------------------------------------------------

def classify_risk_level(liquidity_ratio: float) -> str:
    """
    Classify financial liquidity risk based on liquidity ratio.

    liquidity_ratio = current_assets / current_liabilities

    Thresholds:
        >= 1.5  -> LOW
        1.0-1.49 -> MEDIUM
        < 1.0   -> HIGH
    """
    if liquidity_ratio >= 1.5:
        return "LOW"
    elif 1.0 <= liquidity_ratio < 1.5:
        return "MEDIUM"
    else:
        return "HIGH"


# -----------------------------------------------------
# Cash Risk Score
# -----------------------------------------------------

def calculate_cash_risk_score(
    current_cash: float,
    projected_min_balance: float,
    overdue_receivables: float,
) -> float:
    """
    Compute a composite cash risk score (0-100).

    Higher score = higher risk.

    Components:
        - Negative projected balance increases risk
        - Low cash buffer increases risk
        - High overdue receivables increases risk
    """

    score = 0.0

    # Projected negative balance impact
    if projected_min_balance < 0:
        score += min(abs(projected_min_balance) / 1000, 40)

    # Low cash buffer
    if current_cash < 50000:
        score += 20

    # Overdue receivables risk
    if overdue_receivables > 0:
        score += min(overdue_receivables / 2000, 40)

    return min(score, 100.0)


# -----------------------------------------------------
# Recommendation Engine
# -----------------------------------------------------

def generate_recommendation(risk_level: str) -> str:
    """
    Generate CFO recommendation based on risk classification.
    """

    recommendations = {
        "LOW": (
            "Liquidity position is healthy. Maintain current strategy "
            "and consider short-term investment opportunities."
        ),
        "MEDIUM": (
            "Moderate liquidity pressure detected. Tighten receivables "
            "collection and delay non-essential expenses."
        ),
        "HIGH": (
            "Severe liquidity risk detected. Reduce discretionary spending, "
            "accelerate collections, negotiate payables, or seek short-term funding."
        ),
    }

    return recommendations.get(
        risk_level,
        "Unable to determine recommendation due to unknown risk level.",
    )


# -----------------------------------------------------
# Unified Decision Function
# -----------------------------------------------------

@dataclass
class ReasoningResult:
    liquidity_ratio: float
    risk_level: str
    risk_score: float
    recommendation: str


def evaluate_financial_state(
    current_assets: float,
    current_liabilities: float,
    current_cash: float,
    projected_min_balance: float,
    overdue_receivables: float,
) -> ReasoningResult:
    """
    End-to-end financial evaluation used by CFOxGraph.

    Returns structured reasoning result.
    """

    if current_liabilities == 0:
        liquidity_ratio = float("inf")
    else:
        liquidity_ratio = current_assets / current_liabilities

    risk_level = classify_risk_level(liquidity_ratio)

    risk_score = calculate_cash_risk_score(
        current_cash=current_cash,
        projected_min_balance=projected_min_balance,
        overdue_receivables=overdue_receivables,
    )

    recommendation = generate_recommendation(risk_level)

    return ReasoningResult(
        liquidity_ratio=liquidity_ratio,
        risk_level=risk_level,
        risk_score=risk_score,
        recommendation=recommendation,
    )