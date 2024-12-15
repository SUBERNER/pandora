import os
import shutil
import Buffle
# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files


def dump(source: str):
    """
    Moves files from the folder's directory to its parent's directory
    :param source: Target folder's directory / location
    :type source: str
    """
    try:
        move(source, os.path.dirname(source))
    except Exception as e:
        Buffle.Display.methods.error_result(source, "dump", str(e.args))


def move(source: str, destination: str):
    """
    Moves files from one folder or a single file to another folder
    :param source: File's old directory / location
    :type source: str
    :param destination: File's new directory / location
    :type destination: str
    """
    try:
        # If source is a directory
        if os.path.isdir(source):
            for file in os.scandir(source):
                if file.is_file():  # Only move files, not subdirectories
                    shutil.move(file.path, destination)
                    Buffle.Display.methods.result(source, "move", os.path.dirname(destination), os.path.dirname(file.path))

        # If source is a single file
        elif os.path.isfile(source):
            shutil.move(source, destination)
            Buffle.Display.methods.result(source, "move", os.path.dirname(destination), os.path.dirname(source))

    except Exception as e:
        Buffle.Display.methods.error_result(source, "move", str(e.args))


def zip(source: str, extension: str = "zip"):
    """
    Creates Zip files and renames extension, formatting the mod / addon
    :param source: File's old directory / location
    :type source: str
    :param extension:
    :type extension: str
    """
    try:
        zip_source = shutil.make_archive(os.path.basename(source), "zip", source)

        # Adds the correct extension
        sor, ext = os.path.splitext(zip_source)
        new_source = sor + extension  # updated extension
        os.rename(zip_source, new_source)

        Buffle.Display.methods.result(source, "zip", os.path.basename(new_source), os.path.basename(source))

    except Exception as e:
        Buffle.Display.methods.error_result(source, "zip", str(e.args))


def delete(source: str):
    """
    Deletes a file or folder
    :param source: File's directory / location
    :type source: str
    """
    try:
        os.remove(source)
        if os.path.exists(source):  # used for better results
            new_source = os.path.basename(source)
        else:
            new_source = None

        Buffle.Display.methods.result(source, "delete", new_source, os.path.basename(source))

    except Exception as e:
        Buffle.Display.methods.error_result(source, "delete", str(e))


def rename(source: str, name: str):
    """
    Renames a file or folder
    :param source: File's directory / location
    :type source: str
    :param name: New name for the file or folder
    :type name: str
    """
    try:
        os.rename(source, os.path.dirname(source) + name)
        Buffle.Display.methods.result(source, "rename", os.path.basename(source), os.path.basename(source))

    except Exception as e:
        Buffle.Display.methods.error_result(source, "rename", str(e))


