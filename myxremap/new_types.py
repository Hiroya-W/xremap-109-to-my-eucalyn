from typing import Dict, NamedTuple, NewType

from myxremap.new_keys import Modifier


class Key(NamedTuple):
    key: str
    modifiers: Modifier = Modifier.NONE


KeyMap = NewType("KeyMap", Dict[Key, Dict[Modifier, Key]])
