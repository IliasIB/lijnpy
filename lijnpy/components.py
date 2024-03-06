from enum import Enum


class Bedieningtype(Enum):
    BELBUS = 0
    FABRIEKSLIJN = 1
    NACHTLIJN = 2
    NORMAAL = 3
    SCHOOLBUS = 4
    SNELDIENST = 5
    TECHNISCHE_LIJN = 6


class Gemeente:
    def __init__(self, nummer: int, omschrijving: str):
        self.nummer = nummer
        self.omschrijving = omschrijving
