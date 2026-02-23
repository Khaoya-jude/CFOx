from typing import Dict
from app.agents.llm import LLMPlanner
from app.utils.logging import get_logger

logger = get_logger(__name__)

class NegotiationAgent:
    """
    Handles autonomous negotiation with suppliers or customers.
    """

    def __init__(self, llm: LLMPlanner):
        self.llm = llm

    def propose(self, counterparty: str, context: Dict) -> Dict:
        """
        Returns structured negotiation action:
        {"tool": "send_notification", "args": {...}}
        """
        prompt = (
            f"You are an autonomous CFO negotiation agent.\n"
            f"Negotiating with {counterparty}.\n"
            f"Context: {context}\n"
            f"Suggest next action strictly as JSON: {{'tool': str, 'args': dict}}"
        )
        plan = self.llm.plan(prompt)
        logger.info(f"Negotiation plan: {plan}")
        return plan
