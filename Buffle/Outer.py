from Buffle import random  # used for seeds
import os
import uuid
import Buffle
from Buffle.Filter import *


def normal(files: str | list[str], *, chance: float = 1, duplicates: bool = False,
           ignores: Ignore | list[Ignore] | None = None, swaps: Swap | list[Swap] | None = None):
    """
    Shuffles and randomizes the names of all files.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to shuffle.

    Keyword Parameter:
        chance (float): Probability of altering each file. Defaults to 1.
            - 0.0: No file is altered.
            - 1.0: All files are altered.

        duplicates (bool): Whether the same file can be selected multiple times during shuffling. Defaults to False.
    """
    try:
        # makes files and filters always a list
        if isinstance(files, str):
            files = [files]
        if isinstance(ignores, Ignore):
            ignores = [ignores]
        if isinstance(swaps, Swap):
            swaps = [swaps]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        temp_files = []  # temporary list of all uuid files
        chance_files = []  # temporary list of all files that will be altered

        # renames files to avoid conflict
        for index, file in enumerate(files):
            if chance >= random.random():
                temp_name = f"{uuid.uuid4().hex}{os.path.splitext(os.path.basename(file))[1]}"  # creates unique name for file
                temp_file = os.path.join(os.path.dirname(file), temp_name)  # creates a path for the file
                os.rename(os.path.abspath(file), temp_file)
                # adds to lists
                chance_files.append(file)
                temp_files.append(temp_file)
            else:  # displays file as unaltered as it was ignored do to chance
                Buffle.Display.outer.result(os.path.abspath(file), "normal", os.path.basename(file), os.path.basename(file))

        # randomly shuffles files
        if duplicates:  # options can be selected multiple times
            random_files = random.choices(chance_files, k=len(chance_files))
        else:  # normal randomizing of files
            random_files = chance_files.copy()
            random.shuffle(random_files)

        # alters files
        for temp_file, new_file, original_file in zip(temp_files, random_files, chance_files):
            os.rename(os.path.abspath(temp_file), os.path.abspath(new_file))
            Buffle.Display.outer.result(os.path.abspath(original_file), "normal", os.path.basename(new_file), os.path.basename(original_file))

    except Exception as e:
        Buffle.Display.image.error_result(files, "normal", str(e.args))


def group(files: str | list[str], contains: str | list[str], *, chance: float = 1, duplicates: bool = False,
          ignores: Ignore | list[Ignore] | None = None, swaps: Swap | list[Swap] | None = None):
    """
    Shuffles and randomizes the specified substrings ('contains') within file names, grouped by similarity.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to shuffle.

        contains (str | list[str]): Substring(s) to search for and shuffle within the file names.

    Keyword Parameter:
        chance (float): Probability of altering each group. Defaults to 1.
            - 0.0: No group is altered.
            - 1.0: All groups are altered.

        duplicates (bool): Whether the same substring can be selected multiple times during shuffling. Defaults to False.
    """
    try:
        # makes files, contains, and filters always a list
        if isinstance(files, str):
            files = [files]
        if isinstance(contains, str):
            contains = [contains]
        if isinstance(ignores, Ignore):
            ignores = [ignores]
        if isinstance(swaps, Swap):
            swaps = [swaps]

        # gets size of largest path for better result formatting
        Buffle.Display.outer.set_length(max(files, key=len))

        temp_names = []  # temporary list of all uuid files
        display_names = files.copy()  # temporary list of all original files
        chance_contains = []  # temporary list of all groups that will be altered

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
            else:  # displays file as unaltered as it was ignored do to chance
                for file in files:
                    if contain in os.path.basename(file):
                        Buffle.Display.outer.result(os.path.abspath(file), "group", os.path.basename(file), os.path.basename(file))

        # randomly shuffles files
        if duplicates:  # options can be selected multiple times
            assign_names = random.choices(chance_contains, k=len(chance_contains))
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
                    Buffle.Display.outer.result(os.path.abspath(display_names[index]), "group", os.path.basename(final_name), os.path.basename(display_names[index]))
    except Exception as e:
        Buffle.Display.image.error_result(files, "group", str(e.args))


def reverse(files: str | list[str], *, chance: float = 1,
    ignores: Ignore | list[Ignore] | None = None, swaps: Swap | list[Swap] | None = None):
    """
    Reverses the order of file names in a directory.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to reverse.

    Keyword Parameter:
        chance (float): Probability of reversing each file. Defaults to 1.
            - 0.0: No file is altered.
            - 1.0: All files are reversed.
    """
    try:
        # makes files and filters always a list
        if isinstance(files, str):
            files = [files]
        if isinstance(ignores, Ignore):
            ignores = [ignores]
        if isinstance(swaps, Swap):
            swaps = [swaps]

        # Sort files in natural order (to ensure consistent reversal)
        files.sort()

        # Check chance condition
        if chance < random.random():
            for file in files:
                Buffle.Display.outer.result(os.path.abspath(file), "reverse", os.path.basename(file), os.path.basename(file))
            return

        # Create a temporary renaming scheme
        temp_files = {}
        for file in files:
            temp_name = f"{uuid.uuid4().hex}{os.path.splitext(file)[1]}"
            temp_path = os.path.join(os.path.dirname(file), temp_name)
            os.rename(file, temp_path)
            temp_files[temp_path] = file  # Store original file mapping

        # Reverse the file order
        reversed_files = list(temp_files.values())[::-1]

        # Rename files back in reversed order
        for temp_file, new_file in zip(temp_files.keys(), reversed_files):
            os.rename(temp_file, new_file)
            Buffle.Display.outer.result(os.path.abspath(new_file), "reverse", os.path.basename(new_file), os.path.basename(temp_file))

    except Exception as e:
        Buffle.Display.image.error_result(files, "reverse", str(e.args))
