import re
from typing import Any

from colorama import Fore
from tabulate import tabulate

from .algos import Hasher, hash_table
from .types import FilePath, HashingAlgorithm, match_n, match_y


def check_file(file: FilePath, algo: HashingAlgorithm) -> dict[str, str]:
    """Check file for matching hash and other such information."""
    # TODO: add a recursive run that works
    if algo is HashingAlgorithm.ALL:
        for hash in hash_table:
            check_file(file, hash)

    file = str(file)
    notes = ""

    hash_in_file: Any = re.search(hash_table[algo], file)

    if not hash_in_file:
        notes = f"Could not find {algo.value} hash in file!"
    else:
        hash_in_file = re.sub(r"[\]\[]", "", hash_in_file.group(0)).strip()

    hash_obj = Hasher(file)
    hash_of_file = hash_obj.get_hash(algo)

    return {
        'File': f"{Fore.CYAN}{file[:64]}{Fore.RESET}",
        f'{algo.value.upper()} found': f"{Fore.MAGENTA if hash_in_file else Fore.RED}{hash_in_file}{Fore.RESET}",
        f'{algo.value.upper()} calculated': f"{Fore.LIGHTMAGENTA_EX}{hash_of_file}{Fore.RESET}",
        'Match': match_y if hash_in_file == hash_of_file else match_n,
        'Diff': "".join([f"{Fore.LIGHTGREEN_EX if x is y else Fore.RED}{x}{Fore.RESET}" for x, y in
                         zip(list(hash_in_file or "X" * len(hash_of_file)), list(hash_of_file))]),
        'Notes': notes
    }


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
