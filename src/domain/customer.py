from dataclasses import dataclass
from typing import Dict, Optional
from .enums import SegmentType

@dataclass
class Customer:
    id: str
    budget: float
    true_value_drivers: Dict[str, float]
    segment: Optional[SegmentType] = None
