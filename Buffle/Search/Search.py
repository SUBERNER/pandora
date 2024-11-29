import os
from typing import Literal

# used to determine how the search finds files
_TYPE_SEARCH = Literal["any", "all"]


# region FULL
def full(source: str, deep_search: bool, inverse_search: bool):
    files = []  # will store all files found in this search

    if not inverse_search:  # ignores everything but the source in an inverse_search
        files.extend([f.path for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

    if deep_search:  # if enabled, will also go through all subfolders inside source
        folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
        for folder in folders:  # goes through each folder
            files.extend([f.path for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

    return files  # returns all files in a list
# endregion


# region NAME
def name(source: str, contains: str | list[str], deep_search: bool, inverse_search: bool, type_search: _TYPE_SEARCH = "all"):
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


    return files  # returns all files in a list
# endregion


# region CONTENT
def content(source: str, contains: str | list[str], deep_search: bool, inverse_search: bool, type_search: _TYPE_SEARCH = "all"):
    original_files = []  # will store all files found in this search
    formatted_files = []  # will store all the files after determining their content

    # makes contains always a list
    if isinstance(contains, str):
        contains = [contains]
    print(contains)

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

    return formatted_files  # returns all files in a list
# endregion