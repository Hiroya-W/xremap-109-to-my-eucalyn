from typing import Dict
from xremap.dsl import define_keymap  # noqa
from myxremap.types import Key, KeyMapping, KeyMap
from myxremap.keys import PREFIXES


def key2str(key: Key) -> str:
    if key.modifiers == ["None"]:
        return key.key
    else:
        return "-".join(key.modifiers) + "-" + key.key


TO_EUCALYN = KeyMap(
    [
        KeyMapping(Key("Q"), Key("Q")),
        KeyMapping(Key("E"), Key("Comma")),
        KeyMapping(Key("R"), Key("Dot")),
        KeyMapping(Key("T"), Key("Semicolon")),
        KeyMapping(Key("Y"), Key("M")),
        KeyMapping(Key("U"), Key("R")),
        KeyMapping(Key("I"), Key("D")),
        KeyMapping(Key("O"), Key("Y")),
        KeyMapping(Key("P"), Key("P")),
        KeyMapping(Key("A"), Key("A")),
        KeyMapping(Key("S"), Key("O")),
        KeyMapping(Key("D"), Key("E")),
        KeyMapping(Key("F"), Key("I")),
        KeyMapping(Key("G"), Key("U")),
        KeyMapping(Key("H"), Key("G")),
        KeyMapping(Key("J"), Key("T")),
        KeyMapping(Key("K"), Key("K")),
        KeyMapping(Key("L"), Key("S")),
        KeyMapping(Key("Semicolon"), Key("N")),
        KeyMapping(Key("Z"), Key("Z")),
        KeyMapping(Key("X"), Key("X")),
        KeyMapping(Key("C"), Key("C")),
        KeyMapping(Key("V"), Key("V")),
        KeyMapping(Key("B"), Key("F")),
        KeyMapping(Key("N"), Key("B")),
        KeyMapping(Key("M"), Key("H")),
        KeyMapping(Key("Comma"), Key("J")),
        KeyMapping(Key("Dot"), Key("L")),
    ]
)

TO_EUCALYN_WITH_MODIFIERS = KeyMap([])

for mapping in TO_EUCALYN:
    for prefix in PREFIXES:
        from_ = Key(mapping.from_.key, prefix)
        to = Key(mapping.to.key, prefix)
        TO_EUCALYN_WITH_MODIFIERS.append(KeyMapping(from_, to))


GLOBAL_KEYMAP: Dict[str, str] = {}

for mapping in TO_EUCALYN_WITH_MODIFIERS:
    GLOBAL_KEYMAP[key2str(mapping.from_)] = key2str(mapping.to)

define_keymap({}, GLOBAL_KEYMAP, "Global")
