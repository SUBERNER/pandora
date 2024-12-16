import os
import shutil
import zipfile
import Buffle
# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files


def dump(source: str):
    """
    Moves files from the folder's directory to its parent's directory
    :param source: Target folder's directory / location
    :type source: str
    :return Destination path
    """
    try:
        return move(source, os.path.dirname(source))
    except Exception as e:
        Buffle.Display.methods.error_result(source, "dump", str(e))
        return None


def move(source: str, destination: str):
    """
    Moves files from one folder or a single file to another folder
    :param source: File's old directory / location
    :type source: str
    :param destination: File's new directory / location
    :type destination: str
    :return Destination path
    """
    try:
        # If source is a directory
        if os.path.isdir(source):
            for file in os.scandir(source):
                if file.is_file() or file.is_dir():  # Move files
                    shutil.move(file.path, destination)
                    Buffle.Display.methods.result(source, "move", os.path.join(destination, os.path.basename(file.path)), os.path.dirname(file.path))

        # If source is a single file
        elif os.path.isfile(source):
            # Special handling for ZIP files
            if zipfile.is_zipfile(source):
                shutil.move(source, destination)
            else:
                shutil.move(source, destination)
            Buffle.Display.methods.result(source, "move", os.path.dirname(destination), os.path.dirname(source))

        return destination
    except Exception as e:
        Buffle.Display.methods.error_result(source, "move", str(e))
        return None


def zip(source: str, extension: str = "zip"):
    """
    Compress Zip files.
    :param source: File's directory / location
    :type source: str
    :param extension: the compressing format for the files and folders
    :type extension: str
    :return Zip file path
    """
    try:
        extension = extension.replace('.', '')
        new_source = shutil.make_archive(source, extension, source)

        Buffle.Display.methods.result(source, "zip", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(source, "zip", str(e))
        return None


def unzip(source: str):
    """
    Extracts Zip files.
    :param source: File's directory / location
    :type source: str
    :return Unzipped file path
    """
    try:
        new_source = os.path.splitext(source)[0]  # removes the extension form the zip file

        # removes the extra . added in the extension before used
        shutil.unpack_archive(source, new_source)

        Buffle.Display.methods.result(source, "unzip", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(source, "unzip", str(e))
        return None


def delete(source: str):
    """
    Deletes a file or folder
    :param source: File's directory / location
    :type source: str
    :return deleted file's path (should be None)
    """
    try:
        source = os.path.normpath(source)

        if os.path.isfile(source):
            if zipfile.is_zipfile(source):  # Check if it's a ZIP file
                os.remove(source)  # Delete the ZIP file
            else:
                os.remove(source)  # Delete the file
        elif os.path.isdir(source):
            shutil.rmtree(source)  # Delete the directory

        if os.path.exists(source):  # used for better results
            new_source = os.path.basename(source)
        else:
            new_source = None

        Buffle.Display.methods.result(source, "delete", new_source, os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(source, "delete", str(e))
        return None


def create(source: str):
    """
    Creates a folder
    :param source: Folder's directory / location
    :type source: str
    :return created folder's path
    """
    try:
        os.mkdir(source)

        if not os.path.isdir(source):  # if folder cannot be found after created
            source = None

        Buffle.Display.methods.result(source, "delete", source, None)

        return source
    except Exception as e:
        Buffle.Display.methods.error_result(source, "delete", str(e))
        return None


def rename(source: str, name: str):
    """
    Renames a file or folder
    :param source: File's directory / location
    :type source: str
    :param name: New name for the file or folder
    :type name: str
    :return file or folder path after new name
    """
    try:
        new_source = os.path.join(os.path.dirname(source), name)
        os.rename(source, new_source)

        Buffle.Display.methods.result(source, "rename", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(source, "rename", str(e))
        return None


def reextension(source: str, extension: str):
    """
    Changes a files extension
    :param source: File's directory / location
    :type source: str
    :param extension: New type of extension
    :type extension: str
    :return file or folder path after new extension
    """
    try:
        sor, ext = os.path.splitext(source)
        # removes the extra . added in the extension before used
        new_source = sor + '.' + extension.replace('.', '')  # updated extension
        os.rename(source, new_source)

        Buffle.Display.methods.result(source, "reextension", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(source, "reextension", str(e))
        return None

