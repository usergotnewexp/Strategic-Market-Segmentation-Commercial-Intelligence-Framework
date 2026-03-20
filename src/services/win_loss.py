from typing import List, Dict, Any
from ..domain.deal import Deal
from ..domain.enums import DealStatus, SegmentType, Competitor

class WinLossAnalyzer:
    def __init__(self, deals: List[Deal]):
        self.deals = deals

    def analyze_by_segment(self, segment: SegmentType) -> Dict[str, Any]:
        segment_deals = [d for d in self.deals if d.customer.segment == segment]
        if not segment_deals:
            return {"total": 0, "won": 0, "lost": 0, "win_rate": 0.0}

        won_deals = [d for d in segment_deals if d.status == DealStatus.WON]
        lost_deals = [d for d in segment_deals if d.status == DealStatus.LOST]

        return {
            "total": len(segment_deals),
            "won": len(won_deals),
            "lost": len(lost_deals),
            "win_rate": round(len(won_deals) / len(segment_deals) * 100, 1),
            "avg_won_deal_size": sum(d.amount for d in won_deals) / len(won_deals) if won_deals else 0,
            "avg_lost_deal_size": sum(d.amount for d in lost_deals) / len(lost_deals) if lost_deals else 0,
        }

    def aggregate_competitor_strengths(self) -> Dict[Competitor, str]:
        # Based on problem intelligence insights
        return {
            Competitor.L_AND_T: "Dominates small commercial (price + local manufacturing).",
            Competitor.ABB: "Strong brand perception (Swiss quality), high trust, weak local support.",
            Competitor.SIEMENS: "Best-in-class system integration, dominant in large industrial.",
            Competitor.SCHNEIDER: "Best value - Siemens quality at ABB prices, local advantage."
        }

    def get_loss_reasons(self, segment: SegmentType) -> Dict[str, int]:
        reasons = {}
        for deal in self.deals:
            if deal.customer.segment == segment and deal.status == DealStatus.LOST and deal.loss_reason:
                reasons[deal.loss_reason] = reasons.get(deal.loss_reason, 0) + 1
        return reasons
