import logging

from app.utils.time import now_utc

logger = logging.getLogger("audit")


def audit_log(action_id: str, action: str, target: str, metadata: dict, event: dict):
    logger.info(
        f"AUDIT | action_id={action_id} | action={action} | "
        f"target={target} | metadata={metadata}"
    )

    print({
        "timestamp": now_utc().isoformat(),
        "event": event
    })
