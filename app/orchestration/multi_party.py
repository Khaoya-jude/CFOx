from app.orchestration.graph import CFOxGraph
from typing import List

def optimize_supply_chain(agent_graphs: List[CFOxGraph]):
    """
    Orchestrates multiple agents to optimize cash across the supply chain
    """
    for graph in agent_graphs:
        graph.run(graph.agent.memory.recall({}))  # Each agent runs using its latest state
