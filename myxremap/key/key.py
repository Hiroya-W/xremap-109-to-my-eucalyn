from myxremap.key.modifiers import Modifier


class Key:
    def __init__(self, key: str, modifiers: Modifier = Modifier.NONE):
        self.key = key
        self.modifiers = modifiers

    def __str__(self) -> str:
        if self.modifiers == Modifier.NONE:
            return self.key

        prefixes = []
        if self.modifiers & Modifier.CTRL:
            prefixes.append("Ctrl")
        if self.modifiers & Modifier.ALT:
            prefixes.append("Alt")
        if self.modifiers & Modifier.SHIFT:
            prefixes.append("Shift")
        if self.modifiers & Modifier.SUPER:
            prefixes.append("Super")

        return "-".join(prefixes) + "-" + self.key
