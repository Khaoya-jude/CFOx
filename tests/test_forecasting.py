"""
CFOx Forecasting Tests
"""

import pytest
from app.forecasting.cashflow import CashflowForecast
from app.forecasting.stress import revenue_drop_scenario, expense_spike_scenario
from app.forecasting.features import generate_feature_summary


@pytest.fixture
def sample_data():
    return [
        {"date": "2025-01-01", "inflow": 10000, "outflow": 7000},
        {"date": "2025-01-02", "inflow": 12000, "outflow": 8000},
        {"date": "2025-01-03", "inflow": 9000, "outflow": 6000},
    ]


def test_forecast_generates_correct_days(sample_data):
    forecast_engine = CashflowForecast(sample_data)
    projections = forecast_engine.forecast(days=10)

    assert len(projections) == 10
    assert "projected_balance" in projections[0]


def test_revenue_drop_scenario(sample_data):
    stressed = revenue_drop_scenario(sample_data, drop_percent=50)

    assert stressed[0]["inflow"] == 5000


def test_expense_spike_scenario(sample_data):
    stressed = expense_spike_scenario(sample_data, spike_percent=50)

    assert stressed[0]["outflow"] == 10500


def test_feature_summary(sample_data):
    summary = generate_feature_summary(sample_data, current_cash=50000)

    assert "average_inflow" in summary
    assert summary["current_cash"] == 50000