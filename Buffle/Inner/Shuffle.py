from Buffle import random  # used for seeds
import os
import re
import uuid
import Buffle


# used to collect and randomize text inside a multiple files
def normal(files: str | list[str], contains: str | list[str], *, weight: int | list[int] | None = None, chance: float = 1, duplicates: bool = False, flags: list[re.RegexFlag] = None):
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

        flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).

        duplicates (bool): Whether the same match can be selected multiple times during shuffling. Defaults to False.
    """
    try:
        # makes files and contains always a list
        if isinstance(files, str):
            files = [files]
        if isinstance(contains, str):
            contains = [contains]

        # Combine selected flags or default to 0 (no flags)
        combined_flags = 0
        if flags:
            combined_flags = sum(flags)

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
                matches = re.findall(contain, text, flags=combined_flags)  # Find all matches
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
    except Exception as e:
        Buffle.Display.image.error_result(files, "normal shuffle", str(e.args))


# used to collect and randomize text in groups inside a multiple files
def group(files: str | list[str], contains: str | list[str], *, weight: int | list[int] | None = None, chance: float = 1, duplicates: bool = False, flags: list[re.RegexFlag] = None):
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

        flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).

        duplicates (bool): Whether the same group can be selected multiple times during shuffling. Defaults to False.
    """
    try:
        # Ensure files and contains are lists
        if isinstance(files, str):
            files = [files]
        if isinstance(contains, str):
            contains = [contains]

        # Combine selected flags or default to 0 (no flags)
        combined_flags = 0
        if flags:
            combined_flags = sum(flags)

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
                    if len(re.findall(contain, text, flags=combined_flags)) != 0:  # make sure something was found
                        matches = re.findall(contain, text, flags=combined_flags)  # finds all text in file
                        if matches:
                            group_matches[index].extend(matches)  # dumps all finds in an existing group inside the list
                    else:
                        valid_group = False
                        break
                if not valid_group:  # if a section in the group is empty, it ignores the rest of the folder
                    continue

            # determines sizes of groups and formats of groups, removing unnecessary data
            group_limit = len(min(group_matches, key=len))
            if group_limit == 0:
                continue  # skips processing if any group is empty

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
                while placeholder in text and random_groups:
                    current_group = random_groups.pop(0)
                    for temp_text, new_text in current_group:
                        if temp_text in text:
                            text = text.replace(temp_text, new_text, 1)
                            Buffle.Display.inner.result(os.path.abspath(entry), "group shuffle", new_text, temp_text)  # FIX THIS

            # saves changes made to file after shuffle
            with open(entry, 'w') as file:
                file.write(text)
    except Exception as e:
        Buffle.Display.image.error_result(files, "group shuffle", str(e.args))


def reverse(files: str | list[str], contains: str | list[str], *, chance: float = 1, flags: list[re.RegexFlag] = None):
    """
    Reverses the order of matching substrings or patterns within file contents.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to process.

        contains (str | list[str]): Substring(s) or pattern(s) to search for in the file(s).
            - Matches found in the file contents will be reversed in order.

    Keyword Parameter:
        chance (float): Probability (0.0 to 1.0) of applying the reversal for each match.
            - 1.0: Always reverse the matches.
            - 0.0: Matches are never reversed.

        flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - re.A: ASCII-only matching.
            - re.I: Ignore case.
            - re.L: Locale dependent.
            - re.M: Multi-line mode.
            - re.S: Dot matches all (dotall).
            - re.U: Unicode matching.
            - re.X: Verbose (allow comments and whitespace).
            - Defaults to None (no flags).
    """
    try:
        # makes files and contains always a list
        if isinstance(files, str):
            files = [files]
        if isinstance(contains, str):
            contains = [contains]

        # Combine selected flags or default to 0 (no flags)
        combined_flags = 0
        if flags:
            combined_flags = sum(flags)

        # gets size of largest path for better result formatting
        Buffle.Display.inner.set_length(max(files, key=len))

        placeholder = f"{uuid.uuid4().hex}"  # text used as a placeholder for replacing text
        chance_matches = []  # temporary location of all text matching the contains
        # gets data from the fills to be shuffled later
        for entry in files:
            with open(entry, 'r') as file:
                text = file.read()  # stores all the data in a variable

            for contain in contains:
                matches = re.findall(contain, text, flags=combined_flags)  # Find all matches
                for match in matches:
                    if chance >= random.random():
                        chance_matches.append(match)
                        text = text.replace(match, placeholder, 1)  # Replace first occurrence of match with placeholder
                    else:  # displays file as unaltered as it was ignored do to chance
                        Buffle.Display.inner.result(os.path.abspath(entry), "reverse shuffle", os.path.basename(match), os.path.basename(match))

            with open(entry, 'w') as file:  # saves changes to file temporarily
                file.write(text)

        # randomly shuffles data
        reverse_matches = chance_matches.copy()
        reverse_matches.reverse()

        # changes the file data and shuffles text
        for index, entry in enumerate(files):
            with open(entry, 'r') as file:  # opens file
                text = file.read()  # stores all the data in a variable
            while text.count(placeholder) > 0:
                text = text.replace(placeholder, reverse_matches[0], 1)
                Buffle.Display.inner.result(files[index], "reverse shuffle", reverse_matches.pop(0), chance_matches.pop(0))

            with open(entry, 'w') as file:
                file.write(text)
    except Exception as e:
        Buffle.Display.image.error_result(files, "reverse shuffle", str(e.args))








