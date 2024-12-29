import os
from . import Color


class Result:
    # formats for how the file location is displayed
    # 0 = full: full file directory
    # 1 = limited: 2 directories deep
    # 2 = file: only file
    _file_format = None
    # enabled or disabled displaying relevant information
    _display_results = None
    # the minimum amount of space given to the source file section of a result
    _source_length = 0
    # the color used in method section to identify what method is being used
    _method_color = None
    # stops the script while running if an error_result is displayed
    _error_quit = True

    def __init__(self, file_format: int, display_results: bool, method_color: str = f"\033[38;2;{255};{255};{255}m"):
        self._file_format = file_format
        self._display_results = display_results
        self._method_color = self.set_color(method_color)

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

    def set_color(self, hex_color: str = None):
        if hex_color is not None:
            hex_color = hex_color.lstrip("#")
            r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
            self._method_color = f"\033[38;2;{r};{g};{b}m"
        return self._method_color

    def set_length(self, file: str):
        """
        Formats the minimum width of the source section of a result, improving result readability
        :param file: Determines length of source display based on the length of a file path, should be the longest path.
        :type file: str
        """

        if self._file_format == 1:  # limited
            limited_parts = file.split(os.sep)[-3:]
            self._source_length = len(os.path.join(*limited_parts))
        elif self._file_format == 2:  # file
            self._source_length = len(file.split("\\")[-1])
        else:  # full
            self._source_length = len(file)

        return self._source_length

    def set_error(self, quit: bool = None):
        """
        Enables or Disables displaying results from this package's altering methods
        :type display: bool
        :return If results are enabled or disabled for this package's altering methods
        """
        if quit is not None:
            self._error_quit = quit
        return self._error_quit

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
                print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|>   altered <|> [{Color.RED}{original_value}{Color.RESET}] --> [{Color.GREEN}{updated_value}{Color.RESET}]")
            else:
                print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|> unaltered <|> [{Color.YELLOW}{updated_value}{Color.RESET}]")
        except Exception as e:
            self.error_result(f"{source:>{self._source_length}}", method, str(e.args))

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
            print(f"{Color.RED_BACKGROUND}{source:>{self._source_length}} <|> {method} <|>     ERROR <|> {error}{Color.RESET}")
            if self._error_quit:
                quit()  # ends running code

        except Exception as e:
            print(f"{Color.RED_BACKGROUND}{source:>{self._source_length}} <|> {method}<|>     ERROR <|> {e.args}{Color.RESET}")
            if self._error_quit:
                quit()  # ends running code

        # the delay after an error until processes can run again

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
            print(f"{Color.YELLOW_BACKGROUND}{source:>{self._source_length}} <|> {method} <|>   WARNING <|> {warning}{Color.RESET}")

        except Exception as e:
            print(f"{Color.RED_BACKGROUND}{source:>{self._source_length}} <|> {method}<|>   WARNING <|> {e.args}{Color.RESET}")
            if self._error_quit:
                quit()  # ends running code

        # the delay after an error until processes can run again
