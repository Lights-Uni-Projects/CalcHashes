from pathlib import Path
import os
from enum import Enum
from colorama import Fore

__all__: list[str] = [
    'FilePath',
    'HashingAlgorithm',
    'match_n', 'match_y',
]

match_y = f"{Fore.LIGHTGREEN_EX}Match found!{Fore.RESET}"
match_n = f"{Fore.RED}No match!{Fore.RESET}"


class HashingAlgorithm(str, Enum):
    """Enum representing a hashing algorithm."""

    CRC32 = "crc32"
    MD5 = "md5"
    SHA256 = "sha256"
    ALL = "all"


# Type indicating a path to a file.
FilePath = str | os.PathLike | Path
