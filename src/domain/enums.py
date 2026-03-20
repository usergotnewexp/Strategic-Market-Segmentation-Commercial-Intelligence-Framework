from enum import Enum, auto

class SegmentType(Enum):
    SMALL_COMMERCIAL = auto()
    INDUSTRIAL = auto()
    INFRASTRUCTURE = auto()

class Competitor(Enum):
    SCHNEIDER = auto()
    L_AND_T = auto()
    ABB = auto()
    SIEMENS = auto()

class DealStatus(Enum):
    WON = auto()
    LOST = auto()
    OPEN = auto()
