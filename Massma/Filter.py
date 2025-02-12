import Massma
import re
import os
from enum import IntEnum

class Logic(IntEnum):
    AND = 0
    NAND = 1
    OR = 2
    NOR = 3
    XOR = 4
    XNOR = 5


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
                 *, test_files: str | list[str] | None = None, logic_strings: Logic = Logic.AND, logic_files: Logic = Logic.AND):
        # makes each variable always a list
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files
        self.logic_strings = [logic_strings] if isinstance(logic_strings, str) else logic_strings
        self.logic_files = [logic_files] if isinstance(logic_files, str) else logic_files

    def __call__(self, file: str) -> bool:
        try:
            texts = []  # stores all text found to be logic tested later
            matches_text = []  # stores all matches found in text to be logic tested later
            for files in self.files:
                if file == files:
                    if self.test_files is not None:
                        for test_file in self.test_files:
                            with open(test_file, "r") as f:
                                texts.append(f.read())
                    else:
                        with open(file, "r") as f:
                            texts.append(f.read())

                    for text in texts:  # stores matches for each text file separately for logic
                        matches_string = [bool(re.search(test, text)) for test in self.test_strings]
                        if self.logic_strings == Logic.AND:
                            result = all(matches_string)  # all patterns must match
                        elif self.logic_strings == Logic.OR:
                            result = any(matches_string)  # at least one must match
                        elif self.logic_strings == Logic.NAND:
                            result = not all(matches_string)  # opposite of AND
                        elif self.logic_strings == Logic.NOR:
                            result = not any(matches_string)  # opposite of OR
                        elif self.logic_strings == Logic.XOR:
                            result = sum(matches_string) == 1  # exactly one match
                        elif self.logic_strings == Logic.XNOR:
                            result = sum(matches_string) != 1  # opposite of XOR
                        else:
                            result = False  # default case
                        matches_text.append(result)

                    if self.logic_files == Logic.AND:
                        result = all(matches_text)  # all patterns must match
                    elif self.logic_files == Logic.OR:
                        result = any(matches_text)  # at least one must match
                    elif self.logic_files == Logic.NAND:
                        result = not all(matches_text)  # opposite of AND
                    elif self.logic_files == Logic.NOR:
                        result = not any(matches_text)  # opposite of OR
                    elif self.logic_files == Logic.XOR:
                        result = sum(matches_text) == 1  # exactly one match
                    elif self.logic_files == Logic.XNOR:
                        result = sum(matches_text) != 1  # opposite of XOR
                    else:
                        result = False  # default case

                    if result:
                        Massma.Display.filter.result(os.path.abspath(file), "exclude", file, ''.join(char + '\u0336' for char in file))
                    return result
            return False
        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file), "exclude", e)
            return False


class Alter:
    def __init__(self, files: str | list[str], test_strings: str | list[str], replace_strings: tuple[str, str] | list[tuple[str, str]],
                 *, test_files: str | list[str] | None = None, replace_files: str | list[str] | None = None, logic_strings: Logic = Logic.AND, logic_files: Logic = Logic.AND):
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files
        self.replace_strings = [replace_strings] if isinstance(replace_strings, tuple) else replace_strings
        self.replace_files = [replace_files] if isinstance(replace_files, str) else replace_files
        self.logic_strings = [logic_strings] if isinstance(logic_strings, str) else logic_strings
        self.logic_files = [logic_files] if isinstance(logic_files, str) else logic_files

    def __call__(self, file: str) -> bool:
        try:
            texts = []  # stores all text found to be logic tested later
            matches_text = []  # stores all matches found in text to be logic tested later
            for files in self.files:
                if file == files:
                    if self.test_files is not None:
                        for test_file in self.test_files:
                            with open(test_file, "r") as f:
                                texts.append(f.read())
                    else:
                        with open(file, "r") as f:
                            texts.append(f.read())

                    for text in texts:  # stores matches for each text file separately for logic
                        matches_string = [bool(re.search(test, text)) for test in self.test_strings]
                        if self.logic_strings == Logic.AND:
                            result = all(matches_string)  # all patterns must match
                        elif self.logic_strings == Logic.OR:
                            result = any(matches_string)  # at least one must match
                        elif self.logic_strings == Logic.NAND:
                            result = not all(matches_string)  # opposite of AND
                        elif self.logic_strings == Logic.NOR:
                            result = not any(matches_string)  # opposite of OR
                        elif self.logic_strings == Logic.XOR:
                            result = sum(matches_string) == 1  # exactly one match
                        elif self.logic_strings == Logic.XNOR:
                            result = sum(matches_string) != 1  # opposite of XOR
                        else:
                            result = False  # default case
                        matches_text.append(result)

                    if self.logic_files == Logic.AND:
                        result = all(matches_text)  # all patterns must match
                    elif self.logic_files == Logic.OR:
                        result = any(matches_text)  # at least one must match
                    elif self.logic_files == Logic.NAND:
                        result = not all(matches_text)  # opposite of AND
                    elif self.logic_files == Logic.NOR:
                        result = not any(matches_text)  # opposite of OR
                    elif self.logic_files == Logic.XOR:
                        result = sum(matches_text) == 1  # exactly one match
                    elif self.logic_files == Logic.XNOR:
                        result = sum(matches_text) != 1  # opposite of XOR
                    else:
                        result = False  # default case

                    if result:
                        Massma.Display.filter.result(os.path.abspath(file), "alter", file, ''.join(char + '\u0336' for char in file))
                    return result
            return False
        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file), "alter", e)
            return False


class Input:
    def __init__(self, files: str | list[str], test_inputs: str | list[str], *, logic_inputs: Logic | list[Logic] = Logic.AND):
        self.files = [files] if isinstance(files, str) else files
        self.test_inputs = [test_inputs] if isinstance(test_inputs, str) else test_inputs
        self.logic_inputs = [logic_inputs] if isinstance(logic_inputs, Logic) else logic_inputs

    def __call__(self, file: str, input: str) -> bool:
        try:
            for files in self.files:
                if file == files:
                    # gets boolean values for if input_string was found
                    matches = [bool(re.search(test, input)) for test in self.test_inputs]
                    if self.logic_inputs == Logic.AND:
                        result = all(matches)  # all test_inputs must match
                    elif self.logic_inputs == Logic.OR:
                        result = any(matches)  # at least one must match
                    elif self.logic_inputs == Logic.NAND:
                        result = not all(matches)  # opposite of AND
                    elif self.logic_inputs == Logic.NOR:
                        result = not any(matches)  # opposite of OR
                    elif self.logic_inputs == Logic.XOR:
                        result = sum(matches) == 1  # exactly one match
                    elif self.logic_inputs == Logic.XNOR:
                        result = sum(matches) != 1  # opposite of XOR
                    else:
                        result = False

                    if result:
                        Massma.Display.filter.result(os.path.abspath(file), "input", input, ''.join(char + '\u0336' for char in input))
                    return result
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