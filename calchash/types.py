import binascii
import hashlib
import os
from enum import Enum
from pathlib import Path

from colorama import Fore

from .exceptions import FileEmptyError

__all__: list[str] = [
    "FilePath",
    "HashingAlgorithm",
    "match_n", "match_y",
    "Hasher",
    "hash_table",
]

match_y = f"{Fore.LIGHTGREEN_EX}Match found!{Fore.RESET}"
match_n = f"{Fore.RED}No match!{Fore.RESET}"

# Type indicating a path to a file.
FilePath = str | os.PathLike | Path


class Hasher:
    """Hasher class containing different hashing algorithms."""

    file: Path
    data: bytes

    def __init__(self, file: FilePath) -> None:
        """
        Interface for running multiple hashing algos over a given file.

        :param file:                    Input file.

        :raises FileNotFoundError:      Input file could not be found or is a directory.
        :raises FileEmptyError:         Input file is empty.
        """
        file = Path(file)

        if not any([file.exists(), file.is_file()]):
            raise FileNotFoundError(file)

        if file.stat().st_size == 0:
            raise FileEmptyError(file)

        self.file = file

        with open(file, 'rb') as f:
            self.data = f.read()

    def crc32(self) -> str:
        """Compute and returns a Cyclic Redundancy Check (CRC) checksum, 32bit unsigned."""
        return "%08X" % (binascii.crc32(self.data) & 0xFFFFFFFF)

    def md5(self) -> str:
        """Compute and returns a message-digest algorithm (MD5) checksum."""
        return hashlib.md5(self.data).hexdigest()

    def sha256(self) -> str:
        """Compute and returns Secure Hash Algorithm 2 (SHA-2) checksum, 32bit (SHA-256)."""
        return hashlib.sha256(self.data).hexdigest()


class HashingAlgorithm(str, Enum):
    """Enum representing a hashing algorithm."""

    CRC32 = "crc32"
    MD5 = "md5"
    SHA256 = "sha256"
    ALL = "all"

    def get_hash(self, hasher: str | FilePath | Hasher) -> str:
        if isinstance(hasher, (str, FilePath)):
            hasher = Hasher(hasher)

        if self is self.CRC32:
            return hasher.crc32()

        if self is self.MD5:
            return hasher.md5()

        if self is self.SHA256:
            return hasher.sha256()

        raise NotImplementedError


# Different hash search strings table
hash_table: dict[HashingAlgorithm, str] = {
    HashingAlgorithm.CRC32: r"\s?\[[0-9a-fA-F]{8}\]",
    HashingAlgorithm.MD5: r"\s?\[[a-fA-F]{32}\]",
    HashingAlgorithm.SHA256: r"\s?\[[A-Fa-f0-9]{64}\]",
}
