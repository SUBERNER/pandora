import os
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

    def __init__(self, file_format: int, display_results: bool):
        self._file_format = file_format
        self._display_results = display_results

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
        :param file: Longest file path.
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
            if os.path.isfile(source) or os.path.isdir(source):
                if self._file_format == 1:  # limited
                    limited_parts = source.split(os.sep)[-3:]
                    source = os.path.join(*limited_parts)
                elif self._file_format == 2:  # file
                    source = source.split("\\")[-1]

                if original_value != updated_value:
                    print(f"{source:>{self._file_length}} <|> {method} <|>   altered <|> [{Color.RED}{original_value}{Color.RESET}] --> [{Color.GREEN}{updated_value}{Color.RESET}]")
                else:
                    print(f"{source:>{self._file_length}} <|> {method} <|> unaltered <|> [{Color.YELLOW}{updated_value}{Color.RESET}]")
            else:
                self.error_result(f"{source:>{self._file_length}}", method, "not file or folder")
        except Exception as e:
            self.error_result(f"{source:>{self._file_length}}", method, e.__str__())

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
            print(f"{Color.RED_BACKGROUND}{source:>{self._file_length}} <|> {method} <|>     ERROR <|> {e.__str__()}{Color.RESET}")