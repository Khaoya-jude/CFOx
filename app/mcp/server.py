import threading
import os
from fastmcp.server import FastMCP

try:
    from fastmcp.models import SessionConfig  # type: ignore
except Exception:
    # Fallback SessionConfig if fastmcp is not installed or the module path differs
    from dataclasses import dataclass

    @dataclass
    class SessionConfig:
        auto_create: bool = False
        timeout_seconds: int = 0

# Docker-friendly host + port
HOST = os.getenv("MCP_HOST", "0.0.0.0")
PORT = int(os.getenv("MCP_PORT", 8000))

# Singleton MCP instance
_mcp_instance: FastMCP | None = None

def start_mcp_server():
    """
    Start the FastMCP server in a background daemon thread.
    Automatically handles sessions for clients.
    """
    global _mcp_instance

    if _mcp_instance is not None:
        return

    _mcp_instance = FastMCP("cfox-mcp")

    # Auto-create sessions for clients
    _mcp_instance.session_config = SessionConfig(
        auto_create=True,
        timeout_seconds=3600
    )

    def run_server():
        try:
            _mcp_instance.run(
                transport="http",
                host=HOST,
                port=PORT,
            )
        except Exception as e:
            print("[ERROR] Failed to start MCP server:", e)

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    print(f"[INFO] CFOx MCP Server started at http://{HOST}:{PORT}/mcp")

def get_mcp_client():
    """
    Return a FastMCP HTTP client connected to the running server.
    """
    from fastmcp.client import Client

    if _mcp_instance is None:
        raise RuntimeError("MCP server is not running")

    docker_host = os.getenv("MCP_CLIENT_HOST", "localhost")
    return Client(f"http://{docker_host}:{PORT}/mcp")