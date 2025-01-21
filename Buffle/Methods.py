from Buffle import random  # used for seeds
import os
import shutil
import zipfile
import Buffle
# Methods will not be accessed from this file but from Buffle itself
# These are to be used from the player from the parent folder Buffle and to be use dy other .py files


def seed(value: int):
    """
    Moves a singular file or folder from one directory to another.

    Parameter:
        source (str): Path of the file or folder being moved.

        destination (str): Path of the new directory for the file or folder.

    Return:
        str | None: Path of the moved file or folder, or None if an error occurs.
    """
    try:
        random.seed(value)
        Buffle.Display.methods.result(f"None", "seed", value, 0)
        return value
    except Exception as e:
        Buffle.Display.methods.error_result(f"None", "seed", str(e.args))
        return None


def move(source: str, destination: str) -> str | None:
    """
    Moves a singular file or folder from one directory to another.

    Parameter:
        source (str): Path of the file or folder being moved.

        destination (str): Path of the new directory for the file or folder.

    Return:
        str | None: Path of the moved file or folder, or None if an error occurs.
    """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        destination = shutil.move(source, destination)

        if not os.path.exists(destination):  # checks if file or folder was moved correctly
            Buffle.Display.methods.warning_result(original_source, "move", 'destination file or folder could not be found')
            destination = None

        Buffle.Display.methods.result(original_source, "move", os.path.abspath(destination), os.path.abspath(source))

        return destination
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "move", str(e.args))
        return None


def copy(source: str, destination: str) -> str | None:
    """
    Copies a singular file or folder from one directory to another.

    Parameter:
        source (str): Path of the file or folder being copied.

        destination (str): Path of the new directory for the file or folder.

    Return:
        str | None: Path of the copied file or folder, or None if an error occurs.
    """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        if os.path.isfile(source):  # files
            destination = shutil.copy2(source, destination)
        elif os.path.isdir(source):  # folders
            destination = shutil.copytree(source, destination)

        if not os.path.exists(destination):  # checks if file or folder was moved correctly
            Buffle.Display.methods.warning_result(original_source, "move", 'destination file or folder could not be found')
            destination = None

        Buffle.Display.methods.result(original_source, "copy", os.path.abspath(destination), os.path.abspath(source))

        return destination
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "copy", str(e.args))
        return None


def zip(source: str, extension: str = "zip") -> str | None:
    """
    Compresses files or folders into a zip archive.

    Parameter:
        source (str): Path of the file or folder to compress.

        extension (str): Compression format, defaults to "zip".

    Return:
        str | None: Path of the created zip archive, or None if an error occurs.
        """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        extension = extension.replace('.', '')

        new_source = shutil.make_archive(source, extension, source)

        source = os.path.basename(source)  # formats for Display

        # checks if zip file is empty and warns
        with zipfile.ZipFile(new_source, 'r') as zip_ref:
            if len(zip_ref.namelist()) == 0:
                Buffle.Display.methods.warning_result(original_source, "zip", 'zipped file or folder is empty')

        Buffle.Display.methods.result(original_source, "zip", os.path.basename(new_source), source)

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "zip", str(e.args))
        return None


def unzip(source: str) -> str | None:
    """
    Extracts the contents of a zip archive.

    Parameter:
        source (str): Path of the zip archive.

    Return:
        str | None: Path of the extracted contents, or None if an error occurs.
    """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        new_source = os.path.splitext(source)[0]  # removes the extension form the zip file
        shutil.unpack_archive(original_source, new_source)

        if not os.path.exists(source):
            Buffle.Display.methods.warning_result(original_source, "unzip", 'zipped file or folder does not existed')
            source = None

        Buffle.Display.methods.result(original_source, "unzip", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "unzip", str(e.args))
        return None


def delete(source: str) -> str | None:
    """
    Deletes a file or folder.

    Parameter:
        source (str): Path of the file or folder to delete.

    Return:
        str | None: Path of the deleted file or folder, or None if an error occurs.
    """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        source = os.path.normpath(source)  # Normalizes path

        if os.path.exists(source):
            if os.path.isfile(source):  # used for deleting non-zip or zip files
                os.remove(source)
            elif os.path.isdir(source):  # deletes folders
                shutil.rmtree(source)
        else:  # if no file was found
            Buffle.Display.methods.warning_result(original_source, "delete", 'file or folder dose not exist')
            source = None

        # checks if it exists, used for the results
        if os.path.exists(original_source):
            Buffle.Display.methods.warning_result(original_source, "delete", 'file or folder still exists')
            new_source = source
        else:
            new_source = None

        Buffle.Display.methods.result(original_source, "delete", new_source, source)

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "delete", str(e.args))
        return None


def create_folder(source: str) -> str | None:
    """
    Creates a new folder.

    Parameter:
        source (str): Path of the new folder to create.

    Return:
        str | None: Path of the created folder, or None if an error occurs.
    """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        source = os.path.normpath(source)  # Normalizes path
        os.mkdir(source)  # makes the folder

        if not os.path.exists(source):   # checks if folder was correctly made
            Buffle.Display.methods.warning_result(original_source, "create folder", 'source folder could not be found')
            source = None

        Buffle.Display.methods.result(original_source, "create folder", source, None)

        return source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "create folder", str(e.args))
        return None


def create_file(source: str) -> str | None:
    """
    Creates a new file.

    Parameter:
        source (str): Path of the new file to create.

    Return:
        str | None: Path of the created file, or None if an error occurs.
    """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        source = os.path.normpath(source)  # Normalizes path
        with open(source, 'x') as file:
            pass  # creates file

        if not os.path.exists(source):   # checks if file was correctly made
            Buffle.Display.methods.warning_result(original_source, "create file", 'source file could not be found')
            source = None

        Buffle.Display.methods.result(original_source, "create file", source, None)

        return source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "create file", str(e.args))
        return None


def redo_name(source: str, name: str) -> str | None:
    """
        Renames a file or folder.

        Parameter:
            source (str): Current path of the file or folder.

            name (str): New name for the file or folder.

        Return:
            str | None: Path of the renamed file or folder, or None if an error occurs.
        """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        new_source = os.path.join(os.path.dirname(source), name)
        os.rename(source, new_source)

        Buffle.Display.methods.result(original_source, "redo name", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "redo name", str(e.args))
        return None


def redo_extension(source: str, extension: str) -> str | None:
    """
        Changes the extension of a file.

        Parameter:
            source (str): Current path of the file.

            extension (str): New extension for the file.

        Return:
            str | None: Path of the file with the new extension, or None if an error occurs.
        """
    original_source = source
    try:
        os.chmod(source, 0o755)  # rewrites file permissions
        sor, ext = os.path.splitext(source)
        # removes the extra . added in the extension before used
        new_source = sor + '.' + extension.replace('.', '')  # updated extension
        os.rename(source, new_source)

        Buffle.Display.methods.result(original_source, "redo extension", os.path.basename(new_source), os.path.basename(source))

        return new_source
    except Exception as e:
        Buffle.Display.methods.error_result(original_source, "redo extension", str(e.args))
        return None