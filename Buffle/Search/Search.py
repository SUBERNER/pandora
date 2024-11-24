import os


# region FULL
def full(source: str, deep_search: bool, inverse_search: bool):
    files = []  # will store all files found in this search

    files.extend([f for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

    if deep_search:  # if enabled, will also go through all subfolders inside source
        folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
        for folder in folders: # goes through each folder
            files.extend([f for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

    return files  # returns all files in a list
# endregion


# region NAME
def name(source: str, contains: str, deep_search: bool, inverse_search: bool):
    files = []  # will store all files found in this search

    files.extend([f for f in os.scandir(source) if f.is_file() and contains in f.name])  # gets all files with the substring inside source directory

    if deep_search:  # if enabled, will also go through all subfolders inside source
        folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
        for folder in folders:  # goes through each folder
            files.extend([f for f in os.scandir(folder) if f.is_file() and contains in f.name])  # gets all files with the substring inside source directory

    return files  # returns all files in a list
# endregion


# region CONTENT
def content(source: str, contains: str, deep_search: bool, inverse_search: bool):
    original_files = []  # will store all files found in this search
    formatted_files = []  # will store all the files after determining their content

    original_files.extend([f for f in os.scandir(source) if f.is_file()])  # gets all files inside source directory

    if deep_search:  # if enabled, will also go through all subfolders inside source
        folders = [f[0] for f in os.walk(source)]  # get all subfolders inside source
        for folder in folders:  # goes through each folder
            original_files.extend([f for f in os.scandir(folder) if f.is_file()])  # gets all files inside source directory

    # determines if substring is inside file
    for entry in original_files:
        with open(entry, 'r') as file:
            if contains in file.read():  # determines if contains is inside the file text
                formatted_files.append(entry)

    return original_files  # returns all files in a list

# endregion