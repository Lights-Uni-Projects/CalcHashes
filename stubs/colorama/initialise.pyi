import typing
from collections.abc import Generator

from _typeshed import Incomplete

from .ansitowin32 import AnsiToWin32 as AnsiToWin32


def reset_all() -> None: ...
def init(autoreset: bool = ..., convert: Incomplete | None = ...,
         strip: Incomplete | None = ..., wrap: bool = ...) -> None: ...


def deinit() -> None: ...
def just_fix_windows_console() -> None: ...
def colorama_text(*args: typing.Any, **kwargs: typing.Any) -> Generator[None, None, None]: ...
def reinit() -> None: ...


def wrap_stream(stream: typing.Any, convert: typing.Any, strip: typing.Any,
                autoreset: typing.Any, wrap: typing.Any) -> typing.Any: ...
