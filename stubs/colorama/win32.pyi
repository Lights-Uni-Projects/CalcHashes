from _typeshed import Incomplete
from ctypes import Structure
import typing

STDOUT: int
STDERR: int
ENABLE_VIRTUAL_TERMINAL_PROCESSING: int
windll: Incomplete
SetConsoleTextAttribute: Incomplete
winapi_test: Incomplete
COORD: Incomplete


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    ...


def GetConsoleScreenBufferInfo(stream_id: typing.Any = ...) -> typing.Any: ...
def SetConsoleCursorPosition(stream_id: typing.Any, position: typing.Any, adjust: bool = ...) -> typing.Any: ...


def FillConsoleOutputCharacter(stream_id: typing.Any, char: typing.Any,
                               length: typing.Any, start: typing.Any) -> typing.Any: ...
def FillConsoleOutputAttribute(stream_id: typing.Any, attr: typing.Any,
                               length: typing.Any, start: typing.Any) -> typing.Any: ...


def SetConsoleTitle(title: typing.Any) -> typing.Any: ...
def GetConsoleMode(handle: typing.Any) -> typing.Any: ...
def SetConsoleMode(handle: typing.Any, mode: typing.Any) -> None: ...
