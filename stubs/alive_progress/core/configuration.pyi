from ..utils.terminal import FULL as FULL, NON_TTY as NON_TTY
from _typeshed import Incomplete
from typing import NamedTuple, Any

ERROR: Incomplete

class Config(NamedTuple):
    title: Incomplete
    length: Incomplete
    spinner: Incomplete
    bar: Incomplete
    unknown: Incomplete
    force_tty: Incomplete
    disable: Incomplete
    manual: Incomplete
    enrich_print: Incomplete
    receipt: Incomplete
    receipt_text: Incomplete
    monitor: Incomplete
    elapsed: Incomplete
    stats: Incomplete
    title_length: Incomplete
    spinner_length: Incomplete
    refresh_secs: Incomplete
    monitor_end: Incomplete
    elapsed_end: Incomplete
    stats_end: Incomplete
    ctrl_c: Incomplete
    dual_line: Incomplete

def create_config() -> Any: ...

config_handler: Incomplete
