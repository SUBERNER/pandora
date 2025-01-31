from Buffle import random  # used for seeds
from enum import IntEnum
import re
import os

# Used when filtering out and specifying what changes can and cannot be made when shuffling files.
# This allows for greater control over the shuffle, making results stable or constrained as needed.


class Ignore:
    """
    Filters out specific files from being processed.

    Parameter:
        files (str | list[str]): File path(s) to ignore.

    Behavior:
        - If a file is listed in `files`, the filter will return `True`, indicating it should be ignored.
        - Otherwise, it returns `False`, allowing the file to be processed.
    """

    def __init__(self, files: str | list[str]):
        self.files = [files] if isinstance(files, str) else files

    def __call__(self, file: str) -> bool:
        for files in self.files:
            if file == files:
                return True
        return False


class Input:
    def __init__(self, files: str | list[str], test_inputs: str | list[str]):
        self.files = [files] if isinstance(files, str) else files
        self.test_inputs = [test_inputs] if isinstance(test_inputs, str) else test_inputs

    def __call__(self, file: str, input: str, *, regex: bool = False) -> bool:
        for files in self.files:
            if file == files:
                for test_input in self.test_inputs:
                    if (regex and re.search(test_input, input)) or (test_input in input):
                        return True
        return False


class Exclude:
    """
    Filters out files based on their content.
    If a file contains any of the specified `test_strings`, it is excluded.

    Parameter:
        files (str | list[str]): Target file(s) to check.

        test_strings (str | list[str]): Strings or patterns to search for in the file(s).

        test_files (str | list[str] | None): If specified, the search will occur in these files instead of `files`.

    Keyword Parameter:
        regex (bool): Whether `test_strings` should be treated as regular expressions. Defaults to False.
    """

    def __init__(self, files: str | list[str], test_strings: str | list[str], test_files: str | list[str] | None = None):
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files

    def __call__(self, file: str, *, regex: bool = False) -> bool:
        for target_file in self.files:
            if target_file == file:
                search_files = self.test_files if self.test_files else [file]
                for search_file in search_files:
                    with open(search_file, 'r') as f:
                        text = f.read()
                        for test_string in self.test_strings:
                            if (regex and re.search(test_string, text)) or (test_string in text):
                                return True
        return False


class Alter:
    """
    Modifies file contents based on search-and-replace rules.
    If a file contains any of the specified `test_strings`, the corresponding `replace_strings` value replaces it.

    Parameter:
        files (str | list[str]): Target file(s) to modify.

        test_strings (str | list[str]): Strings or patterns to search for.

        test_files (str | list[str] | None): If specified, the search occurs in these files instead.

        replace_strings (tuple[str, str] | list[tuple[str, str]]): Pairs of (old, new) strings to replace.

        replace_files (str | list[str] | None): If specified, changes are written to these files instead of `files`.

    Keyword Parameter:
        regex (bool): Whether `test_strings` and `replace_strings` should be treated as regex patterns. Defaults to False.
    """

    def __init__(self, files: str | list[str], test_strings: str | list[str], replace_strings: tuple[str, str] | list[tuple[str, str]], replace_files: str | list[str] | None = None, test_files: str | list[str] | None = None):
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files
        self.replace_strings = [replace_strings] if isinstance(replace_strings, tuple) else replace_strings
        self.replace_files = [replace_files] if isinstance(replace_files, str) else replace_files

    def __call__(self, file: str, *, regex: bool = False):
        replace = False
        for target_file in self.files:
            if target_file == file:
                search_files = self.test_files if self.test_files else [file]
                for search_file in search_files:
                    with open(search_file, 'r') as f:
                        text = f.read()
                        for test_string in self.test_strings:
                            if (regex and re.search(test_string, text)) or (test_string in text):
                                replace = True

        if replace:
            write_files = self.replace_files if self.replace_files else [file]
            for write_file in write_files:
                with open(write_file, 'w') as f:
                    for old, new in self.replace_strings:
                        text = re.sub(old, new, text) if regex else text.replace(old, new)
                    f.write(text)


class Swap:
    """
    Swaps file names between two or more files.
    If called again, the files swap back to their original names.

    Parameter:
        files (tuple[str, str] | list[tuple[str, str]]): Pairs of (old file, new file) to swap.
    """

    def __init__(self, files: tuple[str, str] | list[tuple[str, str]]):
        self.files = [files] if isinstance(files, tuple) else files

    def __call__(self):
        for file in self.files:
            os.rename(file[0], file[1])
            file[0], file[1] = file[1], file[0]  # swaps them to and swaps back to normal once its recalled


class Logic(IntEnum):
    AND = 0
    NAND = 1
    OR = 2
    NOR = 3
    XOR = 4
    XNOR = 5