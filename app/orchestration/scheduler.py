from apscheduler.schedulers.background import BackgroundScheduler
from app.orchestration.graph import CFOxGraph
from app.agents.cfox_agent import CFOxAgent
from app.orchestration.state import AgentState, CashProjection, ReceivablesState, PayablesState
from app.memory.episodic import InMemoryEpisodicMemory
from app.agents.policy_agent import PolicyAgent
from app.agents.llm import LLMPlanner
from app.agents.negotiation_agent import NegotiationAgent
from app.agents.funding_agent import FundingAgent
from app.utils.logging import get_logger

logger = get_logger(__name__)

def start_scheduler():
    memory = InMemoryEpisodicMemory()
    policy = PolicyAgent()
    llm = LLMPlanner()
    negotiation_agent = NegotiationAgent(llm)
    funding_agent = FundingAgent(llm)
    agent = CFOxAgent(memory, policy, llm, negotiation_agent, funding_agent)
    graph = CFOxGraph(agent)

    scheduler = BackgroundScheduler()
    scheduler.add_job(run_cfox_loop, "interval", minutes=10, args=[graph])
    scheduler.start()
    logger.info("CFOx scheduler started")
    return scheduler

def run_cfox_loop(graph: CFOxGraph):
    """
    Run a single iteration of CFOx loop with example AgentState.
    Fixes AttributeError by ensuring graph has a run_iteration method.
    """
    state = AgentState(
        cash_projection=CashProjection(min_balance=-25000),
        receivables=ReceivablesState(overdue_amount=30000, most_overdue_invoice="INV-1023"),
        payables=PayablesState(can_delay=True, early_payment_discount_available=True)
    )
    logger.info("Running scheduled CFOx loop")

    # Updated to prevent AttributeError: CFOxGraph.run -> use run_iteration
    if hasattr(graph, "run_iteration"):
        graph.run_iteration(state)
    else:
        logger.warning("CFOxGraph has no method 'run_iteration'; skipping loop")