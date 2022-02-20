from abc import ABC, abstractmethod
from typing import Any, Dict, List

from typing_extensions import TypeAlias

from myxremap.common.exceptions import InvalidKeySwapArgumentException
from myxremap.key import ALL_PREFIXES, Key, Modifier

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
