import os
import shutil
import Buffle
# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files


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
    if source is os.path.isdir(source):  # multiple files in a folder
        for file in os.scandir(source):
            shutil.move(file, destination)

        os.scandir(source)
        if delete:
            os.remove(source)

    if source is os.path.isfile(source):  # single file in a folder
        shutil.move(source, destination)

    return destination


# STILL NEEDS TO BE WORKED ON
def zip(source: str, name: str, extension: str = None, delete: bool = False):
    """
    Creates Zip files and renames extension, formatting the mod / addon
    :param source: File's old directory / location
    :type source: str
    :param name: Name of the zipped file
    :type name: str
    :param extension:
    :type extension: str
    :param delete:
    :type delete: bool
    :return:
    """
    try:
        zip_source = shutil.make_archive(name, "zip", os.path.dirname(source))

        if extension is not None:  # replaces the zip extension with a custom one
            sor, ext = os.path.splitext(zip_source)
            os.rename(source, sor + extension)

        if delete:
            os.remove(source)

    except Exception as e:
        Buffle.Display.methods.error_result(source, "zip", e.__str__())


