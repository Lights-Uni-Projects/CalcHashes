from ..utils.cells import VS_15 as VS_15, combine_cells as combine_cells, fix_cells as fix_cells, has_wide as has_wide, is_wide as is_wide, join_cells as join_cells, mark_graphemes as mark_graphemes, split_graphemes as split_graphemes, strip_marks as strip_marks, to_cells as to_cells
from ..utils.colors import BLUE as BLUE, BLUE_BOLD as BLUE_BOLD, CYAN as CYAN, DIM as DIM, GREEN as GREEN, ORANGE as ORANGE, ORANGE_BOLD as ORANGE_BOLD, RED as RED, YELLOW_BOLD as YELLOW_BOLD
from ..utils.terminal import FULL as FULL
from .utils import bordered as bordered, extract_fill_graphemes as extract_fill_graphemes, fix_signature as fix_signature, spinner_player as spinner_player
from _typeshed import Incomplete

def bar_factory(chars: Incomplete | None = ..., *, tip: Incomplete | None = ..., background: Incomplete | None = ..., borders: Incomplete | None = ..., errors: Incomplete | None = ...): ...
def bar_controller(inner_bar_factory): ...
def check(bar, t_compile, verbosity: int = ..., *, steps: int = ...) -> None: ...
SECTION = ORANGE_BOLD
CHECK: Incomplete
HELP_MSG: Incomplete

def spec_data(bar): ...
def format_codepoints(frame): ...
def render_data(bar, show_codepoints, steps): ...
def bar_repr(bar, p): ...
def animate(bar) -> None: ...