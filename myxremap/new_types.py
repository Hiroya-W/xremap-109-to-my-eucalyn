from typing import Dict, NewType

from myxremap.new_keys import Modifier


class Key:
    def __init__(self, key: str, modifiers: Modifier = Modifier.NONE):
        self.key = key
        self.modifiers = modifiers

    def __str__(self) -> str:
        if self.modifiers == Modifier.NONE:
            return self.key

        prefixes = []
        if self.modifiers == Modifier.CTRL:
            prefixes.append("CTRL")
        if self.modifiers == Modifier.ALT:
            prefixes.append("ALT")
        if self.modifiers == Modifier.SHIFT:
            prefixes.append("SHIFT")
        if self.modifiers == Modifier.SUPER:
            prefixes.append("SUPER")

        return "-".join(prefixes) + "-" + self.key


KeyMap = NewType("KeyMap", Dict[Key, Dict[Modifier, Key]])
