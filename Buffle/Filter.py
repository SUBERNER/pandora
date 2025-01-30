from Buffle import random  # used for seeds
# used when filtering out and specifying what changes can and cannot be made when shuffling files
# This allows for MUCH more control over the shuffle, such as making the results of shuffles stable or possible


class Ignore:
    files = [str]  # the files checked in the filter

    def __init__(self, files: str | list[str]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):
            self.files = [files]
        else:
            self.files = files

class Exclude:
    files = [str]  # the files checked in the filter
    test_string = [str]  # the substrings that are tested in the filter
    test_files = [str]  # if added, the tests will happen in "test_files" and not "files"

    def __init__(self, files: str | list[str], test_strings: str | list[str], test_files: str | list[str]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):
            self.files = [files]
        else:
            self.files = files
        if isinstance(test_strings, str):
            self.test_string = [test_strings]
        else:
            self.test_string = test_strings
        if isinstance(test_files, str):
            self.test_files = [test_files]
        else:
            self.test_files = test_files


class Alter:
    files = [str]  # the files checked in the filter
    test_strings = [str]  # the substrings that are tested in the filter
    test_files = [str]  # if added, the tests will happen in "test_files" and not "file"
    replace_strings = [tuple[str, str]]  # the substrings that are replacing other substrings
    replace_files = [str]  # if added, the replacing will happen in "replace_files" and not "replace_strings"

    def __init__(self, files: str | list[str], test_strings: str | list[str], test_files: str | list[str], replace_strings: tuple[str, str] | list[tuple[str, str]], replace_files: str | list[str]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):
            self.files = [files]
        else:
            self.files = files
        if isinstance(test_strings, str):
            self.test_string = [test_strings]
        else:
            self.test_string = test_strings
        if isinstance(test_files, str):
            self.test_files = [test_files]
        else:
            self.test_files = test_files
        if isinstance(replace_strings, str):  # FIX THIS PART
            self.replace_strings = [replace_strings]
        else:
            self.replace_strings = replace_strings
        if isinstance(replace_files, str):
            self.replace_files = [replace_files]
        else:
            self.replace_files = replace_files


class Swap:
    files = [tuple[str, str]]  # the names of files that will be swapping before and after a method

    def __init__(self, files: tuple[str, str] | list[tuple[str, str]]):
        # makes sure parts of filer are always a list if needed
        if isinstance(files, str):  # FIX THIS PART
            self.files = [files]
        else:
            self.files = files


# THIS IS A MESS, FIX LATER
def ignore_test(ignores: Ignore | list[Ignore], file: str) -> bool:
    for ignore in ignores:
        for files in ignore.files:
            if file == files:
                return True
    return False

