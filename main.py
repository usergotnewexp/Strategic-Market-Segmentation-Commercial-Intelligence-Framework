import sys
from src.data.mock_generator import MockDataGenerator
from src.services.segmentation import SegmentationService
from src.services.win_loss import WinLossAnalyzer
from src.services.metrics import MetricsCalculator

def print_separator(title=""):
    if title:
        print(f"\n{'-'*20} {title.upper()} {'-'*20}")
    else:
        print(f"{'-'*60}")

def main():
    # 1. Generate Historical Data
    print("Initializing Data Generator... Generating 100 historical deals.")
    generator = MockDataGenerator()
    deals = generator.generate_deals()
    
    # 2. Segment Customers
    segmenter = SegmentationService()
    for deal in deals:
        segmenter.segment_customer(deal.customer)

    # 3. Analyze Win-Loss Data
    analyzer = WinLossAnalyzer(deals)
    metrics_calc = MetricsCalculator()

    # Output: Executive Summary
    print_separator("Strategic Business Impact")
    impact = metrics_calc.calculate_business_impact(
        win_rate_history=38.0, target_win_rate=49.0, avg_deal_size=78000.0, total_leads_per_year=7800)
    print(f"Projected Annual Revenue Opportunity:  ₹{impact.total_revenue_opportunity:,.0f} (+₹12Cr+ potential)")
    print(f"Win Rate Improvement Target:         {impact.win_rate_before}% -> {impact.win_rate_after}% (+11 pts)")
    print(f"Average Deal Size Target:            ₹{impact.avg_deal_size_before:,.0f} -> ₹{impact.avg_deal_size_after:,.0f} (+18%)")
    print(f"Sales Cycle Time Reduction:          {impact.proposal_cycle_days_before} days -> {impact.proposal_cycle_days_after} days")

    # Output: Win-Loss By Segment
    print_separator("Win-Loss Intelligence By Segment")
    for profile in segmenter.profiles:
        stats = analyzer.analyze_by_segment(profile.segment_type)
        print(f"Segment: {profile.name}")
        print(f"  - Total Deals Evaluated: {stats['total']}")
        print(f"  - Historical Win Rate:   {stats['win_rate']}%  (Target: ~{stats['win_rate'] + 14 if profile.name.startswith('Small') else (stats['win_rate'] + 4 if profile.name.startswith('Rel') else stats['win_rate'] + 8)}%)")
        print(f"  - Value Drivers Assessed:")
        for driver in profile.primary_drivers:
            print(f"    * {driver.name.title().replace('_', ' ')} ({(driver.weight * 100):.0f}%)")
        print(f"  - Active Schneider Positioning -> '{profile.schneider_positioning}'")
        print("")

    # Output: Competitive Insights
    print_separator("Competitive Strengths & Weaknesses")
    strengths = analyzer.aggregate_competitor_strengths()
    for comp, desc in strengths.items():
        print(f"[{comp.name}]")
        print(f"  -> {desc}\n")

    print_separator("System Execution Completed")

if __name__ == "__main__":
    main()
