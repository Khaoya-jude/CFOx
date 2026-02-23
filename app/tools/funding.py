import uuid
from app.security.audit import audit_log


def initiate_funding(
    funding_type: str,
    amount: float,
):
    """
    Initiate funding such as:
    - short-term loan
    - invoice factoring
    - credit line drawdown
    """

    action_id = str(uuid.uuid4())

    audit_log(
        action_id=action_id,
        action="initiate_funding",
        target=funding_type,
        metadata={
            "amount": amount,
        },
    )

    return {
        "action_id": action_id,
        "status": "initiated",
        "funding_type": funding_type,
        "amount": amount,
        "risk_level": "medium",
    }


