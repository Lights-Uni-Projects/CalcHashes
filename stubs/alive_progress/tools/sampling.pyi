from ..core.configuration import config_handler as config_handler
from .utils import toolkit as toolkit
from _typeshed import Incomplete

def overhead(total: Incomplete | None = ..., *, calibrate: Incomplete | None = ..., **options): ...

OVERHEAD_SAMPLING_GROUP: Incomplete
OVERHEAD_SAMPLING: Incomplete

def overhead_sampling() -> None: ...

class __lock:
    def __enter__(self) -> None: ...
    def __exit__(self, _type, value, traceback) -> None: ...
