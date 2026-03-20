from dataclasses import dataclass
from typing import Dict
from .enums import SegmentType

@dataclass
class ValueDriver:
    name: str
    weight: float

@dataclass
class SegmentProfile:
    segment_type: SegmentType
    name: str
    budget_range: tuple[float, float]
    primary_drivers: list[ValueDriver]
    schneider_positioning: str
    win_strategy: str

    def matches_customer(self, budget: float, drivers: Dict[str, float]) -> bool:
        min_b, max_b = self.budget_range
        if not (min_b <= budget <= max_b):
            return False
            
        driver_match_score = 0.0
        for driver in self.primary_drivers:
            if driver.name in drivers:
                driver_match_score += drivers[driver.name] * driver.weight
                
        return driver_match_score > 0.5
