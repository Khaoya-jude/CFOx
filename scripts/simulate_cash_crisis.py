"""
CFOx Cash Crisis Simulation
---------------------------
Runs stress scenarios and checks for liquidity risks.
"""

import json
from pathlib import Path

from app.forecasting.cashflow import CashflowForecast
from app.forecasting.stress import revenue_drop_scenario, expense_spike_scenario
from app.forecasting.features import generate_feature_summary


DATA_PATH = Path("scripts/demo_cashflow.json")


def detect_cash_crisis(forecast_data, threshold: float = -50000):
    """
    Detect if projected balance falls below threshold.
    """
    for day in forecast_data:
        if day["projected_balance"] <= threshold:
            return True, day["date"]
    return False, None


def main():
    if not DATA_PATH.exists():
        print("No demo data found. Run seed_demo_data.py first.")
        return

    with open(DATA_PATH) as f:
        data = json.load(f)

    print("\n=== Running Stress Scenario ===")

    # Scenario 1: 30% revenue drop
    stressed_data = revenue_drop_scenario(data, drop_percent=30)

    # Scenario 2: 20% expense spike
    stressed_data = expense_spike_scenario(stressed_data, spike_percent=20)

    # Generate forecast
    forecast_engine = CashflowForecast(stressed_data)
    projections = forecast_engine.forecast(days=30)

    crisis, date = detect_cash_crisis(projections)

    feature_summary = generate_feature_summary(stressed_data, current_cash=250000)

    print("\nFeature Summary:")
    print(feature_summary)

    if crisis:
        print(f"\n⚠️  CASH CRISIS DETECTED around {date}")
    else:
        print("\n✅ No immediate liquidity crash detected.")


if __name__ == "__main__":
    main()