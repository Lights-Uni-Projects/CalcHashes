from .. import alive_bar as alive_bar
from ..styles import BARS as BARS
from ..utils.colors import BOLD as BOLD, ORANGE_IT as ORANGE_IT
from .sampling import OVERHEAD_SAMPLING as OVERHEAD_SAMPLING
from .utils import toolkit as toolkit
from _typeshed import Incomplete
from typing import NamedTuple

class Case(NamedTuple):
    name: str
    count: int
    config: dict
    done: bool
    hooks: bool
    title: str

def title(text) -> None: ...

cases: Incomplete
features: Incomplete

def demo(sleep: Incomplete | None = ...) -> None: ...
