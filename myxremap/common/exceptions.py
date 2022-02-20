from myxremap.key import Key


class XremapException(Exception):
    def __init__(self, msg: str = "") -> None:
        self.msg = msg


class InvalidKeySwapArgumentException(XremapException):
    def __init__(self, key: Key, msg: str = "") -> None:
        super().__init__(msg)
        self.key = key

    def __str__(self) -> str:
        exception_msg = "InvalidKeySwapArgumentException: \n"
        exception_msg += "  " + self.msg + "\n"
        exception_msg += "  " + str(self.key) + "\n"
        return exception_msg
