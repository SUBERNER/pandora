import os
import shutil
import random


# shuffles all file names inside a directory
def directory(directory: str, dump=False):
    i = 0  # indexing files
    os.chdir(directory)  # changes directory

    files = os.scandir()  # stores the actual files
    names = os.listdir()  # stores the file names

    for file in files:
        os.rename(file.name, str(i) + os.path.splitext(file)[1])
        i += 1

    files = os.scandir(directory)  # updates to files new names

    for file in files:
        if file.is_dir() or file.is_file():
            __shuffle(file, names)

    if dump:
        __dump(files, directory)


# shuffles all files that have the string in their name
def name(directory: str, contains: str, dump=False):
    i = 0  # indexing files
    os.chdir(directory)  # changes directory

    files = os.scandir()  # stores the actual files
    names = os.listdir()  # stores the file names

    names = [name for name in names if contains in name]  # removes everything not matching

    for file in files:
        if (file.is_dir() or file.is_file()) and contains in file.name:
            os.rename(file.name, str(i) + os.path.splitext(file)[1])
            i += 1

    files = os.scandir(directory)  # updates to files new names

    for file in files:
        if (file.is_dir() or file.is_file()) and os.path.basename(file)[0].isdigit():
            __shuffle(file, names)

    if dump:
        __dump(files, directory)


def __shuffle(file, names: list):
    random_name = random.choice(names)  # selects a file name
    os.rename(file.name, random_name)  # renames file
    names.remove(random_name)


# dumps file to parent folder
def __dump(files: list, directory: str):
    for file in os.scandir():
        shutil.move(file, os.path.dirname(directory))