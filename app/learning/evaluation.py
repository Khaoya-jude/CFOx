from app.utils.logging import get_logger

logger = get_logger(__name__)

class Metrics:
    """
    Tracks CFOx performance metrics
    """

    def __init__(self):
        self.metrics = {
            "discounts_captured": 0.0,
            "financing_cost_saved": 0.0,
            "late_fees_avoided": 0.0
        }

    def update(self, event: dict):
        self.metrics["discounts_captured"] += event.get("discounts", 0.0)
        self.metrics["financing_cost_saved"] += event.get("financing_saved", 0.0)
        self.metrics["late_fees_avoided"] += event.get("late_fees_avoided", 0.0)

        logger.info(f"Updated metrics: {self.metrics}")

    def report(self):
        return self.metrics
