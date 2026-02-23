import uuid
import httpx
from app.utils.logging import get_logger

logger = get_logger(__name__)

MCP_ENDPOINT = "http://localhost:3333"


def observe_node(state):
    logger.debug("Observing state")
    return state


def reason_node(agent, state):
    logger.debug("Reasoning step")
    return agent.reason(state)


def act_node(action: dict):
    """
    Execute action via MCP JSON-RPC over HTTP.
    """
    tool = action["tool"]
    args = action["args"]

    logger.info(f"Executing action via MCP: {tool}")

    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "tools/call",
        "params": {
            "name": tool,
            "arguments": args,
        },
    }

    with httpx.Client(timeout=10.0) as client:
        response = client.post(MCP_ENDPOINT, json=payload)
        response.raise_for_status()

    data = response.json()

    if "error" in data:
        raise RuntimeError(f"MCP error: {data['error']}")

    result = data.get("result")

    logger.info(f"Tool result: {result}")
    return result


def learn_node(agent, state, action, result):
    logger.debug("Learning from outcome")

    agent.memory.remember(
        {
            "state": state,
            "action": action,
            "result": result,
        }
    )
