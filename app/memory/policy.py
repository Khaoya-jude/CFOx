class AutonomyPolicy:
    MAX_AUTONOMOUS_FUNDING = 500_000

    @staticmethod
    def funding_allowed(amount: float) -> bool:
        return amount <= AutonomyPolicy.MAX_AUTONOMOUS_FUNDING
 