from app.orchestration.state import AgentState


class PolicyAgent:
    """
    Enforces autonomy limits and risk rules.
    """

    def is_action_allowed(self, state: AgentState):
        # Example guardrails
        if abs(state.cash_projection.min_balance) > 500_000:
            return False, "Funding amount exceeds autonomy limit"

        return True, "Allowed"
