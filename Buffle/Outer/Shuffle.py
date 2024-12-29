import os
import random
import uuid

import Buffle


# shuffles all file names inside a directory
def normal(files: str | list[str]):
    """
    Shuffles and randomizes the names of all files.
    :param files: Target file's paths
    :type files: str | list[str]
    """

    # makes files always a list
    if isinstance(files, str):
        files = [files]

    # gets size of largest path for better result formatting
    Buffle.Display.outer.set_length(max(files, key=len))

    # renames files to avoid conflict
    temp_files = []  # temporary list of all uuid files
    for file in files:
        temp_name = f"{uuid.uuid4().hex}{os.path.splitext(os.path.basename(file))[1]}"  # creates unique name for file
        temp_file = os.path.join(os.path.dirname(file), temp_name)  # creates a path for the file
        os.rename(os.path.abspath(file), temp_file)
        temp_files.append(temp_file)

    # alters files
    random_files = files.copy()
    random.shuffle(random_files)
    for temp_file, new_file, original_file in zip(temp_files, random_files, files):
        os.rename(os.path.abspath(temp_file), os.path.abspath(new_file))
        Buffle.Display.outer.result(os.path.abspath(original_file), "Normal Name Shuffle", os.path.basename(new_file), os.path.basename(original_file))


# HELL TO EXPLAIN AND CODE (WILL DO LATER)
def group(files: str | list[str], contains: list[str]):
    """
    Shuffles and randomizes the 'contains' substrings by groups within file names files in a directory.
    :param files: Target folder's directory
    :param contains: Substrings searched for inside file names
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    # gets size of largest path for better result formatting
    Buffle.Display.outer.set_length(max(files, key=len))

    assign_names = contains.copy()

    temp_names = []  # temporary list of all uuid files
    for contain in contains:
        temp_name = f"{uuid.uuid4().hex}"  # used as a placeholder for the contains text
        temp_names.append(temp_name)
        for index, file in enumerate(files):
            if contain in os.path.basename(file):
                # Replace the substring with the index in the filename
                new_name = os.path.basename(file).replace(contain, temp_name)
                new_path = os.path.join(os.path.dirname(file), new_name)
                os.rename(file, new_path)
                files[index] = new_path

    # alters files
    random.shuffle(assign_names)  # Randomize order for final names
    for i in range(len(contains) - 1, -1, -1):  # Process in reverse order
        target_name = assign_names.pop()  # Select a random name from the list
        contain_name = contains.pop()
        for file in files:
            if temp_names[i] in os.path.basename(file):
                # Replace the index in the filename with the random target name
                final_name = os.path.basename(file).replace(temp_names[i], target_name)
                os.rename(os.path.abspath(file), os.path.join(os.path.dirname(file), final_name))
                Buffle.Display.outer.result(os.path.abspath(file), f"Group Name Shuffle", contain_name, target_name)


# reverses all files inside a directory
def reverse(files: str | list[str]):
    """
    Reverses the order of names of all files from a directory.
    :param files: Target folder's directory
    :type files: str | list[str]
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    # gets size of largest path for better result formatting
    Buffle.Display.outer.set_length(max(files, key=len))

    # renames files to avoid conflict
    temp_files = []  # temporary list of all uuid files
    for file in files:
        temp_name = f"{uuid.uuid4().hex}{os.path.splitext(os.path.basename(file))[1]}"  # creates unique name for file
        temp_path = os.path.join(os.path.dirname(file), temp_name)  # creates a path for the file
        os.rename(os.path.abspath(file), temp_path)
        temp_files.append(temp_path)

    # alters files
    reverse_files = files.copy()
    reverse_files.reverse()
    for temp_file, new_file, original_file in zip(temp_files, reverse_files, files):
        new_file = os.path.join(os.path.dirname(original_file), new_file)
        os.rename(temp_file, new_file)
        Buffle.Display.outer.result(os.path.abspath(original_file), "Reverse Name Shuffle", os.path.basename(new_file), os.path.basename(original_file))
