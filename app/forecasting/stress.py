"""
CFOx Financial Stress Testing Engine
-------------------------------------
Simulates adverse financial scenarios.
"""

from typing import List, Dict


def revenue_drop_scenario(data: List[Dict], drop_percent: float) -> List[Dict]:
    """
    Simulates a revenue drop.
    """
    stressed = []
    for entry in data:
        stressed.append({
            "date": entry["date"],
            "inflow": entry["inflow"] * (1 - drop_percent / 100),
            "outflow": entry["outflow"]
        })
    return stressed


def expense_spike_scenario(data: List[Dict], spike_percent: float) -> List[Dict]:
    """
    Simulates sudden expense increase.
    """
    stressed = []
    for entry in data:
        stressed.append({
            "date": entry["date"],
            "inflow": entry["inflow"],
            "outflow": entry["outflow"] * (1 + spike_percent / 100)
        })
    return stressed


def liquidity_shock(current_cash: float, shock_amount: float) -> float:
    """
    Immediate liquidity reduction.
    """
    return max(current_cash - shock_amount, 0)