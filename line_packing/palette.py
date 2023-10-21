from enum import Enum

class Earthy(Enum):
    ROSE_TAUPE = (125, 97, 103)
    SAGE = (177, 182, 149)
    LION = (190, 149, 122)
    PINE_GREEN = (21, 122, 110)
    DARK_MOSS_GREEN = (71, 104, 44)


class Bright(Enum):
    AUREOLIN = (244,228, 9)
    IMPERIAL_RED = (240, 58, 71)
    EMERALD = (12, 206, 107)
    BYZANTIUM = (130, 2, 99)
    LAVENDER_PINK = (255, 196, 235)

    
EARTHY = [color.value for color in Earthy]
BRIGHT = [color.value for color in Bright]