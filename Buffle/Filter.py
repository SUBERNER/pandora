from Buffle import random  # used for seeds
from enum import IntEnum
# used when filtering out and specifying what changes can and cannot be made when shuffling files
# This allows for MUCH more control over the shuffle, such as making the results of shuffles stable or possible


class Ignore:
    files = [str]  # the files checked in the filter

    def __init__(self, files: str | [str]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):
            self.files = [files]


class Exclude:
    files = [str]  # the files checked in the filter
    test_string = [str]  # the substrings that are tested in the filter
    test_files = [str]  # if added, the tests will happen in "test_files" and not "files"

    def __init__(self, files: str | [str], test_strings: str | [str], test_files: str | [str]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):
            self.files = [files]
        if isinstance(test_strings, str):
            self.test_string = [test_strings]
        if isinstance(test_files, str):
            self.test_files = [test_files]


class Alter:
    files = [str]  # the files checked in the filter
    test_strings = [str]  # the substrings that are tested in the filter
    test_files = [str]  # if added, the tests will happen in "test_files" and not "file"
    replace_strings = [tuple[str, str]]  # the substrings that are replacing other substrings
    replace_files = [str]  # if added, the replacing will happen in "replace_files" and not "replace_strings"

    def __init__(self, files: str | [str], test_strings: str | [str], test_files: str | [str], replace_strings: tuple[str, str] | [tuple[str, str]], replace_files: str | [str]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):
            self.files = [files]
        if isinstance(test_strings, str):
            self.test_string = [test_strings]
        if isinstance(test_files, str):
            self.test_files = [test_files]
        if isinstance(replace_strings, str):  # FIX THIS PART
            self.replace_strings = [replace_strings]
        if isinstance(replace_files, str):
            self.replace_files = [replace_files]


class Swap:
    files = [tuple[str, str]]  # the names of files that will be swapping before and after a method

    def __init__(self, files: tuple[str, str] | [tuple[str, str]]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):  # FIX THIS PART
            self.files = [files]


class Type(IntEnum):
    AND = 0
    OR = 1
    XOR = 2


