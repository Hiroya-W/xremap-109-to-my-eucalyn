from enum import Flag, auto
import itertools
from typing import List


class Modifier(Flag):
    NONE = 0
    CTRL = auto()
    ALT = auto()
    SHIFT = auto()
    SUPER = auto()


_MODIFIER_LIST = list(Modifier)[1:]

ALL_PREFIXES: List[Modifier] = [Modifier.NONE]

for n in range(1, len(_MODIFIER_LIST) + 1):
    for combination in itertools.combinations(_MODIFIER_LIST, n):
        prefix = Modifier.NONE
        for mod in combination:
            prefix |= mod
        ALL_PREFIXES.append(prefix)
