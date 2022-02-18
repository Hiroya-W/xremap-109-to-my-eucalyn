from typing import List, NamedTuple, NewType


class Key(NamedTuple):
    key: str
    modifiers: List[str] = ["None"]


class KeyMapping(NamedTuple):
    from_: Key
    to: Key


KeyMap = NewType("KeyMap", List[KeyMapping])
