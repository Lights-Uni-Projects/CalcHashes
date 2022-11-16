import argparse
import os
from glob import glob

from alive_progress import alive_bar

from .exceptions import FileEmptyError
from .functions import check_file, construct_table, gather_data
from .types import Hasher, HashingAlgorithm

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

    if HashingAlgorithm(str(args.algorithm.lower())) == HashingAlgorithm.ALL:
        print(f"{Fore.RED}\"{args.algorithm}\" is currently not supported!{Fore.RESET} "
              "Please try another algorithm.")
        exit()

    if os.path.isdir(args.input_file):
        files = glob(f"{args.input_file}/*")
    else:
        files = [args.input_file] if args.input_file else glob('*')

    results: list[dict[str, str]] = list()

    with alive_bar(len(files), dual_line=True, title='Processing files...') as bar:
        for file in files:
            try:
                Hasher(file)
            except (FileNotFoundError, FileEmptyError, PermissionError) as e:
                print(f"{Fore.YELLOW}[?!] Skipped {file} due to an {Fore.RED}exception ({e}){Fore.YELLOW} "
                      f"(this may not display entirely correctly)!{Fore.RESET}")
                bar()
                continue

            results += [check_file(file, HashingAlgorithm(str(args.algorithm).lower()), args.append)]
            bar()

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
                        help="input file or directory")
    parser.add_argument("-R", "--recursive",
                        action="store_true", default=False,
                        help="recursively go over every file in the current directory (default: %(default)s)")
    parser.add_argument("-a", "--append",
                        action="store_true", default=False,
                        help="append calculated hash to filename (default: %(default)s)")
    parser.add_argument("-A", "--algorithm",
                        action="store", default='CRC32', choices=[x.value.upper() for x in HashingAlgorithm],
                        help="hashing algorithm to use (default: %(default)s)")
    parser.parse_args()
    args = parser.parse_args()

    main(args)
