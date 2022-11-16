"""Hashing algorithms."""
import binascii
import hashlib
from pathlib import Path

from .exceptions import FileEmptyError
from .types import FilePath, HashingAlgorithm

__all__: list[str] = [
    "Hasher",
    "hash_table",
]


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

    def get_hash(self, algo: HashingAlgorithm = HashingAlgorithm.CRC32) -> str:
        """Run a hashing algorithm based on the given algo if available."""
        if algo is HashingAlgorithm.ALL:
            raise ValueError("Cannot run \"HashingAlgorithm.ALL\"!")

        return str(getattr(self, algo.value.lower())())

    def crc32(self) -> str:
        """Compute and returns a Cyclic Redundancy Check (CRC) checksum, 32bit unsigned."""
        return "%08X" % (binascii.crc32(self.data) & 0xFFFFFFFF)

    def md5(self) -> str:
        """Compute and returns a message-digest algorithm (MD5) checksum."""
        return hashlib.md5(self.data).hexdigest()

    def sha256(self) -> str:
        """Compute and returns Secure Hash Algorithm 2 (SHA-2) checksum, 32bit (SHA-256)."""
        return hashlib.sha256(self.data).hexdigest()


# Different hash search strings table
hash_table: dict[HashingAlgorithm, str] = {
    HashingAlgorithm.CRC32: r"\s?\[[0-9a-fA-F]{8}\]",
    HashingAlgorithm.MD5: r"\s?\[[a-fA-F]{32}\]",
    HashingAlgorithm.SHA256: r"\s?\[[A-Fa-f0-9]{64}\]",
}
