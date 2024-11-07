import os
import shutil

# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files

# region DISPLAY_RESULTS
# [0] display_file_results
# [1] display_text_results
# [2] display_texture_results
# [3] display_manual_results
# enabled or disabled by user to display relevant information
__displays_results = [True, True, True, True]
# formats for how the file location is displayed
# 0 = full: full file directory
# 1 = limited: 2 directories deep
# 2 = file: only file
__file_format = 0


def display_file_format(format: int = None):
    """
    The format used when displaying file's directory / location
    0 = full | 1 = limited | 2 = file
    :type format: int
    :return Format of displayed file's directory / location
    """
    if format is not None:
        global __file_format
        __file_format = format
    return __file_format


def display_all_results(display: bool = None):
    """
    Enables or Disables displaying results from all file & folder altering methods
    :type display: bool
    :return If results are enabled or disabled for all file & folder altering methods
    """
    if display is not None:
        for dr in __displays_results:
            dr = display
    return __displays_results


def display_file_results(display: bool = None):
    """
    Enables or Disables displaying results from File methods
    :type display: bool
    :return If results are enabled or disabled
    """
    if display is not None:
        __displays_results[0] = display
    return __displays_results[0]


def display_text_results(display: bool = None):
    """
    Enables or Disables displaying results from Text methods
    :type display: bool
    :return If results are enabled or disabled
    """
    if display is not None:
        __displays_results[1] = display
    return __displays_results[1]


def display_texture_results(display: bool = None):
    """
    Enables or Disables displaying results from Texture methods
    :type display: bool
    :return If results are enabled or disabled
    """
    if display is not None:
        __displays_results[2] = display
    return __displays_results[2]


def display_manual_results(display: bool = None):  # not implemented yet or will be till future updates
    """
    Enables or Disables displaying results from all Manual methods
    :type display: bool
    :return If results are enabled or disabled
    """
    if display is not None:
        __displays_results[3] = display
    return __displays_results[3]


def result(file: str, method: str, updated_value, original_value):
    """
    Displays the output and processes of a method altering files
    :param file: Target file's directory / location
    :type file: str
    :param method: name of the method / action done
    :type method: str
    :param updated_value: value after alteration
    :param original_value: value before alteration
    """
    try:
        if os.path.isfile(file):
            if __file_format == 1:  # limited
                limited_parts = file.split(os.sep)[-2:]
                file = os.path.join(*limited_parts)
            elif __file_format == 2:  # file
                file = file.split("\\")[-1]

            if original_value != updated_value:
                print(f"{file} <|> {method} <|> altered <|> [{original_value}] -> [{updated_value}]")
            else:
                print(f"{file} <|> {method} <|> unaltered <|> [{updated_value}]")
        else:
            print(f"{file} <|> ERROR <|> file not found")
    except:
        print(f"{file} <|> ERROR <|> displaying alters")


def __results(file: str, method: str, updated_value, original_value):
    try:
        if os.path.isfile(file):
            if original_value != updated_value:
                print(f"{file} <|> {method} <|> altered <|> [{original_value}] -> [{updated_value}]")
            else:
                print(f"{file} <|> {method} <|> unaltered <|> [{updated_value}]")
        else:
            print(f"{file} <|> ERROR <|> file not found")
    except:
        print(f"{file} <|> ERROR <|> displaying alters")


# endregion


# region DIRECTORY
def dump(source: str, delete: bool = False):
    """
    Moves files from the folder's directory to its parent's directory
    :param source: Target folder's directory / location
    :type source: str
    :param delete: Deletes the target folder's directory / location after dumped
    :type delete: bool
    """
    move(source, os.path.dirname(source), delete)


def move(source: str, destination: str, delete: bool = False):
    """
    Moves files from one folder to another folder
    :param source: File's old directory / location
    :type source: str
    :param destination: File's new directory / location
    :type destination: str
    :param delete: Deletes the source folder's directory / location after moved
    :type delete: bool
    """
    for file in os.scandir(source):
        shutil.move(file, destination)

    os.scandir(source)
    if delete:
        os.remove(source)
# endregion