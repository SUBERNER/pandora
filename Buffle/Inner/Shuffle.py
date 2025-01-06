import os
import random
import re
import uuid
import Buffle


# used to collect and randomize text inside a multiple files
def normal(files: str | list[str], contains: str | list[str], *, weight: int | list[int] | None = None, chance: float = 1, duplicates: bool = False):
    """
    Randomizes and shuffles occurrences of specific substrings across multiple files.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to modify.

        contains (str | list[str]): Substring(s) to search for within the files.

    Keyword Parameter:
        weight (int | list[int] | None): Weight(s) for random selection. Used only if `duplicates` is True.
            - None: Equal weights for all matches.
            - int: Single weight applied to all matches.
            - list[int]: Individual weights for each match.

        chance (float): Probability of altering each match. Defaults to 1.
            - 0.0: No matches are altered.
            - 1.0: All matches are altered.

        duplicates (bool): Whether the same match can be selected multiple times during shuffling. Defaults to False.
    """

    # makes files and contains always a list
    if isinstance(files, str):
        files = [files]
    if isinstance(contains, str):
        contains = [contains]

    # gets size of largest path for better result formatting
    Buffle.Display.inner.set_length(max(files, key=len))

    placeholder = f"{uuid.uuid4().hex}"  # text used as a placeholder for replacing text
    chance_matches = []  # temporary location of all text matching the contains
    if weight:
        chance_weight = []  # Stores weights for randomization
    else:
        chance_weight = None

    # gets data from the fills to be shuffled later
    for entry in files:
        with open(entry, 'r') as file:
            text = file.read()  # stores all the data in a variable

        for contain in contains:
            matches = re.findall(contain, text)  # Find all matches
            for match in matches:
                if chance >= random.random():
                    chance_matches.append(match)
                    if weight is not None:
                        chance_weight.append(weight[0])  # gets the first value from weight
                    text = text.replace(match, placeholder, 1)  # Replace first occurrence of match with placeholder
                else:  # displays file as unaltered as it was ignored do to chance
                    Buffle.Display.inner.result(os.path.abspath(entry), "normal shuffle", os.path.basename(match), os.path.basename(match))
                if weight is not None:
                    weight.pop(0)  # removes first value for next value to get stored in chance_weight

        with open(entry, 'w') as file:  # saves changes to file temporarily
            file.write(text)

    # randomly shuffles data
    if duplicates:  # options can be selected multiple times
        random_matches = random.choices(chance_matches, weights=chance_weight, k=len(chance_matches))
    else:  # normal randomizing of data
        random_matches = chance_matches.copy()
        random.shuffle(random_matches)

    # changes the file data and shuffles text
    for index, entry in enumerate(files):
        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable
        while text.count(placeholder) > 0:
            text = text.replace(placeholder, random_matches[0], 1)
            Buffle.Display.inner.result(files[index], "normal shuffle", random_matches.pop(0), chance_matches.pop(0))

        with open(entry, 'w') as file:
            file.write(text)


# used to collect and randomize text in groups inside a multiple files
def group(files: str | list[str], contains: str | list[str], *, weight: int | list[int] | None = None, chance: float = 1, duplicates: bool = False):
    """
    Groups and randomizes occurrences of specific substrings across multiple files, preserving group structure.

    Parameters:
        files (str | list[str]): Path(s) of the file(s) to modify.

        contains (str | list[str]): Substring(s) to group and shuffle within the files.

    Keyword Parameters:
        weight (int | list[int] | None): Weight(s) for random selection. Used only if `duplicates` is True.
            - None: Equal weights for all groups.
            - int: Single weight applied to all groups.
            - list[int]: Individual weights for each group.

        chance (float): Probability of altering each group. Defaults to 1.
            - 0.0: No groups are altered.
            - 1.0: All groups are altered.

        duplicates (bool): Whether the same group can be selected multiple times during shuffling. Defaults to False.
    """
    # Ensure files and contains are lists
    if isinstance(files, str):
        files = [files]
    if isinstance(contains, str):
        contains = [contains]

    # Set display length for better result formatting
    Buffle.Display.inner.set_length(max(files, key=len))

    placeholder = f"{uuid.uuid4().hex}"  # Unique placeholder for temporary replacements
    chance_groups = []  # Stores groups that will be altered
    if weight:
        chance_weight = []  # Stores weights for randomization
    else:
        chance_weight = None

    # gets data and alters file to prepare for shuffling text
    for entry in files:
        group_matches = [[] for index in contains]  # groups text together to me shuffled together
        valid_group = True  # checks if file should be ignored

        with open(entry, 'r') as file:  # opens file
            text = file.read()  # stores all the data in a variable
            for index, contain in enumerate(contains):
                if len(re.findall(contain, text)) != 0:  # make sure something was found
                    group_matches[index].extend(re.findall(contain, text))  # dumps all finds in an existing group inside the list
                else:
                    valid_group = False
                    break
            if not valid_group:  # if a section in the group is empty, it ignores the rest of the folder
                continue

        # determines sizes of groups and formats of groups, removing unnecessary data
        group_limit = len(min(group_matches, key=len))
        group_matches = [group[:group_limit] for group in group_matches]  # Trim groups to smallest size

        # Create placeholder replacements for all groups
        if chance >= random.random():
            temp_group = []  # Temporary list for placeholder replacements
            for i in range(group_limit):
                for j, match in enumerate(group_matches):
                    temp_group.append([f"{placeholder}<{j}>", match[i]])
                    text = text.replace(match[i], f"{placeholder}<{j}>", 1)  # Replace only the first instance

            # Add the group if selected
            chance_groups.append(temp_group)
            if weight:
                chance_weight.append(weight[0])  # Append the corresponding weight

        else:
            # displays skipped data
            for i in range(group_limit):
                for match in [group[i] for group in group_matches]:
                    Buffle.Display.inner.result(os.path.abspath(entry), "group shuffle", match, match)
                if weight:
                    weight.pop(0)  # Consume weights for skipped groups

        # saves changes made to file to be altered in the future
        with open(entry, 'w') as file:
            file.write(text)

    # shuffles groups
    if duplicates:
        random_groups = random.choices(chance_groups, weights=chance_weight, k=len(chance_groups))
    else:
        random_groups = chance_groups.copy()
        random.shuffle(random_groups)

    # make alterations to files
    for entry in files:
        with open(entry, 'r') as file:
            text = file.read()
            while placeholder in text:
                for index in range(len(random_groups[0])):
                    text = text.replace(random_groups[0][index][0], random_groups[0][index][1], 1)
                    Buffle.Display.inner.result(os.path.abspath(entry), "group shuffle", random_groups[0][index][1], chance_groups[0][index][1])

                # moves on to next groups of data
                random_groups.pop(0)
                chance_groups.pop(0)
                if weight:
                    chance_weight.pop(0)

        # saves changes made to file after shuffle
        with open(entry, 'w') as file:
            file.write(text)










