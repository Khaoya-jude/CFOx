import uuid
from app.security.audit import audit_log


def chase_receivable(
    invoice_id: str,
    tone: str,
    discount_offer: float | None = None,
):
    action_id = str(uuid.uuid4())

    audit_log(
        action_id=action_id,
        action="chase_receivable",
        target=invoice_id,
        metadata={
            "tone": tone,
            "discount_offer": discount_offer,
        },
    )

    return {
        "action_id": action_id,
        "status": "executed",
        "expected_impact": "Improved probability of payment within 7 days",
        "risk_level": "low",
    }

def chase_invoice(invoice_id: str, urgency: str):
    return {
        "status": "success",
        "message": f"Invoice {invoice_id} chased with {urgency} urgency",
        "data": {"invoice_id": invoice_id}
    }
