import os
import shutil
import Buffle
# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files


def move(source: str, destination: str) -> str | None:
    """
    Moves a file or folder from one directory to another directory
    :param source: Path of file or folder being moved.
    :type source: str
    :param destination: Path of new directory for the file or folder being moved
    :type destination: str
    :return destination
    """
    original_source = source
    try:
        shutil.move(source, destination)

        os.path.abspath(destination)  # formats for Display
        if not os.path.exists(destination):
            Buffle.Display.methods.warning_result(original_source, "move", 'Destination file or folder could not be found')
            destination = None

        Buffle.Display.methods.result(original_source, "move", destination, os.path.dirname(source))

        return destination
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "move", str(e.args))
        return None


def zip(source: str, extension: str = "zip") -> str | None:
    """
    Compress Zip files.
    :param source: File's directory / location
    :type source: str
    :param extension: the compressing format for the files and folders
    :type extension: str
    :return Zip file path
    """
    original_source = source
    try:
        extension = extension.replace('.', '')

        new_source = shutil.make_archive(source, extension, source)

        source = os.path.basename(source)  # formats for Display
        if not os.path.exists(source):
            Buffle.Display.methods.warning_result(original_source, "zip", 'Unzipped file or folder could not be found')
            source = None

        Buffle.Display.methods.result(original_source, "zip", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "zip", str(e.args))
        return None


def unzip(source: str) -> str | None:
    """
    Extracts Zip files.
    :param source: File's directory / location
    :type source: str
    :return Unzipped file path
    """
    original_source = source
    try:
        new_source = os.path.splitext(source)[0]  # removes the extension form the zip file
        shutil.unpack_archive(original_source, new_source)

        if not os.path.exists(source):
            Buffle.Display.methods.warning_result(original_source, "unzip", 'Zipped file or folder does not existed')
            source = None

        Buffle.Display.methods.result(original_source, "unzip", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "unzip", str(e.args))
        return None


def delete(source: str) -> str | None:
    """
    Deletes a file or folder
    :param source: File's directory / location
    :type source: str
    :return deleted file's path (should be None)
    """
    original_source = source
    try:
        source = os.path.normpath(source)  # Normalizes path

        if os.path.exists(source):
            if os.path.isfile(source):  # used for deleting non-zip or zip files
                os.remove(source)
            elif os.path.isdir(source):  # deletes folders
                shutil.rmtree(source)
        else:  # if no file was found
            Buffle.Display.methods.warning_result(original_source, "delete", ' Source file or folder dose not exist')
            source = ''

        # checks if it exists, used for the results
        if os.path.exists(source):
            new_source = source
        else:
            new_source = None

        Buffle.Display.methods.result(original_source, "delete", new_source, os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "delete", str(e.args))
        return None


def create_folder(source: str) -> str | None:
    """
    Creates a folder
    :param source: Folder's directory / location
    :type source: str
    :return created folder's path
    """
    original_source = source
    try:
        source = os.path.normpath(source)  # Normalizes path
        os.mkdir(source)  # makes the folder

        if not os.path.exists(source):   # checks if folder was correctly made
            Buffle.Display.methods.warning_result(original_source, "create folder", 'Source folder could not be found')
            source = None

        Buffle.Display.methods.result(original_source, "create folder", source, None)

        return source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "create folder", str(e.args))
        return None


def create_file(source: str) -> str | None:
    """
    Creates a file
    :param source: File's directory / location
    :type source: str
    :return created file's path
    """
    original_source = source
    try:
        source = os.path.normpath(source)  # Normalizes path
        with open(source, 'x') as file:
            pass  # creates file

        if not os.path.exists(source):   # checks if file was correctly made
            Buffle.Display.methods.warning_result(original_source, "create file", 'Source file could not be found')
            source = None

        Buffle.Display.methods.result(original_source, "create file", source, None)

        return source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "create file", str(e.args))
        return None


def redo_name(source: str, name: str) -> str | None:
    """
    Renames a file or folder
    :param source: File's directory / location
    :type source: str
    :param name: New name for the file or folder
    :type name: str
    :return file or folder path after new name
    """
    original_source = source
    try:
        new_source = os.path.join(os.path.dirname(source), name)
        os.rename(source, new_source)

        Buffle.Display.methods.result(original_source, "redo name", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "redo name", str(e.args))
        return None


def redo_extension(source: str, extension: str) -> str | None:
    """
    Changes a files extension
    :param source: File's directory / location
    :type source: str
    :param extension: New type of extension
    :type extension: str
    :return file or folder path after new extension
    """
    original_source = source
    try:
        sor, ext = os.path.splitext(source)
        # removes the extra . added in the extension before used
        new_source = sor + '.' + extension.replace('.', '')  # updated extension
        os.rename(source, new_source)

        Buffle.Display.methods.result(original_source, "redo extension", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "redo extension", str(e.args))
        return None

