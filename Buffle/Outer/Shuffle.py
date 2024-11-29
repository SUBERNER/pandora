import os
import random
import Buffle
import uuid


# shuffles all file names inside a directory
def normal(files: str | list[str]):
    """
    Shuffles and randomizes the names of all files.
    :param files: Target file's paths
    :type files: str | list[str]
    """
    # makes contains always a list
    if isinstance(files, str):
        files = [files]

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
        Buffle.display_file_results.result(os.path.dirname(original_file), "Normal Name Shuffle", os.path.basename(original_file), os.path.basename(new_file))


# HELL TO EXPLAIN AND CODE (WILL DO LATER)
def group(source: str, contains: list):
    """
    Shuffles and randomizes the 'contains' substrings by groups within file names files in a directory.
    :param source: Target folder's directory
    :param contains: Substrings searched for inside file names
    """
    files = [f for f in os.scandir(source) if f.is_file()]  # stores the actual files
    assign_names = contains.copy()

    temp_names = []  # temporary list of all uuid files
    for contain in contains:
        temp_name = f"{uuid.uuid4().hex}"  # used as a placeholder for the contains text
        temp_names.append(temp_name)
        for file in files:
            if contain in file.name:
                # Replace the substring with the index in the filename
                new_name = file.name.replace(contain, temp_name)
                os.rename(file.path, os.path.join(source, new_name))

    # Refresh the file list to include updated names
    files = [f for f in os.scandir(source) if f.is_file()]

    # alters files
    random.shuffle(assign_names)  # Randomize order for final names
    for i in range(len(contains) - 1, -1, -1):  # Process in reverse order
        target_name = assign_names.pop()  # Select a random name from the list
        contain_name = contains.pop()
        for file in files:
            if temp_names[i] in file.name:
                # Replace the index in the filename with the random target name
                final_name = file.name.replace(temp_names[i], target_name)
                os.rename(file.path, os.path.join(source, final_name))
                Buffle.display_file_results.result(source, "Group Name Shuffle", target_name, contain_name)


# reverses all files inside a directory
def reverse(files: str | list[str]):
    """
    Reverses the order of names of all files from a directory.
    :param files: Target folder's directory
    :type files: str | list[str]
    """
    # makes contains always a list
    if isinstance(files, str):
        files = [files]

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
        Buffle.display_file_results.result(os.path.dirname(original_file), "Reverse Name Shuffle", os.path.basename(original_file), os.path.basename(new_file))
