"""
CFOx Cashflow Forecasting Engine
---------------------------------
Provides rolling cashflow projections and trend-based forecasting.
Designed for SME-level financial orchestration.
"""

from datetime import datetime, timedelta
from typing import List, Dict
import statistics


class CashflowForecast:
    def __init__(self, historical_data: List[Dict]):
        """
        historical_data format:
        [
            {"date": "2026-01-01", "inflow": 10000, "outflow": 7000},
            ...
        ]
        """
        self.historical_data = historical_data

    def _calculate_net_values(self) -> List[float]:
        return [
            entry["inflow"] - entry["outflow"]
            for entry in self.historical_data
        ]

    def average_net_cashflow(self) -> float:
        nets = self._calculate_net_values()
        return statistics.mean(nets) if nets else 0.0

    def forecast(self, days: int = 30) -> List[Dict]:
        """
        Generates a rolling forecast based on historical average net.
        """
        avg_net = self.average_net_cashflow()
        last_date = datetime.strptime(
            self.historical_data[-1]["date"], "%Y-%m-%d"
        )

        projections = []
        running_balance = 0

        for i in range(1, days + 1):
            forecast_date = last_date + timedelta(days=i)
            running_balance += avg_net

            projections.append({
                "date": forecast_date.strftime("%Y-%m-%d"),
                "projected_net": avg_net,
                "projected_balance": running_balance
            })

        return projections