from myxremap.types import Key


def key2str(key: Key) -> str:
    if key.modifiers == ["None"]:
        return key.key
    else:
        return "-".join(key.modifiers) + "-" + key.key
