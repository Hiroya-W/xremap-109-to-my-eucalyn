from enum import IntFlag, auto


class Modifier(IntFlag):
    CTRL = auto()
    ALT = auto()
    SHIFT = auto()
    SUPER = auto()
