"""
CFOx Reasoning Engine Tests
"""

import pytest
from app.orchestration.reasoning import (
    classify_risk_level,
    generate_recommendation
)


def test_low_risk_classification():
    risk = classify_risk_level(liquidity_ratio=2.0)
    assert risk == "LOW"


def test_high_risk_classification():
    risk = classify_risk_level(liquidity_ratio=0.5)
    assert risk == "HIGH"


def test_generate_recommendation_high_risk():
    rec = generate_recommendation("HIGH")
    assert "reduce" in rec.lower() or "cut" in rec.lower()