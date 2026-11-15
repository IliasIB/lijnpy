from enum import Enum


class Accessibility(Enum):
    MOTOR_DISABILITY = "MOTORISCHE_BEPERKING"
    VISUAL_DISABILITY = "VISUELE_BEPERKING"
    MOTOR_WITH_ASSIST = "MOTORISCH_MET_ASSIST"


class OperationType(Enum):
    NIGHT = "NACHTLIJN"
    FACTORY = "FABRIEKSLIJN"
    NORMAL = "NORMAAL"
    EXPRESS = "SNELDIENST"
    SCHOOL = "SCHOOLBUS"


class TransportType(Enum):
    TRAM = "TRAM"
    BUS = "BUS"


class Language(Enum):
    DUTCH = "NEDERLANDS"
    FRENCH = "FRANS"
    BILINGUAL = "TWEETALIG"
    UNKNOWN = "?"


class LineDirection(Enum):
    TO = "HEEN"
    FROM = "TERUG"
