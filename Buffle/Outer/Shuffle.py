import os
import random
import uuid

import Buffle


def normal(files: str | list[str], *, weight: int | list[int] | None = None, chance: float = 1, duplicates: bool = False):
    """
    Shuffles and randomizes the names of all files.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to shuffle.

    Keyword Parameter:
        weight (int | list[int] | None): Weight(s) for random selection. Used only if `duplicates` is True.
            - None: Equal weights for all files.
            - int: Single weight applied to all files.
            - list[int]: Individual weights for each file.

        chance (float): Probability of altering each file. Defaults to 1.
            - 0.0: No file is altered.
            - 1.0: All files are altered.

        duplicates (bool): Whether the same file can be selected multiple times during shuffling. Defaults to False.
    """

    # makes files always a list
    if isinstance(files, str):
        files = [files]

    # gets size of largest path for better result formatting
    Buffle.Display.outer.set_length(max(files, key=len))

    temp_files = []  # temporary list of all uuid files
    chance_files = []  # temporary list of all files that will be altered
    if weight:
        chance_weight = []  # temporary list of all groups weights that will be altered
    else:
        chance_weight = None

    # renames files to avoid conflict
    for index, file in enumerate(files):
        if chance >= random.random():
            temp_name = f"{uuid.uuid4().hex}{os.path.splitext(os.path.basename(file))[1]}"  # creates unique name for file
            temp_file = os.path.join(os.path.dirname(file), temp_name)  # creates a path for the file
            os.rename(os.path.abspath(file), temp_file)
            # adds to lists
            chance_files.append(file)
            chance_weight.append(weight[index])
            temp_files.append(temp_file)
        else:  # displays file as unaltered as it was ignored do to chance
            Buffle.Display.outer.result(os.path.abspath(file), "normal shuffle", os.path.basename(file), os.path.basename(file))

    # randomly shuffles files
    if duplicates:  # options can be selected multiple times
        random_files = random.choices(chance_files, weights=chance_weight, k=len(chance_files))
    else:  # normal randomizing of files
        random_files = chance_files.copy()
        random.shuffle(random_files)

    # alters files
    for temp_file, new_file, original_file in zip(temp_files, random_files, chance_files):
        os.rename(os.path.abspath(temp_file), os.path.abspath(new_file))
        Buffle.Display.outer.result(os.path.abspath(original_file), "normal shuffle", os.path.basename(new_file), os.path.basename(original_file))


def group(files: str | list[str], contains: str | list[str], *, weight: int | list[int] | None = None, chance: float = 1, duplicates: bool = False):
    """
    Shuffles and randomizes the specified substrings ('contains') within file names, grouped by similarity.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to shuffle.

        contains (str | list[str]): Substring(s) to search for and shuffle within the file names.

    Keyword Parameter:
        weight (int | list[int] | None): Weight(s) for random selection. Used only if `duplicates` is True.
            - None: Equal weights for all groups.
            - int: Single weight applied to all groups.
            - list[int]: Individual weights for each group.

        chance (float): Probability of altering each group. Defaults to 1.
            - 0.0: No group is altered.
            - 1.0: All groups are altered.

        duplicates (bool): Whether the same substring can be selected multiple times during shuffling. Defaults to False.
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]
    if isinstance(contains, str):
        contains = [contains]

    # gets size of largest path for better result formatting
    Buffle.Display.outer.set_length(max(files, key=len))

    temp_names = []  # temporary list of all uuid files
    display_names = files.copy()  # temporary list of all original files
    chance_contains = []  # temporary list of all groups that will be altered
    if weight:
        chance_weight = []  # temporary list of all groups weights that will be altered
    else:
        chance_weight = None

    for index, contain in enumerate(contains):
        if chance >= random.random():
            temp_name = f"{uuid.uuid4().hex}"  # used as a placeholder for the contains text
            temp_names.append(temp_name)
            for i, file in enumerate(files):
                if contain in os.path.basename(file):
                    # Replace the substring with the index in the filename
                    new_name = os.path.basename(file).replace(contain, temp_name)
                    new_file = os.path.join(os.path.dirname(file), new_name)
                    os.rename(file, new_file)
                    files[i] = new_file

            # altered continents and weights after determining chance
            chance_contains.append(contain)
            chance_weight.append(weight[index])
        else:  # displays file as unaltered as it was ignored do to chance
            for file in files:
                if contain in os.path.basename(file):
                    Buffle.Display.outer.result(os.path.abspath(file), "group shuffle", os.path.basename(file), os.path.basename(file))

    # randomly shuffles files
    if duplicates:  # options can be selected multiple times
        assign_names = random.choices(chance_contains, weights=chance_weight, k=len(chance_contains))
    else:  # normal randomizing of files
        assign_names = chance_contains.copy()
        random.shuffle(assign_names)  # Randomize order for final names
    # alters files
    for i in range(len(chance_contains) - 1, -1, -1):  # Process in reverse order
        target_name = assign_names.pop()  # Select a random name from the list
        chance_contains.pop()
        for index, file in enumerate(files):
            if temp_names[i] in os.path.basename(file):
                # Replace the index in the filename with the random target name
                final_name = os.path.basename(file).replace(temp_names[i], target_name)
                os.rename(os.path.abspath(file), os.path.join(os.path.dirname(file), final_name))
                Buffle.Display.outer.result(os.path.abspath(display_names[index]), "group shuffle", os.path.basename(final_name), os.path.basename(display_names[index]))


def reverse(files: str | list[str], *, chance: float = 1):
    """
    Reverses the order of file names in a directory.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to reverse.

    Keyword Parameter:
        chance (float): Probability of reversing each file. Defaults to 1.
            - 0.0: No file is altered.
            - 1.0: All files are reversed.
    """
    # makes files always a list
    if isinstance(files, str):
        files = [files]

    # gets size of largest path for better result formatting
    Buffle.Display.outer.set_length(max(files, key=len))

    temp_files = []  # temporary list of all uuid files
    chance_files = []  # temporary list of all files that will be altered
    # renames files to avoid conflict
    for file in files:
        if chance >= random.random():
            temp_name = f"{uuid.uuid4().hex}{os.path.splitext(os.path.basename(file))[1]}"  # creates unique name for file
            temp_file = os.path.join(os.path.dirname(file), temp_name)  # creates a path for the file
            os.rename(os.path.abspath(file), temp_file)
            # adds to lists
            chance_files.append(file)
            temp_files.append(temp_file)
        else:  # displays file as unaltered as it was ignored do to chance
            Buffle.Display.outer.result(os.path.abspath(file), "reverse shuffle", os.path.basename(file), os.path.basename(file))

    # randomly shuffles files
    reverse_files = chance_files.copy()
    reverse_files.reverse()
    # alters files
    for temp_file, new_file, original_file in zip(temp_files, reverse_files, chance_files):
        new_file = os.path.join(os.path.dirname(original_file), new_file)
        os.rename(temp_file, new_file)
        Buffle.Display.outer.result(os.path.abspath(original_file), "reverse shuffle", os.path.basename(new_file), os.path.basename(original_file))
