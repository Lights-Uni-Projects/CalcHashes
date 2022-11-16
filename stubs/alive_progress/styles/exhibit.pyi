from ..animations.spinners import scrolling_spinner_factory as scrolling_spinner_factory, sequential_spinner_factory as sequential_spinner_factory
from ..animations.utils import spinner_player as spinner_player
from ..core.configuration import config_handler as config_handler
from ..utils.cells import combine_cells as combine_cells, print_cells as print_cells
from ..utils.terminal import FULL as FULL
from .internal import BARS as BARS, SPINNERS as SPINNERS, THEMES as THEMES
from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

Show: Incomplete

def showtime(show=..., *, fps: Incomplete | None = ..., length: Incomplete | None = ..., pattern: Incomplete | None = ...) -> None: ...

class Info(NamedTuple):
    title: Incomplete
    descr: Incomplete
    tech: Incomplete

def show_spinners(*, fps: Incomplete | None = ..., length: Incomplete | None = ..., pattern: Incomplete | None = ...) -> None: ...
def show_bars(*, fps: Incomplete | None = ..., length: Incomplete | None = ..., pattern: Incomplete | None = ...) -> None: ...
def show_themes(*, fps: Incomplete | None = ..., length: Incomplete | None = ..., pattern: Incomplete | None = ...) -> None: ...
def exhibit_spinner(spinner) -> Generator[Incomplete, None, None]: ...
def exhibit_bar(bar, fps) -> Generator[Incomplete, None, Incomplete]: ...
