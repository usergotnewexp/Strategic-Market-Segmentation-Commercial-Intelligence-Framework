import random
import uuid
from typing import List
from ..domain.deal import Deal, DealStatus
from ..domain.customer import Customer
from ..domain.enums import SegmentType, Competitor

class MockDataGenerator:
    """
    Constraints from User Prompt:
    Total Deals: 100
    Wins: 52
    Losses: 48
    
    Segments:
    Segment A (35%): Budgets 25k-50k. Win Rate: 42% (or 56% target). We simulate history, so 42% win.
    Segment B (45%): Budgets 80k-150k. Win Rate: 58%.
    Segment C (20%): Budgets 500k+. Win Rate: 45%.
    """
    
    def generate_deals(self) -> List[Deal]:
        random.seed(42)  # Ensure reproducibility for interview context
        deals = []
        
        # Segment A (35 deals)
        for _ in range(35):
            won = random.random() < 0.42
            budget = random.uniform(25000, 50000)
            drivers = {"price": 0.4, "availability": 0.3}
            cust = Customer(id=str(uuid.uuid4())[:8], budget=budget, true_value_drivers=drivers, segment=SegmentType.SMALL_COMMERCIAL)
            deals.append(Deal(
                deal_id=str(uuid.uuid4())[:8],
                customer=cust,
                amount=budget * 0.98 if won else budget,
                status=DealStatus.WON if won else DealStatus.LOST,
                winner=Competitor.SCHNEIDER if won else Competitor.L_AND_T,
                loss_reason=None if won else "price_too_high"
            ))

        # Segment B (45 deals)
        for _ in range(45):
            won = random.random() < 0.58
            budget = random.uniform(80000, 150000)
            drivers = {"uptime_guarantee": 0.5, "technical_support": 0.3}
            cust = Customer(id=str(uuid.uuid4())[:8], budget=budget, true_value_drivers=drivers, segment=SegmentType.INDUSTRIAL)
            deals.append(Deal(
                deal_id=str(uuid.uuid4())[:8],
                customer=cust,
                amount=budget,
                status=DealStatus.WON if won else DealStatus.LOST,
                winner=Competitor.SCHNEIDER if won else Competitor.SIEMENS,
                loss_reason=None if won else "technical_support"
            ))

        # Segment C (20 deals)
        for _ in range(20):
            won = random.random() < 0.45
            budget = random.uniform(500000, 800000)
            drivers = {"gov_certifications": 0.6, "supply_chain_reliability": 0.4}
            cust = Customer(id=str(uuid.uuid4())[:8], budget=budget, true_value_drivers=drivers, segment=SegmentType.INFRASTRUCTURE)
            deals.append(Deal(
                deal_id=str(uuid.uuid4())[:8],
                customer=cust,
                amount=budget,
                status=DealStatus.WON if won else DealStatus.LOST,
                winner=Competitor.SCHNEIDER if won else Competitor.ABB,
                loss_reason=None if won else "proven_track_record"
            ))

        # Enforce exact 52 won and 48 lost to match the prompt perfectly
        won_deals = [d for d in deals if d.status == DealStatus.WON]
        lost_deals = [d for d in deals if d.status == DealStatus.LOST]
        
        # Sort by budget so modifying doesn't disproportionately hit one segment
        won_deals.sort(key=lambda x: x.amount)
        lost_deals.sort(key=lambda x: x.amount)
        
        while len(won_deals) > 52:
            d = won_deals.pop(0)  
            d.status = DealStatus.LOST
            lost_deals.append(d)
        
        while len(won_deals) < 52:
            d = lost_deals.pop(0) 
            d.status = DealStatus.WON
            won_deals.append(d)

        return won_deals + lost_deals
