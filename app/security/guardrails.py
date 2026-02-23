"""
CFOx Guardrails Module
Validation functions for budget and transaction constraints.
"""

def validate_budget_limit(current_cash: float, spend_amount: float) -> bool:
    """Check if spending amount doesn't exceed current cash."""
    return spend_amount <= current_cash


def validate_transaction_input(amount: float) -> bool:
    """Validate that transaction amount is positive."""
    return amount > 0