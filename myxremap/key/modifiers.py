import itertools
from enum import Flag, auto
from typing import List


class Modifier(Flag):
    NONE = 0
    CTRL = auto()
    ALT = auto()
    SHIFT = auto()
    SUPER = auto()


__MODIFIER_LIST = list(Modifier)[1:]

ALL_PREFIXES: List[Modifier] = []

for bits in itertools.product([0, 1], repeat=len(__MODIFIER_LIST)):
    prefix = Modifier.NONE
    for modifier, bit in zip(__MODIFIER_LIST, bits):
        if bit == 1:
            prefix |= modifier
    ALL_PREFIXES.append(prefix)
