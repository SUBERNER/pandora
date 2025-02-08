from Buffle import random  # used for seeds
import os
import re
import uuid
import Buffle
from Buffle.Filter import *


# used to collect and randomize text inside a multiple files
def normal(files: str | list[str], contains: str | list[str], *, chance: float = 1, duplicates: bool = False, replaces_manual: str | list[str] | None = None, replace_auto: bool = False, flags: list[re.RegexFlag] = None,
           ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    """
    Randomizes and shuffles occurrences of specific substrings across multiple files.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to modify.

        contains (str | list[str]): Substring(s) to search for within the files.

    Keyword Parameter:
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
        # makes files, contains, and filters always a list
        if isinstance(files, str):
            files = [files]
        if isinstance(contains, str):
            contains = [contains]
        if isinstance(ignores, Ignore):
            ignores = [ignores]
        if isinstance(excludes, Exclude):
            excludes = [excludes]
        if isinstance(alters, Alter):
            alters = [alters]
        if isinstance(replaces_manual, str):
            replaces_manual = [replaces_manual]

        # combine selected flags or default to 0 (no flags)
        combined_flags = 0
        if flags:
            combined_flags = sum(flags)

        # gets size of largest path for better result formatting
        Buffle.Display.inner.set_length(max(files, key=len))

        placeholder = f"{uuid.uuid4().hex}"  # text used as a placeholder for replacing text
        chance_matches = []  # temporary location of all text matching the contains
        # gets data from the fills to be shuffled later
        for entry in files:
            # checks if a file should be ignored, excluded, or altered:
            if (ignores is None or not any(ignore(entry) for ignore in ignores)) and (excludes is None or not any(exclude(entry) for exclude in excludes)):
                # Apply Alter before reading file
                if alters is not None:
                    for alter in alters:
                        alter(entry)

                with open(entry, 'r') as file:
                    text = file.read()  # stores all the data in a variable

                for contain in contains:
                    matches = re.findall(contain, text, flags=combined_flags)  # Find all matches
                    for match in matches:
                        if isinstance(match, tuple):
                            match = ''.join(match)  # Convert tuple to string
                        if chance >= random.random():
                            chance_matches.append(match)
                            text = text.replace(match, placeholder, 1)  # Replace first occurrence of match with placeholder

                        else:  # displays file as unaltered as it was ignored do to chance
                            Buffle.Display.inner.result(os.path.abspath(entry), "normal", os.path.basename(match), os.path.basename(match))

                with open(entry, 'w') as file:  # saves changes to file temporarily
                    file.write(text)

            # Step 1: Remove duplicates but keep the correct list length
            if replace_auto:
                if replaces_manual is not None:
                    replaces_manual = list(set(replaces_manual))  # Remove duplicates
                else:
                    unique_matches = list(set(chance_matches))  # Remove duplicates
                    if len(unique_matches) < len(chance_matches):
                        chance_matches = random.choices(unique_matches, k=len(chance_matches))  # Fill back to original size
                    else:
                        chance_matches = unique_matches  # If same size, no need to expand

            # Step 2: Shuffle replacements if `replaces_manual` exists
            if replaces_manual is not None:
                random.shuffle(replaces_manual)

            # Step 3: Ensure `random_matches` is always the correct size
            if duplicates:
                if replaces_manual is None:
                    unique_matches = list(set(chance_matches))  # Remove duplicates
                    random_matches = random.choices(unique_matches, k=len(chance_matches))  # Fill back up
                    print(random_matches)
                else:
                    unique_replaces = list(set(replaces_manual))  # Remove duplicates
                    random_matches = random.choices(unique_replaces, k=len(chance_matches))  # Fill to correct size
                    print(random_matches)
            else:
                if replaces_manual is None:
                    random_matches = chance_matches.copy()
                else:
                    random_matches = replaces_manual.copy()
                random.shuffle(random_matches)  # Shuffle for randomness
            random.shuffle(random_matches)

        # changes the file data and shuffles text
        for index, entry in enumerate(files):
            with open(entry, 'r') as file:  # opens file
                text = file.read()  # stores all the data in a variable
            while text.count(placeholder) > 0:
                text = text.replace(placeholder, random_matches[0], 1)
                Buffle.Display.inner.result(files[index], "normal", random_matches.pop(0), chance_matches.pop(0))

            with open(entry, 'w') as file:
                file.write(text)
    except Exception as e:
        Buffle.Display.image.error_result(files, "normal", str(e.args))


# used to collect and randomize text in groups inside a multiple files
def group(files: str | list[str], contains: str | list[str], *, replaces_manual: str | list[str] | None = None, replace_auto: bool = False, chance: float = 1, duplicates: bool = False, flags: list[re.RegexFlag] = None,
          ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
    """
    Groups and randomizes occurrences of specific substrings across multiple files, preserving group structure.

    Parameter:
        files (str | list[str]): Path(s) of the file(s) to modify.

        contains (str | list[str]): Substring(s) to group and shuffle within the files.

    Keyword Parameter:
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
        # Ensure files, contains, and filters are lists
        if isinstance(files, str):
            files = [files]
        if isinstance(contains, str):
            contains = [contains]
        if isinstance(ignores, Ignore):
            ignores = [ignores]
        if isinstance(excludes, Exclude):
            excludes = [excludes]
        if isinstance(alters, Alter):
            alters = [alters]

        # Combine selected flags or default to 0 (no flags)
        combined_flags = 0
        if flags:
            combined_flags = sum(flags)

        # Set display length for better result formatting
        Buffle.Display.inner.set_length(max(files, key=len))

        placeholder = f"{uuid.uuid4().hex}"  # Unique placeholder for temporary replacements
        chance_groups = []  # Stores groups that will be altered

        # gets data and alters file to prepare for shuffling text
        for entry in files:
            # checks if a file should be ignored or excluded:
            if (ignores is None or not any(ignore(entry) for ignore in ignores)) and (excludes is None or not any(exclude(entry) for exclude in excludes)):
                # Apply Alter before reading file
                if alters is not None:
                    for alter in alters:
                        alter(entry)

                group_matches = [[] for index in contains]  # groups text together to me shuffled together
                valid_group = True  # checks if file should be ignored

                with open(entry, 'r') as file:  # opens file
                    text = file.read()  # stores all the data in a variable

                    for index, contain in enumerate(contains):
                        if len(re.findall(contain, text, flags=combined_flags)) != 0:  # make sure something was found
                            matches = re.findall(contain, text, flags=combined_flags)  # finds all text in file
                            if matches:
                                for match in matches:
                                    if isinstance(match, tuple):
                                        match = ''.join(match)
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

                else:
                    # displays skipped data
                    for i in range(group_limit):
                        for match in [group[i] for group in group_matches]:
                            Buffle.Display.inner.result(os.path.abspath(entry), "group", match, match)

                # saves changes made to file to be altered in the future
                with open(entry, 'w') as file:
                    file.write(text)

        # Step 1: Remove duplicates but keep the correct list length
        if replace_auto:
            if replaces_manual is not None:
                replaces_manual = list(set(replaces_manual))  # Remove duplicates
            else:
                unique_groups = list(set(chance_groups))  # Remove duplicates
                if len(unique_groups) < len(chance_groups):
                    chance_groups = random.choices(unique_groups, k=len(chance_groups))  # Fill back to original size
                else:
                    chance_groups = unique_groups  # If same size, no need to expand

        # Step 2: Shuffle replacements if `replaces_manual` exists
        if replaces_manual is not None:
            random.shuffle(replaces_manual)

        # Step 3: Ensure `random_matches` is always the correct size
        if duplicates:
            if replaces_manual is None:
                unique_groups = list(set(chance_groups))  # Remove duplicates
                random_groups = random.choices(unique_groups, k=len(chance_groups))  # Fill back up
                print(random_groups)
            else:
                unique_replaces = list(set(replaces_manual))  # Remove duplicates
                random_groups = random.choices(unique_replaces, k=len(chance_groups))  # Fill to correct size
                print(random_groups)
        else:
            if replaces_manual is None:
                random_groups = chance_groups.copy()
            else:
                random_groups = replaces_manual.copy()
            random.shuffle(random_groups)  # Shuffle for randomness
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
                            Buffle.Display.inner.result(os.path.abspath(entry), "group", new_text, temp_text)  # FIX THIS

            # saves changes made to file after shuffle
            with open(entry, 'w') as file:
                file.write(text)
    except Exception as e:
        Buffle.Display.image.error_result(files, "group", str(e.args))


def reverse(files: str | list[str], contains: str | list[str], *, chance: float = 1, flags: list[re.RegexFlag] = None,
            ignores: Ignore | list[Ignore] | None = None, excludes: Exclude | list[Exclude] | None = None, alters: Alter | list[Alter] | None = None):
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
        # makes files, contains, and filters always a list
        if isinstance(files, str):
            files = [files]
        if isinstance(contains, str):
            contains = [contains]
        if isinstance(ignores, Ignore):
            ignores = [ignores]
        if isinstance(excludes, Exclude):
            excludes = [excludes]
        if isinstance(alters, Alter):
            alters = [alters]

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
            # checks if a file should be ignored, excluded, or altered:
            if (ignores is None or not any(ignore(entry) for ignore in ignores)) and (excludes is None or not any(exclude(entry) for exclude in excludes)):
                # Apply Alter before reading file
                if alters is not None:
                    for alter in alters:
                        alter(entry)

                with open(entry, 'r') as file:
                    text = file.read()  # stores all the data in a variable

                for contain in contains:
                    matches = re.findall(contain, text, flags=combined_flags)  # Find all matches
                    for match in matches:
                        if isinstance(match, tuple):
                            match = ''.join(match)  # Convert tuple to string
                        if chance >= random.random():
                            chance_matches.append(match)
                            text = text.replace(match, placeholder, 1)  # Replace first occurrence of match with placeholder
                        else:  # displays file as unaltered as it was ignored do to chance
                            Buffle.Display.inner.result(os.path.abspath(entry), "reverse", os.path.basename(match), os.path.basename(match))

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
                Buffle.Display.inner.result(files[index], "reverse", reverse_matches.pop(0), chance_matches.pop(0))

            with open(entry, 'w') as file:
                file.write(text)
    except Exception as e:
        Buffle.Display.image.error_result(files, "reverse", str(e.args))


def multiply(files: str | list[str], contains: str | list[str], factor: float | tuple[float, float], *, chance: float = 1, flags: list[re.RegexFlag] = None, allow_zeros: bool = True):
    """
    Modifies numbers found within specified file(s) based on a mathematical operation.

    Parameters:
        files (str | list[str]): Path(s) of the file(s) to process.
        contains (str | list[str]): Substring(s) or pattern(s) to search for in the file(s).
        factor (float | tuple[float, float]):
            - If float: Exact value by which to modify the found numbers.
            - If tuple: A range (min, max) from which a random multiplier will be chosen.

    Keyword Parameters:
        chance (float): Probability (0.0 to 1.0) of applying the operation for each match.
            - 1.0: Always modify the matches.
            - 0.0: Matches are never modified.

        flags (list[re.RegexFlag]): List of `re` module flags to apply during regex matching.
            - Defaults to None (no flags).

        allow_zeros (bool): Whether to allow the result to be zero.
            - True: Zero values are allowed.
            - False: Values that would be zero are set to 1.
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

        for entry in files:
            with open(entry, 'r') as file:
                text = file.read()

            for contain in contains:
                matches = re.findall(contain, text, flags=combined_flags)  # Find all matches
                for match in matches:
                    # Handle tuple matches by joining them into a string
                    if isinstance(match, tuple):
                        match_string = ''.join(match)
                    else:
                        match_string = match

                    # Only proceed if chance condition is met
                    if chance >= random.random():
                        # Find numbers in the match
                        original_numbers = re.findall(r"-?\d+\.?\d*", match_string)

                        new_numbers = []
                        for num in original_numbers:
                            # Determine the factor: exact float or random range
                            if isinstance(factor, tuple):
                                current_factor = random.uniform(factor[0], factor[1])  # Random between range
                            else:
                                current_factor = factor  # Exact value

                            multiplied_value = float(num) * current_factor

                            # Apply the allow_zeros check
                            if not allow_zeros and multiplied_value == 0:
                                multiplied_value = 1

                            # Convert to int if no decimal in original number
                            if '.' in num:
                                new_value = str(multiplied_value)  # Keep as float
                            else:
                                new_value = str(int(round(multiplied_value)))  # Round to nearest int

                            new_numbers.append(new_value)

                        # Replace each original number in the match string
                        new_match_string = match_string
                        for original_number, new_number in zip(original_numbers, new_numbers):
                            new_match_string = new_match_string.replace(original_number, new_number, 1)

                        # Replace the entire match in the text
                        text = text.replace(match_string, new_match_string, 1)

                        # Display the result
                        Buffle.Display.inner.result(
                            os.path.abspath(entry), "multiply", new_match_string, match_string
                        )
                    else:
                        # Display file as unaltered if ignored due to chance
                        Buffle.Display.inner.result(os.path.abspath(entry), "multiply", "None", "None")

            # Save the modified text back to the file
            with open(entry, 'w') as file:
                file.write(text)

    except Exception as e:
        Buffle.Display.image.error_result(files, "multiply", str(e.args))
