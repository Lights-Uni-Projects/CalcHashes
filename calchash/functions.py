import os
import re
from itertools import zip_longest
from typing import Any

from colorama import Fore
from tabulate import tabulate

from .types import FilePath, HashingAlgorithm, add_hash_response, hash_table, match_n, match_y

__all__: list[str] = [
    "check_file",
    "construct_table",
    "gather_data",
]


def check_file(file: FilePath, algo: HashingAlgorithm, add_hash: bool = False) -> dict[str, str]:
    """
    Check file for matching hash and other such information.

    :param file:        Path to input file.
    :param algo:        Hashing algorithm to verify.
    :param add_hash:    Whether to add the hash to the filename or not.
                        Will replace any existing hashes it can find.

    :return:            Dictionary with the following keys:
                        {file, algo found, algo calculated, match, diff, notes}

    :raises ValueError: `ALL` is passed to `algo`.
    """
    # TODO: add a recursive run that works
    if algo is HashingAlgorithm.ALL:
        raise ValueError(f"\"{algo}\" is currently not supported!")

    file = str(file)
    notes = ""

    hash_in_file: Any = re.search(hash_table[algo], file)

    if not hash_in_file:
        notes += f"No {algo.value} hash found! "
    else:
        hash_in_file = re.sub(r"[\]\[]", "", hash_in_file.group(0)).strip()

    hash_of_file = algo.get_hash(file)

    if add_hash:
        success = add_hash_to_filename(file, algo, hash_of_file)
        notes += add_hash_response[success]

    return {
        'File': f"{Fore.CYAN}{file[:64]}{'...' if len(file) > 64 else ''}{Fore.RESET}",  # This is immensely cursed fyi
        f'{algo.value.upper()} found': f"{Fore.MAGENTA if hash_in_file else Fore.RED}{hash_in_file}{Fore.RESET}",
        f'{algo.value.upper()} calculated': f"{Fore.LIGHTMAGENTA_EX}{hash_of_file}{Fore.RESET}",
        'Match': match_y if hash_in_file == hash_of_file else match_n,
        'Diff': "".join([f"{Fore.LIGHTGREEN_EX if x is y else Fore.RED}{x}{Fore.RESET}" for x, y in
                         zip_longest(list(hash_in_file or "X" * len(hash_of_file)), list(hash_of_file))]),
        'Notes': notes
    }


def add_hash_to_filename(file: str, algo: HashingAlgorithm, hash: str) -> int:
    """
    Try adding the hash to the filename.

    :param file:    Path to input file.
    :param algo:    Hashing algorithm.
    :param hash:    Pre-calculated hash.

    :return:        Integer signifying a `note`.
    """
    try:
        if re.search(hash, file):
            return 3

        if re.search(hash_table[algo], file):
            os.rename(file, re.sub(hash_table[algo], f" [{hash}]", file))
            return 2

        str_f = re.sub(hash_table[algo], '', file)
        os.rename(str_f, f'{os.path.splitext(str_f)[0]} [{hash}]{os.path.splitext(str_f)[1]}')

        return 1
    except Exception:
        return 0


def construct_table(results: list[dict[str, str]]) -> str:
    """Construct a table using tabulate."""
    return str(tabulate([x.values() for x in results], results[0].keys(), tablefmt="pretty"))


def gather_data(results: list[dict[str, str]]) -> str:
    """Gather basic statistics printed at the end of the process."""
    # Multi-line comments aren't working with me and idk why...
    data = f"Files checked: {Fore.LIGHTBLUE_EX}{len(results)}{Fore.RESET}, "
    data += f"matches: {Fore.GREEN}{len([item for item in results if item['Match'] == match_y])}{Fore.RESET}/"
    data += f"{Fore.RED}{len(results)}{Fore.RESET}..."

    return data
