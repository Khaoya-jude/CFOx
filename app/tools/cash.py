def get_cash_position():
    """
    Deterministic, read-only tool.
    Replace with real bank API later.
    """
    available_cash = 120_000
    committed_outflows = 75_000

    return {
        "available_cash": available_cash,
        "committed_outflows": committed_outflows,
        "net_position": available_cash - committed_outflows,
        "currency": "USD",
    }
