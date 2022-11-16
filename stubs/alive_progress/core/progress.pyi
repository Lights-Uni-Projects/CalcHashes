from ..utils import terminal as terminal
from ..utils.cells import combine_cells as combine_cells, fix_cells as fix_cells, print_cells as print_cells, to_cells as to_cells
from ..utils.timing import elapsed_text as elapsed_text, eta_text as eta_text, gen_simple_exponential_smoothing_eta as gen_simple_exponential_smoothing_eta
from .calibration import calibrated_fps as calibrated_fps, custom_fps as custom_fps
from .configuration import config_handler as config_handler
from .hook_manager import buffered_hook_manager as buffered_hook_manager, passthrough_hook_manager as passthrough_hook_manager
from _typeshed import Incomplete
from typing import Any


def alive_bar(total: Incomplete | None = ..., *, calibrate: Incomplete | None = ..., **options: Any) -> Any: ...


class _Widget:
    func: Incomplete
    f: Incomplete
    def __init__(self, func: Any, value: Any, default: Any) -> None: ...
    def __call__(self) -> Any: ...


class _GatedProperty:
    prop: Incomplete
    def __set_name__(self, owner: Any, name: Any) -> None: ...
    def __get__(self, obj: Any, objtype: Incomplete | None = ...) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...


class _GatedAssignProperty(_GatedProperty):
    def __set__(self, obj: Any, value: Any) -> None: ...


class __AliveBarHandle:
    pause: Incomplete
    current: Incomplete
    text: Incomplete
    title: Incomplete
    def __init__(self, pause: Any, get_current: Any, set_title: Any, set_text: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...


def alive_it(it: Any, total: Incomplete | None = ..., *, finalize: Incomplete
             | None = ..., calibrate: Incomplete | None = ..., **options: Any) -> Any: ...


class __AliveBarIteratorAdapter:
    def __init__(self, it: Any, finalize: Any, inner_bar: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, item: Any) -> Any: ...
    def __setattr__(self, key: Any, value: Any) -> Any: ...
