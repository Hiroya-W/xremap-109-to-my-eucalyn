from enum import IntFlag, auto


class Modifier(IntFlag):
    NONE = 0
    CTRL = auto()
    ALT = auto()
    SHIFT = auto()
    SUPER = auto()
