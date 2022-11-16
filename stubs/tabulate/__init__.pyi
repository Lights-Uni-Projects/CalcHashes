import textwrap
from _typeshed import Incomplete
from typing import NamedTuple, Any


class Line(NamedTuple):
    begin: Incomplete
    hline: Incomplete
    sep: Incomplete
    end: Incomplete


class DataRow(NamedTuple):
    begin: Incomplete
    sep: Incomplete
    end: Incomplete


class TableFormat(NamedTuple):
    lineabove: Incomplete
    linebelowheader: Incomplete
    linebetweenrows: Incomplete
    linebelow: Incomplete
    headerrow: Incomplete
    datarow: Incomplete
    padding: Incomplete
    with_header_hide: Incomplete


tabulate_formats: Incomplete


def simple_separated_format(separator: Any) -> Any: ...


def tabulate(tabular_data: Any, headers: Any = ..., tablefmt: str = ..., floatfmt: Any = ..., intfmt: Any = ...,
             numalign: Any = ..., stralign: Any = ...,
             missingval: Any = ..., showindex: str = ..., disable_numparse: bool = ...,
             colalign: Incomplete | None = ..., maxcolwidths: Incomplete | None = ..., rowalign: Incomplete | None = ...,
             maxheadercolwidths: Incomplete | None = ...) -> Any: ...


class JupyterHTMLStr(str):
    @property
    def str(self) -> Any: ...


class _CustomTextWrap(textwrap.TextWrapper):
    max_lines: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
