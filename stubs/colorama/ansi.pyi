import typing

from _typeshed import Incomplete

CSI: str
OSC: str
BEL: str


def code_to_chars(code: typing.Any) -> typing.Any: ...
def set_title(title: typing.Any) -> typing.Any: ...
def clear_screen(mode: int = ...) -> typing.Any: ...
def clear_line(mode: int = ...) -> typing.Any: ...


class AnsiCodes:
    def __init__(self) -> None: ...


class AnsiCursor:
    def UP(self, n: int = ...) -> typing.Any: ...
    def DOWN(self, n: int = ...) -> typing.Any: ...
    def FORWARD(self, n: int = ...) -> typing.Any: ...
    def BACK(self, n: int = ...) -> typing.Any: ...
    def POS(self, x: int = ..., y: int = ...) -> typing.Any: ...


class AnsiFore(AnsiCodes):
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    WHITE: int
    RESET: int
    LIGHTBLACK_EX: int
    LIGHTRED_EX: int
    LIGHTGREEN_EX: int
    LIGHTYELLOW_EX: int
    LIGHTBLUE_EX: int
    LIGHTMAGENTA_EX: int
    LIGHTCYAN_EX: int
    LIGHTWHITE_EX: int


class AnsiBack(AnsiCodes):
    BLACK: int
    RED: int
    GREEN: int
    YELLOW: int
    BLUE: int
    MAGENTA: int
    CYAN: int
    WHITE: int
    RESET: int
    LIGHTBLACK_EX: int
    LIGHTRED_EX: int
    LIGHTGREEN_EX: int
    LIGHTYELLOW_EX: int
    LIGHTBLUE_EX: int
    LIGHTMAGENTA_EX: int
    LIGHTCYAN_EX: int
    LIGHTWHITE_EX: int


class AnsiStyle(AnsiCodes):
    BRIGHT: int
    DIM: int
    NORMAL: int
    RESET_ALL: int


Fore: Incomplete
Back: Incomplete
Style: Incomplete
Cursor: Incomplete
