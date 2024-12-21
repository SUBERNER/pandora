import os
import time
from . import Color


class Result:
    # formats for how the file location is displayed
    # 0 = full: full file directory
    # 1 = limited: 2 directories deep
    # 2 = file: only file
    _file_format = None
    # enabled or disabled displaying relevant information
    _display_results = True
    # the minimum amount of space given to the file section of a result
    _file_length = 0
    # delay between each error
    _error_delay = 0

    def __init__(self, file_format: int, display_results: bool):
        self._file_format = file_format
        self._display_results = display_results

    def set_delay(self, length: float = None):
        """
        sets the delay until another method can be executed after a Buffle error
        :param length: Duration of the delay in seconds
        :type length: float
        :return Format of displayed file's directory / location
        """
        if length is not None:
            if length < 0:  # makes sure it is positive
                length = 0

            self._error_delay = length
        return self._error_delay

    def set_format(self, format: int = None):
        """
        The format used when displaying file's directory / location
        0 = full | 1 = limited | 2 = file
        :type format: int
        :return Format of displayed file's directory / location
        """
        if format is not None:
            self._file_format = format
        return self._file_format

    def set_length(self, file: str):
        """
        Formats the minimum width of the source section of a result, improving result readability
        :param file: Determines length of source display based on the length of a file path, should be the longest path.
        :type file: str
        """

        if self._file_format == 1:  # limited
            limited_parts = file.split(os.sep)[-3:]
            self._file_length = len(os.path.join(*limited_parts))
        elif self._file_format == 2:  # file
            self._file_length = len(file.split("\\")[-1])
        else:  # full
            self._file_length = len(file)

        return self._file_length

    def set_display(self, display: bool = None):
        """
        Enables or Disables displaying results from this package's altering methods
        :type display: bool
        :return If results are enabled or disabled for this package's altering methods
        """
        if display is not None:
            self._display_results = display
        return self._display_results

    def result(self, source: str, method: str, updated_value, original_value):
        """
        Displays the output and processes of a method altering files
        :param source: Target file's or folder's directory / location
        :type source: str
        :param method: name of the method / action done
        :type method: str
        :param updated_value: value after alteration
        :param original_value: value before alteration
        """
        try:
            if self._file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif self._file_format == 2:  # file
                source = source.split("\\")[-1]

            if original_value != updated_value:
                print(f"{source:>{self._file_length}} <|> {method} <|>   altered <|> [{Color.RED}{original_value}{Color.RESET}] --> [{Color.GREEN}{updated_value}{Color.RESET}]")
            else:
                print(f"{source:>{self._file_length}} <|> {method} <|> unaltered <|> [{Color.YELLOW}{updated_value}{Color.RESET}]")
        except Exception as e:
            self.error_result(f"{source:>{self._file_length}}", method, str(e.args))

    def error_result(self, source: str, method: str, error: str):
        """
        Displays the output and processes of a method altering files
        :param source: Target file's or folder's directory / location
        :type source: str
        :param method: Name of the method / action done
        :type method: str
        :param error: Statement of what went wrong
        :type error: str
        """
        try:
            if self._file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif self._file_format == 2:  # file
                source = source.split("\\")[-1]
            print(f"{Color.RED_BACKGROUND}{source:>{self._file_length}} <|> {method} <|>     ERROR <|> {error}{Color.RESET}")

        except Exception as e:
            print(f"{Color.RED_BACKGROUND}{source:>{self._file_length}} <|> {method}<|>     ERROR <|> {e.args}{Color.RESET}")

        # the delay after an error until processes can run again
        time.sleep(self._error_delay)

    def warning_result(self, source: str, method: str, warning: str):
        """
        Displays the output and processes of a method altering files
        :param source: Target file's or folder's directory / location
        :type source: str
        :param method: Name of the method / action done
        :type method: str
        :param warning: Statement of what went wrong
        :type warning: str
        """
        try:
            if self._file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif self._file_format == 2:  # file
                source = source.split("\\")[-1]
            print(f"{Color.YELLOW_BACKGROUND}{source:>{self._file_length}} <|> {method} <|>   WARNING <|> {warning}{Color.RESET}")

        except Exception as e:
            print(f"{Color.RED_BACKGROUND}{source:>{self._file_length}} <|> {method}<|>   WARNING <|> {e.args}{Color.RESET}")

        # the delay after an error until processes can run again
        time.sleep(self._error_delay)
