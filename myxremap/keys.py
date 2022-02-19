from typing import List
from typing_extensions import Literal, TypeAlias
import itertools

MODIFIER = Literal["Shift", "Alt", "Ctrl", "Super"]
MODIFIERS: TypeAlias = List[MODIFIER]
MODS: MODIFIERS = ["Shift", "Alt", "Ctrl", "Super"]

PREFIXES: List[MODIFIERS] = [
    [],
    *[[mod] for mod in MODS],
    *[[*mod] for mod in list(itertools.combinations(MODS, 2))],
    *[[*mod] for mod in list(itertools.combinations(MODS, 3))],
    *[[*mod] for mod in list(itertools.combinations(MODS, 4))],
]
