from typing import Any, Dict, List
from typing_extensions import TypeAlias
from abc import ABC, abstractmethod

from myxremap.keys import Modifier, ALL_PREFIXES
from myxremap.exceptions import InvalidKeySwapArgumentException


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


KeyMapping: TypeAlias = Dict[Key, Key]


class KeyMapBase(ABC):
    def __init__(self) -> None:
        self.key_map: KeyMapping = {}

    def get_key_map(self) -> KeyMapping:
        return self.key_map

    @abstractmethod
    def dump(self) -> Dict[str, Any]:
        raise NotImplementedError


class KeySwap(KeyMapBase):
    def __init__(self, from_: Key, to: Key):
        super().__init__()
        if from_.modifiers != Modifier.NONE:
            raise InvalidKeySwapArgumentException(
                from_, "The key of the swap source must be Modifier.NONE."
            )
        if to.modifiers != Modifier.NONE:
            raise InvalidKeySwapArgumentException(
                to, "The key of the swap target must be Modifier.NONE."
            )

        self._create_mapping_to_all_modifiers(from_, to)

    def dump(self) -> Dict[str, Any]:
        res: Dict[str, str] = {}
        for from_, to in self.key_map.items():
            res[str(from_)] = str(to)
        return res

    def _create_mapping_to_all_modifiers(self, from_: Key, to: Key) -> None:
        for prefix in ALL_PREFIXES:
            from_with_prefix = Key(from_.key, prefix)
            to_with_prefix = Key(to.key, prefix)
            self.key_map[from_with_prefix] = to_with_prefix


class KeyMap(KeyMapBase):
    def __init__(self, key_map: KeyMapping = {}):
        super().__init__()
        self.key_map = key_map

    def __getitem__(self, key: Key) -> Key:
        return self.key_map[key]

    def __setitem__(self, key: Key, value: Key) -> None:
        self.key_map[key] = value

    def dump(self) -> Dict[str, Any]:
        res: Dict[str, str] = {}
        for from_, to in self.key_map.items():
            res[str(from_)] = str(to)
        return res

    def extend(self, key_maps: List[KeyMapBase]) -> None:
        for key_map in key_maps:
            self.key_map.update(key_map.get_key_map())
