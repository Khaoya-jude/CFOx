"""
CFOx Financial Feature Engineering
-----------------------------------
Extracts structured indicators from raw financial data
for forecasting and risk analysis.
"""

from typing import List, Dict
import statistics


def compute_volatility(data: List[Dict]) -> float:
    """
    Standard deviation of net cashflow.
    """
    nets = [d["inflow"] - d["outflow"] for d in data]
    if len(nets) < 2:
        return 0.0
    return statistics.stdev(nets)


def compute_burn_rate(data: List[Dict]) -> float:
    """
    Average daily negative net.
    """
    nets = [d["inflow"] - d["outflow"] for d in data]
    negatives = [n for n in nets if n < 0]
    return abs(statistics.mean(negatives)) if negatives else 0.0


def liquidity_ratio(current_cash: float, avg_monthly_expense: float) -> float:
    """
    Months of runway.
    """
    if avg_monthly_expense == 0:
        return float("inf")
    return current_cash / avg_monthly_expense


def generate_feature_summary(data: List[Dict], current_cash: float) -> Dict:
    avg_expense = statistics.mean([d["outflow"] for d in data])
    return {
        "volatility": compute_volatility(data),
        "burn_rate": compute_burn_rate(data),
        "runway_months": liquidity_ratio(current_cash, avg_expense)
    }