from dataclasses import dataclass, field
from typing import Optional, List
from .enums import SegmentType, Competitor, DealStatus
from .customer import Customer

@dataclass
class Deal:
    deal_id: str
    customer: Customer
    amount: float
    status: DealStatus
    winner: Optional[Competitor] = None
    competitors_involved: List[Competitor] = field(default_factory=list)
    loss_reason: Optional[str] = None
    win_reason: Optional[str] = None
