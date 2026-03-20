from typing import Optional
from ..domain.customer import Customer
from ..domain.segment import SegmentProfile
from ..domain.value_drivers import PROFILES

class SegmentationService:
    def __init__(self, profiles: list[SegmentProfile] = PROFILES):
        self.profiles = profiles

    def segment_customer(self, customer: Customer) -> Optional[SegmentProfile]:
        for profile in self.profiles:
            # We determine segment primarily by budget bounds in a real scenario
            # or by doing a distance match on value drivers.
            # Here, we do a blend: Budget must match the tier.
            min_b, max_b = profile.budget_range
            if min_b <= customer.budget <= max_b:
                customer.segment = profile.segment_type
                return profile
        
        return None
