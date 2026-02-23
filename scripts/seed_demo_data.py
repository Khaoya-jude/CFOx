"""
CFOx Demo Data Seeder
---------------------
Generates synthetic SME financial history
for forecasting and stress testing.
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path


DATA_PATH = Path("scripts/demo_cashflow.json")


def generate_demo_cashflow(days: int = 90):
    """
    Generates realistic SME daily inflow/outflow.
    """
    base_date = datetime.today() - timedelta(days=days)
    data = []

    for i in range(days):
        date = base_date + timedelta(days=i)

        # Simulate weekday business cycles
        weekday_factor = 1.2 if date.weekday() < 5 else 0.6

        inflow = random.randint(8000, 15000) * weekday_factor
        outflow = random.randint(5000, 12000)

        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "inflow": round(inflow, 2),
            "outflow": round(outflow, 2)
        })

    return data


def main():
    print("Generating demo financial data...")
    data = generate_demo_cashflow()

    DATA_PATH.write_text(json.dumps(data, indent=4))
    print(f"Demo data saved to {DATA_PATH}")


if __name__ == "__main__":
    main()