"""Constants used in the archeryutils package."""
from types import SimpleNamespace

YARD_TO_METRE = 0.9144
CM_TO_METRE = 0.01

YARD_ALIASES = (
    "Yard",
    "yard",
    "Yards",
    "yards",
    "Y",
    "y",
    "Yd",
    "yd",
    "Yds",
    "yds",
)

METRE_ALIASES = (
    "Metre",
    "metre",
    "Metres",
    "metres",
    "M",
    "m",
    "Ms",
    "ms",
)

CM_ALIASES = (
    "Centimeter",
    "centimeter",
    "Centimeters",
    "centimeters",
    "CM",
    "cm",
    "CMs",
    "cms",
)


DistanceUnits = SimpleNamespace(
    yard = YARD_ALIASES,
    metre = METRE_ALIASES,
    cm = CM_ALIASES,
)
