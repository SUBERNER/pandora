import os
import shutil


# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files

# region DISPLAY_RESULTS
class DisplayResults:
    # formats for how the file location is displayed
    # 0 = full: full file directory
    # 1 = limited: 2 directories deep
    # 2 = file: only file
    __file_format = None
    # enabled or disabled displaying relevant information
    __display_results = None

    def __init__(self, file_format: int, display_results: bool):
        self.file_format = file_format
        self.display_results = display_results

    @classmethod
    def set_format(cls, format: int = None):
        """
        The format used when displaying file's directory / location
        0 = full | 1 = limited | 2 = file
        :type format: int
        :return Format of displayed file's directory / location
        """
        if format is not None:
            cls.__file_format = format
        return cls.__file_format

    @classmethod
    def set_display(cls, display: bool = None):
        """
        Enables or Disables displaying results from this package's altering methods
        :type display: bool
        :return If results are enabled or disabled for this package's altering methods
        """
        if display is not None:
            cls.__display_results = display
        return cls.__display_results

    @classmethod
    def result(cls, source: str, method: str, updated_value, original_value):
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
                if cls.__file_format == 1:  # limited
                    limited_parts = source.split(os.sep)[-3:]
                    source = os.path.join(*limited_parts)
                elif cls.__file_format == 2:  # file
                    source = source.split("\\")[-1]

                if original_value != updated_value:
                    print(f"{source} <|> {method} <|>   altered <|> [{original_value}] --> [{updated_value}]")
                else:
                    print(f"{source} <|> {method} <|> unaltered <|> [{updated_value}]")
            else:
                print(f"{source} <|> ERROR <|> not file or folder")
        except:
            print(f"{source} <|> ERROR <|> displaying alters")


# all the DisplayResults classes
display_texture_results = DisplayResults(1, True)
display_text_results = DisplayResults(1, True)
display_file_results = DisplayResults(1, True)
display_manual_results = DisplayResults(1, True)
# endregion


# region DIRECTORY
def dump(source: str, delete: bool = False):
    """
    Moves files from the folder's directory to its parent's directory
    :param source: Target folder's directory / location
    :type source: str
    :param delete: Deletes the target folder's directory / location after dumped
    :type delete: bool
    :return destination
    """
    return move(source, os.path.dirname(source), delete)


def move(source: str, destination: str, delete: bool = False):
    """
    Moves files from one folder or a single file to another folder
    :param source: File's old directory / location
    :type source: str
    :param destination: File's new directory / location
    :type destination: str
    :param delete: Deletes the source folder's directory / location after moved
    :type delete: bool
    :return destination
    """
    if source is os.path.isdir():  # multiple files in a folder
        for file in os.scandir(source):
            shutil.move(file, destination)

        os.scandir(source)
        if delete:
            os.remove(source)

    if source is os.path.isfile():  # single file in a folder
        shutil.move(source, destination)

    return destination
# endregion
