import Massma
import re
import os
from enum import IntEnum


class Ignore:
    def __init__(self, files: str | list[str]):
        # makes each variable always a list
        self.files = [files] if isinstance(files, str) else files

    def __call__(self, file: str) -> bool:
        try:
            for files in self.files:
                if file == files:
                    Massma.Display.filter.result(os.path.abspath(file), "ignore", file, ''.join(char + '\u0336' for char in file))
                    return True
            return False
        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file), "ignore", e)
            return False


class Exclude:
    def __init__(self, files: str | list[str], test_strings: str | list[str],
                 *, test_files: str | list[str] | None = None, logic = 0):
        # makes each variable always a list
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files

    def __call__(self, file: str) -> bool:
        pass


class Alter:
    def __init__(self, files: str | list[str], test_strings: str | list[str], replace_strings: tuple[str, str] | list[tuple[str, str]],
                 *, test_files: str | list[str] | None = None, replace_files: str | list[str] | None = None, logic = 0):
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files
        self.replace_strings = [replace_strings] if isinstance(replace_strings, tuple) else replace_strings
        self.replace_files = [replace_files] if isinstance(replace_files, str) else replace_files

    def __call__(self, file: str) -> bool:
        pass


class Input:
    def __init__(self, files: str | list[str], test_inputs: str | list[str], *, logic = 0):
        self.files = [files] if isinstance(files, str) else files
        self.test_inputs = [test_inputs] if isinstance(test_inputs, str) else test_inputs

    def __call__(self, file: str, input: str) -> bool:
        try:
            for files in self.files:
                if file == files:
                    for test_inputs in self.test_inputs:
                        if re.search(test_inputs, input):
                            Massma.Display.filter.result(os.path.abspath(file), "input", input, ''.join(char + '\u0336' for char in input))
                            return True
            return False
        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file), "input", e)
            return False


class Swap:
    def __init__(self, files: tuple[str, str] | list[tuple[str, str]]):
        # makes each variable always a list
        self.files = [files] if isinstance(files, tuple) else files

    def __call__(self):
        file = self.files[0]  # soul purpose is for if the try and except fails before it can get in the for loop
        try:
            for index, file in enumerate(self.files):
                os.rename(file[0], file[1])
                Massma.Display.filter.result(os.path.abspath(file[0]), "swap", os.path.abspath(file[1]), os.path.abspath(file[0]))
                self.files[index] = (file[1], file[0])  # swaps them to and swaps back to normal once its recalled
        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file[0]), "swap", e)


class Logic(IntEnum):
    AND = 0
    NAND = 1
    OR = 2
    NOR = 3
    XOR = 4
    XNOR = 5