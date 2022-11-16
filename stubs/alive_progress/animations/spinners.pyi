from ..utils.cells import combine_cells as combine_cells, fix_cells as fix_cells, has_wide as has_wide, mark_graphemes as mark_graphemes, strip_marks as strip_marks, to_cells as to_cells
from .spinner_compiler import spinner_controller as spinner_controller
from .utils import combinations as combinations, overlay_sliding_window as overlay_sliding_window, round_even as round_even, spinner_player as spinner_player, split_options as split_options, spread_weighted as spread_weighted, static_sliding_window as static_sliding_window
from _typeshed import Incomplete

def frame_spinner_factory(*frames): ...
def scrolling_spinner_factory(chars, length: Incomplete | None = ..., block: Incomplete | None = ..., background: Incomplete | None = ..., *, right: bool = ..., hide: bool = ..., wrap: bool = ..., overlay: bool = ...): ...
def bouncing_spinner_factory(chars, length: Incomplete | None = ..., block: Incomplete | None = ..., background: Incomplete | None = ..., *, right: bool = ..., hide: bool = ..., overlay: bool = ...): ...
def sequential_spinner_factory(*spinner_factories, intermix: bool = ...): ...
def alongside_spinner_factory(*spinner_factories, pivot: Incomplete | None = ...): ...
def delayed_spinner_factory(spinner_factory, copies, offset: int = ..., *, dynamic: bool = ...): ...
