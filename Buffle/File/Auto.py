import os
import random
import Buffle
import uuid


# shuffles all file names inside a directory
def directory(source: str, dump=False):
    files = [f for f in os.scandir(source) if f.is_file()]  # stores the actual files
    original_names = [f.name for f in files]  # stores the file names

    # renames files to avoid conflict
    temp_names = []  # temporary list of all uuid files
    for file in files:
        temp_name = f"{uuid.uuid4().hex}{os.path.splitext(file.name)[1]}"  # creates unique name for file
        temp_path = os.path.join(source, temp_name)  # creates a path for the file
        os.rename(file.path, temp_path)
        temp_names.append(temp_path)

    # alters files
    random_names = original_names.copy()
    random.shuffle(random_names)
    for temp_path, new_name, original_name in zip(temp_names, random_names, original_names):
        new_path = os.path.join(source, new_name)
        os.rename(temp_path, new_path)
        Buffle.display_file_results.result(source, "Directory Shuffle", original_name, new_name)

    if dump:
        Buffle.dump(source)


# shuffles all files that have the string in their name
def name(source: str, contains: str, dump=False):
    files = [f for f in os.scandir(source) if f.is_file()]  # stores the actual files
    original_names = [f.name for f in files if contains in f.name]  # stores the file names with contain in it

    # renames files to avoid conflict
    temp_names = []  # temporary list of all uuid files
    for file in files:
        temp_name = f"{uuid.uuid4().hex}{os.path.splitext(file.name)[1]}"  # creates unique name for file
        temp_path = os.path.join(source, temp_name)  # creates a path for the file
        os.rename(file.path, temp_path)
        temp_names.append(temp_path)

    # alters files
    random_names = original_names.copy()
    random.shuffle(random_names)
    for temp_path, new_name, original_name in zip(temp_names, random_names, original_names):
        new_path = os.path.join(source, new_name)
        os.rename(temp_path, new_path)
        Buffle.display_file_results.result(source, "Directory Shuffle", original_name, new_name)

    if dump:
        Buffle.dump(source)


# HELL TO EXPLAIN AND CODE (WILL DO LATER)
def group(source: str, contains: list, dump=False):
    i = 0  # indexing files
    os.chdir(source)  # changes directory

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
    files = os.scandir(source)  # updates to files new names

    # alters files
    while i >= 0:
        files = os.scandir(source)  # updates to files new names
        random_name = random.choice(names)  # selects a file name
        for file in files:
            if (file.is_dir() or file.is_file()) and str(i) in file.name:
                os.rename(file.name, file.name.replace(str(i), random_name))  # renames file
        names.remove(random_name)
        i -= 1

    if dump:
        Buffle.dump(source)


# reverses all files inside a directory
def reverse(source: str, dump=False):
    i = 0  # indexing files
    os.chdir(source)  # changes directory

    files = os.scandir()  # stores the actual files
    
    names = os.listdir()  # stores the file names

    # formats files to be altered
    for file in files:
        os.rename(file.name, str(i) + os.path.splitext(file)[1])
        i += 1

    files = os.scandir(source)  # updates to files new names
    names.reverse()

    # alters files
    for file in files:
        if file.is_dir() or file.is_file():
            os.rename(file.name, names[0])  # renames file
            names.remove(names[0])

    if dump:
        Buffle.dump(source)
