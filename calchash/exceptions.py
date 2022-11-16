__all__: list[str] = [
    'FileEmptyError',
    'FileRelatedError',
]


class FileEmptyError(OSError):
    """Raise when a file has a size of 0kb."""

    ...


class FileRelatedError(OSError):
    """Raise exception related to files in general."""

    ...
