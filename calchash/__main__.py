import argparse
from glob import glob

from .algos import Hasher
from .exceptions import FileEmptyError
from .types import HashingAlgorithm
from .functions import check_file, construct_table, gather_data

try:
    from colorama import Fore, init
except ModuleNotFoundError:
    raise ModuleNotFoundError("Missing dependency: colorama (`pip install colorama`)!")

# Doing this here now for an early exit if it can't be found.
try:
    import tabulate  # noqa
except ModuleNotFoundError:
    raise ModuleNotFoundError("Missing dependency: tabulate (`pip install tabulate`)!")

init(convert=True)


def main(args: argparse.Namespace) -> None:
    """Run the program."""
    if not any([args.input_file, args.recursive]):
        print(f"{Fore.RED}[!!] You must either pass an input file (-i) or run a recursive check (-R)!{Fore.RESET}")
        exit()

    files = [args.input_file] if args.input_file else glob('*')

    results: list[dict[str, str]] = list()

    for file in files:
        try:
            Hasher(file)
        except (FileNotFoundError, FileEmptyError, PermissionError):
            print(f"{Fore.YELLOW}[!?] Skipped {file} due to an {Fore.RED}exception{Fore.RESET}!")
            continue

        results += [check_file(file, HashingAlgorithm(str(args.algorithm).lower()))]

    if args.recursive:
        print("\n")

    if not results:
        print(f"{Fore.RED}[!!] No files could be checked! Please double-check your file(s)!{Fore.RESET}")
        exit()

    print(construct_table(results))
    print(gather_data(results))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file",
                        action="store", default=False, dest="input_file",
                        help="input file to verify checksum of")
    parser.add_argument("-R", "--recursive",
                        action="store_true", default=False,
                        help="recursively go over every file in the current directory (default: %(default)s)")
    parser.add_argument("-S", "--strip",
                        action="store_true", default=False,
                        help="strip CRCs from filenames (default: %(default)s)")
    parser.add_argument("-A", "--algorithm",
                        action="store", default='CRC32', choices=['CRC32', 'MD5', 'SHA256', 'ALL'],
                        help="hashing algorithm to use (default: %(default)s)")
    parser.parse_args()
    args = parser.parse_args()

    main(args)
