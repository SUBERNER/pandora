import os


class Color:
    # Used to better communicate how methods effected files
    # Used to make Errors and Warnings more noticeable
    ERROR = '\033[41m'  # Red Background, errors that have stopped the code completely, unless told to ignore
    NOTIFY = '\033[42m'  # Green Background, notification for something positive or completion
    WARNING = '\033[43m'  # Yellow Background, warning users that the input or output might not be what they wanted
    RED = '\033[31m'  # Red Text, original value or trait before change or shuffled
    GREEN = '\033[32m'  # Green Text, new value or trait after change or shuffle
    YELLOW = '\033[33m'  # Yellow Text, value or trait is unchanged before and after change or shuffle
    RESET = '\033[0m'  # Removes all effects

    # Used to better communicate the grouping of methods effected files
    # These are the recommend colors to be used, as they are more likely to work with many terminals
    GROUPS = (
        "\033[91m",  # [0] light red
        "\033[31m",  # [1] red
        "\033[92m",  # [2] light green
        "\033[32m",  # [3] green
        "\033[93m",  # [4] light yellow
        "\033[33m",  # [5] dark yellow
        "\033[94m",  # [6] light blue
        "\033[34m",  # [7] blue
        "\033[95m",  # [8] light purple
        "\033[35m",  # [9] purple
        "\033[96m",  # [10] light cyan
        "\033[36m",  # [11] cyan
        "\033[97m",  # [12] white
        "\033[37m",  # [13] light gray
        "\033[90m",  # [14] dark gray
        "\033[30m",  # [15] black
    )


class Result:
    _display_results = True  # Displaying input, process, and output information from a method
    _display_warning = False  # Displaying warning information from a method
    _source_compression = True  # Shortens the method's source to the last 3 directories
    _source_length = 0  # Minimum amount of space given to the source section of a result for readability
    _method_color = None  # Colors used for easier method groups identification
    _raw_error = False  # Displays errors in an non-formatted style
    _quit_error = True  # Stops script program while running is an error result appears
    _quit_warning = False  # Stops script program while running is a warning result appears
    _stats = tuple[0, 0, 0, 0]  # data for the result output for a method group [altered, unaltered, warnings, errors]

    def __init__(self, *, method_color: str = Color.GROUPS[12], display_results: bool = True, display_warning: bool = False,
                 source_compression: bool = True, raw_error: bool = False, quit_error: bool = True, quit_warning: bool = False):
        try:
            self._display_results = display_results
            self._method_color = method_color
            self._display_warning = display_warning
            self._source_compression = source_compression
            self._raw_error = raw_error
            self._quit_error = quit_error
            self._quit_warning = quit_warning
        except Exception as e:
            self.error_result(f"None", "display", str(e if self._raw_error else e.args))

    def result(self, source: str, method: str, updated_value, original_value):
        try:
            if self._source_compression:
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)

            if original_value != updated_value:  # value changed
                print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|>   altered <|> [{Color.RED}{original_value}{Color.RESET}] -> [{Color.GREEN}{updated_value}{Color.RESET}]")

            else:  # value unchanged
                print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|> unaltered <|> [{Color.YELLOW}{updated_value}{Color.RESET}]")

        except Exception as e:
            self.error_result(f"{source:>{self._source_length}}", method, str(e if self._raw_error else e.args))

    def error_result(self, source: str, method: str, error: str):
        try:
            if self._source_compression:
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)

            print(f"{Color.ERROR}{source:>{self._source_length}} <|> {method} <|>     ERROR <|> {error}{Color.RESET}")
            if self._quit_error:
                quit()  # ends running code

        except Exception as e:
            print(f"{Color.ERROR}{source:>{self._source_length}} <|> {method}<|>     ERROR <|> {e if self._raw_error else e.args}{Color.RESET}")
            if self._quit_error:
                quit()  # ends running code

    def warning_result(self, source: str, method: str, warning: str):
        try:
            if self._display_warning:  # if warning will be displayed
                if self._source_compression:
                    limited_parts = source.split(os.sep)[-3:]
                    source = os.path.join(*limited_parts)

                print(f"{Color.WARNING}{source:>{self._source_length}} <|> {method} <|>   WARNING <|> {warning}{Color.RESET}")
                if self._quit_warning:
                    quit()  # ends running code

        except Exception as e:
            self.error_result(f"{source:>{self._source_length}}", method, str(e if self._raw_error else e.args))