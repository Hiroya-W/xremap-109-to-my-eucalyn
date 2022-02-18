from typing import List
import itertools

MODIFIERS: List[str] = ["Shift", "Alt", "Ctrl", "Super"]

PREFIXES: List[List[str]] = [
    ["None"],
    *[[mod] for mod in MODIFIERS],
    *[[*mod] for mod in list(itertools.combinations(MODIFIERS, 2))],
    *[[*mod] for mod in list(itertools.combinations(MODIFIERS, 3))],
    *[[*mod] for mod in list(itertools.combinations(MODIFIERS, 4))],
]
