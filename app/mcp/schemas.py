from typing import TypedDict, Optional
from pydantic import BaseModel

class ToolResult(BaseModel):
    status: str
    message: str
    data: dict | None = None



class ActionResult(TypedDict):
    action_id: str
    status: str
    expected_impact: str
    risk_level: str


class ChaseReceivableInput(TypedDict):
    invoice_id: str
    tone: str
    discount_offer: Optional[float]
