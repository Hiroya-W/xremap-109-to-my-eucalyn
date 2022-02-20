from typing import Any, Dict
from typing_extensions import TypeAlias
from abc import ABC, abstractmethod

from myxremap.new_keys import Modifier, ALL_PREFIXES
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


MappingTo: TypeAlias = Dict[Modifier, Key]
KeyMapping: TypeAlias = Dict[Key, MappingTo]


class KeyMapBase(ABC):
    @abstractmethod
    def get_key_map(self) -> KeyMapping:
        pass

    @abstractmethod
    def dump(self) -> Dict[str, Any]:
        raise NotImplementedError


class KeySwap(KeyMapBase):
    def __init__(self, from_: Key, to: Key):
        if from_.modifiers != Modifier.NONE:
            raise InvalidKeySwapArgumentException(
                from_, "The key of the swap source must be Modifier.NONE."
            )
        if to.modifiers != Modifier.NONE:
            raise InvalidKeySwapArgumentException(
                to, "The key of the swap target must be Modifier.NONE."
            )

        self.key_map: KeyMapping = {}
        self._create_mapping_to_all_modifiers(from_, to)

    def get_key_map(self) -> KeyMapping:
        return self.key_map

    def dump(self) -> Dict[str, Any]:
        raise NotImplementedError

    def _create_mapping_to_all_modifiers(self, from_: Key, to: Key) -> None:
        mapping_to = {}
        for prefix in ALL_PREFIXES:
            mapping_to[prefix] = to
        self.key_map[from_] = mapping_to


class KeyMap(KeyMapBase):
    def __init__(self, key_map: KeyMapping = {}):
        self.key_map = key_map

    def __getitem__(self, key: Key) -> MappingTo:
        return self.key_map[key]

    def __setitem__(self, key: Key, value: MappingTo) -> None:
        self.key_map[key] = value

    def get_key_map(self) -> KeyMapping:
        return self.key_map

    def dump(self) -> Dict[str, Any]:
        raise NotImplementedError

    def extend(self, key_map: KeyMapBase) -> None:
        self.key_map.update(key_map.get_key_map())
