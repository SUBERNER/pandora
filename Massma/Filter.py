import Massma
import re
import os
from enum import IntEnum


class Logic(IntEnum):
    AND = 0  # all patterns must match
    NAND = 1  # opposite of AND
    OR = 2  # at least one must match
    NOR = 3  # opposite of OR
    XOR = 4  # exactly one match
    XNOR = 5  # opposite of XOR


class Ignore:
    """
    Ignores files that match specified filenames.
    """
    def __init__(self, files: str | list[str]):
        """
        Initializes the Ignore filter.

        Parameters:
            files (str | list[str]): Filename(s) to be ignored.
        """
        # makes each variable always a list
        self.files = [files] if isinstance(files, str) else files

    def __call__(self, file: str) -> bool:
        """
        Checks if a given file should be ignored.

        Parameters:
            file (str): The filename to check.

        Return:
            bool: True if the file should be ignored, False otherwise.
        """
        try:
            for files in self.files:
                if file == files:
                    Massma.Display.filter.result(os.path.abspath(file), "ignore", file, ''.join(char + '\u0336' for char in file))
                    return True
            return False
        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file), "ignore", str(e))
            return False


class Exclude:
    """
    Excludes files based on specified substrings or patterns within file content.
    """
    def __init__(self, files: str | list[str], test_strings: str | list[str], *, test_files: str | list[str] | None = None,
                 logic_strings: Logic = Logic.AND, logic_files: Logic = Logic.AND, flags: list[re.RegexFlag] = None):
        """
       Initializes the Exclude filter.

       Parameters:
           files (str | list[str]): Filename(s) to check.

           test_strings (str | list[str]): Strings or regex patterns to look for within the files.

           test_files (str | list[str] | None): Alternative files to check instead of the primary files.

           logic_strings (Logic): Logical operation applied between test strings. Defaults to AND.

           logic_files (Logic): Logical operation applied between test files. Defaults to AND.

           flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).
       """
        # makes each variable always a list
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files
        self.logic_strings = logic_strings
        self.logic_files = logic_files
        self.flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

    def __call__(self, file: str) -> bool:
        """
        Determines whether a file should be excluded based on its content.

        Parameters:
            file (str): The filename to check.

        Return:
            bool: True if the file should be excluded, False otherwise.
        """
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
                        matches_string = [bool(re.search(test, text, flags=self.flags)) for test in self.test_strings]
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
            Massma.Display.filter.result_error(os.path.abspath(file), "exclude", str(e))
            return False


class Alter:
    """
    Alters file contents by replacing specific patterns with new values based on logical operations.
    """
    def __init__(self, files: str | list[str], test_strings: str | list[str], replace_strings: tuple[str, str] | list[tuple[str, str]], *, test_files: str | list[str] | None = None, replace_files: str | list[str] | None = None,
                 logic_strings: Logic = Logic.AND, logic_files: Logic = Logic.AND, flags: list[re.RegexFlag] = None):
        """
        Initializes the Alter filter.

        Parameters:
            files (str | list[str]): List of file paths to check.

            test_strings (str | list[str]): List of substrings to search for within the files.

            replace_strings (tuple[str, str] | list[tuple[str, str]]): List of tuples containing old and new substrings for replacement.

            test_files (str | list[str] | None): List of alternative files to check for the test strings.

            replace_files (str | list[str] | None): List of files where the replacements should be made.

            logic_strings (Logic): Logical condition applied to test_strings (default is AND).

            logic_files (Logic): Logical condition applied to test_files (default is AND).

            flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).
        """
        self.files = [files] if isinstance(files, str) else files
        self.test_strings = [test_strings] if isinstance(test_strings, str) else test_strings
        self.test_files = [test_files] if isinstance(test_files, str) else test_files
        self.replace_strings = [replace_strings] if isinstance(replace_strings, tuple) else replace_strings
        self.replace_files = [replace_files] if isinstance(replace_files, str) else replace_files
        self.logic_strings = logic_strings
        self.logic_files = logic_files
        self.flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

    def __call__(self, file: str):
        """
        Applies alterations to a file by replacing specified patterns with new values.

        Parameters:
            file (str): File path to alter.
        """
        try:
            texts = []  # stores all text found to be logic tested later
            matches_text = []  # stores all matches found in text to be logic tested later
            replaces_text = []  # stores all the texts that will be replaced
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
                        matches_string = [bool(re.search(test, text, flags=self.flags)) for test in self.test_strings]
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

                    # replacing data in files
                    if result:
                        if self.replace_files is not None:
                            for replace_file in self.replace_files:
                                with open(replace_file, "r") as f:
                                    text = f.read()
                                with open(replace_file, "w") as f:
                                    for old, new in self.replace_strings:
                                        text = re.sub(old, new, text)
                                        Massma.Display.filter.result(os.path.abspath(replace_file), "alter", old, new)  # DISPLAYS CHANGED IT DOSE NOT ALWAYS MAKE
                                    f.write(text)

                        else:
                            with open(file, "r") as f:
                                text = f.read()

                            with open(file, "w") as f:
                                for old, new in self.replace_strings:
                                    text = re.sub(old, new, text)
                                    Massma.Display.filter.result(os.path.abspath(file), "alter", old, new)  # DISPLAYS CHANGED IT DOSE NOT ALWAYS MAKE
                                f.write(text)

        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file), "alter", str(e))


class Input:
    """
        Validates user input by checking for predefined patterns before processing.
    """
    def __init__(self, files: str | list[str], test_inputs: str | list[str],
                 *, logic_inputs: Logic = Logic.AND, flags: list[re.RegexFlag] = None):
        """
        Initializes an Input instance.

        Parameters:
            files (str | list[str]): The file(s) where validation applies.

            test_inputs (str | list[str]): Patterns against which the input is tested.

            logic_inputs (Logic): Logical condition for pattern matching (AND, OR, XOR, etc.). Defaults to Logic.AND.

            flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).
        """
        self.files = [files] if isinstance(files, str) else files
        self.test_inputs = [test_inputs] if isinstance(test_inputs, str) else test_inputs
        self.logic_inputs = logic_inputs
        self.flags = 0 if flags is None else sum(flags)  # Combine selected flags or default to 0 (no flags)

    def __call__(self, file: str, input: str) -> bool:
        """
        Validates user input by checking for predefined patterns.

        Parameters:
            file (str | list[str]): The file(s) where validation applies.

            input (str | list[str]): Patterns against which the input is tested.

        Keyword Parameters:
            logic_inputs (Logic): Logical condition for pattern matching (AND, OR, XOR, etc.). Defaults to Logic.AND.
        """
        try:
            for files in self.files:
                if file == files:
                    # gets boolean values for if input_string was found
                    matches = [bool(re.search(test, input, flags=self.flags)) for test in self.test_inputs]
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
            Massma.Display.filter.result_error(os.path.abspath(file), "input", str(e))
            return False


class Swap:
    """
    Swaps the names of specified files.
    """
    def __init__(self, files: tuple[str, str] | list[tuple[str, str]]):
        """
        Initializes the Swap filter.

        Parameters:
            files (tuple[str, str] | list[tuple[str, str]]): Pairs of filenames to swap.
        """
        # makes each variable always a list
        self.files = [files] if isinstance(files, tuple) else files

    def __call__(self):
        """
        Executes the swap operation on the specified file pairs.
        """
        file = self.files[0]  # soul purpose is for if the try and except fails before it can get in the for loop
        try:
            for index, file in enumerate(self.files):
                os.rename(file[0], file[1])
                Massma.Display.filter.result(os.path.abspath(file[0]), "swap", os.path.abspath(file[0]), os.path.abspath(file[1]))
                self.files[index] = (file[1], file[0])  # swaps them to and swaps back to normal once its recalled
        except Exception as e:
            Massma.Display.filter.result_error(os.path.abspath(file[0]), "swap", str(e))