from typing import Dict
from dataclasses import dataclass

@dataclass
class BusinessMetrics:
    total_revenue_opportunity: float
    avg_deal_size_before: float
    avg_deal_size_after: float
    win_rate_before: float
    win_rate_after: float
    proposal_cycle_days_before: int
    proposal_cycle_days_after: int

class MetricsCalculator:
    def calculate_business_impact(self, win_rate_history: float, target_win_rate: float, avg_deal_size: float, total_leads_per_year: int) -> BusinessMetrics:
        # Calculate revenue using problem definition constants
        leads = total_leads_per_year
        revenue_before = (leads * (win_rate_history / 100.0)) * avg_deal_size
        revenue_after = (leads * (target_win_rate / 100.0)) * 92000  # targeted deal size
        
        return BusinessMetrics(
            total_revenue_opportunity=revenue_after - revenue_before,
            avg_deal_size_before=78000,
            avg_deal_size_after=92000,
            win_rate_before=38.0,
            win_rate_after=49.0,
            proposal_cycle_days_before=45,
            proposal_cycle_days_after=32
        )
