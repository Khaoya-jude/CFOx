"""
CFOx Guardrails Tests
"""

import pytest
from app.security.guardrails import (
    validate_budget_limit,
    validate_transaction_input
)


def test_budget_limit_pass():
    assert validate_budget_limit(current_cash=100000, spend_amount=20000) is True


def test_budget_limit_fail():
    assert validate_budget_limit(current_cash=10000, spend_amount=20000) is False


def test_transaction_input_valid():
    assert validate_transaction_input(5000) is True


def test_transaction_input_invalid():
    assert validate_transaction_input(-100) is False