from dataclasses import dataclass


@dataclass
class CashProjection:
    min_balance: float


@dataclass
class ReceivablesState:
    overdue_amount: float
    most_overdue_invoice: str | None


@dataclass
class PayablesState:
    can_delay: bool
    early_payment_discount_available: bool


@dataclass
class AgentState:
    cash_projection: CashProjection
    receivables: ReceivablesState
    payables: PayablesState
