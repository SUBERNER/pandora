import os
from . import Color

# formats for how the file location is displayed
# 0 = full: full file directory
# 1 = limited: 2 directories deep
# 2 = file: only file
__file_format = None
# enabled or disabled displaying relevant information
__display_results = None
# the minimum amount of space given to the file section of a result
__file_length = 0


def __init__(self, file_format: int, display_results: bool):
    self.file_format = file_format
    self.display_results = display_results


def set_format(format: int = None):
    """
    The format used when displaying file's directory / location
    0 = full | 1 = limited | 2 = file
    :type format: int
    :return Format of displayed file's directory / location
    """
    if format is not None:
        __file_format = format
    return __file_format


def set_length(file: str):
    """
    Formats the minimum width of the source section of a result, improving result readability
    :param file: Longest file path.
    :type file: str
    """

    if __file_format == 1:  # limited
        limited_parts = file.split(os.sep)[-3:]
        __file_length = len(os.path.join(*limited_parts))
    elif __file_format == 2:  # file
        __file_length = len(file.split("\\")[-1])
    else:  # full
        __file_length = len(file)

    return __file_length


def set_display(display: bool = None):
    """
    Enables or Disables displaying results from this package's altering methods
    :type display: bool
    :return If results are enabled or disabled for this package's altering methods
    """
    if display is not None:
        __display_results = display
    return __display_results


def result(source: str, method: str, updated_value, original_value):
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
            if __file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif __file_format == 2:  # file
                source = source.split("\\")[-1]

            if original_value != updated_value:
                print(f"{source:>{__file_length}} <|> {method} <|>   altered <|> [{Color.RED}{original_value}{Color.RESET}] --> [{Color.GREEN}{updated_value}{Color.RESET}]")
            else:
                print(f"{source:>{__file_length}} <|> {method} <|> unaltered <|> [{Color.YELLOW}{updated_value}{Color.RESET}]")
        else:
            print(f"{Color.RED_BACKGROUND}{source:>{__file_length}} <|> {method}-ERROR <|> not file or folder{Color.RESET}")
    except:
        print(f"{Color.RED_BACKGROUND}{source:>{__file_length}} <|> {method}-ERROR <|> displaying alters{Color.RESET}")


def result_error(source: str, method: str, error: str):
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
        if os.path.isfile(source) or os.path.isdir(source):
            if __file_format == 1:  # limited
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)
            elif __file_format == 2:  # file
                source = source.split("\\")[-1]

            print(f"{Color.RED_BACKGROUND}{source:>{__file_length}} <|> {method}-ERROR<|> {error}{Color.RESET}")

        else:
            print(f"{Color.RED_BACKGROUND}{source:>{__file_length}} <|> {method}-ERROR <|> not file or folder{Color.RESET}")
    except:
        print(f"{Color.RED_BACKGROUND}{source:>{__file_length}} <|> {method}-ERROR <|> displaying alters{Color.RESET}")