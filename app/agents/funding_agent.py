from typing import Dict
from app.agents.llm import LLMPlanner
from app.utils.logging import get_logger

logger = get_logger(__name__)

class FundingAgent:
    """
    Chooses the optimal funding source based on cost, speed, and cash need.
    """

    def __init__(self, llm: LLMPlanner):
        self.llm = llm

    def select_funding(self, cash_shortfall: float, options: Dict) -> Dict:
        """
        Returns structured funding action:
        {"tool": "initiate_funding", "args": {...}}
        """
        prompt = (
            f"You are a funding agent.\n"
            f"Cash shortfall: {cash_shortfall}\n"
            f"Funding options: {options}\n"
            f"Output strictly as JSON {{'tool': str, 'args': dict}}"
        )
        plan = self.llm.plan(prompt)
        logger.info(f"Funding plan: {plan}")
        return plan
