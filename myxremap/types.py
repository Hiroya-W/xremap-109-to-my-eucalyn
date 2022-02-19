from typing import List, NamedTuple, NewType

from myxremap.keys import MODIFIERS


class Key(NamedTuple):
    key: str
    modifiers: MODIFIERS = []


class KeyMapping(NamedTuple):
    from_: Key
    to: Key


KeyMap = NewType("KeyMap", List[KeyMapping])
