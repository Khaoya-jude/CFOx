from app.orchestration.nodes import (
    observe_node,
    reason_node,
    act_node,
    learn_node,
)
from app.orchestration.state import AgentState
from app.orchestration.reasoning import evaluate_financial_state
from app.utils.logging import get_logger

logger = get_logger(__name__)


class CFOxGraph:
    """
    Deterministic Observe → Reason → Act → Learn loop
    Enhanced with structured financial reasoning.
    """

    def __init__(self, agent):
        self.agent = agent

    def run(self, state: AgentState):
        """
        Execute one full CFOx reasoning cycle.
        """

        logger.info("Starting CFOx graph execution")

        # -------------------------------------------------
        # 1️⃣ Observe
        # -------------------------------------------------
        state = observe_node(state)

        # -------------------------------------------------
        # 2️⃣ Deterministic Financial Evaluation
        # -------------------------------------------------
        reasoning_result = evaluate_financial_state(
            current_assets=state.cash_projection.min_balance + 100000,  # simulated assets
            current_liabilities=100000,  # placeholder until DB integrated
            current_cash=state.cash_projection.min_balance,
            projected_min_balance=state.cash_projection.min_balance,
            overdue_receivables=state.receivables.overdue_amount,
        )

        logger.info(
            f"Liquidity Ratio: {reasoning_result.liquidity_ratio:.2f} | "
            f"Risk Level: {reasoning_result.risk_level} | "
            f"Risk Score: {reasoning_result.risk_score:.2f}"
        )

        logger.info(f"Recommendation: {reasoning_result.recommendation}")

        # -------------------------------------------------
        # 3️⃣ Agent Reasoning Layer (LLM / policy driven)
        # -------------------------------------------------
        action = reason_node(self.agent, state)

        # -------------------------------------------------
        # 4️⃣ Act
        # -------------------------------------------------
        if action:
            logger.info(f"Executing action: {action}")

            result = act_node(action)

            # -------------------------------------------------
            # 5️⃣ Learn
            # -------------------------------------------------
            learn_node(self.agent, state, action, result)

        logger.info("CFOx graph execution completed")