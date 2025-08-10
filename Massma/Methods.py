from Massma import random  # used for seeds
import Massma
import os
import shutil
import gc  # cleaner file handling


def seed(value: int) -> int:
    """
    Sets the seed value for random operations.

    Parameters:
        value (int): The seed value to set.

    Returns:
        int: The seed value used.
    """
    try:
        random.seed(value)  # changed the randomness of the library
        Massma.Display.methods.result(os.getcwd(), "seed", "Unknown", value)
        return value
    except Exception as e:
        Massma.Display.methods.result_error(os.getcwd(), "seed", e)
        return value


def move(source: str | list[str], destination: str, *, garbage_collection: bool = True) -> str:
    """
    Moves a file or directory to a new location.

    Parameters:
        source (str | list[str]): The file or folder to move.

        destination (str): The target directory.

    Keyword Parameters:
        garbage_collection (bool): If True, forces garbage collection before operation to prevent file locks. Defaults to True.

    Returns:
        str: The new location of the moved file or directory.
    """
    try:
        if garbage_collection:
            gc.collect()  # Close any lingering file handles

        destination = shutil.move(source, destination)
        Massma.Display.methods.result(source, "move", os.path.abspath(source), os.path.abspath(destination))

        return destination
    except Exception as e:
        Massma.Display.methods.result_error(source, "move", e)
        return source


def copy(source: str | list[str], destination: str, *, garbage_collection: bool = True) -> str:
    """
    Copies a file or directory to a new location.

    Parameters:
        source (str | list[str]): The file or folder to copy.

        destination (str): The target directory.

    Keyword Parameters:
        garbage_collection (bool): If True, forces garbage collection before operation to prevent file locks. Defaults to True.

    Returns:
        str: The new location of the copied file or directory.
    """
    try:
        if garbage_collection:
            gc.collect()  # Close any lingering file handles

        if os.path.isfile(source):  # copying files
            destination = shutil.copy2(source, destination)
        elif os.path.isdir(source):  # copying folders
            destination = shutil.copytree(source, destination)

        Massma.Display.methods.result(source, "copy", os.path.abspath(source), os.path.abspath(destination))

        return destination
    except Exception as e:
        Massma.Display.methods.result_error(source, "copy", e)
        return source


def zip(source: str, extension: str) -> str:
    """
    Compresses files or folders into an archive.

    Parameters:
        source (str): Path to the file or folder to be compressed.

        extension (str): Compression format (e.g., "zip").

    Returns:
        str: Path to the created archive.
    """
    original_source = source  # used for better displays
    try:
        extension = extension.replace('.', '')  # corrects extensions
        new_source = shutil.make_archive(source, extension, source)

        if not os.path.exists(source):  # checks if zip is being created form nothing
            Massma.Display.methods.result_warning(source, "zip", 'zipped file or folder created from nothing')
            source = "None"

        Massma.Display.methods.result(original_source, "zip", os.path.basename(source), os.path.basename(new_source))

        return new_source
    except Exception as e:
        Massma.Display.methods.result_error(original_source, "zip", e)
        return original_source


def unzip(source: str) -> str:
    """
    Extracts the contents of an archive.

    Parameters:
        source (str): Path to the archive to be extracted.

    Returns:
        str: Path to the extracted content.
    """
    try:
        new_source = os.path.splitext(source)[0]  # removes the extension form the zip file
        shutil.unpack_archive(source, new_source)

        Massma.Display.methods.result(source, "unzip", os.path.basename(source), os.path.basename(new_source))

        return source
    except Exception as e:
        Massma.Display.methods.result_error(source, "unzip", e)
        return source


def delete(source: str, *, garbage_collection: bool = True) -> str | None:
    """
    Deletes a file or directory.

    Parameters:
        source (str): Path to the file or folder to be deleted.

    Keyword Parameters:
        garbage_collection (bool): If True, forces garbage collection before operation to prevent file locks. Defaults to True.

    Returns:
        None if the deletion is successful, otherwise returns the original source.
    """
    original_source = source  # used for better displays
    try:
        if garbage_collection:
            gc.collect()  # Close any lingering file handles

        if os.path.exists(source):
            if os.path.isfile(source):  # deleting files
                os.remove(source)
            elif os.path.isdir(source):  # deletes folders
                shutil.rmtree(source)
        else:  # if no file was found
            Massma.Display.methods.result_warning(original_source, "delete", 'file or folder dose not exist')
            source = None

        Massma.Display.methods.result(original_source, "delete", source, None)

        return None
    except Exception as e:
        Massma.Display.methods.result_error(source, "delete", e)
        return source


def create_folder(source: str) -> str | None:
    """
    Creates a new folder.

    Parameters:
        source (str): Path of the new folder to create.

    Returns:
        str: Path of the created folder, or None if an error occurs.
    """
    try:
        os.mkdir(source)
        Massma.Display.methods.result(source, "create folder", None, source)

        return source
    except Exception as e:
        Massma.Display.methods.result_error(source, "create_folder", e)
        return None


def create_file(source: str) -> str | None:
    """
    Creates a new empty file.

    Parameters:
        source (str): Path of the new file to create.

    Returns:
        str: Path of the created file, or None if an error occurs.
    """
    try:
        with open(source, 'x'):
            pass  # creates file
        Massma.Display.methods.result(source, "create file", None, source)

        return source
    except Exception as e:
        Massma.Display.methods.result_error(source, "create file", e)
        return None


def redo_name(source: str, name: str, *, garbage_collection: bool = True) -> str:
    """
    Renames a file or folder.

    Parameters:
        source (str): Path to the existing file or folder.

        name (str): New name for the file or folder.

    Keyword Parameters:
        garbage_collection (bool): If True, forces garbage collection before operation to prevent file locks. Defaults to True.

    Returns:
        str: New path after renaming.
    """
    try:
        if garbage_collection:
            gc.collect()  # Close any lingering file handles

        new_source = os.path.join(os.path.dirname(source), name)
        os.rename(source, new_source)

        Massma.Display.methods.result(source, "redo name", os.path.basename(source), os.path.basename(new_source))

        return new_source
    except Exception as e:
        Massma.Display.methods.result_error(source, "redo name", e)
        return source


def redo_extension(source: str, extension: str, *, garbage_collection: bool = True) -> str:
    """
    Changes the file extension.

    Parameters:
        source (str): Path to the existing file.

        extension (str): New extension for the file.

    Keyword Parameters:
        garbage_collection (bool): If True, forces garbage collection before operation to prevent file locks. Defaults to True.

    Returns:
        str: New path after renaming.
    """
    try:
        if garbage_collection:
            gc.collect()  # Close any lingering file handles

        sor, ext = os.path.splitext(source)
        # removes the extra . added in the extension before used
        new_source = sor + '.' + extension.replace('.', '')  # updated extension
        os.rename(source, new_source)

        Massma.Display.methods.result(source, "redo extension", os.path.basename(source), os.path.basename(new_source))

        return new_source
    except Exception as e:
        Massma.Display.methods.result_error(source, "redo extension", e)
        return source
