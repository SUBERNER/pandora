import os
import shutil
import random


# shuffles all file names inside a directory
def directory(directory: str, dump=False):
    i = 0  # indexing files
    os.chdir(directory)  # changes directory

    files = os.scandir()  # stores the actual files
    names = os.listdir()  # stores the file names

    # formats files to be altered
    for file in files:
        os.rename(file.name, str(i) + os.path.splitext(file)[1])
        i += 1

    files = os.scandir(directory)  # updates to files new names

    # alters files
    for file in files:
        if file.is_dir() or file.is_file():
            random_name = random.choice(names)  # selects a file name
            os.rename(file.name, random_name)  # renames file
            names.remove(random_name)

    if dump:
        __dump(directory)


# shuffles all files that have the string in their name
def name(directory: str, contains: str, dump=False):
    i = 0  # indexing files
    os.chdir(directory)  # changes directory

    files = os.scandir()  # stores the actual files
    names = os.listdir()  # stores the file names

    names = [name for name in names if contains in name]  # removes everything not matching

    # formats files to be altered
    for file in files:
        if (file.is_dir() or file.is_file()) and contains in file.name:
            os.rename(file.name, str(i) + os.path.splitext(file)[1])
            i += 1

    files = os.scandir(directory)  # updates to files new names

    # alters files
    for file in files:
        if (file.is_dir() or file.is_file()) and os.path.basename(file)[0].isdigit():
            random_name = random.choice(names)  # selects a file name
            os.rename(file.name, random_name)  # renames file
            names.remove(random_name)

    if dump:
        __dump(directory)


# HELL TO EXPLAIN AND CODE (WILL DO LATER)
def group(directory: str, contains: list, dump=False):
    i = 0  # indexing files
    os.chdir(directory)  # changes directory

    files = os.scandir()  # stores the actual files
    names = contains.copy()  # copies for alterations

    # formats files to be altered
    for contain in contains:
        files = os.scandir()  # refresh files list after each renaming
        for file in files:
            if contain in file.name:
                name = file.name.replace(contain, str(i))  # replaces a part of the string with a number
                os.rename(file.name, name)
        i += 1

    i -= 1  # removes last indent
    files = os.scandir(directory)  # updates to files new names

    # alters files
    while i >= 0:
        files = os.scandir(directory)  # updates to files new names
        random_name = random.choice(names)  # selects a file name
        for file in files:
            if (file.is_dir() or file.is_file()) and str(i) in file.name:
                os.rename(file.name, file.name.replace(str(i), random_name))  # renames file
        names.remove(random_name)
        i -= 1

    if dump:
        __dump(directory)


# reverses all files inside a directory
def reverse(directory: str, dump=False):
    i = 0  # indexing files
    os.chdir(directory)  # changes directory

    files = os.scandir()  # stores the actual files
    names = os.listdir()  # stores the file names

    # formats files to be altered
    for file in files:
        os.rename(file.name, str(i) + os.path.splitext(file)[1])
        i += 1

    files = os.scandir(directory)  # updates to files new names
    names.reverse()

    # alters files
    for file in files:
        if file.is_dir() or file.is_file():
            os.rename(file.name, names[0])  # renames file
            names.remove(names[0])

    if dump:
        __dump(directory)


# dumps file to parent folder
def __dump(directory: str):
    for file in os.scandir():
        shutil.move(file, os.path.dirname(directory))