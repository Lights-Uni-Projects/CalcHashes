# CalcHash

Calculate the hash of one or multiple files
and compare them to a hash present in the filename.
This is mainly useful for files like anime fansub episodes,
as those commonly include the CRC32 hash in the filename.

## Installation

You can simply install it with the following command:

```console
pip install git+https://github.com/Lights-Uni-Projects/CalcHashes.git
```

If you're downloading it from this repo as a zip, make sure you run the following command:

```console
python setup.py install
```

Note that this module requires Python 3.**10**!

## Usage

This module currently has two modes: single file, and recursively searching in the current directory.

Single file mode can be run using the following syntax:

```bash
python -m calchash -i "file"
```

Multi-file can be run using the following syntax:

```bash
python -m calchash -R
```

To check for a hash, you can run the following command:

```bash
python -m calchash -i "file" -A CRC32
```

The default is CRC32.
This setting is **case-sensitive**.

For a list of all currently-supported hashing algorithms, please run `--help`.
