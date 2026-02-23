# app/agents/cfox_agent.py
from app.agents.llm import LLMPlanner

class CFOxAgent:
    def __init__(self, memory, policy_agent, llm, negotiation_agent=None, funding_agent=None):
        self.memory = memory
        self.policy_agent = policy_agent
        self.llm = llm
        self.negotiation_agent = negotiation_agent
        self.funding_agent = funding_agent

    def reason(self, state):
        # Guardrails first
        allowed, reason = self.policy_agent.is_action_allowed(state)
        if not allowed:
            return None

        # Cash shortfall logic
        if state.cash_projection.min_balance < 0:
            if self.negotiation_agent and state.receivables.overdue_amount > 0:
                return self.negotiation_agent.propose(
                    counterparty="Customer",
                    context={"overdue_invoice": state.receivables.most_overdue_invoice}
                )
            elif self.funding_agent:
                return self.funding_agent.select_funding(
                    cash_shortfall=abs(state.cash_projection.min_balance),
                    options={
                        "credit_line": 0.05,
                        "factoring": 0.07
                    }
                )

        # Otherwise fallback to LLM reasoning
        prompt = self._build_prompt(state)
        return self.llm.plan(prompt)


    def _build_prompt(self, state):
        return (
            f"You are an autonomous CFO agent.\n"
            f"Current state:\n{state}\n"
            f"Decide the next best action using only approved tools: "
            f"chase_invoice, optimize_payables, initiate_funding, send_notification.\n"
            f"Output strictly as JSON {{'tool': str, 'args': dict}}."
        )
