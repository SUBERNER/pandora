import Buffle
import random
import os


def full(source: str, *, deep_search: bool, inverse_search: bool, chance: float = 1) -> list[str] | None:
    """
    Searches for files in a directory.

    parameter:
        source (str): Directory being searched.

    keyword parameter:
        deep_search (bool): Includes files from all subdirectories inside the directory.

        inverse_search (bool): Searches for files that do NOT match the specified criteria.

        chance (float): Probability of retrieving each file. Defaults to 1.
            - 0.0: No file(s) are retrieved.
            - 1.0: All file(s) are retrieved.

    return:
        (list[str]) | None: List of file paths found during the search, or None if an error occurs.
    """
    try:
        files = []  # will store all files found in this search

        if not inverse_search:  # ignores everything but the source in an inverse_search
            files.extend([f.path for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

        if deep_search:  # if enabled, will also go through all subfolders inside source
            folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
            for folder in folders:  # goes through each folder
                if folder == source:  # skips source folder, as it is already scanned in the first if
                    continue
                files.extend([f.path for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

        # test chances to see if files will stay in list
        for file in files:
            if chance <= random.random():
                files.remove(file)

        Buffle.Display.search.result(source, "full search", len(files), 0)
        return files  # returns all files in a list
    except Exception as e:
        Buffle.Display.audio.error_result(source, "full search", str(e.args))
        return None


def name(source: str, contains: str | list[str], *, deep_search: bool, inverse_search: bool, type_search="all", chance: float = 1) -> list[str] | None:
    """
    Searches for files in a directory whose names match a specific substring.

    parameter:
        source (str): Directory being searched.

        contains (str | list[str]): Substring(s) to look for in file names.

    keyword parameter:
        deep_search (bool): Includes files from all subdirectories inside the directory.

        inverse_search (bool): Searches for files that do NOT match the specified criteria.

        type_search (str): Determines matching criteria, defaults to "all".
            - "all": File(s) must contain all specified substrings.
            - "any": File(s) must contain at least one of the specified substrings.

        chance (float): Probability of retrieving each file. Defaults to 1.
            - 0.0: No file(s) are retrieved.
            - 1.0: All file(s) are retrieved.

    return:
        (list[str]) | None: List of file paths found during the search, or None if an error occurs.
    """
    try:
        files = []  # will store all files found in this search

        # makes contains always a list
        if isinstance(contains, str):
            contains = [contains]

        if type_search == "all":
            files.extend([f.path for f in os.scandir(source) if f.is_file() and ((all(contain in f.name for contain in contains) and not inverse_search) or (any(contain not in f.name for contain in contains) and inverse_search))])  # gets all files with the substring inside source directory
        elif type_search == "any":
            files.extend([f.path for f in os.scandir(source) if f.is_file() and ((any(contain in f.name for contain in contains) and not inverse_search) or (all(contain not in f.name for contain in contains) and inverse_search))])  # gets all files with the substring inside source directory

        if deep_search:  # if enabled, will also go through all subfolders inside source
            folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
            for folder in folders:  # goes through each folder
                if type_search == "all":
                    files.extend([f.path for f in os.scandir(folder) if f.is_file() and ((all(contain in f.name for contain in contains) and not inverse_search) or (any(contain not in f.name for contain in contains) and inverse_search))])  # gets all files with the substring inside source directory
                elif type_search == "any":
                    files.extend([f.path for f in os.scandir(folder) if f.is_file() and ((any(contain in f.name for contain in contains) and not inverse_search) or (all(contain not in f.name for contain in contains) and inverse_search))])  # gets all files with the substring inside source directory

        # test chances to see if files will stay in list
        for file in files:
            if chance <= random.random():
                files.remove(file)

        Buffle.Display.search.result(source, "name search", len(files), 0)
        return files  # returns all files in a list
    except Exception as e:
        Buffle.Display.audio.error_result(source, "name search", str(e.args))
        return None


def content(source: str, contains: str | list[str], *, deep_search: bool, inverse_search: bool, type_search="all", chance: float = 1) -> list[str] | None:
    """
    Searches for files in a directory whose contents match a specific substring.

    parameter:
        source (str): Directory being searched.

        contains (str | list[str]): Substring(s) to look for in file names.

    keyword parameter:
        deep_search (bool): Includes files from all subdirectories inside the directory.

        inverse_search (bool): Searches for files that do NOT match the specified criteria.

        type_search (str): Determines matching criteria, defaults to "all".
            - "all": File(s) must contain all specified substrings.
            - "any": File(s) must contain at least one of the specified substrings.

        chance (float): Probability of retrieving each file. Defaults to 1.
            - 0.0: No file(s) are retrieved.
            - 1.0: All file(s) are retrieved.

    return:
        (list[str]) | None: List of file paths found during the search, or None if an error occurs.
    """
    try:
        original_files = []  # will store all files found in this search
        formatted_files = []  # will store all the files after determining their content

        # makes contains always a list
        if isinstance(contains, str):
            contains = [contains]

        original_files.extend([f for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

        if deep_search:  # if enabled, will also go through all subfolders inside source
            folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
            for folder in folders:  # goes through each folder
                original_files.extend([f for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

        # determines if substring is or is not inside file
        for entry in original_files:
            if entry.is_file():
                with open(entry, 'r') as file:
                    text = file.read()
                    if type_search == "all":
                        if ((all(contain in text for contain in contains) and not inverse_search) or (any(contain not in text for contain in contains) and inverse_search)):  # determines if contains is inside the file text
                            formatted_files.append(entry.path)
                    elif type_search == "any":
                        if ((any(contain in text for contain in contains) and not inverse_search) or (all(contain not in text for contain in contains) and inverse_search)):  # determines if contains is not inside the file text
                            formatted_files.append(entry.path)

        # test chances to see if files will stay in list
        for file in formatted_files:
            if chance <= random.random():
                formatted_files.remove(file)

        Buffle.Display.search.result(source, "content search", len(formatted_files), 0)
        return formatted_files  # returns all files in a list
    except Exception as e:
        Buffle.Display.audio.error_result(source, "content search", str(e.args))
        return None
