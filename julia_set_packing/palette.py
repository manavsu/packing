from enum import Enum

class Earthy(Enum):
    ROSE_TAUPE = (125, 97, 103)
    SAGE = (177, 182, 149)
    LION = (190, 149, 122)
    PINE_GREEN = (21, 122, 110)
    DARK_MOSS_GREEN = (71, 104, 44)

EARTHY = [color.value for color in Earthy]