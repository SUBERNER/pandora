import os
import shutil
import random


# shuffles all file names inside a directory
def directory(directory: str, dump=False):
    os.chdir(directory)  # changes directory

    files = os.scandir()  # stores the actual files
    names = os.listdir()  # stores the file names

    __shuffle(files, names, directory)

    if dump:  # dumps file to parent folder
        for file in os.scandir():
            shutil.move(file, os.path.dirname(directory))


# shuffles all files that have the string in their name
def name(directory: str, contains: str, dumb=False):
    shuffledText = []  # stores all the text that will be shuffled


def __shuffle(files: list, names: list, directory: str):
    i = 0  # indexing files
    for file in files:
        os.rename(file.name, str(i) + os.path.splitext(file)[1])
        i += 1

    files = os.scandir(directory)  # updates to files new names

    for file in files:
        if file.is_dir() or file.is_file():
            random_name = random.choice(names)  # selects a file name
            os.rename(file.name, random_name)  # renames file
            names.remove(random_name)

