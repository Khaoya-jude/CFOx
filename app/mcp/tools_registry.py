def register_tools(mcp):
    """
    Register all MCP-exposed tools here.
    """
    from app.tools.cash import get_cash_position
    from app.tools.receivables import chase_receivable
    from app.tools.payables import optimize_payables
    from app.tools.funding import initiate_funding
    from app.tools.notifications import send_notification

    mcp.tool()(send_notification)
    mcp.tool()(get_cash_position)
    mcp.tool()(chase_receivable)
    mcp.tool()(optimize_payables)
    mcp.tool()(initiate_funding)
