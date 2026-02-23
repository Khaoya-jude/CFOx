"""
CFOx MCP Tools Tests
"""

import pytest
from app.tools import list_tools, execute_tool


def test_list_tools_returns_array():
    tools = list_tools()
    assert isinstance(tools, list)


def test_execute_known_tool():
    tools = list_tools()
    if not tools:
        pytest.skip("No tools registered.")

    tool_name = tools[0]["name"]
    result = execute_tool(tool_name, {})

    assert result is not None


def test_execute_invalid_tool():
    with pytest.raises(ValueError):
        execute_tool("non_existent_tool", {})