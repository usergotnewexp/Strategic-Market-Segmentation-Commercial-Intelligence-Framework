from .segment import SegmentProfile, ValueDriver
from .enums import SegmentType

# Small Commercial (Segment A)
SEGMENT_A = SegmentProfile(
    segment_type=SegmentType.SMALL_COMMERCIAL,
    name="Small Commercial (Segment A)",
    budget_range=(20000, 75000),  # Broadened slightly to catch edges mapping to 25k-50k core
    primary_drivers=[
        ValueDriver("price", 0.40),
        ValueDriver("availability", 0.25),
        ValueDriver("basic_reliability", 0.20),
        ValueDriver("local_service", 0.15)
    ],
    schneider_positioning="Competitive pricing ₹28-35K, 2-week lead time, 120 service centers",
    win_strategy="Price match or beat L&T, emphasize local availability"
)

# Industrial (Segment B)
SEGMENT_B = SegmentProfile(
    segment_type=SegmentType.INDUSTRIAL,
    name="Reliability-Driven Industrial (Segment B)",
    budget_range=(75001, 400000), # Core is 100k-150k
    primary_drivers=[
        ValueDriver("uptime_guarantee", 0.35),
        ValueDriver("technical_support", 0.25),
        ValueDriver("warranty", 0.20),
        ValueDriver("system_integration", 0.15),
        ValueDriver("price", 0.05)
    ],
    schneider_positioning="7-year warranty (industry-best), 24/7 support, IEC 61947 certified, systems integration capability",
    win_strategy="Lead with warranty + support advantage, show case studies of zero-downtime operations"
)

# Infrastructure/Utilities (Segment C)
SEGMENT_C = SegmentProfile(
    segment_type=SegmentType.INFRASTRUCTURE,
    name="Project-Driven Infrastructure (Segment C)",
    budget_range=(400001, 10000000), # Core is 500k+
    primary_drivers=[
        ValueDriver("gov_certifications", 0.40),
        ValueDriver("supply_chain_reliability", 0.25),
        ValueDriver("proven_track_record", 0.20),
        ValueDriver("system_design_support", 0.10),
        ValueDriver("cost", 0.05)
    ],
    schneider_positioning="✓ BIS certified, ✓ 50,000+ unit capacity, ✓ Deployed in 15+ major projects, ✓ Free system engineering",
    win_strategy="Leverage infrastructure portfolio, provide references, offer dedicated project manager"
)

PROFILES = [SEGMENT_A, SEGMENT_B, SEGMENT_C]
